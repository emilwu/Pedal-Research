# 設備可調參數詞彙

**產生日期**：2026-09-11
**最後更新**：2026-09-11（補完七項資料缺口後回頭校正，見文末「2026-09-11 的缺口補齊結果」）
**資料來源**：`shared/equipment_database/` 底下 26 份 spec YAML（效果器 17、吉他 4、音箱 3、配件 2）
**用途**：供 Pedal-Web-Service-Planning 設計 `UserEquipment.settings` 與 `SignalChainItem.settings` 的 Json 結構時作為依據

---

## 這份文件是什麼，不是什麼

**是**：本知識庫裡「設備實際上有哪些可調參數」的詞彙整理，以及「資料本身長成這樣，所以任何結構都必須面對什麼」的限制清單。

**不是**：Json 欄位設計、資料型別建議、schema 草案。那是 Pedal-Web-Service-Planning 的職權，本 repo 不做那個決定。

第 5 節的限制不是「建議你怎麼做」，而是「不管你怎麼做，這些事實會讓某些設計行不通」。第 6 節是 Research 答不出來、必須由 Planning 決定的問題。

---

## 怎麼產生的

9 個 agent，26 份 YAML 全部完整讀過（非 grep）。抽取規則是**只記錄檔案裡真的寫了的東西**：不補齊、不推論、不用對該型號的既有知識填空。

最後一個 agent 專門反查捏造與遺漏，逐行比對原檔。它的判定是 `pass-with-issues`，三處問題已在第 8 節列出並修正。

---

## 涵蓋範圍

| 類型 | 檔案數 | 有 controls | 有 settings preset |
|---|---|---|---|
| 效果器 | 17 | 17 | **4** |
| 吉他 | 4 | 4 | 0 |
| 音箱 | 3 | 3 | 0 |
| 配件 | 2 | **0** | 0 |
| 合計 | 26 | 24 | 4 |

26 台裡只有 4 台有建議設定值：`aasb`、`cali76_fet`、`empress_mkii`、`nucleo`。其餘 22 台只有控制項名稱。

---

## 參數詞彙

### 效果器（17 台，43 個概念上獨立的參數）

同一台設備內出現兩次同名控制（例如雙通道的兩個 Volume）只算一次。

**出現在 2 台以上的：**

| 標準名稱 | 台數 | 型態 | 見過的原文寫法 | 值的樣子 |
|---|---|---|---|---|
| Volume（輸出電平） | 14 | continuous | `Volume` `Level` `LEVEL` `OUT` `OUTPUT` `NOR LEVEL` `DRV LEVEL` | 多數未標刻度；preset 裡出現過「Unity」「70-100%」 |
| Drive／Gain（增益量） | 10 | continuous | `Drive` `DRIVE` `Gain` `GAIN` | 多為文字描述，未標數值範圍 |
| Tone（單旋鈕整體音色） | 7 | continuous | `Tone` `TONE` | `empress_mkii` 特別註明是 Tilt EQ（500Hz 中心） |
| MIX（乾濕混合） | 5 | continuous | `MIX` `Mix` `DRY` | 多標「0-100%」或無範圍。`DRY` 是以乾訊號比例描述，方向相反 |
| Treble（高頻） | 3 | continuous | `Treble` | 文字描述「高頻 cut/boost」 |
| Bass（低頻） | 3 | continuous | `Bass` | 文字描述「低頻 cut/boost」 |
| Attack（壓縮啟動速度） | 2 | continuous | `ATTACK` | 未標範圍 |
| Release（壓縮恢復速度） | 2 | continuous | `RELEASE` | `cali76_fet` 標 69.5-398ms；`empress_mkii` 標 50ms-1s |
| Ratio（壓縮比） | 2 | **mixed** | `RATIO` | `empress_mkii` 是離散，列出 2:1／4:1／10:1；`cali76_fet` 是**連續**旋鈕，4:1 ~ 20:1（2026-09-11 依官方手冊 V2.2 查實。原本記為「宣告是選擇但沒給檔位」，那個判讀本身就是錯的） |
| Input Gain／Threshold | 2 | continuous | `IN` `INPUT` | 未標範圍 |
| Decay（殘響／延遲長度） | 2 | unknown | `DECAY` `DECAY/PRE-D` | 文字描述「長至無限」，無刻度 |
| Pre-Delay（預延遲） | 2 | continuous | `X Control` `PRE-D` | 文字描述「低至中」，**未標時間單位** |
| Octave／Pitch Level | 2 | continuous | `Y Control` `X Control` `AIR/PITCH` | 文字描述，無音程或 dB 單位 |
| Routing／Order Switch | 2 | discrete | `Order Toggle` `Routing select` | 檔位：BB→Klon／Klon→BB、Parallel／Series |
| **模式相依複合旋鈕** | 2 | **compound** | `X Control` `Y Control` `BLEND/VOLUME` `MOD/RATE` `AIR/PITCH` `FLUX/SPEED` `DECAY/PRE-D` `TONE/DIFF` `FREEZE-PITCH/FREEZE-VOLUME` | **一個實體旋鈕對應多個邏輯參數，依裝置當下模式而定，各自值域不同** |

