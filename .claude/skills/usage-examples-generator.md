# Skill: Usage Examples Generator

**Skill Name:** Usage Examples Generator
**Version:** 1.0
**Created:** 2026-01-11
**Purpose:** 根據 YAML 技術資料和 Research 文件，生成效果器實際使用範例文件

---

## Skill Role

你是 **Usage Examples Generator Skill**，負責將效果器的技術規格轉化為實用的使用範例文件。

**核心功能:**
1. 解析效果器 YAML 技術資料
2. 整合 Research 文件的資訊
3. 生成控制介面完整說明
4. 創建實際使用範例（針對不同音樂風格）
5. 提供設定建議與故障排除

**知識來源:**
- `shared/equipment_database/pedals/*.yaml` (技術規格)
- `projects/*/research/*.md` (研究文件)
- `.claude/knowledge/pairing_rules.yaml` (配對規則)
- `projects/[current_project]/inventory/music_styles.yaml` (音樂風格資料)

---

## Trigger Conditions

當滿足以下條件時，應該生成使用範例文件：

1. **新完成 YAML 技術資料收集** - 剛建立或更新某效果器的 YAML 檔案
2. **用戶明確請求** - "生成 [效果器] 使用範例"、"建立 [效果器] 範例文件"
3. **Research 文件完成後** - 完成深度研究後的延伸產出

---

## Input Format

```yaml
input:
  pedal_id: "ff1y"
  yaml_path: "shared/equipment_database/pedals/ff1y.yaml"
  research_path: "projects/2025-v3-signal-chain/research/compressor_eq_spatial_effects_technical_data.md"

  additional_context:
    user_music_styles:
      - "Jazz"
      - "Neo Soul"
      - "Post Rock"
      - "Ambient"

    user_guitars:
      - "ESP Throbber CTM"
      - "ESP Eclipse CTM"

    user_amps:
      - "Tone King Imperial MKII"
      - "Roland JC-22"

    signal_chain_context: "兩條訊號鏈共用，位於 FX Loop"
```

---

## Document Structure Template

### **完整範例文件應包含的章節：**

```markdown
# [品牌] [型號] - 使用範例與控制說明

**版本:** 1.0
**更新日期:** [date]
**資料來源:** [YAML 路徑]

---

## 目錄

1. [控制介面完整說明](#控制介面完整說明)
2. [實際使用範例](#實際使用範例)
3. [音樂風格設定指南](#音樂風格設定指南)
4. [進階技巧](#進階技巧)
5. [故障排除](#故障排除)

---

## 控制介面完整說明

### 主要旋鈕與按鈕

#### **[旋鈕/按鈕名稱]**
- **位置:** [描述在面板上的位置]
- **功能:** [主要功能描述]
- **範圍:** [調整範圍，如 0-100%、20ms-2000ms]
- **調整影響:**
  - **向上/順時針** → [效果]
  - **向下/逆時針** → [效果]
- **使用技巧:**
  - [情境 1]: [設定建議]
  - [情境 2]: [設定建議]

[重複每個控制項]

---

## 實際使用範例

### **範例 1: [範例名稱]**

**音樂風格**: [Jazz, Post Rock, etc.]

**設定**:
| 參數 | 設定值 | 說明 |
|------|--------|------|
| [旋鈕1] | [值] | [為何這樣設定] |
| [旋鈕2] | [值] | [為何這樣設定] |

**效果**:
- [描述實際聽到的效果]
- [適合的應用場景]

**適合場景**:
- [具體使用情境]

[提供 3-5 個不同風格/用途的範例]

---

## 音樂風格設定指南

### **[音樂風格]**

**典型設定**:
[參數表格]

**關鍵要點**:
- [要點1]
- [要點2]

[重複每個主要音樂風格]

---

## 進階技巧

### **[技巧名稱]**

**目的**: [為何需要這個技巧]

**步驟**:
1. [步驟1]
2. [步驟2]

**注意事項**:
- [注意事項]

---

## 故障排除

**問題：[常見問題]**
- **解決方案**: [解決方法]

[列出 5-10 個常見問題]

---

## 與其他設備搭配

### **與吉他搭配**

[根據用戶的吉他提供建議]

### **與音箱搭配**

[根據用戶的音箱提供建議]

---

## 總結

### **核心優勢**
[列出 3-5 個關鍵優勢]

### **最佳使用建議**
- **初學者**: [建議]
- **中階使用者**: [建議]
- **進階使用者**: [建議]

### **適合音樂風格**
[表格總結]

---

**相關文件**:
- [YAML 路徑] - 完整技術規格
- [Research 路徑] - 深度技術分析
```

