# 現有 AI Agent 系統摘要

本文件摘要現有 Pedal Research AI Agent 系統的架構和資源，供網頁服務開發時參考。

---

## 系統概覽

現有系統是一個由 Claude AI 驅動的 CLI 工具，包含：
- 3 個專門 Agents
- 7 個可重用 Skills
- 2 個知識庫文件
- 完整的設備數據庫

**原始專案位置**：`/Users/emilwu/VSCode/Pedal-Research/`

---

## Agents 摘要

### 1. Project Initializer Agent
**檔案**：`.claude/agents/0_project-initializer.md`

**功能**：
- 專案初始化
- 設備清單收集（問答式）
- 專案繼承機制

**網頁服務對應**：用戶註冊流程、初始設備清單建立

---

### 2. Pedal Research Agent
**檔案**：`.claude/agents/1_pedal-researcher.md`

**功能**：
- 網路搜尋設備資料
- 生成結構化報告（YAML + Markdown）
- 設定建議生成

**核心邏輯摘要**：
```
1. 搜尋優先順序：
   - 官方產品網站（最高優先）
   - 官方產品手冊 PDF
   - 權威評測網站（Premier Guitar, Reverb, Sweetwater）
   - YouTube 評測影片
   - 用戶論壇

2. 輸出格式：
   - YAML：結構化資料（供程式處理）
   - Markdown：人類閱讀版本

3. 分析項目：
   - 基本規格
   - 音色特性
   - 建議設定（依情境）
   - 音樂風格適配
   - 吉他/音箱配對建議
```

**網頁服務對應**：設備研究請求功能

---

### 3. Signal Chain Builder Agent
**檔案**：`.claude/agents/2_signal-chain-builder.md`

**功能**：
- 問答式訊號鏈建構
- 配對計算
- 訊號流程圖生成

**核心邏輯摘要**：
```
1. 輸入收集：
   - 吉他選擇
   - 音箱選擇
   - 音樂風格選擇

2. 處理流程：
   - 呼叫 Guitar-Pedal Pairing Skill
   - 決定訊號鏈方法（4CM / Pre-Amp Only）
   - 生成配置

3. 輸出：
   - ASCII 訊號流程圖
   - 各效果器設定建議
   - 演奏建議
```

**網頁服務對應**：訊號鏈生成功能（v2.0）

---

## Skills 摘要

### 1. Inventory Manager Skill
**檔案**：`.claude/skills/inventory-manager.md`

**功能**：設備清單 CRUD

**網頁服務對應**：個人設備清單模組

---

### 2. Guitar-Pedal Pairing Skill ⭐
**檔案**：`.claude/skills/guitar-pedal-pairing.md`

**功能**：根據吉他特性與音樂風格計算最佳效果器配對

**核心邏輯**：
```
輸入：
- 吉他特性（拾音器類型、輸出等級、琴身類型）
- 音樂風格
- 可用效果器清單

處理：
- 讀取 pairing_rules.yaml
- 匹配吉他特性 → 效果器調整
- 匹配音樂風格 → 效果器需求
- 從可用清單中選擇最佳匹配

輸出：
- 推薦 Compressor + 設定
- 推薦 Overdrive + 設定
- EQ 調整建議
- Delay/Reverb 配置
- 警告訊息
```

**網頁服務對應**：智慧配對模組（核心）

---

### 3. Equipment Optimizer Skill
**檔案**：`.claude/skills/equipment-optimizer.md`

**功能**：優化效果器組合，減少功能重疊

**網頁服務對應**：設備替代分析（v2.0）

---

### 4. 其他 Skills
| Skill | 功能 | 網頁服務對應 |
|-------|------|-------------|
| Budget Analyzer | 財務分析 | 暫不實作 |
| Implementation Planner | 升級計畫 | 暫不實作 |
| Technical Deep-Dive | 技術深度分析 | 可整合至設備研究 |
| Usage Examples Generator | 使用範例生成 | 可整合至設備詳情 |

---

## 知識庫摘要

### 1. pairing_rules.yaml ⭐
**檔案**：`.claude/knowledge/pairing_rules.yaml`
**大小**：約 12 KB

**結構**：
```yaml
music_style_requirements:
  Jazz:
    compressor:
      preference: ["optical", "fet", "transparent_vca"]
      ratio: "low"
      mix: "70-100%"
    overdrive:
      preference: ["transparent", "warm", "low_gain"]
      bypass_default: true
    delay:
      type: "analog_style"
      time: "300-500ms"
    reverb:
      type: ["spring", "plate", "room"]
      mix: "20-40%"

  Neo Soul:
    compressor: ...
    overdrive: ...

  # ... 其他風格

guitar_characteristics:
  active_humbucker:
    compressor_adjustment:
      threshold: "+3dB"
      ratio: "-1"
    overdrive_adjustment:
      gain: "-20%"

  passive_humbucker:
    compressor_adjustment: ...
    overdrive_adjustment: ...

  # ... 其他拾音器類型

amp_characteristics:
  tube:
    signal_chain_method: "4CM_preferred"
    overdrive_position: "before_preamp"

  solid_state:
    signal_chain_method: "pre_amp_only"
    overdrive_position: "always_before"

  # ... 其他音箱類型
```

