# 工作紀錄：2026-10 Imperial MKII 耳機訊號鏈

**用途**：context compact 之後接續工作用。50% context 時由 Semi 收尾更新。
**開始**：2026-10-13

## 使用者需求（原文要點）

新訊號鏈，依序：

1. Free the Tone PA10G（使用者確認 = 現有 PA-1QG）
2. Origin Effects Cali76 Stacked Compressor（與現有 Cali76 FET 不同型號）
3. Device2 From Yesterday
4. JHS NotADumble V2
5. Virtues Arca
6. Device2 RAAT（手工訂製，只做 3 顆。參考 `docs/RAAT-Research.md`）
7. Lichtlaerm Audio As Above So Below
8. Hologram Chroma Console
9. Free the Tone FF-1Y

前提：

- 每個單元都會疊加使用。**例外：5 Arca 與 6 RAAT 不會同時開**（兩種情況各自準備）
- 輸出：Tone King Imperial MKII 當 pedal platform，耳機 + 內建 cab sim。沒有其他音箱
- 沒有 Swiss Things／Buffer++，沒有接 FX loop，全部串在前級
- 不在這條鏈裡的效果器都還留著（Empress MKII、Cali76 FET、Sweet Honey、Horsemeat、Morning Glory、Blacklon、Source Code、ODL-1-CS、Nucleo、Buffer++ 為 planned）
- 目標音色：沿用 `music_styles.yaml`（Neo Soul、Post Rock、Blues、Jazz 等），**新增 J-Rock/J-Pop 與器樂搖滾**

RAAT 與 ProCo RAT 的差異（使用者口述）：

- a) 內建 Ruetz Mod，做成旋鈕：0 = stock，全開 = Ruetz
- b) 有 Turbo RAT 一樣的 Filter 旋鈕
- c) 切換器：Ge／LEC／Si 三種 clipping

要回答的三個問題：

- A. 是否符合目標音色
- B. 功能重疊或不建議的搭配
- C. 搭配器材庫 5 把吉他會不會有問題

## Context Watchdog

- statusLine 外包腳本：scratchpad `ctx-statusline.sh`，已接到 `.claude/settings.local.json`（該檔被追蹤進 git，**工作結束後要還原 statusLine 欄位，不要 commit**）
- 背景監看：Bash 背景工作，到 50% 時通知 → 更新本檔

## 進度

- [x] 2026-10-13 Arca、From Yesterday 加回 inventory（「待新訊號鏈指派」區塊）
- [x] 前置檢查：本庫狀況表（見下）
- [x] 階段 1：研究 6 台（PA-1QG 使用者確認相同，不研究）。workflow `wf_f3df9fbb-2f6` 完成，12 agent 0 失敗
  - 新 spec：`origin_cali76_stacked.yaml`、`jhs_notadumble_v2.yaml`、`hologram_chroma_console.yaml`、`device2_raat.yaml`
  - 重寫：`from_yesterday_kot.yaml`（Device2，台灣品牌為推論）、`virtues_arca.yaml`（translucent OD，非 BB）
  - 兩份舊 report 加了過期橫幅
  - 意外發現：RAAT 有官方頁（Device2 2026-01 批次 "RAAT" Ultra Spec With uPC156A，TWD 7,800）
- [x] 階段 2a：inventory 更新（19 條目、18 active；新增 `active_signal_chain` 區塊；V3 的 signal_routing 保留為歷史）；`project_meta.yaml` 快取已更新
- [x] 階段 2b：訊號鏈文件由階段 3 的 synthesizer 寫出；`signal_chains/README.md` 已標明新鏈是現況
- [x] 階段 3：A/B/C 分析 + 訊號鏈 YAML/MD（7 agent 0 失敗，critic 一輪）。workflow runId `wf_b63c075c-70f`（task `ww7cejucr`）
  - scriptPath：`~/.claude/projects/-Users-emilwu-VSCode-PedalGuy-Pedal-Research-projects-2025-v3-signal-chain/188dbc7c-e574-4716-a746-456032587fcc/workflows/scripts/signal-chain-analysis-2026-10-wf_b63c075c-70f.js`
  - 3 分析 → 各 1 critic（一輪）→ 1 synthesizer。草稿在 scratchpad `analysis/`
  - 產出：`signal_chains/signal_chain_2026-10_imperial_headphone.yaml` 與 `signal_chains/signal_chain_2026-10_imperial_headphone.md`
- [x] `signal_chains/README.md` 已更新
- [x] HANDOFF.md 新增「2026-10-13 做了什麼」，含跨 repo 待辦
- [x] 還原 settings.local.json 的 statusLine，停止 context watchdog

## 本庫狀況（前置檢查結果）

