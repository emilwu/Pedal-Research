# Skill: Budget Analyzer

**Skill Name:** Budget Analyzer
**Version:** 1.0
**Created:** 2025-12-30
**Purpose:** 財務分析、成本優化、投資回報計算、預算友好替代方案

---

## Skill Role

你是 **Budget Analyzer Skill**，負責分析效果器配置的財務狀況，計算成本、投資回報、提供預算友好的替代方案。

**核心功能:**
1. 總投資計算
2. Cost-per-function 分析
3. 回收金額估算
4. ROI（投資回報）計算
5. 預算友好替代方案
6. 購買優先順序排序

**知識來源:**
- `shared/inventory/pedals.yaml` (價格資訊)
- `shared/equipment_database/pedals/*.yaml` (詳細規格)
- Equipment Optimizer Skill 的優化建議

---

## Input Format

```yaml
input:
  current_configuration:
    pedals:
      - id: "empress_mkii"
        status: "owned"
        price: 219
        usage_rate: 95%

      - id: "from_yesterday"
        status: "owned"
        price: 335
        usage_rate: 16%

      - id: "sweet_honey"
        status: "owned"
        price: 220
        usage_rate: 60%

  optimization_recommendations:
    remove:
      - id: "from_yesterday"
        reason: "PA-1QG LEVEL 取代"
        reclaim_value: 335
        market_price_range: [250, 350]

      - id: "soul_food"
        reason: "Colosseum Klon Side 取代"
        reclaim_value: 90
        market_price_range: [60, 80]

    upgrade_to_core:
      - id: "twa_source_code"
        from: "tier_2"
        status: "owned"
        cost: 0

  budget_constraints:
    max_total_investment: 5000
    monthly_budget: null
    priority: "optimize_existing"  # or "add_new"

  analysis_options:
    include_roi: true
    include_alternatives: true
    time_horizon: "2_years"
```

---

## Budget Analysis Algorithm

### Step 1: 當前財務狀況分析

#### 1.1 總投資計算

```python
def calculate_total_investment(pedals):
    total = 0
    breakdown = {
        'compressor': 0,
        'eq': 0,
        'overdrive': 0,
        'delay': 0,
        'reverb': 0
    }

    for pedal in pedals:
        if pedal.status == 'owned':
            total += pedal.price
            breakdown[pedal.type] += pedal.price

    return {
        'total': total,
        'breakdown': breakdown,
        'pedal_count': len(pedals)
    }
```

**輸出範例:**

```yaml
current_investment:
  total: 3847
  currency: "USD"

  breakdown_by_type:
    compressor: 588  # Empress MKII (219) + Cali76 FET (369)
    eq: 425          # PA-1QG
    overdrive: 1863  # From Yesterday (335) + Sweet Honey (220) + Soul Food (90) + Colosseum (380) + Blacklon (200) + ODL-1-CS (425) + Morning Glory (179) + Virtues Arca (280)
    delay: 400       # FT-1Y
    reverb: 575      # Nucleo (350) + AASB (225)

  breakdown_by_tier:
    core_pedals: 3847  # 12 顆核心
    tier_2_backup: 578  # TWA Source Code (299) + PRS Horsemeat (279)

  pedal_count: 12
  average_cost_per_pedal: 321
```

#### 1.2 Cost-per-Function 分析

```python
def calculate_cost_per_function(pedals, signal_chains):
    analysis = []

    for pedal in pedals:
        # 計算此效果器提供的功能數
        functions = count_functions(pedal)

        # 計算使用率
        usage_rate = calculate_usage_rate(pedal, signal_chains)

        # Cost-per-function
        cpf = pedal.price / functions if functions > 0 else pedal.price

        # Effective cost (考慮使用率)
        effective_cost = pedal.price / (usage_rate / 100)

        analysis.append({
            'pedal': pedal.id,
            'price': pedal.price,
            'functions': functions,
            'usage_rate': usage_rate,
            'cost_per_function': cpf,
            'effective_cost': effective_cost,
            'value_score': usage_rate / cpf
        })

    return sorted(analysis, key=lambda x: x['value_score'], reverse=True)
```

