# Overdrive 效果器庫存分析報告

**建立日期:** 2026-01-02
**版本:** 1.0
**分析範圍:** 6 顆 Overdrive 效果器

---

## 一、完整庫存清單

| ID | 品牌 | 型號 | 類型 | Gain 範圍 | 價格 |
|---|---|---|---|---|---|
| sweet_honey | Mad Professor | Sweet Honey Deluxe | Transparent Warm | Low-Medium | $220 |
| prs_horsemeat | PRS | Horsemeat | Klon-style Transparent | Clean-Medium High | $279 |
| morning_glory | JHS | Morning Glory V3 | Bluesbreaker | Low-Medium | $179 |
| roshi_blacklon | Roshi | Blacklon | Amp Simulator | Variable | $200 |
| twa_source_code | TWA | Source Code | TS Evolution | Low-High | $299 |
| odl1cs | Free the Tone | ODL-1-CS | Dumble-style | Variable | $425 |

**總價值:** $1,602

---

## 二、核心特性分析

### 1. Sweet Honey Overdrive Deluxe (溫暖派)

**核心 DNA:** Honey Bee 演化，溫暖偶次諧波

**技術規格:**
- **Gain 範圍:** Low-Medium (比 TS 稍低)
- **頻率特性:** 溫暖中頻，可調 Bass (pre-gain) + Treble (post-gain)
- **動態:** 極高觸鍵敏感度，適中壓縮
- **電源:** 9V DC / Battery, 5mA
- **Bypass:** True Bypass

**獨特控制:**
- **FOCUS** - 調整失真起點與音色柔和度
  - CCW (逆時針): 需要更用力彈奏才產生失真，音色較柔和 (Jazz/Blues)
  - CW (順時針): 更早產生失真，帶有輕微高頻提升 (Classic Rock)

**音色特性:**
- **Gain Type:** Low-Medium Gain Overdrive
- **Frequency:** 溫暖、飽滿中頻，可調 Bass/Treble
- **Dynamics:** 極高觸鍵敏感度，適中且可調壓縮
- **Harmonics:** 溫暖、豐富，偏偶次諧波

**最適合:**
- Jazz, Neo Soul, Blues, Post Rock, Funk

**疊加特性:**
- 極佳疊加能力，適合作為底層溫暖音色
- 適合 always-on 使用模式

**訊號鏈配置:**
- Position: pre_amp_gain
- Swiss Things Assignment: loop_1
- Notes: 訊號鏈1核心溫暖 OD，Neo Soul 甜蜜點

---

### 2. PRS Horsemeat (透明派 - Klon 路線)

**核心 DNA:** Klon-inspired 但原創設計，Germanium 二極體

**技術規格:**
- **Gain 範圍:** Clean boost → Medium-high gain
- **頻率特性:** 溫暖飽滿，midrange richness，可能偏暗
- **動態:** 高觸鍵敏感度，Germanium 適中壓縮
- **電源:** 9V DC, 16mA
- **Bypass:** True Bypass
- **Diodes:** Germanium (提供溫暖而不刺耳的音色)

**獨特控制:**
- **VOICE** - 核心秘密武器
  - 從 saturated meaty distortion 到 glassy singing overdrive 的連續變化
  - 需要時間習慣，但提供極大彈性

**獨特設計:**
- **High Headroom Design:** 比典型 horse-themed OD 更多 headroom
- **Frequency Boost:** 低頻與高頻都有提升
- **2-band EQ:** Bass + Treble 獨立控制

**音色特性:**
- **Design Goal:** 透明，不染色，amp-like
- **Frequency:** 溫暖飽滿低頻，豐富厚實中頻，不刺耳高頻
- **Harmonics:** Germanium 偶次諧波豐富

**最適合:**
- Transparent boost, Blues, Rock, Jazz, 疊加用

**疊加特性:**
- 極佳 always-on pedal，可推動其他 OD
- 與其他 pedals 疊加優異

