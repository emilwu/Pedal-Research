# Imperial MKII 耳機訊號鏈：第一版架構分析

**日期**：2026-10-13
**狀態**：active — 使用者實際接起來的訊號鏈（第一版）
**更新**：2026-10-13 凌晨，依使用者回覆更新六點（見文末「2026-10-13 使用者確認」）
**鏈定義**：`signal_chain_2026-10_imperial_headphone.yaml`（同目錄）

## 結論摘要

- **A 音色**：兩個情境大致涵蓋所有目標風格。真正缺的只有 envelope filter、flanger，chorus 只能近似。權重最高的未知是 Cali76 Stacked 能不能細緻到 Jazz（佔 80%）。
- **B 架構**：使用者的順序整體合理。實質問題有兩個：立體聲在進 Imperial 前全部折成單聲道；AASB → FF-1Y 的順序會讓 delay 重複殘響（2026-10-13 起，Chroma 破音殘響、SPACE 疊 AASB 這兩點已依使用者用法排除）。電源需要至少五路獨立大電流輸出。
- **C 吉他**：鏈前兩台都是 buffered，換琴只差在電平，不差在阻抗。Thinline 在耳機鏈裡最容易被聽到交流聲。

**最重要的三個行動**

1. 依 B-7 的電源表決定電源供應器。RAAT 已確認 9V、中心負 [user]，耗流仍未知。Cali76 已確認是現行款（只能 9V、200 mA）[user]。
2. PA-1QG 每把琴存一個 preset，把電平拉近，讓 Cali76 的設定能跨琴共用。踏板 drive 開著時，Imperial 用 Rhythm 聲道當平台。
3. 分配殘響角色：日常殘響交給 Imperial 內建 reverb，AASB 留給 shimmer。要保留 Chroma 與 FF-1Y 的立體聲，可把 7–9 移到 Imperial 的 FX loop（使用者確認 Send／Return 與輸出都是立體聲、走四線法沒問題 [user]，見「可選的調整」第 4 項）。

---

## 訊號鏈總覽

吉他 → 1 → 2 → … → 9 → Imperial MKII 前面輸入（單聲道，1 MΩ）→ 耳機（內建 IR cab sim）。
沒有 router，沒有 FX loop，全部串聯。

| # | 單元 | 角色 | Bypass | 單／立體聲 | 情境 Arca | 情境 RAAT |
|---|---|---|---|---|---|---|
| 1 | Free the Tone PA-1QG | 每把琴的 EQ 與電平 | Buffered（HTS）* | mono | ● | ● |
| 2 | Origin Cali76 Stacked | 主壓縮器 | Buffered [official] | mono | ● | ● |
| 3 | Device2 From Yesterday | BB／KOT V2 系 OD | [unknown] | mono | ● | ● |
| 4 | JHS NOTADÜMBLË V2 | TS 系 Dumble OD ＋ clean boost | [unknown] | mono | ● | ● |
| 5 | Virtues Arca | translucent OD | True bypass [official] | mono | ● | — |
| 6 | Device2 RAAT | RAT 系 distortion | [unknown]，推測 true bypass | mono | — | ● |
| 7 | Lichtlaerm AASB | shimmer／octave reverb | Relay，buffered* | **mono** | ● | ● |
| 8 | Hologram Chroma Console | 多效果 | 三選一，出廠預設 [unknown] | 立體聲機，單聲道使用 | ● | ● |
| 9 | Free the Tone FF-1Y | 主 delay | spec 未寫 | 立體聲機，單聲道使用 | ● | ● |

\* PA-1QG、AASB、FF-1Y、Imperial MKII 的 spec 是舊格式，沒有標證據等級。下文引用時不另加標籤。例外：Imperial MKII 的電源段已於 2026-10-13 依官方手冊改正並加上證據等級。

**兩個情境**：Arca（1–5、7–9）與 RAAT（1–4、6–9）。第 5、6 位永不同時開啟 [user]。

**兩個先釐清的前提**

- AASB 是 **mono in／mono out**（`aasb.yaml`，2026-10-13 使用者確認 [user]）。Imperial spec 的接線範例把它寫成 stereo effect，那是錯的。所以立體聲折疊只影響 Chroma 與 FF-1Y。
- RAAT 的 Ge 是**削波二極體**，在 op-amp 增益級之後，不是 Fuzz Face 那種鍺電晶體輸入級。前面有 buffer 不會讓它變調 [inference]。

---

## A. 是否符合目標音色

### 結論

- 兩個情境共用 clean 平台與空間效果，差別只在第 5／6 位的增益性格。
- Arca 情境偏 Jazz、Neo Soul、Blues、J-Pop。RAAT 情境偏 J-Rock、器樂搖滾重段落、Post Rock 音牆。
- Jazz 是唯一「部分」符合的高權重風格，關鍵在壓縮器。
- 鏈上與庫存都補不了的只有 envelope filter 與 flanger。