**只出現在 1 台的（29 項）：**

離散或開關類 — `SIDECHAIN HPF`（120Hz／OFF／240Hz）、`Bright Cut Toggle`、`6L6/6V6 Mode Toggle`、`Mellow/Drive Mode Toggle`、`EQ ON / GLASS Switch`、`ROCK / JAZZ Switch`、`PRESET Switch`（1／2／3／4）、`ON/OFF Switch`

連續類 — `Dampen`、`Rate/Speed`、`Diffusion`、`Clean Control`、`Clip Blender`、`Focus`、`Bite`、`Voice`、`Reverb Level`、`Delay Time`、`Feedback`、`PARAMETER Encoder`

`ff1y` 的 `EQ (3-band)` 於 2026-09-11 查實為 **TREBLE（面板絲印 TREB）／MIDDLE（MID）／BASS** 三段。每段各有三個可選中心頻率點，增益 -15.0 dB 到 +15.0 dB。三段都沒有專屬旋鈕，要用 EQ 開關選段、PARAMETER encoder 改值。

型態不明或資料不全 — `SAVE Switch`、`Freeze`、`Cursor Keys`

**2026-09-11 已解決**（原本列在這一段，現已依官方手冊補實）：

- `odl1cs` 的 `PUSH` 與 `HI CUT` — 兩者皆為**連續**控制。PUSH 是大旋鈕，不是按鈕也不是 push-pull；HI CUT 是前面板小 trim，不是撥桿
- `empress_buffer_plus_plus` — 1 個 footswitch、2 個旋鈕、6 個撥桿，全部有名稱與功能
- `ff1y` 的 `Modulation controls` — 實為 DEPTH／RATE／RFPM 三個參數
- `ff1y` 的 `Soft Clipping control` — 實為 LEVEL 與 GAIN 兩顆旋鈕，加一個 SOFT CLIPPING ON 開關

### 吉他（4 台）

| 標準名稱 | 台數 | 型態 | 見過的原文寫法 | 說明 |
|---|---|---|---|---|
| Volume | 6 個實例／4 台 | **unknown** | `Volume (Neck)` `Volume (Bridge)` `Volume (共用)` | 純名稱字串，**四份檔案都沒寫 controlKind、刻度、taper**。2026-09-12：`esp_throbber_ctm` 經使用者確認實機是 Master Volume 一顆，原記兩顆（實例數 7 → 6） |
| Tone | 4 個實例／4 台 | **unknown** | `Tone (共用)` | 同上。兩次更正後**四把琴的 Tone 都是共用一顆**：`esp_eclipse_ctm`（2026-09-11）與 `esp_throbber_ctm`（2026-09-12）原本各記兩顆，經使用者確認實機後更正（實例數 6 → 5 → 4）。`Tone (Neck)` `Tone (Bridge)` 這兩種寫法已不再出現在任何一份檔案裡 |
| Pickup Selector Switch | 4 | discrete | `3-way pickup selector`、`5-Way Lever PU Selector` | **檔數不一致**：三把是 3 檔，`esp_throbber_ctm` 是 **5 檔**（2026-09-11 經使用者確認實機為 ESP 上位機種 THROBBER，原本誤記為 3-way）。檔位名稱只有 `fender_tokyo_thinline` 查到官方寫法（Position 1 Bridge／2 Bridge+Neck／3 Neck），其餘三把的官方文件一律不命名檔位 |

四份檔案都完整讀過，`pickups.controls` 之外沒有其他使用者可調項目（沒有 coil-split、push-pull、主動 EQ）。

作用範圍在同一把琴內不一致：

| 吉他 | Volume | Tone | 旋鈕數 |
|---|---|---|---|
| `esp_eclipse_ctm` | per-pickup | 共用 | 3 |
| `esp_throbber_ctm` | 共用 | 共用 | 2 |
| `fender_tokyo_thinline` | 共用 | 共用 | 2 |
| `greco_te500` | per-pickup | 共用 | 3 |