**使用建議:**
- 如果 rig 已經偏暗需注意 Treble 設定
- VOICE 控制需要實驗找到甜蜜點

**訊號鏈配置:**
- Position: pre_amp_gain
- Swiss Things Assignment: loop_1
- Notes: V3.0 新增，取代 Colosseum Klon Side，訊號鏈1透明 Boost

---

### 3. Morning Glory V3 (透明派 - BB 路線)

**核心 DNA:** Marshall Bluesbreaker 改良，極度透明

**技術規格:**
- **Gain 範圍:** Low-Medium (edge of breakup)
- **頻率特性:** 中性不染色，不像 TS 突出中頻
- **動態:** 極高觸鍵敏感度，極低壓縮
- **電源:** 9V DC
- **Bypass:** True Bypass

**V3 升級:**
- 4倍 headroom (相比 V2)
- 2倍 gain range
- 新增 Bright Cut Toggle

**獨特控制:**
- **Bright Cut Toggle** - 高頻調整開關
  - Left (OFF): 保留完整高頻 (適合 Humbucker)
  - Right (ON): 削減高頻 (適合 Single-coil)

**音色特性:**
- **Type:** Transparent Low-Medium Gain Overdrive
- **Frequency:** 飽滿低頻但不過度，中性中頻，平滑高頻
- **Dynamics:** 極高觸鍵敏感度與音量敏感度，極低壓縮
- **Harmonics:** 清晰、開放，偏偶次諧波

**最適合:**
- Blues, Classic Rock, Jazz, Neo Soul, British tones

**疊加特性:**
- "市場上最透明的 overdrive 之一"
- 極佳的疊加能力，適合放在其他 OD 前面
- 常見組合: Morning Glory → Tube Screamer / OCD / KOT

**評價:**
- "Everything your guitar and amp sound like only a little dirty" - Josh Scott

**訊號鏈配置:**
- Position: pre_amp_gain
- Swiss Things Assignment: loop_1
- Notes: V3.0 新增，取代 Colosseum BB Side，經典 BB 音色

---

### 4. Roshi Blacklon (音箱模擬派)

**核心 DNA:** Fender Blackface AB763 音箱模擬

**技術規格:**
- **Gain 範圍:** Variable (取決於模式)
- **頻率特性:** 極度透明，反映音箱特性，Blackface 適度削減低/高頻
- **動態:** 極高觸鍵與音量敏感度
- **電源:** DC9V (最大 10V，不可超過)
- **Design Philosophy:** "如同腳下有台音箱"

**4種模式組合:**

#### 6L6 vs 6V6 Mode:
- **6L6 (左):**
  - 更大 headroom
  - 低頻延伸更好
  - 適合 Heavy riff
  - 廣闊頻率範圍
  - 適合搭配 Fuzz pedals

- **6V6 (右):**
  - Neo Soul 風格 mellow tone
  - 類似 Fuzz Face + Crunch amp
  - 較溫暖柔和

#### Mellow vs Drive Mode:
- **Mellow (左):**
  - 豐富低頻
  - 較少失真
  - Tone 控制較溫和

- **Drive (右):**
  - 削減低頻 (避免泥濘)
  - 更多失真
  - Tone 控制更激進
  - 更寬廣音色調整範圍

**音色特性:**
- 豐富低頻與高頻分離感並存
- 適度 Compression 的 Clean tone
- 失真質感如音箱般 破裂 (edgy attack)
- 極度透明，能反映音箱特性

**最適合:**
- 讓 JC-22 等電晶體音箱有真空管感
- Post Rock, Neo Soul, Blues
- 可作為 amp 替代使用

**使用注意:**
- 僅能使用 DC9V，超過 10V 會損壞
- 6L6/6V6 切換後約 30 秒旋鈕挙動不穩定 (正常現象)

**訊號鏈配置:**
- Position: pre_amp_gain
- Swiss Things Assignment: loop_1
- Notes: 訊號鏈2 Blackface 管機模擬，讓 JC-22 有管機感

---

### 5. TWA Source Code (TS 進化派)

