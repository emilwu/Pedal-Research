# Skill: Equipment Optimizer

**Skill Name:** Equipment Optimizer
**Version:** 1.1
**Created:** 2025-12-30
**Last Updated:** 2026-01-12
**Purpose:** 優化效果器組合，減少功能重疊，提升使用率

**Version 1.1 Changes (2026-01-12)**:
- 移除 "minimize_cost" 作為優化目標
- 移除所有成本相關的決策考量
- 專注於功能重疊和使用率優化

---

## Skill Role

你是 **Equipment Optimizer Skill**，負責分析現有效果器配置，找出功能重疊、使用率低的設備，並提供優化建議。

**核心功能:**
1. 版本比較分析（如 V1.0 vs V2.0）
2. 效果器替換邏輯驗證
3. 功能重疊檢測
4. 使用率分析
5. 替代方案建議

**知識來源:**
- `projects/[current_project]/inventory/pedals.yaml`
- `shared/equipment_database/pedals/*.yaml`
- `.claude/knowledge/pairing_rules.yaml`

---

## Input Format

```yaml
input:
  current_configuration:
    pedals:
      - id: "empress_mkii"
        status: "active"
        usage_contexts:
          - signal_chain: "chain_1"
            music_styles: ["Jazz", "Neo Soul", "Funk"]
            usage_rate: 80%
      - id: "from_yesterday"
        status: "active"
        usage_contexts:
          - signal_chain: "chain_1"
            mode: "Yellow Clean Mode"
            usage_rate: 16%
      # ... 其他效果器

  signal_chains:
    - id: "chain_1"
      name: "Jazz / Neo Soul / Funk"
      pedals: ["empress_mkii", "pa1qg", "from_yesterday", "sweet_honey", "soul_food"]
    - id: "chain_2"
      name: "Post Rock / Fusion"
      pedals: ["cali76_fet", "pa1qg", "colosseum", "odl1cs"]

  music_style_usage:
    Jazz: 80%
    Neo_Soul: 70%
    Funk: 60%
    Post_Rock: 40%
    Fusion: 30%
    Pop_Rock: 30%
    Rock: 20%

  optimization_goals:
    - "reduce_overlap"          # 減少功能重疊
    - "improve_usage_rate"      # 提升使用率
    - "maintain_coverage"       # 維持音樂風格覆蓋
```

---

## Optimization Algorithm

### Step 1: 功能重疊檢測

#### 1.1 讀取效果器詳細資料

```
For each pedal in current_configuration:
    Read: shared/equipment_database/pedals/{pedal_id}.yaml

    Extract:
    - type (compressor, overdrive, delay, reverb)
    - subtype (vca, fet, transparent, klon_style, etc.)
    - features (特殊功能列表)
    - controls (控制項)
```

#### 1.2 建立功能矩陣

```yaml
# 建立功能對照表
function_matrix:
  clean_boost:
    providers:
      - pedal: "from_yesterday"
        mode: "Yellow Clean Mode"
        usage_rate: 16%
      - pedal: "pa1qg"
        feature: "LEVEL control (-12dB to +12dB)"
        usage_rate: 95%
      - pedal: "soul_food"
        mode: "Low Gain Boost"
        usage_rate: 20%

  klon_transparent_od:
    providers:
      - pedal: "soul_food"
        mode: "Normal Klon OD"
        usage_rate: 20%
        cost: 90
      - pedal: "colosseum"
        side: "Klon Side"
        usage_rate: 40%
        cost: 380 (已擁有，可共用)
      - pedal: "prs_horsemeat"
        mode: "Transparent"
        usage_rate: 0% (Tier 2)
        cost: 279

  # ... 其他功能類別
```

#### 1.3 檢測重疊

```python
# Pseudo code

overlap_analysis = []

for function_category, providers in function_matrix:
    if len(providers) > 1:
        # 有多個效果器提供相同功能

        # 計算重疊度
        overlap_score = calculate_overlap(providers)

        # 提取關鍵資訊
        overlap_analysis.append({
            'function': function_category,
            'providers': providers,
            'overlap_score': overlap_score,
            'recommendation': analyze_best_provider(providers)
        })

def calculate_overlap(providers):
    # 基於使用率、成本、邊際價值計算
    total_usage = sum(p.usage_rate for p in providers)
    redundancy = (total_usage - max(p.usage_rate for p in providers)) / total_usage
    return redundancy * 100  # 重疊百分比
```