### 目標風格的範圍

`music_styles.yaml` 列了 7 種：Jazz（80%）、Neo Soul（70%）、Funk（60%）、Post Rock（40%）、Fusion（30%）、Pop Rock（30%）、Rock（20%）。

Blues 不在這份檔案裡，只出現在吉他與效果器的 `best_for`。因為使用者列為目標，下表另立一列。

`music_styles.yaml` 的 `recommended_equipment` 寫的是舊的 JC-22／Swiss Things 器材。本報告只沿用各風格的 `characteristics`。

J-Rock／J-Pop 與器樂搖滾在本庫沒有定義。以下是**本庫歸納**：

| 風格 | 特徵（本庫歸納） |
|---|---|
| J-Pop | clean 或輕 crunch 分解和弦，壓縮明顯，聲音明亮，中等空間效果，常用 chorus 類調變 |
| J-Rock | crunch 到中高增益刷弦，中頻往前，lead 要延音。一部分接近現代 high gain |
| 器樂搖滾 | clean 與破音段落對比強，點弦、分解和弦要顆粒清楚，tap tempo delay，loop 與質地層 |

### 風格覆蓋

| 風格 | 情境 | 主要單元 | 評等 | 理由 |
|---|---|---|---|---|
| Jazz（80%） | 兩者相同 | PA-1QG、Cali76、Imperial Rhythm、FF-1Y、Imperial reverb | **部分** | clean 平台足夠：Rhythm 聲道 headroom 高，FF-1Y 乾音全類比。問題在壓縮：Cali76 官方宣傳偏重壓縮 [official]，Sound On Sound 也說設計目標是極端壓縮 [independent]；官方另說可做輕度 always-on 動態修飾 [official]，但每級固定 4:1 [official]，細緻程度 [unknown]。AASB 不是 Jazz 要的 room reverb |
| Neo Soul（70%） | 兩者，Arca 多一層 | Cali76、From Yesterday、NOTADÜMBLË、Arca、Chroma、FF-1Y | 充分 | 溫暖 OD 疊加有三到四台。chorus 只能用 Chroma VIBRATO 近似 [inference] |
| Funk（60%） | 兩者相同 | Cali76（官方點名 funk squish）、NOTADÜMBLË clean、Imperial Rhythm | 部分 | 壓縮與 clean boost 充分。缺 envelope filter：Chroma 的 FILTER、HOWL、SWELL 都不是依包絡掃動的濾波器 [official]。壓縮後的 clean boost 交給 NOTADÜMBLË clean（最大提升量 [unknown]，理由見 B-2） |
| Post Rock（40%） | 兩者 | Cali76、AASB（Freeze）、Chroma（SWELL、REVERSE、CAPTURE）、FF-1Y | 充分（限單聲道） | 素材齊全。FF-1Y spec 沒有 HOLD 功能，無限延續改由 AASB Freeze 與 Chroma CAPTURE（最長 30 秒 [official]）負責。立體寬度見 B-5 |
| Fusion（30%） | 兩者相同 | NOTADÜMBLË OD、Cali76、FF-1Y | 充分 | JHS 官方點名 Larry Carlton、Robben Ford 的 violin tone [official] |
| Pop Rock（30%） | 兩者相同 | 3–5 的 OD、Chroma（PHASER、VIBRATO）、FF-1Y | 充分 | 原本列為缺口的 modulation，Chroma 補上了 phaser 與 tremolo [official] |
| Rock（20%） | 兩者 | From Yesterday（BB 系）、NOTADÜMBLË（TS 系）、Arca／RAAT | 充分 | `music_styles.yaml` 要的 Bluesbreaker 與 TS 兩種都有 |
| Blues | 兩者，Arca 較順手 | From Yesterday、Arca、NOTADÜMBLË、Imperial reverb／tremolo | 充分 | 低到中增益 OD 多台可選 |
| J-Pop | 兩者，Arca 較順手 | Cali76、PA-1QG preset、Arca／From Yesterday、Chroma、FF-1Y | 充分 | chorus 是近似；DOUBLER 折成單聲道後能不能用待實測 |
| J-Rock | Arca：crunch 到中增益；RAAT：distortion | Arca、RAAT、NOTADÜMBLË OD 推 RAAT | 主流充分；high gain 分支部分 | Arca 官方增益範圍是 clean 到 classical distortion [official]，示範影片由田渕ひさ子演奏 [official]。鏈上與庫存都沒有專用 high gain 單元 |
| 器樂搖滾 | 兩者，重段落偏 RAAT | Cali76、PA-1QG、NOTADÜMBLË clean、FF-1Y tap、Chroma（PITCH ±1 oct、CAPTURE） | 充分 | 功能對應來自官方功能表 [official]，風格適配是推論 |

Jazz、Funk、Fusion 幾乎只用共用部分，兩個情境沒有差別。

### 缺口與庫存補位

