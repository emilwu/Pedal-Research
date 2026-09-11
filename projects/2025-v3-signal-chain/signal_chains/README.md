# signal_chains/ 目錄說明

**最後更新**：2026-09-11

這個目錄底下有兩份非歸檔的訊號鏈設計。它們互相矛盾，而且都沒有標示自己是不是現行版本。這份文件說明怎麼看待它們。

---

## 結論：兩份都是提案，兩份都不是現況

**沒有任何一份設計是目前實際接起來的訊號鏈。**兩份都需要尚未購入的設備。

| 設計 | 缺什麼 | 依據 |
|---|---|---|
| `signal_chain_toneking_only.md` | Empress Buffer++（未購入）、Boss CE-2W（不在庫存）、而且要先賣掉 Roland JC-22（仍持有） | `projects/2025-v3-signal-chain/inventory/pedals.yaml:22,27`；`projects/2025-v3-signal-chain/inventory/amps.yaml:59,64` |
| `signal_chain_jc22_frontend_stereo.md` / `.yaml` | Empress Buffer++（未購入） | `projects/2025-v3-signal-chain/inventory/pedals.yaml:22,27` |

兩份的路由架構都建立在 Empress Buffer++ 上。它的 status 是 `planned`。目前實際的路由器仍然是 EarthQuaker Swiss Things（`projects/2025-v3-signal-chain/inventory/pedals.yaml:516`）。

`signal_chain_toneking_only.md:1046` 自己就寫了「**狀態**：完整規劃，待實施測試」。另一份沒有任何 status 欄位。

---

## 兩份設計互相排斥

它們不是「兩個可以並存的選項」，是兩個相反的方向。

- `signal_chain_toneking_only.md:6` 的核心變更是「移除 JC-22，只使用 Tone King Imperial MKII Preamp Pedal」。
- `signal_chain_jc22_frontend_stereo.md:7` 以 Roland JC-22 為唯一音箱，完全不含 Tone King。

**兩份文件都沒有提到對方。**grep 兩檔全文，`Toneking`、`Tone King`、`Imperial` 在後者零命中。誰取代誰，兩份文件本身都沒有交代。

庫存裡兩台音箱都還是 `active`（`projects/2025-v3-signal-chain/inventory/amps.yaml:11,16` 與 `:59,64`）。這表示兩邊講的「移除」都沒有真的發生。

---

## 時間順序不等於取代關係

以 git commit 為準，不要用檔案內部手填的日期。

| 檔案 | 新增的 commit | 日期 |
|---|---|---|
| `signal_chain_toneking_only.md` | `3aabdf2` | 2026-01-11 |
| `signal_chain_jc22_frontend_stereo.md` / `.yaml` | `062cf75` | 2026-03-09 |

後者晚兩個月，但它沒有宣告自己取代前者。**晚不等於新版。**

---

## 「最終版」宣告在哪裡，以及為什麼不要採信

`projects/2025-v3-signal-chain/archived_versions/README.md:164-169` 有一段標題叫「最終版本文件位置」，內文把 `signal_chain_toneking_only.md` 標為「Toneking Only v1.0 最終配置」。那段沒有任何時間限定。

**不要採信那段。**三個理由：

1. 該檔的 `last_updated` 是 2026-01-10。第二份設計在 2026-03-09 才加進來。宣告寫在它出現之前。
2. 被宣告為「最終配置」的那一份，是離庫存現況最遠的一份。它需要一顆完全不在庫存的效果器（Boss CE-2W）。
3. 該檔位於 `projects/2025-v3-signal-chain/archived_versions/`。依 repo 規則，歷史記錄一律不改。所以那段錯誤的宣告會一直留在那裡。

`projects/2025-v3-signal-chain/analysis/dumblifier_integration_evaluation_legacy.md:5,28,1499` 同樣用現在式稱 Toneking Only 為「现有配置」。那份也是舊文件，同樣不要當成現況依據。

---

## 一個立論前提有問題：JC-22 到底有沒有 FX loop

