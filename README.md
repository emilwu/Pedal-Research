# Pedal Research - 吉他效果器研究與訊號鏈管理系統

**版本:** 2.0
**最後更新:** 2025-12-30
**系統狀態:** ✅ 已建立核心架構

---

## 專案概述

這是一個由 AI Agent 驅動的吉他效果器研究與訊號鏈管理系統，專為以下需求設計：

✅ **動態設備管理** - 吉他、效果器、音箱清單可隨時更新
✅ **智慧配對邏輯** - 根據音樂風格、吉他特性自動推薦最佳效果器組合
✅ **專案化管理** - 支援多個獨立專案，可延續舊專案或建立新專案
✅ **雙格式輸出** - 人類可讀的 Markdown + AI 可讀的 YAML
✅ **版本控制** - 所有文件版本化，追蹤變更歷史

---

## 系統架構

```
Pedal-Research/
├── .claude/                  # AI Agents 與知識庫
│   ├── agents/              # 專門的 AI Agents
│   ├── skills/              # 可重用的 Skills
│   └── knowledge/           # 核心知識庫
│
├── projects/                # 所有專案（可以有多個）
│   └── 2025-v3-signal-chain/  # 前次專案（已完成）
│
├── shared/                  # 跨專案共享資料
│   ├── inventory/          # 當前設備清單（動態）
│   │   ├── guitars.yaml
│   │   ├── pedals.yaml
│   │   ├── amps.yaml
│   │   └── music_styles.yaml
│   │
│   ├── equipment_database/ # 設備完整資料庫
│   └── templates/          # 文件模板
│
└── reference_docs/         # 通用參考文件
```

---

## 核心 Agents

### 0. Project Initializer Agent
**用途:** 專案初始化，偵測新/舊專案
**觸發:** 專案開始時
**功能:**
- 檢測是否為新專案或現有專案
- 建立/讀取 Inventory
- 收集設備清單（透過問答）

---

### 1. Pedal Research Agent
**用途:** 研究新效果器，生成技術報告
**觸發:** `"研究 [品牌] [型號]"`
**功能:**
- 搜尋官網、評測、YouTube
- 與 Inventory 中現有設備比較
- 分析音樂風格適配性
- 輸出 MD + YAML 報告

**Web Search 優先順序:**
1. 官方產品網站
2. 官方產品手冊 (PDF)
3. 權威評測網站 (Premier Guitar, Reverb, Sweetwater)
4. YouTube (TPS, JHS Pedals, Reverb, Premier Guitar)
5. 用戶論壇

---

### 2. Signal Chain Builder Agent
**用途:** 建立訊號鏈配置
**觸發:** `"建立訊號鏈配置"`
**功能:**
- 透過問答收集需求（吉他/音箱/風格）
- 從 Inventory 讀取可用設備
- 使用 Pairing Logic Skill 計算最佳配對
- 生成詳細訊號鏈配置 (MD + YAML)

**問答流程:**
```
Q1: 選擇吉他 (從 Inventory 動態讀取)
Q2: 選擇音箱 (從 Inventory 動態讀取)
Q3: 選擇音樂風格 (從 Inventory 動態讀取)
Q4: 是否啟用預算分析？
```

---

## 核心 Skills

### Inventory Manager Skill
**用途:** 管理動態設備清單
**功能:**
- 新增設備
- 移除設備
- 更新設備資訊
- 查詢 Inventory

---

### Guitar-Pedal Pairing Logic Skill
**用途:** 計算最佳效果器配對
**輸入:**
- 吉他特性 (拾音器類型、輸出等級、琴身類型)
- 音樂風格
- 可用效果器清單 (從 Inventory)

**輸出:**
- 推薦的 Compressor + 設定
- 推薦的 Overdrive + 設定
- EQ 調整建議
- Delay/Reverb 配置

**核心邏輯:** 參考 `.claude/knowledge/pairing_rules.yaml`