| 缺口 | 鏈上狀況 | 庫存可補 | 影響 |
|---|---|---|---|
| 細緻、透明的壓縮 | Cali76 輕用法細緻度待實測 | **Empress MKII**（`music_styles.yaml` 原本為 Jazz 指定）；Cali76 FET | **最大**。Jazz 佔 80%。見「可選的調整」 |
| Envelope filter | 無 | 無 | 需另購（`music_styles.yaml` 已列為待購） |
| Chorus | Chroma VIBRATO 近似 [inference] | 無 | Neo Soul、Fusion、J-Pop |
| Flanger | 無 | 無 | 低 |
| 自然 room reverb | Imperial 內建（spec：convolution spring）、Chroma SPACE | Nucleo | AASB 不擔任這個角色 |
| 現代 high gain | RAAT ＋ 前面的 OD 疊推 [inference] | 無 | 只影響 J-Rock 一個分支 |

### Imperial ＋ 耳機對各風格族的影響

- **Clean 族**（Jazz、Funk、J-Pop clean、器樂搖滾 clean）：Rhythm 聲道的 headroom 是基礎。原廠 IR 有 1x12 Imperial、2x12 AC30、4x12 G12M-25；clean 族用 1x12 最直接 [inference]。耳機會放大底噪（見 C）。
- **破音族**（Blues、Rock、Pop Rock、Fusion lead、J-Rock）：破音來自 3–6 位，Imperial 用 Rhythm 接收。AASB、Chroma、FF-1Y 都在前級**之前**；若用 Lead 聲道或把前級推到破音，delay 與殘響尾巴會一起破音 [inference]。Lead 聲道的 spec 是「British-voiced（預估）」。RAT 系的 fizz 在耳機裡較明顯，可用 Imperial Editor 的每聲道 Low-Pass Filter 收 [spec]。
- **氛圍族**（Post Rock、器樂搖滾質地層）：立體聲折疊是 Imperial 接法對目標音色最大的妥協。`music_styles.yaml` 的 usage_context 把 stereo 列為可優先考慮的事項。錄音為主（80%），可以在 DAW 用雙軌補寬度。機制見 B-5。

---

## B. 鏈的架構：功能重疊與不建議的搭配

### B-1. 增益級疊加

**最後一級決定質地。** Arca 與 RAAT 都在 drive 區最後，都是 hard clip [dealer／official 批次頁]。疊加時，From Yesterday、NOTADÜMBLË 主要變成推動器與前置 EQ，最後的削波質地由第 5／6 位決定 [inference]。

From Yesterday 的「雙通道」是兩組增益級還是共用增益級只切音量 [unknown]。

**合理的疊法**

| 疊法 | 理由 |
|---|---|
| From Yesterday（Boost 或低增益）→ NOTADÜMBLË OD | BB 系打底、TS 系上色（`overdrive_stacking_theory.md` Principle 1） |
| NOTADÜMBLË Clean ↔ OD（前面板 Order 開關） | 官方明寫：Clean → Drive 是 boost 推 OD；Drive → Clean 是 lead lift [official] |
| 一個 boost → Arca 或 RAAT | 低增益推高增益（Principle 2） |
| Arca 單開進 Imperial Rhythm | Imperial clean 當平台，Arca 提供 edge-of-breakup 與中頻 [inference] |
| RAAT 單開或加一個 boost | RAT 增益範圍已接近 fuzz [dealer，對 RAT 2 的描述]，不需要再疊 OD |

**容易糊或重複的疊法**

| 疊法 | 問題 |
|---|---|
| From Yesterday ＋ NOTADÜMBLË OD ＋ Arca 全在中高增益 | 理論文件列的「all pedals medium-high gain」錯誤：過量、糊、過度壓縮 |
| NOTADÜMBLË OD ＋ Arca 都在中等以上增益 | TS 中頻駝峰加上 Arca 強調的中頻，有遮蔽風險 [inference] |
| 任何 OD 推 RAAT 的 Ge 檔 | Ge 最早削波、最壓縮；再被推會偏 fuzz、底噪更高 [inference] |
| 多級踏板 drive ＋ Imperial Lead | Lead 自己就是一級 overdrive，形成重複增益級。Imperial spec 自己也把 overdrive 踏板列為 not_recommended，除非特殊疊加需求 |
| Cali76 重壓縮 ＋ 多級 drive | 壓縮器拉高底噪與交流聲 [official]，每一級 drive 再放大一次 |

粗略上限：同時開的削波級（含 Imperial Lead）以兩級為宜，第三級只當 boost [inference]。這是起點，不是規則。

### B-2. 壓縮器與 EQ 的位置

**Cali76 在 drive 前：合理。** 官方建議放在鏈最前面，只有 vintage fuzz、wah 要放它前面 [official]。PA-1QG 是 buffered EQ，不屬於官方擔心的類型 [inference]。

副作用：

