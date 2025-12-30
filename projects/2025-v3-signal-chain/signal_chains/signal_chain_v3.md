# Emil 吉他訊號鏈配置 - 版本三 (V3.0)

**版本:** 3.0
**更新日期:** 2025-12-30
**基於:** V2.0 (2025-12-30) 進一步調整

---

## V3.0 更新摘要

### 相較於 V2.0 的關鍵變更

**移除效果器：**
- ❌ **Cornerstone Colosseum** ($380)
  - 理由：簡化訊號鏈，用單功能專用效果器取代雙通道設計

**新增效果器：**
- ✅ **PRS Horsemeat** (取代 Colosseum Klon Side)
  - 角色：訊號鏈1的透明 Boost
  - 特性：極度透明的 Klon-style Overdrive

- ✅ **JHS Morning Glory V3** (取代 Colosseum BB Side)
  - 角色：訊號鏈2的 Bluesbreaker Overdrive
  - 特性：經典 BB 音色，無 clipping 問題

---

## V3.0 核心效果器清單（10顆）

### 【Compressor】2顆
1. ✅ **Empress MKII** ($219)
   - 訊號鏈1主力壓縮器

2. ✅ **Origin Effects Cali76 FET** ($369)
   - 訊號鏈2主力壓縮器

---

### 【EQ + Clean Boost】1顆
3. ✅ **Free the Tone PA-1QG** ($425)
   - EQ + LEVEL 功能（Clean Boost）
   - 99預設，MIDI 支援

---

### 【Overdrive/Drive】5顆
4. ✅ **Mad Professor Sweet Honey Deluxe** ($220)
   - 訊號鏈1核心溫暖 OD

5. ✅ **PRS Horsemeat**
   - **V3.0 新增**：取代 Colosseum Klon Side
   - 訊號鏈1透明 Boost
   - Klon-style 透明推動

6. ✅ **JHS Morning Glory V3**
   - **V3.0 新增**：取代 Colosseum BB Side
   - 訊號鏈2 Bluesbreaker OD
   - 經典 BB 音色

7. ✅ **Roshi Blacklon** ($200)
   - 訊號鏈2 Amp-in-a-Box（Blackface 模擬）

8. ✅ **TWA Source Code** ($299)
   - 訊號鏈2 TS Evolution（中頻突出）

9. ✅ **Free the Tone ODL-1-CS** ($425)
   - 訊號鏈2 Dumble 雙通道（高階音色）

---

### 【Delay】1顆
10. ✅ **Free the Tone FT-1Y** ($400)
    - 兩條訊號鏈共用
    - Realtime BPM Analyzer

---

### 【Reverb】2顆
11. ✅ **Cornerstone Nucleo** ($350)
    - 兩條訊號鏈共用
    - Stereo 主 Reverb

12. ✅ **Lichtlaerm AASB** ($225)
    - 訊號鏈2特殊音景
    - Shimmer/Drone 雙向八度

---

## 完整訊號鏈設計 V3.0

### 訊號鏈 1：Jazz / Neo Soul / Funk 專用

**目標音樂類型**：Jazz, Neo Soul, Funk, Pop Rock
**主要吉他**：Greco TE-500, Fender Tokyo Thinline, ESP Throbber-CTM
**主要音箱**：Roland JC-22
**評分**：★★★★★ (98/100)

#### 完整 4-Cable Method 配置

