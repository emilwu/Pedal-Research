# Skill: Inventory Manager

**Skill Name:** Inventory Manager
**Version:** 1.0
**Created:** 2025-12-30
**Purpose:** 管理動態設備清單（guitars, pedals, amps）

---

## Skill Role

你是 **Inventory Manager Skill**，負責管理 `projects/[current_project]/inventory/` 中的設備清單。

你提供以下功能：
1. 新增設備（Add）
2. 移除設備（Remove）
3. 更新設備資訊（Update）
4. 查詢設備清單（Query）

---

## Working Directory

```
Base Directory: /Users/emilwu/Projects/Pedal-Research
Inventory Path: projects/[current_project]/inventory/
```

---

## Operations

### Operation 1: Add Equipment (新增設備)

**觸發指令:**
- "新增吉他 [品牌] [型號]"
- "新增效果器 [品牌] [型號]"
- "新增音箱 [品牌] [型號]"

**Workflow:**

1. **解析指令**
   ```
   輸入: "新增效果器 Strymon BigSky"
   解析:
     - equipment_type: "pedal"
     - brand: "Strymon"
     - model: "BigSky"
   ```

2. **生成 ID**
   ```
   ID = brand_model_normalized
   範例: "strymon_bigsky"

   正規化規則:
   - 轉小寫
   - 空格改底線
   - 移除特殊字元（保留字母、數字、底線）
   ```

3. **檢查是否已存在**
   ```yaml
   # Read projects/[current_project]/inventory/[equipment_type]s.yaml
   # 搜尋是否有相同 ID

   if ID exists:
       回應: "⚠️ [品牌] [型號] 已在清單中！"
       詢問: "是否要更新資訊？(yes/no)"
       if yes → 執行 Operation 3: Update
       if no → 取消操作
   ```

4. **收集基本資訊（透過問答）**

   #### 對於吉他 (Guitar):
   ```
   Q1: 拾音器類型？
   1. Active Humbucker
   2. Passive Humbucker
   3. Single-coil
   4. P90
   5. Wide Range Humbucker
   6. Other

   Q2: 輸出等級？
   1. High (主動拾音器、高輸出)
   2. Medium (一般被動拾音器)
   3. Low (Vintage 風格)

   Q3: 琴身類型？
   1. Solid (實心)
   2. Semi-hollow (半空心)
   3. Hollow (空心)
   ```

   #### 對於效果器 (Pedal):
   ```
   Q1: 效果器類型？
   1. Compressor
   2. EQ
   3. Overdrive
   4. Distortion
   5. Fuzz
   6. Boost
   7. Delay
   8. Reverb
   9. Modulation (Chorus/Phaser/Flanger)
   10. Other

   Q2: 購買價格？(USD, 可選)
   ```

   #### 對於音箱 (Amp):
   ```
   Q1: 音箱類型？
   1. Tube (真空管)
   2. Solid-state (晶體)
   3. Hybrid (混合)
   4. Preamp only (前級)

   Q2: 是否有 FX Loop？
   1. Yes
   2. No
   ```

5. **建立基礎資料條目**

   #### Guitar YAML Entry:
   ```yaml
   - id: "[id]"
     brand: "[Brand]"
     model: "[Model]"
     full_name: "[Brand] [Model]"

     # 從問答收集
     pickup_type: "[user_input]"
     output_level: "[user_input]"
     body_type: "[user_input]"

     # 預設值
     status: "active"
     acquired_date: null
     research_file: null
     notes: "Added by Inventory Manager, awaiting detailed research"
   ```

   #### Pedal YAML Entry:
   ```yaml
   - id: "[id]"
     brand: "[Brand]"
     model: "[Model]"

     # 從問答收集
     type: "[user_input]"
     subtype: null

     status: "active"
     acquired_date: null
     price:
       amount: "[user_input or null]"
       currency: "USD"

     research_file: null
     notes: "Added by Inventory Manager, awaiting detailed research"
   ```

   #### Amp YAML Entry:
   ```yaml
   - id: "[id]"
     brand: "[Brand]"
     model: "[Model]"
     full_name: "[Brand] [Model]"

     # 從問答收集
     type: "[user_input]"
     has_fx_loop: "[user_input]"

     status: "active"
     acquired_date: null
     research_file: null
     notes: "Added by Inventory Manager, awaiting detailed research"
   ```

6. **更新 Inventory 檔案**
   ```
   - 讀取 projects/[current_project]/inventory/[equipment_type]s.yaml
   - 新增條目到 [equipment_type]s 列表
   - 更新 last_updated 欄位
   - 更新 stats 統計資訊
   - 寫回檔案
   ```