**輸出範例:**

```yaml
overlaps_detected:
  - function: "clean_boost"
    overlap_score: 67%  # (16% + 20%) / (16% + 95% + 20%) ≈ 27% 重疊
    providers:
      - pedal: "from_yesterday"
        usage_rate: 16%
        marginal_value: "低 (僅使用 1/6 功能)"
      - pedal: "pa1qg"
        usage_rate: 95%
        marginal_value: "高 (同時提供 EQ)"
      - pedal: "soul_food"
        usage_rate: 20%
        marginal_value: "中"

    recommendation:
      action: "移除 from_yesterday 和 soul_food，統一使用 pa1qg LEVEL"
      reason: "PA-1QG 已擁有，且提供針對不同吉他的獨立 Preset"

  - function: "klon_transparent_od"
    overlap_score: 33%
    providers:
      - pedal: "soul_food"
        usage_rate: 20%
      - pedal: "colosseum"
        usage_rate: 40%

    recommendation:
      action: "移除 soul_food，使用 Colosseum Klon Side"
      reason: "Colosseum 已有 Klon Side，可低 Gain 設定當 Boost，訊號鏈2可雙通道疊加"
```

---

### Step 2: 使用率分析

#### 2.1 計算每顆效果器的使用率

```python
def calculate_pedal_usage_rate(pedal, signal_chains, music_style_usage):
    total_usage = 0

    for chain in signal_chains:
        if pedal.id in chain.pedals:
            # 計算此訊號鏈的加權使用率
            chain_usage = 0
            for style in chain.music_styles:
                chain_usage += music_style_usage[style]

            # 考慮在此訊號鏈中的實際使用情境
            if pedal.bypass_default:
                # 如果預設 Bypass，使用率折半
                chain_usage *= 0.5

            total_usage += chain_usage

    return total_usage / len(signal_chains)
```

**輸出範例:**

```yaml
usage_analysis:
  high_usage:  # >= 70%
    - pedal: "empress_mkii"
      usage_rate: 95%
      contexts: ["chain_1: Jazz/Neo Soul/Funk"]
      status: "保留 - 核心設備"

    - pedal: "pa1qg"
      usage_rate: 95%
      contexts: ["chain_1", "chain_2"]
      status: "保留 - Always-on"

  medium_usage:  # 40-69%
    - pedal: "sweet_honey"
      usage_rate: 60%
      contexts: ["chain_1: Neo Soul/Jazz"]
      status: "保留 - 核心音色"

    - pedal: "colosseum"
      usage_rate: 45%
      contexts: ["chain_2: Post Rock/Fusion"]
      status: "保留 - 雙通道靈活"

  low_usage:  # < 40%
    - pedal: "from_yesterday"
      usage_rate: 16%
      contexts: ["chain_1: Clean Boost only (Yellow Clean Mode)"]
      reason: "僅使用 1/6 功能"
      recommendation: "移除候選"

    - pedal: "soul_food"
      usage_rate: 20%
      contexts: ["chain_1: Klon Boost"]
      reason: "功能與 Colosseum Klon Side 重疊"
      recommendation: "移除候選"

  tier_2_unused:  # 0% (備用但未使用)
    - pedal: "twa_source_code"
      usage_rate: 0%
      reason: "降至 Tier 2，訊號鏈中未使用"
      potential: "可替代 from_yesterday 的透明 OD 角色"
```

---

### Step 3: 替代方案分析

#### 3.1 移除效果器後的空缺分析

