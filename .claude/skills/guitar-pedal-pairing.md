# Skill: Guitar-Pedal Pairing Logic

**Skill Name:** Guitar-Pedal Pairing Logic
**Version:** 1.0
**Created:** 2025-12-30
**Purpose:** 根據吉他特性與音樂風格計算最佳效果器配對

---

## Skill Role

你是 **Guitar-Pedal Pairing Logic Skill**，負責計算吉他與效果器的最佳配對。

輸入:
- 吉他特性 (拾音器類型、輸出等級、琴身類型)
- 音樂風格
- 可用效果器清單 (從 Inventory)

輸出:
- 推薦的 Compressor + 詳細設定
- 推薦的 Overdrive + 詳細設定
- EQ 調整建議
- Delay/Reverb 配置建議

核心邏輯來源: `.claude/knowledge/pairing_rules.yaml`

---

## Input Format

```yaml
input:
  guitar:
    id: "esp_throbber_ctm"
    brand: "ESP"
    model: "Throbber-CTM"
    pickup_type: "passive_humbucker"
    pickup_detail: "Seymour Duncan APH-1"
    output_level: "medium"
    body_type: "semi_hollow"

  music_style: "Jazz"

  available_equipment:
    compressors:
      - id: "empress_mkii"
        model: "Empress MKII"
        subtype: "vca"
      - id: "cali76_fet"
        model: "Origin Effects Cali76 FET"
        subtype: "fet"

    overdrives:
      - id: "sweet_honey"
        model: "Mad Professor Sweet Honey Deluxe"
        subtype: "transparent_warm"
      - id: "prs_horsemeat"
        model: "PRS Horsemeat"
        subtype: "klon_style_transparent"

    # ... 其他類型效果器

  budget_enabled: false  # 是否考慮預算
```

---

## Pairing Algorithm

### Step 1: 讀取配對規則

```
Read: .claude/knowledge/pairing_rules.yaml

Load:
- music_style_requirements
- guitar_characteristics
- amp_characteristics
- swiss_things_routing
```

### Step 2: 音樂風格需求分析

```yaml
# 從 pairing_rules.yaml 讀取

music_style_requirements.Jazz:
  compressor:
    preference: ["optical", "fet", "transparent_vca"]
    ratio: "low"
    mix: "70-100%"

  overdrive:
    preference: ["transparent", "warm", "low_gain"]
    gain_level: "low"
    bypass_default: true

  eq:
    adjustment: "subtle"
    focus_freq: [800, 3200]
    boost: "+0 to +3dB"

  # ... 其他需求
```

### Step 3: 吉他特性調整

```yaml
# 基於吉他特性，調整配對規則

guitar_characteristics:
  pickup_type:
    passive_humbucker:
      compressor_adjustment:
        input_level: "medium"
        ratio: "medium"

  body_type:
    semi_hollow:
      compressor_adjustment:
        preference: ["optical", "fet", "warm"]
      reverb_adjustment:
        decay: "-10%"
      feedback_warning: true
```

### Step 4: 效果器選擇邏輯

#### 4.1 Compressor 選擇

```python
# Pseudo code

def select_compressor(available_compressors, music_style, guitar):
    # 1. 根據音樂風格過濾
    style_prefs = pairing_rules.music_style_requirements[music_style].compressor.preference
    # ["optical", "fet", "transparent_vca"]

    # 2. 根據吉他特性調整
    if guitar.body_type == "semi_hollow":
        # 偏好溫暖類型
        style_prefs = ["optical", "fet"] + style_prefs

    # 3. 從可用清單中匹配
    candidates = []
    for comp in available_compressors:
        if comp.subtype in style_prefs:
            score = calculate_match_score(comp, style_prefs)
            candidates.append((comp, score))

    # 4. 選擇最高分
    best_compressor = max(candidates, key=lambda x: x[1])

    return best_compressor
```

**範例結果:**

```yaml
selected_compressor:
  id: "cali76_fet"
  model: "Origin Effects Cali76 FET"
  reason: |
    FET 壓縮特性溫暖，非常適合 Jazz。
    Semi-hollow 琴身需要溫和壓縮，FET 符合需求。
    Cali76 的 Dry mix 功能可保留動態，完美適合 Jazz。

  recommended_settings:
    in: "5-6 LED"
    attack: "fast"
    release: "medium"
    ratio: "1176 fixed (類似 4:1)"
    dry_mix: "70%"
    notes: |
      - IN: 中等輸入（passive medium output）
      - DRY: 70% 保留動態，符合 Jazz 需求
```

#### 4.2 Overdrive 選擇

```python
def select_overdrive(available_overdrives, music_style, guitar, amp):
    style_prefs = pairing_rules.music_style_requirements[music_style].overdrive.preference
    # ["transparent", "warm", "low_gain"]

    # 考慮吉他輸出
    if guitar.output_level == "high":
        # 高輸出需要透明 OD
        prefer_transparent = True

    # 考慮音箱類型
    if amp.type == "solid_state":
        # 晶體機需要增添溫暖度
        prefer_warm_or_amp_sim = True

    # 匹配
    candidates = match_overdrive(available_overdrives, style_prefs, ...)

    return best_overdrive
```

