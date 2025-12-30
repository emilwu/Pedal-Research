# EarthQuaker Devices Swiss Things® - 訊號路徑邏輯完整文件

**版本:** 1.0
**建立日期:** 2025-12-22
**用途:** 供 AI Agent 理解並建立 Swiss Things 訊號鏈配置

---

## 核心功能概述

Swiss Things 是一個全功能訊號路徑管理中心（Pedalboard Reconciler），整合以下功能：
- 2個 Flexi-Switch® 效果循環（Loop 1: 無緩衝 / Loop 2: 有緩衝）
- AB-Y 切換器（Output B 具變壓器隔離）
- 緩衝調音器輸出
- 20dB 乾淨增益
- Expression Pedal 音量控制輸出
- 高動態範圍輸出緩衝

**建議位置:** Pedalboard 右上角

---

## 技術規格

| 項目 | 規格 |
|------|------|
| **尺寸** | 4.75" × 5.65" × 2.25" |
| **電流消耗** | 40 mA |
| **輸入阻抗** | 1 MΩ |
| **輸出阻抗** | 1 kΩ |
| **供電** | 9V DC (2.1mm center-negative) |
| **Bypass 類型** | Relay-based True Bypass (需供電) |

---

## 訊號路徑方塊圖邏輯

### 完整訊號流程（由左至右）

```
🎸 Guitar
  ↓
INPUT (1/4" Jack) ← [Always-on pedals 應放在此之前]
  ↓
┌─────────────────────────────────────────────────────┐
│                    BUFFER (Input)                    │
│              (Input Impedance: 1 MΩ)                │
└─────────────────────────────────────────────────────┘
  ↓
  ├──→ TUNER OUTPUT (Buffered, Always-on required)
  ↓
┌─────────────────────────────────────────────────────┐
│         EFFECTS LOOP 1 (Unbuffered)                 │
│    Flexi-Switch® (Latching + Momentary)             │
│                                                      │
│    SEND → [OD/Distortion/Fuzz Pedals] → RETURN     │
│                                                      │
│    用途: Boost, Overdrive, Distortion, Fuzz         │
│    特性: 無緩衝，保留 vintage 效果器特性             │
│    當空接時: 正常訊號通過                            │
└─────────────────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────────────────┐
│                    BUFFER                            │
│         (Loop 1 後方的內部緩衝)                      │
└─────────────────────────────────────────────────────┘
  ↓
  ├──→ VOLUME EXP OUTPUT (Buffered Expression Pedal)
  │    位置: Loop 1 後方，可控制音量但不影響增益
  ↓
┌─────────────────────────────────────────────────────┐
│         EFFECTS LOOP 2 (Buffered)                   │
│    Flexi-Switch® (Latching + Momentary)             │
│                                                      │
│    SEND → [Delay/Reverb/Modulation] → RETURN       │
│                                                      │
│    用途: Time-based & Modulation effects           │
│    特性: 有緩衝，適合 delay/reverb/chorus/phaser   │
│    當空接時: 作為 MUTE 功能                         │
└─────────────────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────────────────┐
│              BOOSTER (up to 20dB)                   │
│         Flexi-Switch® (Latching + Momentary)        │
│         位置: Post-effects loops                     │
│         用途: Output booster                         │
└─────────────────────────────────────────────────────┘
  ↓
┌─────────────────────────────────────────────────────┐
│                    BUFFER                            │
│         (Output Impedance: 1 kΩ)                    │
└─────────────────────────────────────────────────────┘
  ↓
  ├────────────────────────────┬─────────────────────┐
  │                            │                     │
  │ A/B Switch                 │  Both Flexi-Switch® │
  │                            │                     │
  ↓                            ↓                     ↓
OUTPUT A                   OUTPUT B              OUTPUT A+B
(Direct)              (Transformer-Isolated)    (同時輸出)
                       + Phase Switch
```

---

## 五個主要腳踏開關功能

### 1. Loop 1 開關（右下）