四把琴全部經使用者確認實機（2026-09-11 與 09-12 兩次）。

**Tone 四把都是共用。Volume 兩把 per-pickup、兩把共用。**所以 `esp_eclipse_ctm` 與
`greco_te500` 是「同一把琴內兩種規則並存」，另外兩把則是一致的。這張表仍然是
「不能假設同一把琴內規則一致」的直接證據，只是不一致的是那兩把，不是原本以為的一把。

### 音箱（3 台）

| 標準名稱 | 出現數 | 型態 | 見過的原文寫法 |
|---|---|---|---|
| Volume | 4 | unknown／mixed | `Volume`、`Volume knob` |
| Treble | 4 | unknown／mixed | `Treble` |
| Bass | 4 | unknown／mixed | `Bass` |
| Middle／Mid | 4 | unknown／mixed | `Middle`（dsm、roland）、`Mid`（tone_king） |
| Bright Switch／BRIGHT | 2 | **mixed**（一個標 toggle，一個標 discrete 含 OFF／ON） | `Bright Switch`、`BRIGHT` |
| Mid Boost／Mid-Bite Switch | 2 | unknown／mixed | `Mid Boost Switch`、`Mid-Bite Switch` |
| Chorus Speed／Depth | 2 | unknown | `Speed`、`Depth`（皆標 range 0-10） |
| HF Comp／Low-Pass Filter | 2 | **software** | 標明只能透過 Tone King Editor 軟體編輯，per_channel |

單一出現：`Drive`、`Gain`、`Rock/Jazz Switch`、`PAB (Preamp Boost)`、`Reverb Level`、`Reverb Type`（Room／Ethereal／Plate）、`Reverb (footswitch enable)`、`Cab Sim Switch`、`Ground Lift Switch`、`Chorus ON/OFF`

**兩個在 controls 清單外的真實控制項**：
- `shared/equipment_database/amps/specs/roland_jc22.yaml:189` 的 REVERB 旋鈕，只出現在 `built_in_effects.reverb`，不在該檔自己的 controls 區塊
- `shared/equipment_database/amps/specs/dsm_dumblifier.yaml:105` 的 Input Boost switch，只出現在 `connectivity.inputs`

三份檔案都沒寫任何連續控制的電位器阻值、段位數或 taper。

### 配件（2 台）

`rockboard_mod2_v2` 與 `rockboard_mod3_v2` 兩份完整讀過，**任何 controls 路徑下都是零筆**。它們沒有可調參數，記錄的是 `connectors`、`core_features` 這類接線規格。

---

## 資料事實構成的限制

以下每一條都不是建議，是資料長成這樣所造成的既成事實。

### C1 — 參數名稱在裝置內不唯一

雙通道效果器與雙通道音箱都有兩份同名旋鈕，必須靠通道歸屬才能分辨。

- `shared/equipment_database/pedals/specs/cornerstone_colosseum.yaml:39-53` — Volume／Drive／Tone 在 `bb_side` 與 `klon_side` 各一份
- `shared/equipment_database/pedals/specs/from_yesterday_kot.yaml:44-56` — 同樣在 `red_channel` 與 `yellow_channel` 各一份
- `shared/equipment_database/amps/specs/tone_king_imperial_mkii.yaml:63-66,77-81` — rhythm 與 lead channel 各自列出 Volume／Treble／Mid／Bass，**兩邊完全同名且 YAML 沒有任何區分標記**

`odl1cs` 更進一步：兩個通道用**不同名字**指涉同一種功能角色。`normal` 用 `GAIN`／`NOR LEVEL`，`drive` 用 `DRIVE`／`DRV LEVEL`（`shared/equipment_database/pedals/specs/odl1cs.yaml:38,43`）。

**忽略的話**：把參數名稱當成裝置內的唯一鍵，雙通道裝置的兩個旋鈕會互相覆蓋成一筆。用字面比對做設定值比較，`odl1cs` 的兩個通道會被判成結構不同的裝置——字面上找不到共同的 key。

### C2 — 吉他的參數名稱把拾音器位置寫進字串裡，且範圍規則在同一把琴內可能不一致

`Volume (Neck)`、`Tone (共用)` 這種寫法把「參數」與「作用位置」黏在同一個字串。

四把琴分成兩組（行號為 2026-09-12 實際值）：