- 送進 drive 的動態被壓平，OD 對撥弦力度的反應變小 [inference]。Jazz、Neo Soul 要保留觸彈動態時，壓縮量要輕。
- 通電預設為開啟（ON）[official]。沒有 router，每次開機它都是開的。

**PA-1QG 在 Cali76 前：合理，而且是這條鏈的關鍵。**

- `pairing_rules.yaml` 的標準順序是 compressor → EQ。使用者是反過來。
- Cali76 Stacked 是**固定門檻**，輸入越大壓越多 [official]。PA-1QG 每個 preset 有獨立音量 [spec]，可以先把五把琴的電平拉近，Cali76 的反應就不會因換琴大幅改變 [inference]。
- 代價：PA-1QG 的音量提升與頻段增益，在 Cali76 開著時大多變成更多壓縮，不是更大聲 [inference]。所以壓縮之後的 clean boost 交給 NOTADÜMBLË clean 聲道較直接。
- 以五把輸出不同的吉他來看，維持使用者順序比較划算 [inference]。

### B-3. Buffer、bypass 與阻抗

| # | 單元 | Bypass | 阻抗 |
|---|---|---|---|
| 1 | PA-1QG | Buffered（HTS） | 輸入 INST 1 MΩ／LINE 300 kΩ |
| 2 | Cali76 Stacked | Buffered [official] | 輸入 1 MΩ、輸出 1 kΩ [official] |
| 3 | From Yesterday | [unknown] | [unknown] |
| 4 | NOTADÜMBLË V2 | [unknown]；官方 V2 頁沒寫，不可沿用 V1 的 true bypass | [unknown] |
| 5 | Arca | True bypass [official] | [unknown] |
| 6 | RAAT | [unknown]；3PDT 平台推測 true bypass [inference] | [unknown] |
| 7 | AASB | Relay，buffered，spillover 可切 | — |
| 8 | Chroma Console | Buffered／Buffered with trails／True bypass 三選一（全域）[official]；出廠預設 [unknown] | 輸入 1 MΩ、輸出 <1 kΩ [official] |
| 9 | FF-1Y | spec 未寫 | 輸入 ≥500 kΩ |

**結論**

- 第 1、2 位都是 buffered。從第 3 位起，每台看到的都是低輸出阻抗訊號，不論自己是不是 true bypass [inference]。
- 鏈尾有 AASB 與 Chroma（buffered 模式）的 buffer。中段 3–6 位的 bypass 多數未知，但不會造成長線高頻流失 [inference]。
- 鏈上沒有對 buffer 敏感的單元（vintage fuzz、wah），沒有衝突。
- RAAT 真正的順序議題在**輸出**：三種削波門檻差很多，切檔時音量會明顯跳動（Ge 最小、LED 最大）[inference]。下游 7–9 與 Imperial 看到的電平會跟著變。

### B-4. 時間系效果順序：AASB → Chroma → FF-1Y

| 後果 | 說明 |
|---|---|
| FF-1Y 重複的是殘響後的訊號 | 每一下 repeat 都帶 shimmer 尾巴，容易變成一片 wash [inference] |
| Chroma 的 drive 類模組在殘響之後 | ~~會把 AASB 殘響一起破音~~ **2026-10-13 已不成立**：使用者基本不用 Character 模組，破音都交給 Arca、RAAT、NOTADÜMBLË [user]。剩下 Texture 模組的 SQUASH、CASSETTE 若開著仍會壓縮、飽和殘響 [official 功能說明／inference]。AASB 開著時 Chroma 只用 Texture [user]，所以這是刻意的質地處理，不是衝突 |
| ~~Chroma SPACE 疊在 AASB 上~~ | **2026-10-13 已不成立**：AASB 開著時 Chroma 只用 Texture，不開 Diffusion（SPACE 等）[user] |

對 Post Rock 音牆是合理選擇。對要清楚 repeat 的風格容易糊。但 Jazz、Neo Soul 多半不開 AASB，實際衝突只在「AASB 開著、又要清楚 delay」時發生。調整方案見「可選的調整」。

Chroma 內部四個模組的順序可重排、隨 preset 儲存 [official]，不是架構問題。

### B-5. 立體聲效果進單聲道的 Imperial

**會失去什麼**

- 進 Imperial 前面輸入之前，所有立體聲都變單聲道。
- 耳機裡的立體感，只剩 Imperial 自己的 stereo reverb 與 stereo tremolo。
- Chroma：DOUBLER、VIBRATO DRIFT 的寬度消失 [official 效果說明 ＋ inference]。若單一輸出是左右相加，doubler 類的時間差可能產生梳狀濾波 [inference]。
- FF-1Y：PAN 與 RFPM（官方說 Stereo 模式效果最好）變弱或消失 [inference]。

**基準接法**