---

## Generation Algorithm

### Step 1: 解析 YAML 技術資料

```python
def parse_yaml_data(yaml_path):
    """
    從 YAML 提取關鍵資訊
    """
    data = read_yaml(yaml_path)

    extracted = {
        'basic_info': data['basic_info'],
        'controls': data.get('controls', {}),
        'innovative_features': data.get('innovative_features', {}),
        'tonal_characteristics': data.get('tonal_characteristics', {}),
        'special_features': data.get('special_features', {}),
        'usage_recommendations': data.get('usage_recommendations', {}),
        'usage_tips': data.get('usage_tips', {})
    }

    return extracted
```

**注意事項：**
- 如果 YAML 中 `controls` 詳細度不足（如只有控制項名稱清單），應**標註需要補充**
- 如果缺少 `usage_tips`，應根據 `tonal_characteristics` 推測基礎使用建議

---

### Step 2: 整合 Research 文件資訊

```python
def integrate_research_data(research_path):
    """
    從 Research MD 文件提取補充資訊
    """
    content = read_markdown(research_path)

    # 提取相關段落
    extracted = {
        'technical_specs': extract_section(content, 'technical_specs'),
        'sound_characteristics': extract_section(content, 'sound'),
        'usage_suggestions': extract_section(content, 'usage'),
        'comparison': extract_section(content, 'comparison')
    }

    return extracted
```

---

### Step 3: 生成控制介面說明

```python
def generate_control_descriptions(controls_data, innovative_features):
    """
    為每個控制項生成詳細說明
    """
    descriptions = []

    for control in controls_data:
        desc = {
            'name': control['name'],
            'position': infer_position(control),  # 從 YAML 推測或標註待確認
            'function': control.get('description', '待手冊確認'),
            'range': control.get('range', '待手冊確認'),
            'impact': generate_impact_description(control, innovative_features),
            'usage_tips': generate_usage_tips(control, music_styles)
        }
        descriptions.append(desc)

    return descriptions

def generate_impact_description(control, features):
    """
    根據控制項類型和效果器特性，生成調整影響描述
    """
    # 例如：Feedback 控制 → "向上旋轉會增加重複次數"
    # 例如：Mix 控制 → "向上旋轉會增加效果明顯度"
    pass
```

**處理缺失資訊：**
```python
if control['range'] == 'unknown':
    description += "\n- **範圍:** 待手冊確認（典型 [效果器類型] 為 [推測範圍]）"
```

---

### Step 4: 生成使用範例

```python
def generate_usage_examples(pedal_data, user_context):
    """
    根據效果器特性和用戶音樂風格，生成實際使用範例
    """
    examples = []

    # 1. 從 usage_tips 提取基礎範例
    if 'usage_tips' in pedal_data:
        for tip_category, tip_data in pedal_data['usage_tips'].items():
            example = convert_tip_to_example(tip_data, user_context)
            examples.append(example)

    # 2. 根據 innovative_features 生成特色範例
    for feature, feature_data in pedal_data['innovative_features'].items():
        example = generate_feature_showcase_example(feature, feature_data)
        examples.append(example)

    # 3. 根據用戶音樂風格生成客製化範例
    for style in user_context['music_styles']:
        if style in pedal_data['music_styles']:
            example = generate_style_specific_example(pedal_data, style)
            examples.append(example)

    return examples

def convert_tip_to_example(tip_data, user_context):
    """
    將 YAML usage_tips 轉換為完整範例
    """
    example = {
        'title': tip_data['use_case'],
        'music_style': infer_music_style(tip_data),
        'settings': parse_settings_from_tip(tip_data['steps']),
        'effect_description': tip_data['description'],
        'suitable_scenarios': generate_scenarios(tip_data, user_context)
    }
    return example
```

**範例生成規則：**

1. **基礎範例（3-4個）**
   - 從 YAML `usage_tips` 直接轉換
   - 確保涵蓋主要使用情境

2. **特色功能範例（1-2個）**
   - 展示 `innovative_features` 的應用
   - 例如：FF-1Y 的 Random Phase Modulation、Dual Delay 路由

3. **音樂風格範例（每種風格 1 個）**
   - 根據用戶的 `music_styles` 偏好
   - 每個範例針對特定風格優化

4. **進階技巧範例（2-3個）**
   - 結合多個功能的複雜應用
   - 例如：模式切換、與其他效果器搭配