**輸出範例:**

```yaml
cost_per_function_analysis:
  high_value:  # Value Score > 1.0
    - pedal: "pa1qg"
      price: 425
      functions: 3  # EQ + Clean Boost + MIDI Preset
      usage_rate: 95%
      cost_per_function: 142
      effective_cost: 447
      value_score: 0.67
      verdict: "✅ 高價值 - 多功能且高使用率"

    - pedal: "empress_mkii"
      price: 219
      functions: 1  # Compression
      usage_rate: 95%
      cost_per_function: 219
      effective_cost: 231
      value_score: 0.43
      verdict: "✅ 高價值 - 核心設備"

  medium_value:  # Value Score 0.3-1.0
    - pedal: "colosseum"
      price: 380
      functions: 2  # BB + Klon 雙通道
      usage_rate: 45%
      cost_per_function: 190
      effective_cost: 844
      value_score: 0.24
      verdict: "⚠️ 中等價值 - 雙通道但使用率中等"

  low_value:  # Value Score < 0.3
    - pedal: "from_yesterday"
      price: 335
      functions: 6  # 雙通道 × 3 模式
      usage_rate: 16%
      cost_per_function: 56
      effective_cost: 2094
      value_score: 0.29
      verdict: "❌ 低價值 - 僅使用 1/6 功能"

    - pedal: "soul_food"
      price: 90
      functions: 1  # Klon Boost
      usage_rate: 20%
      cost_per_function: 90
      effective_cost: 450
      value_score: 0.22
      verdict: "❌ 低價值 - 功能重疊"
```

---

### Step 2: 優化後財務分析

#### 2.1 計算優化節省

```yaml
optimization_impact:
  removed_pedals:
    - pedal: "from_yesterday"
      purchase_price: 335
      reclaim_estimate:
        low: 250  # 保守估計 (75%)
        mid: 300  # 合理估計 (90%)
        high: 350 # 樂觀估計 (105%)
      reclaim_method: "二手市場 (Reverb)"

    - pedal: "soul_food"
      purchase_price: 90
      reclaim_estimate:
        low: 60
        mid: 70
        high: 80
      reclaim_method: "二手市場"

    - pedal: "morning_glory"
      purchase_price: 179
      reclaim_estimate:
        low: 130
        mid: 150
        high: 170

    - pedal: "virtues_arca"
      purchase_price: 280
      reclaim_estimate:
        low: 210
        mid: 240
        high: 270

  total_reclaim:
    conservative: 650  # 250+60+130+210
    reasonable: 760    # 300+70+150+240
    optimistic: 870    # 350+80+170+270

  cost_reduction:
    removed_investment: 884  # 335+90+179+280
    new_investment: 0        # TWA Source Code 已擁有
    net_reduction: 884

  final_investment:
    before: 3847
    after: 2963   # 3847 - 884
    reduction: 884
    reduction_percentage: 23%
```

#### 2.2 新配置成本效益

```yaml
optimized_configuration:
  total_investment: 2963
  pedal_count: 10
  average_cost_per_pedal: 296  # 降低 8%

  average_usage_rate: 95%      # 提升 5%

  value_metrics:
    cost_per_usage_point: 31.2  # 2963 / 95
    vs_before: 42.7             # 3847 / 90
    improvement: 27%

  cost_efficiency:
    total_usage_points: 950     # 10 pedals × 95%
    vs_before: 1080             # 12 pedals × 90%
    cost_per_point: "$3.12 per usage point"
    vs_before: "$3.56 per usage point"
    improvement: "12% more efficient"
```

---

### Step 3: ROI 分析

#### 3.1 時間維度 ROI

```python
def calculate_roi(initial_investment, optimized_investment, reclaim_value, time_horizon):
    # 計算回收金額
    cash_return = reclaim_value

    # 計算避免的未來支出 (減少維護、不必要升級等)
    avoided_costs = (initial_investment - optimized_investment) * 0.1  # 假設每年 10% 維護成本

    # 計算使用效率提升帶來的價值
    efficiency_gain = (optimized_usage_rate - initial_usage_rate) * optimized_investment / 100

    # 總收益
    total_benefit = cash_return + (avoided_costs + efficiency_gain) * time_horizon

    # ROI
    roi = (total_benefit - optimized_investment) / optimized_investment * 100

    return roi
```

