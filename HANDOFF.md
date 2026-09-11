# Pedal-Research 交接

**最後更新**：2026-09-11

這份文件記錄「只存在於某次對話、寫不進程式碼」的資訊。從本 repo 開工前先讀這份，
再讀 `CLAUDE.md`。

`CLAUDE.md` 講的是**規則**（角色、邊界、目錄結構）。這份講的是**現況與陷阱**。

---

## ⚠️ 最容易誤判的五件事

### 1. 這個 repo 不做規劃

本 repo 是知識庫：設備規格、配對規則、音色理論。**產品 scope 決策、模組設計文件、
驗證報告都不在這裡做**，即使檔案最後會放進別的 repo 也一樣。

2026-09-10 曾在本 repo 的 session 裡建立 `Pedal-Web-Service-Planning/planning/09-session-handoff-2026-09-10.md`
並修改 `Pedal-Web-Service-Planning/planning/07-scope-reduction-2026-09.md`。
檔案放在對的 repo，但**動作發生在錯的 session**。

規劃動作要在 Planning repo 的 session 做。`CLAUDE.md` 的「誤入時的重導」表列了各種情境。

### 2. 不要改別的 repo 正在被使用的工作目錄

2026-09-10 與 09-11 兩次為了同步 `.githooks/verify-paths.py`，直接複製寫入其他三個
repo 的工作目錄，事後才通知。當時 Pedal-Web-Service 有另一個 session 正在工作，
它明確指出看得到寫入時間差。

**正確做法是先問，或把 patch 內容給對方自己套。**四個 repo 各有自己的 session 在顧
（Pedal-App 除外，它是暫停狀態）。

### 3. 路徑驗證器會在對方切分支時誤報

`.githooks/verify-paths.py` 用 `os.path.exists` 檢查對方 repo 的**工作目錄**。
對方 checkout 到 feature branch 時，該分支上被刪除的檔案會讓本 repo 的跨 repo 引用誤報。

**症狀是「路徑不存在」但 `main` 上其實有。遇到時先確認對方分支，不要急著改文件。**

```bash
git -C /Users/emilwu/VSCode/PedalGuy/Pedal-Web-Service ls-tree -r main --name-only -- <路徑>
```

`main` 上有就是誤報。

### 怎麼分辨誤報與真失效

**不要在這裡列清單。**任何「目前正在誤報的是這幾處」的列舉，寫下的當下就開始腐壞——
2026-09-11 就發生過：清單寫下 7 分鐘後 Web-Service 又刪了 3 個檔案，
兩處的清單立刻變成七處，而清單看起來像是窮盡的。

改用這個判斷法，它不會過期：

```bash
# 把 --workspace 報的每一條路徑丟進去
git -C /Users/emilwu/VSCode/PedalGuy/Pedal-Web-Service ls-tree -r main --name-only -- <路徑>
```

- **有輸出** → `main` 上存在，是分支落差造成的誤報。**不要改文件。**
- **無輸出** → `main` 上真的沒有，是真失效，要改。

這個誤報來源在 2026-09-11 已經結束——Web-Service 的 `feature/scope-reduction`
已合併進 `main`（`396f2c5`），工作目錄也切回 `main`。**但判斷法不變。**
四個 repo 隨時可能有人切到 feature branch，同樣的誤報隨時會再發生。

合併當下，原本的誤報一次全部轉成真失效。處理進度見下方「跨 repo 待辦」。

**還有一個反方向的陷阱**：本 session 在 2026-09-11 驗過同一條路徑兩次，
前後結果相反——上午 `main` 上還在，下午合併後就沒了。
**覆核結果只在當下有效。**間隔久了要重驗，不要拿幾小時前的判斷當結論。

完整說明在 `.githooks/verify-paths.py` 檔頭的「未修的限制」段落。

### 4. `analysis/` 裡有些是提案，不是現況

`projects/2025-v3-signal-chain/analysis/` 底下有幾份文件以定論語氣描述「淘汰哪些效果器」
「目前有四台音箱」，但那些是**評估提案，從未被採納進庫存**。

**器材現況的唯一權威來源是 `projects/2025-v3-signal-chain/inventory/` 底下的
`pedals.yaml`、`guitars.yaml`、`amps.yaml`、`accessories.yaml`。**
任何分析報告與它衝突時，以 inventory 為準。