| 單元 | 接法 | 未知 |
|---|---|---|
| Chroma Console | INPUT L → OUTPUT L | 單進單出官方沒有記載 [unknown]。True bypass 模式時輸出直通「對應的」輸入 [official]，所以同側接法三種模式都有訊號 [inference]。效果開啟時單一輸出拿到左、右或混合 [unknown] |
| FF-1Y | A IN → A OUT | STEREO 模式下只接 A 時聽不聽得到 B [unknown]。SERIES 模式兩單元串在同一路徑 [spec]，單聲道鏈較能用到兩個單元 [inference]；但 SERIES 模式的 PAN 變成 tremolo，只作用於 B |

### B-6. 功能重疊與分工

`music_styles.yaml` 多數風格的 room reverb 原本由 Nucleo 負責，Nucleo 不在這條鏈。所以殘響重疊不全是浪費，而是需要分工。

| 功能 | 提供者 | 判定 | 建議分工 |
|---|---|---|---|
| EQ | PA-1QG；Imperial 3-band；各 drive tone；Chroma TILT／FILTER | 保留 | PA-1QG 管每把琴，Imperial 管音箱 voicing |
| 壓縮 | Cali76；Chroma SWEETEN／SQUASH；Imperial HF Comp | 輕度重疊 | Cali76 為主；Chroma 的壓縮當效果用 |
| Clean boost | PA-1QG 音量；NOTADÜMBLË Clean；From Yesterday Boost 模式；Arca 低 Gain [dealer] | **重疊** | 選一個當主 boost。NOTADÜMBLË Clean 最靈活 [inference] |
| Overdrive | From Yesterday；NOTADÜMBLË OD；Arca；Imperial Lead（Chroma Character 不使用 [user]） | **重疊** | 踏板 drive 開著時 Imperial 用 Rhythm；OD 不要同時開在中高增益 |
| Distortion／fuzz | RAAT（Chroma Character 不使用 [user]） | 無重疊 | — |
| Reverb | AASB；Chroma SPACE；Imperial spring | 輕度重疊 | AASB 與 Chroma SPACE 不會同開 [user]。日常殘響交給 Imperial（推測在前級之後 [inference]，且仍保有立體聲）；AASB 留給 shimmer、drone |
| Delay | FF-1Y；Chroma CASCADE／REELS／REVERSE 等 | 輕度重疊 | FF-1Y 主 delay；Chroma 做 lo-fi、reverse 質地 |
| Tremolo | Imperial；Chroma TREMOLO；FF-1Y PAN（SERIES） | 重疊 | Imperial 的在單聲道鏈裡唯一保有立體聲 |
| Freeze／loop | AASB Freeze；Chroma CAPTURE | 輕度重疊 | 用途不同（pad vs 短 loop），保留 |
| 立體聲 | Chroma；FF-1Y | **衝突** | 見 B-5 與可選的 FX loop |
| 時間系順序 | AASB → Chroma → FF-1Y | **條件式衝突** | 見 B-4 |
| 情境互斥 | Arca／RAAT | 無衝突 | 兩者不同時開，各自決定該情境的削波質地 |

### B-7. 電源

inventory 沒有記錄電源供應器，供電方案未定。

| # | 單元 | 電壓 | 電流 | 證據與備註 |
|---|---|---|---|---|
| 1 | PA-1QG | 9V | 200 mA | spec 寫不建議 daisy chain |
| 2 | Cali76 Stacked | **只能 9V**（內部升壓 24V） | 200 mA，供應器需 >200 mA | [official]；使用者確認是 2025 現行款 [user] |
| 3 | From Yesterday | 9V，中心負 | 6 mA | [independent，僅 RockBoard]；可否 18V [unknown] |
| 4 | NOTADÜMBLË V2 | **9V 上限**，中心負 | 25 mA | [official]；超過 9V 保固失效 |
| 5 | Arca | 9V，中心負 | [unknown]（官方「確認中」） | [official] |
| 6 | RAAT | 9V，中心負 [user] | [unknown] | 2026-10-13 使用者確認電壓與極性；可否 18V [unknown] |
| 7 | AASB | **只能 9V** | 150 mA | |
| 8 | Chroma Console | 9V，中心負 | [unknown] | 供應器至少 500 mA 連續 [official]；這是供應器下限，不是耗電量 |
| 9 | FF-1Y | 9V，中心負 | 350 mA | |
| — | Imperial MKII | **9–12V**，中心負 [official] | 官方未公布 mA；需 ≥ 9W [official]（12V 時 ≥ 750 mA、9V 時 ≥ 1000 mA [inference]） | 附 Universal 12V 變壓器 [official]。2026-10-13 依官方手冊改正，原本寫 9–18V、300 mA（預估） |