**輸出範例:**

```yaml
roi_analysis:
  time_horizon: "2_years"

  initial_state:
    investment: 3847
    usage_rate: 90%
    annual_maintenance_est: 385  # 10% of investment

  optimized_state:
    investment: 2963
    usage_rate: 95%
    annual_maintenance_est: 296

  benefits:
    immediate_cash_return: 760  # 二手出售回收
    avoided_maintenance: 178    # (385-296) × 2 years
    efficiency_gain: 148        # (95%-90%) × 2963
    total_benefit: 1086

  costs:
    optimization_effort: 0      # 僅重新配置，無額外購買

  roi:
    calculation: "(1086 - 0) / 2963 × 100"
    percentage: 37%
    verdict: "✅ 高回報 - 2年內回收 37%"

  break_even:
    time: "立即"  # 因為有現金回收
    note: "出售效果器後立即回收部分投資"
```

---

### Step 4: 預算友好替代方案

#### 4.1 針對不同預算等級的建議

```yaml
budget_tiers:
  tier_1_essential:
    budget: 1500
    description: "核心必備 - 最小可行配置"
    pedals:
      - empress_mkii: 219     # Compressor
      - pa1qg: 425            # EQ + Boost
      - sweet_honey: 220      # Warm OD
      - ft1y: 400             # Delay
      - nucleo: 350           # Reverb
    total: 1614
    coverage: "Jazz, Neo Soul, Funk"
    compromise: "無 Post Rock/Fusion 支援"

  tier_2_versatile:
    budget: 2500
    description: "多功能配置 - 70% 風格覆蓋"
    pedals:
      - tier_1_essential
      - cali76_fet: 369       # 第二顆 Compressor
      - twa_source_code: 299  # TS-style OD
      - aasb: 225             # Shimmer Reverb
    total: 2507
    coverage: "Jazz, Neo Soul, Funk, Post Rock, Fusion"
    compromise: "訊號鏈單一，無 Swiss Things"

  tier_3_complete:
    budget: 3500
    description: "完整配置 - 100% 風格覆蓋"
    pedals: [當前優化後的 10 顆效果器]
    total: 2963
    coverage: "100% 音樂風格"
    bonus: "預算有餘裕，可考慮 Swiss Things ($499)"
```

#### 4.2 便宜替代品建議

```yaml
budget_alternatives:
  # 如果預算緊張，可用便宜替代品

  high_end_pedals:
    - current: "PA-1QG"
      price: 425
      alternative: "Boss GE-7"
      alt_price: 130
      savings: 295
      compromise: "無預設功能、無 MIDI"

    - current: "FT-1Y"
      price: 400
      alternative: "Boss DD-8"
      alt_price: 200
      savings: 200
      compromise: "無 Realtime BPM Analyzer"

    - current: "Nucleo"
      price: 350
      alternative: "TC Electronic Hall of Fame 2"
      alt_price: 150
      savings: 200
      compromise: "無核電廠 IR、功能較少"

  total_potential_savings: 695

  verdict:
    recommendation: "不建議替換 - 功能損失大於成本節省"
    reason: "核心設備的獨特功能無可取代（如 PA-1QG Presets, FT-1Y BPM Analyzer）"
```

---

### Step 5: 購買優先順序

#### 5.1 基於成本效益排序

