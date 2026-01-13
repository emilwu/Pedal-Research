# Equipment Database 重構規劃

**日期**: 2026-01-13
**目標**: 分離技術規格（YAML）、研究報告（MD）、使用範例（Examples），建立清晰的目錄結構

---

## 問題分析

### 當前狀況
```
shared/equipment_database/
  pedals/
    *.yaml              # 17 個 YAML 規格檔
    examples/           # 1 個 MD 範例檔
    archived/           # 封存目錄
  guitars/
    *.yaml              # 4 個 YAML 規格檔
  amps/
    *.yaml              # 2 個 YAML 規格檔
  accessories/
    *.yaml              # 2 個 YAML 規格檔
```

### 問題點
1. ❌ **缺少 Markdown 研究報告** - Pedal Researcher 文檔要求產出，但實際未產出
2. ❌ **Examples 位置不一致** - 只有一個檔案在 `pedals/examples/`，無統一邏輯
3. ❌ **混合檔案類型** - YAML 與子目錄混在同層級，不易擴展
4. ❌ **Agent 文檔與實作不符** - 文檔說要產 MD + YAML，實際只產 YAML

### 設計原則
- **三種內容類型**：
  1. **Specs (YAML)** - AI 讀取的技術規格（跨專案共享）
  2. **Research (MD)** - 人類閱讀的研究報告（跨專案共享）
  3. **Examples (MD)** - 使用範例與設定（可選產出）

- **目錄原則**：
  - 器材類型為第一層（pedals, guitars, amps, accessories）
  - 內容類型為第二層（specs, research, examples）
  - 保持檔案命名一致性

---

## 新架構設計

### 方案 A：子目錄分層（推薦）

```
shared/equipment_database/
  pedals/
    specs/                    # YAML 規格檔（AI 讀取）
      cali76_fet.yaml
      sweet_honey.yaml
      ...
    research/                 # Markdown 研究報告（人類閱讀）
      cali76_fet_v1.md
      cali76_fet_v2.md        # 支持版本迭代
      sweet_honey_v1.md
      ...
    examples/                 # 使用範例（可選）
      cali76_fet_examples.md
      ff1y_examples.md
      ...
    archived/                 # 封存舊版（保持現有）
      ...

  guitars/
    specs/
      esp_eclipse_ctm.yaml
      ...
    research/
      esp_eclipse_ctm_v1.md
      ...
    examples/
      (可選)

  amps/
    specs/
      tone_king_imperial_mkii.yaml
      ...
    research/
      tone_king_imperial_mkii_v1.md
      ...
    examples/
      (可選)

  accessories/
    specs/
      rockboard_mod2_v2.yaml
      ...
    research/
      rockboard_mod2_v2_v1.md
      ...
    examples/
      (可選)
```

### 優點
- ✅ 清楚分離三種內容
- ✅ 保持器材類型聚合
- ✅ 支持版本迭代（research 可有多版本）
- ✅ 擴展性強（未來可加 reviews/, comparisons/ 等）
- ✅ 符合部分現有結構（examples, archived 已存在）

### 檔案命名規則

| 類型 | 檔名規則 | 範例 | 說明 |
|------|---------|------|------|
| **YAML Spec** | `[brand]_[model].yaml` | `cali76_fet.yaml` | 不含版本號，內部記錄版本 |
| **Research MD** | `[brand]_[model]_v[N].md` | `cali76_fet_v1.md` | 含版本號，支持迭代研究 |
| **Examples MD** | `[brand]_[model]_examples.md` | `cali76_fet_examples.md` | 不含版本號，持續更新 |

### 版本管理邏輯

#### YAML (specs/)
- 檔名**不含**版本號
- 版本資訊記錄在 `version` 欄位
- 更新時直接覆蓋檔案
- AI 總是讀取最新版本

#### Markdown (research/)
- 檔名**包含**版本號 `_v[N]`
- 每次更新建立新檔案（v1, v2, v3...）
- 保留歷史研究記錄
- 人類可查看演進過程

#### Examples (examples/)
- 檔名不含版本號
- 持續累積更新
- 可選產出（有實際使用範例時才建立）

---

## 遷移計劃

### Phase 1: 建立新目錄結構

```bash
# 為每個器材類型建立子目錄
for type in pedals guitars amps accessories; do
  mkdir -p shared/equipment_database/$type/specs
  mkdir -p shared/equipment_database/$type/research
  # examples 和 archived 已存在或按需建立
done
```