**核心 DNA:** TS808 終極進化版，原創者 Susumu Tamura 設計

**技術規格:**
- **Gain 範圍:** Low-High (比 TS808 更廣)
- **電源:** 9VDC 輸入，內部升壓至 18V
- **18V Operation 優勢:**
  - 更大 headroom
  - 更好的動態範圍
  - 更清晰的音色
- **Bypass:** True Bypass

**獨特控制:**
- **BITE** - 遊戲規則改變者！
  - 調整 odd/even-order harmonics 平衡
  - Min: Symmetrical clipping (對稱削波)
  - Max: Asymmetrical clipping (不對稱削波，high-gain tube amp 感)
  - 從平滑到 high-gain tube amp 感覺

**特殊功能:**
- +6dB boost circuit
- Multi-transistor input buffer
- Magic IC OpAmp

**音色特性:**
- **Frequency:** 比傳統 TS 更飽滿低頻，保留 TS 特色中頻但更平衡，更開放高頻
- **Dynamics:** 高觸鍵敏感度與音量敏感度，適中壓縮
- **Harmonics:** 可透過 BITE 從偶次到奇次調整

**vs TS808 比較:**
- Headroom 顯著增加
- Gain range 更廣
- Bite 提供前所未有的諧波控制
- 更透明，較少中頻堆疊
- 全新 multi-transistor buffer design

**最適合:**
- Rock, Blues, Fusion, Classic Rock, TS-style mid boost, High headroom overdrive

**疊加特性:**
- 與其他 pedal 疊加優異
- Always-on multi-transistor buffer

**使用建議:**
- Bite 建議從 12 點鐘開始調整

**訊號鏈配置:**
- Position: pre_amp_gain
- Swiss Things Assignment: loop_1
- Notes: 訊號鏈2 TS Evolution，Classic Rock 時需要 TS 中頻開啟

---

### 6. Free the Tone ODL-1-CS (高階派)

**核心 DNA:** Dumble Overdrive Special，設計師有 20+ 年 Dumble 維修經驗

**技術規格:**
- **Gain 範圍:** Variable (Dual channel)
- **電源:** DC9V 輸入，內部升壓至 10-19V 可調 (CS 版本)
- **電流:** 95mA (需 200mA 以上供電能力)
- **不支援電池** (高電流消耗)
- **Bypass:** Buffered Bypass (HTS circuit, always-on)

**雙通道:**

#### Normal Channel:
- 無 clipping diodes/LEDs
- 豐富諧波，即使在 clean 設定下
- Controls: NOR LEVEL, TONE, GAIN
- Switches: EQ ON/GLASS, ROCK/JAZZ

#### Drive Channel:
- Dedicated drive circuit module
- 在 Normal Channel 之前
- CS 版本 module 更敏感
- Controls: DRV LEVEL, DRIVE, PUSH, HI CUT

**獨特開關:**

#### EQ ON / GLASS:
- **EQ ON:** 啟動 Tone circuit
- **GLASS:** Bypass Tone circuit (類似 Blackface Fender Vibroverb 的 Bright switch，玻璃般清晰音色)

#### ROCK / JAZZ:
- **ROCK:** 增加 gain，略削減低頻 (避免 amp 過載)，適合 Rock 音色塑造
- **JAZZ:** 降低整體 gain，強調低頻豐富度，適合 Jazz 音色

**CS vs Standard 差異:**
- **Custom Module:** CS 使用不同零件，更敏感反應
- **Voltage Adjustment:** Standard 固定 14.5V，CS 可 10-19V 連續調整
- **Tone:** CS 版本更細膩、更敏感

**HTS Circuit:**
- Full Name: Holistic Tonal Solution
- 不同於傳統 buffer
- 最大化吉他音色特性
- 平衡音色與低噪音
- 輸出與輸入同相位

**音色特性:**
- Dumble 特有的諧波豐富度
- Clean 也帶有輕微失真質感
- Amp-like 反應，如同音箱有意識般回應
- 跨弦平衡 (1-6/7弦)

