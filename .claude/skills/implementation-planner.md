# Skill: Implementation Planner

**Skill Name:** Implementation Planner
**Version:** 1.0
**Created:** 2025-12-30
**Purpose:** 產生分階段實施計畫、購物清單、Pedalboard 佈局、測試驗證流程

---

## Skill Role

你是 **Implementation Planner Skill**，負責將訊號鏈配置轉化為實際可執行的分階段計畫。

**核心功能:**

1. 分階段執行步驟（Phase 1-5）
2. 購買優先順序與購物清單
3. Pedalboard 佈局設計
4. 電源供應計算與建議
5. 線材需求分析
6. 測試驗證 Checklist

**知識來源:**

- Signal Chain Builder 的訊號鏈配置
- Budget Analyzer 的購買優先順序
- Equipment Optimizer 的優化建議
- `.claude/knowledge/signal_chain_fundamentals.md`

---

## Input Format

```yaml
input:
  signal_chains:
    - id: "chain_1"
      name: "Jazz / Neo Soul / Funk"
      pedals:
        - empress_mkii
        - pa1qg
        - sweet_honey
        - prs_horsemeat
        - ft1y
        - nucleo

    - id: "chain_2"
      name: "Post Rock / Fusion"
      pedals:
        - cali76_fet
        - pa1qg
        - roshi_blacklon
        - twa_source_code
        - odl1cs
        - ft1y
        - nucleo
        - aasb

  routing_system:
    type: "swiss_things"
    model: "JHS Swiss Things"
    loops:
      before_input: ["empress_mkii", "cali76_fet", "pa1qg"]
      loop_1: ["sweet_honey", "prs_horsemeat", "roshi_blacklon", "twa_source_code", "odl1cs"]
      loop_2: ["ft1y", "nucleo", "aasb"]

  amps:
    - id: "tone_king"
      model: "Tone King Imperial MKII"
      fx_loop: true
    - id: "jc22"
      model: "Roland JC-22"
      fx_loop: false

  current_status:
    owned_pedals: [全部 10 顆已擁有]
    owned_cables: ["部分 patch cables"]
    owned_power: null

  budget:
    total: 1000
    priority: "power_supply_first"

  timeline:
    target: "8_weeks"
    flexibility: "可延長至 12 週"
```

---

## Implementation Planning Algorithm

### Step 1: 階段劃分策略

#### 1.1 分析依賴關係

```python
def analyze_dependencies(signal_chains, routing_system):
    # 1. 基礎設施需求
    infrastructure = {
        'pedalboard': True,  # 必需
        'power_supply': True,  # 必需
        'cables': True,  # 必需
        'routing_system': routing_system.type != None
    }

    # 2. 效果器分組
    pedal_groups = {
        'always_on': [],      # Phase 1 優先
        'core_tone': [],      # Phase 2
        'modulation_time': [] # Phase 3
    }

    # 3. 測試驗證階段
    testing_phases = {
        'phase_1': '基礎訊號鏈',
        'phase_2': 'Overdrive 堆疊',
        'phase_3': '完整 4-Cable Method',
        'phase_4': 'MIDI 整合'
    }

    return {
        'infrastructure': infrastructure,
        'pedal_groups': pedal_groups,
        'testing_phases': testing_phases
    }
```

**輸出範例:**