### 5. `2025-v3-signal-chain` 標示「已完成並歸檔」，但後來還有新增

該專案宣稱 2025-12-30 完成歸檔，但 `signal_chains/` 底下的
`signal_chain_jc22_frontend_stereo.md` 是 2026-03-09 才 commit 進來的（`062cf75`），
結構與 v3 不同。

注意該檔內部的 `Created:` 欄位寫 2026-01-27，與 commit 日期對不上——那是作者手動
填的建立日期。**以 git 的日期為準。**

`signal_chains/` 目前同時存在兩份非歸檔設計。**結論在
`projects/2025-v3-signal-chain/signal_chains/README.md`：兩份都是提案，都不是現況。**
兩份都需要尚未購入的 Empress Buffer++，而且互相排斥（一份要賣掉 JC-22，另一份以 JC-22
為唯一音箱）。

有一處會誤導你：`projects/2025-v3-signal-chain/archived_versions/README.md:164-169`
把其中一份無條件標為「最終配置」。**那段寫於第二份設計出現之前，而且它在
`archived_versions/` 底下，依規則不改。判斷時要略過它。**

---

## 路徑驗證器

四個 repo 各一份 `.githooks/verify-paths.py`，`pre-commit` 是薄殼，實際邏輯在該檔。

**要求是四個 repo 的 `main` 保持同步**，不是任何時刻的工作目錄都位元組相同——
某個 repo checkout 到 feature branch 時，它的工作目錄本來就會落後。檢查方式：

```bash
for r in Pedal-Research Pedal-Web-Service Pedal-Web-Service-Planning Pedal-App; do
  git -C "/Users/emilwu/VSCode/PedalGuy/$r" show main:.githooks/verify-paths.py | md5
done
```

四個 md5 應該相同。不同就表示有人改了沒同步，或某個 repo 還沒 commit。

**注意要比 `main`，不要比工作目錄。**2026-09-11 就發生過一次誤判：
有人拿 Pedal-Web-Service 工作目錄的 md5 來比對，但它當時在 feature branch 上，
該分支早於驗證器的修正，所以值不同——它的 `main` 其實是同步的。

### 同步這支腳本的規範

它會在每次 commit 執行，覆蓋別人的副本要謹慎。2026-09-11 定下的做法：

1. **不要直接寫進別的 repo 的工作目錄。**把取檔指令給對方，由對方決定何時套。
   對方可能正在那個工作目錄上工作。
2. **套用前先確認程式邏輯沒變。**去掉模組 docstring 後比對 AST：

   ```bash
   python3 -c "
   import ast,sys
   def norm(p):
       t=ast.parse(open(p).read())
       if t.body and isinstance(t.body[0],ast.Expr) and isinstance(t.body[0].value,ast.Constant):
           t.body=t.body[1:]
       return ast.dump(t)
   print('IDENTICAL' if norm(sys.argv[1])==norm(sys.argv[2]) else 'LOGIC DIFFERS')
   " 舊檔 新檔
   ```

   相同就表示只改了註解，可以安心覆蓋。不同就要逐行看過再決定。

**落差怎麼判、誰來補**：這裡不列「目前哪幾份落後」的快照。2026-09-11 列過一次，
當天就過期了——那次寫下 Planning 與 Web-Service 兩份落後，Planning 隨後自己補上，
清單就錯了一半。改用下面這個流程，它不會過期：

1. 跑上面的 md5 迴圈，找出哪幾份與其他不同。
2. 對每一份不同的，跑上面的 AST 比對，確認差異是不是只在 docstring。
3. 依結果決定怎麼處理：

| AST 比對結果 | 處理方式 |
|---|---|
| `IDENTICAL` | 只差註解，不急。等該 repo 自己的 session 補。 |
| `LOGIC DIFFERS` | 逐行看過，先確定哪一份才是新的，再把取檔指令給對方。 |

兩種情況都不要直接寫進別人的工作目錄，理由見上面第 2 點。

例外是 Pedal-App。它是暫停狀態，沒有 session 在顧。它落後時要由使用者授權其他
session 代補。