**最適合:**
- Blues, Jazz, Fusion, Rock
- Larry Carlton / Robben Ford / Eric Johnson / SRV / John Mayer style

**使用建議:**
- CS 版本可調 10-19V 找到個人喜好
- 使用電池時設定 DC9V mode (Int.PS 耗電快)

**訊號鏈配置:**
- Position: pre_amp_gain
- Swiss Things Assignment: loop_1
- Notes: 訊號鏈2 Dumble 高階音色，Fusion 經典

---

## 三、2-3顆疊加組合分析

### 【方案 A】Neo Soul / Jazz 溫暖派 (2顆)

```
Horsemeat (always-on clean boost) → Sweet Honey (溫暖主音色)
```

**音色特性:** 極溫暖、甜美、豐富諧波

**角色分配:**
- **Horsemeat:** Germanium 底層溫暖 + transparent boost
- **Sweet Honey:** 主要音色塑造，FOCUS 控制動態

**適合風格:** Neo Soul, Jazz, Funk

**吉他搭配:** Throbber-CTM (semi-hollow + APH-1), Greco TE-500

**設定建議:**
- Horsemeat: VOICE 在 mellow side，提供底層溫暖
- Sweet Honey: FOCUS 逆時針，柔和動態響應

---

### 【方案 B】Classic Rock / Blues 經典派 (2-3顆)

```
選項1: Morning Glory → Source Code
選項2: Horsemeat → Morning Glory → Source Code (3顆)
```

**音色特性:** 經典 British + TS 中頻推力

**角色分配:**
- **Morning Glory:** 透明 BB 音色，edge of breakup
- **Source Code:** TS 中頻 boost，BITE 可調諧波特性
- **Horsemeat (可選):** 前置 clean boost，增加 clarity

**適合風格:** Classic Rock, Blues, British Rock

**吉他搭配:** ESP Eclipse CTM (EMG active)

**設定建議:**
- Morning Glory: Drive 低設定，作為底層 crunch
- Source Code: BITE 在 12 點鐘，提供 TS 中頻特性

---

### 【方案 C】Post Rock / Ambient 大動態派 (2顆)

```
Blacklon (6V6 + Mellow) → Sweet Honey or Morning Glory
```

**音色特性:** 真空管感 + 溫暖/透明疊加

**角色分配:**
- **Blacklon:** Amp simulation 底層，讓 JC-22 有管機感
- **疊加選擇:**
  - Sweet Honey: 更溫暖、更多 sustain (Post Rock)
  - Morning Glory: 更透明、更開放 (Ambient clean)

**適合風格:** Post Rock, Ambient, Neo Soul

**吉他搭配:** Throbber-CTM, Fender Thinline

**設定建議:**
- Blacklon: 6V6 + Mellow mode，提供溫暖管機底色
- 疊加 OD: 低 gain 設定，保留動態

---

### 【方案 D】Fusion / High-end 頂級派 (2-3顆)

```
選項1: ODL-1-CS (dual channel 獨立使用)
選項2: Horsemeat → ODL-1-CS (Normal channel)
選項3: Morning Glory → ODL-1-CS (Drive channel)
```

**音色特性:** Dumble 高階音色

**ODL-1-CS 特性:**
- Dual channel 可獨立使用 (不需疊加)
- Normal: 豐富諧波，即使 clean 也帶質感
- Drive: 專用 drive module

**疊加建議:** ODL-1-CS 已經很完整，但可用透明 OD 前置推動

**適合風格:** Fusion, Jazz, Blues (Larry Carlton / Robben Ford)

**吉他搭配:** Throbber-CTM, Greco TE-500

**設定建議:**
- ODL-1-CS: JAZZ mode (降 gain, 強調低頻)
- 如疊加: 透明 OD 作為 clean boost

---

### 【方案 E】Modern Rock 全能派 (3顆)

```
Horsemeat (boost) → Morning Glory (foundational) → Source Code (lead)
```