```
🎸 吉他（選擇對應 Preset）
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【前級鏈 - 進音箱 Input】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↓
① Empress MKII Compressor
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • INPUT: 低 (1-2 LED)                │
   │ • RATIO: 2:1                         │
   │ • ATTACK: 快                         │
   │ • RELEASE: 中                        │
   │ • TILT EQ: 12點鐘（正午）            │
   │ • MIX: 80-100%                       │
   │ • OUTPUT: 正常                       │
   ├─────────────────────────────────────┤
   │ 目的：極度透明動態控制               │
   │ 效果：保持撥弦動態，輕微控制峰值     │
   └─────────────────────────────────────┘
  ↓
② Free the Tone PA-1QG
   ┌─────────────────────────────────────┐
   │ 功能：EQ + LEVEL (Clean Boost)       │
   ├─────────────────────────────────────┤
   │ Preset 配置：                        │
   │                                      │
   │ • Preset 1: ESP EC-CTM               │
   │   - LEVEL: 0dB（高輸出不需 Boost）   │
   │   - EQ: 提升 800Hz-3.2kHz           │
   │                                      │
   │ • Preset 2: Greco TE-500             │
   │   - LEVEL: +3dB（中等輸出適度 Boost）│
   │   - EQ: 提升 800Hz-3.2kHz           │
   │                                      │
   │ • Preset 3: ESP Throbber-CTM         │
   │   - LEVEL: +6dB（低輸出需較大 Boost）│
   │   - EQ: 平衡中頻                    │
   │                                      │
   │ • Preset 4: Fender Tokyo Thinline    │
   │   - LEVEL: +4dB（中等輸出適度 Boost）│
   │   - EQ: 提升中高頻                  │
   ├─────────────────────────────────────┤
   │ 目的：                               │
   │ 1. EQ 調整（為每把吉他建立專用 EQ）  │
   │ 2. Clean Boost（LEVEL 線性放大）    │
   │ 效果：針對不同吉他輸出補償音量       │
   └─────────────────────────────────────┘
  ↓
③ Mad Professor Sweet Honey Overdrive Deluxe
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • DRIVE: 11-12點鐘                   │
   │ • FOCUS: 1-2點鐘（Neo Soul 甜蜜點）  │
   │ • VOLUME: 12-1點鐘                   │
   │ • TONE: 12點鐘                       │
   ├─────────────────────────────────────┤
   │ 目的：溫暖 Neo Soul 核心音色         │
   │ 效果：低至中等增益，溫暖甜美         │
   └─────────────────────────────────────┘
  ↓
④ PRS Horsemeat
   ┌─────────────────────────────────────┐
   │ ⭐ V3.0 關鍵變更：取代 Colosseum Klon  │
   ├─────────────────────────────────────┤
   │ 設定：                               │
   │ • DRIVE: 9-10點鐘（低 Gain）         │
   │ • VOLUME: 2點鐘（Boost 模式）        │
   │ • TONE: 12-1點鐘                     │
   ├─────────────────────────────────────┤
   │ 目的：Klon-style 透明 Boost          │
   │ 效果：推動前面 Sweet Honey OD        │
   │ 特性：極度透明，增加中頻穿透力       │
   └─────────────────────────────────────┘
  ↓
🎛️ Roland JC-22 Input
   ┌─────────────────────────────────────┐
   │ 音箱設定：                           │
   │ • VOLUME: 5-6                        │
   │ • TREBLE: 6                          │
   │ • MIDDLE: 5                          │
   │ • BASS: 5-6                          │
   │ • CHORUS: ON                         │
   │   - SPEED: 3-4                       │
   │   - DEPTH: 4-5                       │
   │ • BRIGHT: 視吉他決定                 │
   └─────────────────────────────────────┘
  ↓
JC-22 前級處理 → Send (Stereo L+R)
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【Effects Loop - Stereo】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↓
⑤ Free the Tone FT-1Y Delay
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • MODE: Digital                      │
   │ • TIME: 視曲目（建議 1/4 note）      │
   │ • FEEDBACK: 3-4 repeats              │
   │ • MIX: 20-40%                        │
   │ • REALTIME BPM ANALYZER: ON          │
   ├─────────────────────────────────────┤
   │ 目的：精準 BPM 同步 Delay            │
   │ 效果：自動偵測節奏，精準同步         │
   └─────────────────────────────────────┘
  ↓
⑥ Cornerstone Nucleo Reverb (Stereo)
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • MODE: Room/Hall（視場景）          │
   │ • DECAY: 30-50%                      │
   │ • BLEND: 30-50%                      │
   │ • VOICING: Normal                    │
   │ • OUTPUT: Stereo L+R                 │
   │ • RIGHT OUTPUT: Transformer-Isolated │
   │   （避免 Ground Loop）               │
   ├─────────────────────────────────────┤
   │ 目的：Stereo 主 Reverb               │
   │ 效果：豐富空間感，Stereo 寬度        │
   └─────────────────────────────────────┘
  ↓
🎛️ JC-22 Return (Stereo L+R) → JC-22 Output
```

#### 效果器使用統計