```yaml
# 假設移除 "from_yesterday"

gap_analysis:
  removed_pedal: "from_yesterday"

  lost_functions:
    - function: "clean_boost"
      impact: "低"
      alternative: "PA-1QG LEVEL 完美替代"

    - function: "transparent_od"
      impact: "中"
      alternative: "訊號鏈1已有 Sweet Honey, 訊號鏈2缺少中等透明度 OD"

  coverage_check:
    music_styles:
      Jazz: "✅ 維持 (Sweet Honey + PA-1QG)"
      Neo_Soul: "✅ 維持"
      Funk: "✅ 維持"
      Post_Rock: "⚠️ 缺少 TS-style 中頻"
      Fusion: "⚠️ 缺少中等透明度 OD"

    gap_identified: true
    gap_description: "訊號鏈2缺少 TS-style 中頻突出 OD"
```

#### 3.2 填補空缺的候選分析

```yaml
# 分析 Tier 2 效果器是否可填補空缺

candidates_for_gap:
  gap: "TS-style 中頻 OD"

  candidates:
    - pedal: "twa_source_code"
      match_score: 95%
      reasons:
        - "✅ TS Evolution（保留 TS 中頻特性）"
        - "✅ 18V 內部升壓（比傳統 TS 更透明）"
        - "✅ Bite Control（調整偶次/奇次諧波）"
        - "✅ 原創設計者 Susumu Tamura"
      technical_validation:
        headroom: "18V 內部升壓 > 傳統 TS 9V"
        transparency: "中等透明度（介於 BB 和 Dumble 之間）"
        unique_feature: "Bite Control 無可取代"

      recommendation: "提升至核心，填補 from_yesterday 空缺"

    - pedal: "prs_horsemeat"
      match_score: 60%
      reasons:
        - "✅ Klon-style 透明"
        - "⚠️ 較溫暖，與 Sweet Honey 風格接近"
        - "❌ 無 TS-style 中頻"

      recommendation: "不適合，風格重疊"
```

---

### Step 4: 技術驗證

#### 4.1 替換邏輯驗證

```yaml
# 驗證 PA-1QG LEVEL 是否真能取代 Clean Boost

technical_validation:
  replacement: "PA-1QG LEVEL → From Yesterday Clean Boost"

  comparison:
    characteristic: "線性放大 (1:1)"
      from_yesterday: true
      pa1qg_level: true
      verdict: "✅ 相同"

    characteristic: "零壓縮"
      from_yesterday: true
      pa1qg_level: true
      verdict: "✅ 相同"

    characteristic: "透明度"
      from_yesterday: "極度透明"
      pa1qg_level: "極度透明 (EQ 平坦時)"
      verdict: "✅ 相同"

    characteristic: "針對不同吉他調整"
      from_yesterday: "❌ 固定設定"
      pa1qg_level: "✅ 每把吉他獨立 Preset"
      verdict: "✅ PA-1QG 更優"

    characteristic: "MIDI 切換"
      from_yesterday: "❌ 無"
      pa1qg_level: "✅ 自動對應吉他"
      verdict: "✅ PA-1QG 更優"

    characteristic: "額外功能"
      from_yesterday: "❌ 僅 Boost"
      pa1qg_level: "✅ 同時做 EQ 調整"
      verdict: "✅ PA-1QG 更優"

  conclusion: "PA-1QG LEVEL 完美取代 From Yesterday Clean Boost，且功能更強大"
  confidence: 100%
```

---

### Step 5: 優化建議生成

```yaml
optimization_recommendations:
  version: "V2.0"
  based_on: "V1.0"

  decisions:
    - decision_id: "D1"
      action: "移除 From Yesterday"
      reason: "PA-1QG LEVEL 取代 Clean Boost"
      technical_validation: "✅ 通過"
      impact:
        usage_rate_change: "16% → 0% (功能移至 PA-1QG)"
        coverage_loss: "無"

    - decision_id: "D2"
      action: "移除 Soul Food"
      reason: "Colosseum Klon Side 取代"
      technical_validation: "✅ 通過"
      impact:
        usage_rate_change: "20% → 0% (功能移至 Colosseum)"
        coverage_loss: "無"

    - decision_id: "D3"
      action: "提升 TWA Source Code 至核心"
      reason: "填補 from_yesterday 空缺 (TS-style 中頻)"
      technical_validation: "✅ 通過"
      impact:
        usage_rate_change: "0% → 35%"
        coverage_gain: "✅ Post Rock/Fusion TS-style 中頻"

    - decision_id: "D4"
      action: "保持原有移除建議 (Morning Glory + Virtues Arca)"
      reason: "功能已被其他效果器覆蓋"

  summary:
    pedal_count: "12 → 10 (-17%)"
    average_usage_rate: "90% → 95% (+5%)"
    overlap_reduction: "100%"
    coverage_maintenance: "100%"
```

