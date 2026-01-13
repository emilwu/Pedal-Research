# Skill: Technical Deep-Dive

**Skill Name:** Technical Deep-Dive
**Version:** 1.0
**Created:** 2025-12-30
**Purpose:** 技術深度分析、阻抗匹配、訊號路徑驗證、效果器功能差異比較

---

## Skill Role

你是 **Technical Deep-Dive Skill**，負責提供技術深度分析，驗證訊號鏈的技術可行性，並解釋效果器功能差異。

**核心功能:**
1. 阻抗匹配分析
2. 訊號路徑技術驗證
3. 效果器功能差異比較（如：Compressor vs Clean Boost）
4. 音頻特性分析
5. 潛在問題識別與解決方案

**知識來源:**
- `shared/equipment_database/pedals/specs/*.yaml` (技術規格)
- `.claude/knowledge/signal_chain_fundamentals.md`
- Signal Chain Builder 的訊號鏈配置

---

## Input Format

```yaml
input:
  signal_chain:
    - pedal: "esp_eclipse_ctm"
      type: "guitar"
      output_impedance: "~10kΩ (active pickups)"

    - pedal: "empress_mkii"
      type: "compressor"
      input_impedance: "高阻抗 (適合被動/主動拾音器)"
      output_impedance: "低阻抗"
      bypass: "True Bypass"

    - pedal: "pa1qg"
      type: "eq"
      input_impedance: "INST(1MΩ) / LINE(300kΩ)"
      output_impedance: "min. 10kΩ"
      bypass: "Buffered Bypass (HTS Circuit)"

    # ... 其他效果器

  analysis_requests:
    - type: "impedance_matching"
      focus: "訊號鏈阻抗是否匹配"

    - type: "function_comparison"
      pedals: ["empress_mkii", "from_yesterday"]
      question: "Compressor 是否能取代 Clean Boost？"

    - type: "signal_path_validation"
      routing: "4-Cable Method"
      amp: "tone_king"

    - type: "tone_suck_analysis"
      concern: "True Bypass 效果器過多是否導致 Tone Suck"
```

---

## Technical Analysis Algorithm

### Step 1: 阻抗匹配分析

#### 1.1 阻抗匹配原則

```yaml
impedance_matching_rules:
  rule_1:
    name: "輸出阻抗應低於輸入阻抗"
    formula: "Z_out < Z_in / 10"
    reason: "避免訊號衰減與頻率響應改變"

  rule_2:
    name: "高阻抗輸出 (吉他) 應連接高阻抗輸入"
    formula: "Guitar (10-50kΩ) → Pedal (>500kΩ)"
    reason: "保持高頻響應，避免 Tone Suck"

  rule_3:
    name: "Buffer 位置策略"
    placement: "訊號鏈前段或中段"
    reason: "驅動長導線與多個 True Bypass 效果器"

  rule_4:
    name: "避免連續高輸出阻抗"
    warning: "連續 True Bypass → True Bypass 可能導致訊號衰減"
    solution: "在中間加入 Buffer"
```

#### 1.2 訊號鏈阻抗分析

```python
def analyze_impedance_chain(signal_chain):
    analysis = []

    for i in range(len(signal_chain) - 1):
        current = signal_chain[i]
        next = signal_chain[i + 1]

        # 檢查阻抗匹配
        match_quality = check_impedance_match(
            current.output_impedance,
            next.input_impedance
        )

        analysis.append({
            'connection': f"{current.id} → {next.id}",
            'z_out': current.output_impedance,
            'z_in': next.input_impedance,
            'match_quality': match_quality,
            'issues': identify_issues(match_quality),
            'recommendation': get_recommendation(match_quality)
        })

    return analysis

def check_impedance_match(z_out, z_in):
    # 理想: Z_out < Z_in / 10
    ratio = z_in / z_out

    if ratio >= 10:
        return 'excellent'
    elif ratio >= 5:
        return 'good'
    elif ratio >= 3:
        return 'acceptable'
    else:
        return 'poor'
```