**功能:** 啟動/關閉 Effects Loop 1
**電路特性:** 無緩衝（Unbuffered）
**Flexi-Switch®:**
- **輕踩一次 (Latching):** 開啟 Loop 1，再踩一次關閉
- **長按 (Momentary):** 按住時開啟，放開時關閉

**適用效果器:**
- Boost / Overdrive / Distortion / Fuzz
- Vintage pedals
- 低輸入阻抗效果器（需與拾音器直接互動）

**訊號路徑:**
```
Input Buffer → Loop 1 Send → [你的 OD/Dist/Fuzz 效果器鏈] → Loop 1 Return → 繼續
```

---

### 2. Loop 2 開關（左下）

**功能:** 啟動/關閉 Effects Loop 2
**電路特性:** 有緩衝（Buffered）
**Flexi-Switch®:**
- **輕踩一次 (Latching):** 開啟 Loop 2，再踩一次關閉
- **長按 (Momentary):** 按住時開啟，放開時關閉

**適用效果器:**
- Delay / Reverb / Modulation
- Chorus / Phaser / Flanger
- 所有 time-based effects

**特殊功能:**
⚠️ **當 Loop 2 Send/Return 空接時，Loop 2 開關作為 MUTE（靜音）功能**

**訊號路徑:**
```
Loop 1 後 → Loop 2 Send → [你的 Delay/Reverb/Mod 效果器鏈] → Loop 2 Return → 繼續
```

---

### 3. Boost 開關（中央）

**功能:** 啟動 20dB 乾淨增益
**位置:** Post-effects loops（所有 Loop 之後）
**Flexi-Switch®:**
- **輕踩一次 (Latching):** 開啟 Boost，再踩一次關閉
- **長按 (Momentary):** 按住時開啟，放開時關閉

**用途:**
- Solo boost
- 整體輸出音量提升
- 推動後級音箱

**控制旋鈕:**
- **Boost Gain:** 可調整 Boost 量（最高 20dB）

---

### 4. A/B 開關（右上）

**功能:** 選擇 Output A 或 Output B
**非 Flexi-Switch（標準 Toggle）**

**模式:**
- **A 位置:** 訊號僅送至 Output A
- **B 位置:** 訊號僅送至 Output B

**Output B 特性:**
- 變壓器隔離（Transformer-Isolated）
- 具備 Phase Switch（相位反轉開關）
- 用於多音箱設定，防止 ground loop 和相位問題

---

### 5. Both 開關（左上）

**功能:** 同時啟動 Output A 和 Output B
**Flexi-Switch®:**
- **輕踩一次 (Latching):** 同時開啟 A+B，再踩一次關閉
- **長按 (Momentary):** 按住時 A+B 開啟，放開時關閉

**用途:**
- 雙音箱設定
- 立體聲效果（需配合 stereo effects）

**重要注意:**
- 使用 Stereo effects 時，應將 stereo pedals 放在 Output A 和 Output B **之後**
- 兩個 Output 都必須使用 Both 開關選擇
- 如使用 stereo effects，請勿開啟 Phase Switch，否則 L/R 會相位相反

---

## 輸入/輸出連接埠邏輯

### 訊號輸入

#### 1. INPUT (吉他輸入)
- **位置:** 右側
- **功能:** 連接吉他或樂器
- **阻抗:** 1 MΩ
- **重要:** Always-on pedals（Compressor, Preamp, EQ）應放在此之前

---

### Loop 1 連接埠（右側中段）

#### 2. Loop 1 SEND
- **功能:** 連接至第一顆 gain-type pedal 的輸入
- **訊號:** 來自 Input Buffer

#### 3. Loop 1 RETURN
- **功能:** 連接至最後一顆 gain-type pedal 的輸出
- **訊號:** 返回 Swiss Things 繼續處理

**建議連接範例:**
```
Loop 1 Send → Boost → Overdrive → Distortion → Fuzz → Loop 1 Return
```

---

### Loop 2 連接埠（右側上段）

#### 4. Loop 2 SEND
- **功能:** 連接至第一顆 modulation/time-based pedal 的輸入
- **訊號:** 來自 Loop 1 後的 Buffer