```yaml
implementation_phases:
  phase_1_foundation:
    duration: "Week 1-2"
    focus: "建立基礎設施"
    tasks:
      - "選購 Pedalboard"
      - "選購電源供應器"
      - "購買基礎線材"
    dependencies: []
    success_criteria: "硬體到位，可開始佈線"

  phase_2_core_setup:
    duration: "Week 3-4"
    focus: "設定核心效果器 (Always-on)"
    tasks:
      - "安裝 Empress MKII / Cali76 FET"
      - "設定 PA-1QG Presets (吉他專用 EQ)"
      - "測試基礎訊號路徑"
    dependencies: ["phase_1_foundation"]
    success_criteria: "Clean tone 優化完成"

  phase_3_tone_shaping:
    duration: "Week 5-6"
    focus: "Overdrive 訊號鏈"
    tasks:
      - "整合 Overdrive 效果器 (5 顆)"
      - "設定 Colosseum 雙通道"
      - "測試 Overdrive 堆疊"
    dependencies: ["phase_2_core_setup"]
    success_criteria: "Jazz/Neo Soul/Rock 音色達標"

  phase_4_time_effects:
    duration: "Week 7-8"
    focus: "Delay & Reverb"
    tasks:
      - "整合 FT-1Y Delay"
      - "整合 Nucleo & AASB Reverb"
      - "設定 4-Cable Method (Tone King)"
    dependencies: ["phase_3_tone_shaping"]
    success_criteria: "完整訊號鏈運作"

  phase_5_midi_optional:
    duration: "Week 9-12 (可選)"
    focus: "MIDI 整合"
    tasks:
      - "購買 MIDI Controller"
      - "設定 PA-1QG MIDI Presets"
      - "設定 FT-1Y MIDI Sync"
    dependencies: ["phase_4_time_effects"]
    success_criteria: "MIDI 一鍵切換吉他 Preset"
```

---

### Step 2: 購物清單生成

#### 2.1 Pedalboard 需求計算

```python
def calculate_pedalboard_size(pedals, routing_system):
    # 計算總佔地面積
    total_width = 0
    total_depth = 0

    for pedal in pedals:
        # 從 equipment database 讀取尺寸
        size = get_pedal_size(pedal.id)
        total_width += size.width
        total_depth = max(total_depth, size.depth)

    # 加上 routing system
    if routing_system:
        total_width += routing_system.width

    # 加上間距緩衝 (15%)
    recommended_width = total_width * 1.15
    recommended_depth = total_depth * 1.2

    return recommend_pedalboard(recommended_width, recommended_depth)
```

**輸出範例:**

```yaml
shopping_list:
  pedalboard:
    required_size:
      width: 60  # cm (10 pedals + Swiss Things + 間距)
      depth: 35  # cm

    recommendations:
      option_1:
        brand: "Pedaltrain"
        model: "Classic Pro"
        size: "61 × 40 cm"
        price: 129
        pros:
          - "標準尺寸，適合 10-12 顆效果器"
          - "附硬盒"
          - "Velcro 安裝"

      option_2:
        brand: "Rockboard"
        model: "TRES 3.1"
        size: "61 × 32.6 cm"
        price: 189
        pros:
          - "整合電源安裝位"
          - "模組化設計"

      recommended: "Pedaltrain Classic Pro"
      reason: "性價比最佳，尺寸充足"

  power_supply:
    total_current_draw:
      calculation: |
        Empress MKII: 100mA
        Cali76 FET: ~150mA
        PA-1QG: 200mA
        Sweet Honey: 5mA
        PRS Horsemeat: 16mA
        Roshi Blacklon: ~50mA
        TWA Source Code: ~100mA
        ODL-1-CS: 95mA
        FT-1Y: 400mA (12V!)
        Nucleo: ~150mA
        AASB: 150mA
        Swiss Things: 100mA
        ────────────────
        Total: ~1516mA (9V) + 400mA (12V)

    recommendations:
      option_1:
        brand: "Strymon"
        model: "Zuma"
        outputs: "9× 500mA (9V)"
        total: "4500mA"
        price: 279
        pros:
          - "高電流輸出"
          - "完全隔離"
          - "噪音極低"
        cons:
          - "無 12V 輸出 (需另購 FT-1Y 專用)"

      option_2:
        brand: "Truetone"
        model: "CS12"
        outputs: "8× 100mA + 2× 250mA + 2× 500mA (9V)"
        total: "3000mA"
        price: 199
        pros:
          - "多種電流輸出"
          - "隔離設計"
        cons:
          - "無 12V 輸出"

      special_note:
        pedal: "FT-1Y"
        voltage: "12V DC, 400mA"
        solution: "需單獨 12V 變壓器 (原廠附贈) 或購買支援 12V 的電供"

      recommended: "Strymon Zuma + FT-1Y 原廠變壓器"
      total_cost: 279

  cables:
    patch_cables:
      quantity: 15  # 10 pedals + Swiss Things 連接
      type: "短導線 (10-30cm)"
      recommendation:
        brand: "EBS"
        model: "Flat Patch Cables"
        price_per_pack: 30  # 6 條裝
        packs_needed: 3
        total: 90

    instrument_cables:
      - type: "Guitar to Pedalboard"
        length: "3m"
        recommendation: "高品質導線"
        price: 30

      - type: "Pedalboard to Amp Input"
        length: "3m"
        price: 30

    4_cable_method:
      required_for: "Tone King Imperial MKII"
      cables:
        - "Guitar → Swiss Things Input"
        - "Swiss Things Send → Amp Input"
        - "Amp FX Send → Swiss Things Return"
        - "Swiss Things Output → Amp FX Return"
      total_cables: 4
      recommendation: "同品牌同長度 (視覺整齊)"
      price: 120

    midi_cables:
      optional: true
      required_if: "啟用 MIDI 整合"
      cables:
        - "MIDI Controller → PA-1QG"
        - "PA-1QG → FT-1Y (MIDI Thru)"
      price: 40

  total_estimate:
    pedalboard: 129
    power_supply: 279
    patch_cables: 90
    instrument_cables: 60
    4_cable_cables: 120
    midi_cables: 40 (optional)
    ────────────────
    minimum: 678
    with_midi: 718
```