| 組別 | 吉他 | Volume | Tone |
|---|---|---|---|
| 同一把琴內兩種規則並存 | `guitars/specs/esp_eclipse_ctm.yaml:79-81`、`guitars/specs/greco_te500.yaml:89-91` | per-pickup | 共用 |
| 同一把琴內規則一致 | `guitars/specs/esp_throbber_ctm.yaml:89-90`、`guitars/specs/fender_tokyo_thinline.yaml:88-89` | 共用 | 共用 |

**忽略的話**：假設「同一把琴內所有旋鈕的範圍規則一致」，`esp_eclipse_ctm` 與 `greco_te500` 會被錯誤處理。位置資訊若被吃進參數名字串而未獨立辨識，日後想把它與其他琴的 Volume 放在同一個比較維度時對不齊。

### C3 — 效果器的控制項混了三種本質不同的操作型態，而且標示方式不統一

連續旋鈕、有限檔位的離散開關、純二態開關三種混在同一份 controls 清單裡，來源檔案沒有統一的欄位標示方式。

- `shared/equipment_database/pedals/specs/empress_mkii.yaml:52-56` — RATIO 與 SIDECHAIN HPF 明確列出檔位
- ~~`shared/equipment_database/pedals/specs/cali76_fet.yaml:52` — 同概念的 RATIO 只有「壓縮比例選擇」文字，沒有檔位列表~~
  **2026-09-11 解決**：它根本不是離散控制。官方手冊 V2.2 確認為連續旋鈕（4:1 ~ 20:1）。當時判定它「宣告是選擇」本身就是誤判——`function` 欄的「選擇」兩字不表示離散。
- `shared/equipment_database/pedals/specs/morning_glory.yaml:37` — Bright Cut Toggle 的檔位不在 control 條目裡，要到另一個 `bright_cut` 區塊（`:66-77`）才找得到 `left_off.setting: "關閉"` 與 `right_on.setting: "開啟"`

**忽略的話**：假設所有 discrete 控制都會在同一個地方寫出完整選項，會漏掉 `cali76_fet` 這種「宣告是離散但沒給檔位」與 `morning_glory` 這種「選項要去別的區塊反推」。兩者外觀相同但可信度完全不同。

### C4 — 同一份檔案內的結構就可能不一致

`shared/equipment_database/amps/specs/roland_jc22.yaml:48-72`：

- Treble／Middle／Bass／Speed／Depth 只給 `range: "0-10"`，**沒說是連續電位器還是 10 段固定檔位**
- 功能相同的二態開關被分成兩種分類方式：BRIGHT 用 `positions: [OFF, ON]`（`:67`），Chorus ON/OFF 沒有 positions 欄位（`:71`）
- `volume` 是純字串值（`volume: "Volume knob"`），`tone`／`chorus`／`switches` 是物件陣列

**忽略的話**：假設「range 存在等於連續值」，會把可能是段位式的旋鈕誤判成連續。假設「同一份檔案內同性質欄位用同一種結構」，解析器會在 volume 這個字串欄位上走錯程式路徑。

### C5 — 現有 preset 的值幾乎全是中文自然語言，不是數字

4 台有 preset 的裝置，值長這樣：

- `shared/equipment_database/pedals/specs/empress_mkii.yaml:116-123` — `input: "輕微觸發(1-2 LED)"`、`output: "Unity"`、`tone: "正午"`
- `shared/equipment_database/pedals/specs/aasb.yaml:127-133` — `mix: "50-70%"`、`decay: "中至長"`、`dampen: "中性至略暗"`
- `shared/equipment_database/pedals/specs/cali76_fet.yaml:97-104` — `attack: "慢"`、`release: "中至快"`

即便偶有百分比，也是文字裡嵌入的範圍區間，不是單一數值。

**忽略的話**：把這些 preset 直接當成「可比較的設定值」來源會失敗。「正午」是鐘面隱喻、「中至高」是模糊區間、「1-2 LED」是裝置特定的視覺指示——彼此無法做數值層級的距離比較。這是資料本身的限制，不是顯示格式的問題。

### C6 — preset 的 key 與 controls 的 name 是兩套獨立詞彙表

三種落差同時存在：