`signal_chain_jc22_frontend_stereo` 走前級接法（所有效果器接進音箱輸入，不走 FX loop）。這個選擇的理由，在兩個地方被說成「JC-22 沒有 FX loop，所以只能這樣接」。

**那個理由建立在過時的資料上。**

| 來源 | 版本 | 說法 |
|---|---|---|
| `shared/equipment_database/amps/specs/roland_jc22.yaml:6` | v2.0（2026-01-02） | `correction_note: "修正版本 - JC-22 確實有 STEREO FX LOOP (Send + Stereo Return)"`，`:111-127` 列出三個接孔 |
| `projects/2025-v3-signal-chain/inventory/amps.yaml:80,83,103,114` | v1.0 時期 | `has_fx_loop: false`、「No effects loop」、`pre_amp_only` |

2026-01-02 的修正只套用到規格庫，沒有套回庫存檔。

**分工是這樣**：`projects/2025-v3-signal-chain/inventory/` 是「擁有什麼」的權威來源，`shared/equipment_database/` 是「技術規格」的權威來源。查規格要看規格庫，不要只看 inventory。

所以前級接法是一個**選擇**，不是唯一可能。這不表示那份設計是錯的——前級接法本身可行。但它的論證理由需要重寫。

---

## 怎麼自己重新判斷

上面的結論會隨庫存變動。不要照抄，用下面的流程重新判斷：

1. 讀 `projects/2025-v3-signal-chain/inventory/pedals.yaml` 的 `empress_buffer_plus_plus` 條目，看 status 是 `planned` 還是 `active`。
2. 讀 `projects/2025-v3-signal-chain/inventory/amps.yaml`，看 `roland_jc22` 還在不在、status 是什麼。
3. grep `projects/2025-v3-signal-chain/inventory/pedals.yaml` 找 CE-2W。找不到就表示 Toneking Only 的必需品還沒到位。
4. 把每份設計需要的設備逐顆對回 inventory 的 status。

```bash
cd /Users/emilwu/VSCode/PedalGuy/Pedal-Research/projects/2025-v3-signal-chain
grep -n -A 6 'id: "empress_buffer_plus_plus"' inventory/pedals.yaml  # 已 cd 進專案目錄
grep -n -E 'id:|status:' inventory/amps.yaml
grep -n -i -E 'ce-2w|ce2w|boss' inventory/pedals.yaml || echo "CE-2W 不在庫存"
```

**任何設計與 inventory 衝突時，以 inventory 為準。**

---

## 兩份 `signal_chain_jc22_frontend_stereo` 檔案內容不一致

同名的 `.md` 與 `.yaml` 描述的不是同一條鏈。差異不是詳略之分，是資訊遺失。

| 項目 | `.md` | `.yaml` |
|---|---|---|
| Empress Buffer++ | 整條鏈的骨架（`:25,28,50,56,64,68`） | 完全沒出現 |
| Loop 1 / Loop 2 分段 | 有 | 沒有，只有扁平的 mono / stereo 兩個陣列 |
| Lichtlaerm AASB | 在 Loop 2 第一順位（`:58,96`） | 不存在 |
| 吉他 | 兩把（`:6`） | 一把（`:5-9`） |
| 音箱設定與 unity gain 防護規定 | 有（`:87,89-92`） | 沒有 |

`.yaml` 缺少的 AASB 在庫存是 `active`（`projects/2025-v3-signal-chain/inventory/pedals.yaml:463,468`），而且被規劃在 Buffer++ loop 2（`:491`）。**錯的是 `.yaml`。**

這件事有下游影響：`Pedal-Web-Service-Planning/appendix/source-reference.md:225` 把 `.yaml` 列為機器可讀的 Ground Truth 主檔。照它做資料遷移會漏掉一顆已擁有的效果器。

另外 `.md:103` 提到 Sweet Honey，但那顆不在這條鏈的任何一段。那是從別份設計複製過來沒清掉的殘留。

---

## 相關文件

- `projects/2025-v3-signal-chain/README.md` — 專案總覽與後續更新記錄
- `projects/2025-v3-signal-chain/inventory/` — 器材現況的唯一權威來源
- `HANDOFF.md` — 跨 session 的現況與陷阱