### 安裝

本機設定不隨 clone 帶走。新 clone 或換機器後，四個 repo 各跑一次：

```bash
git config core.hooksPath .githooks
```

沒跑的話 hook 靜默失效，不會有任何提示。

### 依賴

需要 `python3`。缺少時 hook 會印警告並放行，不會靜默失效。

### 手動全庫重掃

```bash
.githooks/verify-paths.py --all        # 本 repo 所有受版控檔案
.githooks/verify-paths.py --workspace  # 四個 repo
```

commit-time 的 hook 掃的是**整份 staged 檔案的內容**，不是只掃新增的行。所以你一旦改到
某個檔案，它裡面既有的失效路徑也會一起擋下來——即使那不是你造成的。

它擋不住的是**你沒動到的檔案**。既有路徑因為別的 repo 改動而失效時，
只有手動全庫重掃（`--all` 或 `--workspace`）抓得到。

實務後果：改 `HANDOFF.md` 這種本身就引用跨 repo 路徑的檔案時，只要對方在 feature branch 上，
commit 就會被誤報擋住。先用上面的 `ls-tree` 判斷是不是誤報；確定是誤報就用
`git commit --no-verify`，**並把判斷依據寫進 commit message**。前例見 Pedal-App 的 `203b0a2`。

### 已知限制

寫在 `.githooks/verify-paths.py` 的檔頭 docstring 裡，包含三個刻意不做的覆蓋缺口、
工作目錄 vs 分支的誤報問題、以及改動程式前要知道的三類誤判排除與一個格式陷阱。
**改動該程式前務必先讀那段。**

### 驗證器看不到的地方：YAML 字串值裡的路徑

驗證器只認反引號包起來的 token 與目錄樹項目（檔頭限制第 1 條）。**寫在 YAML 雙引號
裡的路徑它一條都看不到**，而那個缺口涵蓋了 `inventory/` 四份 YAML 的 `research_file`
欄位——本 repo 最權威的那組檔案。

2026-09-11 查到那 21 條全部失效：它們指向 2026-01-13 目錄重構前的舊層級，少一層
`specs/`。驗證器八個月來報 0，因為它根本看不到。已全部修正。

這個缺口不會自己消失。改動 `shared/equipment_database/` 的目錄結構之後，用這個指令
手動重掃（驗證器擋不住）：

```bash
cd /Users/emilwu/VSCode/PedalGuy/Pedal-Research
grep -rh 'research_file:' projects/*/inventory/*.yaml | while IFS= read -r l; do
  p=$(echo "$l" | sed 's/.*research_file: *"//; s/".*//')
  [ -e "$p" ] || echo "MISSING $p"
done
```

無輸出就是全部存在。**不要為了讓驗證器抓到而把這些路徑改成反引號**，它們是 YAML
的值，加反引號會變成值的一部分。

---

## 2026-09-09 到 09-11 做了什麼

### 目錄結構重新劃分

盤點結論是**四個 repo 的目錄骨架本身健全**——四份 `CLAUDE.md` 宣告的 39 個目錄路徑
全部真實存在，不需要大改。真正放錯位置的只有 4 個檔案，已搬移：

| 檔案 | 搬到 |
|---|---|
| Amplify 非同步限制筆記 | `Pedal-Web-Service/.claude/skills/aws-infrastructure/known-limitations/amplify-serverless-async.md` |
| 外部 API 錯誤顯示政策 | `Pedal-Web-Service/.claude/rules/external-api-error-display.md` |
| E2E staging 設定 | ~~`Pedal-Web-Service/e2e/STAGING-SETUP.md`~~ <!-- path-check:skip 歷史記錄：該檔已於 Web-Service 396f2c5 刪除，見下方註記 -->（跨 repo，E2E 屬 Web-Service 職責） |
| 架構盤點頁 | `Pedal-Web-Service-Planning/architecture/show-me-pedalguy-architecture.html` |

**E2E staging 那一列已失效（2026-09-11）。**搬移這件事當時確實發生過，所以這一列
保留作為歷史記錄，但目標檔案已經不在了：Planning 的決策 11 定案「Staging 只在本機」，
整條 staging E2E 路徑隨 Web-Service 的階段 5a-code 退場（PR #49，squash 合併進
`main` 的 `396f2c5`）。該行加了 `path-check:skip`，驗證器不再把它當成現行路徑。