---

## Knowledge Base

### 1. pairing_rules.yaml
配對規則庫，定義：
- 音樂風格 → 效果器需求
- 吉他特性 → 效果器調整
- 音箱特性 → 訊號鏈配置
- Swiss Things 路由規則

### 2. signal_chain_fundamentals.md
訊號鏈基礎知識：
- 標準訊號鏈順序
- 效果器分類與位置
- 4-Cable Method
- 阻抗與緩衝
- Gain Staging

### 3. music_style_reference.md (待建立)
音樂風格特性參考

---

## 使用流程

### 首次使用（新專案）

```
1. 觸發: "開始新的效果器研究專案"
   → Project Initializer Agent 啟動

2. Agent 詢問:
   - "請列出你擁有的吉他："
   - "請列出你擁有的效果器："
   - "請列出你擁有的音箱："
   - "主要演奏的音樂風格："

3. Agent 建立:
   ✅ shared/inventory/*.yaml
   ✅ shared/equipment_database/
   ✅ projects/[新專案名]/

4. 完成！可以開始研究效果器或建立訊號鏈
```

---

### 日常使用（現有專案）

#### 情境 1: 研究新效果器

```
User: "研究 Strymon BigSky，啟用預算分析"

→ Pedal Research Agent:
   1. 讀取 Inventory (發現已有 2 個 reverb)
   2. 研究 Strymon BigSky (官網、評測、YouTube)
   3. 與現有 reverb 比較 (Nucleo, AASB)
   4. 輸出報告:
      - data/research/pedals/strymon_bigsky_v1.md
      - data/research/pedals/strymon_bigsky_v1.yaml
   5. 詢問: "是否加入 Inventory？"

✅ 完成！
```

---

#### 情境 2: 建立訊號鏈

```
User: "建立訊號鏈配置"

→ Signal Chain Builder Agent:
   Q1: "選擇吉他："
       1. ESP Eclipse CTM (EMG, high output)
       2. ESP Throbber-CTM (SD APH-1, medium)
       3. Greco TE-500 (Lindy Fralin, medium)
       4. Fender Tokyo Thinline (single-coil)
   A1: 2

   Q2: "選擇音箱："
       1. Tone King Imperial MKII (有 FX loop)
       2. Roland JC-22 (無 FX loop)
   A2: 1

   Q3: "選擇音樂風格："
       1. Jazz (priority 1)
       2. Neo Soul (priority 2)
       ...
   A3: 1

   Q4: "啟用預算分析？"
   A4: 否

   → Agent 使用 Pairing Logic:
      - 推薦 Cali76 FET (溫暖適合 Jazz + semi-hollow)
      - 推薦 Sweet Honey (低增益，bypass 為主)
      - 建立 PA-1QG "Throbber Jazz" preset
      - 使用 4CM (Imperial 有 FX loop)

   → 輸出:
      - signal_chains/jazz_throbber_imperial_v1.md
      - signal_chains/jazz_throbber_imperial_v1.yaml

✅ 完成！
```

---

#### 情境 3: 更新 Inventory

```
User: "我賣掉了 JHS Morning Glory，買了 Walrus Slö"

→ Inventory Manager Skill:
   1. 移除 JHS Morning Glory
      Q: "保留研究資料？"
      A: 保留

   2. 新增 Walrus Slö
      - 發現已有研究資料 (之前研究過)
      - 加入 pedals.yaml

   3. 檢查影響
      - 發現 signal_chain_X 使用了 Morning Glory
      - 標記為 outdated
      Q: "是否重建受影響的訊號鏈？"

✅ Inventory 已更新！
```

---

## 當前設備清單（基於 2025-v3-signal-chain 專案）

### 吉他 (4)
1. ESP Eclipse CTM (EMG JH Set, high output)
2. ESP Throbber-CTM (SD APH-1, medium output, semi-hollow)
3. Greco TE-500 (Lindy Fralin Wide Range, medium output)
4. Fender Tokyo Thinline (Momose VT-1 single-coil, medium output)

