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

## 本目錄結構

| 路徑 | 用途 |
|------|------|
| `shared/equipment_database/` | 設備技術規格（效果器、吉他、音箱、線材） |
| `shared/tone_theory/` | 音色理論、信號鏈原理 |
| `.claude/knowledge/` | 配對規則 YAML、信號鏈基礎 |
| `.claude/skills/` | L1 研究用 agent 技能 |
| `analysis/` | 設備分析報告 |
| `projects/` | 專案特定配對設定 |

---

## 硬性規則

**本目錄是唯讀的。** Web Service 的 Agent 系統（architect、builder、validator）不得寫入本目錄。

本目錄的資料被以下方式引用：
- `data-migrator` agent 讀取 `shared/equipment_database/` 產生遷移腳本
- `ai-integrator` agent 讀取 `.claude/knowledge/` 產生 prompt 模板
- `spec-reader` skill 讀取設備規格作為驗證依據

---

## 如何開始工作

如果你是 Agent 並從本目錄啟動：

1. 本目錄有自己的 L1 agent 系統（`.claude/`），用於設備研究和配對分析。

2. 若要進行 Web Service 開發，切換到：
   `/Users/emilwu/VSCode/PedalGuy/Pedal-Web-Service/`（Agent commands 在 `.claude/commands/`）

3. 若要進行 App 開發，切換到：
   `/Users/emilwu/VSCode/PedalGuy/Pedal-App/`（Agent commands 在 `.claude/commands/`）

4. 若要查看產品規格和設計文件：
   `/Users/emilwu/VSCode/PedalGuy/Pedal-Web-Service-Planning/planning/`
