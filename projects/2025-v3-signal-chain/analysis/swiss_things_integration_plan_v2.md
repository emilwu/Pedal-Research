# Swiss Things 整合方案 - V3.0 效果器配置

**版本:** 2.0
**建立日期:** 2025-12-30
**基於:** signal_chain_v3.md + swiss_things_signal_routing_logic.md
**目標:** 透過 Swiss Things 切換兩組訊號鏈（Jazz/Neo Soul 與 Post Rock）- V3.0 版本

---

## 執行摘要

Swiss Things 的核心優勢是 **2 個獨立 Effects Loop**（Loop 1 無緩衝 + Loop 2 有緩衝），完美對應 V3.0 的兩組訊號鏈設計：

- **Loop 1 (Unbuffered)**: 放置 Jazz/Neo Soul 訊號鏈（Sweet Honey + PRS Horsemeat）
- **Loop 2 (Buffered)**: 放置 Post Rock 訊號鏈（Blacklon + Morning Glory + TWA Source + ODL-1-CS）
- **Swiss Things 之前**: Always-on pedals（Empress MKII / Cali76 FET + PA-1QG）
- **Swiss Things 之後**: Time-based effects（FT-1Y + AASB + Nucleo）

透過腳踏開關，可在演出中快速切換兩組訊號鏈，實現：
- **Loop 1 ON, Loop 2 OFF** = Jazz/Neo Soul 音色
- **Loop 1 OFF, Loop 2 ON** = Post Rock/Fusion 音色
- **Loop 1 ON, Loop 2 ON** = 疊加所有 OD（實驗音色）

### V3.0 版本特點

相較於 V2.0 整合方案，本版本的關鍵變更：
- **移除**: Cornerstone Colosseum（雙通道 OD）
- **新增**: PRS Horsemeat（訊號鏈1）+ JHS Morning Glory V3（訊號鏈2）
- **效果器總數**: 11顆核心 + Swiss Things = 12顆
- **理念**: 單功能專用效果器，訊號鏈更單純

---

## 目錄