7. **詢問是否要建立詳細資料**
   ```
   ✅ [品牌] [型號] 已加入清單！

   是否要立即建立詳細技術資料？
   - 這會觸發 Research Agent 進行深度研究
   - 包含規格、音色特性、使用建議等

   建立詳細資料？(yes/no):
   ```

   - **If yes**: 觸發 `Pedal Research Agent` 並傳遞品牌、型號
   - **If no**: 完成

---

### Operation 2: Remove Equipment (移除設備)

**觸發指令:**
- "移除吉他 [品牌] [型號]"
- "移除效果器 [品牌] [型號]"
- "移除音箱 [品牌] [型號]"

**Workflow:**

1. **解析指令並生成 ID**
   ```
   輸入: "移除效果器 Strymon BigSky"
   ID = "strymon_bigsky"
   ```

2. **檢查是否存在**
   ```
   if ID not found:
       回應: "❌ 未找到 [品牌] [型號]"
       建議: "請檢查名稱是否正確，或使用 '查看清單' 指令查看所有設備"
       結束
   ```

3. **確認移除**
   ```
   ⚠️ 確認移除

   你即將移除:
   - 類型: [Type]
   - 品牌: [Brand]
   - 型號: [Model]

   此操作將從設備清單中移除此設備。

   確認移除？(yes/no):
   ```

4. **詢問是否保留研究資料**
   ```
   是否保留此設備的研究資料？

   - 保留: 研究資料檔案會保留在 shared/equipment_database/
            (以後重新購買可直接使用)

   - 刪除: 完全移除所有相關資料

   保留研究資料？(yes/no):
   ```

5. **執行移除**
   ```
   - 從 projects/[current_project]/inventory/[equipment_type]s.yaml 移除條目
   - 更新 last_updated
   - 更新 stats 統計資訊
   - 如果選擇刪除研究資料:
       - 刪除 shared/equipment_database/[type]/[id].yaml
       - 刪除相關 research 報告
   - 寫回檔案
   ```

6. **檢查受影響的訊號鏈配置**
   ```
   🔍 檢查受影響的訊號鏈...

   if 有訊號鏈使用此設備:
       顯示:
       ⚠️ 以下訊號鏈配置使用了此設備：

       1. [signal_chain_name_1]
       2. [signal_chain_name_2]

       這些配置現在標記為 outdated。

       是否要重新建立這些訊號鏈？
       1. 是，立即重建
       2. 否，稍後手動處理

       請選擇 (1/2):
   ```

7. **完成回應**
   ```
   ✅ [品牌] [型號] 已從清單移除

   更新後的設備統計：
   - [Type]: [N] 個 (之前: [N+1])
   ```

---

### Operation 3: Update Equipment (更新設備)

**觸發指令:**
- "更新吉他 [品牌] [型號]"
- "更新效果器 [品牌] [型號]"
- "更新音箱 [品牌] [型號]"

**Workflow:**

1. **解析指令並找到設備**
   ```
   if ID not found:
       回應: "❌ 未找到 [品牌] [型號]"
       結束
   ```

2. **顯示當前資訊**
   ```
   當前資訊：

   品牌: [Brand]
   型號: [Model]
   類型: [Type]
   狀態: [Status]
   [... 其他欄位 ...]

   請選擇要更新的欄位：
   1. 類型 (Type)
   2. 拾音器/規格
   3. 狀態 (Active/Sold/Stored)
   4. 價格
   5. 備註
   6. 取消

   請輸入欄位編號:
   ```

3. **根據選擇更新欄位**
   ```
   範例: 用戶選擇 2 (拾音器)

   新的拾音器型號:
   輸入 (或 'skip' 跳過):

   [更新對應欄位]
   ```

4. **詢問是否要觸發 Research Agent 更新**
   ```
   資訊已更新！

   是否要更新詳細技術資料？
   - 這會觸發 Research Agent 重新研究此設備
   - 生成新版本的資料檔案 (v[N+1])

   更新技術資料？(yes/no):
   ```

5. **更新 Inventory 檔案**
   ```
   - 更新對應條目
   - 更新 last_updated
   - 寫回檔案
   ```

6. **如果影響訊號鏈，標記為需重新評估**
   ```
   🔍 檢查受影響的訊號鏈...

   if 有訊號鏈使用此設備:
       在訊號鏈 YAML 中加入:
       needs_reevaluation: true
       reevaluation_reason: "[Equipment] specifications updated on [date]"
   ```

---

### Operation 4: Query Inventory (查詢清單)

**觸發指令:**
- "查看吉他清單"
- "查看效果器清單"
- "查看音箱清單"
- "查看所有設備"