| 效果器 | 使用率 | 角色 |
|--------|--------|------|
| Empress MKII | 95% | 透明壓縮 |
| PA-1QG | 100% | EQ + Clean Boost |
| Sweet Honey | 90% | 核心 OD 音色 |
| PRS Horsemeat | 80% | 透明 Klon Boost |
| FT-1Y | 100% | 主 Delay |
| Nucleo | 95% | 主 Reverb |

**總計**：6顆效果器（前級4顆 + Loop 2顆）

---

### 訊號鏈 2：Post Rock / Fusion / Ambient 專用

**目標音樂類型**：Post Rock, Fusion, Ambient, Alternative Rock, Classic Rock
**主要吉他**：ESP EC-CTM, Greco TE-500
**主要音箱**：Tone King Imperial MKII 或 Roland JC-22
**評分**：★★★★★ (96/100)

#### 完整 4-Cable Method 配置

```
🎸 吉他（ESP EC-CTM 或 Greco TE-500）
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【前級鏈 - 進音箱 Input】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↓
① Origin Effects Cali76 FET
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • IN: 中（5-6 LED）                  │
   │ • ATTACK: 快                         │
   │ • RELEASE: 中                        │
   │ • RATIO: 固定 1176 風格              │
   │ • DRY: 70-80%（混入原始訊號）        │
   ├─────────────────────────────────────┤
   │ 目的：                               │
   │ 1. 增加 Sustain（Post Rock 延音）    │
   │ 2. 染色增添管機感                    │
   │ 3. DRY 混合保留撥弦動態              │
   │ 效果：溫暖圓潤，延音豐富             │
   └─────────────────────────────────────┘
  ↓
② Free the Tone PA-1QG
   ┌─────────────────────────────────────┐
   │ Preset 配置：                        │
   │                                      │
   │ • Preset 5: ESP EC-CTM (Post Rock)   │
   │   - LEVEL: 0dB（高輸出不需 Boost）   │
   │   - EQ: 提升 100Hz-400Hz（厚度）    │
   │                                      │
   │ • Preset 6: Greco TE-500 (Post Rock) │
   │   - LEVEL: +3dB（中等輸出適度 Boost）│
   │   - EQ: 提升低頻與中高頻            │
   │                                      │
   │ • Preset 7: Solo Boost（通用）       │
   │   - LEVEL: +9dB（大音量 Solo）       │
   │   - EQ: 平坦或提升 800Hz-3.2kHz     │
   ├─────────────────────────────────────┤
   │ 目的：EQ 調整 + 視需求 Boost         │
   └─────────────────────────────────────┘
  ↓
③ Roshi Blacklon (Amp-in-a-Box)
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • TUBE: 6L6 Mode（Post Rock）        │
   │         6V6 Mode（Neo Soul）         │
   │ • TONE: Drive Mode（增益模式）       │
   │         Mellow Mode（溫暖模式）      │
   │ • DRIVE: 11-1點鐘                    │
   │ • VOLUME: 12-1點鐘                   │
   ├─────────────────────────────────────┤
   │ 目的：Blackface 管機模擬             │
   │ 效果：讓 JC-22 晶體機有管機感        │
   │ 用途：                               │
   │ • 6L6 + Drive = Post Rock Crunch     │
   │ • 6V6 + Mellow = Neo Soul 溫暖       │
   └─────────────────────────────────────┘
  ↓
④ JHS Morning Glory V3
   ┌─────────────────────────────────────┐
   │ ⭐ V3.0 關鍵變更：取代 Colosseum BB    │
   ├─────────────────────────────────────┤
   │ 設定：                               │
   │ • GAIN: 10-12點鐘                    │
   │ • VOLUME: 12-1點鐘                   │
   │ • TONE: 12點鐘                       │
   │ • SWITCH: 根據需求選擇模式           │
   ├─────────────────────────────────────┤
   │ 目的：Bluesbreaker Overdrive         │
   │ 效果：經典 BB 音色，開放清晰         │
   │ 特性：無 clipping 問題，動態自然     │
   └─────────────────────────────────────┘
  ↓
⑤ TWA Source Code (TS Evolution)
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • DRIVE: 10-12點鐘                   │
   │ • TONE: 12-1點鐘                     │
   │ • VOLUME: 12點鐘                     │
   │ • BITE CONTROL: 調整諧波平衡         │
   │   - 逆時針：偶次諧波（溫暖）         │
   │   - 順時針：奇次諧波（明亮）         │
   ├─────────────────────────────────────┤
   │ 目的：                               │
   │ 1. TS-style 中頻突出（800Hz-1.5kHz） │
   │ 2. Bite Control 微調諧波            │
   │ 3. 18V 升壓提供大 headroom           │
   │ 使用時機：                           │
   │ • Classic Rock 需要 TS 中頻時開啟    │
   │ • 其他風格可 Bypass                  │
   │ 效果：TS 特有中頻穿透力              │
   └─────────────────────────────────────┘
  ↓
⑥ Free the Tone ODL-1-CS (Dumble)
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • CHANNEL: Drive Channel             │
   │ • VOLTAGE: 14-16V                    │
   │ • MODE: ROCK Mode                    │
   │ • DRIVE: 10-1點鐘                    │
   │ • VOLUME: 12點鐘                     │
   │ • TONE: 12點鐘                       │
   ├─────────────────────────────────────┤
   │ 目的：Dumble 高階音色                │
   │ 效果：Fusion 經典音色                │
   │ （Larry Carlton, Robben Ford 風格）  │
   └─────────────────────────────────────┘
  ↓
🎛️ 音箱 Input
   ┌─────────────────────────────────────┐
   │ Imperial MKII:                       │
   │ • Lead Channel, Mid-Bite ON          │
   │ 或                                   │
   │ JC-22:                               │
   │ • Volume 6-7, Bright ON              │
   └─────────────────────────────────────┘
  ↓
音箱前級處理 → Send
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【Effects Loop】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↓
⑦ Free the Tone FT-1Y Delay
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • MODE: Analog/Digital（視需求）     │
   │ • TIME: 長 Delay（1/2, 1/1 note）    │
   │ • FEEDBACK: 高（建構 Ambient Pad）   │
   │ • MIX: 40-70%                        │
   │ • HOLD: 開啟（建構音景層次）         │
   ├─────────────────────────────────────┤
   │ 目的：                               │
   │ 1. 精準 BPM 同步                     │
   │ 2. Hold 功能建構 Pad                 │
   │ 效果：Post Rock 音景層次             │
   └─────────────────────────────────────┘
  ↓
⑧ Lichtlaerm AASB Shimmer Reverb
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • MODE: Above（高八度）              │
   │         Both（雙向八度）             │
   │ • MIX: 60-90%（大比例 Wet）          │
   │ • DECAY: 長                          │
   │ • FREEZE: 開啟（凍結音景）           │
   ├─────────────────────────────────────┤
   │ 目的：雙向八度 Shimmer/Drone         │
   │ 效果：天堂與地底碰撞的音景           │
   └─────────────────────────────────────┘
  ↓
⑨ Cornerstone Nucleo
   ┌─────────────────────────────────────┐
   │ 設定：                               │
   │ • MODE: Reactor（核電廠模式）        │
   │ • DECAY: 60-90秒（極長）             │
   │ • BLEND: 50-80%                      │
   │ • FREEZE: 開啟（凍結音景）           │
   ├─────────────────────────────────────┤
   │ 目的：核電廠空間感                   │
   │ 效果：建構複雜 Post Rock 音景        │
   │ 用法：                               │
   │ • AASB + Nucleo 雙 Freeze            │
   │ • 建立多層次音景                     │
   └─────────────────────────────────────┘
  ↓
🎛️ 音箱 Return → Output
```

