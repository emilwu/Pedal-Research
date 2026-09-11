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

Scope 縮減執行期間（Web-Service 停在 `feature/scope-reduction`），
誤報數量會隨它的進度**持續增加**。看到 `--workspace` 報一串失效是常態，
不代表索引壞了。逐條套上面那個指令判斷。

合併之後誤報會一次全部轉成真失效，處理方式見下方「跨 repo 待辦」。

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

`signal_chains/` 目前同時存在兩份非歸檔設計，本 repo 的文件沒有說哪一份是最終版。
詳見 `projects/2025-v3-signal-chain/README.md`。

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

**2026-09-11 的已知落差**：本檔的 docstring（已知限制、誤判來源那幾段）
只同步到 Pedal-Research 與 Pedal-App。Pedal-Web-Service-Planning 與
Pedal-Web-Service 兩份還是舊 docstring，程式邏輯相同、只差註解。
兩邊各有自己的 session 在顧，等它們同步。

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

commit-time 的 hook 只擋「新增的」失效路徑，擋不住「既有路徑因為別的 repo 改動而失效」。
後者只有手動全庫重掃抓得到。

### 已知限制

寫在 `.githooks/verify-paths.py` 的檔頭 docstring 裡，包含三個刻意不做的覆蓋缺口、
工作目錄 vs 分支的誤報問題、以及改動程式前要知道的三類誤判排除與一個格式陷阱。
**改動該程式前務必先讀那段。**

---

## 2026-09-09 到 09-11 做了什麼

### 目錄結構重新劃分

盤點結論是**四個 repo 的目錄骨架本身健全**——四份 `CLAUDE.md` 宣告的 39 個目錄路徑
全部真實存在，不需要大改。真正放錯位置的只有 4 個檔案，已搬移：

| 檔案 | 搬到 |
|---|---|
| Amplify 非同步限制筆記 | `Pedal-Web-Service/.claude/skills/aws-infrastructure/known-limitations/amplify-serverless-async.md` |
| 外部 API 錯誤顯示政策 | `Pedal-Web-Service/.claude/rules/external-api-error-display.md` |
| E2E staging 設定 | `Pedal-Web-Service/e2e/STAGING-SETUP.md`（跨 repo，E2E 屬 Web-Service 職責） |
| 架構盤點頁 | `Pedal-Web-Service-Planning/architecture/show-me-pedalguy-architecture.html` |

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

### 設備資料缺口（7 項）

完整清單在 `shared/equipment_database/PARAMETER_VOCABULARY.md` 的
「Research 這邊自己該補的資料缺口」章節。摘要：

1. `empress_buffer_plus_plus` 的控制項數量與功能全是 TBD
2. `odl1cs` 的 7 個通道控制沒有任何功能說明，`PUSH` 與 `HI CUT` 功能不明
3. 四把吉他的 pickup selector 都沒寫出三個檔位的實際名稱
4. `cali76_fet` 的 RATIO 宣告是離散但沒給檔位
5. `ff1y` 的 EQ (3-band) 未列出個別旋鈕名稱
6. `roland_jc22` 的 REVERB 旋鈕與 `dsm_dumblifier` 的 Input Boost switch 沒收進各自的 controls 區塊
7. 「controls 是否包含內部微調項」這條標準沒有在資料庫層級明文定義

**這 7 項的優先順序已降級。** 因為 `settings` 與規格庫解耦，它們不再擋住任何功能，
只影響 `/gear/[id]` 的規格顯示——而規格缺漏在那裡會誠實顯示為「無資料」，不猜測。

### 跨 repo 待辦

### 有一項排程中，觸發條件是「Web-Service 合併」

`Pedal-Web-Service-Planning/development/web/designs/scope-reduction-manifest.md`
的**階段 5c**：`feature/scope-reduction` 合併進 `main` 之後，上面第 3 點那兩處
Pedal-App 引用會從誤報變成真失效，要改。

- **誰改**：Pedal-App session。若當時沒有 App session，由使用者授權其他 session 代改
  ——**可能會是 Research**，所以記在這裡
- **驗收**：合併後跑 `.githooks/verify-paths.py --workspace`，要求 exit 0
- **權威記錄**：manifest 的 5c，不是本節

**合併之前不要動那兩處。**現在改會讓 Pedal-App 的文件提前偏離 `main`，
變成另一個方向的 BIAS。

除此之外沒有等 Research 動手的跨 repo 待辦。

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
| `Pedal-Web-Service` | Web 產品程式碼 | 在 `feature/scope-reduction` 分支執行縮減清單 |
| `Pedal-App` | APP 產品程式碼 | **暫停中。**不要在該 repo 執行 `/design`、`/build`、`/validate`、`/cycle`、`/issuework` |

跨 repo 的規劃文件都在 `Pedal-Web-Service-Planning/planning/`，最新的交接是
`Pedal-Web-Service-Planning/planning/09-session-handoff-2026-09-10.md`。

---

## 隱性外部依賴

`PedalGuy/.claude/settings.json` 的 Stop hook 依賴環境變數 `AGENT_TEAM_REPO`。
新機器上若未設定 `~/.config/agent-team/env`，Stop hook 會直接失敗。
四份 `CLAUDE.md` 都沒有記載這個依賴。