### Phase 2: 遷移 YAML 檔案

```bash
# 移動所有 YAML 到 specs/ 子目錄
cd shared/equipment_database

# Pedals
mv pedals/*.yaml pedals/specs/ 2>/dev/null

# Guitars
mv guitars/*.yaml guitars/specs/ 2>/dev/null

# Amps
mv amps/*.yaml amps/specs/ 2>/dev/null

# Accessories
mv accessories/*.yaml accessories/specs/ 2>/dev/null
```

**檔案數量**：
- Pedals: 17 個 YAML
- Guitars: 4 個 YAML
- Amps: 2 個 YAML
- Accessories: 2 個 YAML
- **總計**: 25 個 YAML 檔案

### Phase 3: 遷移 Examples

```bash
# 目前只有一個 example
# pedals/examples/FF-1Y_Examples.md 已在正確位置，無需移動
# 但需重新命名以符合新規則

mv pedals/examples/FF-1Y_Examples.md pedals/examples/ff1y_examples.md
```

### Phase 4: 建立初始 Research 報告（可選）

**選項 A：暫不建立**
- 等待 Pedal Researcher 未來執行時自動產出
- 優點：避免手動建立空檔案

**選項 B：建立佔位符**
- 為現有 25 個器材建立初始 MD 範本
- 內容標記為 "待研究" 或 "待補充"
- 優點：結構完整性

**建議：選項 A**（等待自然產出）

### Phase 5: 更新 Agent 文檔

**需要更新的檔案**：
1. `.claude/agents/1_pedal-researcher.md`
   - 更新輸出路徑：
     - YAML: `shared/equipment_database/[type]/specs/[brand]_[model].yaml`
     - MD: `shared/equipment_database/[type]/research/[brand]_[model]_v[N].md`
     - Examples: `shared/equipment_database/[type]/examples/[brand]_[model]_examples.md`

2. `.claude/skills/usage-examples-generator.md`
   - 更新輸出路徑到 `examples/` 子目錄
   - 統一檔名規則

**其他讀取 equipment_database 的檔案**：
- `.claude/agents/2_signal-chain-builder.md`
- `.claude/skills/guitar-pedal-pairing.md`
- 需要更新路徑為 `specs/` 子目錄

### Phase 6: 清理與驗證

```bash
# 確認 specs/ 目錄中的檔案
ls shared/equipment_database/*/specs/*.yaml

# 確認舊位置已清空（只剩子目錄）
ls shared/equipment_database/pedals/
# 應該只顯示：specs/, research/, examples/, archived/

# 確認 examples 檔案
ls shared/equipment_database/*/examples/*.md
```

---

## Examples 檔案邏輯

### 何時產生 Examples？

**由 Usage Examples Generator Skill 產生**，當：
1. 用戶明確要求產生使用範例
2. 器材已加入 inventory 並實際使用
3. 有具體的設定參數需要記錄

### Examples 內容

```markdown
# [Brand] [Model] - Usage Examples

## 場景 1: [Music Style / Use Case]

**目標**: [description]

### Settings
- [Control 1]: [value]
- [Control 2]: [value]
- ...

### Context
- Guitar: [model]
- Amp: [model]
- Position: [signal chain position]

### Notes
[實際使用心得]

---

## 場景 2: ...
```

### Examples 的更新策略
- 隨著實際使用持續累積
- 檔案內記錄 `last_updated` 日期
- 不使用版本號（持續更新同一檔案）

---

## 相關檔案路徑對照表

### 當前 → 新架構

| 當前路徑 | 新路徑 | 數量 |
|---------|--------|------|
| `pedals/*.yaml` | `pedals/specs/*.yaml` | 17 |
| `guitars/*.yaml` | `guitars/specs/*.yaml` | 4 |
| `amps/*.yaml` | `amps/specs/*.yaml` | 2 |
| `accessories/*.yaml` | `accessories/specs/*.yaml` | 2 |
| `pedals/examples/FF-1Y_Examples.md` | `pedals/examples/ff1y_examples.md` | 1 |
| (不存在) | `pedals/research/*.md` | 0 (待產出) |

### Agent 路徑更新

| Agent/Skill | 舊路徑引用 | 新路徑引用 |
|-------------|-----------|-----------|
| Pedal Researcher | `shared/equipment_database/pedals/` | `specs/`, `research/` |
| Signal Chain Builder | `shared/equipment_database/pedals/` | `specs/` |
| Pairing Skill | `shared/equipment_database/` | `specs/` |
| Usage Examples Generator | `pedals/examples/` | `examples/` |