#### 5. Loop 2 RETURN
- **功能:** 連接至最後一顆 modulation/time-based pedal 的輸出
- **訊號:** 返回 Swiss Things 繼續處理

**建議連接範例:**
```
Loop 2 Send → Chorus → Delay → Reverb → Loop 2 Return
```

---

### 輔助輸出

#### 6. TUNER OUTPUT (右側最上方)
- **功能:** 連接調音器（Tuner）
- **特性:** Buffered output
- **⚠️ 重要:** 調音器必須**永遠開啟**，若 bypass 會造成 ground loop 或 hum

#### 7. VOLUME EXP (右側下方)
- **功能:** 連接任何 Expression Pedal 以控制音量
- **位置:** Loop 1 之後，Boost 之前
- **優勢:**
  - 避免傳統 Volume Pedal 的 tone-suck 問題
  - Buffered output
  - 可在不影響增益的情況下調整音量
  - 任何 Expression Pedal 皆可使用

---

### 訊號輸出

#### 8. OUTPUT A (左上)
- **功能:** 連接至主音箱
- **特性:** 直接輸出，無隔離
- **阻抗:** 1 kΩ

#### 9. OUTPUT B (左上，A 旁)
- **功能:** 連接至第二台音箱
- **特性:**
  - **變壓器隔離（Transformer-Isolated）**
  - **具備 Phase Switch（相位開關）**
- **用途:**
  - 多音箱設定
  - Stereo 設定
  - 避免 ground loop
  - 處理相位反轉的音箱/效果器

**Phase Switch 位置:** Output B 上方的小型 toggle switch

**Phase Switch 使用時機:**
- 當使用的音箱或效果器會反轉相位時，開啟 Phase Switch
- **注意:** 若在 Swiss Things **之後**使用 stereo effects，請勿開啟 Phase Switch，否則 L/R 會相位相反

---

## 訊號鏈建構邏輯（給 AI Agent 的規則）

### 規則 1: Always-On Pedals 位置

**必須放在 Swiss Things INPUT 之前的效果器:**
- Compressor（壓縮器）
- Preamp（前級）
- EQ（等化器）
- Buffer（緩衝器）
- 任何需要 "always-on" 的 pedal

**訊號鏈:**
```
🎸 Guitar → Compressor → EQ → INPUT (Swiss Things)
```

---

### 規則 2: Loop 1 配置（Gain Section）

**Loop 1 應放置的效果器類型:**
- Boost
- Overdrive
- Distortion
- Fuzz
- Octave (如 octave-fuzz)
- Vintage pedals
- 任何不喜歡被 buffer 的效果器

**特性:**
- 無緩衝（Unbuffered）
- True Bypass（透過 Flexi-Switch®）
- 保留 pickup 與效果器的直接互動

**建議順序（Loop 1 內部）:**
```
Loop 1 Send → Octave → Fuzz → Overdrive → Distortion → Boost → Loop 1 Return
```

或依個人喜好:
```
Loop 1 Send → Boost → Overdrive → Distortion → Fuzz → Loop 1 Return
```

---

### 規則 3: Loop 2 配置（Modulation/Time Section）

**Loop 2 應放置的效果器類型:**
- Delay
- Reverb
- Chorus
- Phaser
- Flanger
- Tremolo
- Vibrato
- 所有 time-based 和 modulation effects

**特性:**
- 有緩衝（Buffered）
- True Bypass（透過 Flexi-Switch®）

**建議順序（Loop 2 內部）:**
```
Loop 2 Send → Chorus → Phaser → Delay → Reverb → Loop 2 Return
```

或更複雜:
```
Loop 2 Send → Phaser → Flanger → Chorus → Delay → Reverb → Loop 2 Return
```

---

### 規則 4: Stereo Effects 配置

**若使用 Stereo Effects，有兩種方式:**

#### 方式 A: Stereo Effects 在 Swiss Things 之前（Mono → Stereo）
```
🎸 Guitar → [Mono Chain] → INPUT (Swiss Things)
→ Loop 1 (Mono) → Loop 2 (Mono) → Boost
→ OUTPUT A → Stereo Effect Input L
→ OUTPUT B → Stereo Effect Input R
→ Stereo Effect Output L → Amp 1
→ Stereo Effect Output R → Amp 2
```