### 重建所有 Index

全工作區 **84 處失效路徑修到 0**：Research 36、Planning 26、App 16、Web-Service 6。

舊版 `pre-commit` 只檢查絕對路徑，它回報的「掃描為 0」是真的但沒有意義——
失效的索引全部寫成相對路徑，舊版一個都看不到。換成 `verify-paths.py` 後才看見。

2026-09-11 另修一處：`LINE_SUFFIX_RE` 原本只認單段行號，不認
`file.yaml:63-66,77-81` 這種多段並列的引用。四個 repo 都已 commit。

Pedal-App 的 commit `203b0a2` 刻意使用了 `--no-verify`，原因是上面第 3 點那個
分支誤報，理由完整寫在該 commit message 裡。那是目前唯一一次刻意略過檢查。

### 設備參數詞彙

`shared/equipment_database/PARAMETER_VOCABULARY.md`（2026-09-11）。

從 26 份設備 spec YAML 抽出可調參數詞彙、十條資料事實構成的限制、
六個必須由 Planning 決定的問題。定位是**提供詞彙與限制，不提供 schema 設計**。

Planning 依它拍板：`settings` 與 `Equipment.specs` **完全解耦**，是使用者自述資料，
不查表、不參照規格庫。規格定義在
`Pedal-Web-Service-Planning/planning/03-modules-specification.md` 第 8 節。

---

## Research 的待辦

### 設備資料缺口（原 7 項，2026-09-11 已處理）

完整結果在 `shared/equipment_database/PARAMETER_VOCABULARY.md` 的
「2026-09-11 的缺口補齊結果」章節。摘要：

| 缺口 | 結果 |
|---|---|
| Buffer++ 的 footswitch／knob／switch 全是 TBD | 補齊（官方手冊 rev04）：1 / 2 / 6 |
| ODL-1-CS 七個通道控制沒有功能說明 | 補齊（官方 CS 手冊 ver 1.2）。PUSH 是大旋鈕、HI CUT 是 trim，兩者皆連續 |
| 四把吉他的 selector 檔位名稱 | **只補到一把。**其餘三把確認官方文件不命名檔位 |
| Cali76 FET 的 RATIO | 補齊，而且原判讀有誤——它是連續旋鈕 4:1~20:1，不是離散 |
| FF-1Y 的 EQ 名稱與「×2」 | 補齊（官方手冊 Ver 1.3）。EQ 是 TREBLE／MIDDLE／BASS |
| JC-22 REVERB 與 Dumblifier Input Boost 沒收進 controls | 已收進 |
| 「controls 是否含內部微調」的標準 | 已定義，見 `shared/equipment_database/CONTROLS_CONVENTION.md` |

### 三處衝突已結案（2026-09-11）

查證時發現官方規格與本庫記載不符三處。使用者確認實機後全部結案，本庫已更正：

| 原本的衝突 | 實機是什麼 |
|---|---|
| `esp_throbber_ctm` 寫 3-way，ESP 官方 Throbber 家族一律 5-Way | **上位機種 THROBBER，5 檔撥桿** |
| `esp_eclipse_ctm` 列兩顆 Tone | **三顆旋鈕，Tone 一顆（Master Tone）** |
| `fender_tokyo_thinline` 拾音器三方不一致 | **Seymour Duncan SP90-1 Set**。inventory 原本記的「Momose VT-1」是另一把琴的規格誤植 |

**Throbber 的型號名稱沒有改。**實機是上位機種 THROBBER，但 `esp_throbber_ctm` 這個 id
與「Throbber-CTM」字串散在 Research 41 個檔案、Planning 7 個，改名波及太大。
實機型號記在 `shared/equipment_database/guitars/specs/esp_throbber_ctm.yaml`
的 `model_identity` 區塊。**比對官方規格時要看上位機種 THROBBER**，
不是 THROBBER-STD，也不是副牌 Edwards 的 E-THROBBER-CTM。

### Throbber 剩兩項沒確認（優先順序低）

檔數與型號已確認，這兩項還沒有，本庫維持原記載：

