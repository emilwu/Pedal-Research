# Emil 訊號鏈配置完整指南

**版本:** 1.0
**建立日期:** 2025-12-13
**適用範圍:** 4把吉他 × 2個音箱 × 17顆效果器 → 最佳訊號鏈配置

---

## 目錄
1. [設備總覽](#設備總覽)
2. [功能重疊分析](#功能重疊分析)
3. [訊號鏈1：Jazz/Neo Soul專用](#訊號鏈1jazzneo-soul專用)
4. [訊號鏈2：Post Rock/Fusion專用](#訊號鏈2post-rockfusion專用)
5. [最終黃金組合](#最終黃金組合)
6. [移除與Tier 2建議](#移除與tier-2建議)
7. [音樂類型快速參考](#音樂類型快速參考)
8. [供電與Pedalboard配置](#供電與pedalboard配置)
9. [4-Cable Method詳解](#4-cable-method詳解)

---

## 設備總覽

### 吉他收藏（4把）

| 吉他 | 拾音器 | 輸出類型 | 最佳風格 |
|------|--------|----------|----------|
| ESP EC-CTM | EMG JH HET SET (主動) | 高輸出 13.5k/10.5k | Modern Rock, Metal, Progressive |
| ESP Throbber-CTM | SD APH-1 PAF (被動) | 中等 7.75k/8.0k | Jazz, Blues, Classic Rock |
| Greco TE-500 | Lindy Fralin Wide Range (被動) | 中高 7.5-9.0k | Neo Soul, Funk, Classic Rock |
| Fender Tokyo Thinline | SD SP90-1 P90 (被動) | 中高 8.0-9.0k | Neo Soul, Jazz, Fusion, Pop Rock |

### 音箱配置（2台，都支援4-Cable Method）

**Tone King Imperial MKII**
- 類型：20W 管機
- 通道：Rhythm (Blackface) + Lead (Tweed)
- Effects Loop：Send/Return
- 特殊功能：Ironman II衰減器（5段），內建Reverb + Tremolo
- 最佳風格：Jazz, Blues, Classic Rock, Vintage-oriented Neo Soul

**Roland JC-22**
- 類型：30W 立體聲晶體機
- 內建效果：Dimensional Space Chorus, Stereo Reverb
- Effects Loop：Stereo Send/Return（Series/Parallel切換）
- 特殊功能：耳機輸出，Line Out
- 最佳風格：Neo Soul, Funk, Modern Jazz, Post Rock, Pop Rock

### 效果器清單（17顆）

**Compressor (2)**
1. Origin Effects Cali76 FET - 1176風格，輕微染色
2. Empress MKII - 極度透明，Tilt EQ

**EQ (2)**
3. Boss GE-7 - 7-band Graphic EQ
4. Free the Tone PA-1QG - 10-band Programmable, 99預設

**Overdrive (10)**
5. Mad Professor Sweet Honey Overdrive Deluxe - 溫暖Low-Medium Gain
6. JHS Morning Glory V3 - 透明Bluesbreaker
7. EHX Soul Food - Klon Clone
8. TWA Source Code - TS Evolution, Bite Control
9. From Yesterday (KOT Clone) - 雙通道極度透明
10. Cornerstone Colosseum - BB + Klon雙通道
11. Virtues Arca - BB-like有顆粒感
12. Roshi Blacklon - Amp-in-a-Box (Fender Blackface)
13. Free the Tone ODL-1-CS - Dumble-style雙通道
14. PRS Horsemeat - 透明Germanium

**Delay (1)**
15. Free the Tone FT-1Y - Realtime BPM Analyzer

**Reverb (2)**
16. Cornerstone Nucleo - Stereo Reverb, Freeze
17. Lichtlaerm AASB - Shimmer Reverb雙向八度

---

## 功能重疊分析

### ⚠️ 嚴重重疊（需要決策）

#### 1. 透明Overdrive重疊（4顆）
- **JHS Morning Glory V3** - 極度透明Bluesbreaker
- **From Yesterday (KOT Clone)** - 雙通道極度透明
- **EHX Soul Food** - 透明Klon Clone
- **PRS Horsemeat** - 透明但溫暖Germanium

**分析：**
- From Yesterday (KOT) 雙通道可單獨取代 Morning Glory
- Morning Glory 與 KOT 功能100%重疊
- Soul Food 與 Horsemeat 都是Klon-inspired

**決策：**
- ❌ **移除 JHS Morning Glory V3** - From Yesterday完全取代
- ✅ **保留 From Yesterday (KOT)** - 雙通道，三種模式
- ✅ **保留 EHX Soul Food** - 便宜實用Clean Boost
- 📦 **Horsemeat移至Tier 2** - Germanium溫暖是獨特價值

#### 2. Bluesbreaker風格重疊（3顆）
- **JHS Morning Glory V3** - BB改良
- **Cornerstone Colosseum (BB Side)** - BB無clipping diodes改良
- **Virtues Arca** - BB-like有顆粒感

**分析：**
- Colosseum已包含BB side且功能更好
- Virtues Arca 與 Colosseum BB side功能80%重疊

**決策：**
- ❌ **移除 Virtues Arca** - Colosseum BB Side更優
- ✅ **保留 Cornerstone Colosseum** - BB + Klon雙通道高效

#### 3. EQ功能重疊（2顆）
- **Boss GE-7** - 7-band簡單實用
- **Free the Tone PA-1QG** - 10-band, 99預設，MIDI

**分析：**
- PA-1QG完全包含GE-7功能並超越
- GE-7存在意義僅剩「簡單」與「便宜」

**決策：**
- 📦 **GE-7移至Tier 2** - 作為PA-1QG備份
- ✅ **保留 PA-1QG** - 核心EQ，99預設為每把吉他建立專用設定

#### 4. Compressor功能相似（2顆）
- **Cali76 FET** - 1176風格，輕微染色
- **Empress MKII** - 極度透明

**分析：**
- 兩者都是FET壓縮，但音色取向不同
- Cali76偏染色，Empress偏透明

**決策：**
- ✅ **保留兩者** - Empress適合Clean-focused，Cali76適合Post Rock/Ambient

#### 5. Reverb功能部分重疊（2顆）
- **Cornerstone Nucleo** - Stereo Reverb, Shimmer (AIR功能)
- **Lichtlaerm AASB** - Shimmer Reverb雙向八度, Mono

**分析：**
- Nucleo的AIR可做Shimmer（高八度）
- AASB獨特的Below（低八度）與Both（雙向）是Nucleo沒有的
- Nucleo是**Stereo**，AASB是**Mono**

**決策：**
- ✅ **保留兩者** - Nucleo主Reverb，AASB特殊Shimmer/Drone

---

## 訊號鏈1：Jazz/Neo Soul專用

### 目標音樂類型
Jazz, Neo Soul, Funk, Pop Rock

### 主要吉他
- Greco TE-500 (Wide Range + JC-22 = Neo Soul教科書)
- Fender Tokyo Thinline (P90 + JC-22 = 現代流行標準)
- ESP Throbber-CTM (PAF + Imperial MKII = Wes Montgomery Tone)

### 主要音箱
Roland JC-22 (利用內建Stereo Chorus)

### 4-Cable Method 配置

```
🎸 吉他
  ↓
【前級鏈 - 進音箱Input】
  ↓
① Empress MKII Compressor
   - INPUT: 低（輕微壓縮1-2 LED）
   - ATTACK: 中
   - RELEASE: 中至快
   - MIX: 80-100%
   - TONE: 正午（平坦）
   - RATIO: 2:1
   - Sidechain HPF: 120Hz或OFF
  ↓
② Free the Tone PA-1QG
   - Preset 1: Greco TE-500專用EQ
   - Preset 2: Fender Tokyo Thinline專用EQ
   - Preset 3: ESP Throbber-CTM專用EQ
   - Preset 4: Solo Boost (+6dB)
  ↓
③ From Yesterday (KOT Clone)
   - Yellow側: Clean Mode (Clean Boost)
   - Red側: OD Mode (備用中等增益)
   - Yellow Volume: 略高於Unity
   - Yellow Drive: 低至中
  ↓
④ Mad Professor Sweet Honey Overdrive Deluxe
   - Volume: 3點鐘（Unity或略高）
   - Drive: 11-12點鐘（低至中增益）
   - Focus: 1-2點鐘（Neo Soul甜蜜點）
   - Bass: 12-1點鐘
   - Treble: 12點鐘
  ↓
⑤ EHX Soul Food
   - Drive: 9-10點鐘（低增益）
   - Volume: 2-3點鐘（Clean Boost）
   - Treble: 11-12點鐘
   - 用途：推動前面的OD但不染色
  ↓
🎛️ Roland JC-22 Input
   - Volume: 5-6
   - Treble: 5-6
   - Bass: 5-6
   - Chorus Speed: 3-4
   - Chorus Depth: 4-5
   - Reverb: 2-3（因Loop中還有Nucleo）
   - Bright Switch: 依吉他調整
  ↓
JC-22 前級處理 → Send (Stereo)
  ↓
【Effects Loop - Send/Return之間】
  ↓
⑥ Free the Tone FT-1Y Delay
   - Realtime BPM Analyzer: ON
   - Tap Tempo輸入大概BPM
   - 演奏時自動微調至實際速度
   - Time Offset: 依需求微調
   - Feedback: 30-50%（Neo Soul/Jazz）
   - Mix: 20-40%
   - LPF/HPF: 依需求調整
  ↓
⑦ Cornerstone Nucleo Reverb (Stereo)
   - Mode: Room（親密空間）或 Hall（寬廣大廳）
   - Voicing: Normal（清晰現代）
   - Blend: 30-50%
   - Decay: 中等（1-3秒）
   - Tone: 正午
   - MOD: 細微（增添深度）
   - AIR: 關閉或極低（除非需要Shimmer）
   - FLUX: 關閉
   - **Stereo Output → JC-22 Return L+R**
  ↓
🎛️ JC-22 Return → 後級 → Stereo Output
```

### 音色策略

**Clean Tone（Jazz/Neo Soul）**
- 關閉所有OD
- 僅Empress MKII + PA-1QG + JC-22 Clean
- JC-22 Chorus ON，Blend 30-40%
- Nucleo Room模式，短Decay

**Neo Soul Rhythm**
- Sweet Honey低增益（Drive 11-12點鐘）
- Focus 1-2點鐘（溫暖甜美）
- Soul Food關閉或極低增益Boost
- FT-1Y短Delay（BPM同步）

**Funk Spank**
- From Yesterday Yellow Clean Mode
- PA-1QG提升800Hz-3.2kHz（穿透力）
- JC-22 Bright Switch ON
- FT-1Y短Delay（增添空間感）

**Jazz Lead**
- Sweet Honey或KOT Yellow
- 使用吉他Neck拾音器
- Nucleo Hall模式
- FT-1Y細微Delay

### 為何選這些效果器？

- **Empress MKII:** 極度透明，不破壞JC-22的Clean特性
- **PA-1QG:** 可為三把主要吉他儲存專用EQ，MIDI整合
- **From Yesterday (KOT):** 雙通道極度透明，可Clean/OD切換
- **Sweet Honey:** 溫暖、Touch-sensitive，完美適合Neo Soul
- **Soul Food:** Klon透明Boost，推動前面的OD但不染色
- **FT-1Y:** Stereo Loop中提供精準Delay，BPM Analyzer同步節奏
- **Nucleo:** Stereo Reverb完美適合JC-22，Room/Hall模式自然

---

## 訊號鏈2：Post Rock/Fusion專用

### 目標音樂類型
Post Rock, Fusion, Ambient, Alternative Rock, Classic Rock

### 主要吉他
- ESP EC-CTM (高輸出主動拾音器，Post Rock完美)
- Greco TE-500 (Wide Range，Fusion/Classic Rock)

### 主要音箱
Tone King Imperial MKII 或 Roland JC-22（依需求）

### 4-Cable Method 配置

```
🎸 吉他
  ↓
【前級鏈 - 進音箱Input】
  ↓
① Origin Effects Cali76 FET
   - IN: 中（觸發3-5 LED）
   - OUT: Unity或略高（補償）
   - ATTACK: 快至中（超快瞬態）
   - RELEASE: 中（69.5-398ms範圍）
   - RATIO: 中至高（1176風格）
   - DRY: 70-80%（平行壓縮保留瞬態）
   - 目的：增加Sustain，染色增添管機感
  ↓
② Boss GE-7 Equalizer
   - 800Hz: +2dB（穿透力）
   - 1.6kHz: +3dB（清晰度）
   - 3.2kHz: +2dB（存在感）
   - LEVEL: Unity（Solo Boost時大幅向上）
   - 用途：快速調整，Solo Boost
  ↓
③ Roshi Blacklon (Amp-in-a-Box)
   - 6V6/6L6 Mode:
     - 6V6（右）: Neo Soul mellow tone
     - 6L6（左）: Post Rock重Riff，更大headroom
   - Mellow/Drive Mode:
     - Mellow（左）: 豐富低頻，較少失真
     - Drive（右）: 削減低頻，更多失真，更寬音色調整
   - Volume: 依需求
   - Gain: 中至高
   - Tone: 依風格調整
   - **目的：** 讓JC-22也能有Blackface管機感
  ↓
④ Cornerstone Colosseum
   - Order Toggle: Klon → BB順序
   - **Klon Side:**
     - Drive: 低至中
     - Treble: 依需求
     - Clip Blender: 混合Germanium + Silicon
   - **BB Side:**
     - Drive: 中
     - Treble: 依需求
     - Clean Control: 中（混入Clean訊號）
   - 用途：Klon提供透明推動，BB增加開放感
  ↓
⑤ Free the Tone ODL-1-CS
   - **Drive Channel:** 啟動
   - **電壓設定（CS版本）:** 14-16V（Int.PS/VARI Mode）
   - **ROCK/JAZZ:** ROCK（增加Gain，略削減低頻）
   - **EQ ON/GLASS:** 依需求切換
   - Drive Level: 中至高
   - Push: 中
   - Hi Cut: 依需求
   - Normal Channel可作Clean Boost
  ↓
🎛️ 音箱 Input
  ↓
音箱前級處理 → Send
  ↓
【Effects Loop - Send/Return之間】
  ↓
⑥ Free the Tone FT-1Y Delay
   - Realtime BPM Analyzer: ON
   - **Hold Function:** 連接外部踏板
     - 演奏樂句 → 按Hold儲存延遲音
     - 關閉效果 → 按Hold觸發
     - 在延遲音上繼續演奏（建構Pad）
   - Time: 依BPM設定
   - Feedback: 40-70%（Post Rock需要更多重複）
   - Mix: 30-60%
  ↓
⑧ Lichtlaerm AASB Shimmer Reverb
   - Mode:
     - **Above:** 高八度Shimmer（天使般）
     - **Below:** 低八度Drone（深沉Sub-Octave）
     - **Both:** 雙向八度（天堂與地底碰撞）
   - LEVEL: Unity或略高（最高+6dB Boost）
   - MIX: 60-90%（Post Rock需要大量Reverb）
   - DECAY: 長（建構音景）
   - DAMPEN: 中性至略暗（控制高頻）
   - X Control (Above/Below Mode): Pre-Delay 中
   - Y Control (Above/Below Mode): 八度音量 高
   - **Freeze:** 按住Freeze踏板，殘響無限延續
  ↓
⑨ Cornerstone Nucleo (Stereo)
   - Mode: **Reactor**（神秘大氣，核電廠空間）
   - Voicing: Vintage或Lo-Fi（溫暖復古）
   - Blend: 60-80%
   - Decay: 60-90秒（epic decay）
   - MOD: 中（調變深度）
   - AIR: 中至高（Shimmer高八度，疊加AASB）
   - FLUX: 中（顆粒質感，Geiger Counter風格）
   - **Freeze:** 凍結當前殘響，在凍結音上繼續演奏
   - **Stereo Output**
  ↓
🎛️ 音箱 Return → 後級 → Output
```

### 音色策略

**Post Rock Clean Ambient**
- 僅Blacklon Clean（6V6 Mellow）
- AASB Above模式（高八度Shimmer）
- Nucleo Reactor模式，Decay 60-90秒
- FT-1Y Hold功能建立Pad層次

**Post Rock Driven**
- Blacklon 6L6 + Drive
- Colosseum Klon → BB
- AASB Both模式（雙向八度）
- Nucleo Freeze凍結和弦殘響

**Fusion Lead**
- Free the Tone ODL-1-CS Drive Channel
- AASB關閉（清晰度優先）
- FT-1Y精準Delay（BPM同步）
- Nucleo Hall模式中等Decay

**Ambient Soundscape**
- 所有效果全開
- AASB + Nucleo疊加
- FT-1Y Hold + Nucleo Freeze建構複雜音景
- Cali76增加延音

**Classic Rock**
- Roshi Blacklon 6L6 + Drive
- Colosseum BB Side
- 使用Tone King Imperial MKII Lead Channel
- Mid-Bite ON（增加Punch）

### 為何選這些效果器？

- **Cali76 FET:** 染色壓縮增加管機感，Post Rock需要的延音
- **Boss GE-7:** 快速調整頻率，Solo Boost，比PA-1QG更直覺
- **Roshi Blacklon:** Amp-in-a-Box讓JC-22也能有Blackface管機感，4種模式組合
- **Colosseum:** 雙通道一次提供Klon + BB，節省空間，Order可切換
- **Free the Tone ODL-1-CS:** Dumble音色，雙通道，電壓可調（CS版本10-19V）
- **FT-1Y:** Hold功能對Post Rock極有價值，建構Ambient Pad
- **AASB:** 雙向八度是Nucleo沒有的，Post Rock Shimmer必備，Below模式Drone
- **Nucleo:** Reactor模式核電廠空間感，Stereo輸出，Freeze建構層次

---

## 最終黃金組合

### 核心理念
整合兩條訊號鏈的精華，建立一個可同時應對所有音樂類型的終極配置，利用4-cable method發揮最大效能。

### 黃金組合清單（12顆核心效果器）

**【Compressor】2顆**
1. ✅ Empress MKII - 極度透明，Jazz/Neo Soul首選
2. ✅ Origin Effects Cali76 FET - 1176染色，Post Rock/Ambient首選

**【EQ】1顆**
3. ✅ Free the Tone PA-1QG - 10-band, 99預設，MIDI整合

**【Overdrive/Drive】6顆**
4. ✅ From Yesterday (KOT Clone) - 雙通道極度透明，取代Morning Glory
5. ✅ Mad Professor Sweet Honey Overdrive Deluxe - 溫暖Neo Soul專家
6. ✅ EHX Soul Food - Klon透明Boost
7. ✅ Cornerstone Colosseum - BB + Klon雙通道，取代Virtues Arca
8. ✅ Roshi Blacklon - Amp-in-a-Box (Fender Blackface)
9. ✅ Free the Tone ODL-1-CS - Dumble-style雙通道

**【Delay】1顆**
10. ✅ Free the Tone FT-1Y - Realtime BPM Analyzer，核心Delay

**【Reverb】2顆**
11. ✅ Cornerstone Nucleo - Stereo主Reverb，Room/Hall/Reactor
12. ✅ Lichtlaerm AASB - Shimmer/Drone專用，雙向八度

**總價值估算：** 約 $3,628 USD

### 彈性訊號鏈配置

```
🎸 吉他
  ↓
【前級鏈 - 依音樂類型選擇A或B】
  ↓
配置A (Clean-focused)：
Empress MKII → PA-1QG → From Yesterday (KOT)
→ Mad Professor Sweet Honey → EHX Soul Food

配置B (Driven/Ambient)：
Cali76 FET → PA-1QG → Roshi Blacklon
→ Cornerstone Colosseum → Free the Tone ODL-1-CS
  ↓
🎛️ 音箱 Input → 前級 → Send
  ↓
【Effects Loop - 兩個配置共用】
  ↓
Free the Tone FT-1Y Delay
  ↓
Lichtlaerm AASB (需要Shimmer時)
  ↓
Cornerstone Nucleo Reverb (Stereo Out)
  ↓
🎛️ 音箱 Return → 後級 → Output
```

### 黃金組合的核心優勢

**1. 零重疊設計**
- 每顆效果器都有獨特功能定位
- 移除Morning Glory（KOT取代）
- 移除Virtues Arca（Colosseum取代）

**2. 雙通道/多模式最大化**
- From Yesterday: 雙通道OD (Clean/OD/Dist per channel)
- Colosseum: BB + Klon雙通道
- Free the Tone ODL-1-CS: Normal + Drive雙通道
- Roshi Blacklon: 4種模式組合（6L6/6V6 × Mellow/Drive）
- Nucleo: 3種Reverb模式（Room/Hall/Reactor）

**3. 完整音樂類型覆蓋**
- Jazz: Empress + KOT Clean + Sweet Honey + Nucleo Hall
- Neo Soul: Empress + Sweet Honey + Soul Food + Nucleo Room
- Funk: Empress + KOT Clean + PA-1QG高中頻 + FT-1Y
- Post Rock: Cali76 + Blacklon + AASB + Nucleo Reactor
- Fusion: Cali76 + ODL-1-CS + FT-1Y + Nucleo Hall
- Pop Rock: Empress + Soul Food + Colosseum + Nucleo

**4. 4-Cable Method完美應用**
- 前級：Comp → EQ → OD chain
- Loop：Delay → Reverb（避免Reverb進OD導致混濁）
- Nucleo Stereo輸出在Loop中發揮最大效果

**5. MIDI整合能力**
- PA-1QG: 99預設MIDI切換
- FT-1Y: MIDI Program Change
- Nucleo: 128 MIDI預設
- 可建構完整MIDI控制系統

---

## 移除與Tier 2建議

### ❌ 建議移除（嚴重重疊，無獨特價值）

**1. JHS Morning Glory V3**
- 理由：From Yesterday (KOT Clone) 雙通道完全取代其功能
- 重疊度：100%
- 決策：出售或移除
- **預估回收：** $150-180 USD

**2. Virtues Arca**
- 理由：Cornerstone Colosseum的BB Side功能更好
- 重疊度：80%
- 決策：出售或移除
- **預估回收：** $200-250 USD

**總回收資金：** $350-430 USD

---

### 📦 Tier 2（使用機率低，保留備用）

**3. TWA Source Code (TS Evolution)**
- 保留理由：
  - Bite Control（調整偶次/奇次諧波）獨特
  - 18V內部升壓（大headroom）
  - 原創TS808設計者Susumu Tamura設計
- 使用時機：
  - Classic Rock需要傳統TS中頻突出
  - 需要TS風格推動音箱
  - 與其他OD疊加實驗
- 使用機率：**10-15%**

**4. PRS Horsemeat**
- 保留理由：
  - Germanium diodes（比Soul Food的Silicon更溫暖）
  - Voice Control（從saturated到glassy連續可調）
  - 2-band EQ（比Soul Food更多控制）
- 使用時機：
  - Soul Food/Colosseum無法滿足時
  - 需要極度溫暖Klon音色
  - Voice Control微調特殊音色
- 使用機率：**15-20%**

**5. Boss GE-7 Equalizer**
- 保留理由：
  - 極簡操作（無需編輯預設）
  - 視覺化滑桿（直覺調整）
  - 極度耐用可靠
  - PA-1QG備份
- 使用時機：
  - PA-1QG故障備用
  - 簡單現場演出無需預設切換
  - 快速視覺化調整
- 使用機率：**5-10%**

---

## 音樂類型快速參考

### Jazz 演奏

**吉他：** ESP Throbber-CTM
**音箱：** Tone King Imperial MKII

**訊號鏈：**
```
Empress MKII (輕微壓縮)
→ PA-1QG (Throbber專用Preset)
→ From Yesterday Yellow側Clean Mode
→ Sweet Honey (低增益)
→ Imperial MKII Rhythm Channel
→ (Loop) FT-1Y (細微Delay) → Nucleo Hall (低Mix)
```

**關鍵設定：**
- Empress: INPUT低，Ratio 2:1，極度透明
- PA-1QG: Preset 3專為Throbber設定
- From Yesterday: Yellow Clean Mode，Volume略高
- Sweet Honey: Drive 9-10點鐘，Focus 12點鐘
- Imperial: Rhythm Channel, Volume 4-5
- Nucleo: Hall模式，Blend 20-30%

---

### Neo Soul 演奏

**吉他：** Greco TE-500 或 Fender Tokyo Thinline
**音箱：** Roland JC-22

**訊號鏈：**
```
Empress MKII
→ PA-1QG (吉他專用Preset)
→ Mad Professor Sweet Honey (中低增益，Focus 1-2點鐘)
→ EHX Soul Food (Clean Boost模式)
→ JC-22 Input (Chorus ON)
→ (Loop) FT-1Y (BPM同步) → Nucleo Room (Stereo)
```

**關鍵設定：**
- Empress: Tilt EQ正午，透明控制
- PA-1QG: Preset 1 (Greco) 或 Preset 2 (Tokyo Thinline)
- Sweet Honey: Drive 11-12點鐘，Focus 1-2點鐘（甜蜜點）
- Soul Food: Drive低，Volume高（Clean Boost）
- JC-22: Chorus Speed 3-4, Depth 4-5
- Nucleo: Room模式，Blend 30-50%，Stereo輸出

---

### Funk 演奏

**吉他：** Greco TE-500
**音箱：** Roland JC-22

**訊號鏈：**
```
Empress MKII (快Attack, 快Release)
→ PA-1QG (提升800Hz-3.2kHz穿透力)
→ From Yesterday Yellow Clean Mode
→ JC-22 Input (Chorus ON, Bright Switch ON)
→ (Loop) FT-1Y (短Delay) → Nucleo Room (低Mix)
```

**關鍵設定：**
- Empress: ATTACK快，RELEASE快至中，Ratio 4:1
- PA-1QG: 提升800Hz +2dB, 1.6kHz +3dB, 3.2kHz +2dB
- From Yesterday: Yellow Clean Mode，清晰Attack
- JC-22: Bright Switch ON，高頻Sparkle
- FT-1Y: 短Delay（100-150ms），增添空間感
- Nucleo: Room模式，Blend 20-30%

---

### Post Rock 演奏

**吉他：** ESP EC-CTM
**音箱：** Roland JC-22 或 Tone King Imperial MKII

**訊號鏈：**
```
Cali76 FET (中IN, 快ATTACK, 增加Sustain)
→ Roshi Blacklon (6L6 + Drive Mode)
→ Cornerstone Colosseum (Klon → BB)
→ 音箱 Input
→ (Loop) FT-1Y (Hold功能建Pad)
→ AASB (Above或Both模式, Freeze)
→ Nucleo Reactor (長Decay 60-90秒, Freeze)
```

**關鍵設定：**
- Cali76: IN中，ATTACK快，RELEASE中，DRY 70-80%
- Blacklon: 6L6 Mode（大headroom），Drive Mode（更多失真）
- Colosseum: Klon → BB順序，Klon推動BB
- FT-1Y: Hold功能連接外部踏板，建構Ambient Pad
- AASB: Above（高八度）或Both（雙向），Freeze凍結
- Nucleo: Reactor模式，Decay 60-90秒，Freeze建構層次

---

### Fusion 演奏

**吉他：** Fender Tokyo Thinline 或 ESP Throbber-CTM
**音箱：** Roland JC-22

**訊號鏈：**
```
Cali76 FET 或 Empress MKII
→ PA-1QG
→ Free the Tone ODL-1-CS (Drive Channel, 14-16V)
→ JC-22 Input
→ (Loop) FT-1Y (精準BPM Analyzer) → Nucleo Hall
```

**關鍵設定：**
- Compressor: Empress（透明）或Cali76（染色）依需求
- PA-1QG: 吉他專用Preset
- ODL-1-CS: Drive Channel，電壓14-16V，ROCK Mode
- FT-1Y: Realtime BPM Analyzer精準同步
- Nucleo: Hall模式，中等Decay

---

### Classic Rock 演奏

**吉他：** Greco TE-500
**音箱：** Tone King Imperial MKII

**訊號鏈：**
```
Cali76 FET
→ PA-1QG
→ Roshi Blacklon (6L6 + Drive) 或 Cornerstone Colosseum BB Side
→ Imperial MKII Lead Channel (Mid-Bite ON)
→ (Loop) FT-1Y → Nucleo Hall
```

**關鍵設定：**
- Cali76: 增加Sustain與管機染色
- Blacklon: 6L6 + Drive，Blackface Crunch
- Colosseum: BB Side，開放清晰的Classic Rock Tone
- Imperial: Lead Channel，Mid-Bite ON（Punch）
- Nucleo: Hall模式，中等Decay

---

## 供電與Pedalboard配置

### 供電規格總覽

| 效果器 | 電壓 | 電流 | 特殊需求 |
|--------|------|------|----------|
| Empress MKII | 9V DC | 100mA | |
| Cali76 FET | 9V DC | 150mA+ | 內部升壓至24V |
| PA-1QG | 9V DC | 200mA | **勿Daisy Chain** |
| From Yesterday | 9-18V DC | 50mA | 18V更佳 |
| Sweet Honey Deluxe | 9V DC | 5mA | 極低耗電 |
| Soul Food | 9V DC | 50mA | 附電源 |
| Colosseum | 9V DC | 150mA | |
| Roshi Blacklon | 9V DC | 100mA | **勿超過10V** |
| Free the Tone ODL-1-CS | 9V DC | 200mA+ | 內部可升壓10-19V |
| FT-1Y | **12V DC** | **400mA** | **需專用12V** |
| Nucleo | 9V DC | 150mA | |
| AASB | 9V DC | 150mA | **僅支援9V** |

**總電流需求：** 約 1600-1800mA

### 推薦電源供應器

**選項1：Strymon Zuma（高階）**
- 規格：9個隔離輸出 @ 500mA each
- 特色：2個可調電壓輸出（9/12/18V）
- 總電流：4500mA
- 價格：~$280 USD
- **優勢：** 完全隔離，極低雜訊，可調電壓適合FT-1Y 12V需求

**選項2：Truetone CS12（性價比）**
- 規格：12個輸出
  - 8個隔離 @ 100mA
  - 2個 @ 250mA
  - 2個 @ 500mA
- 總電流：3000mA
- 價格：~$200 USD
- **優勢：** 12輸出數量完美適合黃金組合

**選項3：Cioks DC7 + Cioks 4（專業級）**
- DC7：7個隔離輸出 @ 660mA each
- Cioks 4：4個額外輸出
- 可鏈接擴充
- 價格：DC7 ~$250, Cioks 4 ~$75
- **優勢：** 彈性擴充，極低雜訊，專業品質

### 供電配置建議（使用Truetone CS12）

```
CS12 Output 1 (500mA): FT-1Y Delay (12V模式，使用Voltage Doubler Cable)
CS12 Output 2 (500mA): Free the Tone ODL-1-CS (200mA+)
CS12 Output 3 (250mA): PA-1QG (200mA)
CS12 Output 4 (250mA): Nucleo (150mA)
CS12 Output 5 (100mA): Empress MKII (100mA)
CS12 Output 6 (100mA): Cali76 FET (150mA可能需要升級)
CS12 Output 7 (100mA): Colosseum (150mA可能需要升級)
CS12 Output 8 (100mA): AASB (150mA可能需要升級)
CS12 Output 9 (100mA): Roshi Blacklon (100mA，注意勿超過10V)
CS12 Output 10 (100mA): From Yesterday (50mA，可設定18V）
CS12 Output 11 (100mA): Soul Food (50mA)
CS12 Output 12 (100mA): Sweet Honey (5mA)
```

**注意事項：**
- **FT-1Y需要12V**：使用CS12的Voltage Doubler Cable將兩個9V輸出串聯成18V，或使用Zuma的可調電壓輸出
- **PA-1QG, ODL-1-CS, FT-1Y**：需要獨立隔離輸出（勿Daisy Chain）
- **Roshi Blacklon**：嚴禁超過10V
- **Cali76, Colosseum, AASB**：可能需要使用250mA或500mA輸出

---

### Pedalboard實體配置

**推薦Pedalboard尺寸：**
- Pedaltrain Classic 2 (24" x 12.5") 或
- Temple Audio DUO 24 (24" x 12.6") 或
- RockBoard TRES 3.1 (24.4" x 14.6")

**配置策略（Top Row → Bottom Row）：**

```
【Top Row - Compressor & EQ】(左→右)
Empress MKII → Cali76 FET → PA-1QG
```

```
【Middle Row 1 - 透明OD】(左→右)
From Yesterday (KOT) → Sweet Honey → Soul Food
```

```
【Middle Row 2 - 染色OD/Drive】(左→右)
Colosseum → Roshi Blacklon → Free the Tone ODL-1-CS
```

```
【Bottom Row - Effects Loop空間系】(左→右)
FT-1Y Delay → AASB Shimmer → Nucleo Reverb
```

**視覺化配置圖：**
```
┌─────────────────────────────────────────┐
│ Empress  Cali76   PA-1QG                │ Top Row
├─────────────────────────────────────────┤
│ KOT  Sweet Honey  Soul Food             │ Mid 1
├─────────────────────────────────────────┤
│ Colosseum  Blacklon  ODL-1-CS           │ Mid 2
├─────────────────────────────────────────┤
│ FT-1Y    AASB    Nucleo                 │ Bottom
└─────────────────────────────────────────┘
```

### 線材建議

**前級短線：**
- EBS PatchCable Flat（節省空間）
- Rockboard Flat Patch Cable
- 長度：10cm, 15cm, 20cm混用

**Loop連接：**
- 優質TRS Cable（Roland JC-22的Stereo Loop）
- Mogami或Canare品質
- 長度：依Pedalboard到音箱距離，建議3-5米

**Nucleo Stereo Out：**
- 兩條高品質TS Cable（L + R）
- 確保Right Output使用Transformer-Isolated避免Ground Loop

**吉他導線：**
- Mogami或Canare高品質導線
- 長度：3-5米（依演奏距離）

### MIDI整合（可選進階）

**MIDI控制器選項：**
- Disaster Area DMC-6 Gen3
- RJM Mastermind PBC/6X
- Morningstar MC6 MKII

**MIDI控制內容：**
- PA-1QG: Program Change切換99個預設
- FT-1Y: Program Change切換預設，BPM控制
- Nucleo: Program Change切換128個MIDI預設
- 一次切換整套效果器設定（吉他切換/風格切換）

**MIDI連接：**
```
MIDI Controller OUT
→ PA-1QG MIDI IN → PA-1QG MIDI OUT
→ FT-1Y MIDI IN → FT-1Y MIDI OUT
→ Nucleo MIDI IN
```

---

## 4-Cable Method詳解

### 什麼是4-Cable Method？

4-Cable Method（4CM）是一種訊號鏈配置方式，將效果器分為兩組：
1. **前級效果器**（Compressor, EQ, Overdrive）→ 音箱Input
2. **後級效果器**（Delay, Reverb）→ 音箱Effects Loop

**優勢：**
- Delay/Reverb不會被Overdrive失真（避免混濁）
- 可使用音箱前級（Preamp）的失真
- Delay/Reverb在音箱後級（Power Amp）之前，音色更清晰
- 保留音箱本身的音色特性

### Tone King Imperial MKII 4-Cable Method

```
🎸 吉他
  ↓
🎛️ Pedalboard Input
  ↓
【前級鏈】
Compressor → EQ → Overdrive Chain
  ↓
🎛️ Pedalboard Output
  ↓
🔊 Imperial MKII Input
  ↓
Imperial 前級處理 (Rhythm/Lead Channel)
  ↓
🔊 Imperial MKII Send (Effects Loop Send)
  ↓
🎛️ Pedalboard Loop Input
  ↓
【Loop鏈】
Delay → Reverb
  ↓
🎛️ Pedalboard Loop Output
  ↓
🔊 Imperial MKII Return (Effects Loop Return)
  ↓
Imperial 後級處理 (Power Amp)
  ↓
🔊 Imperial Output → Speaker
```

**連接線材：**
1. 吉他 → Pedalboard Input：高品質導線（3-5米）
2. Pedalboard Output → Imperial Input：短導線（30-50cm）
3. Imperial Send → Pedalboard Loop Input：TRS Cable（1-2米）
4. Pedalboard Loop Output → Imperial Return：TRS Cable（1-2米）

**Imperial MKII特殊設定：**
- Effects Loop可切換Series/Parallel（建議Series）
- Ironman II衰減器可依場地調整功率（20W/10W/5W/1W/0.5W）
- 內建Reverb + Tremolo可關閉（因Loop中已有Nucleo）

---

### Roland JC-22 4-Cable Method

```
🎸 吉他
  ↓
🎛️ Pedalboard Input
  ↓
【前級鏈】
Compressor → EQ → Overdrive Chain
  ↓
🎛️ Pedalboard Output
  ↓
🔊 JC-22 Input
  ↓
JC-22 前級處理 (Preamp + Tone Stack)
  ↓
🔊 JC-22 Send (Stereo Effects Loop Send L+R)
  ↓
🎛️ Pedalboard Loop Input (可能需要Stereo to Mono Summing)
  ↓
【Loop鏈】
Delay (Mono In) → Reverb (Mono/Stereo)
  ↓
🎛️ Pedalboard Loop Output (Stereo L+R from Nucleo)
  ↓
🔊 JC-22 Return L+R (Stereo Effects Loop Return)
  ↓
JC-22 後級處理 (Power Amp)
  ↓
🔊 JC-22 Output → Stereo Speakers (2x6.5")
```

**連接線材：**
1. 吉他 → Pedalboard Input：高品質導線（3-5米）
2. Pedalboard Output → JC-22 Input：短導線（30-50cm）
3. JC-22 Send (Stereo TRS) → Pedalboard Loop Input：TRS to Dual TS Cable（1-2米）
4. Pedalboard Loop Output (Nucleo Stereo L+R) → JC-22 Return L+R：兩條TS Cable（1-2米）

**JC-22特殊設定：**
- Effects Loop可切換Series/Parallel（建議Series）
- 內建Chorus + Reverb可調低（因Loop中已有Nucleo）
- **Stereo Loop注意事項：**
  - JC-22 Send是Stereo（但如果Delay是Mono，會自動Summing）
  - Nucleo Stereo Output完美適配JC-22 Stereo Return
  - 確保Nucleo的Right Output使用Transformer-Isolated避免Ground Loop

---

### 4CM常見問題解決

**問題1：Ground Loop Hum（地迴路嗡聲）**
- 解決：使用Nucleo的Right Output（Transformer-Isolated）
- 或使用Hum Eliminator（如Ebtech Hum X）

**問題2：Loop電平不匹配**
- 症狀：Loop效果器音量過小或過大
- 解決：調整Loop中第一顆效果器（FT-1Y）的輸入增益
- 或使用Line Level Converter

**問題3：Stereo Loop訊號丟失**
- 症狀：Stereo Reverb變成Mono
- 解決：確保Return連接兩條Cable（L+R）
- 確認音箱Loop設定為Stereo Mode

**問題4：Loop訊號切換Pop聲**
- 解決：使用Buffered Bypass效果器
- 或加入Loop Switcher（如Boss LS-2）

---

## 效果器使用機率評估

### Tier 1（核心必備，使用率90%+）

| 效果器 | 使用機率 | 核心價值 |
|--------|----------|----------|
| ✅ From Yesterday (KOT) | 95% | 雙通道極度透明，所有風格適用 |
| ✅ Mad Professor Sweet Honey | 90% | Neo Soul核心音色 |
| ✅ PA-1QG | 95% | EQ核心，每把吉他專用Preset |
| ✅ Empress MKII | 85% | Clean-focused音樂類型首選 |
| ✅ FT-1Y | 100% | 唯一Delay，所有風格必備 |
| ✅ Nucleo | 95% | 主Reverb，Stereo輸出核心 |

### Tier 1.5（高使用率，特定風格核心）

| 效果器 | 使用機率 | 核心價值 |
|--------|----------|----------|
| ✅ Soul Food | 75% | Klon Boost，Clean Boost萬用 |
| ✅ Cali76 FET | 70% | Post Rock/Fusion必備 |
| ✅ Colosseum | 80% | BB + Klon雙通道高效率 |
| ✅ Roshi Blacklon | 75% | Amp-in-a-Box，讓JC-22有管機感 |

### Tier 1.8（中高使用率，特殊用途）

| 效果器 | 使用機率 | 核心價值 |
|--------|----------|----------|
| ✅ Free the Tone ODL-1-CS | 60% | Dumble音色，Fusion/Blues專用 |
| ✅ AASB | 50% | Shimmer/Drone，Post Rock Ambient核心 |

### Tier 2（保留備用，使用率低）

| 效果器 | 使用機率 | 保留理由 |
|--------|----------|----------|
| 📦 TWA Source Code | 10-15% | Bite Control獨特，TS Evolution |
| 📦 PRS Horsemeat | 15-20% | Germanium溫暖，Voice Control |
| 📦 Boss GE-7 | 5-10% | PA-1QG備份，極簡操作 |

### 移除清單

| 效果器 | 理由 | 取代方案 |
|--------|------|----------|
| ❌ JHS Morning Glory V3 | 100%重疊 | From Yesterday (KOT) |
| ❌ Virtues Arca | 80%重疊 | Cornerstone Colosseum BB Side |

---

## 階段性建構建議

### 如果需要分階段建立黃金組合

**階段1：核心基礎（6顆，$1,649）**

1. **Free the Tone PA-1QG** ($425) - EQ核心，MIDI整合
2. **From Yesterday (KOT)** ($335) - 透明OD核心，雙通道
3. **Mad Professor Sweet Honey** ($220) - Neo Soul核心
4. **Free the Tone FT-1Y** ($400) - Delay核心，BPM Analyzer
5. **Cornerstone Nucleo** ($350) - Reverb核心，Stereo
6. **Empress MKII** ($219) - Compressor透明選項

**此階段可達成：**
- 完整EQ能力（PA-1QG）
- 透明Overdrive（KOT）
- 溫暖Overdrive（Sweet Honey）
- 核心Delay（FT-1Y）
- 核心Reverb（Nucleo）
- 透明壓縮（Empress）

**音樂類型覆蓋：** Jazz, Neo Soul, Funk基本需求

---

**階段2：擴充雙通道與Amp-in-a-Box（4顆，$1,374）**

7. **Cornerstone Colosseum** ($380) - BB + Klon雙通道
8. **Roshi Blacklon** ($200) - Amp-in-a-Box，讓JC-22有管機感
9. **Free the Tone ODL-1-CS** ($425) - Dumble雙通道，電壓可調
10. **Origin Effects Cali76 FET** ($369) - 染色Compressor，Post Rock

**此階段新增能力：**
- 雙風格Overdrive（Colosseum BB + Klon）
- Blackface管機模擬（Blacklon）
- Dumble高階音色（ODL-1-CS）
- 染色壓縮（Cali76）

**音樂類型覆蓋：** 新增Post Rock, Fusion, Classic Rock完整支援

---

**階段3：特殊效果完成（2顆，$605）**

11. **Lichtlaerm AASB** ($225) - Shimmer/Drone，雙向八度
12. **EHX Soul Food** ($80) - Klon Boost，便宜實用

**此階段新增能力：**
- Post Rock Shimmer（AASB Above模式）
- Drone底層（AASB Below模式）
- 雙向八度音景（AASB Both模式）
- Clean Boost萬用（Soul Food）

**音樂類型覆蓋：** 完整覆蓋所有需求，包括Ambient/Post Rock進階技巧

---

### 優先順序建議

**如果預算有限，優先購買順序：**

1. **Free the Tone FT-1Y** - 唯一Delay，必備
2. **Cornerstone Nucleo** - 主Reverb，Stereo核心
3. **Free the Tone PA-1QG** - EQ核心，多吉他切換
4. **From Yesterday (KOT)** - 透明OD核心
5. **Mad Professor Sweet Honey** - Neo Soul核心
6. **Empress MKII** - 透明壓縮
7. **EHX Soul Food** - 便宜實用Boost（可提早購入）
8. **Cornerstone Colosseum** - 雙通道效率高
9. **Roshi Blacklon** - Amp-in-a-Box實用
10. **Cali76 FET** - Post Rock染色壓縮
11. **Free the Tone ODL-1-CS** - 高階Dumble音色
12. **Lichtlaerm AASB** - 特殊Shimmer效果

---

## 總結與最終建議

### 核心決策

**✅ 立即移除（回收$350-430）：**
- ❌ JHS Morning Glory V3
- ❌ Virtues Arca

**📦 移至Tier 2（備用箱）：**
- TWA Source Code
- PRS Horsemeat
- Boss GE-7

**✅ 黃金組合12顆核心效果器：**
1. Empress MKII
2. Cali76 FET
3. PA-1QG
4. From Yesterday (KOT)
5. Sweet Honey Deluxe
6. Soul Food
7. Colosseum
8. Roshi Blacklon
9. Free the Tone ODL-1-CS
10. FT-1Y
11. Nucleo
12. AASB

### 最終設備配置優勢

**🎸 吉他覆蓋完整：**
- 4把吉他涵蓋所有拾音器類型
- PA-1QG可為每把吉他建立專用EQ Preset

**🎛️ 音箱搭配完美：**
- Imperial MKII：管機溫暖，Vintage風格
- JC-22：晶體機清晰，Modern風格
- 兩者都支援4-Cable Method

**🎵 音樂類型覆蓋全面：**
- Jazz ★★★★★
- Neo Soul ★★★★★
- Funk ★★★★★
- Post Rock ★★★★★
- Fusion ★★★★★
- Pop Rock ★★★★★
- Classic Rock ★★★★★

**⚡ 訊號鏈效率最大化：**
- 零功能重疊
- 雙通道/多模式效果器最大化
- 4-Cable Method完美應用
- MIDI整合能力完整

**💰 投資價值：**
- 總價值：$3,628 USD
- 回收Morning Glory + Arca：-$350-430
- 淨投資：約$3,200 USD
- 12顆頂級效果器，平均每顆$267
- 涵蓋所有音樂類型需求

---

**文件版本：** 1.0
**建立日期：** 2025-12-13
**參考文件：**
- guitar_collection_analysis.md
- guitar_amp_pairing_guide.md
- overdrive_pedals_technical_data.md
- compressor_eq_spatial_effects_technical_data.md
- compare_rules

**適用範圍：** Emil的4吉他×2音箱×17效果器完整配置

---

**下一步行動：**
1. ✅ 決定是否移除Morning Glory V3 + Virtues Arca
2. ✅ 將TWA Source Code, PRS Horsemeat, Boss GE-7移至備用箱
3. ✅ 規劃Pedalboard實體配置
4. ✅ 購買電源供應器（Truetone CS12或Strymon Zuma）
5. ✅ 準備線材（EBS Flat Patch, Mogami/Canare TRS）
6. ✅ 建立PA-1QG預設庫（為每把吉他建立專用EQ）
7. ✅ 測試4-Cable Method連接（兩個音箱）
8. ✅ 考慮MIDI Controller整合（Disaster Area DMC-6或RJM Mastermind）

**祝演奏愉快！**