---

### Step 3: Pedalboard 佈局設計

#### 3.1 最佳化佈局算法

```python
def design_pedalboard_layout(pedals, signal_chain, pedalboard_size):
    # 原則:
    # 1. 訊號流由左至右 (或右至左，依個人習慣)
    # 2. 常用效果器置於前排 (易於踩踏)
    # 3. Always-on 可置於後排
    # 4. 電源供應藏於下方

    layout = {
        'row_1_front': [],  # 前排 (常踩)
        'row_2_back': []    # 後排 (Always-on)
    }

    # 依據使用頻率分配
    for pedal in pedals:
        if pedal.always_on:
            layout['row_2_back'].append(pedal)
        else:
            layout['row_1_front'].append(pedal)

    # 依據訊號鏈順序排列
    layout['row_1_front'].sort(key=lambda p: signal_chain.index(p.id))
    layout['row_2_back'].sort(key=lambda p: signal_chain.index(p.id))

    return layout
```

**輸出範例 (ASCII 圖):**

```text
Pedalboard Layout - Pedaltrain Classic Pro (61 × 40 cm)

┌─────────────────────────────────────────────────────────────┐
│  Row 2 (後排 - Always-on):                                 │
│  ┌────────┐  ┌────────┐  ┌────────┐                        │
│  │Empress │  │ Cali76 │  │ PA-1QG │                        │
│  │  MKII  │  │  FET   │  │        │                        │
│  └────────┘  └────────┘  └────────┘                        │
│                                                              │
│  Row 1 (前排 - 常用):                                       │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐  │
│  │Sweet │ │ PRS  │ │Roshi │ │ TWA  │ │ODL-1 │ │ FT-1Y│  │
│  │Honey │ │Horse │ │Black │ │Source│ │  CS  │ │      │  │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘  │
│                                                              │
│  Row 0 (底層):                                              │
│  ┌──────┐ ┌──────┐ ┌──────────────────────────┐           │
│  │Nucleo│ │ AASB │ │   Strymon Zuma (電源)    │           │
│  └──────┘ └──────┘ └──────────────────────────┘           │
└─────────────────────────────────────────────────────────────┘

訊號流向: Guitar → Empress MKII → PA-1QG → Sweet Honey → ... → AASB → Amp

Swiss Things 配置 (若使用):
  - Before Input: Empress MKII, Cali76 FET, PA-1QG
  - Loop 1: Sweet Honey, PRS Horsemeat, Roshi Blacklon, TWA Source Code, ODL-1-CS
  - Loop 2: FT-1Y, Nucleo, AASB
```

