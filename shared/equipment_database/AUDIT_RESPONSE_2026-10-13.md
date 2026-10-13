# 回應網站逐欄對照報告（2026-10-13）

**對象**：Planning `scripts/migrations/equipment-data/AUDIT-2026-10-13.md`（commit `e10a752`）第二節與第三節
**Research 基準**：本檔所在 commit（spec 修改與本檔同一個 commit）
**做法**：每台設備 1 個 agent 依規則處置，再由 1 個 agent 嘗試推翻（只做一輪）。資料檔的值一律不算證據。

## 給 Website 的執行方式

| 處置 | 件數 | Website 要做什麼 |
|---|---|---|
| **刪除** | 170 | 從 `equipment.json` 移除該值。說明欄寫「只刪某子句」的，只刪那一段，其餘保留 |
| 保留 | 20 | 不用動。spec 本來就支持 |
| 已補進 spec | 23 | 不用動資料檔的值。spec 已補上並附官方來源 |
| 已修正 spec | 1 | 不用動。過期的是 spec，已修正 |

做完後重跑 006。**所有 spec 的 `basic_info.brand`／`model`／`id` 都沒有改，不需要新增 `previousKeys`。**

使用者裁定：`suggestedSettings` 與 `suitableStyles` 一律刪除（Research 不收旋鈕刻度與風格標籤，與 Fumble、DS-1 的前例一致）。

## 第二節：Colosseum 的 Clip Blender 方向

`cornerstone_colosseum.yaml` 的兩處 Clip Blender 描述已改成：

> 逆時針轉到底（面板左側 Ge 標示）＝純 Germanium（原版 Klon 1N34A）；順時針轉到底（面板右側 Si 標示）＝純 Silicon；中間連續混合 [official]

證據等級：[official]。來源：https://www.cornerstonemusicgear.com/wp-content/uploads/2026/02/cs_colosseum-manuali.pdf（Cornerstone 官方產品頁連結的手冊，第 1 頁面板圖與實機照片，CLIP 旋鈕左側印 Ge、右側印 Si）。
網站可以照這個寫法改 `specs.controls.7.function`，刪掉「研究庫兩端記載自相矛盾」的警告。

## 第三節：214 項處置

### #0 The Dumblifier（`dsm_dumblifier.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `specs.reviewSummary.cons` | **刪除** | 官方頁面沒有提到電池；只有經銷商 Thomann 寫「不支援電池」，屬 [dealer]，不符合 add_to_spec 的條件。spec 的 potential_concerns 也沒有這一項 |
| `specs.midi` | **刪除** | 填欄位用的布林值：官方頁面和 gearnews 都沒提 MIDI。spec 沒寫不等於 false |
| `specs.cabinetSimulation.hasIR` | **刪除** | 填欄位用的布林值：官方頁面只寫 analog amplifier modeling，沒有明說 cab sim 是不是 IR。spec 沒寫不等於 false |
| `specs.ampType` | 保留 | 由 spec 的 basic_info.subtype zero_watt_power_amp 和「Full analog amplifier modeling」直接推得 |
| `suggestedSettings.0.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.3.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suitableStyles` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.reviewSummary.earlyReception.2` | **刪除** | 本次抓取的 gearnews.com 文章沒有「contender for 2026 pedal of the year」這句，所以「（gearnews.com）」這個出處標註不成立。網站應刪除這個出處（spec 原本那句沒有標出處，沿用即可） |
| `specs.wattageNote` | 保留 | Zero Watt、全類比放大器建模、Power Amp 模擬都寫在 spec 的 features／special_features；「沒有功率輸出、沒有喇叭」是 Zero Watt 踏板設計的直接推論 |

### #1 JC-22（`roland_jc22.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `specs.guitarPairing.excellent.0` | 已修正 spec | spec 舊稱 Throbber-CTM 已改為 THROBBER-STD（HANDOFF 記載 2026-09-12 使用者確認實機型號，標 [user]）；只改 guitar_pairing.excellent 這一條，id 與其他散文未動 |
| `specs.midi` | **刪除** | 官方規格頁沒有寫「無 MIDI」，spec 沒寫不等於 false，屬於填欄位用的值　驗證補充：值是 false，是 schema 補空用的。本次重新抓的 Roland 官方規格頁沒提到 MIDI，spec 也沒有。spec 沒寫不等於 false。 |
| `specs.cabinetSimulation` | **刪除** | 官方沒有說明 cabinet simulation／IR，hasIR:false 是填欄位用的值，沒有來源　驗證補充：{hasIR:false, irCount:null} 是 schema 補空用的。官方規格頁和 spec 都沒提到 cab sim／IR。 |
| `specs.channelNames` | **刪除** | 官方與 spec 都只寫單一 channel，沒有把它命名為「Clean」　驗證補充：spec 只寫 channels: 1 和 "Single channel"。官方規格頁沒有替這個 channel 命名，"Clean" 是捏造的。 |
| `specs.powerRequirements` | 已補進 spec | Roland 官方規格頁寫 AC IN jack 與 Power Consumption 43 W，已在 spec 新增 power_supply 欄位，標 [official]，並把規格頁加入 sources（來源：https://www.roland.com/us/products/jc-22/specs/） |
| `description` | **刪除** | 刪除「Sag」一詞（「補上管機的 Sag 與溫暖度」改為只講溫暖度）；Blacklon 官方建議用於 JC 系列、增加 tube warmth 有 spec 依據，可保留　驗證補充：只刪「Sag」這段（「補上管機的 Sag」）。spec 支持「Blacklon 官方建議用於 JC 系列音箱」和 tube warmth／管機感，但沒有任何地方提到 Sag。 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除　驗證補充：使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.reviewSummary.conclusion` | **刪除** | （驗證推翻原判 keep）只刪第一句「Jazz、Neo Soul、Funk 的 Clean 音色標準」。spec 只說 JC-22 在 best_for.excellent 裡列了 Jazz／Neo Soul／Funk。「標準」這個說法 spec 只用在 JC-120 上（history.legacy：「JC-120 是 jazz/funk 音箱標準」），而且那句沒提 Neo Soul。第二句「真正透明的 Clean Platform，讓效果器完整發揮」有 spec 支撐（character: transparent；pedal_pairing.philosophy: pedal platform），網站可以保留。 |

### #2 Imperial Tri-tube Preamp（`tone_king_imperial_mkii.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除子句「一般前級只有前級音色，它連功率管段的壓縮與 sag 都有」：官方只說 0 watt poweramp（phase inverter 電路）提供 poweramp 段的 harmonic and dynamic content；沒有功率管、官方從未提 sag，唯一的 compression 是軟體 HF Comp 濾波；「一般前級只有前級音色」的比較說法也沒有來源 |
| `specs.powerRequirements` | **刪除** | 「真空管需要高電壓」有依據（官方手冊：3 x 12AX7 running at proper high voltages，spec 的 tubes.note 已有），但「不支援電池」官方未提，未提不等於不支援；另待追蹤：手冊寫附 Universal 12V Power Supply，spec 卻寫 9-18V DC（預估），本次未改 |
| `suggestedSettings.0.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.3.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #3 Eclipse CTM/E（`esp_eclipse_ctm.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除子句「在高增益下不會有 60Hz Hum」：spec 只有 noise_level「Very low (active pickups 低噪音)」，沒有任何來源支持「不會有 60Hz Hum」這種絕對說法；前半句「主動電路的噪音極低」有 spec 支持，可以保留 |
| `specs.reviewSummary` | **刪除** | spec 沒有 review_summary，也沒有任何評測來源；整個 pros/cons/conclusion 物件都是舊自動生成的內容，沒有證據支持 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.0.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #4 THROBBER-STD（`esp_throbber_ctm.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.reviewSummary.pros` | **刪除** | 「半空心比實心輕、較不疲勞」：spec 與官方規格表都沒有重量資料，無依據 |
| `specs.reviewSummary.pros` | **刪除** | spec 的 best_for 只列整體風格，沒有「頸位→Jazz/Neo Soul、橋位→Blues/Funk、混合位→Indie/Classic Rock」的檔位對應，此對應無依據 |
| `specs.reviewSummary.pros` | **刪除** | 「增加共鳴與延音」有 spec 支持（special_features.effect）；刪除子句「同時保持清晰度」，spec 無此說法 |
| `specs.pickups.configuration` | 保留 | spec 的 neck 與 bridge 都是 passive_humbucker（官方 PICKUPS 欄 APH-1n／TB-APH-1b），HH 為直接推導 |
| `suggestedSettings.1.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.reviewSummary.pros` | **刪除** | Vintage PAF、溫暖、諧波豐富、Alnico II 皆有 spec 支持；刪除「甜美」一詞，spec 只寫 Smooth，無此說法 |

