# 吉他訊號鏈基礎知識
# Guitar Signal Chain Fundamentals

**版本:** 1.0
**建立日期:** 2025-12-30
**用途:** 提供 Signal Chain Builder Agent 的基礎知識

---

## 標準訊號鏈順序

```
🎸 Guitar
  ↓
Tuner (always-on)
  ↓
Compressor (dynamics control)
  ↓
Wah / Filter (frequency sweep)
  ↓
Octave (pitch shifting)
  ↓
Fuzz (early gain, sensitive to impedance)
  ↓
Overdrive (tone shaping)
  ↓
Distortion (high gain)
  ↓
Boost (volume increase)
  ↓
EQ (tone shaping)
  ↓
Modulation (Chorus, Phaser, Flanger, Tremolo)
  ↓
Delay
  ↓
Reverb
  ↓
🎛️ Amp Input

→ (If amp has FX loop)
Amp Preamp → FX Send → [Modulation/Delay/Reverb] → FX Return → Power Amp
```

---

## 效果器分類與位置

### 1. Always-On Pedals (前級，在所有效果之前)

**類型**: Compressor, EQ, Preamp, Buffer

**位置**: Guitar → Always-On Pedals → Swiss Things INPUT (如有使用)

**理由**: 這些效果器需要持續作用，塑造基礎音色

**範例**:
- Guitar → Empress MKII Compressor → PA-1QG EQ → (其他效果器)

---

### 2. Gain Section (破音效果器)

**順序**: Octave → Fuzz → Overdrive → Distortion → Boost

**理由**:
- **Octave**: 需要最乾淨的訊號進行音高偵測
- **Fuzz**: 對阻抗敏感，需要接近吉他
- **Overdrive**: 中等增益，tone shaping
- **Distortion**: 高增益
- **Boost**: 最後推動，可推動前面的效果器或音箱

**Swiss Things**: 放在 Loop 1 (Unbuffered)

---

### 3. EQ Section

**位置**: Gain 之後，Modulation 之前

**用途**:
- 調整整體音色
- 補足吉他或效果器的頻率特性
- 作為 Clean Boost (如 PA-1QG 的 LEVEL 功能)

**Swiss Things**: 通常放在 INPUT 之前 (Always-on)

---

### 4. Modulation Section

**類型**: Chorus, Phaser, Flanger, Tremolo, Vibrato

**位置**: Gain 之後，Time-based 之前

**理由**: Modulation 放在 Gain 之後可以調變已塑形的音色

**Swiss Things**: 放在 Loop 2 (Buffered)

**4CM**: 放在 Amp 的 FX Loop 內

---

### 5. Time-Based Effects

**類型**: Delay, Reverb

**順序**: Delay → Reverb

**位置**: 訊號鏈最後，或 Amp FX Loop 內

**理由**:
- Delay 和 Reverb 應該是最後的空間處理
- 放在 FX Loop 可避免被 Amp 前級失真影響

**Swiss Things**: 放在 Loop 2 (Buffered)

---

## 訊號鏈方法

### Method 1: Pre-Amp Only (無 FX Loop 的音箱)

**適用**: Roland JC-22, 小型練習音箱

```
Guitar → [All Effects] → Amp Input
```

**效果器順序**:
```
Guitar → Compressor → EQ → OD → Distortion →
Modulation → Delay → Reverb → Amp
```

**優點**: 簡單直接
**缺點**: Delay/Reverb 會被音箱前級影響

---

### Method 2: 4-Cable Method (4CM)

**適用**: Tone King Imperial MKII, 有 FX Loop 的音箱

```
Guitar → [Pre-amp Effects] → Amp Input
→ Amp Preamp → Amp FX Send
→ [Post-amp Effects] → Amp FX Return
→ Amp Power Amp → Speaker
```

**效果器分配**:

**Pre-amp (進 Amp Input 之前)**:
- Compressor
- EQ
- Overdrive
- Distortion
- Boost

**FX Loop (Amp FX Send/Return)**:
- Modulation (Chorus, Phaser, Flanger)
- Delay
- Reverb

**優點**: Delay/Reverb 不被前級失真影響，音色更清晰
**缺點**: 需要更多線材，設定較複雜

---

### Method 3: Swiss Things Integration

**EarthQuaker Devices Swiss Things 訊號路徑**:

```
Guitar → [Always-on Pedals] → Swiss Things INPUT
  ↓
  ├→ TUNER OUT → Tuner (always-on)
  ↓
Loop 1 (Unbuffered) → [OD/Dist/Fuzz]
  ↓
  ├→ VOLUME EXP → Expression Pedal
  ↓
Loop 2 (Buffered) → [Delay/Reverb/Mod]
  ↓
BOOST (up to 20dB)
  ↓
OUTPUT A / OUTPUT B → Amp(s)
```