**Workflow:**

1. **讀取對應 Inventory 檔案**

2. **格式化輸出**

   #### 吉他清單範例:
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🎸 吉他清單 (Guitars)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   總計: 4 把

   1. ESP Eclipse CTM
      - ID: esp_eclipse_ctm
      - 拾音器: EMG JH-B / JH-N (active_humbucker)
      - 輸出: High
      - 琴身: Solid
      - 狀態: Active ✅

   2. ESP Throbber-CTM
      - ID: esp_throbber_ctm
      - 拾音器: Seymour Duncan APH-1 (passive_humbucker)
      - 輸出: Medium
      - 琴身: Semi-hollow
      - 狀態: Active ✅

   3. Greco TE-500
      - ID: greco_te500
      - 拾音器: Lindy Fralin Wide Range
      - 輸出: Medium
      - 琴身: Semi-hollow Thinline
      - 狀態: Active ✅

   4. Fender Tokyo Thinline
      - ID: fender_tokyo_thinline
      - 拾音器: Momose VT-1 (single_coil)
      - 輸出: Medium
      - 琴身: Semi-hollow Thinline
      - 狀態: Active ✅

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   統計:
   - Active Humbucker: 1
   - Passive Humbucker: 1
   - Wide Range Humbucker: 1
   - Single-coil: 1

   輸出等級:
   - High: 1
   - Medium: 3

   最後更新: 2025-12-30
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

   #### 效果器清單範例:
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🎛️ 效果器清單 (Pedals)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   總計: 12 顆 | 總價值: $3,344 USD

   【Compressors (2)】
   1. Empress Compressor MKII ($219)
   2. Origin Effects Cali76 FET ($369)

   【EQ (1)】
   3. Free the Tone PA-1QG ($425)

   【Overdrives (5)】
   4. Mad Professor Sweet Honey Deluxe ($220)
   5. PRS Horsemeat ($ TBD)
   6. JHS Morning Glory V3 ($179)
   7. Roshi Blacklon ($200)
   8. TWA Source Code ($299)
   9. Free the Tone ODL-1-CS ($425)

   【Delay (1)】
   10. Free the Tone FF-1Y ($400)

   【Reverb (2)】
   11. Cornerstone Nucleo ($350)
   12. Lichtlaerm AASB ($225)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   按類型統計:
   - Compressor: 2
   - EQ: 1
   - Overdrive: 5
   - Delay: 1
   - Reverb: 2

   最後更新: 2025-12-30
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ```

---

## Error Handling

### 錯誤 1: YAML 解析失敗

```
if YAML parsing error:
    ❌ 錯誤：無法讀取 Inventory 檔案

    檔案: projects/[current_project]/inventory/[file].yaml
    錯誤: [error message]

    可能原因：
    - YAML 格式錯誤
    - 檔案損壞

    建議：
    1. 檢查檔案格式
    2. 使用 YAML validator 驗證
    3. 從備份恢復

    是否要嘗試自動修復？(yes/no):
```

### 錯誤 2: ID 正規化衝突

```
if normalized ID conflicts:
    ⚠️ ID 衝突

    嘗試新增: [Brand] [Model]
    生成 ID: [id]

    但此 ID 已被使用：
    現有設備: [Existing Brand] [Existing Model]

    請選擇：
    1. 使用替代 ID (例: [id]_2)
    2. 取消操作

    請選擇 (1/2):
```

---

## Integration Points

### 呼叫其他 Agent/Skill

1. **呼叫 Research Agent**
   - 當用戶選擇「建立詳細資料」時
   - 傳遞：品牌、型號、設備類型

2. **呼叫 Signal Chain Builder**
   - 當設備移除且影響訊號鏈時
   - 提供重建選項

---

## Output Files

此 Skill 會更新以下檔案：

- `projects/[current_project]/inventory/guitars.yaml`
- `projects/[current_project]/inventory/pedals.yaml`
- `projects/[current_project]/inventory/amps.yaml`

---

## Important Notes

1. **ID 正規化規則**
   ```
   原始: "Free the Tone PA-1QG"
   正規化: "free_the_tone_pa1qg"

   步驟:
   1. 轉小寫
   2. 空格 → 底線
   3. 移除特殊字元（保留英文、數字、底線）
   ```

2. **狀態值**
   ```
   - "active": 當前擁有且使用中
   - "sold": 已出售
   - "stored": 已購入但未使用（庫存）
   ```

3. **原子性操作**
   - 所有 YAML 更新應該是原子性的
   - 先讀取完整檔案 → 修改 → 寫回
   - 避免部分寫入導致損壞

---

**Skill 結束**