---

### Step 4: 測試驗證流程

#### 4.1 分階段測試 Checklist

```yaml
testing_checklist:
  phase_1_basic_signal:
    name: "基礎訊號測試"
    prerequisites:
      - "Pedalboard 組裝完成"
      - "電源連接完成"
      - "Patch cables 安裝完成"

    tests:
      - id: "T1.1"
        test: "Guitar → Amp 直連測試"
        expected: "乾淨訊號，無雜音"
        pass_criteria: "訊號清晰，無 hum/buzz"

      - id: "T1.2"
        test: "加入 Empress MKII (Bypass)"
        expected: "訊號無變化"
        pass_criteria: "True Bypass 正常"

      - id: "T1.3"
        test: "啟用 Empress MKII"
        expected: "壓縮效果，音量略提升"
        pass_criteria: "Gain Reduction LED 亮起"

      - id: "T1.4"
        test: "加入 PA-1QG (EQ Flat)"
        expected: "訊號無變化"
        pass_criteria: "Buffered Bypass 正常，無音色改變"

      - id: "T1.5"
        test: "PA-1QG LEVEL +6dB"
        expected: "音量提升約 2 倍"
        pass_criteria: "Clean Boost 功能正常"

    troubleshooting:
      hum_noise:
        cause: "Ground Loop"
        solution: "使用隔離電源，檢查導線品質"

      signal_loss:
        cause: "阻抗不匹配或線材問題"
        solution: "檢查 patch cable，確認 buffer 位置"

  phase_2_overdrive_stack:
    name: "Overdrive 堆疊測試"
    prerequisites:
      - "Phase 1 通過"
      - "所有 Overdrive 已安裝"

    tests:
      - id: "T2.1"
        test: "Sweet Honey 單獨測試"
        expected: "溫暖 OD，撥弦敏感"
        settings: "Volume 12點鐘, Drive 10點鐘"

      - id: "T2.2"
        test: "PRS Horsemeat → Sweet Honey"
        expected: "透明 Boost 推動 Sweet Honey"
        settings: "Horsemeat (Gain 9點鐘, Level 3點鐘)"

      - id: "T2.3"
        test: "TWA Source Code (TS-style 中頻)"
        expected: "中頻突出，Classic Rock 音色"
        settings: "Drive 12點鐘, Bite 12點鐘"

    pass_criteria:
      - "所有 OD 單獨運作正常"
      - "堆疊無過度 compression"
      - "音色符合預期 (Jazz/Neo Soul/Rock)"

  phase_3_4_cable_method:
    name: "4-Cable Method 測試 (Tone King)"
    prerequisites:
      - "Phase 2 通過"
      - "4-Cable 線材準備完成"

    tests:
      - id: "T3.1"
        test: "Guitar → Swiss Things → Amp Input"
        expected: "Before Input 效果器 (Compressor/EQ) 正常"

      - id: "T3.2"
        test: "Amp FX Send → Swiss Things → Amp FX Return"
        expected: "Loop 2 效果器 (Delay/Reverb) 在 FX Loop 中"

      - id: "T3.3"
        test: "Swiss Things Loop 1 (Overdrive)"
        expected: "OD 在 Amp 前級，推動 Amp"

      - id: "T3.4"
        test: "完整訊號鏈測試"
        path: "Guitar → Compressor → EQ → OD → Amp Input → [Amp Preamp] → Amp FX Send → Delay → Reverb → Amp FX Return → Speaker"
        expected: "所有效果器依序作用"

    troubleshooting:
      fx_loop_noise:
        cause: "FX Loop 訊號電平不匹配"
        solution: "調整 Swiss Things Output Level"

  phase_4_midi_integration:
    name: "MIDI 整合測試 (可選)"
    prerequisites:
      - "Phase 3 通過"
      - "MIDI Controller 已連接"

    tests:
      - id: "T4.1"
        test: "PA-1QG MIDI Program Change"
        expected: "切換吉他時，Preset 自動對應"
        test_steps:
          - "ESP Eclipse → Preset 1"
          - "Throbber → Preset 2"
          - "Greco TE-500 → Preset 3"

      - id: "T4.2"
        test: "FT-1Y MIDI Sync"
        expected: "Delay Time 與 MIDI Clock 同步"

    pass_criteria:
      - "MIDI 訊息正確傳遞"
      - "Preset 切換無延遲"
      - "吉他切換時 EQ + Boost 自動對應"
```

