#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PedalGuy 跨 repo 路徑驗證器

起因：2026-03-09 Planning 把 development/designs/ 分流為 web/ 與 app/，
兩個產品 repo 的 .claude/ 共 41 處硬編碼路徑沒跟上。8 天後才發現，
期間 4 份文件被寫進廢棄路徑。人工維護索引在這個工作區失敗過一次。

前一版 pre-commit 只檢查絕對路徑，抓不到 README 目錄樹與 repo 簡稱前綴
的相對路徑。2026-09-10 的全庫盤點在那個缺口下找到 20 處失效索引。

三種路徑都檢查：
  1. 絕對路徑        /Users/emilwu/VSCode/PedalGuy/<repo>/...
  2. 前綴相對路徑    `Planning/development/web/designs/`、`Pedal-App/src/`
  3. 目錄樹區塊      ``` 圍起來、有根路徑行、用 ├── └── 的巢狀樹

用法：
  verify-paths.py --staged      只檢查 staged 檔案（pre-commit 用）
  verify-paths.py --all         檢查本 repo 所有受版控檔案
  verify-paths.py --workspace   檢查四個 repo 所有受版控檔案

豁免：
  - 行內寫 path-check:skip     該行不檢查
  - 檔案位於 */reports/、*/archive/、*/archived_versions/  整份不檢查（歷史證據）

離開碼：0 = 全部通過，1 = 有失效路徑，2 = 執行錯誤
"""

import os
import re
import subprocess
import sys

WORKSPACE = "/Users/emilwu/VSCode/PedalGuy"

REPOS = [
    "Pedal-Research",
    "Pedal-Web-Service",
    "Pedal-Web-Service-Planning",
    "Pedal-App",
]

# repo 簡稱 → 實際目錄名。比對時長的優先，避免 Pedal-Web-Service 吃掉
# Pedal-Web-Service-Planning。
REPO_ALIASES = {
    "Pedal-Web-Service-Planning": "Pedal-Web-Service-Planning",
    "Pedal-Web-Service": "Pedal-Web-Service",
    "Pedal-Research": "Pedal-Research",
    "Pedal-App": "Pedal-App",
    "Planning": "Pedal-Web-Service-Planning",
    "Web-Service": "Pedal-Web-Service",
    "Research": "Pedal-Research",
    "App": "Pedal-App",
}
ALIAS_ORDER = sorted(REPO_ALIASES, key=len, reverse=True)

SCAN_EXTENSIONS = {
    ".md", ".json", ".yaml", ".yml", ".ts", ".tsx",
    ".js", ".mjs", ".sh", ".prisma", ".html",
}

SKIP_MARKER = "path-check:skip"

# 歷史證據目錄。裡面記錄的是當時的狀態，路徑可能刻意指向已不存在的東西。
HISTORY_DIR_RE = re.compile(r"(^|/)(reports|archive|archived_versions)/")

# 樣板變數。截到變數所在段落之前的目錄。
TEMPLATE_RE = re.compile(r"[\[<*]|\$\{")

ABS_PATH_RE = re.compile(
    re.escape(WORKSPACE) + r"/[^\s\"'`)\]（），、。]*"
)

BACKTICK_RE = re.compile(r"`([^`\n]+)`")

FENCE_RE = re.compile(r"^\s*(```|~~~)")

# 目錄樹的根路徑行：整行只有一個以 / 結尾的路徑，後面可接註解。
TREE_ROOT_RE = re.compile(r"^([A-Za-z0-9_.][^\s]*/)\s*(#.*)?$")

# 目錄樹的項目行：縮排 + ├──/└── + 名稱。
TREE_ENTRY_RE = re.compile(
    r"^((?:(?:[│|]|\s)\s{3})*)(?:[├└]──|\|--)\s+(.+?)\s*$"
)

# 明顯不是路徑的 token。MIME type、正規表示式片段之類。
NON_PATH_PREFIXES = {
    "http:", "https:", "mailto:", "file:", "git@", "npm:", "node:",
    "application", "text", "image", "audio", "video", "multipart",
}