1. **大小寫不對應** — `empress_mkii` 的 controls 用 `INPUT`／`OUTPUT`／`SIDECHAIN HPF`（`:42,44,56`），settings 用 `input`／`output`／`hpf`（`:116,122-123`）
2. **完全新造的 key** — `aasb` 的 controls 只有 `X Control`／`Y Control`（`:54,56`），settings 卻用 `x_predelay`／`y_octave`／`x_low_octave`／`y_high_octave`（`:127-156`）。`nucleo` 的 `mod`／`air`／`flux` 對應到 `MOD/RATE`／`AIR/PITCH`／`FLUX/SPEED` 這種複合命名
3. **同一裝置不同 preset 用不同 key 組合** — `aasb` 的 `basic_shimmer_above` 用 `x_predelay`／`y_octave`，`dual_octave_both` 用 `x_low_octave`／`y_high_octave`，`ambient_pad_freeze` 又完全不同，還多一個 `technique` key（不對應任何 control）

**忽略的話**：假設 preset key 可以靠大小寫正規化對回 controls 的 name，`aasb` 與 `nucleo` 會完全對不上。這不是命名風格問題，是同一份資料在兩個區塊用了兩套詞彙表。

### C7 — 26 台裡只有 4 台有 preset，其餘 22 台從來就沒打算提供

沒有 preset 的：13 台效果器、全部 4 台吉他、全部 3 台音箱、全部 2 台配件。

**忽略的話**：把「有 preset 範例可顯示」當成所有裝置的常態能力來設計，85%（22/26）的裝置會落入「這台完全沒有資料可用」，而不是「資料不足待補齊」——來源檔案本身就沒有這個打算。

### C8 — 部分控制項連功能說明與型態都沒有

- `shared/equipment_database/pedals/specs/odl1cs.yaml:38,43` — 7 個通道控制（`NOR LEVEL`／`TONE`／`GAIN`／`DRV LEVEL`／`DRIVE`／`PUSH`／`HI CUT`）**全部只有名稱，沒有任何 function**。`PUSH` 與 `HI CUT` 連該歸類成哪種概念都判斷不了
- `shared/equipment_database/amps/specs/tone_king_imperial_mkii.yaml:63-66,77-81` — 全部 channel controls 同樣是純字串陣列
- 四把吉他的 Volume／Tone 亦然
- `shared/equipment_database/pedals/specs/empress_buffer_plus_plus.yaml:82,89,96` — footswitches／knobs／switches **連「有幾個」都標示 TBD**，該檔自陳 `data_reliability: "中"`

**忽略的話**：要求「每個參數都要有可展示的功能說明或型態分類」，這些條目沒有真實資料可填。

### C9 — controls 清單不是該裝置全部可調項目的完整枚舉

- `shared/equipment_database/amps/specs/roland_jc22.yaml:187-190` 的 REVERB 旋鈕，不在 `:48-72` 的 controls 區塊
- `shared/equipment_database/amps/specs/dsm_dumblifier.yaml:105` 的 Input Boost switch，不在 `:58-98` 的 controls 區塊
- `shared/equipment_database/pedals/specs/from_yesterday_kot.yaml:65-71` 記載了內部 DIP switches 與 trimpot，未列入 controls

「內部微調不算 controls」這條分界線是抽取時的假設，**檔案本身從未明文宣告這個排除標準**。其他裝置是否也有類似未收錄項目，資料本身無法確認或排除。

### C10 — 四類設備用四種不同的 controls 資料結構

| 類型 | 結構 | 例子 |
|---|---|---|
| 效果器 | 物件陣列，每項有 `name` 與 `function` | `pedals/specs/empress_mkii.yaml:42-56` |
| 吉他 | 純字串陣列，位置資訊內嵌在字串裡 | `guitars/specs/esp_eclipse_ctm.yaml:79-83` |
| 音箱 | 三種並存於同一台：channel 底下的純字串陣列、`shared_controls` 物件陣列、`software_controls` 獨立區塊 | `amps/specs/tone_king_imperial_mkii.yaml:63-66,88,104-110` |
| 音箱（另一種） | **頂層 mapping**，不是 sequence，也不在 `technical_specs` 底下 | `amps/specs/roland_jc22.yaml:48` |
| 配件 | 完全沒有 controls 路徑 | `accessories/specs/rockboard_mod2_v2.yaml` |

**忽略的話**：假設四類設備能共用同一套讀取邏輯，吉他沒有 function 欄位、配件沒有 controls 路徑、音箱同一台內混三種區塊、`roland_jc22` 是 mapping 而非陣列，通用解析會讀到空值或結構不符——這是資料結構本身四套並存的事實，不是單一裝置的例外。

---

## Research 答不出來、必須由 Planning 決定的問題

以下六題都不是設備知識問題，本 repo 無權也無法決定。