1. [Swiss Things 核心功能回顧](#swiss-things-核心功能回顧)
2. [V3.0 效果器配置分析](#v30-效果器配置分析)
3. [整合策略：訊號鏈設計](#整合策略訊號鏈設計)
4. [完整訊號鏈配置](#完整訊號鏈配置)
5. [開關與操作邏輯](#開關與操作邏輯)
6. [實際演出場景切換](#實際演出場景切換)
7. [Pedalboard 配置圖](#pedalboard-配置圖)
8. [供電與佈線計畫](#供電與佈線計畫)
9. [與 V2.0 整合方案對比](#與-v20-整合方案對比)
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

## V3.0 效果器配置分析

### 11 顆核心效果器分類

根據 signal_chain_v3.md，效果器分為：

#### 類別 1: Always-On Pedals（Swiss Things INPUT 之前）
1. **Empress MKII** - 透明壓縮（Jazz/Neo Soul）
2. **Cali76 FET** - 染色壓縮（Post Rock）
3. **PA-1QG** - EQ + Clean Boost

#### 類別 2: Gain-Type Pedals（Swiss Things Loop 內）
**訊號鏈 1（Jazz/Neo Soul）:**
4. **Sweet Honey Deluxe** - 溫暖 OD
5. **PRS Horsemeat** - ⭐ V3.0 新增：Klon-style 透明 Boost

**訊號鏈 2（Post Rock）:**
6. **Roshi Blacklon** - Amp-in-a-Box
7. **JHS Morning Glory V3** - ⭐ V3.0 新增：Bluesbreaker OD
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
- 只需 **2 顆 OD**（Sweet Honey + PRS Horsemeat）
- 音色導向：**透明、溫暖、Clean**
- ⭐ V3.0 變更：Horsemeat 取代 Colosseum Klon Side

**訊號鏈 2（Post Rock）:**
- 使用 **Cali76 FET**（染色壓縮）
- 需要 **4 顆 OD**（Blacklon + Morning Glory + TWA + ODL-1-CS）
- 音色導向：**層次豐富、Gain 疊加、Ambient**
- ⭐ V3.0 變更：Morning Glory 取代 Colosseum BB Side

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
   - 訊號鏈 1 的 Sweet Honey + Horsemeat 都是 OD
   - 完美匹配

2. ✅ **Loop 2 是 Buffered**（原設計給 Time-based，但也可放 OD）
   - 訊號鏈 2 的 Blacklon + Morning Glory + TWA + ODL-1-CS 都是 OD
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
│ Send → Sweet Honey → PRS Horsemeat → Return │
│        ⭐ V3.0: Horsemeat 取代 Colosseum  │
└──────────────────────────────────────────┘
  ↓
  ├→ VOLUME EXP → Expression Pedal
  ↓
┌──────────────────────────────────────────┐
│ Loop 2 (Buffered) - 訊號鏈 2              │
│ Post Rock / Fusion                       │
│                                          │
│ Send → Roshi Blacklon → JHS Morning Glory │
│     → TWA Source Code → ODL-1-CS → Return │
│        ⭐ V3.0: Morning Glory 取代 Colosseum │
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
│ ② PRS Horsemeat                          │
│   ⭐ V3.0 新增：取代 Colosseum Klon       │
│   • DRIVE: 9-10點鐘（低 Gain）           │
│   • VOLUME: 2點鐘（Boost 模式）          │
│   • TONE: 12-1點鐘                       │
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
│ ④ JHS Morning Glory V3                   │
│   ⭐ V3.0 新增：取代 Colosseum BB         │
│   • GAIN: 10-12點鐘                      │
│   • VOLUME: 12-1點鐘                     │
│   • TONE: 12點鐘                         │
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

### 開關功能定義（V3.0 整合後）

#### 1. Loop 1 開關（右下）- **訊號鏈 1 開關**
- **功能**: 啟動/關閉 Jazz/Neo Soul 訊號鏈
- **Flexi-Switch®**:
  - 輕踩一次: 開啟訊號鏈 1（Sweet Honey + PRS Horsemeat）
  - 再踩一次: 關閉訊號鏈 1
  - 長按: 瞬間開啟（放開時關閉）

**適用場景:**
- Jazz Clean → Jazz Solo（踩下 Loop 1，加入 OD）
- Neo Soul Rhythm → Neo Soul Lead

---

#### 2. Loop 2 開關（左下）- **訊號鏈 2 開關**
- **功能**: 啟動/關閉 Post Rock 訊號鏈
- **Flexi-Switch®**:
  - 輕踩一次: 開啟訊號鏈 2（Blacklon + Morning Glory + TWA + ODL-1-CS）
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
→ [Loop 1: Sweet Honey → PRS Horsemeat]
→ FT-1Y (BPM 同步) → Nucleo (Room, Blend 30-50%)
→ Roland JC-22 (Chorus ON)
```

**音色特點:**
- Sweet Honey 溫暖 OD（Drive 11-12點鐘）
- ⭐ V3.0: PRS Horsemeat 透明 Boost，增加中頻穿透力
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
→ [Loop 1: Sweet Honey → PRS Horsemeat]
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
→ [Loop 2: Roshi Blacklon → JHS Morning Glory → TWA Source Code → ODL-1-CS]
→ FT-1Y (Hold) → AASB (Freeze) → Nucleo (Reactor, Freeze)
→ Amp
```

**音色特點:**
- ⭐ V3.0: 4 顆 OD 層次疊加（Blacklon → Morning Glory → TWA → ODL-1-CS）
- Morning Glory 提供經典 BB 開放感，無 clipping 問題
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
→ [Loop 2: Roshi Blacklon (6L6 + Drive) → Morning Glory → TWA Source Code (TS 中頻)]
→ FT-1Y → Nucleo (Hall)
→ Tone King Imperial MKII Lead (Mid-Bite ON)
```

**音色特點:**
- Roshi Blacklon 提供 Blackface Crunch
- ⭐ V3.0: Morning Glory BB 增加開放感與動態
- TWA Source Code 提供 TS 特有中頻突出（800Hz-1.5kHz）
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
→ [Loop 1: Sweet Honey → PRS Horsemeat]
→ [Loop 2: Roshi Blacklon → JHS Morning Glory → TWA → ODL-1-CS]
→ 總共 6 顆 OD 串聯（實驗音色）
→ FT-1Y → AASB → Nucleo
→ Amp
```

**注意:**
- **這是實驗性配置**，音色可能過於飽和
- ⭐ V3.0: 單功能效果器疊加，比 V2.0 Colosseum 雙通道更清晰可控
- 可用於 Doom Metal、Noise Rock、實驗音樂
- 需小心控制各 OD 的 Drive 與 Volume

---

## Pedalboard 配置圖

### 完整 Pedalboard 布局（含 Swiss Things - V3.0）

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PEDALBOARD TOP VIEW - V3.0                       │
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
│  [Row 2 - 訊號鏈 1 (Loop 1)] ⭐ V3.0 變更    │                     │    │
│  ┌──────────┐  ┌──────────┐                │ [Loop2]   [Loop1]   │    │
│  │  Sweet   │  │   PRS    │                └─────────────────────┘    │
│  │  Honey   │  │Horsemeat │ ⭐ 取代 Colosseum Klon                     │
│  └──────────┘  └──────────┘                                           │
│                                                                        │
│  [Row 3 - 訊號鏈 2 (Loop 2) - Part 1] ⭐ V3.0 變更                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                            │
│  │  Roshi   │  │   JHS    │  │   TWA    │                            │
│  │ Blacklon │  │ Morning  │  │  Source  │                            │
│  │          │  │ Glory V3 │  │          │                            │
│  └──────────┘  └──────────┘  └──────────┘                            │
│                 ⭐ 取代 Colosseum BB                                    │
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

總效果器數: 12 顆（11 顆核心 + Swiss Things）
⭐ V3.0 變更: Horsemeat 取代 Colosseum Klon, Morning Glory 取代 Colosseum BB
尺寸需求: 建議 Pedaltrain Terra 42 或 Temple Audio DUO 34
```

---

### 連接導線規劃

#### Input 連接
```
Guitar → Compressor (Empress 或 Cali76) → PA-1QG → SWISS THINGS INPUT
```

#### Swiss Things 內部連接

**Loop 1 (訊號鏈 1 - V3.0):**
```
Loop 1 Send → Sweet Honey Input
Sweet Honey Output → PRS Horsemeat Input ⭐ V3.0
Horsemeat Output → Loop 1 Return
```

**Loop 2 (訊號鏈 2 - V3.0):**
```
Loop 2 Send → Roshi Blacklon Input
Blacklon Output → JHS Morning Glory Input ⭐ V3.0
Morning Glory Output → TWA Source Code Input
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

### 電源需求總計（V3.0）

| 效果器 | 電壓 | 電流 | 備註 |
|--------|------|------|------|
| Swiss Things | 9V | 40mA | |
| Empress MKII | 9V | 50mA | |
| Cali76 FET | 9V | 40mA | |
| PA-1QG | 12V | 200mA | |
| Sweet Honey | 9V | 20mA | |
| **PRS Horsemeat** | **9V** | **~30mA** | ⭐ V3.0 新增 |
| Roshi Blacklon | 9V | 30mA | |
| **JHS Morning Glory V3** | **9V** | **~25mA** | ⭐ V3.0 新增 |
| TWA Source Code | 9V | 25mA | |
| ODL-1-CS | 12V | 180mA | |
| FT-1Y | 12V | 250mA | |
| AASB | 9V | 100mA | |
| Nucleo | 9V | 150mA | |
| **總計 (9V)** | - | **~510mA** | V3.0: -80mA (移除 Colosseum) +55mA (Horsemeat + Morning Glory) |
| **總計 (12V)** | - | **630mA** | 無變化 |

---

### 推薦電源供應器

#### 選項 1: Truetone CS12（推薦）
- **12 個輸出**（8×100mA, 2×250mA, 2×500mA）
- **價格**: ~$200 USD
- **配置方案**:
  - Output 1-9 (100mA): Swiss Things, Empress, Cali76, Sweet Honey, Horsemeat, Blacklon, Morning Glory, TWA, AASB
  - Output 10 (250mA): Nucleo (需 150mA，裕度充足)
  - Output 11 (250mA): FT-1Y (需 250mA，使用 Voltage Doubler 升至 12V)
  - Output 12 (500mA): PA-1QG + ODL-1-CS（並聯 @ 12V，使用 Voltage Doubler）

**需購買**: 2-3 條 Truetone Voltage Doubler Cable（9V→12V）
- PA-1QG, ODL-1-CS, FT-1Y 各需一條（或 PA-1QG + ODL-1-CS 共用一個 12V output）

---

#### 選項 2: Strymon Zuma（高階）
- **9 個輸出**（全部 500mA）
- **2 個可調電壓輸出**（9/12/18V）
- **價格**: ~$280 USD
- **優勢**: 原生 12V 輸出，不需 Voltage Doubler

**配置方案**:
- Output 1-8 (500mA @ 9V): Swiss Things, Empress, Cali76, Sweet Honey, Horsemeat, Blacklon, Morning Glory, TWA, AASB, Nucleo（分配）
- Output 9 (500mA @ 12V): PA-1QG + ODL-1-CS + FT-1Y（並聯，總 630mA > 500mA，需分配）

**實際配置**:
- 需使用 2 個 12V 輸出，或搭配 Zuma Ojai 擴充

---

### 線材需求

**Patch Cable（Pedalboard 內部）:**
- EBS Flat Patch Cable 或 Mogami 短線
- 需求數量：約 16-19 條（10cm, 15cm, 20cm 混合）
- ⭐ V3.0: 相較 V2.0 方案，線材需求相同（移除 Colosseum 雙通道，但新增兩顆單通道）
- 預估成本：$95-130 USD

**Swiss Things 專用線材:**
- Loop 1 Send/Return: 2 條
- Loop 2 Send/Return: 2 條
- Tuner Output: 1 條
- Total: 5 條短線（15-20cm）

**Input/Output 線材:**
- Guitar → Pedalboard: 1 條標準導線（3-5m）
- Pedalboard → Amp: 1 條標準導線（1-2m）
- 預估成本：$40-60 USD

**總線材成本**: ~$135-190 USD

---

## 與 V2.0 整合方案對比

### 方案對比表

| 項目 | V2.0 整合方案 | V3.0 整合方案 | 差異 |
|------|--------------|--------------|------|
| **效果器數** | 10 顆核心 + Swiss Things | 11 顆核心 + Swiss Things | +1 顆 |
| **訊號鏈1 OD** | Sweet Honey + Colosseum Klon | Sweet Honey + PRS Horsemeat | ⭐ 單功能專用 |
| **訊號鏈2 OD** | Blacklon + Colosseum (BB+Klon) + TWA + ODL | Blacklon + Morning Glory + TWA + ODL | ⭐ 單功能專用 |
| **Compressor 切換** | 手動換線 | 手動換線（相同） | 無差異 |
| **訊號鏈切換** | **腳踏開關切換** | **腳踏開關切換** | 無差異 |
| **Solo Boost** | Swiss Things Boost (+20dB) | Swiss Things Boost (+20dB) | 無差異 |
| **雙通道彈性** | ✅ Colosseum 可 BB+Klon 同時 | ❌ 失去雙通道疊加 | ⚠️ V3.0 劣勢 |
| **Clip Blender** | ✅ Colosseum 創意功能 | ❌ 失去 Clip Blender | ⚠️ V3.0 劣勢 |
| **Morning Glory BB** | ❌ 無 | ✅ 經典 BB 音色 | ✅ V3.0 優勢 |
| **訊號鏈複雜度** | 中（Colosseum 雙通道） | 低（單功能效果器） | ✅ V3.0 優勢 |
| **總成本增加** | +$299（Swiss Things） | +$299（Swiss Things） | 無差異 |
| **Pedalboard 尺寸** | 32" × 16" | 32" × 16" | 無差異 |

---

### V3.0 整合方案的關鍵差異

#### ✅ V3.0 優勢

1. **單功能效果器專注性**
   - PRS Horsemeat 專注於 Klon-style Boost，無其他通道干擾
   - JHS Morning Glory 專注於 BB Overdrive，經典音色
   - 訊號鏈更單純易懂

2. **Morning Glory 經典 BB 音色**
   - V1.0 原本因 Colosseum 而移除
   - 無 clipping 問題，動態自然
   - 開放清晰的 Bluesbreaker 特性

3. **PRS Horsemeat Klon 專業化**
   - 專業 Klon-style 設計
   - 極度透明的 Boost
   - 增加中頻穿透力

4. **Swiss Things 整合優勢（與 V2.0 方案相同）**
   - 腳踏開關切換兩組訊號鏈
   - 20dB Clean Boost（Solo Boost）
   - Flexi-Switch® Momentary Mode
   - 內建 AB-Y + Tuner Out + Volume EXP

---

#### ⚠️ V3.0 考量點

1. **失去 Colosseum 雙通道彈性**
   - V2.0 方案可在訊號鏈2同時使用 BB + Klon 雙通道
   - V3.0 訊號鏈2只有 Morning Glory BB OD（無 Klon）
   - 若需 Klon，需切換到訊號鏈1（Horsemeat）

2. **失去 Clip Blender 創意功能**
   - Colosseum 的 Clip Blender 可混合 Klon + BB 兩側 clipping
   - 創造獨特音色層次
   - V3.0 無此功能

3. **效果器數量增加**
   - V2.0 方案：10 顆核心 + Swiss Things = 11 顆
   - V3.0 方案：11 顆核心 + Swiss Things = 12 顆
   - 增加 1 顆（移除 Colosseum，新增 Horsemeat + Morning Glory）

4. **Loop 2 無 Klon Boost**
   - V2.0 訊號鏈2可使用 Colosseum Klon Side
   - V3.0 訊號鏈2無 Klon，僅 BB + TS + Dumble

---

### 選擇建議

#### 建議使用 V3.0 整合方案（如果符合以下條件）

✅ **偏好單功能專用效果器**
- 每顆效果器只負責一種核心音色
- 訊號鏈更簡單直觀

✅ **喜歡 Morning Glory 的經典 BB 音色**
- 無 clipping 問題
- 動態自然，開放清晰

✅ **不需要 Colosseum 的 Clip Blender 創意功能**
- 不使用 BB + Klon 雙通道疊加
- 不需要混合兩側 clipping

✅ **訊號鏈1 專用 Klon，訊號鏈2 專用 BB**
- 風格分離明確
- Jazz/Neo Soul = Klon Boost
- Post Rock = BB Overdrive

---

#### 建議使用 V2.0 整合方案（如果符合以下條件）

⚠️ **喜歡 Colosseum 雙通道的彈性**
- 需要在訊號鏈2同時使用 BB + Klon
- 需要 Clip Blender 功能

⚠️ **想減少效果器數量**
- V2.0 用 1 顆 Colosseum 抵 2 顆（Horsemeat + Morning Glory）
- Pedalboard 空間更節省

⚠️ **Clip Blender 創意功能重要**
- 需要混合 Klon + BB 兩側 clipping
- 創造獨特音色層次

---

## 實施建議與注意事項

### 實施步驟（如果決定整合 Swiss Things - V3.0）

#### Phase 1: 採購與準備（第 1-2 週）

**必要採購:**
- [ ] Swiss Things (~$299 USD)
- [ ] PRS Horsemeat (~$150-200 USD，請確認實際價格) ⭐ V3.0
- [ ] JHS Morning Glory V3 (~$150-180 USD) ⭐ V3.0
- [ ] 升級 Pedalboard（推薦 Pedaltrain Terra 42 或 Temple DUO 34）(~$200-300 USD)
- [ ] 額外 Patch Cable 5-8 條 (~$30-50 USD)
- [ ] Truetone Voltage Doubler Cable × 2-3（如使用 CS12）(~$30-45 USD)

**總預算:** ~$859-1074 USD
⭐ V3.0 額外成本: Horsemeat + Morning Glory (~$300-380 USD)

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

**訊號鏈 1（Loop 1）測試 - V3.0:**
```
PA-1QG → Swiss Things INPUT → Loop 1 Send
→ Sweet Honey → PRS Horsemeat → Loop 1 Return ⭐ V3.0
→ OUTPUT A → FT-1Y → Nucleo → Amp
```

**測試項目:**
- [ ] Loop 1 ON: Sweet Honey + Horsemeat 音色正常
- [ ] Horsemeat 透明度測試（與 Colosseum Klon 對比）
- [ ] Loop 1 OFF: 訊號完全 Bypass（Clean Tone）
- [ ] Unbuffered 特性是否保留

**訊號鏈 2（Loop 2）測試 - V3.0:**
```
PA-1QG → Swiss Things INPUT → Loop 2 Send
→ Blacklon → JHS Morning Glory → TWA → ODL-1-CS → Loop 2 Return ⭐ V3.0
→ OUTPUT A → FT-1Y → Nucleo → Amp
```

**測試項目:**
- [ ] Loop 2 ON: 4 顆 OD 音色正常
- [ ] Morning Glory BB 音色測試（與 Colosseum BB 對比）
- [ ] Morning Glory 無 clipping 問題確認
- [ ] Loop 2 OFF: 訊號完全 Bypass
- [ ] Buffered 對 OD 音色影響（應該極小）

**雙 Loop 疊加測試 - V3.0:**
```
Loop 1 ON + Loop 2 ON = 6 顆 OD 串聯
Sweet Honey → Horsemeat → Blacklon → Morning Glory → TWA → ODL-1-CS
```

**測試項目:**
- [ ] 音色是否過於飽和
- [ ] 各 OD 的 Volume 需調整以平衡
- [ ] 與 V2.0 方案（Colosseum 雙通道）對比
- [ ] 實用性評估

---

#### Phase 4: Pedalboard 配置與佈線（第 6-8 週）

**配置步驟:**
1. 規劃 Pedalboard 布局（參考本文 V3.0 Pedalboard 配置圖）
2. 安裝電源供應器於 Pedalboard 底部
3. 固定所有效果器（使用 Velcro 或 Temple Audio 插板）
4. 佈線連接（Input → Swiss Things → Loop 1/2 → Output）
5. ⭐ V3.0: 確認 Horsemeat 和 Morning Glory 位置正確
6. 供電連接（確認所有電壓正確）
7. Cable Management（整理線材，避免雜亂）

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
5. ⭐ V3.0: 對比 Horsemeat vs Colosseum Klon 音色差異
6. ⭐ V3.0: 對比 Morning Glory vs Colosseum BB 音色差異

**問題排查:**
- 若有 Ground Loop Hum → 檢查 Tuner 是否 Always-on
- 若切換有 Pop 聲 → 檢查 Swiss Things 供電
- 若音色有變化 → 檢查 Loop 2 Buffered 影響
- ⭐ V3.0: 若 Horsemeat 透明度不足 → 調整 DRIVE 與 VOLUME
- ⭐ V3.0: 若 Morning Glory 有 clipping → 檢查 GAIN 設定

---

### 關鍵注意事項

#### ⚠️ Swiss Things 使用警告（與 V2.0 方案相同）

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

#### ⭐ V3.0 特有注意事項

1. **PRS Horsemeat 設定**
   - DRIVE 保持在 9-10點鐘（低 Gain）
   - VOLUME 推至 2點鐘（Boost 模式）
   - 若透明度不足，降低 DRIVE，提高 VOLUME

2. **JHS Morning Glory V3 設定**
   - GAIN 保持在 10-12點鐘
   - 避免過高 GAIN（可能造成 clipping）
   - 利用 SWITCH 選擇適合的模式

3. **訊號鏈2無 Klon**
   - V3.0 訊號鏈2無 Klon Boost（Morning Glory 取代）
   - 若需 Klon 音色，切換到訊號鏈1（Horsemeat）
   - 或考慮在訊號鏈2加入 Klon pedal（需額外空間）

4. **失去 Clip Blender 功能**
   - V2.0 Colosseum 的 Clip Blender 無法在 V3.0 複製
   - 若此功能重要，考慮保留 V2.0 方案

---

## 總結與最終建議

### V3.0 Swiss Things 整合價值評估

**核心價值:**
- ✅ **腳踏開關切換兩組訊號鏈**（演出必備）
- ✅ **20dB Clean Boost**（強勁 Solo Boost）
- ✅ **Flexi-Switch® Momentary Mode**（演奏技巧豐富）
- ✅ **內建 AB-Y + Tuner Out + Volume EXP**（多功能整合）
- ⭐ **V3.0 新增：單功能專用效果器**（訊號鏈更單純）
- ⭐ **V3.0 新增：Morning Glory 經典 BB 音色**（無 clipping）

**增加成本（相較於原 V3.0 方案）:**
- Swiss Things: $299 USD
- 升級 Pedalboard: $200-300 USD
- 線材: $50-80 USD
- **總計: $549-679 USD**

**增加成本（相較於 V2.0 整合方案）:**
- Horsemeat + Morning Glory - Colosseum: ~$300-380 - $380 = -$80 to +$100 USD
- **總計: 與 V2.0 整合方案相近，或略微增加**

---

### 最終建議

#### 情境 A: 演出導向 + 偏好單功能效果器 → **強烈推薦 V3.0 整合方案**

如果你：
- 經常演出，需要在台上快速切換風格
- 偏好單功能專用效果器（每顆一個角色）
- 喜歡 Morning Glory 的經典 BB 音色
- 不需要 Colosseum 的 Clip Blender 功能
- 需要 Solo Boost（+20dB）
- 預算充足（$549-679 USD 可接受）

**結論:** V3.0 整合 Swiss Things 是 **最佳選擇**，訊號鏈單純且演出實用性高。

---

#### 情境 B: 演出導向 + 喜歡 Colosseum 雙通道 → **推薦 V2.0 整合方案**

如果你：
- 經常演出，需要腳踏開關切換
- 喜歡 Colosseum 雙通道的彈性（BB + Klon 同時使用）
- 需要 Clip Blender 創意功能
- 想減少效果器數量（1 顆抵 2 顆）

**結論:** V2.0 整合 Swiss Things 更適合，保留 Colosseum 獨特性。

---

#### 情境 C: 練習/錄音導向 → **可選，非必要**

如果你：
- 主要在家練習或錄音室
- 可手動切換訊號鏈（拔插導線）
- 預算有限
- Pedalboard 空間受限

**結論:** Swiss Things 是 **錦上添花**，但非必要。原 V3.0 方案已足夠。

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

此整合方案提供完整的 Swiss Things 與 V3.0 效果器配置整合邏輯，包含訊號鏈設計、開關邏輯、Pedalboard 配置、供電計畫，以及實施步驟與注意事項。相較於 V2.0 整合方案，本版本強調單功能專用效果器的優勢，以及 Morning Glory 經典 BB 音色的回歸。

**下一步:** 請決定是否整合 Swiss Things，並選擇 V2.0 或 V3.0 方案。若決定使用 V3.0 整合方案，可開始 Phase 1 採購與準備。🎸