**輸出範例:**

```yaml
impedance_analysis:
  signal_chain: "ESP Eclipse → Empress MKII → PA-1QG → Sweet Honey → ... → Amp"

  connections:
    - connection: "ESP Eclipse → Empress MKII"
      z_out: "~10kΩ (active pickups)"
      z_in: "高阻抗 (>500kΩ)"
      ratio: ">50:1"
      match_quality: "✅ Excellent"
      notes: "完美匹配，吉他主動拾音器低輸出阻抗"

    - connection: "Empress MKII → PA-1QG"
      z_out: "低阻抗 (~1kΩ)"
      z_in: "1MΩ (INST mode)"
      ratio: "1000:1"
      match_quality: "✅ Excellent"
      notes: "極佳匹配，PA-1QG 高阻抗輸入"

    - connection: "PA-1QG → Sweet Honey"
      z_out: "min. 10kΩ"
      z_in: "~1MΩ"
      ratio: "100:1"
      match_quality: "✅ Excellent"
      notes: "PA-1QG Buffered Output 驅動後續效果器"

    - connection: "Sweet Honey → PRS Horsemeat"
      z_out: "~10-50kΩ (True Bypass Off 時)"
      z_in: "~1MΩ"
      ratio: "20-100:1"
      match_quality: "✅ Good to Excellent"
      notes: "True Bypass 效果器，但前面有 PA-1QG Buffer 保護"

    - connection: "... → FF-1Y → Amp Input"
      z_out: "min. 1kΩ (低阻抗負載)"
      z_in: "1MΩ (Amp input)"
      ratio: "1000:1"
      match_quality: "✅ Excellent"
      notes: "FF-1Y 低阻抗輸出，可驅動長導線"

  overall_assessment:
    verdict: "✅ 全鏈路阻抗匹配優異"
    key_factors:
      - "PA-1QG 提供 Buffer，保護整條訊號鏈"
      - "所有連接比例 >10:1"
      - "無潛在 Tone Suck 風險"

  buffer_strategy:
    primary_buffer: "PA-1QG (Always-on, HTS Circuit)"
    position: "訊號鏈前段 (第 3 位)"
    coverage: "保護後續所有 True Bypass 效果器"
    additional_buffers:
      - "FF-1Y (內建低阻抗輸出)"
      - "Nucleo (Buffered Output)"
```

---

### Step 2: 功能差異深度比較

#### 2.1 Compressor vs Clean Boost