1. **雙通道裝置的兩份同名參數，要視為「同一個邏輯參數的兩個值」還是「兩個獨立參數」？** 若視為獨立，要用什麼方式讓使用者知道這兩個 Volume 分屬不同通道？
   — YAML 只記錄了「Volume 這個字在 `bb_side` 出現一次、在 `klon_side` 出現一次」這個事實。

2. **使用者輸入的設定值要不要限制成數字？** 還是允許保留「正午」「輕微觸發(1-2 LED)」這類自然語言？若要數值化，由誰、依什麼規則把既有 4 台的中文描述轉成數字？
   — 這是輸入驗證與資料正規化的產品決策。來源檔案從未提供對照的數值刻度。

3. **22 台沒有 preset 的裝置，系統要呈現什麼？** 空白、猜測值、還是不提供該裝置的設定紀錄功能？
   — Research 只能確認「這 22 台確實沒有」，無權自行生成猜測值——那會違反不補齊、不推論的資料規則。

4. **型態標為 unknown 的參數要用什麼互動元件？** 滑桿、下拉選單、還是純文字欄位？
   — 來源資料沒寫是連續還是離散。在型態不明下要用哪種元件，是介面設計決策。

5. **C9 那些「存在但未列入 controls」的真實控制項要不要算正式參數？** 由誰決定要不要補齊？
   — 這牽涉 controls 清單的完整性標準要多嚴格，是產品決策。

6. **`empress_buffer_plus_plus` 這種資料完整度最差的裝置，上線前要不要有資料品質門檻？** 排除、標示警告、還是原樣呈現？
   — 這是產品上線標準與資料治理政策。

---

## 2026-09-11 的缺口補齊結果

原本列了七項缺口。以下是每一項的處理結果。

| # | 缺口 | 結果 |
|---|---|---|
| 1 | `empress_buffer_plus_plus` 的 footswitches／knobs／switches 數量與功能全是 TBD | **已補齊**（官方手冊 rev04） |
| 2 | `odl1cs` 的 7 個通道控制沒有功能說明，`PUSH` 與 `HI CUT` 功能不明 | **已補齊**（官方 CS 手冊 ver 1.2） |
| 3 | 四把吉他的 pickup selector 都沒寫出三個檔位的實際名稱 | **一把補齊、三把確認查不到** |
| 4 | `cali76_fet` 的 RATIO 宣告是離散但沒給檔位 | **已補齊**，而且原判讀有誤（是連續不是離散） |
| 5 | `ff1y` 的 EQ (3-band) 未列出個別旋鈕名稱；Delay Time／Feedback 的「×2」意義不明 | **已補齊**（官方手冊 Ver 1.3） |
| 6 | `roland_jc22` 的 REVERB 與 `dsm_dumblifier` 的 Input Boost 應收進 controls 區塊 | **已收進** |
| 7 | 「controls 是否包含內部微調項」的標準應在資料庫層級明文定義 | **已定義**，見 `CONTROLS_CONVENTION.md` |

### 缺口 3 為什麼只補了一把

四把琴查過官方產品頁、原廠目錄與官方手冊。結果是：

- `fender_tokyo_thinline` — Fender 官方規格表明列三個檔位名稱。**已補進該檔**
- `esp_eclipse_ctm` — ESP 從產品頁到 20 頁的 OWNER'S MANUAL 都只標開關型態（Toggle PU Selector），全書不命名檔位
- `esp_throbber_ctm` — 同上，而且這個型號在 ESP 官網搜尋不到
- `greco_te500` — 1976 與 1979 兩份原廠目錄都只寫「3回路切替スイッチ」「3段切替スイッチ」

三把查不到的已在各自的 spec YAML 標成 `positions: null`，並列出**查過哪些來源**。那是查證結果，不是還沒查。**不要用「雙 humbucker 的 3-way 就是 Neck/Both/Bridge」這種常識推論填空。**

## 三處衝突已由使用者確認實機結案（2026-09-11）

查證時發現三處官方規格與本庫記載不符。使用者確認實機後，三處全部結案。

| # | 原本的衝突 | 實機確認結果 | 處置 |
|---|---|---|---|
| 1 | `esp_throbber_ctm` 寫 3-way，ESP 目錄機種 THROBBER 是 5-Way | **是 ESP THROBBER，5 檔** | 本庫改為 `5-Way Lever PU Selector` |
| 2 | `esp_eclipse_ctm` 列兩顆 Tone，ESP 官方寫 Master Tone 一顆 | **面板三顆旋鈕，Tone 一顆** | 本庫 controls 改為 `Tone (共用)` |
| 3 | `fender_tokyo_thinline` 的拾音器三方不一致 | **Seymour Duncan SP90-1 Set (SP90-1 + SP90-1N)** | spec 移除「或 Lollar」的模糊寫法；inventory 的「Momose VT-1」是另一把琴的規格誤植，已更正 |