**此方式設定:**
- 使用 Both 開關同時啟動 A+B
- **Phase Switch 關閉**（否則 L/R 會相位相反）

#### 方式 B: Stereo Effects 在 Loop 2 內（需 Stereo Loop Pedals）
```
🎸 Guitar → INPUT → Loop 1 (Mono)
→ Loop 2 Send → [Stereo Delay/Reverb with Stereo I/O] → Loop 2 Return
→ OUTPUT A (Left) → Amp 1
→ OUTPUT B (Right) → Amp 2
```

**此方式設定:**
- Loop 2 需使用支援 Stereo 的效果器
- 使用 Both 開關同時啟動 A+B
- **Phase Switch 關閉**

---

### 規則 5: 雙音箱設定

#### 配置 1: 兩台相同音箱（Wet/Dry 或 Stereo）
```
OUTPUT A → Amp 1 (Main)
OUTPUT B → Amp 2 (Secondary)
```

**設定:**
- Both 開關開啟
- Phase Switch 依需求調整（若有 hum 或音色怪異，嘗試切換）

#### 配置 2: 兩台不同音箱（避免 Ground Loop）
```
OUTPUT A → Fender Amp (Direct)
OUTPUT B → Marshall Amp (Transformer-Isolated)
```

**設定:**
- Both 開關開啟
- Output B 的變壓器隔離可防止 ground loop
- Phase Switch 依音箱特性調整

---

### 規則 6: Expression Pedal Volume 配置

**連接:**
```
VOLUME EXP → Expression Pedal (如 Moog EP-3, Boss EV-30)
```

**特性:**
- 位置在 Loop 1 之後，Loop 2 之前
- 可調整音量但不影響 Loop 1 的 gain 特性
- Buffered output，無 tone-suck
- 任何 Expression Pedal 皆可使用（不限 volume pedal）

**優勢:**
- 傳統 Volume Pedal 會有 "tone-suck"（訊號損耗）
- Swiss Things 的 buffered output 解決此問題
- 可用便宜的 Expression Pedal 達成相同效果

---

### 規則 7: Tuner 配置

**連接:**
```
TUNER OUTPUT → Tuner Input
```

**⚠️ 重要規則:**
- Tuner **必須永遠開啟**（Always-on）
- **不可將 Tuner bypass**，否則會造成:
  - Ground loop（地迴路）
  - Hum（嗡嗡聲）
  - 訊號問題

**建議 Tuner:**
- TC Electronic Polytune
- Boss TU-3
- Korg Pitchblack
- 任何有 "always-on" 模式的 Tuner

---

## 完整訊號鏈範例

### 範例 1: 基礎 Rock/Blues 配置

```
🎸 Guitar
  ↓
Compressor (Origin Effects Cali76)
  ↓
EQ (Boss GE-7)
  ↓
──────────────────────────────────────
         SWISS THINGS INPUT
──────────────────────────────────────
  ↓
  ├→ TUNER OUT → TC Polytune (Always-on)
  ↓
[Loop 1 - Unbuffered]
  Send → Boost → Overdrive → Fuzz → Return
  ↓
  ├→ VOLUME EXP → Expression Pedal
  ↓
[Loop 2 - Buffered]
  Send → Chorus → Delay → Reverb → Return
  ↓
[Boost] (關閉或視需要)
  ↓
OUTPUT A → Fender Deluxe Reverb
OUTPUT B → (未使用)
```

**開關設定:**
- Loop 1: 開啟
- Loop 2: 開啟
- Boost: 關閉（或視需要）
- A/B: 選 A
- Both: 關閉

---

### 範例 2: 雙音箱 + Stereo Reverb 配置