```python
def calculate_purchase_priority(pedals, budget, music_styles):
    priority_list = []

    for pedal in pedals:
        # 計算優先度分數
        score = 0

        # 1. 音樂風格覆蓋廣度 (0-40分)
        style_coverage = count_supported_styles(pedal, music_styles)
        score += (style_coverage / len(music_styles)) * 40

        # 2. 功能獨特性 (0-30分)
        uniqueness = calculate_uniqueness(pedal, pedals)
        score += uniqueness * 30

        # 3. Cost-per-function (0-20分)
        cpf_score = 1 - (pedal.price / max_price)
        score += cpf_score * 20

        # 4. Always-on 加分 (0-10分)
        if pedal.always_on:
            score += 10

        priority_list.append({
            'pedal': pedal,
            'priority_score': score,
            'cumulative_cost': cumulative_cost
        })

    return sorted(priority_list, key=lambda x: x['priority_score'], reverse=True)
```

**輸出範例:**

```yaml
purchase_priority:
  phase_1_must_have:
    - rank: 1
      pedal: "empress_mkii"
      price: 219
      cumulative: 219
      priority_score: 92
      reasons:
        - "Always-on 核心設備"
        - "支援 7/7 音樂風格"
        - "無可替代"

    - rank: 2
      pedal: "pa1qg"
      price: 425
      cumulative: 644
      priority_score: 89
      reasons:
        - "Always-on"
        - "EQ + Boost 二合一"
        - "MIDI Preset 切換"

  phase_2_versatile:
    - rank: 3
      pedal: "sweet_honey"
      price: 220
      cumulative: 864
      priority_score: 78
      reasons:
        - "核心溫暖 OD"
        - "支援 Jazz/Neo Soul/Funk"

    - rank: 4
      pedal: "ft1y"
      price: 400
      cumulative: 1264
      priority_score: 75
      reasons:
        - "Realtime BPM Analyzer 獨特"
        - "支援所有風格"

  phase_3_complete:
    [其他效果器...]

  budget_checkpoints:
    at_1000: "Phase 1 完成 (4 顆)"
    at_2000: "Phase 2 完成 (7 顆)"
    at_3000: "Phase 3 完成 (10 顆全部)"
```

---

## Output Format

### Markdown 報告

```markdown
# 財務分析與預算報告

**版本:** V2.0
**分析日期:** 2025-12-30
**時間範圍:** 2年

---

## 執行摘要

**當前投資:** $3,847 (12顆效果器)
**優化後投資:** $2,963 (10顆效果器)
**成本降低:** $884 (-23%)
**預估回收:** $650-790 (二手出售)

**ROI (2年):** 37%

---

## 財務狀況對比

### 當前配置 (V1.0)

| 項目 | 數值 |
|------|------|
| 總投資 | $3,847 |
| 效果器數量 | 12 顆 |
| 平均成本 | $321/顆 |
| 平均使用率 | 90% |
| Cost-per-usage | $42.7 |

### 優化後配置 (V2.0)

| 項目 | 數值 | 改善 |
|------|------|------|
| 總投資 | $2,963 | -23% |
| 效果器數量 | 10 顆 | -17% |
| 平均成本 | $296/顆 | -8% |
| 平均使用率 | 95% | +5% |
| Cost-per-usage | $31.2 | -27% |

---

## Cost-per-Function 分析

[詳細表格...]

---

## ROI 分析

[計算過程...]

---

## 購買優先順序建議

[分階段購買計畫...]

---

## 預算友好替代方案

[不同預算等級建議...]
```

### YAML 資料

```yaml
budget_analysis:
  date: "2025-12-30"
  version: "V2.0"

  current_state:
    total_investment: 3847
    pedal_count: 12
    average_usage: 90%

  optimized_state:
    total_investment: 2963
    pedal_count: 10
    average_usage: 95%

  financial_impact:
    cost_reduction: 884
    reclaim_estimate: 760
    roi_2years: 37%

  purchase_priority:
    - rank: 1
      pedal: "empress_mkii"
      price: 219
    [...]
```

---

## Error Handling

### 錯誤 1: 價格資訊缺失

```
Error: Price not found for pedal 'from_yesterday'
Solution: 補充 shared/inventory/pedals.yaml 中的價格資訊
```

### 錯誤 2: 回收估算不合理

```
Warning: 回收估算 $400 超過原價 $335
Solution: 調整回收估算為原價的 75-105%
```

---

**文件行數:** ~485 行
**版本:** 1.0
**最後更新:** 2025-12-30