---

## Output Format

### Markdown 報告

```markdown
# 效果器優化分析報告

**版本:** V2.0
**基於版本:** V1.0
**分析日期:** 2025-12-30

---

## 執行摘要

本次優化分析發現 3 處功能重疊，4 顆低使用率效果器，透過替換與升級策略，
可在維持 100% 音樂風格覆蓋的前提下，實現：

- ✅ 效果器數量：12顆 → **10顆** (-17%)
- ✅ 使用率：90% → **95%** (+5%)
- ✅ 功能重疊：**0%**

---

## 決策分析

### 決策 1: 移除 From Yesterday，用 PA-1QG LEVEL 取代 Clean Boost

**問題發現:**
- From Yesterday 在訊號鏈1僅使用 Yellow Clean Mode (1/6 功能)
- 使用率僅 16%

**替代方案:**
- PA-1QG LEVEL 控制 (-12dB to +12dB) 提供線性放大
- 功能更強：每把吉他獨立 Preset + MIDI 切換

**技術驗證:**
[對照表...]

**結論:** ✅ 移除 From Yesterday

---

### 決策 2: 移除 Soul Food，用 Colosseum Klon Side 取代

[分析...]

---

## 最終建議

[優化後的效果器清單...]
```

### YAML 資料

```yaml
optimization_report:
  version: "V2.0"
  date: "2025-12-30"

  current_state:
    pedal_count: 12
    average_usage_rate: 90%
    overlap_count: 3

  optimized_state:
    pedal_count: 10
    average_usage_rate: 95%
    overlap_count: 0

  improvements:
    pedal_reduction: -2
    usage_increase: +5%

  decisions:
    - id: "D1"
      action: "remove"
      target: "from_yesterday"
      reason: "PA-1QG LEVEL 取代 Clean Boost"

    - id: "D2"
      action: "remove"
      target: "soul_food"
      reason: "Colosseum Klon Side 取代"

    - id: "D3"
      action: "upgrade"
      target: "twa_source_code"
      from: "tier_2"
      to: "core"
      reason: "填補 TS-style 中頻空缺"

  final_pedal_list:
    - empress_mkii
    - cali76_fet
    - pa1qg
    - sweet_honey
    - prs_horsemeat
    - morning_glory
    - roshi_blacklon
    - twa_source_code
    - odl1cs
    - ft1y
    - nucleo
    - aasb
```

---

## Error Handling

### 錯誤 1: 找不到效果器資料

```
Error: Pedal data not found for 'from_yesterday'
Solution: 檢查 shared/equipment_database/pedals/from_yesterday.yaml 是否存在
```

### 錯誤 2: 移除後覆蓋不足

```
Warning: 移除 'from_yesterday' 後 Post Rock 覆蓋率降至 60%
Recommendation: 考慮保留或尋找替代方案
```

### 錯誤 3: 替換邏輯驗證失敗

```
Error: PA-1QG LEVEL 無法完美替代 Clean Boost
Reason: PA-1QG LEVEL 範圍僅 ±12dB，From Yesterday 可達 +20dB
Recommendation: 重新評估替換方案
```

---

## Usage Example

```bash
# 在 Signal Chain Builder Agent 中呼叫

Equipment Optimizer Skill:
  Input: current_pedal_configuration.yaml
  Process:
    1. 檢測功能重疊
    2. 分析使用率
    3. 提出優化建議
    4. 技術驗證
  Output:
    - optimization_report_v2.md
    - optimization_report_v2.yaml
```

---

**文件行數:** ~490 行
**版本:** 1.0
**最後更新:** 2025-12-30