- 至少五台需要獨立、隔離、大電流的輸出孔：PA-1QG、Cali76、AASB、Chroma、FF-1Y。一般 100 mA 的孔不夠 [inference]。
- **Imperial 用原廠附的 12V 變壓器** [inference]。它需要至少 9W，一般隔離式效果器電源的單一輸出孔供不起。
- 原廠變壓器**不接地**。官方手冊提醒：只接吉他與耳機時，吉他可能收到較多交流聲 [official]。這正是這條鏈的接法。對策是改用接地的電源，或把 SEND／RETURN／BALANCED OUT／USB 其中一個接到有接地的設備 [official]。
- NOTADÜMBLË V2、Cali76（現行款）、AASB 不可接 18V；Imperial MKII 上限 12V [official]。供應器若有可調電壓的孔，要特別標示。
- 未知值不加總。總電流等 RAAT、Arca、Chroma 確認後再算。

---

## C. 搭配器材庫的吉他

### 前提

阻抗面的分析見 B-3：PA-1QG 用 INST 輸入時，五把琴看到的都是同一個 1 MΩ 負載，後面的 drive 看到的是上游 buffer。**換琴造成的差異主要是輸入電平** [inference]。電平對齊靠 PA-1QG preset，理由見 B-2。

這改寫了知識庫兩條建議：

- Eclipse spec 建議用有 input pad 的 buffer（如 Buffer++）。這條鏈沒有 pad。PA-1QG 的 preset 音量在它的輸入級之後，保護不了 INST 輸入；唯一的退路是 LINE 輸入（300 kΩ、+14 dBu）。但 300 kΩ 會讓被動拾音器失去高頻 [inference]，若這個開關是全域設定，換琴時要記得切回。
- 多份吉他 spec 的「半空心高音量會 feedback」是以音箱喇叭為前提。這條鏈只用耳機，沒有聲學回授。半空心琴在高增益下真正的限制是**交流聲** [inference]。

**噪音**：鏈上沒有 noise gate（Chroma 與 Imperial 的 spec 都查不到）。耳機加 80% 錄音，底噪與交流聲會完整被聽到。Cali76 手冊明說壓縮器會放大單線圈交流聲，單線圈宜輕壓 [official]。

### 五把吉他與鏈的互動

| 吉他 | 拾音器／輸出 | 對 PA-1QG／Cali76 | 對 Arca | 對 RAAT | 噪音 | 建議情境 |
|---|---|---|---|---|---|---|
| **ESP Eclipse CTM/E** | EMG JH-N／JH-B 主動式，high | 輸出最高，Cali76 被推得最深。是否超過 PA-1QG INST 上限 +4 dBu [unknown] | 低增益端就容易開始破 [inference] | EMG＋Cali76＋Ge 是全鏈最壓縮的組合 [inference] | 主動式低噪，最適合高增益進耳機 | **RAAT** |
| **ESP THROBBER-STD**（id：esp_throbber_ctm） | SD APH-1n／TB-APH-1b，medium；5-way，Pos 2、4 為切單 [official] | 標準電平，適合當 gain staging 的參考琴 [inference] | 中頻 PAF 加半空心，適合低中增益 | humbucker 檔各模式可用；切單檔在高增益下有交流聲 | humbucker 檔安靜 | **兩者皆可** |
| **Greco TE-500** | Fralin Wide Range ×2，medium，humbucking | 標準電平 | 最契合。Arca 保留中頻 [dealer]，Wide Range 個性留下 | 可用；Si 高增益可能偏刺，靠 Filter 收 [inference] | 安靜 | **Arca** |
| **Fender Tokyo Thinline** | SD SP90 ×2，P90。inventory 記 medium，spec 記 medium_high，兩檔不一致 | Cali76 會放大 P90 的交流聲 [official 通則] | 很好。P90 中頻與 Arca 取向相合 [inference] | 只建議低增益用法 [inference] | **五把裡最吵**。Cali76＋RAAT 高增益進耳機是最壞情況 | **Arca** |
| **Pearson Omega 6** | Pearson A2，Alnico 2 PAF，官方稱 lower output；兩顆各一個切單 toggle | 實際電平沒有量測；若確實偏低，PA-1QG preset 要補 [inference] | 很好。低輸出 PAF 適合 clean boost 到 low gain 的區間 | humbucker 狀態可用；切單加高增益有交流聲 | humbucker 安靜 [independent] | **Arca 為主** |

### 各琴重點

- **Eclipse**：最適合長時間開 RAAT 高增益錄音。spec 把 Jazz、Blues 列為 not ideal。
- **Throbber**：五把裡最平衡，當全鏈 gain staging 的參考琴。RAAT 情境請停在 humbucker 檔。
- **Greco**：Jazz、Neo Soul、Funk 的主力，Arca 情境首選。
- **Thinline**：P90 的咬勁適合 J-Rock／J-Pop crunch 與 Rock。在無 gate 的耳機鏈裡，高增益會把 hum 一起放大。
- **Omega 6**：尚無使用者彈奏紀錄，以上全是推論。

### 風格適性（全部 [inference]，無實際彈奏紀錄）

◎ 首選　△ 需要遷就（未列出的風格為「可用」）。Blues 併入 Rock。