**音色特性:** 三層疊加，clean → crunch → lead

**訊號流:**
1. **Horsemeat:** Always-on clean boost, VOICE 在 glassy
2. **Morning Glory:** Rhythm crunch, Bright Cut 依吉他調整
3. **Source Code:** Solo lead, BITE 增加諧波複雜度

**適合風格:** Modern Rock, Blues Rock, 需要多層次音色變化

**吉他搭配:** 全吉他通用

**切換邏輯:**
- Clean: 只開 Horsemeat
- Rhythm: Horsemeat + Morning Glory
- Lead: 全開 (Horsemeat + Morning Glory + Source Code)

---

## 四、使用場景推薦總表

| 音樂風格 | 主推組合 | 替代方案 | 核心特色 |
|---|---|---|---|
| **Neo Soul** | Horsemeat → Sweet Honey | Blacklon (6V6+Mellow) → Sweet Honey | 極溫暖甜美 |
| **Jazz** | Sweet Honey 單顆 | ODL-1-CS (JAZZ mode) | 動態控制優異 |
| **Fusion** | ODL-1-CS 單顆 | Morning Glory → ODL-1-CS | Dumble 頂級音色 |
| **Blues** | Morning Glory → Sweet Honey | Horsemeat → ODL-1-CS | 經典溫暖 |
| **Classic Rock** | Morning Glory → Source Code | Horsemeat → Morning Glory → Source Code | British + TS |
| **Post Rock** | Blacklon → Sweet Honey | Morning Glory → Sweet Honey | 管機感 + sustain |
| **Ambient** | Blacklon (6V6+Mellow) → Morning Glory | Morning Glory 單顆 | 透明大動態 |
| **Modern Rock** | Horsemeat → Morning Glory → Source Code | Morning Glory → Source Code | 三層疊加 |

---

## 五、關鍵洞察與建議

### Always-On 候選

1. **Horsemeat** - Klon-style transparent boost (首選)
   - 理由: 極透明，Germanium 溫暖，VOICE 控制靈活
   - 適合: 任何需要底層溫暖 boost 的場合

2. **Morning Glory** - 極透明 BB (次選)
   - 理由: "市場上最透明的 overdrive 之一"
   - 適合: 需要完全不染色的 always-on

3. **Sweet Honey** - 溫暖 always-on (Jazz/Neo Soul 專用)
   - 理由: 極高觸鍵敏感度，FOCUS 控制動態
   - 適合: Jazz, Neo Soul 溫暖底色

### Solo/Lead 推薦

- **Source Code** - BITE 控制提供 solo 時的諧波複雜度
  - 優勢: 18V headroom，可調 odd/even harmonics
  - 適合: 需要穿透力的 solo

- **ODL-1-CS Drive channel** - Dumble 高階 lead tone
  - 優勢: Dumble 質感，CS 版本可調內部電壓
  - 適合: Fusion, Blues 高階 solo

### 特殊應用

- **Blacklon** - 讓 Roland JC-22 有真空管感
  - 用途: Amp simulator，特別適合電晶體音箱
  - 模式: 6V6 + Mellow (Neo Soul), 6L6 + Drive (Rock)

- **ODL-1-CS** - CS 版本 10-19V 可調
  - 用途: 針對不同吉他優化內部電壓
  - 開關: ROCK/JAZZ 切換不同風格

### 疊加順序原則

```
Transparent Boost → Foundational OD → High Gain OD
(Horsemeat/Morning Glory) → (Sweet Honey/Morning Glory) → (Source Code/ODL-1-CS Drive)
```

**原則說明:**
1. **第一級 (Boost):** 最透明的 OD，提供底層音色增強
2. **第二級 (Foundation):** 主要音色塑造，定義核心 tone
3. **第三級 (Lead):** 高 gain 或特殊諧波，solo 時開啟

---

## 六、與吉他配對建議

### ESP Eclipse CTM (EMG JH-B active, high output)