```yaml
technical_comparison:
  question: "Empress MKII Compressor 是否能取代 Clean Boost？"

  devices:
    device_a:
      name: "From Yesterday (KOT Clone) - Clean Boost Mode"
      type: "Clean Boost"
      working_principle:
        input: "吉他訊號"
        process: "線性放大 (1:1)"
        output: "放大後訊號"
      characteristics:
        dynamic_range: "1:1 (完全保留)"
        frequency_response: "平坦 (±0.5dB)"
        thd: "<0.01% (極低失真)"
        gain_range: "+0 to +20dB"

    device_b:
      name: "Empress MKII Compressor"
      type: "VCA Compressor"
      working_principle:
        input: "吉他訊號"
        process: "動態範圍壓縮 (2:1/4:1/10:1) + 補償增益"
        output: "壓縮後訊號"
      characteristics:
        dynamic_range: "2:1 / 4:1 / 10:1 (壓縮)"
        frequency_response: "平坦至20Hz (Tilt EQ可調)"
        thd: "<0.01% (極低失真)"
        gain_range: "OUTPUT 可補償增益"

  key_differences:
    difference_1:
      aspect: "動態範圍處理"
      clean_boost: "1:1 (線性放大，完全保留動態)"
      compressor: "2:1/4:1/10:1 (壓縮動態，最低 2:1)"
      impact: "Compressor 會改變動態，撥弦力度細節減少"
      verdict: "❌ 不同本質"

    difference_2:
      aspect: "撥弦敏感度"
      clean_boost: "100% 保留 (輕撥弦→輕音量, 重撥弦→大音量)"
      compressor: "壓縮後減少差異 (輕重撥弦音量差異變小)"
      impact: "Jazz/Neo Soul 需要極細微動態，Compressor 會影響表現力"
      verdict: "❌ Compressor 降低敏感度"

    difference_3:
      aspect: "工作原理"
      clean_boost:
        formula: "V_out = V_in × Gain"
        nature: "純粹數學放大"
      compressor:
        formula: "V_out = f(V_in, Threshold, Ratio, Attack, Release)"
        nature: "複雜動態處理"
      verdict: "❌ 完全不同的處理邏輯"

    difference_4:
      aspect: "頻率響應"
      clean_boost: "完全平坦 (±0dB across spectrum)"
      compressor: "可透過 Tilt EQ 調整，但基礎壓縮仍作用"
      verdict: "⚠️ Compressor 雖可 EQ 平坦，但動態壓縮仍存在"

  can_replace:
    answer: "❌ 不能"
    reasons:
      - "Compressor 最低 Ratio 為 2:1，無法達到 1:1 線性放大"
      - "即使設定 INPUT 低、RATIO 2:1、MIX 50%，仍會壓縮動態"
      - "Jazz/Neo Soul 需要極細微的撥弦動態，Compressor 會改變音樂表現力"

  alternative_solution:
    device: "PA-1QG LEVEL Control"
    working_principle: "EQ 處理後的線性音量調整"
    characteristics:
      dynamic_range: "1:1 (線性)"
      frequency_response: "依 EQ 設定 (可設為平坦)"
      gain_range: "-12dB to +12dB"
    verdict: "✅ 可以取代 Clean Boost"
    advantage: "每把吉他獨立 Preset，MIDI 切換"
```

#### 2.2 PA-1QG LEVEL vs From Yesterday Clean Boost

```yaml
detailed_comparison:
  scenario: "Throbber PAF 8.7k 推動 Sweet Honey OD"

  method_1_from_yesterday:
    signal_path:
      - "Throbber 8.7k"
      - "→ From Yesterday (Yellow Clean, Gain 0, Volume +6dB)"
      - "→ Sweet Honey"
    output_level: "~12k equivalent"
    dynamic_preservation: "100%"
    frequency_response: "Flat"
    cost: "$335 (獨立效果器)"

  method_2_pa1qg_level:
    signal_path:
      - "Throbber 8.7k"
      - "→ PA-1QG (Preset 2: EQ Flat, LEVEL +6dB)"
      - "→ Sweet Honey"
    output_level: "~12k equivalent"
    dynamic_preservation: "100%"
    frequency_response: "Flat (EQ 設為正午)"
    cost: "$0 (PA-1QG 已擁有)"

  result:
    audio_equivalence: "✅ 100% 等效"
    technical_validation: "✅ 通過"
    cost_advantage: "✅ PA-1QG 邊際成本為 0"
    functional_advantage: "✅ PA-1QG 額外提供 EQ + MIDI Preset"

  conclusion:
    verdict: "PA-1QG LEVEL 完美取代 From Yesterday Clean Boost"
    confidence: "100%"
    recommendation: "移除 From Yesterday，回收 $335"
```

---

### Step 3: 訊號路徑技術驗證

#### 3.1 4-Cable Method 分析