#### 效果器使用統計

| 效果器 | 使用率 | 角色 |
|--------|--------|------|
| Cali76 FET | 80% | 染色壓縮 + Sustain |
| PA-1QG | 95% | EQ 調整 |
| Roshi Blacklon | 75% | 管機模擬 |
| Morning Glory | 85% | Bluesbreaker OD |
| TWA Source Code | 60% | TS 中頻（Classic Rock 時） |
| ODL-1-CS | 70% | Dumble 高階音色 |
| FT-1Y | 100% | 主 Delay + Hold |
| AASB | 50% | Shimmer/Drone |
| Nucleo | 95% | 主 Reverb |

**總計**：9顆效果器（前級6顆 + Loop 3顆）

---

## V3.0 與 V2.0 對比分析

### 訊號鏈1變更

**V2.0**：
```
Empress MKII → PA-1QG → Sweet Honey → Colosseum Klon Side → JC-22
```

**V3.0**：
```
Empress MKII → PA-1QG → Sweet Honey → PRS Horsemeat → JC-22
```

**改進**：
- ✅ **PRS Horsemeat 專注單一功能**：專業 Klon-style Boost，無其他通道干擾
- ✅ **訊號鏈更單純**：每顆效果器只有一個核心角色
- ⚠️ **失去 Colosseum Clean Control**：Horsemeat 可能沒有混合乾訊號功能

