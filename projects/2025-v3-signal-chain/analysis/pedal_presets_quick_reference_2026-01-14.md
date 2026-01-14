# Pedal Presets 快速參考手冊

**更新日期:** 2026-01-14
**配置:** 11 Pedals + 4 Amps

---

## 目錄

1. [Always-on Foundation](#always-on-foundation)
2. [音樂類型 Presets](#音樂類型-presets)
3. [Amp 選擇指南](#amp-選擇指南)
4. [Pedal 開關組合速查表](#pedal-開關組合速查表)
5. [KOT 雙通道設定](#kot-雙通道設定)
6. [特殊應用場景](#特殊應用場景)

---

## Always-on Foundation

**所有場景都需要：**

```
Guitar → Empress MKII → PA-1QG → [Amp-specific pedals]
```

### Empress MKII 標準設定

```
INPUT:   低至中 (1-2 LED 觸發)
OUTPUT:  Unity gain
ATTACK:  中
RELEASE: 中
MIX:     80-100%
TONE:    正午 (12 點鐘)
RATIO:   2:1 (透明) 或 4:1 (標準)
SC HPF:  120Hz (6 弦吉他) 或 OFF
```

### PA-1QG 標準設定

```
10-band EQ: 針對吉他/音箱調整
LEVEL:      Unity (或略高做 boost)
```

---

## 音樂類型 Presets

### 1. Jazz (Clean)

**Amp:** JC-22 / Special 25 Clean / DSM Clean
**Pedals:** KOT Yellow Clean + Sweet Honey
**特性:** 極度乾淨，觸鍵敏感，溫暖

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → KOT (Yellow Clean) → Sweet Honey → Amp
                                   ↑ Always-on         ↑ Low gain
```

**Pedal 設定:**

**KOT Yellow:**
- Mode: **Clean Mode** (內部 DIP switch)
- Volume: 高 (boost)
- Drive: 低 (minimal distortion)
- Tone: 12 點鐘
- Footswitch: **Always-on**

**Sweet Honey:**
- Volume: Unity
- Drive: 低 (edge of breakup)
- **Focus: CCW** (需要用力彈奏才失真，Jazz 風格)
- Treble: 12 點鐘
- Bass: 略高於 12 點鐘
- Footswitch: On (或 always-on)

**Amp 設定:**
- JC-22: Clean channel, Chorus 適量
- Special 25: Clean channel, Boost off
- DSM: Clean channel

---

### 2. Neo Soul

**Amp:** JC-22 (首選，JC Chorus 是關鍵)
**Pedals:** Sweet Honey + Horsemeat
**特性:** 溫暖甜美，豐富諧波，中頻飽滿

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → Sweet Honey → Horsemeat → JC-22
                                   ↑ 核心音色    ↑ Solo boost
```

**Pedal 設定:**

**Sweet Honey:**
- Volume: Unity 或略高
- Drive: 中 (sweet spot)
- **Focus: 12 點鐘** (平衡設定)
- Treble: 12 點鐘
- Bass: 12 點鐘
- Footswitch: **Always-on**

**Horsemeat:**
- Level: Unity 或略高 (solo boost)
- Gain: 低至中
- **Voice: 中偏 CW** (略偏 glassy)
- Treble: 12 點鐘
- Bass: 略高於 12 點鐘 (Germanium 溫暖)
- Footswitch: 需要時開啟

**JC-22 設定:**
- Chorus: **On, 適量** (Neo Soul 關鍵)
- Reverb: 少量
- Stereo FX Loop: Nucleo stereo reverb

---

### 3. Blues

**Amp:** JC-22 / Special 25
**Pedals:** KOT Red OD + Sweet Honey
**特性:** 透明 overdrive + 溫暖感，動態豐富

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → KOT (Red OD) → Sweet Honey → Amp
```

**Pedal 設定:**

**KOT Red:**
- Mode: **OD Mode** (內部 DIP switch)
- Volume: Unity 或略高
- Drive: 中 (medium gain, 類似 Morning Glory)
- Tone: 12 點鐘
- Footswitch: On

**Sweet Honey:**
- Volume: Unity
- Drive: 低至中
- **Focus: CCW 至 12 點鐘** (Blues 風格)
- Treble: 12 點鐘
- Bass: 略高於 12 點鐘
- Footswitch: Always-on 或疊加使用

**Amp 設定:**
- JC-22: Clean channel
- Special 25: Clean channel 或 Drive channel (low gain)

---

### 4. Fusion

**Amp:** DSM (錄音) / Special 25 (舞台)
**Pedals:** KOT + ODL-1 CS
**特性:** Dumble 高階音色，豐富諧波，Fusion 經典

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → KOT (Yellow Clean) → ODL-1 CS → Amp
                                   ↑ Optional boost    ↑ Dumble tone
```

**Pedal 設定:**

**KOT Yellow:**
- Mode: Clean Mode
- Volume: 高 (boost)
- Drive: 低
- Footswitch: Optional (可選)

**ODL-1 CS:**
- Channel: **Normal** (或 Drive 視需求)
- NOR LEVEL: Unity 或略高
- TONE: 12 點鐘
- GAIN: 低至中
- **EQ Switch: GLASS ON** (類似 Fender Vibroverb bright)
- **ROCK/JAZZ: JAZZ** (降低 gain，強調低頻)
- Footswitch: On

**Amp 設定:**
- DSM: Clean 或 OD channel
- Special 25: Clean channel

**進階技巧:**
- Dumble on Dumble: ODL-1 CS → DSM OD channel (超厚音色)

---

### 5. Classic Rock

**Amp:** JC-22 / Special 25
**Pedals:** Source Code + Horsemeat
**特性:** TS 中頻 boost + Klon 透明 boost，經典 Rock 音色

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → Source Code → Horsemeat → Amp
                                   ↑ TS 中頻     ↑ Klon boost
```

**Pedal 設定:**

**Source Code:**
- Level: Unity 或略高
- Drive: 中
- Tone: 12 點鐘至 1 點鐘 (略偏明亮)
- **Bite: 12 點鐘** (平衡 odd/even harmonics)
- Footswitch: On

**Horsemeat:**
- Level: 略高 (boost)
- Gain: 低至中
- **Voice: CW** (偏 glassy，Classic Rock 音色)
- Treble: 12 點鐘
- Bass: 12 點鐘
- Footswitch: On (疊加 Source Code)

**Amp 設定:**
- JC-22: Clean channel
- Special 25: Drive channel (low gain)

---

### 6. Post Rock (Clean Ambient)

**Amp:** JC-22 (Stereo 必要)
**Pedals:** KOT Yellow Clean only
**特性:** Minimal drive, focus on reverb

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → KOT (Yellow Clean) → JC-22 INPUT
           ↑ 重要                                       ↓
                                                  JC-22 FX SEND
                                                        ↓
                                                  Nucleo (Stereo) → AASB → FF-1Y
                                                        ↓
                                                  JC-22 FX RETURN L/R
```

**Pedal 設定:**

**Empress MKII:**
- **Post Rock 專用設定:**
- INPUT: 中 (更多壓縮)
- OUTPUT: Unity
- ATTACK: 慢 (平滑 attack)
- RELEASE: 中至慢
- MIX: 70-80% (平行壓縮)
- RATIO: 4:1
- **重要:** Post Rock 需要更多壓縮控制 sustain

**KOT Yellow:**
- Mode: Clean Mode
- Volume: 高 (boost)
- Drive: 極低 (minimal)
- Footswitch: Always-on

**JC-22 FX Loop (Stereo):**
- FF-1Y: Long delay, stereo
- Nucleo: Large hall, 長 decay, **stereo imaging 完整發揮**
- AASB: Shimmer reverb

**重點:** Stereo reverb 是 Post Rock 核心，JC-22 stereo speakers 完整發揮

---

### 7. Funk

**Amp:** JC-22 (JC Chorus + Compression)
**Pedals:** Empress MKII + KOT Yellow Clean
**特性:** Tight compression, clean tone, JC Chorus

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → KOT (Yellow Clean) → JC-22
           ↑ Funk 壓縮重要
```

**Pedal 設定:**

**Empress MKII:**
- **Funk 專用設定:**
- INPUT: 中 (明顯壓縮)
- OUTPUT: Unity 或略高
- ATTACK: **快** (保留 transient)
- RELEASE: **快至中** (Funk 節奏感)
- MIX: 80-100%
- RATIO: 4:1
- SC HPF: 120Hz (避免低頻過度壓縮)

**KOT Yellow:**
- Mode: Clean Mode
- Volume: 高 (boost)
- Drive: 極低 (保持 clean)
- Footswitch: Always-on

**JC-22 設定:**
- Chorus: **On, 中等量** (Funk 關鍵)
- Clean channel

---

### 8. Shoegaze (Maximum Gain)

**Amp:** JC-22 / Special 25 Drive
**Pedals:** All stacked (KOT → Sweet Honey → ODL-1 Drive → Source Code)
**特性:** 漸進疊加，複雜失真質感，大量 reverb

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → KOT → Sweet Honey → ODL-1 CS (Drive) → Source Code → Amp
                                   ↑1    ↑2          ↑3                  ↑4
                                   漸進疊加失真
```

**Pedal 設定:**

**1. KOT (Red OD):**
- Mode: OD Mode (或 Dist Mode)
- Volume: Unity
- Drive: 中
- Footswitch: On

**2. Sweet Honey:**
- Volume: Unity
- Drive: 中
- Focus: 12 點鐘至 CW
- Footswitch: On

**3. ODL-1 CS:**
- Channel: **Drive**
- DRV LEVEL: Unity
- DRIVE: 中至高
- PUSH: 中至高
- HI CUT: 適量 (控制高頻尖銳)
- **ROCK/JAZZ: ROCK** (增加 gain)
- Footswitch: On

**4. Source Code:**
- Level: Unity
- Drive: 中
- Bite: 順時針 (更多 odd harmonics，更多顆粒感)
- Footswitch: On

**Amp 設定:**
- JC-22: Clean (或 Special 25 Drive channel)
- **重要:** 大量 stereo reverb (Nucleo + AASB)

---

### 9. High Gain Rock

**Amp:** Special 25 Drive channel
**Pedals:** ODL-1 CS Drive + Source Code (optional)
**特性:** Special 25 內建 "wild saturation" 已足夠

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → [Minimal pedals] → Special 25 (Drive channel)
                                   ↑ Optional: ODL-1 CS Drive + Source Code
```

**Pedal 設定:**

**ODL-1 CS (Optional):**
- Channel: Drive
- DRV LEVEL: Unity
- DRIVE: 高
- PUSH: 高
- **ROCK/JAZZ: ROCK**
- Footswitch: On

**Source Code (Optional):**
- Level: Unity
- Drive: 中至高
- Bite: 順時針
- Footswitch: On (疊加 ODL-1)

**Special 25 設定:**
- Channel: **Drive**
- Gain: 中至高 ("wild saturation")
- Master: 適量

**重點:** Special 25 Drive channel 本身已經可達 "wild saturation"，外部 pedals 可選

---

### 10. Country

**Amp:** JC-22
**Pedals:** KOT Yellow Clean + Horsemeat
**特性:** Clean tone with twang

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → KOT (Yellow Clean) → Horsemeat → JC-22
```

**Pedal 設定:**

**KOT Yellow:**
- Mode: Clean Mode
- Volume: 高
- Drive: 低
- Footswitch: Always-on

**Horsemeat:**
- Level: Unity 或略高
- Gain: 低 (clean boost)
- **Voice: CCW** (偏 saturated/meaty，接近 Fender 溫暖)
- Treble: 略高於 12 點鐘 (twang)
- Bass: 12 點鐘
- Footswitch: On

**⚠️ 限制:**
- 缺少 Fender Blackface 特有音色 (Blacklon 被淘汰)
- 覆蓋度: 85%

**緩解方案:**
- 可選: ODL-1 CS Normal + GLASS mode (類似 Fender Vibroverb)

---

### 11. Ambient

**Amp:** JC-22 (Stereo) / Imperial (Stereo XLR 錄音)
**Pedals:** KOT Yellow Clean + Nucleo + AASB
**特性:** Minimal drive, maximum reverb, stereo imaging

**訊號鏈:**
```
Guitar → Empress MKII → PA-1QG → KOT (Yellow Clean) → JC-22
                                                         ↓
                                                   JC-22 FX SEND
                                                         ↓
                                                   Nucleo (Stereo) → AASB (Stereo) → FF-1Y
                                                         ↓
                                                   JC-22 FX RETURN L/R
```

**Pedal 設定:**

**KOT Yellow:**
- Mode: Clean Mode
- Volume: 高
- Drive: 極低
- Footswitch: Always-on

**Nucleo:**
- **Large hall 或 ambient preset**
- Decay: 長
- Mix: 高 (50-70%)
- **Stereo width: 最大**

**AASB:**
- Shimmer reverb
- **Stereo mode**
- Mix: 適量

**重點:** Stereo reverb 是 Ambient 核心，JC-22 stereo speakers 或 Imperial stereo XLR 完整發揮

---

## Amp 選擇指南

### 錄音場景

| 音色需求 | 首選 Amp | Pedal 配置 | 理由 |
|---------|---------|-----------|------|
| **British Tube Tone** | Imperial MKII | Minimal (2-3 個) | 內建 Lead channel + 15 IRs |
| **Dumble ODS Tone** | DSM Dumblifier | Minimal (2-3 個) | 完整 Dumble ODS amp sim |
| **Fusion / Jazz** | DSM 或 Imperial | ODL-1 CS (optional) | 高階音色 |

**錄音訊號鏈標準:**
```
Guitar → Empress MKII → PA-1QG → [Optional OD] → Amp → XLR → Interface
```

---

### 舞台場景

| 音色需求 | 首選 Amp | Pedal 配置 | 理由 |
|---------|---------|-----------|------|
| **Clean Platform (Stereo)** | JC-22 | 完整 (11 個) | Stereo speakers + JC Chorus + 完整 OD stack |
| **Tube Class A** | Special 25 | 精簡 (6-7 個) | 內建 Drive channel + Class A 音色 |
| **需要 Stereo 空間感** | JC-22 (唯一選擇) | 完整 | Stereo FX loop + stereo speakers |
| **高增益 Rock** | Special 25 | Minimal | Drive channel "wild saturation" |

**舞台訊號鏈標準 (JC-22):**
```
Guitar → Empress MKII → PA-1QG → Buffer++ LOOP 1 [5 OD pedals] → JC-22 INPUT
                                                                      ↓
                                                                JC-22 FX SEND
                                                                      ↓
                                                       Buffer++ LOOP 2 [Stereo effects]
                                                                      ↓
                                                                JC-22 FX RETURN L/R
```

---

## Pedal 開關組合速查表

### JC-22 使用 (完整配置)

| 音樂類型 | KOT Yellow | KOT Red | Sweet Honey | Horsemeat | ODL-1 CS | Source Code |
|---------|-----------|---------|-------------|-----------|----------|-------------|
| **Jazz** | ✅ Clean | ❌ | ✅ Low | ❌ | ❌ | ❌ |
| **Neo Soul** | ✅ Clean | ❌ | ✅ Med | ✅ Boost | ❌ | ❌ |
| **Blues** | ❌ | ✅ OD | ✅ Low | ❌ | ❌ | ❌ |
| **Fusion** | ✅ Clean | ❌ | ❌ | ❌ | ✅ Normal | ❌ |
| **Classic Rock** | ❌ | ❌ | ❌ | ✅ On | ❌ | ✅ On |
| **Post Rock** | ✅ Clean | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Funk** | ✅ Clean | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Shoegaze** | ✅ OD | ✅ OD | ✅ Med | ❌ | ✅ Drive | ✅ On |
| **High Gain** | ❌ | ❌ | ❌ | ❌ | ✅ Drive | ✅ On |
| **Country** | ✅ Clean | ❌ | ❌ | ✅ Low | ❌ | ❌ |
| **Ambient** | ✅ Clean | ❌ | ❌ | ❌ | ❌ | ❌ |

**圖例:**
- ✅ = 開啟
- ❌ = 關閉
- Clean/OD/Drive = 模式或通道選擇
- Low/Med/High = Drive 設定

---

### Special 25 使用 (精簡配置)

| 音樂類型 | Amp Channel | Pedal 組合 | 數量 |
|---------|------------|-----------|------|
| **Jazz** | Clean | KOT Clean (optional) | 1 |
| **Neo Soul** | Clean | Sweet Honey | 1 |
| **Blues** | Drive (low) | Horsemeat boost | 1 |
| **Classic Rock** | Drive | Source Code (optional) | 0-1 |
| **Fusion** | Clean/Drive | ODL-1 CS | 1 |
| **High Gain** | Drive | Minimal 或無 | 0-1 |
| **Shoegaze** | Drive | ODL-1 Drive + Source Code | 2 |

---

## KOT 雙通道設定

### 推薦設定 A: Always-on + Switchable OD (最通用)

**用途:** 取代 Morning Glory，適合所有場景

```
Yellow Channel: Clean Mode (Always-on)
  - Volume: 高 (boost)
  - Drive: 低 (minimal distortion)
  - Tone: 12 點鐘
  - Footswitch: Always-on (或接 expression pedal volume)

Red Channel: OD Mode (Footswitch)
  - Volume: Unity 或略高
  - Drive: 中 (medium gain)
  - Tone: 12 點鐘
  - Footswitch: 需要 OD 時開啟

內部設定:
  - Yellow: Clean Mode (DIP switch 1: OFF, 2: OFF)
  - Red: OD Mode (DIP switch 3: OFF, 4: OFF)
  - Order: Yellow → Red (內部跳線)
```

---

### 推薦設定 B: Dual OD (疊加使用)

**用途:** 建構複雜音色，Blues / Fusion

```
Yellow Channel: OD Mode (Low gain)
  - Volume: Unity
  - Drive: 低 (light OD)
  - Tone: 11 點鐘
  - Footswitch: 可單獨或疊加

Red Channel: OD Mode (Medium gain)
  - Volume: Unity
  - Drive: 中 (medium OD)
  - Tone: 1 點鐘
  - Footswitch: 可單獨或疊加

內部設定:
  - Yellow: OD Mode
  - Red: OD Mode
  - Order: Yellow → Red
```

---

### KOT 18V Operation (可選)

**如果 pedalboard power supply 支援 18V:**
- 推薦使用 18V 供電
- 優點: 更大 headroom, 更清晰音色, 更 amp-like

---

## 特殊應用場景

### 場景 1: 錄音 - British Rock (Imperial)

**Amp:** Imperial MKII Lead channel
**Pedals:** Empress MKII + PA-1QG only

```
Guitar → Empress MKII → PA-1QG → Imperial MKII (Lead ch) → XLR → Interface
```

**理由:** Imperial 內建 British-voiced Lead channel 已足夠，無需外部 OD

---

### 場景 2: 錄音 - Dumble Fusion (DSM)

**Amp:** DSM Dumblifier OD channel
**Pedals:** Empress MKII + PA-1QG + ODL-1 CS (optional)

```
Guitar → Empress MKII → PA-1QG → ODL-1 CS (Normal, GLASS) → DSM (OD ch) → XLR → Interface
```

**理由:** Dumble on Dumble (超厚音色)

---

### 場景 3: 舞台 - Stereo Ambient (JC-22)

**Amp:** JC-22 Stereo FX Loop
**Pedals:** KOT Yellow Clean + Nucleo + AASB + FF-1Y (全部 stereo)

```
Guitar → Empress MKII → PA-1QG → KOT (Yellow Clean) → JC-22 INPUT
                                                         ↓
                                                   JC-22 FX SEND
                                                         ↓
                                           Buffer++ LOOP 2 (Stereo):
                                           FF-1Y → Nucleo → AASB
                                                         ↓
                                                   JC-22 FX RETURN L/R
                                                         ↓
                                                   JC-22 Stereo Speakers
```

**重點:** 完整發揮 JC-22 stereo speakers，Nucleo stereo reverb 完整 imaging

---

### 場景 4: 舞台 - High Gain (Special 25)

**Amp:** Special 25 Drive channel
**Pedals:** Minimal

```
Guitar → Empress MKII → PA-1QG → Special 25 (Drive ch, wild saturation)
```

**理由:** Special 25 Drive channel 本身可達 "wild saturation"，外部 pedals 可選

---

## 快速故障排除

### 問題 1: 音色太冷/太亮 (JC-22)

**解決方案:**
- 開啟 Sweet Honey (提供溫暖感)
- Horsemeat Voice control 轉 CCW (更 saturated/meaty)
- PA-1QG 削減高頻

---

### 問題 2: 需要更多 sustain (Post Rock)

**解決方案:**
- Empress MKII: INPUT 提高, RATIO 4:1 或 10:1
- Empress MKII: MIX 降低 (平行壓縮保留動態)
- Sweet Honey 低 Drive 設定 (溫暖 sustain)

---

### 問題 3: 需要 Fender Blackface 音色 (Country)

**解決方案 (Blacklon 被淘汰):**
- 用 ODL-1 CS Normal + GLASS mode (類似 Fender Vibroverb)
- 用 Sweet Honey 提供溫暖感
- 或接受 JC-22 就是 clean platform

---

### 問題 4: Stereo reverb 不夠寬 (Ambient)

**解決方案:**
- 確認 Buffer++ LOOP 2 是 stereo 模式
- 確認 Nucleo 設定為 stereo output
- 確認 JC-22 FX RETURN L/R 都有連接
- Nucleo stereo width 調到最大

---

### 問題 5: 高增益時噪音太多

**解決方案:**
- PA-1QG 放在最前面 (Always-on foundation)
- 檢查導線品質
- Buffer++ Dolby-style noise filtering
- ODL-1 CS HI CUT 控制高頻噪音

---

## 附錄: Pedal 控制快速參考

### Empress MKII 控制

```
INPUT:   輸入增益 → 觸發壓縮閾值
OUTPUT:  輸出電平補償 (可做 boost)
ATTACK:  壓縮啟動速度
RELEASE: 壓縮恢復速度 (50ms-1s)
MIX:     平行壓縮混合 (100% = 全壓縮)
TONE:    Tilt EQ (500Hz 中心, CW = 提升高頻)
RATIO:   2:1 / 4:1 / 10:1 切換
SC HPF:  Sidechain 高通濾波器 (120Hz / OFF / 240Hz)
```

---

### PA-1QG 控制

```
10-band EQ: 31.25Hz, 62.5Hz, 125Hz, 250Hz, 500Hz, 1kHz, 2kHz, 4kHz, 8kHz, 16kHz
LEVEL:      輸出音量 (可做 clean boost)
```

---

### KOT 控制

```
Yellow Channel:
  - Volume, Drive, Tone
  - Mode: OD / Clean / Dist (內部 DIP switch)

Red Channel:
  - Volume, Drive, Tone
  - Mode: OD / Clean / Dist (內部 DIP switch)

內部設定:
  - DIP switch 1-2: Yellow channel mode
  - DIP switch 3-4: Red channel mode
  - Treble Trimpot: 內部高頻微調
  - Order jumper: Yellow → Red 或 Red → Yellow
```

---

### Horsemeat 控制

```
Level:   輸出音量
Gain:    從 clean boost 到 medium-high OD
Voice:   核心音色塑造 (CCW = saturated/meaty, CW = glassy/singing)
Treble:  高頻 cut/boost
Bass:    低頻 cut/boost
```

---

### Sweet Honey 控制

```
Volume:  輸出音量
Drive:   增益量控制
Focus:   動態響應與 EQ (CCW = 需用力彈奏, CW = 更早失真)
Treble:  高頻控制 (post-gain)
Bass:    低頻控制 (pre-gain)
```

---

### ODL-1 CS 控制

```
Normal Channel:
  - NOR LEVEL, TONE, GAIN
  - EQ Switch: EQ ON / GLASS
  - ROCK/JAZZ Switch

Drive Channel:
  - DRV LEVEL, DRIVE, PUSH, HI CUT

Switches:
  - EQ ON: 啟動 Tone circuit
  - GLASS: Bypass Tone (Fender Vibroverb-like bright)
  - ROCK: 增加 gain, 略削減低頻
  - JAZZ: 降低 gain, 強調低頻豐富度
```

---

### Source Code 控制

```
Level:   輸出音量
Drive:   增益量控制
Tone:    音色控制
Bite:    調整 odd/even-order harmonics (CCW = symmetrical, CW = asymmetrical)
```

---

## 版本歷史

**v1.0 - 2026-01-14**
- 初版發布
- 11 種音樂類型 presets
- 完整 pedal 設定建議
- Amp 選擇指南
- KOT 雙通道設定
- 快速故障排除

---

**最後更新:** 2026-01-14
**配置:** Empress MKII + PA-1QG + KOT + Horsemeat + Sweet Honey + ODL-1 CS + Source Code + FF-1Y + Nucleo + AASB + Buffer++
**Amps:** Imperial MKII + DSM Dumblifier + JC-22 + Special 25

**快速參考原則:** 所有設定都是起點，請根據實際吉他/音箱/場地調整。