| # | 效果器 | 狀況 |
|---|---|---|
| 1 | PA-1QG | 已有 spec 與 inventory |
| 2 | Cali76 Stacked | 沒有，要新增 |
| 3 | From Yesterday | inventory 有；spec `from_yesterday_kot.yaml` 寫的是 KOT 代理資料，要重寫（保留 id，改 brand/model，加 aliases） |
| 4 | NotADumble V2 | 沒有，要新增 |
| 5 | Arca | inventory 有；spec 沒有官方來源，要查證 |
| 6 | RAAT | 沒有，要新增 |
| 7 | AASB | 已有 |
| 8 | Chroma Console | 沒有，要新增 |
| 9 | FF-1Y | 已有 |
| — | Imperial MKII | 已有（`amps.yaml`） |

## 使用者的工作方式指示（2026-10-13 中途追加）

- 挑錯（adversarial verify）要有限度：**最多兩到三輪**。超過就停，回頭檢討計畫為什麼派這麼多人
- 對訊號鏈影響不大、枝微末節的問題**現在不處理**，列成待確認清單，之後實際測試就會知道
- 目標是先完成**整條訊號鏈的第一版架構**

## 執行中的 workflow

- 階段 1 研究：runId `wf_f3df9fbb-2f6`，task `wr45jix3k`
  - scriptPath：`~/.claude/projects/-Users-emilwu-VSCode-PedalGuy-Pedal-Research/188dbc7c-e574-4716-a746-456032587fcc/workflows/scripts/pedal-spec-research-2026-10-wf_f3df9fbb-2f6.js`
  - 結構：6 個研究 agent → 每個 1 個驗證 agent（只一輪）
  - 恢復：`Workflow({scriptPath, resumeFromRunId: "wf_f3df9fbb-2f6"})`
- Context watchdog：背景 task `betk5vrxi`
- RAAT 的「LEC」視為 LED（`docs/RAAT-Research.md` 用 LED），報告裡要提一句

## 決定

- 新訊號鏈文件放在 `projects/2025-v3-signal-chain/signal_chains/`（inventory 在此專案）
- From Yesterday 與 Arca 已在 production（Planning `006_seed_from_research.sql`）。改 brand/model 會造成下次 `/migrate-data` 多插一列。只在 HANDOFF 記錄，不改別的 repo

## 產出檔案

- 報告：`signal_chains/signal_chain_2026-10_imperial_headphone.md`
- 鏈定義：`signal_chains/signal_chain_2026-10_imperial_headphone.yaml`
- 新 spec：`shared/equipment_database/pedals/specs/` 下 `origin_cali76_stacked`、`jhs_notadumble_v2`、`hologram_chroma_console`、`device2_raat`
- 重寫 spec：`from_yesterday_kot`、`virtues_arca`（兩份 report 加過期橫幅）
- inventory、`project_meta.yaml`、`signal_chains/README.md`、`HANDOFF.md`
- 全部未 commit（使用者沒有要求）。`docs/` 是使用者自己的未追蹤目錄，不是本次產出

## 下一步（使用者醒來後）

- 看報告的「待實測確認」前兩條：Cali76 DC 孔標示、RAAT 電源。決定電源方案
- 實測後回填 spec 的 [unknown] 值
- 決定是否 commit
- 採用報告「可選的調整」第 4 項（FX loop）之前，先用 Tone King 官方手冊重新查證 `tone_king_imperial_mkii.yaml`：該 spec 沒有證據等級，FX loop 的描述前後矛盾
- AASB 是單聲道還是立體聲：`aasb.yaml` 與 Imperial spec 的接線範例矛盾，報告暫依 `aasb.yaml`（單聲道）

## 2026-10-13 凌晨：使用者回覆與後續處理

使用者回覆 6 點：

1. Cali76 是 2025 現行款 → 已寫入報告、鏈 YAML、spec（`model_identity.user_confirmed`）、inventory
2. 授權 Research 處理 production 錯誤資料的通知
3. AASB 是單聲道 → 已寫入報告、鏈 YAML、`aasb.yaml`
4. Imperial MKII 輸入單聲道，Send／Return 與輸出立體聲，四線法沒問題 → 報告「可選的調整」第 4 項改為已確認可行；`tone_king_imperial_mkii.yaml` 加 `user_statement_2026_10_13`（spec 寫 mono send，與使用者說法不一致，未核對官方手冊）
5. Chroma Console 的 Character 模組基本不用 → B-4、B-6 對應段落已更新
6. 通知網站更正 → 用 Herdr 開 Pedal-Web-Service 的 Claude session（agent `pedal-website`，pane `w1:p2`），已傳送更正需求，要求 production 寫入前等使用者確認

追加第 7 點：AASB 疊 Chroma 時 Chroma 只用 Texture；單用 Chroma 時才可能用 Movement／Diffusion／Texture；Character 一律不用 → 報告 B-4、B-6、文末確認表與鏈 YAML 已更新。

報告文末新增「2026-10-13 使用者確認」一節。