```yaml
four_cable_method_analysis:
  amp: "Tone King Imperial MKII"
  routing_system: "JHS Swiss Things"

  signal_path:
    path_1_before_amp:
      route: "Guitar → Before Input (Swiss Things) → Amp Input"
      pedals:
        - "Empress MKII / Cali76 FET"
        - "PA-1QG"
      purpose: "塑形吉他基礎音色，在進入 Amp 前"
      technical_note: "Always-on 效果器，不受 Amp 切換影響"

    path_2_amp_preamp:
      route: "Amp Input → [Amp Preamp Gain Stages] → Amp FX Send"
      amp_processing: "Tone King 前級音色染色 + Gain"
      note: "Amp 本身的音色特性"

    path_3_after_preamp_before_power:
      route: "Amp FX Send → Loop 1 (Swiss Things) → Swiss Things Output → Amp FX Return"
      pedals:
        - "Sweet Honey, PRS Horsemeat, Morning Glory, Roshi Blacklon, TWA Source Code, ODL-1-CS"
      purpose: "Overdrive 在 Amp 前級後、功率管前"
      technical_note:
        issue: "⚠️ 此處放 Overdrive 會影響 Amp 前級音色"
        alternative: "應將 Overdrive 放在 Amp Input 前 (Before Input 或 Loop 1 在 Amp 前)"

    path_4_time_effects:
      route: "Amp FX Send → Loop 2 (Swiss Things) → Amp FX Return"
      pedals:
        - "FF-1Y Delay"
        - "Nucleo Reverb"
        - "AASB Shimmer Reverb"
      purpose: "Time-based 效果在 Amp 前級後"
      technical_note: "✅ 正確位置，避免 Delay/Reverb 被 Amp 失真"

  correction:
    issue: "原設計將 Overdrive 放在 FX Loop，技術上不理想"
    reason:
      - "Overdrive 應該推動 Amp 前級，不是在前級後"
      - "FX Loop 通常為 Line Level (+4dBu)，Overdrive 為 Instrument Level (-10dBV)"

    corrected_routing:
      before_input: ["Empress MKII", "Cali76 FET", "PA-1QG"]
      loop_1_before_amp: ["Sweet Honey", "PRS Horsemeat", "Roshi Blacklon", "TWA Source Code", "ODL-1-CS"]
      amp_input: "Swiss Things Output → Amp Input"
      amp_fx_send: "Amp FX Send → Swiss Things Return"
      loop_2_in_fx_loop: ["FF-1Y", "Nucleo", "AASB"]
      amp_fx_return: "Swiss Things Output → Amp FX Return"

  final_signal_path:
    complete_flow: |
      Guitar
      → Swiss Things Input
      → Before Input (Compressor + EQ)
      → Loop 1 (Overdrive) ← 可切換
      → Swiss Things Output
      → Amp Input
      → [Amp Preamp]
      → Amp FX Send
      → Swiss Things Return
      → Loop 2 (Delay + Reverb) ← 可切換
      → Swiss Things Output
      → Amp FX Return
      → [Amp Power Amp]
      → Speaker

    verification: "✅ 訊號路徑正確"
```

---

### Step 4: Tone Suck 分析

#### 4.1 True Bypass 累積效應

```yaml
tone_suck_analysis:
  concern: "訊號鏈中有多個 True Bypass 效果器，是否導致高頻損失？"

  true_bypass_pedals:
    count: 6
    list:
      - "Empress MKII (True Bypass)"
      - "Sweet Honey (True Bypass)"
      - "PRS Horsemeat (True Bypass)"
      - "Morning Glory (True Bypass)"
      - "TWA Source Code (True Bypass)"
      - "AASB (Smart Relay Bypass)"

  cable_analysis:
    patch_cables:
      quantity: 15
      avg_length: "20cm"
      total_length: "3m"
      capacitance: "~100pF/m × 3m = 300pF"

    instrument_cable:
      length: "3m (Guitar to Pedalboard)"
      capacitance: "~100pF/m × 3m = 300pF"

    total_capacitance: "600pF"

  high_frequency_loss_calculation:
    formula: "f_cutoff = 1 / (2π × R × C)"
    guitar_output_impedance: "10kΩ (active pickups)"
    total_capacitance: "600pF"
    cutoff_frequency: "1 / (2π × 10k × 600p) ≈ 26.5kHz"
    impact: "✅ 超過吉他頻率範圍 (20Hz-20kHz)"
    verdict: "✅ 無明顯高頻損失"

  buffer_protection:
    buffer: "PA-1QG (Always-on, HTS Circuit)"
    position: "訊號鏈前段 (第 3 位)"
    input_impedance: "1MΩ"
    output_impedance: "min. 10kΩ"
    protection_range: "PA-1QG 之後的所有效果器"
    verdict: "✅ Buffer 有效保護訊號"

  conclusion:
    tone_suck_risk: "✅ 低風險"
    reasons:
      - "ESP Eclipse 主動拾音器，輸出阻抗低 (~10kΩ)"
      - "PA-1QG Buffer 在前段保護訊號"
      - "總電容 600pF，高頻截止 26.5kHz (安全範圍)"
      - "FF-1Y、Nucleo 也提供 Buffered Output"

  recommendations:
    - "保持 PA-1QG Always-on (不可 Bypass)"
    - "使用高品質低電容導線 (<100pF/m)"
    - "Patch cable 儘量短 (15-30cm)"
```

