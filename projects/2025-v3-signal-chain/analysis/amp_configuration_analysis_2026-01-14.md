# Amp 配置方案完整分析報告
**日期:** 2026-01-14
**分析目標:** 評估 De Cillia Single 25 / Special 25 對現有三個 Amp 的取代性與 Pedal Chain 簡化可能性

> **現況註記（2026-09-11 查證）：本文「現有三個 Amp」為評估購入方案的假設前提，並非全部現有設備。**
> 依權威來源 `projects/2025-v3-signal-chain/inventory/amps.yaml` 查證，實際 `total_amps: 2`，`active: 2`：
> 目前實際擁有的只有 **Tone King Imperial MKII**（`tone_king_imperial_mkii`）與 **Roland JC-22**（`roland_jc22`），兩者狀態均為 `status: "active"`。
> 本文列為「現有設備」之一的 **DSM/HUMBOLDT Dumblifier**，不存在於 amps.yaml 庫存中，屬本文評估情境中假設持有的音箱，尚未購入。
> 以下分析內容維持原文，供評估參考，不代表目前實際的音箱配置。

---

## 目錄

1. [現有設備完整規格](#現有設備完整規格)
2. [De Cillia Amplification 完整規格](#de-cillia-amplification-完整規格)
3. [配置方案分析](#配置方案分析)
4. [Pedal Chain 簡化分析](#pedal-chain-簡化分析)
5. [取代性評估](#取代性評估)
6. [成本對比](#成本對比)
7. [最終建議](#最終建議)

---

## 現有設備完整規格

### 1. DSM/HUMBOLDT Dumblifier ($549)

**定位:** 完整 Amp-in-a-Box (錄音專用)

| 項目 | 規格 |
|------|------|
| **類型** | Dumble ODS 全類比音箱模擬器 |
| **Preamp** | Dual channel (Clean + Overdrive) |
| **Power Amp Sim** | Zero Watt Power Amp (analog) |
| **Cab Sim** | ✅ Stereo cab sim (可選喇叭類型/尺寸) |
| **內建效果** | Stereo reverb (Room/Ethereal/Plate) |
| **FX Loop** | ✅ Stereo (mono send, stereo return) |
| **輸出** | Dual XLR + Dual TRS + Headphone |
| **MIDI** | ❌ 無 |
| **實體喇叭** | ❌ 無 |
| **音色** | 超厚實 Dumble ODS tone |

**核心優勢:**
- 完整 Dumble ODS 音箱模擬（preamp + power amp + cab sim 一體）
- 可直接 XLR 輸出進 interface，silent recording
- 內建 cab sim，無需外部 IR loader
- 三種 stereo reverb

**適用場景:**
- ✅ Studio recording (with cab sim)
- ✅ Silent practice (headphone)
- ✅ Direct to PA (XLR)
- ❌ 無喇叭，不適合獨立舞台演出

---

### 2. Tone King Imperial MKII ($599)

**定位:** 完整 Amp-in-a-Box with Tubes (錄音/前級/4CM)

| 項目 | 規格 |
|------|------|
| **類型** | 真空管前級 + Amp Simulator |
| **Preamp** | 3x 12AX7 真空管 dual channel (Clean + Lead) |
| **Power Amp Sim** | ✅ Zero Watt Power Amp (真實 Imperial MKII phase inverter) |
| **Cab Sim** | ✅ **15組 OwnHammer IRs** (3 factory + 12 via software) |
| **內建效果** | Stereo convolution spring reverb + Tremolo |
| **FX Loop** | ✅ Stereo (mono send, stereo return) |
| **輸出** | Stereo XLR + 1/4" + Headphone |
| **MIDI** | ✅ **128 presets** programmable |
| **軟體控制** | ✅ **Tone King Editor** (USB-C, 可載入自定義 IR) |
| **4CM** | ✅ 支援與其他音箱整合 |
| **實體喇叭** | ❌ 無 |
| **音色** | British-voiced tube tone |

**核心優勢:**
- 15組專業 OwnHammer IRs cab sim
- MIDI 128 presets 可程式化
- 可載入自定義 IR
- 真空管音色
- 4CM 彈性（可與其他音箱整合）
- Stereo XLR 輸出直接錄音

**適用場景:**
- ✅ Studio recording (with IR cab sim)
- ✅ Silent practice (headphone)
- ✅ 4CM with other amps
- ✅ Direct to PA (XLR)
- ❌ 無喇叭，不適合獨立舞台演出

**⚠️ 關鍵發現:**
Imperial 有完整 cab sim + XLR 輸出，**可以完全取代 DSM 的錄音功能**！

---

### 3. Roland JC-22 ($399)

**定位:** 實體電晶體立體聲音箱 (舞台/練習)

| 項目 | 規格 |
|------|------|
| **類型** | 30W solid-state stereo combo |
| **Power Amp** | 30W solid-state |
| **Speakers** | ✅ **2 x 6.5" stereo speakers** |
| **內建效果** | ✅ **Stereo Chorus** (JC 招牌) + Reverb |
| **FX Loop** | ✅ **Stereo** (mono send, stereo return) |
| **輸出** | Stereo speakers + Stereo line outs + Headphone |
| **Cab Sim** | ❌ 無（有實體喇叭） |
| **XLR 輸出** | ❌ 無 |
| **MIDI** | ❌ 無 |
| **Overdrive** | ❌ 無（需 pedals） |
| **音色** | Ultra-clean, transparent, legendary JC tone |

**核心優勢:**
- **真正立體聲**（2個喇叭獨立驅動）
- **傳奇 JC Chorus** 效果
- **Stereo FX Loop** - Nucleo/FF-1Y 完整發揮
- 極度乾淨透明音色
- 完美 Pedal Platform
- 價格親民 ($399)

**適用場景:**
- ✅ 舞台演出（實體喇叭）
- ✅ 練習
- ✅ Stereo effects 展示
- ✅ Jazz/Funk clean tones
- ❌ 無 cab sim/XLR，不適合 direct recording

**限制:**
- 無 Overdrive（完全依賴 pedals）
- Solid-state（無真空管溫暖感）

---

### 現有配置總結

**三個 Amp 的角色分工:**

| 功能 | DSM | Imperial | JC-22 |
|------|-----|----------|-------|
| **錄音 (with cab sim)** | ✅ | ✅ | ❌ |
| **舞台 (實體喇叭)** | ❌ | ❌ | ✅ |
| **Stereo** | Cab sim stereo | XLR stereo | ✅ 真正 stereo speakers |
| **真空管** | ❌ | ✅ | ❌ |
| **Overdrive** | ✅ | ✅ | ❌ |

**功能互補性:** 完美 - 零重疊
- DSM/Imperial: 錄音工具（虛擬音箱）
- JC-22: 舞台/練習工具（實體音箱）

**總成本:** $1,547 USD

---

## De Cillia Amplification 完整規格

### De Cillia Single 25 ($3,590)

**定位:** Single-Ended Class A 真空管實體音箱

| 項目 | 規格 |
|------|------|
| **功率** | 25W / 10W / 4W (可切換) |
| **Class** | Pure Class A, Single-Ended |
| **Power Tube** | 1x KT150 Tung-Sol (世界首創吉他音箱用) |
| **Preamp Tubes** | 2x 12AX7 (ECC83 NOS + TAD 7025-WB) |
| **Reverb Tube** | 1x 12AT7 ECC81 JJ |
| **Speaker** | 12" Eminence Legend 1258 (可客製) |
| **通道** | **單通道** (Single Channel) |
| **內建效果** | ✅ Tube-driven spring reverb |
| **Boost** | ✅ Footswitchable +8dB |
| **Bright Switch** | ✅ 有 |
| **FX Loop** | ❌ **無** |
| **Cab Sim** | ❌ 無 |
| **XLR 輸出** | ❌ 無 |
| **輸出** | Line Out (160Ω), Speaker Out |
| **重量** | 16.9 kg |
| **保固** | 10 年 |
| **等待期** | **31 個月** |

**音色特性 (官方描述):**
- "American Cleans and edge of the breakup tones"
- "Crystal-clear clean to rich overdrive and singing crunch"
- "Incredibly dynamic, warm sound - iron fist in a velvet glove"
- "Outstanding onboard reverb"

**音色定位:** Fender Blackface-style American clean + edge of breakup

**用戶評價:**
- "Sounds unusually good"
- "The reverb is most impressive"
- "Sounds great!"

---

### De Cillia Special 25 ($3,790)

**定位:** Single-Ended Class A 真空管實體音箱 (Dual Channel)

| 項目 | 規格 |
|------|------|
| **功率** | 25W / 10W / 4W / (2W 可訂製) |
| **Class** | Pure Class A, Single-Ended |
| **Power Tube** | 1x KT150 Tung-Sol |
| **Preamp Tubes** | 3x 12AX7 (ECC83 NOS + Genalex + TAD) |
| **Speaker** | 12" Fane F70 |
| **通道** | **雙通道** (Clean + Drive) |
| **Clean Channel** | High-headroom, open, fast, touch-responsive, **more mid-forward than Single 25** |
| **Drive Channel** | Vocal, sustaining overdrive, from bluesy textures to **wild saturation**, independent Gain + Master |
| **內建效果** | (未明確提及 reverb) |
| **Boost** | ✅ Footswitchable +7dB (clean ch) |
| **Mid Switch** | ✅ Footswitchable (500Hz-2kHz) |
| **FX Loop** | ✅ **High-definition buffered FX loop** (adjustable send) |
| **Cab Sim** | ❌ 無 |
| **XLR 輸出** | ❌ 無 |
| **輸出** | Line Out (160Ω), Speaker Out |
| **重量** | 18 kg |
| **保固** | 10 年 |
| **等待期** | **31 個月** |

**音色特性 (官方描述):**
- Clean: "High-headroom, open, fast, touch-responsive, **more mid-forward** than Single 25"
- Drive: "Vocal, sustaining overdrive, from bluesy textures to **wild saturation**"
- "Maintains clarity, definition, and string-to-string separation at all gain levels"
- "Equally at home in blues, expressive rock, post-punk, alternative, and **shoegaze**"

**音色定位:** British-voiced? Mid-forward clean + high-gain capable overdrive

---

### De Cillia Single 25 vs Special 25 對比

| 項目 | Single 25 | Special 25 |
|------|-----------|-----------|
| **價格** | $3,590 | $3,790 (+$200) |
| **通道** | 單通道 | 雙通道 (Clean + Drive) ✅ |
| **Preamp Tubes** | 2x 12AX7 | 3x 12AX7 |
| **Speaker** | Eminence Legend 1258 | Fane F70 |
| **FX Loop** | ❌ 無 | ✅ 有 (buffered) |
| **內建 Reverb** | ✅ Tube-driven | (未明確) |
| **音色** | American clean + edge | British mid-forward + high gain |
| **Overdrive** | Edge of breakup only | ✅ 完整 OD channel |

**關鍵差異:**
- Special 25 多 $200，但增加：
  - ✅ Dual channel (Clean + Drive)
  - ✅ FX Loop (buffered)
  - ✅ 更多 preamp tubes (3x vs 2x)
  - ✅ High-gain capable
  - ✅ Mid Switch

**建議:** 如果考慮購入，**Special 25 明顯更值得** (+$200 換來大幅提升功能)

---

### De Cillia 核心特點

**優勢:**
1. ✅ **世界首創** KT150 吉他音箱
2. ✅ **Pure Class A, Single-Ended** - 真正的 Class A 全功率範圍
3. ✅ **25W Class A ≈ 50W Class AB** - 實際音量很大
4. ✅ **功率可切換** (25W/10W/4W) - 適合不同場合
5. ✅ **10年保固** - 品質保證
6. ✅ **手工製作** - Vienna, Austria
7. ✅ **可客製化** - 多種 finish 選項

**劣勢:**
1. ❌ **價格極高** - $3,590-3,790 (是 JC-22 的 9-10 倍)
2. ❌ **等待期 31 個月** - 2.5 年交貨期
3. ❌ **無 Cab Sim** - 無法 direct recording (需外接 IR loader)
4. ❌ **無 XLR 輸出** - 只有 Line Out (160Ω)
5. ❌ **單喇叭 Mono** - 無 stereo
6. ❌ **重量重** - 17-18 kg
7. ❌ **真空管維護** - 需定期更換 KT150 (昂貴)

---

## 配置方案分析

### 方案 A: 現有配置 (DSM + Imperial + JC-22)

**設備清單:**
- DSM Dumblifier: $549
- Tone King Imperial MKII: $599
- Roland JC-22: $399
- **總計:** $1,547 USD

**角色分工:**

| 用途 | 使用設備 |
|------|---------|
| **錄音 (Dumble tone)** | DSM Dumblifier (with cab sim) → XLR → Interface |
| **錄音 (Tube tone)** | Imperial MKII (with 15 IRs) → XLR → Interface |
| **舞台演出** | JC-22 (stereo speakers + JC Chorus) |
| **練習** | JC-22 或 DSM/Imperial (headphone) |
| **Stereo effects** | JC-22 stereo FX loop |

**Pedal Chain:**
```
【錄音 - DSM】
Guitar → Empress MKII → PA-1QG → DSM (with cab sim) → XLR → Interface

【錄音 - Imperial】
Guitar → Empress MKII → PA-1QG → Imperial (with IR cab sim) → XLR → Interface

【舞台 - JC-22】
Guitar → Empress MKII → PA-1QG → [Blacklon] → [OD Stack] → JC-22 INPUT
  ↓
JC-22 FX SEND → [Stereo Effects: FF-1Y, Nucleo, AASB] → JC-22 FX RETURN L/R
```

**優勢:**
- ✅ **功能零重疊** - 三個 Amp 各司其職
- ✅ **成本最低** - $1,547
- ✅ **Stereo 能力完整** - JC-22 + stereo FX loop
- ✅ **Dumble 音色** - DSM 完整 Dumble ODS
- ✅ **Tube 音色** - Imperial 真空管
- ✅ **JC Chorus** - JC-22 傳奇音色
- ✅ **現貨** - 無等待期
- ✅ **低維護** - 只有 Imperial 需真空管維護

**劣勢:**
- ⚠️ JC-22 無 overdrive（需 pedals）
- ⚠️ JC-22 是 solid-state（無真空管溫暖感）

**Pedal 數量:** ~10-12 (包括完整 OD stack)

---

### 方案 B: Imperial + Special 25 (不購入 DSM)

**設備清單:**
- Tone King Imperial MKII: $599
- De Cillia Special 25: $3,790
- **總計:** $4,389 USD

**淘汰設備:**
- ~~DSM Dumblifier~~ ($549)
- ~~Roland JC-22~~ ($399)

**差額:** $4,389 - $1,547 = **+$2,842 USD**

---

**角色分工:**

| 用途 | 使用設備 |
|------|---------|
| **錄音** | Imperial (with 15 IRs) → XLR → Interface |
| **Dumble tone** | Imperial + ODL-1 CS (Dumble-style OD pedal) |
| **舞台演出** | Special 25 (Clean or Drive channel) |
| **練習** | Special 25 或 Imperial (headphone) |
| **Stereo effects** | ❌ 失去 (Special 25 只有 mono FX loop) |

**Pedal Chain:**
```
【錄音 - Imperial + ODL-1 CS】
Guitar → Empress MKII → PA-1QG → ODL-1 CS (Dumble-style) → Imperial (with IR) → XLR → Interface

【舞台 - Special 25】
Guitar → Empress MKII → PA-1QG → [Minimal OD Stack] → Special 25 (Clean or Drive)
  ↓
Special 25 FX Send → [Time-based Effects (mono only)] → Special 25 FX Return
```

**優勢:**
- ✅ **錄音能力更強** - Imperial 15組 IRs, MIDI, 可載入自定義 IR
- ✅ **真空管音色** - Special 25 Class A tube + Imperial tube preamp
- ✅ **Dual channel** - Special 25 Clean + Drive
- ✅ **內建 Overdrive** - Special 25 Drive channel
- ✅ **Pedal 簡化** - 可減少 3-4 個 pedals
- ✅ **音色彈性** - Clean/Drive footswitch 切換
- ✅ **功率可調** - 25W/10W/4W

**劣勢:**
- ❌ **失去 Stereo** - Special 25 單喇叭 mono
- ❌ **失去 JC Chorus** - 無法替代
- ❌ **失去完整 Dumble ODS** - ODL-1 CS 只是 OD pedal，非完整 amp sim
- ❌ **價格高昂** - +$2,842 USD
- ❌ **等待 31 個月** - 2.5 年交貨期
- ❌ **真空管維護** - Imperial + Special 25 雙重維護
- ❌ **重量增加** - Special 25 18kg vs JC-22 12kg

**Pedal 數量:** ~7-9 (減少 3-4 個)

---

### 方案 C: Imperial + Single 25 (不購入 DSM)

**設備清單:**
- Tone King Imperial MKII: $599
- De Cillia Single 25: $3,590
- **總計:** $4,189 USD

**差額:** $4,189 - $1,547 = **+$2,642 USD**

**劣勢 (相比 Special 25):**
- ❌ **無 FX Loop** - 所有效果器必須放音箱前
- ❌ **無 Dual Channel** - 只有單通道
- ❌ **無內建 Overdrive** - 只有 edge of breakup
- ⚠️ **無法簡化 Pedal Chain** - 反而更複雜

**結論:** **不推薦 Single 25**，如果考慮 De Cillia，**Special 25 明顯更好** (+$200 換來大幅功能提升)

---

## Pedal Chain 簡化分析

### 現有 OD Pedal Stack (推測)

基於之前討論的訊號鏈，假設你有以下 OD pedals:

1. **PRS Horsemeat** - Transparent boost/clean OD
2. **JHS Sweet Honey** - 溫暖 OD
3. **JHS Morning Glory** - Bluesbreaker-style
4. **Free the Tone ODL-1 CS** - Dumble-style (dual channel)
5. **Roshi Blacklon** - Fender Blackface amp sim
6. **(其他 OD pedals?)**

**現有必要 Pedals:**
- Empress MKII (Compressor)
- PA-1QG (EQ)
- FF-1Y (Delay)
- Nucleo (Stereo Reverb)
- AASB (Shimmer Reverb)

**總 Pedal 數量:** ~10-12

---

### 方案 A (現有配置) - Pedal 需求

**配置: DSM + Imperial + JC-22**

#### 錄音用 Pedals (DSM/Imperial):
```
Guitar → Empress MKII → PA-1QG → DSM/Imperial → Interface
```
- ✅ Compressor: Empress MKII
- ✅ EQ: PA-1QG
- ❌ 不需要 OD pedals (DSM 內建 Dumble OD / Imperial 內建 Lead channel)

#### 舞台用 Pedals (JC-22):
```
Guitar → Empress MKII → PA-1QG → [Blacklon?] → [OD Stack] → JC-22
  ↓
JC-22 FX Send → [FF-1Y, Nucleo (Stereo), AASB] → JC-22 FX Return
```

**必要 Pedals:**
- ✅ Compressor: Empress MKII
- ✅ EQ: PA-1QG
- ✅ Amp Sim: Blacklon (讓 JC-22 solid-state 有管機感)
- ✅ OD Stack: Horsemeat, Sweet Honey, Morning Glory, ODL-1 CS 等 (因為 JC-22 無 overdrive)
- ✅ Time-based: FF-1Y, Nucleo, AASB (放 stereo FX loop)

**總 Pedal 數量:** ~10-12
**無法簡化** - JC-22 無 overdrive，需要完整 OD stack

---

### 方案 B (Imperial + Special 25) - Pedal 需求

**配置: Imperial + Special 25 + ODL-1 CS**

#### 錄音用 Pedals (Imperial):
```
Guitar → Empress MKII → PA-1QG → ODL-1 CS → Imperial (with IR) → Interface
```
- ✅ Compressor: Empress MKII
- ✅ EQ: PA-1QG
- ✅ Dumble-style OD: ODL-1 CS (取代 DSM)

#### 舞台用 Pedals (Special 25):
```
Guitar → Empress MKII → PA-1QG → [Minimal OD] → Special 25 (Clean or Drive)
  ↓
Special 25 FX Send → [FF-1Y, Nucleo (mono only)] → Special 25 FX Return
```

**可能淘汰的 Pedals:**

1. **Roshi Blacklon** ✅ **確定淘汰**
   - 用途：讓 JC-22 solid-state 有管機感
   - Special 25 本身就是真空管 Class A
   - **不再需要**

2. **中高增益 OD Pedals (1-2 個)** ⚠️ **可能淘汰**
   - Special 25 Drive channel: "from bluesy textures to wild saturation"
   - 可能不需要 Morning Glory 或其他中增益 OD
   - **取決於 Special 25 Drive channel 的實際音色範圍**

3. **Sweet Honey / 其他溫暖 OD** ⚠️ **可能保留**
   - Special 25 是 British-voiced，不是 Fender-style
   - 如果需要 Fender-style 溫暖 OD，仍需保留

**確定保留的 Pedals:**
- ✅ Empress MKII (Compressor)
- ✅ PA-1QG (EQ)
- ✅ ODL-1 CS (Dumble-style OD)
- ✅ Horsemeat (Transparent boost，推動 Special 25)
- ✅ FF-1Y, Nucleo, AASB (Time-based effects)

**總 Pedal 數量:** ~7-9
**簡化幅度:** 減少 3-4 個 (Blacklon + 2-3 OD pedals)

---

### Pedal 簡化對比

| 項目 | 方案 A (現有配置) | 方案 B (Imperial + Special 25) |
|------|------------------|-------------------------------|
| **Compressor** | Empress MKII ✅ | Empress MKII ✅ |
| **EQ** | PA-1QG ✅ | PA-1QG ✅ |
| **Amp Sim** | Blacklon ✅ | ~~Blacklon~~ ❌ 淘汰 |
| **Dumble OD** | (DSM 內建) | ODL-1 CS ✅ |
| **Transparent Boost** | Horsemeat ✅ | Horsemeat ✅ (可能保留) |
| **溫暖 OD** | Sweet Honey ✅ | Sweet Honey ⚠️ (可能保留) |
| **Bluesbreaker OD** | Morning Glory ✅ | ~~Morning Glory~~ ⚠️ (可能淘汰) |
| **其他 OD** | (其他 OD pedals) | ~~部分 OD~~ ⚠️ (可能淘汰) |
| **Time-based** | FF-1Y, Nucleo, AASB ✅ | FF-1Y, Nucleo, AASB ✅ |
| **總數量** | ~10-12 | ~7-9 (-3-4) |

**簡化結論:**
- ✅ 確定淘汰: **Blacklon** (1個)
- ⚠️ 可能淘汰: **2-3 個中高增益 OD pedals**
- **總計簡化: 3-4 個 pedals**

---

## 取代性評估

### DSM Dumblifier 是否可被取代？

**DSM 提供的功能:**
1. 完整 Dumble ODS 音箱模擬 (preamp + power amp + cab sim 一體)
2. Dual channel (Clean + Overdrive)
3. Stereo cab sim
4. Stereo reverb
5. XLR 輸出
6. Headphone 輸出

**Imperial + ODL-1 CS 的組合:**
1. ODL-1 CS: Dumble-style OD pedal (dual channel)
2. Imperial: Tube preamp + Zero Watt Power Amp + 15 IRs cab sim + XLR

**對比分析:**

| 功能 | DSM Dumblifier | Imperial + ODL-1 CS |
|------|---------------|-------------------|
| **Dumble ODS 音色** | ✅ 100% 完整 amp sim | ⚠️ Dumble-style (OD pedal + tube preamp) |
| **Preamp** | ✅ 內建 Dumble preamp | ✅ Imperial tube preamp |
| **Power Amp Sim** | ✅ Zero Watt (analog) | ✅ Zero Watt (tube phase inverter) |
| **Cab Sim** | ✅ Stereo cab sim (固定) | ✅ 15組 OwnHammer IRs (可客製) |
| **XLR 輸出** | ✅ Dual XLR | ✅ Stereo XLR |
| **MIDI** | ❌ 無 | ✅ 128 presets |
| **自定義 IR** | ❌ 無 | ✅ 可載入 |
| **成本** | $549 | $599 + $425 = $1,024 |

**結論:**
- ✅ **錄音功能: 可取代** - Imperial 有完整 cab sim + XLR
- ⚠️ **Dumble 音色: 接近但非 100%**
  - DSM 是完整 Dumble ODS amp sim
  - ODL-1 CS 只是 Dumble-style OD pedal (設計師有 20+ 年 Dumble 維修經驗)
  - 組合可接近 Dumble 音色，但不完全相同
- ✅ **Imperial 更強的功能**: MIDI, 自定義 IR, 更多 IR 選擇
- ⚠️ **成本增加**: $549 → $1,024 (+$475)

**是否應該取代？**
- 如果你接受 **Dumble-style** 而非 **100% Dumble ODS**，可以取代
- 如果你需要 MIDI 控制和自定義 IR，Imperial 更好
- 如果你需要 100% 準確的 Dumble ODS 音色，保留 DSM

---

### Tone King Imperial 是否可被取代？

**Imperial 提供的功能:**
- 真空管 preamp (3x 12AX7)
- Zero Watt Power Amp
- 15組 OwnHammer IRs cab sim
- MIDI 128 presets
- 可載入自定義 IR
- Stereo XLR 輸出
- 4CM 支援

**De Cillia 提供的功能:**
- 真空管 Class A amp (1x KT150)
- 實體喇叭
- 無 cab sim
- 無 XLR
- 無 MIDI

**結論:**
- ❌ **完全無法取代** - De Cillia 是實體音箱，Imperial 是錄音前級工具
- De Cillia 無 cab sim, 無 XLR, 無 MIDI, 無自定義 IR
- 兩者完全不同類型的設備

---

### Roland JC-22 是否可被取代？

**JC-22 提供的功能:**
1. 實體 stereo speakers (2 x 6.5")
2. Stereo FX Loop
3. 傳奇 JC Chorus
4. Ultra-clean transparent tone
5. 價格親民 ($399)

**De Cillia Special 25 提供的功能:**
1. 實體 mono speaker (1 x 12")
2. Mono FX Loop
3. 無 Chorus
4. Tube Class A tone (有染色)
5. 價格高昂 ($3,790)

**對比分析:**

| 功能 | JC-22 | Special 25 |
|------|-------|-----------|
| **Speakers** | ✅ 2 x 6.5" **stereo** | 1 x 12" mono |
| **FX Loop** | ✅ **Stereo** | Mono only |
| **Chorus** | ✅ 傳奇 JC Chorus | ❌ 無 |
| **音色** | Ultra-clean, transparent | Tube, warm, mid-forward |
| **Overdrive** | ❌ 需 pedals | ✅ 內建 Drive channel |
| **價格** | $399 | $3,790 (9.5倍) |
| **等待期** | 現貨 | 31 個月 |
| **重量** | 12 kg | 18 kg |

**獲得的功能 (Special 25):**
- ✅ 真空管 Class A tone
- ✅ Dual channel (Clean + Drive)
- ✅ 內建 Overdrive
- ✅ 更大功率 (25W tube ≈ 50W solid-state)
- ✅ 功率可調 (25W/10W/4W)

**失去的功能 (JC-22):**
- ❌ Stereo speakers
- ❌ Stereo FX Loop (Nucleo/FF-1Y 立體聲無法發揮)
- ❌ JC Chorus (傳奇音色)
- ❌ Ultra-clean transparent tone (tube 有染色)
- ❌ 價格優勢 (貴 9.5 倍)

**結論:**
- ⚠️ **技術上可取代** - 都是實體音箱
- ❌ **但失去的比獲得的多** - 失去 stereo 和 JC Chorus
- ❌ **價格差距極大** - $3,790 vs $399
- ⚠️ **等待期過長** - 31 個月

**是否應該取代？**
- 如果你**完全不在乎 stereo** → 可以考慮
- 如果你**重視 stereo 和 JC Chorus** → 不建議取代
- 如果你**重視性價比** → 不建議取代

---

## 成本對比

### 總成本比較

| 配置 | 設備清單 | 總成本 | 差額 |
|------|---------|-------|-----|
| **方案 A (現有)** | DSM + Imperial + JC-22 | $1,547 | - |
| **方案 B** | Imperial + Special 25 + ODL-1 CS | $4,814 | +$3,267 |
| **方案 C** | Imperial + Single 25 + ODL-1 CS | $4,614 | +$3,067 |

### 方案 B 詳細成本

**新購設備:**
- De Cillia Special 25: $3,790
- Free the Tone ODL-1 CS: $425
- **新購總計:** $4,215

**保留設備:**
- Tone King Imperial MKII: $599

**淘汰設備:**
- DSM Dumblifier: $549 (回收?)
- Roland JC-22: $399 (回收?)
- Roshi Blacklon: ~$300 (回收?)
- 2-3 個 OD pedals: ~$300-500 (回收?)

**淨成本增加:** +$3,267 USD

**如果出售淘汰設備 (假設 70% 回收):**
- DSM: $549 x 0.7 = $384
- JC-22: $399 x 0.7 = $279
- Blacklon: $300 x 0.7 = $210
- 2-3 OD: $400 x 0.7 = $280
- **回收總計:** ~$1,153

**實際淨成本:** $3,267 - $1,153 = **~$2,114 USD**

---

### 長期成本考量

#### 真空管維護成本

**Imperial MKII:**
- 3x 12AX7: ~$50-100 (每 2-3 年更換)
- 年均: ~$25-50

**De Cillia Special 25:**
- 1x KT150: ~$100-150 (每 3-5 年更換)
- 3x 12AX7: ~$50-100 (每 2-3 年更換)
- 年均: ~$50-80

**方案 A (現有) 年均真空管成本:** ~$25-50 (只有 Imperial)
**方案 B 年均真空管成本:** ~$75-130 (Imperial + Special 25)

**10年真空管維護成本差:** ~$500-800 USD

---

### 等待期成本

**De Cillia 等待期:** 31 個月 (2.5 年)

**期間使用方案:**
1. 繼續使用現有 JC-22 (無額外成本)
2. 購買過渡期音箱 (需額外投資)

**建議:** 保留 JC-22 直到 De Cillia 交貨

---

## 最終建議

### 情境 A: 你非常重視 Stereo

**如果 Stereo 對你很重要:**
- Nucleo/FF-1Y 的立體聲音場是你的核心需求
- JC-22 的 stereo chorus 是你的招牌音色
- 舞台表演需要寬闊的立體聲呈現

**建議: ❌ 不要購入 De Cillia**

**原因:**
- De Cillia 是單喇叭 mono
- Special 25 的 FX loop 也是 mono
- 完全失去 stereo 能力
- Nucleo/FF-1Y 的立體聲無法發揮

**替代方案:**
保持現有配置: DSM + Imperial + JC-22 ($1,547)
- ✅ Stereo 能力完整
- ✅ 功能最完整
- ✅ 成本最低

---

### 情境 B: Stereo 對你不重要

**如果你主要用 mono，或不重視立體聲:**

**建議: ✅ 可以考慮購入 Special 25**

**配置方案:**
- 不購入 DSM
- Imperial MKII + ODL-1 CS (取代 DSM 的 Dumble 音色)
- Special 25 (取代 JC-22 的舞台角色)

**成本:**
- Imperial: $599 (保留)
- Special 25: $3,790 (新購)
- ODL-1 CS: $425 (新購)
- **總計:** $4,814 (+$3,267)

**淘汰設備:**
- ~~DSM~~ → Imperial + ODL-1 CS 取代
- ~~JC-22~~ → Special 25 取代
- ~~Blacklon~~ → 不需要 (Special 25 是真空管)
- ~~2-3 OD pedals~~ → Special 25 內建 Drive channel

**Pedal 簡化:**
- 減少 3-4 個 pedals
- 總 pedal 數: ~7-9

**訊號鏈:**
```
【錄音】
Guitar → Empress MKII → PA-1QG → ODL-1 CS → Imperial (15 IRs) → XLR → Interface

【舞台】
Guitar → Empress MKII → PA-1QG → [Minimal OD] → Special 25 (Clean/Drive)
  ↓
Special 25 FX Send → [Time-based (mono)] → FX Return
```

**優勢:**
- ✅ 真空管 Class A 音色
- ✅ Dual channel 彈性
- ✅ 內建 Overdrive
- ✅ Pedal chain 簡化
- ✅ Imperial 錄音能力更強 (MIDI, 自定義 IR)

**劣勢:**
- ❌ 失去 stereo
- ❌ 失去 JC Chorus
- ❌ 成本 +$3,267
- ❌ 等待 31 個月

---

### 情境 C: 你想要真空管音色但預算有限

**建議: 考慮其他真空管音箱**

**選項 1: Fender '65 Deluxe Reverb Reissue** (~$1,200)
- ✅ 22W tube combo (6V6)
- ✅ 經典 Fender Blackface tone
- ✅ 內建 reverb + vibrato
- ✅ 現貨
- ✅ 可淘汰 Blacklon
- ⚠️ 無 dual channel, 無 stereo

**配置:**
- Deluxe Reverb: $1,200
- Imperial: $599
- ~~DSM~~: 淘汰
- ~~JC-22~~: 淘汰或保留
- ~~Blacklon~~: 淘汰
- **總計:** $1,799 (不含 JC-22) 或 $2,198 (含 JC-22)

**成本增加:** $252 或 $651 (vs $3,267)

---

**選項 2: Vox AC15C1** (~$800)
- ✅ 15W Class A combo
- ✅ British tone
- ✅ 內建 reverb + tremolo
- ✅ 現貨
- ⚠️ 無 dual channel, 無 stereo

**配置:**
- Vox AC15C1: $800
- Imperial: $599
- ~~DSM~~: 淘汰
- ~~JC-22~~: 淘汰或保留
- ~~Blacklon~~: 淘汰
- **總計:** $1,399 (不含 JC-22) 或 $1,798 (含 JC-22)

**成本增加:** -$148 或 $251 (vs $3,267)

---

### 我的最終建議

#### 🏆 推薦方案: 保持現有配置

**配置: DSM + Imperial + JC-22** ($1,547)

**理由:**

1. ✅ **功能最完整**
   - 錄音: DSM (Dumble) + Imperial (Tube, 15 IRs, MIDI)
   - 舞台: JC-22 (Stereo, Chorus)
   - Stereo 能力完整

2. ✅ **成本最低**
   - 總成本 $1,547
   - 只有 Imperial 需真空管維護 (~$25-50/年)

3. ✅ **現貨可用**
   - 無需等待 31 個月

4. ✅ **功能零重疊**
   - 三個 Amp 各司其職
   - 沒有浪費

5. ✅ **Stereo 能力**
   - Nucleo/FF-1Y 完整發揮
   - JC Chorus 傳奇音色

6. ✅ **100% Dumble ODS**
   - DSM 完整 Dumble ODS amp sim

**Pedal Chain:**
```
【錄音 - DSM】
Guitar → Empress MKII → PA-1QG → DSM → XLR → Interface

【錄音 - Imperial】
Guitar → Empress MKII → PA-1QG → Imperial (15 IRs) → XLR → Interface

【舞台 - JC-22】
Guitar → Empress MKII → PA-1QG → [Blacklon] → [OD Stack] → JC-22
  ↓
JC-22 FX Send → [Stereo Effects] → JC-22 FX Return L/R
```

---

#### ⚠️ 條件性推薦: 購入 Special 25

**前提條件 (必須全部符合):**

1. ✅ Stereo **完全不重要**
2. ✅ 非常想要真空管 Class A 音色
3. ✅ 願意等待 31 個月
4. ✅ 願意增加 $3,267 (或實際 ~$2,114 after 出售)
5. ✅ 接受 Dumble-style (ODL-1 CS) 而非 100% Dumble ODS (DSM)
6. ✅ 不介意失去 JC Chorus

**配置: Imperial + Special 25 + ODL-1 CS** ($4,814)

**淘汰:**
- ~~DSM~~ → Imperial + ODL-1 CS
- ~~JC-22~~ → Special 25
- ~~Blacklon~~
- ~~2-3 OD pedals~~

**Pedal 簡化:** 減少 3-4 個
**Pedal 數量:** ~7-9

---

## 附錄: 關鍵決策因素

### 決策樹

```
1. Stereo 對你重要嗎？
   ├─ 是 → 保持現有配置 (DSM + Imperial + JC-22)
   └─ 否 → 繼續

2. 你能等待 31 個月嗎？
   ├─ 否 → 保持現有配置 或 考慮 Fender/Vox
   └─ 是 → 繼續

3. 你能接受增加 $3,267 嗎？
   ├─ 否 → 保持現有配置 或 考慮 Fender/Vox
   └─ 是 → 繼續

4. 你能接受 Dumble-style (ODL-1 CS) 而非 100% Dumble ODS (DSM)？
   ├─ 否 → 保持現有配置 (保留 DSM)
   └─ 是 → 可以考慮購入 Special 25

5. 你能接受失去 JC Chorus 嗎？
   ├─ 否 → 保持現有配置 (保留 JC-22)
   └─ 是 → 可以購入 Special 25
```

---

### 核心權衡

| 項目 | 現有配置 | Imperial + Special 25 |
|------|---------|---------------------|
| **成本** | $1,547 | $4,814 (+210%) |
| **等待期** | 現貨 | 31 個月 |
| **Stereo** | ✅ 完整 | ❌ 失去 |
| **真空管音色** | ⚠️ Imperial only | ✅ Imperial + Special 25 |
| **Dumble 音色** | ✅ 100% (DSM) | ⚠️ Dumble-style (ODL-1 CS) |
| **JC Chorus** | ✅ 有 | ❌ 失去 |
| **Pedal 數量** | ~10-12 | ~7-9 (-3-4) |
| **維護成本** | 低 | 高 (雙重真空管) |

---

## 總結

### 現有配置的完美性

你目前的 **DSM + Imperial + JC-22** 配置其實已經接近完美：

1. ✅ **錄音能力完整** - DSM (Dumble ODS) + Imperial (Tube, 15 IRs, MIDI)
2. ✅ **舞台能力完整** - JC-22 (Stereo, Chorus, Pedal Platform)
3. ✅ **功能零重疊** - 三個設備各司其職
4. ✅ **成本最低** - $1,547
5. ✅ **Stereo 能力完整** - Nucleo/FF-1Y 充分發揮
6. ✅ **現貨可用** - 無等待期

### De Cillia 的定位

De Cillia 是**極致精品級真空管音箱**:
- 世界首創 KT150 吉他音箱
- Pure Class A, Single-Ended
- 手工製作，10年保固
- 適合：追求極致音色的玩家、無預算限制、願意等待

但它**不是萬能解決方案**:
- 無法取代專業錄音工具 (無 cab sim/XLR)
- 無法提供 stereo 能力
- 價格極高，等待期極長

### 最終答案

**除非 Stereo 對你完全不重要，否則建議保持現有配置。**

你的現有配置已經提供：
- ✅ 最佳性價比
- ✅ 最完整功能
- ✅ 最低維護成本
- ✅ Stereo 能力

De Cillia 只會：
- ❌ 增加成本 +210%
- ❌ 失去 stereo
- ❌ 失去 JC Chorus
- ❌ 等待 31 個月
- ✅ 獲得真空管音色 (但 Imperial 已有)
- ✅ Pedal 簡化 3-4 個 (有限收益)

**性價比極低。**

---

**報告結束**

如需進一步分析特定配置或音色需求，請提供更多細節。
