# Free the Tone FF-1Y FUTURE FACTORY - 使用範例與控制說明

**版本:** 1.0
**更新日期:** 2026-01-11
**資料來源:** `shared/equipment_database/pedals/ff1y.yaml`

---

## 目錄

1. [控制介面完整說明](#控制介面完整說明)
2. [Parallel Mode 並聯模式範例](#parallel-mode-並聯模式範例)
3. [Series Mode 串聯模式範例](#series-mode-串聯模式範例)
4. [模式選擇指南](#模式選擇指南)
5. [進階技巧](#進階技巧)

---

## 控制介面完整說明

### 主要旋鈕與按鈕

#### **1. Delay Time (×2) - 延遲時間**
- **位置:** 雙旋鈕（Delay A 和 Delay B 各一個）
- **功能:** 設定延遲音重複的時間間隔
- **範圍:** 待手冊確認（典型數位延遲為 20ms ~ 2000ms）
- **調整影響:**
  - **順時針旋轉** → 延遲時間變長（節奏變慢）
  - **逆時針旋轉** → 延遲時間變短（節奏變快）
- **使用技巧:**
  - **短延遲 (20-120ms)**: Slap Back、增加厚度
  - **中延遲 (120-400ms)**: 節奏延遲、配合歌曲速度
  - **長延遲 (400ms+)**: Ambient、音景創造

#### **2. Feedback (×2) - 回授/重複次數**
- **位置:** 雙旋鈕（Delay A 和 Delay B 各一個）
- **功能:** 控制延遲音重複的次數
- **範圍:** 0% ~ 無限重複（自我振盪）
- **調整影響:**
  - **0%** → 延遲音只出現一次
  - **30-50%** → 延遲音重複 2-4 次
  - **70%+** → 延遲音重複多次
  - **100%** → 無限重複（自我振盪，創造 Drone 效果）
- **使用技巧:**
  - **低 Feedback (1-2次)**: Slap Back、Jazz 細膩延遲
  - **中 Feedback (3-5次)**: 標準延遲效果
  - **高 Feedback (6次+)**: Ambient、Post Rock 音牆
  - **警告**: 過高的 Feedback 可能導致音量累積失控

#### **3. Mix - 乾濕混合**
- **位置:** 單一旋鈕
- **功能:** 調整原始訊號（乾）與延遲訊號（濕）的比例
- **範圍:** 0% ~ 100%
- **調整影響:**
  - **0%** → 只有原始訊號（Bypass）
  - **20-30%** → 細膩的延遲效果（Jazz、Neo Soul）
  - **50%** → 乾濕各半
  - **70%+** → 明顯的延遲效果（Ambient）
  - **100%** → 幾乎只有延遲音（特殊效果）
- **使用技巧:**
  - **Rhythm Guitar**: 20-35%
  - **Lead Guitar**: 35-50%
  - **Ambient Soundscapes**: 60-80%

#### **4. 3-Band EQ - 三頻段等化器**
- **位置:** 三個旋鈕（Low / Mid / High）
- **功能:** **僅塑造延遲音的音色，不影響原始訊號**
- **頻段:**
  - **Low (低頻)**: 待手冊確認（典型為 100-200Hz）
  - **Mid (中頻)**: 待手冊確認（典型為 800-1.5kHz）
  - **High (高頻)**: 待手冊確認（典型為 3.2-6.4kHz）
- **調整影響:**
  - **Low (低頻)**:
    - 提升 → 延遲音溫暖、厚實
    - 削減 → 延遲音清爽、避免混濁
  - **Mid (中頻)**:
    - 提升 → 延遲音更有存在感
    - 削減 → 延遲音更融入背景
  - **High (高頻)**:
    - 提升 → 延遲音明亮、清晰
    - 削減 → 延遲音溫暖、類比感
- **使用技巧:**
  - **清晰延遲**: Low -2dB, Mid +1dB, High +2dB
  - **溫暖延遲**: Low +2dB, Mid 0dB, High -3dB
  - **背景 Pad 感**: Low -3dB, Mid -2dB, High -4dB

#### **5. Modulation Controls - 調變控制**
- **位置:** 待手冊確認（可能包含 Depth 和 Rate）
- **功能:** 控制 **Random Fluctuating Phase Modulation**（世界首創）
- **Random Phase Modulation 特性:**
  - 非傳統固定 LFO 調變
  - 隨機相位變化創造有機感
  - 讓延遲音"會呼吸"
- **調整影響:**
  - **低設定 (Depth: 10-20%)**: 細微的空間感增強，不明顯但豐富
  - **中設定 (Depth: 30-50%)**: 明顯的調變效果，類比感
  - **高設定 (Depth: 60%+)**: 極端調變，實驗性音色
- **使用技巧:**
  - **Jazz/Fusion**: Depth 10-20%（細膩）
  - **Neo Soul/Post Rock**: Depth 30-40%（有機）
  - **Ambient/Experimental**: Depth 50%+（明顯）

#### **6. Routing Select - 路由選擇**
- **位置:** 切換開關
- **功能:** 選擇雙延遲模組的連接方式
- **選項:**
  - **Parallel (並聯)**
  - **Series (串聯)**
- **調整影響:**
  - **Parallel**: 兩組延遲同時處理訊號 → 豐富立體聲效果
  - **Series**: 訊號依序經過兩組延遲 → 複雜疊加效果
- **使用技巧:** 詳見下方範例章節

#### **7. Soft Clipping Control - 軟削波控制**
- **位置:** 旋鈕或開關（待手冊確認）
- **功能:** 為延遲訊號添加諧波失真
- **調整影響:**
  - **關閉 (0%)** → 清晰的數位延遲音
  - **開啟 (10-30%)** → 延遲音帶有溫暖的類比感
  - **高設定 (40%+)** → 明顯的諧波豐富度，類似類比磁帶
- **使用技巧:**
  - **數位清晰感**: 關閉
  - **類比溫暖感**: 10-20%
  - **磁帶回音模擬**: 30-40%

---

### 特殊功能按鈕

#### **Tap Tempo - 節奏輸入**
- **功能:** 透過踩踏節拍，延遲時間自動同步歌曲速度
- **使用方式:** 按 2-4 次節拍，FF-1Y 自動計算並設定延遲時間
- **應用:** 現場演出快速配合歌曲 BPM

#### **Preset 切換**
- **功能:** 快速切換 128 個預設槽位
- **Trail Function:** 切換預設時，前一個預設的延遲音自然消失（不會突然中斷）

#### **Phase Invert - 相位反轉**
- **功能:** 反轉延遲音的相位（180° 相位翻轉）
- **應用:** 解決延遲音在樂團 Mix 中被其他樂器掩蓋的問題

---

### 連接埠

- **Input A / Input B**: 立體聲輸入（可接單聲道或立體聲）
- **Output A / Output B**: 立體聲輸出
- **EXT Jack**: 外部控制（Tap Tempo 或其他功能）
- **MIDI IN**: MIDI 控制輸入（DIN 5-pin）
- **DC 9V**: 電源輸入（Center Negative, 350mA）

---

## Parallel Mode 並聯模式範例

### **運作原理**
```
輸入訊號 ─┬─→ Delay A ─┬─→ 輸出
          └─→ Delay B ─┘
```
- 原始訊號**同時**送入兩組延遲
- 兩組延遲**獨立處理**後混合輸出
- 創造**豐富的立體聲效果**

---

### **範例 1：立體聲 Ping-Pong Delay（乒乓延遲）**

**音樂風格**: Post Rock, Ambient, Neo Soul

**設定**:
| 參數 | Delay A | Delay B |
|------|---------|---------|
| **Time** | 400ms（四分音符） | 600ms（附點四分音符） |
| **Feedback** | 3次重複 | 3次重複 |
| **Pan/Output** | Left（左聲道） | Right（右聲道） |
| **EQ Low** | 0dB | 0dB |
| **EQ Mid** | 0dB | 0dB |
| **EQ High** | +1dB | +2dB（略亮） |

**全局設定**:
- **Mix**: 40-50%
- **Modulation Depth**: 低（10-20%）
- **Soft Clipping**: 關閉或極低
- **Routing**: Parallel

**效果**:
- 延遲音在左右聲道交替出現（Ping-Pong 效果）
- 創造寬廣的立體聲空間感
- Random Phase Modulation 讓延遲音有細微的相位變化

**適合場景**:
- Clean Tone Arpeggios
- Ambient Lead Guitar
- Post Rock Clean Riffs

---

### **範例 2：Double Delay Texture（雙重延遲紋理）**

**音樂風格**: Jazz, Fusion

**設定**:
| 參數 | Delay A（短延遲） | Delay B（長延遲） |
|------|------------------|------------------|
| **Time** | 120ms（Slap Back） | 380ms（中長延遲） |
| **Feedback** | 1次 | 4次 |
| **EQ Low** | -2dB（削減混濁） | 0dB |
| **EQ Mid** | 0dB | 0dB |
| **EQ High** | +1dB | -2dB（溫暖） |

**全局設定**:
- **Mix**: 30%
- **Modulation Depth**: 中等（30%）
- **Soft Clipping**: 10-15%
- **Routing**: Parallel

**效果**:
- 短延遲（Delay A）增加厚度和存在感
- 長延遲（Delay B）創造空間深度
- 兩者疊加創造複雜的延遲紋理
- Soft Clipping 添加細微的類比溫暖感

**適合場景**:
- Jazz Lead Solo
- Neo Soul Chord Stabs
- Fusion Clean Tone

---

### **範例 3：Stereo Ambient Wash（立體聲 Ambient 音牆）**

**音樂風格**: Post Rock, Shoegaze, Ambient

**設定**:
| 參數 | Delay A | Delay B |
|------|---------|---------|
| **Time** | 500ms | 750ms（不同節奏比例） |
| **Feedback** | 6次（長重複） | 5次 |
| **EQ Low** | +1dB | +2dB |
| **EQ Mid** | -2dB（削減，讓延遲音退到背景） | -3dB |
| **EQ High** | +1dB | 0dB |

**全局設定**:
- **Mix**: 60-70%
- **Modulation Depth**: 高（50-60%）
- **Soft Clipping**: 30%（明顯類比感）
- **Routing**: Parallel

**效果**:
- 兩組不同時間的延遲創造複雜節奏紋理
- Random Phase Modulation 高設定讓延遲音"會呼吸"
- Soft Clipping 添加溫暖諧波
- EQ 削減中頻讓延遲音像 Ambient Pad

**適合場景**:
- Post Rock Swells
- Ambient Pads
- Shoegaze Walls of Sound

---

## Series Mode 串聯模式範例

### **運作原理**
```
輸入訊號 ─→ Delay A ─→ Delay B ─→ 輸出
```
- 訊號**先經過 Delay A**
- Delay A 的輸出**再送入 Delay B**
- 創造**疊加的複雜延遲效果**

---

### **範例 1：Rhythmic Cascading Delay（節奏瀑布延遲）**

**音樂風格**: Progressive Rock, Math Rock

**設定**:
| 參數 | Delay A | Delay B |
|------|---------|---------|
| **Time** | 200ms（十六分音符） | 400ms（八分音符） |
| **Feedback** | 2次 | 3次 |
| **EQ Low** | 0dB | 0dB |
| **EQ Mid** | +1dB | 0dB |
| **EQ High** | +2dB（保持清晰） | +1dB |

**全局設定**:
- **Mix**: 45%
- **Modulation Depth**: 低（保持節奏精準）
- **Soft Clipping**: 關閉
- **Routing**: Series

**效果**:
```
原始音 → 200ms → 400ms → 600ms → 800ms → 1000ms...
```
- 創造多個節奏層次的疊加
- 形成類似「瀑布」般的延遲效果
- 每個重複音符都有自己的延遲鏈

**適合場景**:
- Math Rock 複雜節奏 Riff
- Prog Rock Lead
- 實驗性節奏效果

---

### **範例 2：Tape Echo Emulation（磁帶回音模擬）**

**音樂風格**: Blues, Classic Rock, Neo Soul

**設定**:
| 參數 | Delay A（第一次損耗） | Delay B（第二次損耗） |
|------|---------------------|---------------------|
| **Time** | 350ms | 350ms（與 A 相同） |
| **Feedback** | 4次 | 3次 |
| **EQ Low** | 0dB | -1dB |
| **EQ Mid** | 0dB | -1dB |
| **EQ High** | -2dB（模擬磁帶損耗） | -4dB（再削減更多高頻） |

**全局設定**:
- **Mix**: 35%
- **Modulation Depth**: 中等（30-40%，模擬 Wow & Flutter）
- **Soft Clipping**: 35%（明顯類比感）
- **Routing**: Series

**效果**:
- 延遲音經過兩次處理，每次都損失高頻
- 創造類比磁帶回音的漸暗效果
- Modulation 模擬磁帶不穩定的音高飄移
- Soft Clipping 添加磁帶飽和感

**適合場景**:
- Blues Lead Solo
- Classic Rock Rhythm
- Neo Soul Vintage Tones

---

### **範例 3：Experimental Ambient Layers（實驗性 Ambient 層次）**

**音樂風格**: Ambient, Experimental, Post Rock

**設定**:
| 參數 | Delay A | Delay B |
|------|---------|---------|
| **Time** | 800ms | 1200ms（長延遲） |
| **Feedback** | 5次（長尾音） | 6次 |
| **EQ Low** | 0dB | -4dB（大幅削減） |
| **EQ Mid** | 0dB | +2dB（保留中頻） |
| **EQ High** | 0dB | -5dB（大幅削減） |
| **Phase Invert** | 關閉 | **開啟**（反轉相位） |

**全局設定**:
- **Mix**: 65-80%
- **Modulation Depth**: 高（55%）
- **Soft Clipping**: 40%
- **Routing**: Series

**效果**:
- 延遲音經過兩層長時間處理
- **Phase Invert** 創造詭異的空間感與相位抵消效果
- EQ 塑造讓 Delay B 的延遲音聽起來像「背景 Pad」
- 高 Feedback 創造無盡的延遲尾音

**適合場景**:
- Ambient Soundscapes
- Post Rock 音牆
- 實驗性音樂

---

### **範例 4：Dotted Eighth Note Delay Chain（附點八分音符延遲鏈）**

**音樂風格**: U2-style Delay, Pop Rock

**設定（假設 120 BPM）**:
| 參數 | Delay A | Delay B |
|------|---------|---------|
| **Time** | 375ms（附點八分音符 @ 120 BPM） | 375ms（與 A 相同） |
| **Feedback** | 3次 | 2次 |
| **EQ Low** | -1dB | -2dB |
| **EQ Mid** | 0dB | 0dB |
| **EQ High** | +1dB | +2dB（增加清晰度） |

**全局設定**:
- **Mix**: 40%
- **Modulation Depth**: 極低（5-10%，保持節奏精準）
- **Soft Clipping**: 關閉
- **Routing**: Series

**效果**:
```
原始音 → 375ms → 750ms → 1125ms → 1500ms...
但 Delay B 讓每個重複音有自己的延遲鏈
```
- 創造更複雜的附點八分音符節奏紋理
- 每個延遲音有「雙重回音」效果
- 保持節奏精準（低 Modulation）

**適合場景**:
- U2-style Arpeggios
- Pop Rock Clean Rhythm
- Ambient Arpeggios

**使用技巧**:
- 使用 **Tap Tempo** 快速配合歌曲 BPM
- 計算公式：120 BPM → 附點八分音符 = 60000ms ÷ 120 ÷ 2 × 1.5 = 375ms

---

## 模式選擇指南

### **快速選擇表**

| **需求** | **模式選擇** | **原因** |
|---------|------------|---------|
| 寬廣立體聲效果 | **Parallel** | 兩組延遲可分配左右聲道 |
| 複雜節奏疊加 | **Series** | 延遲音會再產生延遲，創造多層節奏 |
| 清晰的延遲音 | **Parallel** | 兩組延遲不會互相影響 |
| 類比磁帶感 | **Series** | 訊號經過兩次處理，累積類比特性 |
| Post Rock Ambient | **Parallel** | 創造寬廣空間感 |
| Math Rock 節奏 | **Series** | 複雜的節奏分割效果 |
| Jazz/Fusion 細膩延遲 | **Parallel** | 可同時擁有短 Slap Back + 長延遲 |
| 實驗性音景 | **Series** | 訊號經過多次處理創造極端效果 |

---

### **與 Random Phase Modulation 的搭配**

#### **並聯模式 + Random Phase Modulation**
- **效果**: 兩組延遲各自產生隨機相位變化
- **聲音**: 非常寬廣、有機、會呼吸的立體聲空間
- **適合**: Ambient、Post Rock、Neo Soul
- **建議設定**: Modulation Depth 30-50%

#### **串聯模式 + Random Phase Modulation**
- **效果**: 相位變化累積疊加（Delay A 的調變被 Delay B 再次調變）
- **聲音**: 更極端、更實驗性的調變效果
- **適合**: Experimental、Drone、Shoegaze
- **建議設定**: Modulation Depth 40-60%

---

## 進階技巧

### **1. 同一首歌內切換模式**

**場景範例：Post Rock 歌曲結構**

| 歌曲段落 | 模式 | 預設設定 | 效果 |
|---------|------|---------|------|
| **Verse（主歌）** | Parallel | Mix 30%, Feedback 低 | 簡單清晰的立體聲延遲 |
| **Chorus（副歌）** | Parallel | Mix 50%, Feedback 中 | 更豐富的空間感 |
| **Bridge/Build-up** | Series | Mix 70-80%, Feedback 高 | 瀑布般的延遲堆疊效果 |
| **Outro（尾奏）** | Series + Trail Function | 保持高 Mix, 高 Feedback | 史詩般的結尾，延遲自然消失 |

**操作方式**:
- 使用 **128 預設功能** 儲存各段落設定
- 使用 **MIDI Program Change** 或 **腳踏板** 快速切換
- 利用 **Trail Function** 讓切換更自然

---

### **2. 與音箱 FX Loop 搭配**

由於 FF-1Y 支援 **Stereo I/O**，搭配 JC-22 或 Tone King 的 Stereo FX Loop：

#### **Parallel 模式**
```
Guitar → Preamp → [FX Send L/R] → FF-1Y (Parallel) → [FX Return L/R] → Power Amp L/R → Speakers
```
- **Delay A** → 送往左聲道
- **Delay B** → 送往右聲道
- **效果**: 充分發揮立體聲空間感

#### **Series 模式**
```
Guitar → Preamp → [FX Send Stereo] → FF-1Y (Series) → [FX Return Stereo] → Power Amp → Speakers
```
- 訊號依序經過 Delay A → Delay B
- 兩組延遲的輸出以立體聲呈現
- **效果**: 複雜的立體聲延遲層次

---

### **3. 預設庫管理策略**

**128 預設槽位建議配置**:

| 預設範圍 | 用途 | 範例 |
|---------|------|------|
| **1-10** | 常用基礎設定 | Slap Back, 標準延遲, Ambient |
| **11-30** | 並聯模式專用 | Ping-Pong, Double Texture, Stereo Wash |
| **31-50** | 串聯模式專用 | Rhythmic Cascade, Tape Echo, Dotted 8th |
| **51-70** | 歌曲專用設定 | 各首歌的 Verse/Chorus/Solo 設定 |
| **71-90** | 實驗性設定 | 極端 Modulation, Phase Invert 效果 |
| **91-99** | 特殊效果 | Self-Oscillation, Drone, Siren |

---

### **4. 初學者建議設定流程**

**步驟 1：從並聯模式開始**
1. 設定 **Routing: Parallel**
2. **Delay A**: Time 400ms, Feedback 3次
3. **Delay B**: Time 600ms, Feedback 3次
4. **Mix**: 40%
5. **Modulation**: 20%
6. **Soft Clipping**: 關閉
7. **EQ**: 全部 0dB（Flat）

**步驟 2：調整至舒適音色**
- 如果延遲音太亮 → 削減 **EQ High**
- 如果延遲音太暗 → 削減 **EQ Low**
- 如果想要類比感 → 開啟 **Soft Clipping 10-20%**
- 如果想要更豐富空間感 → 提升 **Modulation 至 30-40%**

**步驟 3：實驗串聯模式**
1. 切換 **Routing: Series**
2. 聽見差異：延遲音變得更複雜、更疊加
3. 調整 **EQ** 讓 Delay B 的延遲音逐漸變暗（模擬類比）

---

### **5. 故障排除**

**問題：延遲音過於混濁**
- **解決方案**: 削減 **EQ Low** -2 至 -4dB

**問題：延遲音太亮、刺耳**
- **解決方案**: 削減 **EQ High** -2 至 -3dB

**問題：延遲音被吉他音掩蓋**
- **解決方案**:
  1. 提升 **Mix**
  2. 開啟 **Phase Invert** 試試
  3. 調整 **EQ** 讓延遲音佔據不同頻段

**問題：串聯模式下延遲音過多**
- **解決方案**: 降低 **Feedback**（特別是 Delay B）

**問題：想要更明顯的立體聲效果**
- **解決方案**:
  1. 使用 **Parallel 模式**
  2. 設定 **Delay A 和 Delay B 的時間差異更大**（例如 400ms vs 750ms）
  3. 提升 **Modulation Depth**

---

## 總結

### **FF-1Y 核心優勢**

1. **世界首創 Random Fluctuating Phase Modulation** - 創造有機、會呼吸的延遲音
2. **雙延遲模組** - 一台效果器實現兩台延遲效果器的效果
3. **3-band EQ** - 精準塑造延遲音色而不影響原始訊號
4. **Soft Clipping** - 為數位延遲添加類比溫暖感
5. **128 Presets + MIDI** - 適合複雜的現場演出或錄音室使用
6. **Stereo I/O** - 充分發揮雙音箱或立體聲 FX Loop 的能力

### **最佳使用建議**

- **初學者**: 從並聯模式開始，使用相近的 Delay Time，Mix 保持 30-40%
- **中階使用者**: 實驗不同的 Delay Time 組合，善用 3-band EQ 塑造音色
- **進階使用者**: 串聯模式 + Phase Invert + 極端 Modulation 創造實驗性音色，建立完整的 128 預設庫

### **適合音樂風格**

| 風格 | 推薦模式 | 關鍵設定 |
|------|---------|---------|
| **Jazz** | Parallel | 短延遲 + 低 Mix (20-30%) |
| **Neo Soul** | Parallel | 雙重延遲紋理 + 中 Modulation |
| **Post Rock** | 兩者皆可 | 高 Feedback + 高 Mix |
| **Ambient** | 兩者皆可 | 長延遲 + 高 Modulation + Soft Clipping |
| **Math Rock** | Series | 節奏瀑布 + 低 Modulation |
| **Blues/Classic Rock** | Series | 磁帶回音模擬 + Soft Clipping |

---

**文件版本:** 1.0
**最後更新:** 2026-01-11
**下次更新計劃:** 補充實際手冊確認的旋鈕範圍與頻段參數

**相關文件**:
- `shared/equipment_database/pedals/ff1y.yaml` - FF-1Y 完整技術規格
- `projects/2025-v3-signal-chain/research/compressor_eq_spatial_effects_technical_data.md` - 空間系效果器技術資料