**推薦組合:**
- **Clean/Jazz:** Horsemeat (clean boost) → Sweet Honey (warm OD)
- **Rock:** Morning Glory → Source Code
- **Modern Rock:** Horsemeat → Morning Glory → Source Code

**注意事項:**
- EMG active pickup 輸出高，注意 input pad 設定
- Morning Glory Bright Cut 建議 OFF (保留高頻)

---

### ESP Throbber-CTM (SD APH-1, medium output, semi-hollow)

**推薦組合:**
- **Neo Soul:** Horsemeat → Sweet Honey
- **Jazz:** Sweet Honey 單顆 或 ODL-1-CS (JAZZ mode)
- **Blues:** Morning Glory → Sweet Honey

**注意事項:**
- Semi-hollow 本身有溫暖特性，搭配溫暖 OD 效果極佳
- APH-1 是 PAF-style，適合 Sweet Honey 的溫暖路線

---

### Greco TE-500 (Lindy Fralin WideRange, medium output)

**推薦組合:**
- **Jazz/Funk:** Sweet Honey 單顆
- **Neo Soul:** Horsemeat → Sweet Honey
- **Fusion:** ODL-1-CS 單顆

**注意事項:**
- Lindy Fralin WideRange 已經很溫暖，適合溫暖 OD
- 避免過度疊加 warm OD，可能過於 muddy

---

### Fender Tokyo Thinline (Momose VT-1 single-coil, medium output)

**推薦組合:**
- **Clean/Country:** Horsemeat 單顆 (clean boost)
- **Blues:** Morning Glory → Sweet Honey
- **Funk:** Sweet Honey 單顆

**注意事項:**
- Single-coil 建議使用 Morning Glory Bright Cut ON (削減高頻)
- 避免過度 gain，保留 Tele 清晰特性

---

## 七、總結與建議

### 核心優勢

你擁有的 6 顆 overdrive 涵蓋了：
1. **透明派:** Horsemeat (Klon), Morning Glory (BB)
2. **溫暖派:** Sweet Honey (Honey Bee evolution)
3. **TS 派:** Source Code (TS evolution with BITE)
4. **高階派:** ODL-1-CS (Dumble)
5. **特殊派:** Blacklon (Amp simulator)

這個組合幾乎可以應對所有音樂風格需求。

### 建議的訊號鏈配置

#### 訊號鏈 1 (Jazz/Neo Soul/Funk) - Roland JC-22

```
Guitar → [Always-on: Empress MKII, Cali76, PA-1QG]
     → Swiss Things Loop 1 [Horsemeat, Sweet Honey, Morning Glory]
     → Swiss Things Loop 2 [FT-1Y, Nucleo]
     → Roland JC-22
```

**使用邏輯:**
- Horsemeat: Always-on clean boost
- Sweet Honey: Neo Soul 主音色
- Morning Glory: Blues crunch

---

#### 訊號鏈 2 (Post Rock/Fusion/Rock) - Tone King Imperial MKII

```
Guitar → [Always-on: 同上]
     → Swiss Things Loop 1 [Blacklon, Source Code, ODL-1-CS]
     → Swiss Things Loop 2 [FT-1Y, Nucleo, AASB]
     → Tone King Imperial MKII (4CM)
```

**使用邏輯:**
- Blacklon: 讓 rig 有管機底色
- Source Code: Classic Rock TS 中頻
- ODL-1-CS: Fusion 高階 lead

---

### 下一步建議

1. **實際測試疊加組合** - 依照上述方案實際測試，找到個人喜好
2. **針對每把吉他建立 preset** - PA-1QG 有 99 presets，可為每把吉他建立專用 EQ
3. **記錄最佳設定** - 建立每個組合的 knob 設定記錄
4. **考慮 Buffer++ (如果需要 stereo)** - 充分發揮 Nucleo stereo reverb

---

**報告建立日期:** 2026-01-02
**資料來源:** shared/equipment_database/pedals/*.yaml, shared/inventory/pedals.yaml
**分析者:** Claude Code (Sonnet 4.5)
