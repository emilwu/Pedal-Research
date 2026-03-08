# Signal Chain: Pure Solid State - JC-22 Stereo Front-End v1.0

**Version:** 1.0 (Pure Solid State)
**Created:** 2026-01-27
**Guitar:** ESP Throbber-CTM / Greco TE-500
**Amp:** Roland JC-22 Jazz Chorus (Front Inputs Used)
**Music Style:** Neo-Soul / Post-Rock
**Method:** Front-End Stereo (All effects → Amp Inputs)

---

## Signal Flow Diagram

```
🎸 Guitar Input
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【Mono Dynamics & Drive Section - Buffer++ Loop 1】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↓
① PA-1QG (Always-on EQ)
   Settings: Level +3dB (Mild Boost)
  ↓
② Empress Buffer++ Input
  ↓
┌─────────────────────────────────────────────────┐
│ Buffer++ Loop 1                                 │
│                                                 │
│  ├─ ③ Empress MKII (Compressor)                 │
│  │    Result: Control dynamics before drive     │
│  │                                              │
│  ├─ ④ PRS Horsemeat (Transparent Boost)         │
│  │    Result: Pushing the next gain stage       │
│  │                                              │
│  ├─ ⑤ Roshi Blacklon (Virtual Preamp) ⭐核心     │
│  │    Settings: 6V6 Mode, Mellow                │
│  │    Result: Tube warmth simulation            │
│  │                                              │
│  └─ ⑥ ODL-1-CS (Dumble Drive)                   │
│       Result: High-gain smooth lead tone        │
│                                                 │
└─────────────────────────────────────────────────┘
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【Stereo Modulation & Space - Buffer++ Loop 2】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↓
┌─────────────────────────────────────────────────┐
│ Buffer++ Loop 2 (Stereo Mode)                   │
│                                                 │
│  Input (Mono) → Split to Stereo inside Loop 2?  │
│  ⚠️ Note: Buffer++ Send is Mono.                 │
│  Therefore, we must place Stereo Splitter here. │
│                                                 │
│  [Buffer++ Send 2]                              │
│         ↓                                       │
│  ⑦ Lichtlaerm AASB (Mono In / Mono Out)         │
│         ↓                                       │
│  ⑧ Cornerstone Nucleo (Mono In / Stereo Out)    │
│         ↓                                       │
│  ⑨ Free the Tone FF-1Y (Stereo In / Stereo Out) │
│         ↓                                       │
│  [Buffer++ Return 2 L/R]                        │
│                                                 │
└─────────────────────────────────────────────────┘
  ↓
Buffer++ Output L/R (Stereo)
  ↓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【Final Amplification】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ↓
🎛️ Roland JC-22 Input L (Mono)
🎛️ Roland JC-22 Input R
  ↓
🔊 Stereo Speakers
```

---

## 關鍵設置 (Key Settings)

### 1. Roshi Blacklon (Virtual Preamp)
*   **Role**: 取代實體管機前級，這是此訊號鏈的靈魂。
*   **Mode**: 6V6 (Clean/Edge of Breakup)
*   **Volume**: 必須設定在 Unity Gain 或稍微低一點，以免讓 JC-22 的晶體前級過載 (Hard Clipping)。

### 2. JC-22 Settings
*   **Bright Switch**: **OFF** (避免搭配 Dirt Pedals 時聲音太尖銳)。
*   **Chorus**: **OFF** (避免與 FF-1Y/Nucleo 的調制衝突，保持清晰度)。
*   **Volume**: 根據現場需求，但盡量保持在 3-5 之間以獲得最佳動態。

### 3. Stereo Routing Note
*   由於 Buffer++ 的 Loop send 是 Mono，我們利用 **Cornerstone Nucleo** 作為 "Stereo Splitter"。
*   路徑：Buffer++ Loop 2 Send (Mono) → AASB (Mono) → Nucleo (Mono In -> Stereo Out) → FF-1Y (Stereo) → Buffer++ Loop 2 Return (Stereo)。

---

## 音色特性預期

*   **Attack**: 非常快速、直接 (Solid-State 特性)。
*   **Warmth**: 完全依賴 Blacklon 與 Sweet Honey/ODL-1-CS 的調整。可能需要比平常稍微關小一點 Tone 鈕。
*   **Stereo Image**: 寬大且包覆感強，因為空間系效果直接佔據了左右聲道。