| 吉他 | ◎ | △ |
|---|---|---|
| Eclipse | Rock／Blues、Post Rock、J-Rock／J-Pop | Jazz、Neo Soul、Funk |
| Throbber | Jazz、Neo Soul、Fusion、Rock／Blues、Post Rock | — |
| Greco | Jazz、Neo Soul、Funk | J-Rock／J-Pop |
| Thinline | Funk、Pop Rock、Rock／Blues、J-Rock／J-Pop、器樂搖滾 | Post Rock（hum） |
| Omega 6 | Neo Soul、Funk、Pop Rock、器樂搖滾 | — |

器樂搖滾多用 clean 到 crunch 的清楚音色，切單與 P90 有優勢。

---

## 可選的調整

以下都不改寫使用者的基準，只在有實質理由時採用。

| # | 調整 | 理由 | 代價 |
|---|---|---|---|
| 1 | **Imperial 以 Rhythm 聲道為主平台**（通道分工，不改順序） | 避免踏板 drive 與 Lead 聲道重複增益；避免時間系效果被前級破音 | Lead 聲道只留給「踏板 drive 全關」或「只開一個 boost 推 Lead」 |
| 2 | **Jazz 錄音時把第 2 位換成 Empress MKII**（僅在實測 Cali76 不夠細緻時） | Jazz 佔 80%；Empress MKII 是 `music_styles.yaml` 原本為 Jazz 指定的透明壓縮 | 換回 Cali76 給 Funk、Post Rock 要重接線 |
| 3a | **時間系改為 Chroma → FF-1Y → AASB** | 符合 `pairing_rules.yaml` 的 modulation → delay → reverb；repeat 乾淨，殘響包住整體 | 失去「delay 重複 shimmer」的音牆 |
| 3b | **只移 AASB：Chroma → AASB → FF-1Y** | Chroma 的 drive／squash 不再破音殘響；仍保留 delay 重複殘響的音牆 | delay 仍在殘響之後 |
| 4 | **把 7–9 移到 Imperial 的 FX loop**（**2026-10-13 使用者確認可行**） | 使用者確認 Imperial 的 Send／Return 與輸出都是立體聲、走四線法沒問題 [user]。Chroma 與 FF-1Y 的立體聲能保留；時間系效果移到前級之後，用 Lead 聲道時尾巴不會被破音 | spec 寫 send 是 mono，與使用者說法不一致；AASB 是 mono，排在 loop 第一台，所以不影響接法。AASB 能否承受 line level spec 沒寫，待實測 |

接法參考（第 4 項）：SEND → AASB → Chroma INPUT L → Chroma OUTPUT L/R → FF-1Y A/B IN → FF-1Y A/B OUT → RETURN L/R。1–6 照舊進前面輸入。

---

## 待實測確認

依影響程度排序。

1. ~~Cali76 實機 DC 孔標示~~ **已確認**：2025 現行款 [user]。
2. ~~RAAT 的電源電壓與極性~~ **已確認**：9V、中心負（內負外正）[user]。
3. **Cali76 最輕的用法對 Jazz 是否夠細緻**，還是要換 Empress MKII。
4. **Chroma INPUT L → OUTPUT L**：效果開啟時輸出是左、右或混合；開關前後音量是否一致；出廠 bypass 模式。
5. **FF-1Y 只接 A IN／A OUT**：STEREO 模式聽不聽得到 B；SERIES 模式從哪個輸出出來。
6. **RAAT 三段開關**哪一位是 Ge／LED／Si、有沒有 Si 的 DIP 子模式、切檔音量跳動多大，會不會讓 Chroma（Calibration 全域、不隨 preset）或 FF-1Y 過載。
7. **Chroma Calibration 全域檔位**在 clean 與 RAAT 兩種電平下用同一檔是否都合適。
8. **ESP Eclipse 進 PA-1QG INST** 是否削波；INST／LINE 開關是全域還是 per-preset。
9. **Thinline 經 Cali76＋RAAT 進耳機的 hum** 是否可接受。不可接受時才評估 noise gate。
10. **所有 OD 都關掉時，Jazz clean 是否被染色**：From Yesterday、NOTADÜMBLË、RAAT 的 bypass 型式未知，Chroma 的 bypass 模式也有影響。
11. **From Yesterday、Arca 的增益上限**夠不夠撐 J-Rock 主力 distortion；Imperial Lead 聲道的實際性格。
12. **Chroma VIBRATO 能不能當 chorus**；DOUBLER 折成單聲道後還能不能用。
13. **NOTADÜMBLË V2** 兩聲道都關時是否 true bypass；Clean 聲道 Input 旋鈕在 buffer 後面還有沒有作用。
14. **AASB** 八度音量最小時能不能當一般 reverb；FF-1Y feedback 最大能不能長時間保持，當 HOLD 用。
15. **Omega 6 與 Throbber 的切單細節**：Omega 6 切單保留哪一顆線圈、stereo 輸出孔接 TS 導線是否正常；Throbber Pos 4 在 RAAT 增益下是否抵消 hum。
16. **Imperial 原廠變壓器不接地造成的交流聲**：只接吉他與耳機時是否明顯。明顯的話，依官方建議改用接地電源，或把 BALANCED OUT／USB 接到有接地的設備。

