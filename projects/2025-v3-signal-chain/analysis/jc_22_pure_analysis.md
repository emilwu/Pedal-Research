# 訊號鏈轉換分析：Pure JC-22 Front-End Stereo

## 1. 核心概念變更

此配置完全移除了真空管前級 (Tone King Imperial MKII)，並將所有訊號直接輸入到 **Roland JC-22** 的前端輸入 (Front Inputs)。這是一個「純晶體機 (Pure Solid State)」的挑戰，目標是利用效果器模擬出真空管的觸感與動態。

### 角色轉換對比

| 設備 | ToneKing Only (v1.0) | Pure JC-22 (v2.0) | 變動說明 |
|------|-----------------------|-------------------|----------|
| **Primary Amp** | ToneKing Preamp Pedal | **Roland JC-22** | 從管機前級轉為晶體 Combo 音箱 |
| **Virtual Preamp**| (無，本身即為 Preamp) | **Roshi Blacklon** / **ODL-1-CS** | 使用效果器作為「虛擬前級」來染色 |
| **Stereo Routing**| FX Loop Send/Return | **Front Inputs L/R** | 直接進前級輸入，不經過 FX Loop |
| **Gain Staging** | 傳統 Amp 推動 | **Pedal Platform** | 全靠效果器提供增益，Amp 設為 Clean |

---

## 2. 訊號流邏輯：Front-End Stereo

由於 `amps.yaml` 定義 JC-22 為無 FX Loop (或不使用)，我們採用 **Front-End Stereo** 策略。這意味著立體聲效果器 (Nucleo, FF-1Y) 必須位於訊號鏈的最末端，直接接入音箱的 Input L 和 Input R。

### 路由邏輯
1.  **Mono Section (Dynamic & Drive)**: 吉他 → Buffer++ Loop 1 (Compressor, OD, Preamp Pedals)
2.  **Stereo Split**: 訊號在進入空間系效果器 (Nucleo/FF-1Y) 時從 Mono 轉為 Stereo。
3.  **Final Output**: Stereo Left → JC-22 Input L / Stereo Right → JC-22 Input R。

---

## 3. 關鍵挑戰與解決方案

### 3.1 挑戰：失去真空管的溫暖 (Tube Warmth)
JC-22 以 "Ultra-Clean" 聞名，但也意味著它缺乏真空管的壓縮感與諧波。
*   **解決方案**: **Roshi Blacklon** 必須設定為 "Always-On" 或作為基礎音色核心。
    *   **6V6 Mode**: 用於 Neo Soul/Clean，提供類似 Fender Deluxe Reverb 的溫暖。
    *   **6L6 Mode**: 用於 Post Rock，提供更大的 Headroom 和低頻緊實度。
*   **輔助方案**: **Empress Compressor MKII** 可以設定慢一點的 Attack 來模擬管機的 Sag (下陷感)。

### 3.2 挑戰：前級輸入的 Headroom
直接進入 Input L/R 代表訊號會經過 JC-22 的晶體前級 (Preamp Section)。如果輸入訊號過大 (例如來自 PA-1QG 的 Boost)，可能會導致晶體前級產生不悅耳的 Hard Clipping。
*   **解決方案**: 嚴格控制 Buffer++ Output Level。所有的 Gain Staging 應該在效果器鏈內部完成，最終輸出至音箱的電平應保持在 Instrument Level，而非 Line Level。

### 3.3 挑戰：Stereo Chorus 的衝突
JC-22 內建的 Stereo Chorus 是在它的前級之後處理。
*   **策略**: 如果開啟內建 Chorus，它會疊加在已經是 Stereo 的訊號上（來自 Nucleo/FF-1Y）。這可能會造成相位的混亂。
*   **建議**: 在此配置下，建議 **關閉** JC-22 內建 Chorus，改用 **Boss CE-2W** 在 Mono 段做染色，或者僅在需要極度迷幻效果時才開啟內建 Chorus。

---

## 4. 預期音色結果

此配置將獲得最極致的 "Pedal Platform" 體驗。聲音的每一個細節都由腳下的效果器決定，JC-22 僅作為一個忠實、寬廣的立體聲擴音器。

*   **優點**: 音色可塑性極高，不受 Amp 本身個性的太多干擾。立體聲效果直接進 Input，聲音會非常直接 (In-your-face)。
*   **缺點**: 需要花更多時間調整 Drive Pedals 的高頻衰減 (Tone 鈕)，因為 JC-22 不會像管機一樣自然平滑掉尖銳的高頻。

---

## 5. 結論
這是一個現代化的 "Ampless" 概念的實體化（雖然有 Amp，但把 Amp 當 PA 用）。Roshi Blacklon 取代了 ToneKing 成為了「靈魂」，而 JC-22 成為了「身體」。