---

### Step 5: 電平匹配分析

#### 5.1 Instrument Level vs Line Level

```yaml
signal_level_analysis:
  levels:
    instrument_level:
      range: "-10dBV (~316mVrms)"
      devices:
        - "吉他拾音器"
        - "Bass 拾音器"
        - "大部分效果器踏板"

    line_level:
      range: "+4dBu (~1.23Vrms) or -10dBV"
      devices:
        - "Mixer"
        - "Audio Interface"
        - "部分 Amp FX Loop (Tone King)"

  fx_loop_level_matching:
    amp: "Tone King Imperial MKII"
    fx_send_level: "Line Level (+4dBu)"
    fx_return_level: "Line Level (+4dBu)"

    pedals_in_fx_loop:
      - "FF-1Y (Delay)"
      - "Nucleo (Reverb)"
      - "AASB (Reverb)"

    level_matching:
      ft1y:
        max_input: "INST(+2dBm) / LINE(+13dBm)"
        verdict: "✅ 支援 LINE 輸入"

      nucleo:
        input: "Stereo TRS (適合高阻抗樂器)"
        note: "⚠️ 主要為 Instrument Level 設計"
        solution: "調整 Amp FX Send Level 或使用 Swiss Things Level 控制"

      aasb:
        input: "標準吉他 Pedal 阻抗"
        note: "⚠️ Instrument Level"
        solution: "同 Nucleo"

  recommendation:
    use_swiss_things: true
    reason: "Swiss Things 提供 Level Control，可調整 FX Loop 訊號電平"
    setting: "降低 Line Level (+4dBu) 至 Instrument Level (-10dBV)"
```

---

## Output Format

### Markdown 報告

```markdown
# 技術深度分析報告

**訊號鏈:** V2.0 Complete Signal Chain
**分析日期:** 2025-12-30

---

## 阻抗匹配分析

### 全鏈路阻抗檢查

[詳細表格...]

**結論:** ✅ 全鏈路阻抗匹配優異

---

## 功能差異比較

### Compressor vs Clean Boost

**問題:** Empress MKII 是否能取代 Clean Boost？

**分析:**
[詳細比較表...]

**結論:** ❌ 不能取代

**替代方案:** PA-1QG LEVEL ✅ 可以取代

---

## 4-Cable Method 驗證

[訊號路徑圖...]

**結論:** ✅ 路徑正確

---

## Tone Suck 風險評估

**結論:** ✅ 低風險

[詳細分析...]
```

### YAML 資料

```yaml
technical_analysis:
  impedance:
    verdict: "excellent"
    issues: []

  function_comparison:
    compressor_vs_boost:
      can_replace: false
      alternative: "pa1qg_level"

  signal_path:
    validation: "passed"

  tone_suck:
    risk: "low"
```

---

**文件行數:** ~495 行
**版本:** 1.0
**最後更新:** 2025-12-30