### 型號識別：Throbber 保留舊名

**實機型號是 ESP Original Series THROBBER-STD**（2026-09-12 使用者確認）。
ESP 沒有「Throbber-CTM」這個型號——現行產品線只有 THROBBER-STD 與 TB SOLID 系列。

`basic_info.model` 已改為 `THROBBER-STD`，並加 `aliases: ["Throbber-CTM", ...]` 保留舊稱。
同一筆的琴身／琴頸／指板／硬體原本與官方七個欄位全部不符，也已照官方更正。

本庫**沒有改 id 與型號名稱**。`esp_throbber_ctm` 與「Throbber-CTM」這個字串散在
Pedal-Research 41 個檔案、Pedal-Web-Service-Planning 7 個檔案，改名的波及範圍遠大於收益。
實機型號記在 `guitars/specs/esp_throbber_ctm.yaml` 的 `model_identity` 區塊。

**比對官方規格時用現行頁面：**

- 索引：`https://espguitars.co.jp/products/throbber`
- 產品頁：`https://espguitars.co.jp/product/2873/`、`https://espguitars.co.jp/product/2874/`

2026-09-12 由本庫親自開啟逐字核對的 THROBBER-STD 規格：

```
BODY          Alder (Sound Reservoir) w/Ivory Binding (Thickness 45mm)
NECK          Hard Maple (CT System Head Type-3)
FINGERBOARD   Indian Rosewood
SCALE         648mm
FRET          M-SS, 22frets
CONSTRUCTION  Bolt-on (T-5 Ultimate Access)
BRIDGE        ESP FIXED Bridge
PICKUPS       (Neck) Seymour Duncan APH-1n, (Bridge) Seymour Duncan TB-APH-1b
CONTROLS      Master Volume, Master Tone, 5-Way Lever PU Selector
PRICE         616,000 yen (without tax: 560,000 yen)
```

不要用副牌 Edwards 的 E-THROBBER-CTM，那是不同型號。
**也不要用 `espguitars.co.jp/original/throbber/throbber.html`**——理由見下一節。

### Throbber 的兩項後續已結案，且與現行官方規格相符（2026-09-12）

| 項目 | 實機 | 現行官方 THROBBER-STD |
|---|---|---|
| 旋鈕數量 | 兩顆：Master Volume + Master Tone | 相同 |
| 檔數 | 5 檔撥桿 | 相同 |
| 拾音器 | Seymour Duncan APH-1n / TB-APH-1b | 相同 |

本庫原記四顆旋鈕與 3-way，皆已更正。

### 這一組衝突查證時犯了三個錯，值得記住

**第一個**：把反駁 agent 的保留丟掉了。原始研究的反駁 agent 把那條主張從 `high`
降級為 `medium`，理由是「ESP Throbber 家族一律 5 檔」屬三樣本的全稱化。
本庫採用了它的值，沒有把它的保留一起帶進來。

**第二個**：把推論寫成結論。當時寫下「所以這把的拾音器是換過的」，
那需要兩個沒有證據的前提。已更正。

**第三個，也是最隱蔽的**：**引用了一個能開、引文逐字正確、但已經作廢的頁面。**

`https://espguitars.co.jp/original/throbber/throbber.html` 是 2021 年以前舊機種的
廢棄頁，ESP 網站首頁沒有任何入口或路徑到得了它。它列的 PICKUPS 是
ESP Custom Lab CL-P-H-2n / CL-P-H-2b、PRICE 470,000yen。

頁面開得起來，引文我親自核對過逐字無誤——**但它不是現行規格**。
本庫因此推導出一個根本不存在的落差（「實機拾音器與官方不同」），
再從那個落差推導出「可能被換過」。改用現行頁面後，落差整個消失。

### 查外部規格的第三層：來源時效

`HANDOFF.md` 記了跨 repo 路徑查證的兩層（空間、時間）。查外部設備規格還有第三層：

1. **來源可及性**：URL 打得開、引文逐字對得上
2. **型號正確性**：那一頁講的確實是這個型號，不是同系列的別款
3. **來源時效**：**那一頁是不是現行的？**

第三層最容易漏，因為前兩層都會通過。判斷方法：