---

## 風險評估

### 風險 1: 路徑斷裂
- **影響**: Agent 讀取不到 YAML 檔案
- **緩解**:
  - 在遷移前備份整個 `equipment_database/`
  - 逐步更新 Agent，測試後再遷移下一個
- **回滾**: 從備份還原

### 風險 2: 現有引用失效
- **影響**: 其他未列出的檔案可能引用舊路徑
- **緩解**:
  - 全局搜尋 `equipment_database/` 引用
  - 逐一檢查並更新
- **檢測**: `grep -r "equipment_database" .claude/`

### 風險 3: 檔名規則變更
- **影響**: FF-1Y_Examples.md → ff1y_examples.md
- **緩解**:
  - 確認無其他檔案硬編碼引用舊檔名
  - Examples 是新功能，影響範圍小
- **檢測**: `grep -r "FF-1Y_Examples" .claude/`

---

## 實施順序

### 推薦順序：

1. **Phase 1**: 建立新目錄結構（無破壞性）
2. **Phase 2**: 遷移 YAML 檔案到 `specs/`
3. **Phase 5**: 更新 Agent 文檔路徑
4. **Phase 3**: 遷移 Examples
5. **Phase 6**: 清理與驗證
6. **Phase 4**: （未來）自然產生 Research MD

### 時間估計

- Phase 1: 5 分鐘（建立目錄）
- Phase 2: 5 分鐘（移動 25 個 YAML）
- Phase 5: 20-30 分鐘（更新 Agent 文檔）
- Phase 3: 2 分鐘（重新命名 1 個 example）
- Phase 6: 5 分鐘（驗證）

**總計**: 約 40-50 分鐘

---

## 驗證清單

### 遷移後檢查

- [ ] 所有 YAML 檔案在 `specs/` 子目錄
- [ ] 舊位置（根目錄）只剩子目錄，無 YAML 檔案
- [ ] Examples 檔案符合新命名規則
- [ ] Agent 文檔路徑已更新
- [ ] Grep 搜尋確認無殘留舊路徑引用
- [ ] 測試 Pedal Researcher 執行（讀取 specs，產出 research）
- [ ] 測試 Signal Chain Builder 執行（讀取 specs）

### 功能測試

**測試場景 1: 讀取現有器材**
- 運行 Signal Chain Builder
- 確認可正確讀取 `specs/*.yaml`
- 確認配對邏輯正常

**測試場景 2: 研究新器材**
- 運行 Pedal Researcher
- 確認產出到 `research/[brand]_[model]_v1.md`
- 確認產出到 `specs/[brand]_[model].yaml`

**測試場景 3: 產生使用範例**
- 運行 Usage Examples Generator
- 確認產出到 `examples/[brand]_[model]_examples.md`

---

## 回滾計劃

### 備份點
- **路徑**: `Archived/equipment_database.backup-[date]/`
- **時間**: 遷移前建立
- **內容**: 完整的 `equipment_database/` 目錄

### 回滾步驟
```bash
# 如果需要回滾
rm -rf shared/equipment_database
cp -r Archived/equipment_database.backup-[date] shared/equipment_database
```

---

## 後續優化（未來）

### 可能的擴展

1. **Comparisons 目錄**
   - `pedals/comparisons/compressors_comparison.md`
   - 橫向比較同類型器材

2. **Reviews 整合**
   - `pedals/reviews/` 存放外部評測連結或摘要

3. **Tags/Categories**
   - 在 YAML 中增加 tags
   - 方便跨類型搜尋（如 "midi_controllable"）

4. **Visual Assets**
   - `pedals/images/` 存放器材照片、接線圖

---

## 進度追蹤

- [ ] Phase 1: 建立新目錄結構
- [ ] Phase 2: 遷移 YAML 檔案
- [ ] Phase 3: 遷移 Examples
- [ ] Phase 5: 更新 Agent 文檔
- [ ] Phase 6: 清理與驗證
- [ ] 提交與推送

**狀態**: 規劃完成，待執行

---

## 參考資料

- Pedal Researcher Agent: `.claude/agents/1_pedal-researcher.md`
- Usage Examples Generator: `.claude/skills/usage-examples-generator.md`
- Signal Chain Builder: `.claude/agents/2_signal-chain-builder.md`