**關鍵規則**:
- **Always-on pedals** (Comp/EQ) 必須在 Swiss Things INPUT **之前**
- **Loop 1**: Unbuffered，放 Gain pedals
- **Loop 2**: Buffered，放 Time/Mod pedals
- **Loop 2 空接**: 可作為 MUTE 功能
- **Tuner**: 必須 always-on，不可 bypass

---

## 阻抗與緩衝 (Impedance & Buffering)

### 阻抗基礎

**吉他拾音器**: ~1MΩ (高阻抗)
**效果器輸入**: 通常 100kΩ ~ 1MΩ
**效果器輸出**: 通常 1kΩ ~ 10kΩ (低阻抗)

### Tone-Suck 問題

**原因**:
- 長線材 (>6m) + 高阻抗 = 高頻損失
- 多個 True Bypass 效果器串聯 = 累積阻抗損失

**解決方案**:
- 在訊號鏈前端加入 Buffer
- 使用 buffered bypass 效果器
- Swiss Things 內建 buffer

### Buffer 放置位置

**方案 1**: 在訊號鏈最前端
```
Guitar → Buffer → [All pedals] → Amp
```

**方案 2**: 在長線材之後
```
Guitar → [短線] → Pedalboard → Buffer → [長線] → Amp
```

**方案 3**: Swiss Things 整合
```
Guitar → [Always-on] → Swiss Things INPUT (內建 buffer)
```

---

## Gain Staging (增益階段)

### 原則

1. **逐步增加**: 每級效果器適度增加 gain，避免單一效果器過度失真
2. **音量匹配**: 效果器開啟/關閉時音量應相近，避免音量跳躍
3. **Headroom**: 保留足夠 headroom，避免不必要的 clipping

### 疊加策略

**透明 Boost → 溫暖 OD → 音箱**:
```
PRS Horsemeat (低 gain, 高 volume)
  → Sweet Honey (中 gain, 平衡 volume)
  → JC-22 (clean)
```

**多層破音 (Post Rock)**:
```
Roshi Blacklon (管機模擬)
  → Morning Glory (BB crunch)
  → TWA Source Code (TS mid push)
  → ODL-1-CS (Dumble saturation)
  → Imperial MKII (clean)
```

---

## 特殊考量

### 吉他拾音器類型

**主動拾音器 (EMG)**:
- 高輸出
- 內建 buffer
- 降低壓縮器輸入
- 降低 OD gain

**被動拾音器 (Seymour Duncan, Lindy Fralin)**:
- 中等輸出
- 需要注意阻抗匹配
- 標準設定

**單線圈**:
- 較薄音色
- 需要更多壓縮
- EQ 補足低頻

### 琴身類型

**Solid Body**:
- 標準設定

**Semi-Hollow**:
- 注意 feedback 風險
- 適度降低 reverb decay
- 偏好溫和壓縮 (Optical, FET)

---

## 使用情境最佳化

### 錄音室 (80% 使用率)

**優先考量**:
- 噪音控制 (使用 isolated power supply)
- Stereo 配置 (Swiss Things Output A+B)
- 音色品質優先於便攜性
- 可使用多台效果器疊加

### 現場演出 (0% 使用率)

**本專案不需考慮現場演出需求**

---

## 常見問題

### Q: 為什麼 Delay 要放在 Reverb 之前？

**A**: Reverb 是最後的空間處理，應該包覆所有聲音（包括 Delay 的 repeats）。如果 Reverb 在 Delay 之前，Delay 的 repeats 不會有 reverb tail，聽起來不自然。

### Q: Modulation 可以放在 Gain 之前嗎？

**A**: 可以，但不建議。Modulation 放在 Gain 之前會調變原始訊號，然後被 Gain 放大，可能造成不自然的效果。建議放在 Gain 之後。

### Q: Compressor 一定要放最前面嗎？

**A**: 通常是，因為 Compressor 需要處理最原始的動態。但也有人喜歡在 Compressor 之前放 Wah 或 Buffer。

### Q: Fuzz 為什麼要接近吉他？

**A**: Vintage Fuzz (如 Fuzz Face) 對阻抗非常敏感，需要看到吉他拾音器的高阻抗才能正常工作。放在 buffer 之後會失去特性。

---

**文件結束**

此文件提供訊號鏈基礎知識，供 Signal Chain Builder Agent 參考使用。