---

### 訊號鏈2變更

**V2.0**：
```
Cali76 FET → PA-1QG → Roshi Blacklon → Colosseum (BB+Klon雙通道) → TWA Source Code → ODL-1-CS
```

**V3.0**：
```
Cali76 FET → PA-1QG → Roshi Blacklon → Morning Glory → TWA Source Code → ODL-1-CS
```

**改進**：
- ✅ **Morning Glory 經典 BB 音色**：無 clipping 問題，動態自然
- ✅ **訊號鏈更直觀**：BB OD 專注於 BB 角色
- ⚠️ **失去 Klon + BB 疊加組合**：V2.0 的 Colosseum 可同時使用 Klon 和 BB 通道
- ⚠️ **失去 Clip Blender 功能**：Colosseum 獨特的 clipping 混合功能

---

## V3.0 優勢與考量

### ✅ 優勢

1. **專注性更高**
   - 每顆效果器只負責一種核心音色
   - 訊號鏈更簡單易懂

2. **Morning Glory 回歸**
   - V1.0 原本因 Colosseum 而移除
   - 經典 BB 音色，無 clipping 問題

3. **PRS Horsemeat Klon 專業化**
   - 專業 Klon-style 設計
   - 透明度可能更高

### ⚠️ 考量點

1. **失去 Colosseum 雙通道彈性**
   - V2.0 可在訊號鏈2同時使用 BB + Klon
   - V3.0 只有 Morning Glory BB OD

2. **失去 Clip Blender 創意功能**
   - Colosseum 的 Clip Blender 可混合兩側 clipping
   - 創造獨特音色層次

3. **效果器數量未減少**
   - 移除1顆（Colosseum）
   - 新增2顆（Horsemeat + Morning Glory）
   - 實際上增加1顆效果器

---

## 財務分析

### V3.0 相對於 V2.0 的成本變化

**移除**：
- ❌ Cornerstone Colosseum：-$380

**新增**：
- ✅ PRS Horsemeat：+$？（請提供價格）
- ✅ JHS Morning Glory V3：+$150-180

**淨變化**：
- 需要根據 Horsemeat 價格計算
- 如果 Horsemeat = $150，淨支出 ≈ -$80 to -$50 USD（省錢）
- 如果 Horsemeat > $230，淨支出為正（多花錢）

---

## 實施建議

### 如果您已有 Horsemeat 和 Morning Glory

**立即可行動**：
1. [ ] 從 Pedalboard 移除 Colosseum
2. [ ] 在訊號鏈1的 Sweet Honey 後加入 Horsemeat
3. [ ] 在訊號鏈2的 Blacklon 後加入 Morning Glory
4. [ ] 測試新訊號鏈配置

### 如果需要購買 Horsemeat

**建議先測試**：
1. [ ] 保留 Colosseum 作為備用
2. [ ] 先購買 Horsemeat 或 Morning Glory 其中一顆測試
3. [ ] 確認音色符合預期後再移除 Colosseum

---

## 總結

**V3.0 核心理念**：
- 🎯 **專注性**：每顆效果器一個核心角色
- 🎯 **經典音色**：Morning Glory BB + Horsemeat Klon
- 🎯 **訊號鏈簡化**：單通道效果器組合，無雙通道複雜性

**最適合的情境**：
- ✅ 您偏好單功能專用效果器
- ✅ 您喜歡 Morning Glory 的經典 BB 音色
- ✅ 您不需要 Colosseum 的 Clip Blender 創意功能

**建議保留 V2.0 如果**：
- ⚠️ 您喜歡 Colosseum 雙通道的彈性（BB + Klon 同時使用）
- ⚠️ Clip Blender 功能對您很重要
- ⚠️ 您想減少效果器數量（V2.0 用1顆抵2顆）