- 從廠商網站的**產品索引頁**點進去，確認那個 URL 真的在現行導覽裡
- URL 結構本身是線索。`/original/<系列>/<型號>.html` 這種舊式靜態路徑，
  與 `/products/<系列>` + `/product/<數字 id>/` 這種現行結構不同
- 現行索引頁沒有列出的型號，八成是已停產款

**廢棄頁面不要刪掉引用，要標成 deprecated 並寫明為什麼不能用**，
否則下一個人會再撿回去。本庫在 `guitars/specs/esp_throbber_ctm.yaml`
的 `deprecated_source` 區塊示範了這個寫法。

### 還有第四件事：來源是不是同一間公司

2026-09-12 補上。ESP JP（`espguitars.co.jp`）與 ESP USA（`espguitars.com`）
是**兩間獨立公司**，產品線不對應。本庫一度拿美國站的規格當日本站型號的佐證。

這類「品牌層級、查證前必須先知道」的事記在 `BRAND_NOTES.md`。
**查任何品牌的官方規格之前先看那一份。**

它也記了一個 grep 抓不到的坑：整個 repo 沒有任何 `espguitars.com` 的 URL，
但 ESP USA 的引用確實存在——以中文字串「美國官方站」與零售商商品頁的形式存在。
單純 grep 網域會回報乾淨。

## 官方文件自己矛盾、兩面都要記的地方

以下每一組的兩種說法都是官方原文。本庫不代為取捨，兩面都記。

| 設備 | 矛盾 |
|---|---|
| `ff1y` | 延遲時間上限：參數表 10.0 s vs 正文 9,999 msec |
| `ff1y` | TRAIL 預設值：參數表 Off vs 正文「On (default)」 |
| `ff1y` | EQ 低頻段命名：正文與參數表用 BASS，Preset Parameter Sheet 用 EQ LOW |
| `empress_buffer_plus_plus` | fsw function 撥桿的有效範圍：手冊 p.2 寫 Modes 1-6，p.5 與 Mode 6 專頁寫該撥桿在 Mode 6 無作用 |
| `odl1cs` | 電池型號：EN 規格表印 6F22（錳鋅編號），JP 印 6LF22（鹼性編號） |

## 補齊後仍然查不到的項目

這些是官方從未公布的，不是還沒查。各設備的 spec YAML 都有 `unknown` 或 `need_verification` 欄位記載：

- `odl1cs` — 七個控制**全部沒有數值範圍**（轉折頻率、增益量、位準量皆未公布）
- `empress_buffer_plus_plus` — 外接開關要插哪個孔，手冊、產品頁、面板圖三者皆無
- `cali76_fet` — 官方從未使用 continuous／stepped／detented 任一字眼。「RATIO 無段」是從 min/max 措辭推得的合理推論，不是引文
- `ff1y` — EQ 頻率點沒標單位（推定 Hz）；MODULATION 的 RATE 沒有 Hz 或 BPM 對照；TONE 的濾波器型態未說明
- 四把吉他 — 都沒有任何官方文件提到面板上印有檔位字樣

## 順帶修正的兩處

1. **`odl1cs` 的電池支援**：原本寫「不支援電池 (高電流消耗)」，官方 CS 手冊明寫可用 9V 鹼性電池約 3 小時。已改。
   **注意**：同檔 `related_models.odl_1a_cs` 的「不支援電池」是**對的**（ODL-1A-CS 耗流 120mA，官方明文不支援），不要一起改。
2. **`cali76_fet` 的尺寸**：原本寫「約140x76x51mm / 類似Boss尺寸」，官方為 124 x 64 x 58 mm、553 g。已改，並移除 Boss 尺寸比喻（Boss compact 約 73 x 129 x 59 mm，軸向與數值都對不上）。

## 抽取過程中修正的三處

審查 agent 逐行反查原檔後抓到，已在本文件中修正：

1. **一處捏造** — `morning_glory` 的 Bright Cut Toggle 檔位被寫成 `Off (關閉)`／`On (開啟)`。原檔只有裸的「關閉」「開啟」，而且是寫在 `bright_cut` 區塊的 `left_off.setting` 與 `right_on.setting`，不是 control 條目裡的選項列表
2. **行號偏移** — `tone_king_imperial_mkii` 的 lead channel controls 是 77-81 行，不是 78-82
3. **路徑錯誤** — `roland_jc22` 的 `controls:` 是頂層鍵（第 48 行），不在 `technical_specs` 底下（`technical_specs` 的最後一個子項 `power_consumption` 在第 45 行結束）

26 份檔案全數涵蓋，無遺漏。抽取結果中沒有出現越權的 schema 設計。
