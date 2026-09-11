# 控制項分類標準

**適用範圍**：`shared/equipment_database/` 底下所有 spec YAML。
**建立日期**：2026-09-11
**解決的問題**：`PARAMETER_VOCABULARY.md` 的資料缺口第 7 項——「controls 是否包含內部微調項」這條分界線過去只是逐檔的隱性假設，資料庫層級從未明文定義。

---

## 一句話版本

**看使用者要付出什麼代價才能調到它。** 伸手可及的進 `controls`，要拆機殼的進 `internal_controls`，只能接電腦改的進 `software_controls`。

---

## 三個區塊的分界

| 區塊 | 收什麼 | 判斷標準 | 既有範例 |
|---|---|---|---|
| `controls` | 演奏或設定時伸手可調的控制項 | **不需要工具、不需要拆開機殼**。前面板與後面板都算。 | 絕大多數 spec 檔 |
| `internal_controls` | 需要打開機殼才能調整的項目 | 要拆螺絲、拆底板，或要用螺絲起子撥的 DIP switch、trimpot、跳線 | `pedals/specs/from_yesterday_kot.yaml` 的 `internal_controls:` 區塊 |
| `software_controls` | 只能透過廠商軟體編輯的參數 | 實體面板上沒有對應的旋鈕或開關 | `amps/specs/tone_king_imperial_mkii.yaml` 的 `software_controls:` 區塊 |

三個區塊都是選用的。設備沒有該類控制項時就不要建立空區塊。

---

## 為什麼用「拆不拆機殼」當分界

這條線切在使用者體驗的真實斷點上，不是切在電路設計上。

- `controls` 的項目會在一次演奏中被調整。
- `internal_controls` 的項目通常一輩子只設定一次。
- `software_controls` 的項目需要另外準備一台電腦與一條線。

三者的更動頻率差了好幾個數量級。混在同一份清單裡會讓讀者以為它們同樣容易調整。

---

## 怎麼判斷一個控制項該進哪一區

依序回答，第一個「是」就決定歸屬：

1. **要打開機殼嗎？** → 是，進 `internal_controls`。
2. **要接電腦或裝軟體嗎？** → 是，進 `software_controls`。
3. **其他全部** → 進 `controls`。

後面板的控制項走第 3 條，進 `controls`。請額外加一行 `location: "rear_panel"` 標示位置。範例見 `amps/specs/dsm_dumblifier.yaml` 的 Input Boost Switch。

---

## 一個控制項只能出現在一個 controls 區塊

同一個實體旋鈕不要在兩個 controls 區塊各寫一次。

但是控制項可以在**非 controls 的描述性區塊**被再次提及。這種情況很常見，而且合理：

- `amps/specs/roland_jc22.yaml` 的 REVERB 旋鈕收在 `controls.reverb`，同時也在 `built_in_effects.reverb` 被提到。
- `amps/specs/dsm_dumblifier.yaml` 的 Input Boost Switch 收在 `controls.global_controls`，同時也在 `connectivity.inputs` 被列出。

這兩處都加了註解互指。**新增這種交叉引用時請比照辦理**，否則下一個讀者會以為那是兩個不同的控制項。

---

## controls 清單不保證完整

即使照這份標準寫，`controls` 清單也**不等於該設備全部可調項目的完整枚舉**。

原因是來源資料本身可能就沒寫。廠商規格頁常常只列主要旋鈕，略過後面板開關。

因此下游不可以假設「不在 controls 裡」等於「這台設備沒有這個控制項」。這是 `PARAMETER_VOCABULARY.md` 限制 C9 的內容，這份文件不推翻它，只是把分類標準補上。

---

## 怎麼檢查有沒有漏網之魚

不要在這份文件裡列「目前哪幾檔不符合」的清單。那種清單寫下的當下就開始腐壞。

改用這個指令找出「提到了內部調整、但可能沒收進 `internal_controls`」的檔案：

```bash
cd /Users/emilwu/VSCode/PedalGuy/Pedal-Research/shared/equipment_database
grep -rn -i -E 'trimpot|trim pot|dip.?switch|內部.{0,4}(開關|微調|跳線|切換)' \
  --include='*.yaml' . \
  | grep -v 'internal_boost' \
  | grep -v 'internal_voltage'
```

逐條看輸出：

- 命中的行在 `internal_controls:` 區塊裡 → 正確，跳過。
- 命中的行在別的區塊（例如 `special_features`、`bypass`、`buffer_function`）→ 該項目要補進 `internal_controls`，原處保留並加註解互指。

兩個 `grep -v` 濾掉的是內部升壓電壓，那是電路規格不是控制項。

---

## 相關文件

- `PARAMETER_VOCABULARY.md` — 26 台設備的可調參數詞彙，以及十條資料事實構成的限制。限制 C9、C10 與這份標準直接相關。