```
🎸 Guitar
  ↓
Preamp (Free the Tone PA-1QG)
  ↓
──────────────────────────────────────
         SWISS THINGS INPUT
──────────────────────────────────────
  ↓
  ├→ TUNER OUT → Boss TU-3 (Always-on)
  ↓
[Loop 1 - Unbuffered]
  Send → OD1 → OD2 → Distortion → Return
  ↓
  ├→ VOLUME EXP → Boss FV-500H
  ↓
[Loop 2 - Buffered]
  Send → Modulation → Delay → Return
  ↓
[Boost] +10dB (Solo 時使用)
  ↓
OUTPUT A → Strymon BigSky (Input L) → Amp 1
OUTPUT B → Strymon BigSky (Input R) → Amp 2
```

**開關設定:**
- Loop 1: 開啟
- Loop 2: 開啟
- Boost: Solo 時踩下
- A/B: 無關（Both 啟動時無作用）
- Both: 開啟
- Phase Switch: **關閉**（Stereo effects 需同相位）

---

### 範例 3: 極簡 Neo Soul 配置

```
🎸 Guitar
  ↓
Empress MKII Compressor
  ↓
──────────────────────────────────────
         SWISS THINGS INPUT
──────────────────────────────────────
  ↓
  ├→ TUNER OUT → Tuner (Always-on)
  ↓
[Loop 1 - Unbuffered]
  Send → Sweet Honey OD → Soul Food → Return
  ↓
  ├→ VOLUME EXP → (未使用)
  ↓
[Loop 2 - Buffered - 作為 MUTE]
  (空接，可作靜音開關)
  ↓
[Boost] (未使用)
  ↓
OUTPUT A → Roland JC-22
```

**開關設定:**
- Loop 1: 開啟
- Loop 2: 當需要靜音時踩下（Mute 功能）
- Boost: 關閉
- A/B: 選 A
- Both: 關閉

---

### 範例 4: Post Rock / Ambient 完整配置

```
🎸 Guitar
  ↓
Cali76 FET Compressor
  ↓
──────────────────────────────────────
         SWISS THINGS INPUT
──────────────────────────────────────
  ↓
  ├→ TUNER OUT → Tuner (Always-on)
  ↓
[Loop 1 - Unbuffered]
  Send → Roshi Blacklon → Colosseum → ODL-1-CS → Return
  ↓
  ├→ VOLUME EXP → Expression Pedal
  ↓
[Loop 2 - Buffered]
  Send → Modulation → Delay (with Hold) → Return
  ↓
[Boost] +15dB
  ↓
OUTPUT A → Lichtlaerm AASB Shimmer → Amp 1 (L)
OUTPUT B → Nucleo Reverb Stereo In → Amp 2 (R)
```

**開關設定:**
- Loop 1: 開啟
- Loop 2: 開啟
- Boost: Ambient Swell 時使用
- A/B: 無關
- Both: 開啟（Stereo）
- Phase Switch: **關閉**

---

## Flexi-Switch® 技術說明

### 什麼是 Flexi-Switch®？

Flexi-Switch® 是 EarthQuaker Devices 的專利技術，結合兩種開關模式：

#### 模式 1: Latching（鎖定模式）
- **操作:** 輕踩一次開啟，再踩一次關閉
- **用途:** 一般效果器開關使用

#### 模式 2: Momentary（瞬間模式）
- **操作:** 按住開關時效果開啟，放開時效果關閉
- **用途:**
  - 瞬間 boost
  - 瞬間效果（如瞬間 reverb tail）
  - 動態演奏技巧

### 支援 Flexi-Switch® 的開關

Swiss Things 上的 5 個開關中，**4 個**支援 Flexi-Switch®：

✅ Loop 1 開關 - Flexi-Switch®
✅ Loop 2 開關 - Flexi-Switch®
✅ Boost 開關 - Flexi-Switch®
❌ A/B 開關 - 標準 Toggle（不支援）
✅ Both 開關 - Flexi-Switch®

### 技術特性

- **Relay-based switching（繼電器切換）**
- **True Bypass**
- **需要供電才能通過訊號**（無電時無訊號）

---

## 給 AI Agent 的建構指南

### 建構訊號鏈時的決策樹

