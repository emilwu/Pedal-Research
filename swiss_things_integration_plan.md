# Swiss Things 整合方案 - V2.0 效果器配置

**版本:** 1.0
**建立日期:** 2025-12-30
**基於:** comprehensive_analysis_summary_v2.md + swiss_things_signal_routing_logic.md
**目標:** 透過 Swiss Things 切換兩組訊號鏈（Jazz/Neo Soul 與 Post Rock）

---

## 執行摘要

Swiss Things 的核心優勢是 **2 個獨立 Effects Loop**（Loop 1 無緩衝 + Loop 2 有緩衝），完美對應 V2.0 的兩組訊號鏈設計：

- **Loop 1 (Unbuffered)**: 放置 Jazz/Neo Soul 訊號鏈（Sweet Honey + Colosseum Klon）
- **Loop 2 (Buffered)**: 放置 Post Rock 訊號鏈（Blacklon + Colosseum + TWA Source + ODL-1-CS）
- **Swiss Things 之前**: Always-on pedals（Empress MKII / Cali76 FET + PA-1QG）
- **Swiss Things 之後**: Time-based effects（FT-1Y + AASB + Nucleo）

透過腳踏開關，可在演出中快速切換兩組訊號鏈，實現：
- **Loop 1 ON, Loop 2 OFF** = Jazz/Neo Soul 音色
- **Loop 1 OFF, Loop 2 ON** = Post Rock/Fusion 音色
- **Loop 1 ON, Loop 2 ON** = 疊加所有 OD（實驗音色）

---

## 目錄