---

### Step 5: 生成故障排除章節

```python
def generate_troubleshooting(pedal_data):
    """
    根據效果器特性，預測常見問題並提供解決方案
    """
    issues = []

    # 1. 基於效果器類型的通用問題
    type_specific_issues = get_type_specific_issues(pedal_data['type'])
    issues.extend(type_specific_issues)

    # 2. 基於特殊功能的問題
    for feature in pedal_data.get('innovative_features', []):
        feature_issues = get_feature_specific_issues(feature)
        issues.extend(feature_issues)

    # 3. 基於 cons（缺點）推測潛在問題
    if 'review_summary' in pedal_data and 'cons' in pedal_data['review_summary']:
        for con in pedal_data['review_summary']['cons']:
            issue = convert_con_to_troubleshooting(con)
            issues.append(issue)

    return issues

def get_type_specific_issues(pedal_type):
    """
    效果器類型常見問題庫
    """
    common_issues = {
        'delay': [
            {
                'problem': '延遲音過於混濁',
                'solution': '削減 EQ Low -2 至 -4dB'
            },
            {
                'problem': '延遲音太亮、刺耳',
                'solution': '削減 EQ High -2 至 -3dB'
            }
        ],
        'reverb': [
            {
                'problem': '殘響過度掩蓋原音',
                'solution': '降低 Mix 或 調整 Pre-Delay'
            }
        ],
        # ...
    }
    return common_issues.get(pedal_type, [])
```

---

### Step 6: 驗證與補充標註

```python
def validate_and_annotate(generated_document, yaml_data):
    """
    驗證文件完整性，標註需要補充的資訊
    """
    issues = []

    # 檢查控制項說明完整度
    for control in generated_document['controls']:
        if control['range'] == '待手冊確認':
            issues.append({
                'type': 'missing_data',
                'location': f"控制項: {control['name']}",
                'field': 'range',
                'suggestion': f"需要查閱官方手冊確認 {control['name']} 的調整範圍"
            })

    # 檢查範例數量
    if len(generated_document['examples']) < 5:
        issues.append({
            'type': 'insufficient_examples',
            'current_count': len(generated_document['examples']),
            'recommended_count': '5-8',
            'suggestion': '建議增加更多音樂風格的應用範例'
        })

    # 在文件開頭添加資料完整度註記
    if issues:
        note = generate_completeness_note(issues)
        generated_document['header']['completeness_note'] = note

    return generated_document, issues

def generate_completeness_note(issues):
    """
    生成資料完整度註記
    """
    note = "## 資料完整度說明\n\n"

    missing_count = len([i for i in issues if i['type'] == 'missing_data'])
    if missing_count > 0:
        note += f"⚠️ 本文件有 {missing_count} 項資訊待官方手冊確認\n"
        note += "這些項目已標註為「待手冊確認」，並提供合理推測值供參考\n\n"

    return note
```

---

## Output Format

### 文件命名規則

```
[pedal_id]_examples.md

範例:
- ff1y_examples.md
- empress_mkii_examples.md
- pa1qg_examples.md
```

### 儲存位置

```
shared/equipment_database/pedals/examples/[pedal_id]_examples.md
```

---

## Quality Checklist

生成文件後，檢查以下項目：

### ✅ 必要元素
- [ ] 所有控制項都有詳細說明
- [ ] 至少 5 個實際使用範例
- [ ] 涵蓋用戶的主要音樂風格
- [ ] 包含參數設定表格
- [ ] 包含效果描述與適用場景
- [ ] 包含故障排除章節（至少 5 個問題）

### ✅ 資料準確性
- [ ] 所有技術規格與 YAML 一致
- [ ] 控制項範圍標註清楚（已知 or 待確認）
- [ ] 推測的資訊有明確標註
- [ ] 引用來源清楚（YAML 路徑、Research 路徑）

### ✅ 實用性
- [ ] 範例設定可實際操作
- [ ] 參數值合理且有說明
- [ ] 針對用戶的設備（吉他/音箱）提供建議
- [ ] 進階技巧有步驟說明

### ✅ 可讀性
- [ ] 使用清晰的表格呈現設定
- [ ] 章節結構清楚，有目錄
- [ ] 使用 emoji 或符號增強可讀性（✅ ❌ ⚠️）
- [ ] 中英文術語一致

---

## Integration with Research Agent

### 觸發時機

**Pedal Research Agent 完成後自動觸發：**

