# Pedal Research — Knowledge Base

**角色**：知識庫 — 設備資料、配對規則、音色理論（唯讀參考）

本目錄是 Pedal Web Service 的參考知識來源，包含設備技術規格、配對邏輯規則和音色理論。其他目錄的 Agent **僅可讀取，不可寫入**本目錄。

---

## 四目錄架構

| 目錄 | 角色 | 路徑 |
|------|------|------|
| **Planning** | 專案管理：規劃、設計、驗證、部署 | `/Users/emilwu/VSCode/PedalGuy/Pedal-Web-Service-Planning/` |
| **Research（本目錄）** | 知識庫：設備資料、配對規則、音色理論（唯讀） | `/Users/emilwu/VSCode/PedalGuy/Pedal-Research/` |
| **Web-Service** | Web 產品程式碼 + Agent：Next.js + Lambda | `/Users/emilwu/VSCode/PedalGuy/Pedal-Web-Service/` |
| **App** | APP 產品程式碼 + Agent：React Native + Expo | `/Users/emilwu/VSCode/PedalGuy/Pedal-App/` |

---

## Repo 邊界

### 本 repo 負責

- 研究並記錄效果器/吉他/音箱/線材的技術規格（YAML）
- 撰寫設備深度研究報告（MD，含網路驗證資訊）
- 定義吉他-效果器配對規則本體與音色理論（pairing_rules.yaml、tone_theory/）
- 建立與維護訊號鏈配置方案（4-Cable Method、阻抗/緩衝分析）
- 管理動態設備 Inventory（新增/移除/更新，含歸檔）
- 執行設備功能重疊檢測與優化建議
- 規劃設備升級時程、購物清單與 Pedalboard 佈局（implementation-planner skill）
- 產出設備實際使用範例文件
- 維護專案化訊號鏈研究歷史（projects/ 下各專案）

### 本 repo 不負責

- 產品規格、模組設計文件、驗證報告、部署腳本 → 屬 Pedal-Web-Service-Planning
- Web 前端/後端程式碼與其 L2 agent 系統 → 屬 Pedal-Web-Service
- APP 程式碼與其 L2 agent 系統（目前暫停） → 屬 Pedal-App
- 把配對規則轉譯成 AI prompt 模板的工程實作（屬 Pedal-Web-Service 的 ai-integrator/pairing-engine，只能轉譯格式不能改規則本體） → 屬 Pedal-Web-Service
- 會員機制、商業計劃相關內容（已定案暫停） → 不屬於任何 repo 現行職責

### 誤入時的重導

如果使用者在本 repo 要求以下任務，不要執行。回覆說明該任務屬於哪個 repo，並告訴他切換過去後要用哪個指令。

| 使用者可能會說的話 | 正確的 repo | 切換後怎麼做 |
|---|---|---|
| 寫某個 Web 模組的技術設計文件 | Pedal-Web-Service-Planning | 在 Pedal-Web-Service 執行 /design [module]，architect agent 讀取 Planning 規格後寫入 Planning/development/web/designs/ |
| 跑某個模組的 GO/NO-GO 驗證報告 | Pedal-Web-Service-Planning | 在 Pedal-Web-Service 執行 /validate [module]，validator agent 寫入 Planning/development/web/reports/ |
| 討論或更新產品 scope、要不要做某個功能 | Pedal-Web-Service-Planning | 更新 planning/ 下的規格文件（Source of Truth），比照 07-scope-reduction-2026-09.md 的模式留下變更紀錄 |
| 建立 AWS infra 資源或寫 IAM policy | Pedal-Web-Service-Planning | 寫入 scripts/aws/ 的部署 shell script 或 IAM policy JSON |
| 產生設備遷移 SQL 把新資料匯入資料庫 | Pedal-Web-Service-Planning | 在 Pedal-Web-Service 執行 /migrate-data，data-migrator agent 讀取 Pedal-Research 的設備 YAML/MD 產生 idempotent SQL，成品寫入並保管在 Planning/scripts/migrations/ |
| 改網站前端頁面/元件樣式（例如登入頁） | Pedal-Web-Service | 用 /build frontend [module]，改 src/app、src/components 對應頁面/元件 |
| 加一個網站 API 端點 | Pedal-Web-Service | 用 /build backend [module]，在 src/app/api 新增 route 並更新 Prisma schema/migrations |
| 同步 production 和 staging 的設備資料 | Pedal-Web-Service | 用 repo 內 scripts/ 下依賴 Prisma client 的 prod↔staging 資料同步腳本 |
| 跑或新增 Playwright E2E 測試案例 | Pedal-Web-Service | 用 /e2e run\|add\|report，在 e2e/ 下新增或執行對應 spec |
| 產生給 Claude API 用的配對 prompt 模板 | Pedal-Web-Service | 用 /ai-prompt [feature]，ai-integrator agent 讀取配對知識庫的唯讀複本產出 condensed/full 版 TypeScript 模板 |
| 改 App 的畫面或元件（螢幕、UI） | Pedal-App | 確認 README 記載的暫停狀態已解除後，用 /build app [module] 改 src/screens、src/components |
| 調整行動端 Bearer token 認證/過期規則 | Pedal-App | 編輯 .claude/rules/business-rules.md 中的客戶端規則（Bearer token、SecureStore）；若涉及後端驗證邏輯本身要改到 Pedal-Web-Service |
| 查 App 端顯示的 API contract 是不是跟後端不一致 | Pedal-Web-Service | 後端路由本身是權威來源；App 的 app-context/api-reference.md 只是唯讀快照，落差以 Pedal-Web-Service 程式碼為準並回頭校正 App 端文件 |
| 依 GitHub issue 的 label 自動執行對應開發流程 | Pedal-Web-Service | 在 issue 所屬的產品 repo（Pedal-Web-Service，或恢復開發後的 Pedal-App）執行 /issuework [issue-number]，依 label 自動路由 pipeline |