def run(cmd, cwd=None):
    proc = subprocess.run(
        cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise SystemExit(2)
    return proc.stdout


def is_history_file(rel_path):
    return bool(HISTORY_DIR_RE.search("/" + rel_path))


def has_scan_extension(rel_path):
    return os.path.splitext(rel_path)[1].lower() in SCAN_EXTENSIONS


def truncate_template(path):
    """樣板變數截到它所在段落之前的目錄。app-[module].md → 該檔的目錄。"""
    m = TEMPLATE_RE.search(path)
    if not m:
        return path
    cut = path[: m.start()]
    if "/" not in cut:
        return ""
    return cut.rsplit("/", 1)[0]


# 引用某檔案的某一行時會寫成 path.md:63 或 path.md:892-901。
# 驗證的是檔案本身，行號要先拿掉。
LINE_SUFFIX_RE = re.compile(r":\d+(?:-\d+)?$")


def strip_trailing_punct(path):
    path = path.rstrip(".,;:)）」』】、 ")
    return LINE_SUFFIX_RE.sub("", path)


_BRANCH_CACHE = {}


def branch_names(repo_root):
    """
    分支名稱長得跟目錄路徑一樣（archive/v0.3-commercial-planning）。
    文件裡列分支是正當用途，不該被當成失效路徑。
    """
    if repo_root not in _BRANCH_CACHE:
        proc = subprocess.run(
            ["git", "branch", "--list", "--all", "--format=%(refname:short)"],
            cwd=repo_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        names = set()
        if proc.returncode == 0:
            for line in proc.stdout.splitlines():
                name = line.strip()
                if not name:
                    continue
                names.add(name)
                if name.startswith("origin/"):
                    names.add(name[len("origin/"):])
        _BRANCH_CACHE[repo_root] = names
    return _BRANCH_CACHE[repo_root]


def resolve_alias(candidate):
    """前綴相對路徑 → 絕對路徑。不是前綴相對路徑就回 None。"""
    for alias in ALIAS_ORDER:
        if candidate == alias or candidate.startswith(alias + "/"):
            rest = candidate[len(alias):].lstrip("/")
            return os.path.join(WORKSPACE, REPO_ALIASES[alias], rest)
    return None


def plausible_relative(candidate, repo_root, file_dir):
    """
    repo 內相對路徑。第一段必須在 repo 根目錄或該檔案所在目錄真的存在，
    否則視為不是路徑（過濾 application/json 這類 token）。
    回傳要檢查的絕對路徑清單；空清單代表不是路徑。
    """
    first = candidate.split("/", 1)[0]
    if not first or first in NON_PATH_PREFIXES:
        return []
    bases = []
    if os.path.isdir(os.path.join(repo_root, first)):
        bases.append(repo_root)
    if file_dir != repo_root and os.path.isdir(os.path.join(file_dir, first)):
        bases.append(file_dir)
    return [os.path.join(b, candidate) for b in bases]


def collect_candidates(line, repo_root, file_dir):
    """從一行文字抽出要驗證的 (顯示用字串, 候選絕對路徑清單)。"""
    out = []

    for raw in ABS_PATH_RE.findall(line):
        path = strip_trailing_punct(raw)
        path = truncate_template(path)
        if not path or path.rstrip("/") == WORKSPACE:
            continue
        repo = path[len(WORKSPACE) + 1:].split("/", 1)[0]
        # 目標 repo 沒 clone 就跳過，不要因為環境不完整而擋人。
        if not os.path.isdir(os.path.join(WORKSPACE, repo)):
            continue
        out.append((raw, [path]))

    for raw in BACKTICK_RE.findall(line):
        token = raw.strip()
        if "/" not in token or token.startswith(WORKSPACE):
            continue
        if " " in token or token.startswith("/"):
            continue
        token = strip_trailing_punct(token)
        candidate = truncate_template(token)
        if not candidate:
            continue
        absolute = resolve_alias(candidate)
        if absolute is not None:
            repo = os.path.relpath(absolute, WORKSPACE).split("/", 1)[0]
            if not os.path.isdir(os.path.join(WORKSPACE, repo)):
                continue
            out.append((raw, [absolute]))
            continue
        if candidate in branch_names(repo_root):
            continue
        bases = plausible_relative(candidate, repo_root, file_dir)
        if bases:
            out.append((raw, bases))

    return out


def collect_tree_candidates(lines, repo_root, file_dir):
    """
    解析 ``` 圍起來的目錄樹。第一行必須是可解析的根路徑，
    否則整個區塊跳過。回傳 (行號, 顯示字串, 候選絕對路徑清單)。
    """
    results = []
    in_fence = False
    root = None
    stack = []

    for idx, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            root = None
            stack = []
            continue
        if not in_fence:
            continue
        if SKIP_MARKER in line:
            continue

        stripped = line.rstrip()
        if root is None:
            m = TREE_ROOT_RE.match(stripped)
            if not m:
                continue
            candidate = m.group(1)
            absolute = resolve_alias(candidate.rstrip("/"))
            if absolute is None:
                bases = plausible_relative(candidate.rstrip("/"), repo_root, file_dir)
                absolute = bases[0] if bases else None
            if absolute is None:
                continue
            root = absolute
            stack = []
            continue

        m = TREE_ENTRY_RE.match(stripped)
        if not m:
            continue
        depth = len(m.group(1)) // 4
        name = m.group(2)
        # 樹狀圖的項目名後面常接說明文字。只取第一個空白之前的 token。
        name = name.split()[0] if name.split() else ""
        name = name.rstrip("/")
        if not name or name in (".", ".."):
            continue
        if TEMPLATE_RE.search(name):
            continue
        stack = stack[:depth]
        full = os.path.join(root, *stack, name)
        results.append((idx, os.path.join(*(stack + [name])), [full]))
        stack = stack + [name]

    return results


def check_file(repo_root, rel_path):
    """回傳 [(行號, 顯示字串, 說明)]。"""
    abs_file = os.path.join(repo_root, rel_path)
    if not os.path.isfile(abs_file):
        return []
    if is_history_file(rel_path) or not has_scan_extension(rel_path):
        return []

    file_dir = os.path.dirname(abs_file)
    try:
        with open(abs_file, "r", encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
    except OSError as exc:
        return [(0, rel_path, "無法讀取：%s" % exc)]

    failures = []

    for lineno, line in enumerate(lines, start=1):
        if SKIP_MARKER in line:
            continue
        for shown, candidates in collect_candidates(line, repo_root, file_dir):
            if not any(os.path.exists(c) for c in candidates):
                failures.append((lineno, shown, "路徑不存在"))

    for lineno, shown, candidates in collect_tree_candidates(
        lines, repo_root, file_dir
    ):
        if not any(os.path.exists(c) for c in candidates):
            failures.append((lineno, shown, "目錄樹項目不存在"))

    return failures


def list_files(repo_root, staged):
    if staged:
        out = run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            cwd=repo_root,
        )
    else:
        out = run(["git", "ls-files"], cwd=repo_root)
    return [p for p in out.splitlines() if p]


def check_repo(repo_root, staged):
    failures = []
    for rel in list_files(repo_root, staged):
        for lineno, shown, reason in check_file(repo_root, rel):
            failures.append((repo_root, rel, lineno, shown, reason))
    return failures


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--staged"
    if mode not in ("--staged", "--all", "--workspace"):
        sys.stderr.write(__doc__)
        return 2

    if mode == "--workspace":
        roots = [
            os.path.join(WORKSPACE, r)
            for r in REPOS
            if os.path.isdir(os.path.join(WORKSPACE, r, ".git"))
        ]
        staged = False
    else:
        roots = [run(["git", "rev-parse", "--show-toplevel"]).strip()]
        staged = mode == "--staged"

    failures = []
    for root in roots:
        failures.extend(check_repo(root, staged))

    if not failures:
        return 0

    sys.stderr.write("\n")
    current = None
    for root, rel, lineno, shown, reason in failures:
        label = os.path.relpath(os.path.join(root, rel), WORKSPACE)
        key = (root, rel)
        if key != current:
            sys.stderr.write("  %s\n" % label)
            current = key
        sys.stderr.write("    :%d  %s  →  %s\n" % (lineno, reason, shown))

    sys.stderr.write("\n✗ 發現 %d 處失效路徑。\n" % len(failures))
    if staged:
        sys.stderr.write(
            "\n  commit 已中止。修正路徑後重新 commit，"
            "或用 git commit --no-verify 略過。\n"
            "  想看整個 repo 的狀況：.githooks/verify-paths.py --all\n\n"
        )
    else:
        sys.stderr.write("\n")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
