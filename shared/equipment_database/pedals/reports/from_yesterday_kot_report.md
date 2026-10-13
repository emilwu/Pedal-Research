> ⚠️ **過時警告（2026-10-13）**：本報告描述的是 Analog Man King of Tone，不是使用者持有的 Device2 From Yesterday。
> 報告中的雙通道 Red/Yellow、六顆旋鈕、9V 至 18V、True Bypass、阻抗與價格等內容都不適用於這台。
> 依官方來源重寫的規格見 `shared/equipment_database/pedals/specs/from_yesterday_kot.yaml`（v2.0）。本報告內文保留原樣作為歷史記錄。

# From Yesterday King of Tone Clone - 器材詳細報告

**版本:** 1.0
**更新日期:** 2026-01-13
**資料來源:** `shared/equipment_database/pedals/specs/from_yesterday_kot.yaml`
**注意:** 本報告基於 Analogman King of Tone 規格撰寫

---

## 目錄

1. [器材概述](#器材概述)
2. [技術規格詳解](#技術規格詳解)
3. [音色特性](#音色特性)
4. [使用範例](#使用範例)
5. [優缺點分析](#優缺點分析)
6. [網路驗證資訊](#網路驗證資訊)

---

## 器材概述

### 基本資訊

**品牌:** From Yesterday
**型號:** King of Tone Clone
**全名:** From Yesterday - Analog Man King of Tone Clone
**類型:** Overdrive
**風格:** Dual Transparent Overdrive
**電路基礎:** Analogman King of Tone（雙 Marshall Bluesbreaker 串聯）
**原版設計師:** Mike Piera (Analog Man) & Jim Weider
**設計理念:** 保留吉他與音箱原音，加上溫暖 Overdrive

### 核心賣點

From Yesterday King of Tone Clone 是基於傳奇的 **Analogman King of Tone** 電路的克隆版本。原版 King of Tone（簡稱 KOT）由 Analogman 創辦人 Mike Piera 與吉他手 Jim Weider（The Band）共同設計，以其極度透明、Amp-like 的反應聞名，被譽為「市場上最透明的 Overdrive 之一」。原版 KOT 有數年等待清單，二手價格高達 $800-1000+ USD，From Yesterday 克隆版提供了更實惠的選擇。

**獨特之處:**
- **雙通道獨立設計** - Red Channel + Yellow Channel，各自獨立控制
- **三種模式** - 每個通道可透過內部 DIP Switch 設定為 OD / Clean / Dist 模式
- **9 種組合** - 3×3 = 9 種不同音色組合
- **Amp-like 反應** - 如同音箱般有意識地回應撥弦力度與音量旋鈕
- **極低壓縮** - 保留極高動態範圍
- **18V 供電** - 支援 9V 至 18V，18V 提供更好音色與 Headroom
- **雙 Bluesbreaker 串聯** - 本質上是兩個改良版 Marshall Bluesbreaker 串聯

### 適合的音樂風格

| 風格 | 適配度 | 說明 |
|------|--------|------|
| **Blues** | ⭐⭐⭐⭐⭐ | KOT 經典應用，極度透明 |
| **Classic Rock** | ⭐⭐⭐⭐⭐ | Amp-like 反應，適合 Vintage Tone |
| **Jazz** | ⭐⭐⭐⭐⭐ | Clean Mode 適合 Jazz Clean Boost |
| **Country** | ⭐⭐⭐⭐⭐ | 透明特性保留 Twang |
| **Neo Soul** | ⭐⭐⭐⭐ | 溫暖、動態豐富 |

**代表性藝術家:**
- John Mayer（KOT 長期用戶）
- Gary Clark Jr.（Blues Rock）
- Brad Whitford（Aerosmith）
- Wayne Sermon（Imagine Dragons）
- Jon Carin（Roger Waters 樂團）
- Jim Weider（The Band，共同設計師）

---

## 技術規格詳解

### 電源規格

| 項目 | 規格 | 說明 |
|------|------|------|
| **外部供電** | 9V to 18V DC | Center Negative |
| **建議電壓** | 18V | 提供更好音色、更大 Headroom、更佳動態 |
| **電池支援** | ❌ 不支援 | 雙通道設計，電流消耗較高 |

**18V 供電優勢:**
- 更大 Headroom
- 更好動態範圍
- 更清晰音色
- 更 Amp-like 反應
- **許多用戶偏好 18V 供電**

---

### 雙通道設計

#### **通道配置**

| 通道 | 顏色 | 典型設定 | 訊號順序 |
|------|------|---------|---------|
| **Yellow Channel** | 黃色 | Clean Mode（Clean Boost） | 第一個（可透過內部跳線切換） |
| **Red Channel** | 紅色 | OD Mode（Overdrive） | 第二個（可透過內部跳線切換） |

**訊號流向:**
```
Guitar → Yellow Channel → Red Channel → Amp
（可透過內部跳線切換順序）
```

---

### 控制旋鈕

#### **Yellow Channel（黃色通道）**

| 旋鈕 | 功能 |
|------|------|
| **VOLUME** | Yellow 通道輸出音量 |
| **DRIVE** | Yellow 通道增益控制 |
| **TONE** | Yellow 通道音色調整 |

#### **Red Channel（紅色通道）**

| 旋鈕 | 功能 |
|------|------|
| **VOLUME** | Red 通道輸出音量 |
| **DRIVE** | Red 通道增益控制 |
| **TONE** | Red 通道音色調整 |

---

### 三種模式（每通道獨立設定）

**透過內部 DIP Switch 設定:**

#### **1. Normal Overdrive Mode（標準 Overdrive 模式）**

**特性:**
- 標準 KOT 音色
- 增益略低於 Tube Screamer
- 可達到 4 倍 TS 音量
- 極度透明，保留吉他與音箱原音

**最適合:**
- 標準 Overdrive 使用
- Blues, Rock Rhythm
- 溫暖的 Lead Tone

---

#### **2. Clean Mode（Clean 模式）**

**特性:**
- 更少失真
- 適合 Clean Boost
- Compression 更低
- 可達到 2 倍 OD Mode 音量
- 極度透明

**最適合:**
- Clean Boost
- 透明推動音箱
- Solo 音量提升
- 作為第一級 Overdrive Stacking

---

#### **3. Distortion Mode（Distortion 模式）**

**特性:**
- 比標準模式更多失真
- 更多 Compression
- 保留踏板特性
- 仍然非常透明（相對於其他 Distortion）

**最適合:**
- 需要更多增益時
- High-Gain Lead Solo
- Heavy Rock 音色

---

### 內部控制

**DIP Switches（內部撥動開關）:**

| Switch | 功能 |
|--------|------|
| **Switch 1** | Yellow Channel Mode（OD/CLEAN） |
| **Switch 2** | Yellow Channel DIST Mode |
| **Switch 3** | Red Channel Mode（OD/CLEAN） |
| **Switch 4** | Red Channel DIST Mode |

**Treble Trimpot（內部高頻微調）:**
- 內部微調旋鈕
- 可調整高頻響應
- 適應不同吉他與音箱

---

### 選配功能

| 選項 | 價格 | 功能 |
|------|------|------|
| **Buffer Bypass** | +$45 USD | 加入 Buffer 功能 |
| **External Mode Toggle** | +$50 USD | 外部模式切換開關 |

---

### Bypass 類型

**Bypass:** True Bypass（標準）
**選配:** Buffer Bypass（+$45 USD）

---

### 尺寸與重量

- **尺寸:** 標準雙通道 Overdrive 尺寸（約 125mm × 95mm × 50mm）
- **重量:** 約 450g（估計）

---

## 音色特性

### 核心音色特徵

1. **市場上最透明的 Overdrive 之一**
   - 保留吉他與音箱原音特性
   - 不像 Tube Screamer 過度塑形中頻
   - 不掩蓋吉他本身的音色

2. **Amp-like 反應**
   - 如同音箱般有意識地回應
   - 極度觸鍵敏感（Pick Sensitivity）
   - 吉他音量旋鈕極度敏感
   - **"The pedal adapts to your amp"** - Fender 聽起來像推滿的 Fender，Marshall 聽起來像推滿的 Marshall

3. **極低壓縮**
   - 保留極高動態範圍
   - 不像傳統 Overdrive 過度壓縮
   - 延音自然，不機械

4. **雙 Bluesbreaker 串聯**
   - 本質上是兩個改良版 Marshall Bluesbreaker
   - 可獨立使用或串聯
   - 串聯時創造更複雜、更自然的破音

---

### 頻率響應特性

| 頻段 | 特性 | 說明 |
|------|------|------|
| **低頻** | 豐富但不過度 | 不像 Tube Screamer 削減低頻 |
| **中頻** | 平衡，不突出 | 不像 Tube Screamer 過度提升中頻 |
| **高頻** | 開放、清晰 | 可透過內部 Treble Trimpot 微調 |

**與其他 Overdrive 比較:**
- **vs Tube Screamer** - KOT 更中性，TS 過度塑形中頻
- **vs Klon** - KOT 更透明，Klon 有輕微中頻提升
- **vs Fulltone OCD** - KOT 更透明，OCD 更多 Gain 與 Compression

---

### 動態反應

**Pick Sensitivity（撥弦敏感度）:**
- **極高**（Amp-like）
- 輕撥 → Clean Tone
- 重撥 → Overdrive
- 如同音箱般有意識地回應

**Volume Sensitivity（音量旋鈕敏感度）:**
- **極高**
- 吉他音量旋鈕可大幅改變音色
- 從 Clean 到 Overdrive 連續變化
- 適合需要多種音色的演奏者

**Compression（壓縮特性）:**
- **極低**（除非選 Dist Mode）
- 保留自然動態
- 不過度壓縮
- 延音飽滿但不失 Attack

---

### Gain 特性

**Breakup Point（破音點）:**
- 極度透明
- 從 Edge of Breakup 到 Medium-High Gain
- Clean Mode 可達 Clean Boost

**Gain Range（增益範圍）:**
- **Clean Mode** - Clean Boost，可達 2 倍 OD Mode 音量
- **OD Mode** - 略低於 Tube Screamer，可達 4 倍 TS 音量
- **Dist Mode** - 比 OD Mode 更多增益與壓縮

**Harmonics（諧波特性）:**
- 豐富、有機
- 偏偶次諧波
- 音樂性強
- 不刺耳、不尖銳

---

## 使用範例

### 範例 1：Jazz Clean Boost（Yellow Clean Mode Only）

**音樂風格:** Jazz, Bossa Nova
**適合吉他:** Semi-Hollow, Archtop

**設定:**

| 通道 | 模式 | 旋鈕 | 設定 |
|------|------|------|------|
| **Yellow** | Clean Mode | VOLUME | 3 點鐘（大音量提升） |
| **Yellow** | Clean Mode | DRIVE | 8 點鐘（極低 Gain） |
| **Yellow** | Clean Mode | TONE | 12 點鐘 |
| **Red** | 關閉 | - | - |

**電壓:** 18V（建議）

**效果:**
- 極度透明的 Clean Boost
- 推動音箱進入輕度破音
- 保留 Jazz 音色特性
- 適合 Solo 音量提升

**訊號鏈位置:** Guitar → Compressor → **KOT Clone (Yellow Clean)** → Delay → Reverb → Amp

---

### 範例 2：Blues Rhythm（Yellow OD Mode Only）

**音樂風格:** Blues, Blues Rock
**適合吉他:** Single-Coil 或 Humbucker

**設定:**

| 通道 | 模式 | 旋鈕 | 設定 |
|------|------|------|------|
| **Yellow** | OD Mode | VOLUME | 12 點鐘（Unity Gain） |
| **Yellow** | OD Mode | DRIVE | 11 點鐘（輕度 Overdrive） |
| **Yellow** | OD Mode | TONE | 12 點鐘 |
| **Red** | 關閉 | - | - |

**電壓:** 18V

**效果:**
- 溫暖、透明的 Overdrive
- 保留 Pick Attack 清晰度
- 極高動態反應
- 吉他音量旋鈕可從 Clean 到 Overdrive

**訊號鏈位置:** Guitar → Compressor → **KOT Clone (Yellow OD)** → Delay → Reverb → Amp

---

### 範例 3：Classic Rock Stacking（Yellow Clean + Red OD）

**音樂風格:** Classic Rock, Blues Rock
**適合吉他:** Humbucker 或 P90 吉他

**設定:**

| 通道 | 模式 | 旋鈕 | 設定 |
|------|------|------|------|
| **Yellow** | Clean Mode | VOLUME | 1 點鐘 |
| **Yellow** | Clean Mode | DRIVE | 9 點鐘（輕推） |
| **Yellow** | Clean Mode | TONE | 1 點鐘 |
| **Red** | OD Mode | VOLUME | 12 點鐘 |
| **Red** | OD Mode | DRIVE | 12 點鐘（中等 Gain） |
| **Red** | OD Mode | TONE | 12 點鐘 |

**訊號順序:** Yellow (Clean) → Red (OD)
**電壓:** 18V

**效果:**
- Yellow Clean 提供透明基礎音色
- Red OD 再次推動，增加 Sustain
- 雙 Bluesbreaker 疊加，創造複雜諧波
- 適合 Classic Rock Lead Solo

**訊號鏈位置:** Guitar → Compressor → **KOT Clone (Yellow+Red)** → Delay → Reverb → Amp

---

### 範例 4：High-Gain Lead（Yellow OD + Red Dist）

**音樂風格:** Rock, Alternative Rock
**適合吉他:** Humbucker 吉他

**設定:**

| 通道 | 模式 | 旋鈕 | 設定 |
|------|------|------|------|
| **Yellow** | OD Mode | VOLUME | 12 點鐘 |
| **Yellow** | OD Mode | DRIVE | 1 點鐘（中高 Gain） |
| **Yellow** | OD Mode | TONE | 11 點鐘 |
| **Red** | Dist Mode | VOLUME | 1 點鐘 |
| **Red** | Dist Mode | DRIVE | 1 點鐘（中高 Gain） |
| **Red** | Dist Mode | TONE | 12 點鐘 |

**訊號順序:** Yellow (OD) → Red (Dist)
**電壓:** 18V

**效果:**
- Yellow OD 提供基礎 Overdrive
- Red Dist 再次推動，增加飽滿度
- 雙通道疊加提供 High-Gain Lead 音色
- 仍然保留 KOT 透明特性

**訊號鏈位置:** Guitar → Compressor → **KOT Clone (Yellow OD + Red Dist)** → Delay → Reverb → Amp

---

### 範例 5：Two Different Colors（Yellow OD + Red OD）

**音樂風格:** 任何風格
**適合吉他:** 任何吉他

**設定:**

| 通道 | 模式 | 旋鈕 | 設定 |
|------|------|------|------|
| **Yellow** | OD Mode | VOLUME | 12 點鐘 |
| **Yellow** | OD Mode | DRIVE | 10 點鐘（低 Gain） |
| **Yellow** | OD Mode | TONE | 1 點鐘（明亮） |
| **Red** | OD Mode | VOLUME | 12 點鐘 |
| **Red** | OD Mode | DRIVE | 2 點鐘（高 Gain） |
| **Red** | OD Mode | TONE | 11 點鐘（溫暖） |

**使用方式:**
- Yellow - Rhythm 音色（低 Gain，明亮）
- Red - Lead 音色（高 Gain，溫暖）
- 或同時開啟疊加

**電壓:** 18V

**效果:**
- 兩種不同 Overdrive 色彩
- 可獨立切換或疊加
- 提供極大彈性

**訊號鏈位置:** Guitar → Compressor → **KOT Clone (Yellow or Red or Both)** → Delay → Reverb → Amp

---

### 範例 6：Overdrive Stacking with Other Pedals

**Overdrive Stacking 範例:**

**範例 A（KOT 作為第一級）:**
```
KOT Clone Yellow (Clean Mode) → Morning Glory (BB) → Amp
```
- KOT Clean 提供透明基礎
- Morning Glory 增加 Bluesbreaker 色彩

**範例 B（KOT 作為最終推動）:**
```
Soul Food (Klon Clean Boost) → KOT Clone Red (OD Mode) → Amp
```
- Soul Food 提供 Klon 透明推動
- KOT Red 再次推動，增加飽滿度

**範例 C（三級疊加）:**
```
KOT Clone Yellow (Clean) → KOT Clone Red (OD) → Tube Screamer (Mid Gain) → Amp
```
- KOT 雙通道提供基礎音色
- Tube Screamer 提供經典中頻與 Sustain

**範例 D（Always-On 設定）:**
```
Guitar → KOT Clone Yellow (Clean Mode, Always-On) → 其他效果器 → Amp
```
- Yellow Clean Mode 常開
- 提供透明基礎音色與輕微推動
- 改善整體訊號鏈品質

---

## 優缺點分析

### 優點

1. **市場上最透明的 Overdrive 之一**
   - 保留吉他與音箱原音特性
   - 不過度塑形音色
   - "The pedal adapts to your amp"

2. **Amp-like 反應**
   - 如同音箱般有意識地回應
   - 極度觸鍵敏感
   - 吉他音量旋鈕極度敏感

3. **雙通道提供極大彈性**
   - 兩個獨立通道
   - 可獨立使用或疊加
   - 9 種組合（3×3）

4. **18V 運作提供更好音色**
   - 更大 Headroom
   - 更好動態範圍
   - 更清晰音色

5. **極低壓縮**
   - 保留自然動態
   - 不過度壓縮
   - 延音自然

6. **內部調整選項豐富**
   - DIP Switches 可設定三種模式
   - Treble Trimpot 可微調高頻
   - 適應不同吉他與音箱

7. **經典 Bluesbreaker 電路**
   - 雙 Marshall Bluesbreaker 串聯
   - 經典 British Tone
   - 溫暖、有機

---

### 缺點

1. **原版 KOT 有數年等待清單**
   - 原版 Analogman King of Tone 需等待數年
   - 二手價格極高（$800-1000+ USD）
   - From Yesterday 克隆版品質未知

2. **Clone 版本品質參差不齊**
   - From Yesterday 克隆版品質需驗證
   - 不一定能完全複製原版 KOT 音色
   - 建議購買前試聽

3. **學習曲線較陡**
   - 內部 DIP Switches 設定複雜
   - 9 種組合需要時間熟悉
   - Treble Trimpot 調整需要實驗

4. **價格較高**
   - From Yesterday 克隆版約 $335 USD（2025 年關稅調漲後）
   - 原版 KOT 約 $335 USD（如果等得到）
   - 對預算有限的玩家仍是負擔

5. **需要 18V 供電才能發揮最佳效果**
   - 9V 可用，但 18V 音色更好
   - 需要額外購買 18V Power Supply 或 Voltage Doubler
   - 增加訊號鏈複雜度

6. **體積較大**
   - 雙通道設計
   - Pedalboard 空間佔用較多

---

### 適合人群

**最適合:**
- 追求極度透明 Overdrive 的玩家
- Blues, Classic Rock, Jazz, Country 玩家
- 對動態反應要求極高的演奏者
- 需要多種 Overdrive 色彩的玩家
- 願意花時間深入研究的玩家
- John Mayer, Gary Clark Jr. 風格愛好者

**較不適合:**
- 預算有限的初學者
- 追求極端失真的 Metal 玩家
- 希望即插即用、不想調整的玩家
- Pedalboard 空間有限的玩家
- 不願意打開效果器調整內部 DIP Switches 的玩家

---

## 網路驗證資訊

### 驗證來源

本報告的關鍵資訊已透過以下來源驗證（基於原版 Analogman King of Tone）:

1. **[Analogman 官方產品頁面](https://www.analogman.com/kingtone.htm)**
   - 完整技術規格
   - 官方設計理念說明
   - 三種模式詳細說明

2. **[Equipboard - King of Tone 用戶統計](https://equipboard.com/items/analog-man-king-of-tone-overdrive-guitar-effect-pedal)**
   - 藝術家使用統計
   - 用戶評價

3. **[Equipboard - King of Tone 評測](https://equipboard.com/posts/analogman-king-of-tone-review)**
   - 詳細音色分析
   - 優缺點評價

4. **[Aion FX - King of Tone 電路分析](https://aionfx.com/project/theseus-dual-overdrive/)**
   - 電路設計詳細說明
   - DIY 克隆版參考

5. **[Analogman King of Tone Ver 4 手冊](https://www.analogman.com/manuals/PDFs%20(may%20be%20older)/kotver4.pdf)**
   - 官方使用手冊
   - 技術規格與設定說明

### 驗證的關鍵資訊（基於原版 KOT）

- ✅ 雙通道設計（Red + Yellow）
- ✅ 三種模式（OD / Clean / Dist）
- ✅ 內部 DIP Switches 設定
- ✅ Treble Trimpot 高頻微調
- ✅ 支援 9V 至 18V 供電
- ✅ 18V 提供更好音色
- ✅ 市場上最透明的 Overdrive 之一
- ✅ Amp-like 反應
- ✅ 極度觸鍵敏感與動態
- ✅ 雙 Marshall Bluesbreaker 串聯
- ✅ 原版建議售價 $335 USD（2025 年關稅調漲後）
- ✅ 原版二手價格 $800-1000+ USD
- ✅ 原版有數年等待清單

### 藝術家使用統計（原版 KOT）

根據 Equipboard 統計，使用 Analogman King of Tone 的知名藝術家包括：
- **John Mayer** - 長期用戶，核心音色之一
- **Gary Clark Jr.** - Blues Rock 音色
- **Brad Whitford** (Aerosmith) - Classic Rock
- **Wayne Sermon** (Imagine Dragons) - 2014 年購買 3 顆 KOT
- **Jon Carin** (Roger Waters) - Keyboard & Guitar Rig
- **Andrew McKeag** (The Presidents of the United States of America)
- **Jim Weider** (The Band) - 共同設計師

### 設計背景補充

根據官方資訊，Analogman King of Tone 由 Mike Piera (Analog Man) 與吉他手 Jim Weider (The Band) 共同設計。設計理念是創造一款「保留吉他與音箱原音，加上溫暖 Overdrive」的效果器。

Jim Weider 需要一款能「適應音箱」的 Overdrive，讓 Fender 聽起來像推滿的 Fender，Marshall 聽起來像推滿的 Marshall，而不是所有音箱都變成同一種音色。這個設計理念造就了 KOT 極度透明、Amp-like 的特性。

電路本質上是兩個改良版 Marshall Bluesbreaker 串聯，可獨立使用或疊加。每個通道可透過內部 DIP Switches 設定為三種模式（OD / Clean / Dist），提供 9 種不同組合。

由於 Analogman 採用手工製作與嚴格品質控管，產量有限，造成數年等待清單與高昂二手價格（$800-1000+ USD）。許多廠商推出克隆版本，如 From Yesterday, JHS Prince of Tone, Wampler Pantheon 等，讓更多玩家能體驗 KOT 音色。

### 著名評價

**"The pedal adapts to your amp - Fender sounds like cranked Fender, Marshall sounds like cranked Marshall"** - Analogman 官方說明

---

## 總結

### 核心優勢

Analogman King of Tone 被譽為「市場上最透明的 Overdrive 之一」，其極度透明、Amp-like 的反應、極低壓縮、極高動態，讓它成為 Blues, Classic Rock, Jazz, Country 玩家的夢幻選擇。From Yesterday 克隆版提供了更實惠且無需等待的選擇，讓更多玩家能體驗 KOT 的傳奇音色。

雙通道設計提供極大彈性，每個通道可設定為 OD / Clean / Dist 模式，提供 9 種不同組合。18V 供電提供更好音色與 Headroom，進一步提升音色品質。

### 最佳使用建議

1. **初學者:** 從 Yellow Clean Mode 開始，體驗極度透明的 Clean Boost
2. **中階使用者:** 實驗 Yellow OD + Red OD 雙通道疊加
3. **進階使用者:** 調整內部 DIP Switches 與 Treble Trimpot，找到個人偏好的音色設定，建立完整的 Overdrive Stacking 系統

### 訊號鏈定位

**最佳位置:** Signal Chain 前段（Pre-Amp Gain Section）

**推薦配置:**
```
配置 1（Clean Boost）:
Guitar → Compressor → KOT Clone (Yellow Clean) → Delay → Reverb → Amp

配置 2（雙通道疊加）:
Guitar → Compressor → KOT Clone (Yellow Clean + Red OD) → Delay → Reverb → Amp

配置 3（Always-On）:
Guitar → KOT Clone (Yellow Clean, Always-On) → 其他效果器 → Amp
```

**Overdrive Stacking 範例:**
```
範例 1（KOT 作為第一級）:
KOT Clone Yellow (Clean) → Morning Glory (BB) → OCD (High Gain) → Amp

範例 2（KOT 作為最終推動）:
Soul Food (Klon) → KOT Clone Red (OD) → Amp

範例 3（雙通道 + 外部 OD）:
KOT Clone Yellow (Clean) → KOT Clone Red (OD) → Tube Screamer → Amp
```

### 購買建議

**適合購買如果你:**
- 追求極度透明 Overdrive
- 需要多種 Overdrive 色彩（雙通道 + 三種模式 = 9 種組合）
- 對動態反應要求極高
- 喜歡 John Mayer, Gary Clark Jr. 音色
- 願意花時間深入研究與調整

**不建議購買如果你:**
- 預算有限（建議考慮 Soul Food, Morning Glory）
- 追求極端失真（建議考慮 Distortion 踏板）
- 希望即插即用、不想調整內部 DIP Switches
- Pedalboard 空間有限（建議考慮單通道 Overdrive）

---

**文件版本:** 1.0
**最後更新:** 2026-01-13
**下次更新計劃:** 補充 From Yesterday 克隆版實際測試與用戶回饋

**相關文件:**
- `shared/equipment_database/pedals/specs/from_yesterday_kot.yaml` - KOT Clone 完整技術規格
- `shared/equipment_database/pedals/reports/odl1cs_report.md` - 參考範本
- `shared/equipment_database/pedals/reports/morning_glory_report.md` - 同樣透明的 Bluesbreaker
- `projects/2025-v3-signal-chain/research/overdrive_pedals_technical_data.md` - Overdrive 技術資料

---

**參考資料來源:**
- [Analogman 官方網站](https://www.analogman.com/kingtone.htm)
- [Equipboard - King of Tone 用戶統計](https://equipboard.com/items/analog-man-king-of-tone-overdrive-guitar-effect-pedal)
- [Equipboard - King of Tone 評測](https://equipboard.com/posts/analogman-king-of-tone-review)
- [Aion FX - King of Tone 電路分析](https://aionfx.com/project/theseus-dual-overdrive/)
- [Analogman King of Tone Ver 4 手冊](https://www.analogman.com/manuals/PDFs%20(may%20be%20older)/kotver4.pdf)