**網頁服務用途**：智慧配對的核心規則引擎

---

### 2. signal_chain_fundamentals.md
**檔案**：`.claude/knowledge/signal_chain_fundamentals.md`
**大小**：約 7 KB

**內容**：
- 標準訊號鏈順序
- 效果器分類與位置
- 4-Cable Method 說明
- 阻抗與緩衝基礎
- Gain Staging 原則

**網頁服務用途**：訊號鏈生成的參考知識

---

## 設備數據庫摘要

### 目錄結構
```
shared/equipment_database/
├── pedals/
│   ├── specs/          # 13+ YAML 規格檔
│   ├── reports/        # 對應 MD 報告
│   └── examples/       # 使用範例
├── guitars/
│   ├── specs/          # 4 YAML 規格檔
│   └── reports/        # 對應 MD 報告
├── amps/
│   ├── specs/          # 4 YAML 規格檔
│   └── reports/        # 對應 MD 報告
└── accessories/
    └── specs/          # 配件規格
```

### 設備 YAML 結構範例

**效果器**（`pedals/specs/empress_compressor_mkii.yaml`）
```yaml
id: empress_compressor_mkii
brand: Empress
model: Compressor MKII
type: pedal
subtype: compressor
compressor_type: vca
characteristics:
  - transparent
  - studio_grade
  - parallel_compression
controls:
  - name: Threshold
    range: "-40dB to +10dB"
  - name: Ratio
    range: "1:1 to 10:1"
  - name: Mix
    range: "0% to 100%"
recommended_settings:
  - scenario: "Jazz Clean"
    settings:
      threshold: "-20dB"
      ratio: "3:1"
      mix: "80%"
    description: "透明壓縮，保留動態"
music_styles:
  - Jazz
  - Neo Soul
  - Fusion
```

**吉他**（`guitars/specs/esp_eclipse_ctm.yaml`）
```yaml
id: esp_eclipse_ctm
brand: ESP
model: Eclipse CTM
type: guitar
body_type: solid
pickup_type: humbucker
pickup_config: HH
active_passive: active
output_level: high
pickup_model: EMG JH-B
characteristics:
  - modern
  - high_output
  - tight_low_end
music_styles:
  - Metal
  - Hard Rock
  - Fusion
```

### 初始數據統計

| 類型 | 數量 | 檔案格式 |
|-----|------|---------|
| 效果器 | 13+ | YAML + MD |
| 吉他 | 4 | YAML + MD |
| 音箱 | 4 | YAML + MD |
| 配件 | 2 | YAML + MD |

---

## 資料遷移建議

### 需遷移的資源

| 資源 | 路徑 | 用途 |
|-----|------|------|
| 設備規格 | `shared/equipment_database/*/specs/*.yaml` | 初始數據庫 |
| 設備報告 | `shared/equipment_database/*/reports/*.md` | 詳細描述 |
| 配對規則 | `.claude/knowledge/pairing_rules.yaml` | 配對引擎 |
| 訊號鏈知識 | `.claude/knowledge/signal_chain_fundamentals.md` | 參考文件 |

### 遷移注意事項

1. **YAML 結構標準化**
   - 現有 YAML 欄位命名需統一
   - 部分欄位可能需要補充

2. **圖片資源**
   - 現有系統無設備圖片
   - 網頁服務需另行收集或使用佔位圖

3. **版本資訊**
   - 現有檔案有版本標記（v1, v2...）
   - 遷移時取最新版本

---

## Agent 邏輯轉換建議

### Pedal Research Agent → 設備研究服務

**現有邏輯**：
```
用戶輸入品牌+型號 → AI 網路搜尋 → 整理資料 → 生成 YAML+MD
```

**網頁服務調整**：
```
用戶輸入品牌+型號 → 加入隊列 → 背景 AI 處理 → 存入數據庫 → Email 通知
```

**關鍵差異**：
- 非即時處理（排隊機制）
- 結果存入數據庫（非本地檔案）
- 通知機制（Email）

---

### Guitar-Pedal Pairing Skill → 智慧配對服務

**現有邏輯**：
```
讀取吉他資料 + 讀取音樂風格 + 讀取 pairing_rules
    ↓
計算配對
    ↓
輸出推薦 + 設定
```

**網頁服務調整**：
```
用戶選擇吉他/音箱/風格 → 檢查額度 → API 呼叫 AI → 即時返回結果 → 存入歷史
```

**關鍵差異**：
- 即時處理（需優化回應時間）
- 額度控制
- 結果歷史儲存

---

## 相關文件參考

以下文件可在開發時參考：

| 文件 | 路徑 | 說明 |
|-----|------|------|
| 系統 README | `README.md` | 系統總覽 |
| 工作進度 | `.claude/WORK_PROGRESS.md` | 開發歷程記錄 |
| 4音箱設計 | `projects/2025-v3-signal-chain/analysis/4_amps_signal_chain_design.md` | 訊號鏈設計範例 |
| 音樂風格定義 | `projects/2025-v3-signal-chain/inventory/music_styles.yaml` | 風格優先級定義 |
