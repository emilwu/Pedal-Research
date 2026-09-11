# 2025 V3 訊號鏈優化專案

**專案建立日期:** 2025-12-22 ~ 2025-12-30
**專案狀態:** 已完成 ✅
**專案目標:** 優化吉他效果器訊號鏈，建立兩條主要訊號鏈配置

---

## 專案概述

這是 Emil 的吉他效果器盤點與訊號鏈優化專案第三版。專案聚焦於：

1. **完整盤點所有設備**
   - 4 把吉他（ESP Eclipse CTM, ESP Throbber-CTM, Greco TE-500, Fender Tokyo Thinline）
   - 12 顆效果器（2 Compressors, 1 EQ, 6 Overdrives, 1 Delay, 2 Reverbs，依 `inventory/pedals.yaml` stats 核實）
   - 2 台音箱（Tone King Imperial MKII, Roland JC-22）

2. **設計兩條主要訊號鏈**
   - **訊號鏈 1**: Jazz / Neo Soul / Funk 專用（搭配 Roland JC-22）
   - **訊號鏈 2**: Post Rock / Fusion / Ambient 專用（搭配 Tone King Imperial MKII）

3. **Swiss Things 路由器整合**
   - Loop 1: 破音效果器（Unbuffered）
   - Loop 2: 空間效果器（Buffered）
   - 4-Cable Method 應用

---

## 專案成果

### 主要文件

> 以下六份原本是 V3.0 專案完成時（2025-12-30）的當時文件，**均已歸檔**，實際檔名與 120-126 行一致；此處補上完整路徑，勿再用舊檔名尋找。

#### 分析報告（analysis/，已歸檔）
- `archived_versions/analysis/comprehensive_analysis_summary_v2.0_dual_amp_archived.md` - 完整分析報告，包含所有設備技術資料、配對分析、訊號鏈建議（基於雙音箱配置，已被 2026-01-08 的 Toneking Only 配置取代）
- `archived_versions/analysis/signal_chain_master_plan_v1.0_archived.md` - 訊號鏈總計畫（V1.0，已被後續版本取代）
- `archived_versions/analysis/swiss_things_integration_plan_v2.0_dual_amp_archived.md` - Swiss Things 整合計畫（已由 Empress Buffer++ 方案取代）

#### 訊號鏈配置（signal_chains/，V3.0 版本已歸檔）
- `archived_versions/signal_chains/signal_chain_v3.0_dual_amp_archived.md` - V3.0 雙音箱版訊號鏈配置（2025-12-30 建立；已於 2026-01-08 被 Toneking Only 配置取代，且 2026-03-09 又新增了另一種設計，詳見下方「專案後續更新」）
  - 訊號鏈 1: Empress MKII → PA-1QG → Sweet Honey → PRS Horsemeat → JC-22 → FF-1Y → Nucleo
  - 訊號鏈 2: Cali76 FET → PA-1QG → Roshi Blacklon → Morning Glory → TWA Source Code → ODL-1-CS → Imperial → FF-1Y → AASB → Nucleo
- `archived_versions/signal_chains/signal_chain_diagrams_v3.0_dual_amp_archived.md` - 訊號鏈流程圖（原始檔名為 `signal_chain_diagrams_v2.md`，但內容其實是 V3.0，命名為歷史遺留問題，見 `archived_versions/README.md`）

#### 技術研究（research/）
- `compressor_eq_spatial_effects_technical_data.md` - Compressor/EQ/空間系技術資料
- `guitar_amp_pairing_guide.md` - 吉他音箱配對指南
- `guitar_collection_analysis.md` - 吉他收藏分析
- `overdrive_pedals_technical_data.md` - 破音效果器技術資料
- `archived_versions/research/swiss_things_signal_routing_logic_archived.md` - Swiss Things 路由邏輯完整文件（已於 2026-01-02 被 Empress Buffer++ 方案取代）

---

## 關鍵決策記錄