```
開始建構訊號鏈
  ↓
1. 是否有 Always-on pedals（Comp/EQ/Preamp）？
   ├─ 是 → 放在 Swiss Things INPUT 之前
   └─ 否 → 吉他直接進 INPUT
  ↓
2. 分類效果器:
   ├─ Gain-type (OD/Dist/Fuzz/Boost) → Loop 1 候選
   ├─ Time/Mod (Delay/Reverb/Chorus/Phaser) → Loop 2 候選
   └─ Stereo effects → 決定放在 Output 之後或 Loop 2 內
  ↓
3. Loop 1 內部順序:
   ├─ 傳統順序: Octave → Fuzz → OD → Dist → Boost
   └─ 或依使用者喜好調整
  ↓
4. Loop 2 內部順序:
   ├─ 傳統順序: Mod (Chorus/Phaser) → Delay → Reverb
   └─ 或依使用者喜好調整
  ↓
5. 是否使用 Volume control？
   ├─ 是 → VOLUME EXP → Expression Pedal
   └─ 否 → 跳過
  ↓
6. 是否需要 Output Boost？
   ├─ 是 → 設定 Boost 開關與 Gain 量
   └─ 否 → Boost 關閉
  ↓
7. 輸出配置:
   ├─ 單音箱 → OUTPUT A，A/B 選 A
   ├─ 雙音箱（Mono）→ OUTPUT A+B，Both 開啟
   └─ Stereo → OUTPUT A+B，Both 開啟，Phase 關閉
  ↓
8. Tuner 連接:
   └─ TUNER OUTPUT → Tuner (Always-on)
  ↓
完成
```

---

## 常見問題處理邏輯

### Q1: Loop 2 可以當作 Mute 嗎？

**A:** 是的！

**設定方式:**
- 不要連接任何效果器到 Loop 2 Send/Return
- Loop 2 開關踩下時 = 訊號靜音（Mute）
- Loop 2 開關放開時 = 訊號通過

**應用場景:**
- 換吉他時靜音
- 調整效果器時靜音
- 演出時快速靜音

---

### Q2: 為什麼 Tuner 必須 Always-on？

**A:** 技術原因

**原因:**
- TUNER OUTPUT 是從 Input Buffer 分支出來的
- 若 Tuner bypass，會造成開放電路（open circuit）
- 開放電路會導致:
  - Ground loop（地迴路）
  - Hum/Buzz（嗡嗡聲/雜訊）
  - 訊號不穩定

**解決方案:**
- 使用有 "always-on" 模式的 Tuner
- 或使用 buffered tuner
- 不要使用 true-bypass tuner

---

### Q3: Output B 的 Phase Switch 何時使用？

**A:** 特定情況

**使用時機:**
1. **音箱會反轉相位時**
   - 某些音箱設計會反轉相位
   - 開啟 Phase Switch 可補償

2. **與特定效果器搭配時**
   - 某些效果器（如特定 Fuzz）會反轉相位
   - 需要實驗調整

**不使用時機:**
1. **使用 Stereo Effects 時**
   - 若 Phase Switch 開啟，L/R 會相位相反
   - 會造成聲音怪異、抵銷

**判斷方式:**
- 若雙音箱聲音怪異、薄弱、低頻消失 → 嘗試切換 Phase Switch
- 若雙音箱聲音正常飽滿 → Phase Switch 保持關閉

---

### Q4: Expression Pedal 和 Volume Pedal 的差異？

**A:** Expression Pedal 更優

**傳統 Volume Pedal 問題:**
- 高阻抗設計，會 "load down" 訊號
- Tone-suck（訊號衰減、高頻損失）
- 行程有限

**Swiss Things VOLUME EXP 優勢:**
- Buffered output（緩衝輸出）
- 無 tone-suck
- 可用任何便宜的 Expression Pedal
- 位置在 Loop 1 後，可調音量不影響 gain

**建議 Expression Pedals:**
- Moog EP-3
- Boss EV-30
- Mission Engineering EP-1
- Dunlop DVP4
- 任何 Expression Pedal 皆可

---

### Q5: 可以在 Loop 內再串聯 Loop Switcher 嗎？

**A:** 可以，但通常不必要

**可行配置:**
```
Loop 1 Send → [Loop Switcher 管理 6 顆 OD] → Loop 1 Return
```