```yaml
# 在 Pedal Research Agent 的 Step 7 之後

Step 8: 生成使用範例文件 (可選)

  詢問用戶:
    "研究完成！是否要生成使用範例文件？(Y/n)"

  if 用戶同意:
    呼叫 Usage Examples Generator Skill
    input:
      pedal_id: [當前研究的效果器]
      yaml_path: [剛生成的 YAML 路徑]
      research_path: [當前 research 文件路徑]
      user_context: [從 inventory 讀取]
```

---

## Example Workflow

```
User: "根據 FF-1Y 的 YAML 建立使用範例"

Claude:
  Step 1: 讀取 shared/equipment_database/pedals/ff1y.yaml
  Step 2: 讀取 projects/2025-v3-signal-chain/research/compressor_eq_spatial_effects_technical_data.md
  Step 3: 讀取 projects/[current_project]/inventory/music_styles.yaml
  Step 4: 讀取 projects/[current_project]/inventory/guitars.yaml, amps.yaml

  Step 5: 解析 YAML 控制項資料
    發現: controls 只有控制項名稱清單，缺少詳細參數
    → 標註「待手冊確認」並提供推測值

  Step 6: 生成控制介面說明
    - Delay Time (×2): 根據 delay 類型推測範圍
    - Feedback (×2): 標準 feedback 範圍
    - Mix: 標準 mix 範圍
    - EQ (3-band): 根據 innovative_features 說明生成
    - Modulation: 根據 Random Phase Modulation 特性生成
    - Routing Select: 根據 dual_delay_architecture 生成
    - Soft Clipping: 根據 innovative_features 生成

  Step 7: 生成使用範例
    - 從 usage_tips 轉換:
      * dual_delay_routing (Parallel) → "立體聲 Ping-Pong Delay"
      * dual_delay_routing (Series) → "節奏瀑布延遲"
      * soft_clipping_usage → "磁帶回音模擬"

    - 根據音樂風格生成:
      * Jazz → "Double Delay Texture"
      * Post Rock → "Stereo Ambient Wash"
      * Ambient → "實驗性 Ambient 層次"

  Step 8: 生成故障排除
    - 根據 delay 類型常見問題
    - 根據 dual delay 特殊問題
    - 根據 cons 推測（如「複雜功能可能有學習曲線」）

  Step 9: 驗證與標註
    發現 3 項「待手冊確認」
    → 在文件開頭添加完整度說明

  Step 10: 寫入文件
    shared/equipment_database/pedals/examples/ff1y_examples.md

Claude: ✅ 使用範例文件已生成！

路徑: shared/equipment_database/pedals/examples/ff1y_examples.md

包含:
- 7 個控制項完整說明
- 7 個實際使用範例（並聯 3 個 + 串聯 4 個）
- 5 種音樂風格設定指南
- 5 個進階技巧
- 10 個故障排除問題

⚠️ 注意: 有 3 項參數待官方手冊確認（已提供合理推測值）
```

---

## Error Handling

### 錯誤 1: YAML 資料不完整

```
Error: controls 欄位為空或只有名稱清單

Solution:
1. 標註所有控制項為「待手冊確認」
2. 根據效果器類型提供推測值
3. 在文件開頭添加警告：
   "⚠️ 控制項詳細參數待官方手冊確認，目前提供合理推測值"
```

### 錯誤 2: 找不到 Research 文件

```
Error: Research 文件路徑不存在

Solution:
1. 僅依賴 YAML 資料生成
2. 範例較為基礎（3-4 個）
3. 建議用戶先完成 Research
```

### 錯誤 3: 使用範例不足

```
Warning: 只能生成 2 個範例（推薦 5-8 個）

Solution:
1. 生成基礎範例
2. 在文件末尾添加:
   "📝 此文件範例較少，建議補充更多音樂風格應用範例"
```

---

## Future Enhancements

### V1.1 計劃功能

1. **自動從 YouTube 影片提取設定**
   - 分析評測影片中的旋鈕位置
   - 提取評測者的設定建議

2. **互動式範例生成**
   - 詢問用戶：「你最常彈什麼風格？」
   - 根據回答生成客製化範例

3. **範例預設檔案生成**
   - 生成可匯入效果器的預設檔案（如支援）
   - 例如：PA-1QG 的 99 presets 配置檔

4. **與 Signal Chain Builder 整合**
   - 根據訊號鏈位置生成特定範例
   - 例如：FX Loop 中的設定 vs 前級前的設定

---

**文件行數:** ~680 行
**版本:** 1.0
**最後更新:** 2026-01-11