### V3.0 版本變更（相較於 V2.0）

**移除效果器：**
- ❌ Cornerstone Colosseum ($380)
  - 理由：簡化訊號鏈，用單功能專用效果器取代雙通道設計

**新增效果器：**
- ✅ PRS Horsemeat（取代 Colosseum Klon Side）
  - 角色：訊號鏈1 的透明 Klon-style Boost
  - 特性：極度透明，增加中頻穿透力

- ✅ JHS Morning Glory V3（取代 Colosseum BB Side）
  - 角色：訊號鏈2 的 Bluesbreaker Overdrive
  - 特性：經典 BB 音色，無 clipping 問題

### 音樂風格優先順序

1. **Jazz** (最高優先) - 80% 使用率
2. **Neo Soul** - 70% 使用率
3. **Funk** - 60% 使用率
4. **Post Rock** - 40% 使用率
5. **Fusion** - 30% 使用率

### 使用情境

- **居家錄音:** 80%
- **練習:** 20%
- **現場演出:** 0%（不需考慮）

---

## 專案里程碑

- ✅ **2025-12-22**: 專案啟動，建立第一階段提示詞
- ✅ **2025-12-25**: 完成破音效果器技術資料收集
- ✅ **2025-12-27**: 完成 Compressor/EQ/空間系技術資料收集
- ✅ **2025-12-28**: 完成吉他與效果器配對分析
- ✅ **2025-12-29**: 完成訊號鏈 V2.0 設計（使用 Colosseum）
- ✅ **2025-12-30**: 完成訊號鏈 V3.0 設計（移除 Colosseum，新增 Horsemeat + Morning Glory）
- ✅ **2025-12-30**: 專案完成，整理歸檔

---

## 未來改進建議

### 短期（1-3 個月）
1. 實際測試 V3.0 訊號鏈配置
2. 微調 PA-1QG 預設設定
3. 測試 PRS Horsemeat 與 Sweet Honey 的疊加效果

### 中期（3-6 個月）
1. 考慮新增 Modulation 效果器（Chorus/Phaser）填補空白
2. 評估是否需要專用 Volume Pedal
3. 測試 Swiss Things 的 Expression Pedal 音量控制

### 長期（6-12 個月）
1. 考慮增加第三條訊號鏈配置（針對 Rock/Blues）
2. 評估是否需要 MIDI 控制系統整合
3. 建立完整的 Preset 管理系統

---

## 專案歸檔說明

此專案已於 **2025-12-30** 完成並歸檔。

所有相關檔案已整理至 `projects/2025-v3-signal-chain/` 目錄。

如需繼續此專案或建立基於此配置的新專案，請參考（這幾份後續已搬進 `archived_versions/`）：
- 2025-12-30 歸檔當下的訊號鏈配置: `archived_versions/signal_chains/signal_chain_v3.0_dual_amp_archived.md`
  （**不是最終版**。歸檔後 `signal_chains/` 仍持續有新設計加入，見下方「專案後續更新」）
- 完整技術分析: `archived_versions/analysis/comprehensive_analysis_summary_v2.0_dual_amp_archived.md`
- Swiss Things 配置邏輯: `archived_versions/research/swiss_things_signal_routing_logic_archived.md`

---

## 專案後續更新

### 🔥 2026-01-02: 重大設備規格修正與升級建議

**重大發現:**
- ✅ **Roland JC-22 規格修正** - 確認有 **Stereo FX Loop** (mono send, stereo L/R return)
- ✅ **Tone King Imperial 規格確認** - 確認有 **Stereo FX Return** + **Stereo XLR Outputs**
- ⚠️ **Swiss Things 限制** - Loop 2 是 **mono**，無法充分利用兩台設備的 stereo 能力