---

## 本次假設

以下是沒有和使用者確認、由本次分析自行假設的事項。

| 假設 | 依據與影響 |
|---|---|
| ~~Cali76 Stacked 是 2025 年現行款~~ | **2026-10-13 使用者確認，不再是假設** |
| RAAT 使用者原文「LEC」解讀為 LED | 依 `docs/RAAT-Research.md` 與官方文案 |
| RAAT 的批次未知 | 官方頁描述 2026-01 批次（uPC156A、綠色 LED、內部 DIP），不套到使用者這顆 |
| Chroma Console 單進單出（INPUT L → OUTPUT L）可正常使用 | 官方只記載 mono→stereo 與 stereo→mono，沒有 mono→mono |
| Device2 是台灣廠商 | [inference]，官方沒寫 |
| 價格是定價，不是實際購入價 | inventory 已註明多數價格是官方或第三方定價。本報告不做價格結論 |
| ~~AASB 是 mono in／mono out~~ | **2026-10-13 使用者確認，不再是假設** |
| Imperial 內建 reverb／tremolo 在前級之後 | spec 沒寫位置，[inference]。影響「日常殘響交給 Imperial」的建議 |
| Imperial spec 的數值可用 | spec 未標證據等級，耗電、Lead 聲道性格、FX loop 規格都標「預估」 |
| J-Rock／J-Pop、器樂搖滾的特徵 | 本庫歸納，不是使用者提供 |
| Blues 納入目標 | 使用者列為目標，但 `music_styles.yaml` 沒有這一項 |
| `music_styles.yaml` 的器材推薦不採用 | 那是舊的 JC-22／Swiss Things 器材，只沿用各風格的 characteristics |

---

## 資料來源

**效果器 spec**（`shared/equipment_database/pedals/specs/`）

- `pa1qg.yaml`
- `origin_cali76_stacked.yaml`
- `from_yesterday_kot.yaml`（內容為 Device2 From Yesterday）
- `jhs_notadumble_v2.yaml`
- `virtues_arca.yaml`
- `device2_raat.yaml`，另參考使用者研究 `docs/RAAT-Research.md`
- `aasb.yaml`
- `hologram_chroma_console.yaml`
- `ff1y.yaml`

**音箱 spec**

- `shared/equipment_database/amps/specs/tone_king_imperial_mkii.yaml`

**吉他**

- `projects/2025-v3-signal-chain/inventory/guitars.yaml`
- `shared/equipment_database/guitars/specs/`：`esp_eclipse_ctm.yaml`、`esp_throbber_ctm.yaml`、`greco_te500.yaml`、`fender_tokyo_thinline.yaml`、`pearson_omega_6.yaml`

**專案與知識庫**

- `projects/2025-v3-signal-chain/inventory/pedals.yaml`（`active_signal_chain`）
- `projects/2025-v3-signal-chain/music_styles.yaml`
- `.claude/knowledge/pairing_rules.yaml`
- `.claude/knowledge/signal_chain_fundamentals.md`
- `shared/tone_theory/overdrive_stacking_theory.md`
- `shared/tone_theory/compression_theory_and_application.md`

---

## 2026-10-13 使用者確認

使用者在 2026-10-13 凌晨回覆，以下六點已寫進本報告與相關 spec：

| # | 使用者回覆 | 影響 |
|---|---|---|
| 1 | Cali76 是 2025 年現行款 | 電源：只能 9V、200 mA。「待實測確認」第 1 條與對應假設刪除 |
| 2 | AASB 是單聲道 | 確認立體聲折疊只影響 Chroma 與 FF-1Y |
| 3 | Imperial MKII 輸入單聲道，Send／Return 與輸出是立體聲，走四線法沒問題 | 「可選的調整」第 4 項（7–9 移到 FX loop）可行。spec 寫 send 是 mono，與此不一致，以使用者為準並在 spec 註記 |
| 4 | Chroma Console 的 Character 模組基本不用；破音交給 Arca、RAAT、NOTADÜMBLË | B-4「Chroma drive 類模組破音殘響」與 B-6 的 overdrive／fuzz 重疊不再成立 |
| 5 | AASB 疊 Chroma 時，Chroma 只用 Texture。單用 Chroma（不開 AASB）時才可能用 Movement、Diffusion、Texture 三個模組；Character 一律不用 | B-4「SPACE 疊 AASB」不再成立；B-6 reverb 重疊降為輕度。B-4 剩下的實質問題只有 FF-1Y 重複殘響 |
| 6 | RAAT 電源是 9V、內負外正（中心負） | B-7 電源表與「待實測確認」第 2 條已更新 |