### 效果器 (12)
**Compressors (2):**
1. Empress MKII (VCA, transparent)
2. Origin Effects Cali76 FET (FET, warm)

**EQ (1):**
3. Free the Tone PA-1QG (10-band, 99 presets, MIDI)

**Overdrives (5):**
4. Mad Professor Sweet Honey Deluxe (warm, Neo Soul)
5. PRS Horsemeat (Klon-style transparent boost)
6. JHS Morning Glory V3 (Bluesbreaker)
7. Roshi Blacklon (Blackface amp simulator)
8. TWA Source Code (TS evolution)
9. Free the Tone ODL-1-CS (Dumble-style)

**Delay (1):**
10. Free the Tone FT-1Y (Realtime BPM Analyzer, HOLD)

**Reverb (2):**
11. Cornerstone Nucleo (Stereo, nuclear reactor IR)
12. Lichtlaerm AASB (Shimmer, octave up/down/both)

### 音箱 (2)
1. Tone King Imperial MKII (Tube preamp, FX loop, 4CM)
2. Roland JC-22 (Solid-state, no FX loop, built-in chorus)

### 音樂風格偏好
1. Jazz (80% 使用率, priority 1)
2. Neo Soul (70%, priority 2)
3. Funk (60%, priority 3)
4. Post Rock (40%, priority 4)
5. Fusion (30%, priority 5)

**使用情境:** 80% 錄音, 20% 練習, 0% 現場

---

## 前次專案

### 2025 V3 訊號鏈優化專案
**路徑:** `projects/2025-v3-signal-chain/`
**狀態:** ✅ 已完成並歸檔 (2025-12-30)

**成果:**
- 設計兩條主要訊號鏈（Jazz/Neo Soul 和 Post Rock）
- 完整技術資料收集
- Swiss Things 路由器整合
- V3.0 版本變更（移除 Colosseum，新增 Horsemeat + Morning Glory）

**詳情:** 請參考 `projects/2025-v3-signal-chain/README.md`

---

## 下一步

### 待建立的 Agents/Skills

- [ ] Project Initializer Agent (`.claude/agents/0_project-initializer.md`)
- [ ] Inventory Manager Skill (`.claude/skills/inventory-manager.md`)
- [ ] Pedal Research Agent (`.claude/agents/1_pedal-researcher.md`)
- [ ] Guitar-Pedal Pairing Skill (`.claude/skills/guitar-pedal-pairing.md`)
- [ ] Signal Chain Builder Agent (`.claude/agents/2_signal-chain-builder.md`)

### 待建立的 Knowledge Base

- [ ] music_style_reference.md
- [ ] impedance_guide.md

### 待測試

- [ ] 完整工作流程測試
- [ ] 新專案建立流程
- [ ] 現有專案延續流程

---

## 技術細節

### 檔案命名規範

**研究報告:**
```
[brand]_[model]_v[N].md
[brand]_[model]_v[N].yaml
```

**訊號鏈配置:**
```
[style]_[guitar]_[amp]_v[N].md
[style]_[guitar]_[amp]_v[N].yaml
```

### 版本控制

所有文件使用版本號 `_v1`, `_v2`, `_v3` ...

每個新版本必須包含版本差異說明：
```markdown
## Changes from v1
- Added Tone King Imperial MKII pairing analysis
- Updated pricing information (USD)
- Added stereo routing examples
```

---

## 貢獻者

**專案負責人:** Emil Wu
**AI 協作:** Claude Code (Sonnet 4.5)
**專案開始:** 2025-12-22
**系統重構:** 2025-12-30

---

## License

此專案為個人研究專案，僅供個人使用。

---

**系統狀態:** ✅ 核心架構已建立，Agents/Skills 待實作

**最後更新:** 2025-12-30