**優勢:**
- 更細緻的效果器管理
- 可組合複雜音色

**缺點:**
- 增加複雜度
- Swiss Things 本身已提供 Flexi-Switch® 功能
- 可能造成訊號損耗

**建議:**
- 若效果器少於 6 顆，直接用 Swiss Things
- 若超過 10 顆且需要複雜切換，可考慮 Loop Switcher

---

## 供電需求與注意事項

### 電源規格

- **電壓:** 9V DC
- **電流:** 40 mA
- **接頭:** 2.1mm center-negative（標準 Boss 規格）
- **建議電源:**
  - Isolated power supply（隔離電源）
  - Truetone CS12
  - Strymon Zuma
  - Voodoo Lab Pedal Power

### ⚠️ 重要警告

**不可使用高於 9V 的電壓！**
- Swiss Things 僅支援 9V
- 使用 12V 或 18V 會損壞電路

**建議使用 isolated output:**
- Swiss Things 整合多個電路
- Isolated power 可避免 ground loop
- 避免與高電流效果器（如數位 Delay）共用 daisy chain

---

## 進階應用：4-Cable Method (4CM) 整合

Swiss Things 可完美整合 4-Cable Method 配置

### 4CM 概念

將效果器鏈分為兩段：
1. **前級效果（Preamp）** → 音箱 Input 前
2. **後級效果（FX Loop）** → 音箱 Effects Loop 內

### Swiss Things + 4CM 配置

```
🎸 Guitar
  ↓
[Always-on Pedals]
  ↓
SWISS THINGS INPUT
  ↓
Loop 1 (OD/Dist/Fuzz) ← 前級效果
  ↓
OUTPUT A → 🎛️ AMP INPUT
  ↓
🎛️ AMP PREAMP 處理
  ↓
🎛️ AMP FX SEND → Loop 2 Send (Swiss Things)
  ↓
Loop 2 (Delay/Reverb/Mod) ← 後級效果
  ↓
Loop 2 Return → 🎛️ AMP FX RETURN
  ↓
🎛️ AMP POWER AMP → Speaker
```

### 優勢

- Loop 1 效果進入音箱前級（可與音箱前級互動）
- Loop 2 效果在音箱後級（避免被音箱前級失真影響）
- Delay/Reverb 音色更乾淨清晰
- 可使用音箱本身的失真特性

### 適用音箱

需支援 Effects Loop 的音箱：
- Fender Hot Rod Deluxe
- Marshall JCM800
- Mesa Boogie Mark V
- Tone King Imperial MKII
- 等等

---

## 總結：給 AI Agent 的核心邏輯

建構 Swiss Things 訊號鏈時，遵循以下核心邏輯：

### 1. 訊號流向（由前至後）

```
Guitar → Always-on → INPUT → Loop 1 → Volume EXP → Loop 2 → Boost → Output
                        ↓
                    Tuner Out
```

### 2. 效果器分類

- **Loop 1 (Unbuffered):** Gain-type（OD/Dist/Fuzz/Boost）
- **Loop 2 (Buffered):** Time/Mod（Delay/Reverb/Chorus/Phaser）
- **Always-on:** Comp/EQ/Preamp（INPUT 之前）
- **Stereo Effects:** Output A/B 之後

### 3. 開關邏輯

- **Loop 1/2/Boost/Both:** 支援 Flexi-Switch®（Latching + Momentary）
- **A/B:** 標準 Toggle（擇一輸出）
- **Both:** 同時輸出 A+B（Stereo 或雙音箱）

### 4. 特殊功能

- **Loop 2 空接 = Mute**
- **TUNER OUT 必須 Always-on**
- **VOLUME EXP 可用任何 Expression Pedal**
- **Output B 有變壓器隔離 + Phase Switch**

### 5. 避免問題

- Tuner 不可 bypass
- Stereo 時 Phase Switch 關閉
- 不可超過 9V 供電
- 使用 isolated power supply

---

**文件結束**

此文件提供完整的 Swiss Things 訊號路徑邏輯，供 AI Agent 理解並建立訊號鏈配置使用。