1. [Swiss Things 核心功能回顧](#swiss-things-核心功能回顧)
2. [V2.0 效果器配置分析](#v20-效果器配置分析)
3. [整合策略：訊號鏈設計](#整合策略訊號鏈設計)
4. [完整訊號鏈配置](#完整訊號鏈配置)
5. [開關與操作邏輯](#開關與操作邏輯)
6. [實際演出場景切換](#實際演出場景切換)
7. [Pedalboard 配置圖](#pedalboard-配置圖)
8. [供電與佈線計畫](#供電與佈線計畫)
9. [與原 V2.0 方案對比](#與原-v20-方案對比)
10. [實施建議與注意事項](#實施建議與注意事項)

---

## Swiss Things 核心功能回顧

### 關鍵特性（來自 swiss_things_signal_routing_logic.md）

**2 個 Flexi-Switch® Effects Loop:**
- **Loop 1 (Unbuffered)**: 適合 Gain-type pedals（OD/Dist/Fuzz）
- **Loop 2 (Buffered)**: 適合 Time-based/Mod pedals

**其他功能:**
- Buffered Tuner Output（Always-on required）
- 20dB Clean Boost（Solo boost 用途）
- Expression Pedal Volume 控制
- AB-Y Switching（單/雙音箱切換）

**訊號流程:**
```
INPUT → Buffer → Loop 1 (Unbuffered) → Buffer → Volume EXP →
Loop 2 (Buffered) → Booster → Buffer → Output A/B
```

---

## V2.0 效果器配置分析

### 10 顆核心效果器分類

根據 comprehensive_analysis_summary_v2.md，效果器分為：

#### 類別 1: Always-On Pedals（Swiss Things INPUT 之前）
1. **Empress MKII** - 透明壓縮（Jazz/Neo Soul）
2. **Cali76 FET** - 染色壓縮（Post Rock）
3. **PA-1QG** - EQ + Clean Boost

#### 類別 2: Gain-Type Pedals（Swiss Things Loop 內）
**訊號鏈 1（Jazz/Neo Soul）:**
4. **Sweet Honey Deluxe** - 溫暖 OD
5. **Colosseum Klon Side** - Klon Boost

**訊號鏈 2（Post Rock）:**
6. **Roshi Blacklon** - Amp-in-a-Box
7. **Cornerstone Colosseum** - BB + Klon 雙通道
8. **TWA Source Code** - TS Evolution
9. **Free the Tone ODL-1-CS** - Dumble

#### 類別 3: Time-Based Effects（Swiss Things 之後）
10. **FT-1Y** - Delay
11. **AASB** - Shimmer Reverb
12. **Nucleo** - 主 Reverb

---

### 關鍵發現：兩組訊號鏈的天然分離

**訊號鏈 1（Jazz/Neo Soul）:**
- 使用 **Empress MKII**（透明壓縮）
- 只需 **2 顆 OD**（Sweet Honey + Colosseum Klon）
- 音色導向：**透明、溫暖、Clean**

**訊號鏈 2（Post Rock）:**
- 使用 **Cali76 FET**（染色壓縮）
- 需要 **4 顆 OD**（Blacklon + Colosseum + TWA + ODL-1-CS）
- 音色導向：**層次豐富、Gain 疊加、Ambient**

**Swiss Things 整合策略:**
- **Loop 1 放置訊號鏈 1**（Jazz/Neo Soul - 2 顆 OD）
- **Loop 2 放置訊號鏈 2**（Post Rock - 4 顆 OD）

---

## 整合策略：訊號鏈設計

### 核心概念

**Swiss Things 的 Loop 1/Loop 2 本來設計用於不同類型效果器（Gain vs Time），但我們將其重新定義為『兩組獨立訊號鏈』:**

- **Loop 1 = 訊號鏈 1**（Jazz/Neo Soul）
- **Loop 2 = 訊號鏈 2**（Post Rock）

**為何可行？**

1. ✅ **Loop 1 是 Unbuffered**（適合 OD/Fuzz 等 gain pedals）
   - 訊號鏈 1 的 Sweet Honey + Colosseum 都是 OD
   - 完美匹配

2. ✅ **Loop 2 是 Buffered**（原設計給 Time-based，但也可放 OD）
   - 訊號鏈 2 的 Blacklon + Colosseum + TWA + ODL-1-CS 都是 OD
   - Buffered 對這些現代 OD 影響不大

3. ✅ **Time-based effects 放在 Swiss Things 之後**
   - FT-1Y, AASB, Nucleo 放在 Output A 之後
   - 或使用 4-Cable Method 放入音箱 FX Loop

---

### 方案 A：Swiss Things 後接 Time-Based Effects（推薦）

**訊號流程:**
```
🎸 Guitar
  ↓
[Compressor 選擇: Empress MKII 或 Cali76 FET]
  ↓
PA-1QG (EQ + Clean Boost)
  ↓
═══════════════════════════════════════════
      SWISS THINGS INPUT
═══════════════════════════════════════════
  ↓
  ├→ TUNER OUTPUT → Tuner (Always-on)
  ↓
┌──────────────────────────────────────────┐
│ Loop 1 (Unbuffered) - 訊號鏈 1            │
│ Jazz / Neo Soul                          │
│                                          │
│ Send → Sweet Honey → Colosseum Klon → Return │
└──────────────────────────────────────────┘
  ↓
  ├→ VOLUME EXP → Expression Pedal
  ↓
┌──────────────────────────────────────────┐
│ Loop 2 (Buffered) - 訊號鏈 2              │
│ Post Rock / Fusion                       │
│                                          │
│ Send → Roshi Blacklon → Colosseum (雙通道) │
│     → TWA Source Code → ODL-1-CS → Return │
└──────────────────────────────────────────┘
  ↓
[Boost] (20dB - Solo 時使用)
  ↓
OUTPUT A
  ↓
═══════════════════════════════════════════
      Time-Based Effects Chain
═══════════════════════════════════════════
  ↓
FT-1Y Delay
  ↓
AASB Shimmer (Post Rock 時)
  ↓
Nucleo Reverb
  ↓
🎛️ Amp Input
```

**開關邏輯:**
- **Jazz/Neo Soul**: Loop 1 ON, Loop 2 OFF
- **Post Rock**: Loop 1 OFF, Loop 2 ON
- **實驗疊加**: Loop 1 ON, Loop 2 ON（6 顆 OD 疊加）

---

### 方案 B：4-Cable Method（進階，音箱支援 FX Loop）

**訊號流程:**
```
🎸 Guitar
  ↓
[Compressor 選擇: Empress MKII 或 Cali76 FET]
  ↓
PA-1QG
  ↓
═══════════════════════════════════════════
      SWISS THINGS INPUT
═══════════════════════════════════════════
  ↓
  ├→ TUNER OUTPUT → Tuner
  ↓
[Loop 1: Jazz/Neo Soul OD Chain]
  ↓
[Loop 2: Post Rock OD Chain]
  ↓
[Boost]
  ↓
OUTPUT A → 🎛️ AMP INPUT
  ↓
🎛️ AMP PREAMP
  ↓
🎛️ AMP FX SEND
  ↓
FT-1Y → AASB → Nucleo
  ↓
🎛️ AMP FX RETURN → POWER AMP → Speaker
```

**優勢:**
- Delay/Reverb 在音箱後級（不被前級失真影響）
- 更乾淨的 Time-based 音色

---

## 完整訊號鏈配置

### 配置詳細規劃（方案 A - 推薦）

#### 前級鏈（Swiss Things 之前）

```
🎸 Guitar
  ↓
┌──────────────────────────────────────────┐
│ Compressor 選擇器（手動切換吉他線）        │
│                                          │
│ 選項 1: Empress MKII (Jazz/Neo Soul)    │
│         INPUT 低, RATIO 2:1, MIX 80-100% │
│                                          │
│ 選項 2: Cali76 FET (Post Rock)          │
│         IN 中, ATTACK 快, DRY 70-80%     │
└──────────────────────────────────────────┘
  ↓
┌──────────────────────────────────────────┐
│ Free the Tone PA-1QG                     │
│                                          │
│ Preset 配置:                             │
│ • Preset 1-4: 吉他專用 EQ + LEVEL        │
│ • Preset 5-8: 風格專用                   │
│                                          │
│ 功能: EQ 調整 + Clean Boost (LEVEL)      │
└──────────────────────────────────────────┘
  ↓
  導線 → SWISS THINGS INPUT
```

**注意:**
- Compressor 選擇透過手動切換吉他線（或使用 A/B Switch Box）
- Jazz/Neo Soul 場景 → 插入 Empress MKII
- Post Rock 場景 → 插入 Cali76 FET

---

#### Swiss Things 配置

```
═══════════════════════════════════════════
         SWISS THINGS
═══════════════════════════════════════════

INPUT (來自 PA-1QG)
  ↓
  ├→ TUNER OUTPUT → TC Polytune / Boss TU-3
  │                 (Always-on 必須)
  ↓
┌──────────────────────────────────────────┐
│ LOOP 1 (Unbuffered)                      │
│ = 訊號鏈 1: Jazz / Neo Soul              │
├──────────────────────────────────────────┤
│ Loop 1 Send                              │
│   ↓                                      │
│ ① Mad Professor Sweet Honey Deluxe      │
│   • DRIVE: 11-12點鐘                     │
│   • FOCUS: 1-2點鐘（Neo Soul 甜蜜點）    │
│   • VOLUME: 12-1點鐘                     │
│   ↓                                      │
│ ② Cornerstone Colosseum - Klon Side     │
│   • MODE: Klon Side                      │
│   • DRIVE: 9-10點鐘（Boost 模式）        │
│   • VOLUME: 2點鐘                        │
│   • CLEAN: 9-11點鐘                      │
│   ↓                                      │
│ Loop 1 Return                            │
└──────────────────────────────────────────┘
  ↓
  ├→ VOLUME EXP → Expression Pedal (可選)
  ↓
┌──────────────────────────────────────────┐
│ LOOP 2 (Buffered)                        │
│ = 訊號鏈 2: Post Rock / Fusion           │
├──────────────────────────────────────────┤
│ Loop 2 Send                              │
│   ↓                                      │
│ ③ Roshi Blacklon                         │
│   • TUBE: 6L6 Mode (Post Rock)           │
│   • TONE: Drive Mode                     │
│   • DRIVE: 11-1點鐘                      │
│   ↓                                      │
│ ④ Cornerstone Colosseum - 雙通道         │
│   • MODE: Klon → BB 順序                 │
│   • KLON SIDE: Drive 10-12點鐘           │
│   • BB SIDE: Drive 11-1點鐘, Clean 9-11點│
│   • CLIP BLENDER: 混合兩側               │
│   ↓                                      │
│ ⑤ TWA Source Code                        │
│   • DRIVE: 10-12點鐘                     │
│   • BITE CONTROL: 調整諧波               │
│   ↓                                      │
│ ⑥ Free the Tone ODL-1-CS                 │
│   • CHANNEL: Drive Channel               │
│   • VOLTAGE: 14-16V                      │
│   • MODE: ROCK Mode                      │
│   ↓                                      │
│ Loop 2 Return                            │
└──────────────────────────────────────────┘
  ↓
┌──────────────────────────────────────────┐
│ BOOSTER (20dB Clean Boost)               │
│ • Solo 時踩下                            │
│ • Boost Gain: 可調（最高 20dB）          │
└──────────────────────────────────────────┘
  ↓
OUTPUT A → Time-Based Effects Chain
```

---

#### Time-Based Effects Chain（Swiss Things 之後）

```
OUTPUT A (Swiss Things)
  ↓
┌──────────────────────────────────────────┐
│ ⑦ Free the Tone FT-1Y Delay              │
│                                          │
│ Jazz/Neo Soul:                           │
│ • TIME: 1/4 note                         │
│ • FEEDBACK: 3-4 repeats                  │
│ • MIX: 20-40%                            │
│ • REALTIME BPM ANALYZER: ON              │
│                                          │
│ Post Rock:                               │
│ • TIME: 長 Delay (1/2, 1/1 note)         │
│ • FEEDBACK: 高（建構 Pad）               │
│ • MIX: 40-70%                            │
│ • HOLD: 開啟                             │
└──────────────────────────────────────────┘
  ↓
┌──────────────────────────────────────────┐
│ ⑧ Lichtlaerm AASB Shimmer Reverb         │
│                                          │
│ Jazz/Neo Soul: Bypass                    │
│                                          │
│ Post Rock:                               │
│ • MODE: Above / Both                     │
│ • MIX: 60-90%                            │
│ • FREEZE: 開啟                           │
└──────────────────────────────────────────┘
  ↓
┌──────────────────────────────────────────┐
│ ⑨ Cornerstone Nucleo Reverb              │
│                                          │
│ Jazz/Neo Soul:                           │
│ • MODE: Room / Hall                      │
│ • BLEND: 30-50%                          │
│ • VOICING: Normal                        │
│                                          │
│ Post Rock:                               │
│ • MODE: Reactor（核電廠）                │
│ • DECAY: 60-90秒                         │
│ • BLEND: 50-80%                          │
│ • FREEZE: 開啟                           │
└──────────────────────────────────────────┘
  ↓
🎛️ Amp Input (Tone King Imperial MKII 或 Roland JC-22)
```

---

## 開關與操作邏輯

### Swiss Things 腳踏開關配置

Swiss Things 有 **5 個腳踏開關**：

```
┌─────────────────────────────────────────┐
│          SWISS THINGS 開關布局           │
├─────────────────────────────────────────┤
│                                         │
│   [Both]          [A/B]                 │
│   左上            右上                   │
│                                         │
│                                         │
│              [Boost]                    │
│               中央                       │
│                                         │
│                                         │
│   [Loop 2]        [Loop 1]              │
│   左下            右下                   │
│                                         │
└─────────────────────────────────────────┘
```

---

### 開關功能定義（整合後）

#### 1. Loop 1 開關（右下）- **訊號鏈 1 開關**
- **功能**: 啟動/關閉 Jazz/Neo Soul 訊號鏈
- **Flexi-Switch®**:
  - 輕踩一次: 開啟訊號鏈 1（Sweet Honey + Colosseum Klon）
  - 再踩一次: 關閉訊號鏈 1
  - 長按: 瞬間開啟（放開時關閉）

**適用場景:**
- Jazz Clean → Jazz Solo（踩下 Loop 1，加入 OD）
- Neo Soul Rhythm → Neo Soul Lead

---

#### 2. Loop 2 開關（左下）- **訊號鏈 2 開關**
- **功能**: 啟動/關閉 Post Rock 訊號鏈
- **Flexi-Switch®**:
  - 輕踩一次: 開啟訊號鏈 2（Blacklon + Colosseum + TWA + ODL-1-CS）
  - 再踩一次: 關閉訊號鏈 2
  - 長按: 瞬間開啟（放開時關閉）

**適用場景:**
- Clean Ambient → Post Rock Gain Wall（踩下 Loop 2）
- Fusion Clean → Fusion Driven

---

#### 3. Boost 開關（中央）- **Solo Boost**
- **功能**: 20dB Clean Boost（所有 Loop 之後）
- **Flexi-Switch®**:
  - 輕踩一次: 開啟 Boost
  - 再踩一次: 關閉 Boost
  - 長按: 瞬間 Boost（Solo 時）

**適用場景:**
- 任何風格的 Solo Boost
- 推動後級音箱

---

#### 4. A/B 開關（右上）- **音箱選擇**
- **功能**: 選擇 Output A 或 Output B
- **非 Flexi-Switch（標準 Toggle）**

**設定:**
- **A 位置**: 訊號送至 Output A（主音箱）
- **B 位置**: 訊號送至 Output B（第二台音箱，變壓器隔離）

**適用場景:**
- 單音箱設定 → 選 A
- 雙音箱設定 → 配合 Both 開關使用

---

#### 5. Both 開關（左上）- **雙音箱/Stereo**
- **功能**: 同時啟動 Output A 和 Output B
- **Flexi-Switch®**:
  - 輕踩一次: 同時開啟 A+B
  - 再踩一次: 關閉
  - 長按: 瞬間 A+B

**適用場景:**
- 雙音箱設定（Wet/Dry）
- Stereo Reverb（Nucleo Stereo 輸出）

---

## 實際演出場景切換

### 場景 1: Jazz Clean Tone

**目標**: 極度透明、保留撥弦動態

**開關設定:**
- Loop 1: **OFF**
- Loop 2: **OFF**
- Boost: **OFF**
- A/B: **A**
- Both: **OFF**

**訊號流程:**
```
Guitar → Empress MKII → PA-1QG (Preset 3, Throbber +6dB)
→ Swiss Things (兩個 Loop 都 Bypass)
→ FT-1Y (細微 Delay) → Nucleo (Hall, Blend 20%)
→ Tone King Imperial MKII Rhythm
```

**音色特點:**
- 完全 Clean（無 OD）
- Empress MKII 提供透明壓縮
- PA-1QG LEVEL +6dB 補償 Throbber 低輸出

---

### 場景 2: Neo Soul Rhythm

**目標**: 溫暖甜美、中等增益

**開關設定:**
- Loop 1: **ON**
- Loop 2: **OFF**
- Boost: **OFF**
- A/B: **A**
- Both: **OFF**

**訊號流程:**
```
Guitar → Empress MKII → PA-1QG (Preset 2, Greco +3dB)
→ [Loop 1: Sweet Honey → Colosseum Klon Boost]
→ FT-1Y (BPM 同步) → Nucleo (Room, Blend 30-50%)
→ Roland JC-22 (Chorus ON)
```

**音色特點:**
- Sweet Honey 溫暖 OD（Drive 11-12點鐘）
- Colosseum Klon Boost 推動，增加穿透力
- JC-22 Chorus 增加寬度

---

### 場景 3: Neo Soul Solo

**目標**: 音量提升、更多 Gain

**開關設定:**
- Loop 1: **ON**
- Loop 2: **OFF**
- Boost: **ON** ← 新增
- A/B: **A**
- Both: **OFF**

**訊號流程:**
```
Guitar → Empress MKII → PA-1QG (Preset 2)
→ [Loop 1: Sweet Honey → Colosseum Klon]
→ Boost +15dB ← 額外 Solo Boost
→ FT-1Y → Nucleo
→ JC-22
```

**音色特點:**
- 基於 Neo Soul Rhythm
- Swiss Things Boost 提供額外 +15dB（Solo 音量）
- 保持 Sweet Honey 音色不變

---

### 場景 4: Post Rock Ambient Clean

**目標**: 厚重 Pad、長 Delay、Shimmer

**開關設定:**
- Loop 1: **OFF**
- Loop 2: **OFF** ← 先 Clean
- Boost: **OFF**
- A/B: **A**
- Both: **OFF**

**訊號流程:**
```
Guitar → Cali76 FET (增加 Sustain) → PA-1QG (Preset 1, ESP EC 0dB)
→ Swiss Things (兩個 Loop Bypass)
→ FT-1Y (Hold, 長 Delay) → AASB (Above/Both, Freeze) → Nucleo (Reactor, Decay 60-90秒, Freeze)
→ Tone King Imperial MKII / JC-22
```

**音色特點:**
- Clean Tone + Cali76 Sustain
- FT-1Y Hold 建構 Pad
- AASB + Nucleo 雙 Freeze 創造天空音景

---

### 場景 5: Post Rock Gain Wall

**目標**: 多層 OD 疊加、音牆效果

**開關設定:**
- Loop 1: **OFF**
- Loop 2: **ON** ← 開啟訊號鏈 2
- Boost: **OFF**（或視需求）
- A/B: **A**
- Both: **OFF**

**訊號流程:**
```
Guitar → Cali76 FET → PA-1QG (Preset 1)
→ [Loop 2: Roshi Blacklon → Colosseum (BB+Klon 雙通道) → TWA Source Code → ODL-1-CS]
→ FT-1Y (Hold) → AASB (Freeze) → Nucleo (Reactor, Freeze)
→ Amp
```

**音色特點:**
- 4 顆 OD 層次疊加（Blacklon → Colosseum → TWA → ODL-1-CS）
- Cali76 FET 染色 + Sustain
- 複雜 Gain 結構 + Ambient 音景

---

### 場景 6: Classic Rock Crunch

**目標**: TS 中頻突出、Vintage Crunch

**開關設定:**
- Loop 1: **OFF**
- Loop 2: **ON**
- Boost: **OFF**
- A/B: **A**
- Both: **OFF**

**訊號流程:**
```
Guitar → Cali76 FET → PA-1QG (Preset 7, Post Rock EQ)
→ [Loop 2: Roshi Blacklon (6L6 + Drive) → TWA Source Code (TS 中頻) → Colosseum BB]
→ FT-1Y → Nucleo (Hall)
→ Tone King Imperial MKII Lead (Mid-Bite ON)
```

**音色特點:**
- Roshi Blacklon 提供 Blackface Crunch
- TWA Source Code 提供 TS 特有中頻突出（800Hz-1.5kHz）
- Colosseum BB 增加開放感
- Imperial MKII Mid-Bite 增加 Punch

---

### 場景 7: 實驗疊加（兩組訊號鏈同時開啟）

**目標**: 6 顆 OD 全開，極端 Gain

**開關設定:**
- Loop 1: **ON** ← 同時開啟
- Loop 2: **ON** ← 同時開啟
- Boost: **視需求**
- A/B: **A**
- Both: **OFF**

**訊號流程:**
```
Guitar → Cali76 FET → PA-1QG
→ [Loop 1: Sweet Honey → Colosseum Klon]
→ [Loop 2: Roshi Blacklon → Colosseum (雙通道) → TWA → ODL-1-CS]
→ 總共 6 顆 OD 串聯（實驗音色）
→ FT-1Y → AASB → Nucleo
→ Amp
```

**注意:**
- **這是實驗性配置**，音色可能過於飽和
- 可用於 Doom Metal、Noise Rock、實驗音樂
- 需小心控制各 OD 的 Drive 與 Volume

---

## Pedalboard 配置圖

### 完整 Pedalboard 布局（含 Swiss Things）

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PEDALBOARD TOP VIEW                              │
│                    (推薦尺寸: 32" × 16" 或更大)                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  [Row 1 - 最上排]                                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────────────┐    │
│  │ Empress  │  │ Cali76   │  │  PA-1QG  │  │   SWISS THINGS       │    │
│  │  MKII    │  │   FET    │  │          │  │   (4.75"×5.65")      │    │
│  │(選擇一個) │  │(選擇一個) │  │          │  │                     │    │
│  └──────────┘  └──────────┘  └──────────┘  │  [Both]    [A/B]    │    │
│                                             │                     │    │
│                                             │      [Boost]        │    │
│  [Row 2 - 訊號鏈 1 (Loop 1)]                 │                     │    │
│  ┌──────────┐  ┌──────────┐                │ [Loop2]   [Loop1]   │    │
│  │  Sweet   │  │Colosseum │                └─────────────────────┘    │
│  │  Honey   │  │Klon Side │                                           │
│  └──────────┘  └──────────┘                                           │
│                                                                        │
│  [Row 3 - 訊號鏈 2 (Loop 2) - Part 1]                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                            │
│  │  Roshi   │  │Colosseum │  │   TWA    │                            │
│  │ Blacklon │  │(雙通道)   │  │  Source  │                            │
│  └──────────┘  └──────────┘  └──────────┘                            │
│                                                                        │
│  [Row 4 - 訊號鏈 2 (Loop 2) - Part 2 + Time-Based]                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ ODL-1-CS │  │  FT-1Y   │  │   AASB   │  │  Nucleo  │             │
│  │ (Dumble) │  │ (Delay)  │  │(Shimmer) │  │ (Reverb) │             │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘             │
│                                                                        │
│  [Under Pedalboard - 電源供應器]                                        │
│  ┌───────────────────────────────────────────────────────────┐        │
│  │  Truetone CS12 或 Strymon Zuma (12+ outputs)              │        │
│  └───────────────────────────────────────────────────────────┘        │
│                                                                        │
└─────────────────────────────────────────────────────────────────────────┘

總效果器數: 11 顆（含 Swiss Things）
尺寸需求: 建議 Pedaltrain Terra 42 或 Temple Audio DUO 34
```

---

### 連接導線規劃

#### Input 連接
```
Guitar → Compressor (Empress 或 Cali76) → PA-1QG → SWISS THINGS INPUT
```

#### Swiss Things 內部連接

**Loop 1 (訊號鏈 1):**
```
Loop 1 Send → Sweet Honey Input
Sweet Honey Output → Colosseum Input
Colosseum Output → Loop 1 Return
```

**Loop 2 (訊號鏈 2):**
```
Loop 2 Send → Roshi Blacklon Input
Blacklon Output → Colosseum Input
Colosseum Output → TWA Source Code Input
TWA Output → ODL-1-CS Input
ODL-1-CS Output → Loop 2 Return
```

**Tuner:**
```
TUNER OUTPUT → TC Polytune / Boss TU-3 (Always-on)
```

#### Output 連接
```
OUTPUT A → FT-1Y Input
FT-1Y Output → AASB Input
AASB Output → Nucleo Input
Nucleo Output → Amp Input
```

---

## 供電與佈線計畫

### 電源需求總計

| 效果器 | 電壓 | 電流 |
|--------|------|------|
| Swiss Things | 9V | 40mA |
| Empress MKII | 9V | 50mA |
| Cali76 FET | 9V | 40mA |
| PA-1QG | 12V | 200mA |
| Sweet Honey | 9V | 20mA |
| Colosseum | 9V | 80mA |
| Roshi Blacklon | 9V | 30mA |
| TWA Source Code | 9V | 25mA |
| ODL-1-CS | 12V | 180mA |
| FT-1Y | 12V | 250mA |
| AASB | 9V | 100mA |
| Nucleo | 9V | 150mA |
| **總計 (9V)** | - | **535mA** |
| **總計 (12V)** | - | **630mA** |

---

### 推薦電源供應器

#### 選項 1: Truetone CS12（推薦）
- **12 個輸出**（8×100mA, 2×250mA, 2×500mA）
- **價格**: ~$200 USD
- **配置方案**:
  - Output 1-8 (100mA): Swiss Things, Empress, Cali76, Sweet Honey, Colosseum, Blacklon, TWA, AASB
  - Output 9 (250mA): Nucleo (需 150mA，裕度充足)
  - Output 10 (250mA): FT-1Y (需 250mA，使用 Voltage Doubler 升至 12V)
  - Output 11 (500mA): PA-1QG (需 200mA @ 12V，使用 Voltage Doubler)
  - Output 12 (500mA): ODL-1-CS (需 180mA @ 12V，使用 Voltage Doubler)

**需購買**: 3 條 Truetone Voltage Doubler Cable（9V→12V）
- PA-1QG, ODL-1-CS, FT-1Y 各需一條

---

#### 選項 2: Strymon Zuma（高階）
- **9 個輸出**（全部 500mA）
- **2 個可調電壓輸出**（9/12/18V）
- **價格**: ~$280 USD
- **優勢**: 原生 12V 輸出，不需 Voltage Doubler

**配置方案**:
- Output 1-7 (500mA @ 9V): Swiss Things, Empress, Cali76, Sweet Honey, Colosseum, Blacklon, TWA
- Output 8 (500mA @ 12V): PA-1QG + ODL-1-CS（並聯，總 380mA < 500mA）
- Output 9 (500mA @ 12V): FT-1Y

---

### 線材需求

**Patch Cable（Pedalboard 內部）:**
- EBS Flat Patch Cable 或 Mogami 短線
- 需求數量：約 15-18 條（10cm, 15cm, 20cm 混合）
- 預估成本：$90-120 USD

**Swiss Things 專用線材:**
- Loop 1 Send/Return: 2 條
- Loop 2 Send/Return: 2 條
- Tuner Output: 1 條
- Total: 5 條短線（15-20cm）

**Input/Output 線材:**
- Guitar → Pedalboard: 1 條標準導線（3-5m）
- Pedalboard → Amp: 1 條標準導線（1-2m）
- 預估成本：$40-60 USD

**總線材成本**: ~$130-180 USD

---

## 與原 V2.0 方案對比

### 方案對比表

| 項目 | V2.0 原方案 | V2.0 + Swiss Things | 差異 |
|------|------------|---------------------|------|
| **效果器數** | 10 顆核心 | 10 顆核心 + Swiss Things | +1 顆 |
| **Compressor 切換** | 手動換線 | 手動換線（相同） | 無差異 |
| **訊號鏈切換** | 手動換線重接 | **腳踏開關切換** | ✅ 大幅改善 |
| **Solo Boost** | PA-1QG Preset 8 (+9dB) | Swiss Things Boost (+20dB) | ✅ 更強 |
| **Tuner 連接** | 獨立 Tuner Out Pedal | Swiss Things Tuner Out | ✅ 簡化 |
| **Volume Control** | 無（或獨立 Volume Pedal） | Swiss Things Volume EXP | ✅ 新增 |
| **雙音箱支援** | 需獨立 ABY Box | Swiss Things 內建 AB-Y | ✅ 整合 |
| **總成本增加** | - | +$299（Swiss Things） | - |
| **Pedalboard 尺寸** | 24" × 12.5" | **32" × 16"**（更大） | ⚠️ 需升級 |

---

### 優勢分析

#### ✅ Swiss Things 帶來的核心優勢

1. **腳踏開關切換訊號鏈**
   - 原方案：需要手動拔插導線切換兩組訊號鏈（不可能演出中切換）
   - Swiss Things：Loop 1 / Loop 2 腳踏開關即時切換
   - **演出實用性提升 1000%**

2. **20dB Clean Boost（比 PA-1QG +9dB 更強）**
   - PA-1QG Preset 8 最高 +9dB
   - Swiss Things Boost 可達 +20dB
   - **Solo Boost 更強勁**

3. **Flexi-Switch® 技術**
   - Loop 1/2/Boost 都支援 **Momentary Mode**（長按瞬間開啟）
   - 可做瞬間 Boost、瞬間音色切換
   - **演奏技巧更豐富**

4. **內建 Tuner Output**
   - 不需獨立 Tuner Out Pedal
   - 節省 Pedalboard 空間與成本

5. **Volume EXP 功能**
   - 可連接任何 Expression Pedal 控制音量
   - Buffered，無 tone-suck
   - 傳統 Volume Pedal 的替代方案

6. **內建 AB-Y Switching**
   - Output B 有變壓器隔離 + Phase Switch
   - 支援雙音箱設定
   - 防止 Ground Loop

7. **Buffer 管理**
   - Loop 1 Unbuffered（保留 vintage pedal 特性）
   - Loop 2 Buffered（適合長線材與現代 pedal）
   - 智能 Buffer 配置

---

#### ⚠️ Swiss Things 的限制

1. **Pedalboard 尺寸增加**
   - Swiss Things 本身尺寸：4.75" × 5.65" × 2.25"（相當大）
   - 原方案 Pedaltrain Classic 2 (24" × 12.5") **不夠用**
   - 需升級至 **Pedaltrain Terra 42 (42" × 16")** 或 **Temple Audio DUO 34 (34" × 12.6")**
   - 增加成本：$200-300 USD

2. **供電需求增加**
   - Swiss Things 需 40mA @ 9V（不多）
   - 但總效果器數增加，電源供應器壓力增大

3. **佈線複雜度增加**
   - Swiss Things 有 9 個連接埠（Input, Output A/B, Loop 1/2 Send/Return, Tuner, Volume EXP）
   - Patch cable 需求增加約 5-8 條
   - 佈線時間增加

4. **成本增加**
   - Swiss Things: $299 USD
   - 升級 Pedalboard: $200-300 USD
   - 額外線材: $50-80 USD
   - **總增加成本: $549-679 USD**

5. **Loop 2 設計非為 Gain Pedals 優化**
   - Loop 2 原設計為 Buffered（給 Time-based effects）
   - 放置 4 顆 OD（Blacklon + Colosseum + TWA + ODL-1-CS）可能有輕微音色影響
   - 但現代 OD 通常不受 Buffer 影響（測試後確認）

---

### 是否值得整合 Swiss Things？

#### 建議整合（如果符合以下條件）

✅ **演出需求高**
- 需要在演出中快速切換 Jazz/Neo Soul 和 Post Rock 兩種風格
- 需要腳踏開關而非手動換線

✅ **Solo Boost 需求**
- 需要強勁的 Solo Boost（+20dB）
- PA-1QG 的 +9dB 不足

✅ **雙音箱設定**
- 計畫使用兩台音箱（Wet/Dry 或 Stereo）
- 需要 AB-Y Switching 與變壓器隔離

✅ **Expression Pedal Volume**
- 想用 Expression Pedal 控制音量
- 避免傳統 Volume Pedal 的 tone-suck

✅ **預算充足**
- 可接受增加 $549-679 USD 投資

---

#### 不建議整合（如果符合以下條件）

❌ **僅在家練習**
- 不需要演出中切換訊號鏈
- 手動換線可接受

❌ **預算有限**
- $549-679 USD 增加成本太高
- 寧願投資其他效果器

❌ **Pedalboard 空間受限**
- 無法容納 32" 以上的大型 Pedalboard
- 攜帶性重要

❌ **訊號鏈固定**
- 只使用一組訊號鏈（Jazz 或 Post Rock）
- 不需要切換功能

---

## 實施建議與注意事項

### 實施步驟（如果決定整合 Swiss Things）

#### Phase 1: 採購與準備（第 1-2 週）

**必要採購:**
- [ ] Swiss Things (~$299 USD)
- [ ] 升級 Pedalboard（推薦 Pedaltrain Terra 42 或 Temple DUO 34）(~$200-300 USD)
- [ ] 額外 Patch Cable 5-8 條 (~$30-50 USD)
- [ ] Truetone Voltage Doubler Cable × 3（如使用 CS12）(~$30-45 USD)

**總預算:** ~$559-694 USD

---

#### Phase 2: Swiss Things 功能測試（第 3 週）

**測試項目:**
1. **Loop 1/2 Bypass 測試**
   - 確認 Loop 關閉時訊號完全 Bypass
   - 測試 True Bypass 是否乾淨（無 pop 聲）

2. **Flexi-Switch® 測試**
   - 測試 Latching Mode（輕踩鎖定）
   - 測試 Momentary Mode（長按瞬間開啟）
   - 確認切換速度與可靠性

3. **Boost 測試**
   - 測試 Boost Gain 範圍（0-20dB）
   - 確認 Boost 是否乾淨（Clean Boost）
   - 測試 Boost 位置（所有 Loop 之後）

4. **Tuner Output 測試**
   - 連接 Tuner，確認 Always-on 需求
   - 測試是否有 Ground Loop 或 Hum

5. **Volume EXP 測試**
   - 連接 Expression Pedal
   - 測試音量控制範圍與 Tone-suck

---

#### Phase 3: 訊號鏈整合測試（第 4-5 週）

**訊號鏈 1（Loop 1）測試:**
```
PA-1QG → Swiss Things INPUT → Loop 1 Send
→ Sweet Honey → Colosseum Klon → Loop 1 Return
→ OUTPUT A → FT-1Y → Nucleo → Amp
```

**測試項目:**
- [ ] Loop 1 ON: Sweet Honey + Colosseum Klon 音色正常
- [ ] Loop 1 OFF: 訊號完全 Bypass（Clean Tone）
- [ ] Unbuffered 特性是否保留（與直接連接無差異）

**訊號鏈 2（Loop 2）測試:**
```
PA-1QG → Swiss Things INPUT → Loop 2 Send
→ Blacklon → Colosseum → TWA → ODL-1-CS → Loop 2 Return
→ OUTPUT A → FT-1Y → Nucleo → Amp
```

**測試項目:**
- [ ] Loop 2 ON: 4 顆 OD 音色正常
- [ ] Loop 2 OFF: 訊號完全 Bypass
- [ ] Buffered 對 OD 音色影響（應該極小）

**雙 Loop 疊加測試:**
```
Loop 1 ON + Loop 2 ON = 6 顆 OD 串聯
```

**測試項目:**
- [ ] 音色是否過於飽和
- [ ] 各 OD 的 Volume 需調整以平衡
- [ ] 實用性評估（可能僅實驗用途）

---

#### Phase 4: Pedalboard 配置與佈線（第 6-8 週）

**配置步驟:**
1. 規劃 Pedalboard 布局（參考本文 Pedalboard 配置圖）
2. 安裝電源供應器於 Pedalboard 底部
3. 固定所有效果器（使用 Velcro 或 Temple Audio 插板）
4. 佈線連接（Input → Swiss Things → Loop 1/2 → Output）
5. 供電連接（確認所有電壓正確）
6. Cable Management（整理線材，避免雜亂）

**佈線注意事項:**
- Swiss Things 的 Loop Send/Return 使用 **短線材**（15-20cm）
- 避免長線材造成訊號損耗
- 使用高品質 Patch Cable（Mogami, EBS Flat Patch）
- Tuner Output 必須使用 **短線材**（避免 Ground Loop）

---

#### Phase 5: 實際演出測試（第 9-12 週）

**練團測試:**
1. 測試場景 1-7 的快速切換
2. 確認 Flexi-Switch® 的可靠性
3. 測試 Boost 的實用性（Solo 時）
4. 測試雙音箱設定（如適用）

**問題排查:**
- 若有 Ground Loop Hum → 檢查 Tuner 是否 Always-on
- 若切換有 Pop 聲 → 檢查 Swiss Things 供電
- 若音色有變化 → 檢查 Loop 2 Buffered 影響

---

### 關鍵注意事項

#### ⚠️ Swiss Things 使用警告

1. **Tuner 必須 Always-On**
   - Swiss Things 的 TUNER OUTPUT 是從 Input Buffer 分支
   - 若 Tuner Bypass，會造成 Ground Loop 和 Hum
   - 使用支援 Always-on 的 Tuner（TC Polytune, Boss TU-3）

2. **供電電壓嚴格限制**
   - Swiss Things **僅支援 9V DC**
   - **絕對不可使用 12V 或 18V**（會損壞電路）
   - 使用 Isolated Power Supply（避免 Ground Loop）

3. **Loop 2 不可空接作為 Mute**
   - 原 Swiss Things 設計：Loop 2 空接時可作 Mute
   - 本方案 Loop 2 放置 4 顆 OD，**不可空接**
   - 若需 Mute 功能，使用獨立 Mute Pedal

4. **Output B Phase Switch 使用時機**
   - **單音箱設定**: Phase Switch 關閉
   - **雙音箱設定**: 依音箱特性調整（若聲音怪異，嘗試切換）
   - **Stereo Effects 後**: Phase Switch **必須關閉**（否則 L/R 相位相反）

5. **Expression Pedal 相容性**
   - Swiss Things Volume EXP 支援任何 Expression Pedal
   - 推薦：Moog EP-3, Boss EV-30, Mission Engineering EP-1
   - **不建議使用傳統 Volume Pedal**（阻抗不匹配）

---

## 總結與最終建議

### Swiss Things 整合價值評估

**核心價值:**
- ✅ **腳踏開關切換兩組訊號鏈**（演出必備）
- ✅ **20dB Clean Boost**（強勁 Solo Boost）
- ✅ **Flexi-Switch® Momentary Mode**（演奏技巧豐富）
- ✅ **內建 AB-Y + Tuner Out + Volume EXP**（多功能整合）

**增加成本:**
- Swiss Things: $299 USD
- 升級 Pedalboard: $200-300 USD
- 線材: $50-80 USD
- **總計: $549-679 USD**

---

### 最終建議

#### 情境 A: 演出導向 → **強烈推薦整合 Swiss Things**

如果你：
- 經常演出，需要在台上快速切換風格
- 需要 Solo Boost（+20dB）
- 計畫使用雙音箱或 Stereo 設定
- 預算充足（$549-679 USD 可接受）

**結論:** Swiss Things 是 **必備工具**，大幅提升演出實用性。

---

#### 情境 B: 練習/錄音導向 → **可選，非必要**

如果你：
- 主要在家練習或錄音室
- 可手動切換訊號鏈（拔插導線）
- 預算有限
- Pedalboard 空間受限

**結論:** Swiss Things 是 **錦上添花**，但非必要。原 V2.0 方案已足夠。

---

### 替代方案（不使用 Swiss Things）

如果不整合 Swiss Things，可考慮：

**方案 1: 使用簡單 Loop Switcher**
- 例如：Boss LS-2 Line Selector (~$120 USD)
- 可切換 Loop A / Loop B
- 但無 Boost, Tuner Out, Volume EXP 等功能

**方案 2: 使用 MIDI Loop Switcher**
- 例如：RJM Mastermind PBC/6X (~$600-800 USD)
- 可 MIDI 控制 PA-1QG + FT-1Y + Nucleo
- 但成本更高

**方案 3: 維持手動切換**
- 不增加任何設備
- 演出前手動重接訊號鏈
- 成本 $0，但演出靈活性低

---

**文件完成**

此整合方案提供完整的 Swiss Things 與 V2.0 效果器配置整合邏輯，包含訊號鏈設計、開關邏輯、Pedalboard 配置、供電計畫，以及實施步驟與注意事項。

**下一步:** 請決定是否整合 Swiss Things，若決定整合，可開始 Phase 1 採購與準備。🎸