---

### Step 5: 故障排除指南

```yaml
troubleshooting_guide:
  issue_1_hum_noise:
    symptom: "持續性 60Hz Hum 聲"
    possible_causes:
      - "Ground Loop"
      - "電源供應品質不佳"
      - "導線遮蔽不良"
    solutions:
      - "使用隔離電源供應器"
      - "檢查所有導線遮蔽"
      - "確認 Amp 與效果器共用同一電源插座"

  issue_2_signal_loss:
    symptom: "訊號微弱或消失"
    possible_causes:
      - "True Bypass 效果器過多"
      - "導線過長"
      - "阻抗不匹配"
    solutions:
      - "在訊號鏈前段加入 Buffer (PA-1QG 已提供)"
      - "縮短導線長度"
      - "檢查 impedance matching"

  issue_3_tone_suck:
    symptom: "高頻損失，音色變暗"
    possible_causes:
      - "導線電容過高"
      - "效果器輸入阻抗過低"
    solutions:
      - "使用高品質低電容導線"
      - "確認 Buffer 位置正確 (PA-1QG 在前段)"

  issue_4_midi_not_responding:
    symptom: "MIDI Preset 不切換"
    possible_causes:
      - "MIDI Channel 設定錯誤"
      - "MIDI 線材故障"
    solutions:
      - "檢查 PA-1QG MIDI Channel (預設 ALL)"
      - "測試 MIDI 線材"
      - "確認 MIDI Controller Program Change 訊息"
```

---

## Output Format

### Markdown 報告

```markdown
# 實施計畫報告

**專案:** V2.0 訊號鏈實施
**目標完成時間:** 8 週
**預算:** $1,000

---

## 階段總覽

| 階段 | 時間 | 重點 | 預算 |
|------|------|------|------|
| Phase 1 | Week 1-2 | 基礎設施 | $678 |
| Phase 2 | Week 3-4 | 核心設定 | $0 |
| Phase 3 | Week 5-6 | Overdrive | $0 |
| Phase 4 | Week 7-8 | Time Effects | $0 |
| Phase 5 | Week 9-12 | MIDI (可選) | $250 |

---

## 購物清單

### 必需品 ($678)

1. **Pedalboard**
   - Pedaltrain Classic Pro: $129

2. **電源供應**
   - Strymon Zuma: $279

3. **線材**
   - Patch Cables (15條): $90
   - Instrument Cables: $180

### 可選 ($250)

4. **MIDI Controller**
   - Morningstar MC6 MKII: $250

---

## Pedalboard 佈局

[ASCII 圖...]

---

## 測試驗證流程

[詳細 Checklist...]
```

### YAML 資料

```yaml
implementation_plan:
  timeline: "8_weeks"
  budget: 1000

  phases:
    - phase: 1
      duration: "Week 1-2"
      tasks: [...]

  shopping_list:
    pedalboard: {...}
    power_supply: {...}
    cables: {...}

  layout: {...}

  testing: {...}
```

---

**文件行數:** ~510 行
**版本:** 1.0
**最後更新:** 2025-12-30