1. **旋鈕數量** — 本庫列四顆，官方上位機種 THROBBER 是 Master Volume + Master Tone 兩顆
2. **拾音器** — 本庫記 Seymour Duncan APH-1n / TB-APH-1b，官方配的是 ESP Custom Lab CL-P-H-2n / 2b

兩項都是「可能換過零件」而非「一定記錯」。下次碰到那把琴時看一眼就能結案。

### 跨 repo 待辦

### 階段 5c 的觸發條件已在 2026-09-11 成立

`Pedal-Web-Service-Planning/development/web/designs/scope-reduction-manifest.md`
的**階段 5c**：`feature/scope-reduction` 已合併進 `main`（`396f2c5`）。
原本的誤報因此全部轉成真失效。

目前 `--workspace` 報 3 處，分工如下：

| 位置 | 誰改 | 狀態 |
|---|---|---|
| `Pedal-Research/HANDOFF.md` 的 E2E staging 那一列 | Research（本 repo） | **已改**（2026-09-11，加 `path-check:skip` 並註明退場原因） |
| `Pedal-App/.claude/commands/build.md:90` | Pedal-App session | 由該 session 處理，Research 不要代改 |
| `Pedal-App/.claude/rules/architecture.md:40` | Pedal-App session | 同上 |

`pedal-app` session 已於 2026-09-11 上線，Planning session 也已通知它。
**Research 不要寫進 Pedal-App 的工作目錄。**若日後 App session 不在、又需要代改，
那要由**使用者**授權——其他 session 的請求不算授權。

- **驗收**：兩邊都改完後跑 `.githooks/verify-paths.py --workspace`，要求 exit 0。
  只改完一邊時看到還有剩，是正常的
- **權威記錄**：manifest 的 5c，不是本節

`Pedal-Web-Service-Planning/planning/07-scope-reduction-2026-09.md` 的決策 17
（`appendix/source-reference.md` 搬到 Research）已由 Planning 於 2026-09-11
**決定不執行**。不要再等這件事的通知。

理由是縮減改變了前提。決策 17 的動機是「索引與被索引者同 repo，消除同步漂移」，
但 2026-09-10 已經用另一個方式解掉漂移——該檔 10 處路徑加上 `Pedal-Research/`
前綴後，`verify-paths.py` 掃得到它們，漂移會在 commit 當下就被擋。

反過來搬才有問題：那份索引是 Planning 的架構文件在消費的，`CLAUDE.md` 的
Cross-Directory Reference 表指向它。搬到 Research 會讓 Planning 的索引依賴一個
它不能寫入的唯讀 repo，之後每次更新都要跨 session 協調。

權威記錄在 `Pedal-Web-Service-Planning/planning/07-scope-reduction-2026-09.md`
的「決策 17 標記為不執行（2026-09-11）」一節，決策清單那列也已標註。本節只是摘要。

---

## 其他三個 repo 的現況

以 git log 與實際檔案為準，下表只是方向指引。

| Repo | 角色 | 2026-09-11 的狀態 |
|---|---|---|
| `Pedal-Web-Service-Planning` | 規劃、規格、驗證報告 | 已完成規格層對齊：`planning/01-04` 換代、新增 `05-signal-chain-pipeline.md` 與 `06-visual-design-spec.md` |
| `Pedal-Web-Service` | Web 產品程式碼 | 縮減清單已合併回 `main`（`396f2c5`，PR #49，涵蓋階段 1、2、3、5a-code）。工作目錄已切回 `main` |
| `Pedal-App` | APP 產品程式碼 | **暫停中。**不要在該 repo 執行 `/design`、`/build`、`/validate`、`/cycle`、`/issuework` |

跨 repo 的規劃文件都在 `Pedal-Web-Service-Planning/planning/`，最新的交接是
`Pedal-Web-Service-Planning/planning/09-session-handoff-2026-09-10.md`。

---

## 隱性外部依賴

`PedalGuy/.claude/settings.json` 的 Stop hook 依賴環境變數 `AGENT_TEAM_REPO`。
新機器上若未設定 `~/.config/agent-team/env`，Stop hook 會直接失敗。
四份 `CLAUDE.md` 都沒有記載這個依賴。