### 跨 repo 讀寫規則

- Pedal-Research 對外唯讀：Planning、Web-Service、App 只能讀取 shared/、.claude/knowledge/ 內容，不得寫入或修改 Pedal-Research 的任何檔案。
- Web-Service、App 若需要 Pedal-Research 的配對規則/知識，只能在自己 repo 內建立唯讀複本（如 pedal-context/），不可回寫來源，也不可在複本裡新增規則本體。
- 四個 repo 都不得撰寫或保留會員機制、商業計劃相關內容——已定案暫停，不屬於任何 repo 現行職責。

---

## 本目錄結構

| 路徑 | 用途 |
|------|------|
| `shared/equipment_database/` | 設備技術規格（效果器、吉他、音箱、線材） |
| `shared/tone_theory/` | 音色理論、信號鏈原理 |
| `.claude/knowledge/` | 配對規則 YAML、信號鏈基礎 |
| `.claude/skills/` | L1 研究用 agent 技能 |
| `.claude/agents/` | L1 研究用 agent 本體（0/1/2 號） |
| `analysis/` | 設備分析報告 |
| `projects/` | 專案特定配對設定 |
| `projects/2025-v3-signal-chain/inventory/` | 動態設備清單實際位置（吉他/效果器/音箱/配件） |
| `reference_docs/` | 通用參考文件（PDF、評估框架） |
| `.githooks/` | pre-commit、跨 repo 路徑驗證器 |

---

## 硬性規則

**本目錄是唯讀的。** Web-Service 的 Agent（architect、frontend-builder、backend-builder、ai-integrator、validator、data-migrator）與 App 的 Agent（architect、app-builder、api-builder、validator）不得寫入本目錄。

本目錄的資料被以下方式引用：
- `data-migrator` agent 讀取 `shared/equipment_database/` 產生遷移腳本
- `ai-integrator` agent 讀取 `.claude/knowledge/` 產生 prompt 模板
- `spec-reader` skill 讀取設備規格作為驗證依據

---

## 如何開始工作

如果你是 Agent 並從本目錄啟動：

1. 本目錄有自己的 L1 agent 系統（`.claude/`），用於設備研究和配對分析。

2. 若要進行 Web Service 開發，切換到：
   `/Users/emilwu/VSCode/PedalGuy/Pedal-Web-Service/`（Agent commands 在 `Pedal-Web-Service/.claude/commands/`）

3. 若要進行 App 開發，切換到：
   `/Users/emilwu/VSCode/PedalGuy/Pedal-App/`（Agent commands 在 `Pedal-App/.claude/commands/`）

4. 若要查看產品規格和設計文件：
   `/Users/emilwu/VSCode/PedalGuy/Pedal-Web-Service-Planning/planning/`