### #5 Made in Japan Flagship Tokyo Editions Telecaster Thinline（`fender_tokyo_thinline.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `priceReference` | **刪除** | spec 的 price.msrp 是 null，「預估 $1500-2000」只是 YAML 註解裡的佔位文字，不是有出處的價格；本輪沒有查官方定價，整個值刪除 |
| `specs.reviewSummary.pros` | **刪除** | 「Made in Japan Flagship 系列品質極高，Tokyo Editions 限定」：刪掉「Tokyo Editions 限定」，spec 沒有任何地方說它是限定款；前半句「品質極高」在 notes.mij_quality 有，可以留 |
| `specs.reviewSummary.pros` | **刪除** | 「音色多樣：…混合位獨特 Quack」：刪掉「混合位獨特 Quack」，spec 沒有 Quack 的說法；「橋位 P90 咬合感」「頸位溫暖厚實」在 pickups.bridge／neck.characteristics 有，可以留 |
| `specs.reviewSummary.pros` | **刪除** | 「半空心 thinline 輕量、共鳴豐富、f-hole 增加空氣感」：刪掉「輕量」，spec 沒有重量資料；共鳴（resonance: High）與 f-hole 的空氣感（body.special_features）有依據，可以留 |
| `specs.reviewSummary.cons` | 保留 | 由 spec 直接推得：tonal_characteristics.twang 是 Moderate（P90 比傳統 Tele 溫暖），frequency.mid 是 Thick, pronounced midrange |
| `specs.reviewSummary` | 保留 | 保留整個區塊。這次沒被列出的 pros／cons／conclusion 都對得到 spec 欄位：60Hz hum 在 notes.p90_pickups，feedback 在 pedal_pairing.special_notes，敏感度在 dynamics，風格清單在 best_for.excellent，Bluesbreaker 在 overdrive.notes。被列出的子句依各自那一列刪除 |
| `suggestedSettings.0.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.3.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.reviewSummary.cons` | **刪除** | 「半空心結構較脆弱，對溫濕度敏感」：刪掉「溫」。spec 只講濕度，而且濕度敏感是記在 Ash 琴身底下（notes.maintenance），不是半空心結構；「Semi-hollow 結構較脆弱」有依據，可以留 |
| `specs.reviewSummary.cons` | **刪除** | 「Medium-high 輸出仍不如 Humbucker，不適合 Heavy Metal」：刪掉「仍不如 Humbucker」。spec 沒有拿 humbucker 比過，而且本庫 Throbber 的 humbucker 輸出記為 medium，比這把的 medium_high 還低，研究庫自己的資料就和這句矛盾；輸出等級與不適合 Heavy Metal 有依據，可以留 |
| `suggestedSettings.0.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #6 Spacey Sounds TE-500（`greco_te500.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除「Spacey Sounds 是 Greco 當時的高階產品線」：spec 只記 series 名稱，原廠目錄的 ¥50,000 是定價不是產品線定位；Greco 無官方網站可查證 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.reviewSummary` | **刪除** | 區塊內三條無 spec 依據須刪：「音色多樣：頸位 Jazz/Neo Soul、橋位 Funk/Country/Blues、混合位 Indie/Vintage」（spec 無各檔位風格對應，positions 為 null）；「Maple 指板對溫濕度敏感」（spec 只說 Ash 琴身對濕度敏感、Maple 指板需定期清潔）；「多項規格為推測（品絲材質、琴枕材質…）」（品絲／琴枕材質在 spec 是未知 null，不是推測）。其餘 pros/cons/conclusion 為 notes、tonal_characteristics、chain_1 的轉述 |
| `specs.pickups.type` | 保留 | 兩顆拾音器皆為 passive_widerange_humbucker，pickup_set 標明改裝、notes.modification 寫已改裝；wide_range、HH（Wide Range）、modified: true 皆為直接推導 |
| `description` | **刪除** | 刪除子句「同時具備雙線圈的靜音特性」：spec 未記載；Fralin 官方頁本次抓取被擋（403），無法查證。前半「輸出比單線圈高一些但仍保有清晰度」有 spec 依據可保留 |
| `specs.reviewSummary.cons` | **刪除** | 刪除「原廠拾音器型號未知」部分：spec 的 pickup_selector 依 1976／1979 原廠目錄記載原廠為ワイドレインジマイク／PU-103，資料檔自己的 originalPickups 欄也這樣寫；真正未知的是本琴年份與原裝件下落。「改裝日期未知」有 modification_date: null 依據可保留 |

### #7 Omega 6 Standard（`pearson_omega_6.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `specs.reviewSummary.pros.0` | **刪除** | 開放式骨架與從縫隙看得到配線有 spec 支持（body.construction），但「市面罕見的結構」沒有依據，刪這一句 |
| `specs.reviewSummary.pros.1` | **刪除** | 2.5 kg 有 spec 支持（[official]），但「對 24 格無頭琴而言輕」這個評價 spec 沒有，刪這一句 |
| `specs.reviewSummary.conclusion` | **刪除** | 「紐西蘭手工」有誤導：spec 寫琴頸在中國製造、多數五金來自中國，只有組裝在紐西蘭；「極有特色」也沒有依據 |
| `suggestedSettings.0.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.3.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `description` | 保留 | spec 的 notes.qc_reports 記有「評測琴（多為 Pearson 提供）則回報出廠調整良好」[independent]，網站的值是忠實轉述 |
| `specs.reviewSummary.pros.5` | **刪除** | pot 軸徑、拾音器螺距與螺紋、弦距三項都有官方數字，但「完整」與 spec 矛盾（可用深度 [unknown]、output jack 用途 [unknown]），要刪掉「完整」 |
| `specs.reviewSummary.cons.7` | **刪除** | 「不像木頭琴那樣有木質感」有 spec 支持（core_tone [independent]），但 spec 沒有記錄有人反對這個觀察，「見仁見智」沒有依據，刪這一句 |

### #8 DS-1 Distortion（`boss_ds1.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `specs.reviewSummary.pros.5` | **刪除** | 刪除子句「零件與維修資源充足」：官方與 spec 都沒有提到零件或維修。前半「1978 年至今持續生產」有支持：BOSS 文章寫「has remained in the lineup ever since」，已補進 spec 的 production_note　驗證補充：Delete only the clause「零件與維修資源充足」. I re-fetched the BOSS article (articles.boss.info/all-about-the-ds-1-the-benchmark-boss-distortion/) in this run and it says nothing about parts or repair. 「1978 年至今持續生產」 is supported by spec release_year 1978 [official], status in_production [official], and the article's 'has remained in the lineup ever since', so that part can stay. |
| `specs.reviewSummary.conclusion` | **刪除** | 刪除子句「也是 hard-clipping distortion 的基準款」：BOSS 說的是「benchmark BOSS distortion」，指自家的基準失真，不是整個 hard-clipping 類別；其餘內容（BOSS 第一顆失真、現行生產、適用曲風）spec 都有支持　驗證補充：Delete only the clause「也是 hard-clipping distortion 的基準款」. 'Benchmark' appears only in the article title 'The Benchmark BOSS Distortion' and nowhere in the body, and it does not claim to be the benchmark for the whole category. The rest is supported by the spec and can stay: 「BOSS 的第一顆失真踏板」 (basic_info.type [official] 'BOSS's first distortion pedal'), 「現行生產中」 (status in_production), and the genres Rock／Punk／Grunge／Hard Rock／Fusion Lead (usage_recommendations.best_for). |
| `specs.reviewSummary.cons.1` | **刪除** | 刪除子句「或 EQ 補償」：官方只建議選中頻突出的音箱，或搭 blackface 時用 Normal 輸入／關 bright，沒有提 EQ；「中低頻輕微凹陷、靠音箱選擇補償」spec 有支持　驗證補充：Delete only the clause「或 EQ 補償」. 「中低頻有輕微凹陷，需要靠音箱選擇」 is supported by tonal_characteristics.official_description [official], which says BOSS recommends mid-forward amps such as Marshall or Fender tweed. The re-fetched article confirms 'slight dip in the lower midrange… amps that have a prominent midrange presence'. Neither the spec nor BOSS suggests fixing it with EQ. |

### #9 Colosseum（`cornerstone_colosseum.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `suitableStyles` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `description` | **刪除** | 刪「以社群投票決定設計方向的方式」：官方產品頁與手冊只寫 designed with direct input from the community，沒有投票（polls 只見於經銷商文案）。「第一顆社群 Overdrive」已依官方產品頁標題補進 spec basic_info.community_design [official]，可保留 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `description` | **刪除** | 刪「溫暖飽滿、適合 Lead」與「清晰透明、適合 Rhythm」兩個子句：官方只說 toggle 切換兩通道順序，沒有描述各順序的音色或用途。其餘內容 spec order_toggle 已有 |
| `description` | **刪除** | 刪「涵蓋從經典到現代的範圍」：官方寫法是 classic Klon sound 到 a fresh new flavor／full Germanium 到 full Silicon，沒有「現代」；官方原文已補進 spec clip_blender.blend.official_wording，可據此改寫 |
| `description` | 已補進 spec | 官方產品頁與手冊都寫每一側可各自接入 looper，或在兩側之間插入其他效果器；已把 special_features 與 usage_recommendations.integration 改成這個寫法並標 [official]（來源：https://www.cornerstonemusicgear.com/colosseum） |
| `specs.features.5` | 已補進 spec | 證據同上一項（產品頁 Four rear jacks ... each side independently ... insert other pedals in between；手冊同義），spec 已補並標 [official]（來源：https://www.cornerstonemusicgear.com/colosseum） |

### #10 Nucleo（`nucleo.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `specs.bypass` | **刪除** | 官方說明書寫的是 True Bypass（僅 mono 路由、無尾音）／Buffered Bypass（保留尾音）兩種可選，bypass 乾訊號 analog 或 digital 視 Dry Mode 而定；「數位 Bypass」與事實不符。已把官方寫法補進 spec 的 technical_specs.bypass，網站應改用 spec 的值（來源：https://www.cornerstonemusicgear.com/wp-content/uploads/2026/02/NUCLEO-MANUAL-V4.pdf） |
| `specs.tonalCharacteristics.dynamics` | **刪除** | 「動態透明」沒有來源；MOD／FLUX 的描述在 special_features 有，但放在 dynamics 欄位不恰當，整句刪除 |
| `specs.tonalCharacteristics.frequency.low` | **刪除** | spec 只寫 Reactor「巨大、膨脹的聲音」，「低頻支撐」是從這句推出來的，沒有來源 |
| `specs.tonalCharacteristics.frequency.mid` | **刪除** | 「不刻意染色」沒有來源，中頻特性 spec 與官方說明書都沒提 |
| `description` | **刪除** | 刪除「耗資十億歐元建造卻從未啟用的 1970 年代電廠」這段（官方說明書與 spec 都沒有）；Paul 在 Zwentendorf 彈奏、殘響取材自該空間的部分有官方說明書與 spec 的 inspiration／IR 依據，可以保留 |
| `description` | **刪除** | Paul Davids「感覺它在你周圍」這句引言，spec 與官方說明書都沒有，整句刪除 |
| `description` | 保留 | spec 的 connectivity.right_output 已寫 Transformer-Isolated、避免 Ground Loop；官方說明書也寫明是兩台以上音箱時常見的問題 |
| `suggestedSettings.0.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suitableStyles` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `description` | **刪除** | 刪除「建構和聲進行」與「從單純的殘響變成音景設計工具」這兩段（官方只說 Freeze Pitch 可設定 harmonization 區段）；Freeze-Pitch 改凍結音高、MOD／AIR／FLUX 的描述有 spec 依據，可以保留 |
| `specs.tonalCharacteristics.frequency.high` | 已補進 spec | AIR Shimmer 高八度 spec 原本就有；TONE 逆時針較暗、順時針較亮已依官方說明書 p.15 補進 controls TONE/DIFF 的 note，標 [official]（來源：https://www.cornerstonemusicgear.com/wp-content/uploads/2026/02/NUCLEO-MANUAL-V4.pdf） |
| `suggestedSettings.3.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #13 Soul Food（`ehx_soul_food.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除「它的誕生原因很直接：當 Klon Centaur 二手價飆到兩三千美金時，EHX 委託團隊做一顆平價替代品」這段起源敘事：spec 只記載「平價版 Klon」與 Klon 二手價 $2000-3000+，沒有記載誕生原因或「EHX 委託團隊」，兩者的因果關係與委託都沒有來源 |
| `suggestedSettings.0.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.3.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.0.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #14 Buffer++（`empress_buffer_plus_plus.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `specs.impedance.output` | **刪除** | 「Out 2 Transformer 隔離」spec 已有，但「低阻抗」無據：官方手冊 rev04 規格表與產品頁都沒有公布輸出阻抗，這個欄位本身沒有可支撐的值　驗證補充：資料檔值「低阻抗；Out 2 為 Transformer 隔離」。Out 2 transformer 隔離有 spec 支撐（outputs.features、panel_layout），但「低阻抗」在官方手冊 rev04 規格表與產品頁規格欄都沒有（spec 新增的 note 也把輸出阻抗記為 [unknown]）。依預設規則刪除「低阻抗」這一段；transformer 隔離那一段可以留 |
| `specs.bypass` | 保留 | spec technical_specs.type「All-analog buffer」與 signal_path「pristine transparent buffering」直接支撐；本機即 buffer，無 true bypass 路徑 |
| `specs.tonalCharacteristics.frequency.low` | 已補進 spec | 官方規格 Frequency Response 20Hz–20kHz，手冊另寫 1MΩ 時 full frequency range pass untouched；已以 [official] 補入 technical_specs.frequency_response（來源：https://empresseffects.com/cdn/shop/files/BUPP_User_Manual_rev04_Web.pdf） |
| `specs.tonalCharacteristics.frequency.mid` | 已補進 spec | 同上，官方 20Hz–20kHz 頻響涵蓋中頻；in 1 loading 只影響高頻。已以 [official] 補入 spec（來源：https://empresseffects.com/products/buffer-plus-plus） |
| `specs.reviewSummary.conclusion` | 保留 | spec best_for.excellent 列有「複雜訊號鏈」「Stereo pedalboards」，屬忠實轉述；「首選」為輕度修辭，影響低 |
| `suggestedSettings.0.knobs.noise filter 1` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.0.knobs.boost` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1.knobs` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.knobs.noise filter 2` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.knobs.out 2 polarity` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suitableStyles` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.0.knobs.fsw function` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.3` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `description` | **刪除** | 刪「涵蓋從單迴路到雙吉他共享效果的所有配置」：「所有配置」無據，官方手冊只說 12 modes support nearly any setup；「12 種路由模式」本身可留　驗證補充：「12 種路由模式涵蓋從單迴路到雙吉他共享效果的所有配置」：spec 確實列出 12 種 mode，但從沒說過涵蓋「所有配置」。依預設規則刪除「所有配置」這個說法（12 種路由模式本身有 spec 支撐） |

### #15 Guitar Compressor MKII（`empress_mkii.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除「即使在高壓縮設定下也不會有呼吸聲或機械感」整句：spec 只寫極度透明、安靜無雜訊，沒有提到高壓縮下的呼吸聲／機械感；官方頁（empresseffects.com/products/compressor-mkii）只說 sidechain 開關可以避免低頻造成的 pumping，沒有支持「高壓縮也不會有呼吸聲」的說法 |
| `suggestedSettings.1.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #16 FF-1Y FUTURE FACTORY（`ff1y.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `specs.bypass` | **刪除** | 官方產品頁與手冊 Ver 1.3 都沒寫 bypass 型態（buffered／true bypass），只說 HTS 電路讓效果開關時音質一致（spec 已有）；「Buffered」是推論，要刪掉 |
| `description` | **刪除** | 要刪的是「旗艦」這兩個字：官方頁沒有這種說法。「日本 Free the Tone 的雙延遲」本身有 spec 支持 |
| `description` | 已補進 spec | 官方頁有 LFO 依固定週期規律變化、RFPM 相位隨機變化的對比原文，已補進 spec 的 vs_lfo；但「所以聽起來自然而不機械」這句官方沒寫，網站要刪掉（來源：https://www.freethetone.com/en/products/detail43/） |
| `description` | **刪除** | 要刪的是「可用來模擬磁帶回音」：官方只說聲音近似 vintage devices，沒提 tape echo。添加諧波、溫暖類比感這兩點 spec 有 |
| `description` | **刪除** | 要刪的是「讓它足以撐起複雜的現場切換」：這是推論。128 個預設、MIDI、Tap Tempo 這幾項事實可以留 |
| `description` | **刪除** | 整句刪掉：spec 沒有這份評測來源，review_summary.conclusion 的說法也不一樣 |
| `suggestedSettings.0` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.3` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `description` | **刪除** | 要刪的是「會呼吸的飄移感」：這是修飾語。32-bit DSP 高保真、有機的空間感有 spec 支持，可以改用 spec 原本的說法 |

### #17 ODL-1-CS Overdrive（`odl1cs.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | 已補進 spec | 官方 ODL-1A-CS 頁原文：二十年以上 maintaining and repairing Dumble、本人擁有多台 Dumble（列出 Overdrive Special 50W 與 Overdrive Reverb），已以 [official] 補入 basic_info.designer_background；網站「調校」應改為「維護」以貼合原文（來源：https://www.freethetone.com/en/products/detail77/） |
| `specs.reviewSummary.cons` | **刪除** | spec 沒有 cons 鍵；Buffered Bypass 與數值範圍未公布雖是 spec 內的事實，但「價格高昂」「需要適應 Dumble 音色特性」沒有出處，整份缺點清單是生成內容　驗證補充：spec review_summary 沒有 cons 欄位。四項中「Buffered Bypass」（technical_specs.bypass）與「七個控制未公布數值範圍」（undocumented）在 spec 有依據，但「需要適應 Dumble 音色特性」沒有出處，「價格高昂」只是評價。這是低影響的判斷項，所以整欄刪除。 |
| `specs.reviewSummary.conclusion` | **刪除** | 「Fusion 與高階 Blues 的 Dumble 音色終極選擇」是沒有出處的評論結論，spec 沒有對應內容　驗證補充：spec 沒有 conclusion 欄位；「Dumble 音色終極選擇」是修飾用語，沒有出處。 |
| `specs.tonalCharacteristics.frequency.mid` | **刪除** | spec 的 frequency 沒有中頻描述；「中頻厚實與諧波堆疊」沒有官方或其他來源　驗證補充：spec 的 frequency 只有 adjustable／rock_mode／jazz_mode 三項，沒有任何中頻的描述；「中頻厚實與諧波堆疊」沒有出處。 |
| `specs.relatedModels.odl1aCs` | 已補進 spec | 官方產品頁明列 DC9V 120mA 且不支援電池，channel control terminal 也與 spec 相符；已在 related_models.odl_1a_cs.current 以 [official] 補入，並把網址加進 sources（來源：https://www.freethetone.com/en/products/detail77/） |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除　驗證補充：使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suitableStyles` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除　驗證補充：使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #18 PA-1QG Programmable Analog 10 Band EQ（`pa1qg.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | 已補進 spec | 「十年以上研發」spec 已有 development_time；「2018 NAMM 發表」經官方 News 頁確認，已加 basic_info.debut [official] 並列入 sources（來源：https://freethetone.com/en/article/news_copy.html） |
| `description` | **刪除** | 官方只確認創辦人為 Yukihiro Hayashi，未找到官方說明他是 PA-1QG 或 ODL-1-CS 的設計者；整句刪除 |
| `description` | **刪除** | 「被評測稱為當時市場上最好的踏板格式 EQ」是評測評語，spec 沒有、本次也未查證出處，刪除 |
| `description` | **刪除** | 評測形容句（閃亮感、飽滿中頻、品質極為出色）屬評語修飾，spec 沒有對應內容，刪除 |
| `specs.tonalCharacteristics.dynamics` | **刪除** | 預設音量 0-127、unity 100、最大 +12dB 與 Clean Boost 都有 spec 依據，但「不壓縮動態」spec 沒有、官方也沒說；刪除「不壓縮動態」這個子句 |
| `specs.tonalCharacteristics.frequency` | 保留 | 十個頻段與 spec frequency_bands 完全一致；分組描述是由頻段直接推得的一般說法，加上 spec 的「針對吉他音域特別優化」 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suitableStyles` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #21 Morning Glory V3（`morning_glory.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除「由創辦人 Josh Scott 設計，是他的旗艦踏板，多年來從未離開過他自己的 Pedalboard」整句：spec 只有 Josh Scott 引言，官方頁面（V4）也沒有旗艦或從未離板的說法 |
| `description` | 已補進 spec | 官方網站頁尾寫「Guitar Pedals made in Kansas City, USA」，已在 spec 加上 basic_info.brand_origin [official]，並把網址加進 sources（來源：https://jhspedals.info/products/morning-glory） |
| `description` | **刪除** | 刪除「與 P90」這段：spec 的 bright_cut.left_off.best_for 只寫 Humbucker，官方頁面也沒提到 P90；「關閉保留完整高頻（適合雙線圈）」有 spec 支持，可以保留 |
| `description` | **刪除** | 刪除「它在 Praise & Worship 社群中也極受歡迎」整句：spec 沒有寫，官方頁面也沒有 |
| `description` | **刪除** | 刪除「沒有 Buffered 選項，也不支援電池」這兩段：spec 只寫了 True Bypass 和 9V DC，官方頁面只寫 9V DC center negative 與 43mA，沒有否定電池或 buffer，spec 沒寫不等於沒有 |
| `specs.reviewSummary.cons` | **刪除** | spec 的 review_summary 沒有 cons。「不適合 High-Gain 或 Metal」「無 Buffered 選項」沒有來源；只有「低至中等 Gain」「Bright Cut 只有兩段」可以從 spec 推出來，但整個陣列不是 spec 內容，所以整欄刪除 |
| `specs.reviewSummary.conclusion` | **刪除** | 「Bluesbreaker 標竿」是加油添醋的評語，spec 只有 Josh Scott 引言，沒有結論 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suitableStyles.4` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #23 As Above So Below Shimmer Reverb（`aasb.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | 已補進 spec | 官網產品頁與頁首皆寫 Handmade in Berlin，已在 basic_info.manufacturing 補上「手工製造」並標 [official]；柏林、Cinematic Octave Divider（full_name）、Octave Shimmer（官網標題）原本就有依據（來源：https://www.lichtlaermaudio.com/shop/as-above-so-below-cinematic-octave-divider-reverb） |
| `description` | **刪除** | 官網沒有解釋名稱的含意；spec 的「天堂與地底碰撞」講的是 Both 模式，不是名稱，整句刪除 |
| `description` | **刪除** | 官網完全沒提高增益；spec 只寫「搭配高增益（特別設計）」。「多數 Shimmer Reverb…泥濘混濁」「調整過演算法」「仍清晰可辨」都沒有依據，整句刪除（經銷商文案不能當成 add_to_spec 的依據） |
| `description` | **刪除** | 刪除子句「評測與使用者一致」：spec 只寫「被稱為」，沒交代是誰這樣說，這個歸屬沒有依據 |
| `description` | 保留 | 官網寫 Expression 可即時控制疊加的八度，原文是 fading the heavens in and out；spec 也寫「即時控制高/低八度淡入淡出」，「漸強 Shimmer」是直接推得的用法 |
| `specs.tonalCharacteristics.dynamics` | **刪除** | spec 與官網都沒有「對輸入電平敏感」，官網也沒提高增益或「疊在破音之後仍不模糊」，整個值刪除 |
| `suggestedSettings.0.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `description` | 保留 | Mono 有使用者確認並記在 spec；9V DC only 是官方規格；X/Y 依模式而異在 spec 有寫，cons 也寫「可能混淆」。「初期容易」只是措辭差異 |
| `description` | **刪除** | 刪除子句「如地底震動」：官網的 depths／subterranean 和 spec 的「深沉、Drone、Sub-Octave」支持其餘內容，但「震動」這個比喻沒有依據；影響小，依規則刪除 |

### #24 Sweet Honey Overdrive Deluxe（`sweet_honey.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除「傳奇的」與「（設計者 Björn Juhl）」兩個子句：官方手冊沒有提到 Juhl，「傳奇」屬於修飾。「芬蘭」有官方手冊佐證，已以 country 補進 spec；「Honey Bee 電路演進」原本 spec 就有，這兩部分可保留 |
| `description` | **刪除** | 整句刪除（Bias 類比、甜蜜點需要時間實驗）：spec 與官方手冊都沒有這個說法 |
| `description` | 已補進 spec | 官方手冊原文為 Bass「pre distortion, it sets how the bass and low mids are distorted」、Treble「post distortion, it cuts and/or boosts the treble」，已補進 spec。「只改變輸出音色」可從 post-gain 位置直接推得（來源：https://mpamp.com/files/manuals/Sweet%20Honey%20Overdrive%20Deluxe%20manual.pdf） |
| `description` | **刪除** | 刪除「MONO 的 Takaakira Goto 與創作歌手 Andrew Bird 都是使用者」與「評價極高」：spec 只寫「特別受 Post-Rock 音樂人喜愛」，沒有點名任何藝人 |
| `description` | **刪除** | 整句刪除（Rhythm 設定下難切入 Mix、更適合 Lead／Solo）：spec 與官方手冊都沒有提到 |
| `specs.controls.3.function` | 保留 | spec 寫 Treble 在 post-gain，官方原文是「post distortion, cuts and/or boosts the treble」，「只改變輸出音色」可以直接推得 |
| `specs.controls.4.function` | 已補進 spec | 官方手冊原文「BASS, pre distortion, it sets how the bass and low mids are distorted」，已在 spec 補上 official_text 與 effect_on_distortion（來源：https://mpamp.com/files/manuals/Sweet%20Honey%20Overdrive%20Deluxe%20manual.pdf） |
| `specs.tonalCharacteristics.frequency.low` | 已補進 spec | 依官方手冊 Bass 為 pre distortion、決定低頻失真方式，已在 spec 補上 frequency.low_note [official]（來源：https://mpamp.com/files/manuals/Sweet%20Honey%20Overdrive%20Deluxe%20manual.pdf） |
| `specs.tonalCharacteristics.frequency.high` | 保留 | spec 寫 Treble 在 post-gain，「只影響輸出音色」可直接推得；官方原文是 post distortion cuts/boosts treble |
| `specs.reviewSummary.cons.1` | **刪除** | spec 的 review_summary 沒有 cons，官方手冊也沒有「FOCUS 需花時間理解」的說法 |
| `specs.reviewSummary.conclusion` | **刪除** | 刪除「首選」：沒有依據。Jazz／Blues／Neo Soul、always-on、溫暖，以及 Joyo Sweet Baby 為較便宜替代，spec 都有，可以保留 |
| `suggestedSettings.0` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.1` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.3` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.tonalCharacteristics.dynamics` | **刪除** | 刪除「可透過 FOCUS」子句：spec 只寫壓縮「適中且可調」，沒有指明是由 FOCUS 調整，官方手冊也沒有提到壓縮。其餘內容 spec 有，可以保留 |
| `suggestedSettings.2.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |

### #25 Cali76 FET Compressor（`cali76_fet.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除「並取代先前的 Cali76 Compact Deluxe」子句：官方 Compact Deluxe 頁僅歸類 Discontinued，未說被 FET 取代；「2024 年發售」與 spec release_year 一致可留 |
| `description` | 已補進 spec | 官方產品頁與手冊 V2.2 p.6 明寫 inspired by the Urei 1176；已補 technical_specs.compression.inspired_by [official]（「傳奇的」屬修飾語，「設計藍本」對應 inspired by）（來源：https://origineffects.com/product/cali76-fet-compressor/） |
| `description` | **刪除** | 整句刪除：「評測一致認為」無出處；且「高頻更豐富」與 spec「略少於 Compact Deluxe 的光澤」相牴觸 |
| `description` | **刪除** | 刪除「線性」一詞：官方手冊只說 10-LED 依 dB 增益衰減標記，未說線性；其餘（10-LED、dB 刻度、增益衰減）spec 已有可保留 |
| `suggestedSettings.3` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.0.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suggestedSettings.2.description` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.reviewSummary.cons` | 保留 | 兩項都由 spec 直接推得：power.battery false／「不支援電池」（官方產品頁亦確認僅用變壓器），controls.ATTACK direction「與多數壓縮器相反」 |
| `specs.reviewSummary.pros` | 保留 | 是 spec pros「Sustain enhancement」「Dry mix control」與 parallel_compression 的忠實改寫 |
| `description（2024 年發售並取代先前的 Cali76 Compact Deluxe）` | **刪除** | 驗證補充：原 agent 只處理了 description 的 Urei 1176 那一句，這一列漏掉了。spec 的 basic_info.release_year 2024 支持「2024 年發售」，可以保留。「取代先前的 Cali76 Compact Deluxe」只能刪：spec 沒寫，官方產品頁只說是 'latest in a long lineage'，手冊 V2.2 全文也沒提到 Compact Deluxe 或 replace。 |
| `description（評測一致認為這是新舊版最明顯的差異：音色更有機…延音更會唱歌）` | **刪除** | 驗證補充：原 agent 漏掉這一列。spec 沒有任何評測共識的說法，整句刪除。 |
| `description（10-LED 以 dB 刻度線性顯示增益衰減）` | **刪除** | 驗證補充：原 agent 漏掉這一列。spec 的 visual_feedback（10-LED 增益衰減指示器、dB 刻度）支持「10-LED 以 dB 刻度顯示增益衰減」，可以保留。「線性」要刪：手冊 V2.2 只寫 'Marked according to dB of gain reduction'，官方產品頁也沒有說刻度是不是線性。 |

### #27 Horsemeat Transparent Overdrive（`prs_horsemeat.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 刪除「是 PRS 正式進入效果器市場的首批產品之一」：spec、HANDOFF 與官方產品頁都沒有這個說法（頁面建立日期 2022-08-16 只是暗示，不算明文） |
| `description` | 保留 | spec 已有：comparisons.vs_others.description「結合 Timmy, Blues Driver, Klon, OCD 的優點」；「忠於吉他音色」是 design_goal「透明,不染色」與 design_features「Extremely transparent」的改寫。稽核標的 not mentioned 是漏看 |
| `description` | 保留 | spec 都有依據：gain_range「Clean boost to Medium-high gain」、compression「適中」、pick/volume_sensitivity「高」、best_for「Smooth tube-esque tones」、pros「tube-like 音色」；只有「所以」這個因果連接詞是潤飾，影響小 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除　驗證補充：使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `officialUrl` | 已補進 spec | 這是 PRS 官方產品頁。直接連線回 403（Cloudflare 擋了自動抓取），改用 Wayback 快照 20260709021136（狀態 200）核對內容，已在 basic_info 加上 official_url，標 [official]，並列入 sources（來源：https://prsguitars.com/pedals/model/horsemeat） |
| `description（是 PRS 正式進入效果器市場的首批產品之一。）` | **刪除** | 驗證補充：Nothing in the spec says this. The official page I fetched (Wayback 20260709021136 of https://prsguitars.com/pedals/model/horsemeat) does not say it either: the only 'first' on the page is in an artist quote ('the first to really live up to the hype'). Delete the whole sentence. |

### #28 Blacklon Amp-in-a-Box（`roshi_blacklon.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `specs.bypass` | 已補進 spec | 官方頁寫「スイッチング方式：トゥルーバイパス」，已在 technical_specs.bypass 補上並標 [official]（來源：https://roshipedals.com/en/collections/products/products/blacklon） |
| `specs.reviewSummary.cons` | **刪除** | spec 沒有 cons。「品牌小眾、維修支援有限」「不適合現場快速切換」都查無依據；10V 上限已寫在 warnings，不必放在 cons 裡 |
| `specs.reviewSummary.conclusion` | 保留 | 可由 spec 推出：signal_chain.notes「讓 JC-22 有管機感」、special_use.jc_amp、value_proposition 都寫了 |
| `description` | 已補進 spec | 官方原文「Plexitionに続くAMPシリーズの第2弾。」，已補成 basic_info.series_position [official]（來源：https://roshipedals.com/en/collections/products/products/blacklon） |
| `description` | **刪除** | 官方只寫 BLACKFACE 期的 AB763 線路，沒有列出 Deluxe／Princeton／Vibroverb／Twin Reverb 這些機型，整句刪除 |
| `description` | **刪除** | 「評測認為這句話不算誇大」沒有可以追溯的評測來源，刪除這個子句 |
| `description` | 已補進 spec | 官方明寫「JCなどのトランジスタアンプでも真空管アンプのような…質感を得ることができる」，已補成 special_use.jc_amp_official [official]（來源：https://roshipedals.com/en/collections/products/products/blacklon） |
| `description` | **刪除** | 「上限 10V、超過會損壞」spec 已經有；「且無法修復」官方沒有這麼說（官方原文只到「故障の原因」），所以刪除「無法修復」這個子句 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suitableStyles` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `specs.features` | 已補進 spec | 官方頁有 JC 等電晶體音箱可獲得真空管質感的原文，已補成 special_use.jc_amp_official [official]（來源：https://roshipedals.com/en/collections/products/products/blacklon） |
| `description` | **刪除** | 官方和 spec 都只說切換後約 30 秒不穩定、屬正常現象；「不適合現場快速切換」是網站自己推論的，刪除 |
| `officialUrl` | 已補進 spec | 本次已抓取並確認這是官方產品頁，網址已加進 sources（來源：https://roshipedals.com/en/collections/products/products/blacklon） |

### #29 Source Code Overdrive（`twa_source_code.yaml`）

| 欄位 | 處置 | 說明 |
|---|---|---|
| `description` | **刪除** | 整句刪除：官方寫的是 Tamura「50+ years of experience」，網站寫「四十多年」與官方不符；「不是複刻或修改版」是網站自己加的修飾，spec 沒有這個說法 |
| `description` | **刪除** | 前半句（內部穩壓器升到 18V，換來更大 headroom、更好的動態與更清晰的音色）spec 有寫，保留；刪除「複雜和弦在高增益下仍保持分離度」這一段，spec 和官方頁都沒有這個說法 |
| `description` | **刪除** | 整句刪除：Guitar World 的評測結論 spec 沒有收錄，而第三方媒體評語不能用官方來源證實 |
| `specs.tonalCharacteristics.coreTone` | **刪除** | 「TS 中頻推升但更平衡、18V 高 headroom」spec 有寫，保留；刪除「音符分離度」這一段，spec 只寫「更清晰的音色」，沒有寫分離度 |
| `specs.reviewSummary.cons` | **刪除** | 四點缺點 spec 都沒有。官方標價 USD 299，但沒有寫比 TS808 貴約 $100；官方寫的是 mechanical true bypass，「Buffer 為 Always-on」沒有根據（spec 的 impedance.buffer 也寫 Always-on，跟官方矛盾，這不在本次清單內，待另案查證） |
| `specs.reviewSummary.conclusion` | **刪除** | spec 的 review_summary 沒有 conclusion 這個欄位，「首選」是網站自己下的評價，影響小，直接刪 |
| `suggestedSettings` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `suitableStyles.4` | **刪除** | 使用者裁定：suggestedSettings／suitableStyles 一律刪除 |
| `description` | **刪除** | 「增益範圍比 TS808 更廣」spec 的 gain_range 有寫，保留；刪除「從 clean boost 一路到高增益都做得到」這一段，spec 只寫 Low to High，官方也沒有說能當 clean boost |
| `officialUrl` | 已補進 spec | 本次已抓取官方商品頁（HTTP 200，商品標題為 Source Code overdrive designed by Susumu Tamura，標價 USD 299）；已在 basic_info 加上 official_url 並標註 [official]，sources 也補上網址（來源：https://totallywyckedaudio.com/products/sc-01-source-code-overdrive） |

## 不在這次範圍

- 報告第四節（目錄資料裡的使用者個人資訊 24 項）：使用者這次沒有要求處理
- Imperial MKII 的電源：處置 agent 發現官方手冊寫附 Universal 12V 電源，spec 寫 9–18V DC（預估）。本次沒有改 spec，列為 Research 待查

## 補充：回覆 Website ack 的 6 件事（2026-10-13）

| # | 事項 | Research 的結論 | Website 要做什麼 |
|---|---|---|---|
| 1 | JC-22 `specs.pedalPairingNotes[3]` 的「Sag」 | 比照 description，刪掉「Sag」。spec 沒有任何地方提到 Sag | 刪掉「Sag 與」，保留「溫暖度」 |
| 2 | Thinline `specs.reviewSummary.cons` | spec 分開記載：「Ash 琴身對濕度敏感」與「Semi-hollow 結構較脆弱」 | 改寫成兩點，不要把濕度敏感歸給半空心結構 |
| 3 | Imperial MKII 電源 | spec 已依官方手冊改正：**9–12V DC**、中心負、需 ≥ 9W、附 Universal 12V 變壓器（不接地）。官方沒有公布 mA 數。原本的 9–18V、300 mA 是預估值 | 用 `/migrate-data` 同步電源欄位 |
| 4 | Colosseum 電流與輸出阻抗 | spec 已依官方手冊改正：**200mA**、輸出阻抗 **10kΩ** | 同步 |
| 5 | Sweet Honey | spec 已依官方手冊改正：電流 **6 mA**、供電 7.5–18V DC、輸入阻抗 **390kΩ**、輸出阻抗 **25kΩ**、bypass 與電池加上 [official] | 同步 |
| 6 | Source Code bypass | spec 已依官方頁改正：**mechanical true bypass**。input buffer 只在效果開啟時作用，不是 always-on | 同步 |

第 3–6 件每份 spec 由 1 個 agent 修正、1 個 agent 重新抓官方來源驗證。brand／model／id 都沒動，不需要 previousKeys。