**範例結果:**

```yaml
selected_overdrive:
  id: "sweet_honey"
  model: "Mad Professor Sweet Honey Deluxe"
  reason: |
    Sweet Honey 屬於溫暖低增益 OD，非常適合 Jazz。
    FOCUS 控制提供獨特的中頻調整，適合 Jazz chord voicing。

  recommended_settings:
    drive: "9-10 o'clock"
    focus: "12 o'clock"
    volume: "12 o'clock"
    tone: "12 o'clock"

  bypass_default: true
  notes: |
    Jazz 主要使用 clean 音色。
    Sweet Honey 僅在需要輕微 breakup（例如 Blues）時開啟。
```

#### 4.3 EQ 調整建議

```yaml
eq_recommendation:
  pedal: "PA-1QG"
  preset_name: "Throbber Jazz"

  settings:
    level: "+3dB"
    eq_curve:
      - freq: 800
        gain: +2
        notes: "提升溫暖度"
      - freq: 3200
        gain: -1
        notes: "稍微降低高頻，避免過於明亮"

  reason: |
    ESP Throbber-CTM 的 APH-1 拾音器中等輸出，需要 +3dB boost。
    Jazz 需要溫暖音色，提升 800Hz 中頻。
    Semi-hollow 琴身本身有共鳴，高頻稍微降低避免過於明亮。
```

### Step 5: Swiss Things 路由分配

```yaml
swiss_things_routing:
  before_input:
    - "empress_mkii"  # Always-on compressor
    - "pa1qg"         # Always-on EQ

  loop_1:
    - "sweet_honey"   # Overdrive

  loop_2:
    - "ft1y"          # Delay
    - "nucleo"        # Reverb

  notes: |
    - Compressor 和 EQ 必須在 Swiss Things INPUT 之前
    - Overdrive 放 Loop 1 (unbuffered gain section)
    - Delay/Reverb 放 Loop 2 (buffered time section)
```

---

## Output Format

```yaml
pairing_result:
  compressor:
    model: "Origin Effects Cali76 FET"
    id: "cali76_fet"
    reason: "[詳細原因]"
    settings:
      in: "5-6 LED"
      attack: "fast"
      release: "medium"
      ratio: "1176 fixed"
      dry_mix: "70%"
    placement: "before_swiss_things_input"

  overdrive:
    model: "Mad Professor Sweet Honey Deluxe"
    id: "sweet_honey"
    reason: "[詳細原因]"
    settings:
      drive: "9-10 o'clock"
      focus: "12 o'clock"
      volume: "12 o'clock"
    bypass_default: true
    placement: "swiss_things_loop_1"

  eq:
    model: "PA-1QG"
    id: "pa1qg"
    preset_name: "Throbber Jazz"
    settings:
      level: "+3dB"
      eq_curve:
        - freq: 800
          gain: +2
        - freq: 3200
          gain: -1
    placement: "before_swiss_things_input"

  delay:
    model: "Free the Tone FT-1Y"
    id: "ft1y"
    reason: "Jazz 需要短 delay 提供 subtle articulation"
    settings:
      mode: "digital"
      time: "1/4 note"
      feedback: "2-3 repeats"
      mix: "15-25%"
    placement: "swiss_things_loop_2"

  reverb:
    model: "Cornerstone Nucleo"
    id: "nucleo"
    reason: "自然 room reverb 適合 Jazz"
    settings:
      mode: "room"
      decay: "30-40%"
      blend: "20-30%"
    placement: "swiss_things_loop_2"

  warnings:
    - "Semi-hollow 琴身在高音量可能有 feedback 風險"
    - "Reverb decay 不宜過長，保持自然"

  additional_notes: |
    此配對重視 clean headroom 與動態表現，符合 Jazz 需求。
    壓縮器使用 DRY mix 保留撥弦 attack。
    Overdrive 主要 bypass，僅在需要時開啟。
```

---

## Integration with Signal Chain Builder

此 Skill 的輸出會被 Signal Chain Builder Agent 使用：

```
Signal Chain Builder 呼叫:
  → Guitar-Pedal Pairing Skill
  → 取得 pairing_result
  → 建立完整訊號鏈配置
```

---

## Important Notes

1. **動態配對**
   - 所有配對基於 `pairing_rules.yaml`
   - 可隨時更新規則無需修改此 Skill

2. **多因素考量**
   - 音樂風格 (40% 權重)
   - 吉他特性 (30% 權重)
   - 音箱特性 (20% 權重)
   - 使用情境 (10% 權重)

3. **可擴展性**
   - 新增規則到 `pairing_rules.yaml`
   - 此 Skill 自動適應

---

**Skill 結束**