**升級建議:**
- 🔥 **強烈建議升級至 Empress Buffer++** ($299)
  - Buffer++ Loop 2 支援 **stereo**，可充分發揮 JC-22 和 Tone King 的 stereo 能力
  - 可完整利用 Nucleo stereo reverb
  - 2 inputs 可快速切換 4 把吉他
  - Input metering 避免 ESP Eclipse EMG 削波
  - 賣掉 Swiss Things (約 $200-250) 後實際支出僅 $50-100

**相關文檔:**
- 詳細分析: `/analysis/buffer_plus_plus_vs_swiss_things_comparison.md` v2.0
- 遷移指南: `/analysis/SIGNAL_ROUTING_MIGRATION_GUIDE.md`

### 🎸 2026-01-08: Tone King Only 配置

**新增配置:**
- 建立了單 preamp pedal 配置: `signal_chains/signal_chain_toneking_only.md`
- 使用 Empress Buffer++ Mode 5 實現雙訊號鏈切換
- 新增 Boss CE-2W 補償 JC-22 的 Dimensional Space Chorus
- 充分利用 Tone King Stereo FX Loop + XLR 錄音輸出

### 📁 2026-01-11: 專案文件整理與歸檔

**文件整理:**
- ✅ 歸檔 YAML Coverage Report 到 `archived_versions/analysis/yaml_coverage_report_2026-01-03_archived.md`
  - 記錄了 17 顆效果器 YAML 文件的 100% 覆蓋率達成
  - 任務已完成，歸檔作為專案完成記錄
- ✅ 確認所有專案文件組織完善
  - 活躍配置：`signal_chains/signal_chain_toneking_only.md`（**此為 2026-01-11 當時的狀態，2026-03-09 又新增了另一份設計，見下一則更新**）
  - 研究文件：`research/` (5 個文件)
  - 歸檔版本：`archived_versions/` (完整的版本演進歷史)

### 🆕 2026-03-09: 新增 JC-22 Front-End Stereo 訊號鏈設計

**新增檔案：**
- `signal_chains/signal_chain_jc22_frontend_stereo.md`（含同名 `.yaml`），由 commit `062cf75` 加入
  - git commit 日期為 **2026-03-09**；檔案內部標注的 `Created` 欄位寫的是 2026-01-27，兩個日期不一致，以 git commit 記錄為準
- 標示版本為 v1.0，適用曲風為 Neo-Soul / Post-Rock，搭配吉他為 ESP Throbber-CTM / Greco TE-500

**與既有設計的差異（僅陳述事實，不判斷何者為現行版本）：**
- 音箱只用 **Roland JC-22**（不含 Tone King Imperial，與 2026-01-08 的 Toneking Only 配置不同；也不是雙音箱，與已歸檔的 V3.0 不同）
- 採 **Front-End Stereo** 接法：效果器分兩段接進 Empress Buffer++（Loop 1 為單聲道 dynamics/drive、Loop 2 為立體聲空間效果），最終直接接進 JC-22 的 stereo L/R front inputs，不經過音箱的 FX Loop
- 只有**一條**訊號流程，不像 Toneking Only 配置用 Buffer++ Loop 1/2 切換兩種音樂風格的訊號鏈

**目前狀態：** 本專案於 2025-12-30 已宣告「完成並歸檔」，但 `signal_chains/` 目錄在那之後仍持續有新設計加入（2026-01-08 的 Toneking Only、2026-03-09 的 JC-22 Front-End Stereo）。`signal_chains/` 下同時存在這兩份非歸檔設計，音箱配置與訊號路由方式互不相同。

**結論見 `signal_chains/README.md`（2026-09-11 新增）。**摘要：兩份都是提案，都不是現況——兩份的路由架構都建立在尚未購入的 Empress Buffer++ 上，Toneking Only 還額外需要一顆不在庫存的 Boss CE-2W 並要求賣掉仍持有的 JC-22。兩份設計互相排斥，而且都沒有提到對方。判斷方法與逐項依據在該檔。

---

**專案負責人:** Emil Wu
**AI 協作:** Claude Code (Sonnet 4.5)
**最後更新:** 2026-01-11
