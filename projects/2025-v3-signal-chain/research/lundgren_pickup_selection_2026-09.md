# Lundgren 雙 humbucker 選型研究（Pearson Omega 6）

**建立日期**：2026-09-30
**研究期間**：2026-09-26 至 2026-09-27，共三輪
**目標琴**：Pearson Omega 6 Standard，25.5" 直品，Wasp Yellow，Chrome 五金（規格見 `shared/equipment_database/guitars/specs/pearson_omega_6.yaml`）
**狀態**：建議。**尚未換裝**，也還沒有使用者實際試聽的記錄

證據等級標記沿用規格檔的寫法：

- [official]：Lundgren、Pearson、ESP 官方頁面，或創辦人本人的發言
- [dealer]：經銷商或代理商
- [independent]：評測者、車主、論壇
- [inference]：本研究的推論

**所有音色判斷都來自文字與影片逐字稿。沒有任何研究 agent 實際聽過聲音。**

---

## 1. 結論

### 1.1 原廠拾音器已經接近需求

Omega 6 原廠的 Pearson A2 與 Lundgren Heaven 57 是同一類拾音器。

| 項目 | Pearson A2（原廠） | Lundgren Heaven 57 |
|---|---|---|
| 磁鐵 | Alnico 2 [official] | 官方未公開等級。一位聽者說它聽起來像 Duncan Alnico II Pro [independent] |
| 阻值 neck / bridge | 7.0k / 8.1k（Omega 產品頁）、7.2k / 8.4k（2025 年 A2 單賣頁）[official]；實測 7.27k / 8.41k（Hyper B，Pearson 贊助的評測）[independent] | 7.5k / 8.5k [dealer]；一組實測 6.97k / 約 7.89k（照片未標位置、首位數字反光，該組是兩芯編織線版）[independent] |
| 四芯線 | 有 [official] | 50mm 版有 [official] |
| 切單評價 | 多位評測者稱讚 [independent，多半受 Pearson 贊助] | 只有一則間接報告：Lundgren 商店一位買家在 PRS 的 5 檔配線中用 H57 neck，兩顆切單的中間檔「turned out really well」[independent，廠商頁上的評論] |

所以換成 Lundgren 是**精修，不是修正**。第三輪反向驗證給的「比原廠進步」分數只有 4–5 分（滿分 10）。

**建議先用原廠拾音器彈 2–4 週**，再決定要不要換。步驟見第 7 節。

### 1.2 如果要換：兩組最佳搭配

| | 第 1 組（推薦） | 第 2 組 |
|---|---|---|
| Neck | Heaven 57（50mm 版） | Heaven 57（50mm 版） |
| Bridge | **Heaven 67**（50mm 版） | Heaven 57（50mm 版） |
| 價格 | €159 + €159 = €318 | €318（Set 與兩顆單買同價） |
| 與原廠的差別 | bridge 從 Alnico 2 換成 Alnico 5，是這一組裡唯一真正的音色改變（neck 幾乎等於原廠）。改變幅度中等，證據少 | 最接近原廠，同類聲音的精修 |
| 輕破音 | 低頻更緊、高頻更亮，適合 classic rock crunch [official 定位] | 證據最多：官方 TS demo [official]，部落格與 Lundgren 商店買家對 TS、Klon 類效果器的好評 [independent]。全部來自木頭琴 |
| 主要風險 | 評論少；有一位聽者覺得 bridge「有點薄」；鋁框加 JC-22 可能偏刺 | 與原廠差異小 |

第 1 組比較符合使用者自己的音色理論 [inference]。`shared/tone_theory/overdrive_stacking_theory.md:1386-1459`（Strategy 3）寫到 Horsemeat→Sweet Honey 疊加「Requires bright guitar or amp to balance warmth」（:1443），建議「Bridge pickup emphasis」（:1450），並把「Neck pickup」列在「Too Dark」底下（:1453-1456）。Heaven 67 的官方定位是比 Heaven 57 更亮的 bridge。

### 1.3 降級與備案

- **Nashville Split（bridge）降級。** 它是 Lundgren 唯一專為切單設計的型號。但在 Omega 6 上有三個問題：
  - 平頭棒狀磁鐵不能調，在 12" 指板半徑下 D、G 弦離磁柱較遠 [inference]
  - 唯一獨立安裝者形容它「相當亮、不太寬容」[independent]
  - 原廠切單已受好評；想要「內側線圈」的切單音色，可以改接原廠 bridge toggle 試聽，不用買新拾音器 [inference]。但改線不在保固範圍，見第 7 節
- **neck 太暗時的可能備案：BJFE HB neck。** 官方寫它「keeps the low end down」、「a tad brighter than any of our neck pickups」[official]。但有三個保留：
  - 第 3 輪三位評審都把它排除：它是 Lundgren 最亮的 neck，在鋁框加 JC-22 上可能太薄 [inference]
  - 只有一位反向驗證者把它列為「neck 太暗時」的挑戰者
  - 四芯線不保證：一組經銷商新品出貨是兩芯編織線 [dealer]，另一顆是四芯線 [independent]

  第 2 輪在 Eclipse 假設下驗證過 BJFE 一組，結果是削弱。第 3 輪沒有針對 Omega 反向驗證它。

---

## 2. 需求與使用情境

### 2.1 使用者的需求（原話）

> 主要要挑選兩個 Humbucker 拾音器，一個在 neck，一個在 bridge，而且它們都可以切單。
> 幫我找兩個最好的搭配，它們可以是同一個系列，也可以是不同系列的 neck 和 bridge。
> 最主要想要有 clean tone，以及稍微到 rock 一點點的 overdrive 或 distortion，沒有到 metal 那樣的聲音基底。

### 2.2 本庫記載的使用情境

- 風格與使用比例：Jazz 80%、Neo Soul 70%、Funk 60%、Post Rock 40%、Fusion 30%、Pop Rock 30%、Rock 20%（`projects/2025-v3-signal-chain/music_styles.yaml:16-156`）
- 80% 居家錄音、20% 練習、0% 現場（`projects/2025-v3-signal-chain/music_styles.yaml:181-183`）
- 音箱：Roland JC-22（晶體、乾淨、偏亮）、Tone King Imperial MKII（真空管前級）（`projects/2025-v3-signal-chain/inventory/amps.yaml`）
- 破音全部來自低中增益效果器：Sweet Honey、PRS Horsemeat、Morning Glory、Roshi Blacklon、TWA Source Code、ODL-1-CS；常開 Empress MKII 或 Cali76（`projects/2025-v3-signal-chain/inventory/pedals.yaml`）

結論：拾音器不需要高輸出。低中輸出的 PAF 能讓這些效果器停在低增益、觸彈敏感的區間 [inference]。

---

## 3. 研究方法

三輪都用多 agent workflow 執行，每輪 10 個 agent。

| 輪次 | 目標琴假設 | 做了什麼 |
|---|---|---|
| 第 1 輪 | 未指定 | 3 個 agent 讀本庫的研究檔案；1 個 agent 盤點 Lundgren 完整型錄與線材政策；6 個 agent 分家族深入研究每一款 6 弦標準尺寸 humbucker |
| 第 2 輪 | 推測為 ESP Eclipse CTM | 4 位評審從不同角度各推薦 3 組配對（clean／jazz、切單／funk、輕破音、琴體平衡）；1 個 agent 獨立查核關鍵事實；得票前 5 組各交給一個反向驗證 agent 嘗試推翻 |
| 第 3 輪 | 使用者確認為 Pearson Omega 6 | 3 個 agent 查證 Omega 6（官方規格、網路評價、Lundgren 相容性）；3 位評審重新排名；前 4 組反向驗證 |

第 2 輪之後使用者才告知目標琴，所以第 1、2 輪的琴體分析以 Eclipse 為假設。第 5 節記錄那兩輪的結論，供日後換其他琴時參考。

---

## 4. Lundgren 型錄盤點

### 4.1 型錄範圍

2026-09-26 從官方商店 `shop.lundgrenpickups.com` 的 Shopify 產品資料取得完整型錄：共 122 件商品，其中 humbucker 分類 50 件 [official]。扣除 7／8／9 弦、扇形品格版與貝斯款之後，6 弦標準尺寸 humbucker 如下。

| 型號 | 磁鐵 | 阻值 neck / bridge | 四芯線 | 本研究判定 |
|---|---|---|---|---|
| Heaven 57 | Alnico，等級未公開 | 7.5k / 8.5k [dealer] | 50mm 版標配 [official] | **候選（neck 首選）** |
| Heaven 67 | Alnico 5 | 7.3k / 8.3k [dealer]；實測 7.42k / 8.54k [independent] | 50mm 版標配 [official] | **候選（bridge 首選）** |
| Heaven 77 | Alnico 4 | 7.77k / 8.77k [official] | 50mm 版標配 [official] | 排除：官方定位「更 edgy、更熱」，Van Halen 聲音 |
| Smooth Operator | Alnico 2 | 約 7.2–7.8k [independent 實測] | 50mm 版標配 [official] | 可行但未入選：幾乎等於原廠 A2 neck |
| Modern Vintage | Alnico 5 | 7.3k / 8.3k [official] | 只有日本代理商寫四芯 [dealer] | 可行但未入選：四芯線缺官方說明 |
| BJFE HB | Alnico 4 | 7.0k / 8.3k [official] | **不保證**，出貨過兩芯也出貨過四芯 | 備案 neck，需書面確認 |
| Nashville Split | Alnico 棒狀，等級未公開 | 未公開 | 標配 [official] | 第 2 輪入選，第 3 輪降級（見 1.3） |
| The Anomaly 6 | Alnico 5 | bridge 約 8.3k [independent，論壇擋爬蟲，未能複查] | 官方未寫；OEM 與車主證據支持 | 未入選：「不寬容」、demo 極少 |
| Hot Heaven | Alnico 4 | bridge 14.75k [official] | 經銷商寫四芯 [dealer] | 排除：高輸出；商店只賣 bridge |
| The One | Alnico 5 | bridge 約 15k [official] | 車主回報四芯 [independent] | 排除：hard rock，經銷商說不適合 jazz |
| Suckerbucker | 未公開 | 未公開，高輸出 | 標配 [official] | 排除：高輸出，只有 bridge |
| Black Heaven | neck Alnico，bridge ceramic（可選 Alnico V） | 8.56k / 10.4k [official, 2018] | 標配 [official] | 排除：metal 取向 |
| M6 / M6C | Ceramic | 約 8.6k / 11.3k [independent 實測] | 標配 [official, 2012] | 排除：高輸出 metal |
| Big Firebird | 兩根棒狀磁鐵，材質未公開 | 未公開 | **未知** | 排除：無法確認能切單 |
| Firebird、Minihumbucker | — | — | 未知 | 排除：尺寸不是標準 humbucker |

### 4.2 型錄以外找到的型號

- **Custom Operator**：只能 email 客製。唯一描述是一位顧客說它是「過繞的 Smooth Operator」[independent]。沒有規格、價格
- **Lundgren Design No. 2 / No. 5**：只裝在 Hagström Fantomen 原廠琴上，不單賣 [dealer]
- **Revolver**：外型是 humbucker 尺寸，但官方說明它是 P-90 單線圈 [official]，**無法切單**。這是一個容易誤買的陷阱
- **Vintage Bridge / Vintage Neck**：已停產，由 Modern Vintage 取代 [official 舊頁 + inference]

### 4.3 四芯線：50mm 版與 49.2mm 版是兩套包裝

Heaven 57、67、77 與 Smooth Operator 各有兩個商品頁 [official]：

| 商品頁 | 間距 | 線材 | 腳長 | 能否切單 |
|---|---|---|---|---|
| 「50mm」 | 50.0mm | **4 lead** | 短腳（22.4mm） | 可以 |
| 「Vintage 49,2mm」 | 49.2mm | 兩芯編織線 | 長腳（28.8mm） | **不行** |

50mm 頁面的版本說明寫「This Version of the Heaven 57® have a spacing of 50mm , 4 lead cable and short legs(standard).」[official]。

⚠️ Heaven 57 與 67 的 50mm 頁面，下方舊描述仍寫「braided single conductor with shield」。那是從 49.2mm 版複製過來的舊文字，但仍要在訂購時取得書面確認。

Lundgren 沒有公開的「所有型號都可改四芯」政策。2024 年的 Heaven 77 頁面曾提供兩芯與四芯兩種選項，價格相同 [official 存檔]。

### 4.4 尺寸、線色與退貨

- **50mm 短腳圖面** [official]：耳孔間距 78.0mm，全長 84mm，高 22.4mm，螺絲 UNC 3-48
- **F-spaced（52–53mm）**：商店沒有選項。官方文字只有 Hot Heaven 寫「50 mm or 52 mm」。其他型號有人透過備註或 email 訂到 [independent]。2014 年一家經銷商說所有型號都能做 F-spaced，唯獨 Heaven 57 例外 [dealer]；這句話早於 Heaven 67 上市。瑞典經銷商 gitarrdelar.se 目前列有「Heaven 57 Bridge Black 52 mm」（缺貨）[dealer]
- **線色**（黑線版）[official]：Black = logo 線圈起點（熱線）；White = logo 線圈終點；Red = 另一顆線圈終點；Green = 另一顆線圈起點（接地）；Bare = 屏蔽。串聯時 White 接 Red。灰線版以 Blue／Yellow 取代 Black／White。圖面把 logo 線圈標為 South
- **Nashville Split 例外**：官方建議切單時保留 NO LOGO 線圈（紅／綠線，North）[official]
- **退貨** [official]：30 天自願退貨，限「unused, in new condition, and in its original packaging」。EU 14 天鑑賞期只適用 EU 消費者。依個人規格製作的拾音器不適用鑑賞期
- **台灣管道**：Teddy's note 在 2026 年宣布成為台灣代理，並接受客製 [dealer，代理商自己的 Threads 貼文]。Lundgren 官方使用者頁仍列 Shock Music Taiwan [official]

---

## 5. 第 1、2 輪：以 ESP Eclipse CTM 為假設的結果

這兩輪做完時，使用者還沒有說明目標琴。研究推測是 Eclipse [inference]：它有標準 humbucker 槽，兩顆 volume 可以改成推拉切單，也是本庫文件評為最不適合 jazz 的琴。

### 5.1 評審與驗證結果

| 配對 | 評審得分 | 反向驗證 |
|---|---|---|
| Heaven 57 neck + Heaven 67 bridge | 7 分（3 位評審選入） | 成立，需修正 |
| BJFE HB 一組 | 6 分 | 削弱：四芯線不保證；4 位評論者中只有 2 位是驗證買家 |
| Heaven 57 neck + Nashville Split bridge | 5 分 | 成立，需修正 |
| Heaven 57 一組 | 4 分 | 削弱：neck 在實心桃花心木琴上有「太肥」報告 |
| Nashville Split 一組 | 2 分 | 削弱：neck 版完全沒有資料 |

### 5.2 這兩輪留下的通用結論

- **Heaven 57 neck 在實心琴上有偏肥的風險。** 兩份實心琴報告：「almost too fat」（Les Paul，2008）、「a bit too boomy」（24 格 PRS 型，2017）[independent]。正面評價多半來自 archtop 與半空心琴
- **Heaven 67 的優勢是低頻更緊、高頻更亮**，不是「中頻較少」。官方文字寫它「slightly more aggressive mids」[official]
- **Heaven 57 的 F-spaced 版沒有官方選項**：只有經銷商列過 52mm bridge（缺貨），要 email 客製，客製品不能退。見 4.4

### 5.3 研究過程中順帶發現的 Throbber 事實

ESP 現行 THROBBER-STD 產品頁有官方檔位圖。Throbber 的 5 檔撥桿出廠就能切單（Position 2 與 4）。本庫原本記為「官方從不命名檔位」，已在 2026-09-30 更正，見 `shared/equipment_database/guitars/specs/esp_throbber_ctm.yaml` 的 `pickups.pickup_selector`。

因此 Throbber 不適合做這次換裝：它已經能切單，Heaven 57 又接近它原廠的 APH-1，而且 bridge 需要客製 F-spaced。

---

## 6. 第 3 輪：Pearson Omega 6

### 6.1 琴體關鍵事實

完整規格與來源見 `shared/equipment_database/guitars/specs/pearson_omega_6.yaml`。影響選型的事實如下：

| 項目 | 內容 | 對選型的影響 |
|---|---|---|
| 琴身 | 鋁板加不鏽鋼的開放式框架，沒有木頭 [official] | 木頭琴上的評價只能參考 |
| 原廠 neck 的聲音 | 「高頻稍收」（Omega）；同款 A2 在 Hyper B 上「偏柔」「低音弦偏重」[independent] | Heaven 57 neck 可能延續這個傾向，不會修正它 |
| 琴橋弦距 | 10.4mm [official，創辦人] → 琴橋處 E 到 E 約 52.0mm，bridge 拾音器上方約 51mm [inference] | **不需要 F-spaced** [inference]：50mm 版外側磁柱與 E 弦只差約 0.5mm。注意原廠 A2 bridge 是 52mm [official]；第 3 輪相容性 agent 原本建議 F-spaced，反向驗證依 10.4mm 弦距推翻 |
| 拾音器安裝 | 支柱加壓片，沒有拾音器槽；Import Spec 77mm、M3 [official] | Lundgren 是 78mm、3-48，要另買螺絲並確認壓片 |
| 切單 | 產品頁寫「Coil Split: Individual」[official]；形式是每顆一個 mini toggle [independent，多位評測者] | 兩顆都必須是四芯線 |
| 原廠線色 | Green = 熱線，Black + Bare = 接地 [official] | 與 Lundgren 相反，要依功能對接 |
| 保固 | 不涵蓋更換拾音器、改線與焊接，也不涵蓋任何被改過的琴 [official]。「事先同意」只出現在「未授權維修」那一條 | 換拾音器等於放棄這部分保固。換裝前先做完品質檢查 |

### 6.2 評審與驗證結果

| 配對 | 評審得分 | 反向驗證 | 驗證後分數（clean／輕破音／切單／比原廠進步） |
|---|---|---|---|
| Heaven 57 neck + Heaven 67 bridge | 6 分（3 位評審都選入） | 削弱 | 7.5／7.5／5／4.5 |
| Heaven 57 一組 | 6 分（2 位評審選為第 1） | 削弱 | 7.5／8.5／4.5／4 |
| Heaven 57 neck + Nashville Split bridge | 3 分 | 削弱 | 7／6／8／5 |
| Heaven 57 neck + 保留原廠 bridge | 1 分 | **推翻**：只有一顆 Lundgren，不符需求 | 7／6.5／5／2.5 |

未驗證：Heaven 67 neck + Nashville Split bridge；Smooth Operator neck + Modern Vintage bridge。這兩組與「Heaven 57 neck + 保留原廠 bridge」同為 1 分（各有一位評審列第 3）。反向驗證名額只有 4 組，依排序只驗證了其中一組。

三組都被「削弱」的共同原因：

- 原廠 A2 已是同類拾音器，進步幅度有限
- Heaven 67 的切單音色完全沒有報告；Heaven 57 只有一則廠商頁上的間接報告。原廠切單則已受好評
- Lundgren 拾音器焊上之後就不能退貨

### 6.3 第 1 組勝出的理由

第 1 組與第 2 組同分。本研究選第 1 組，理由有三：

1. 三位評審都把它列入前三名
2. Alnico 5 bridge 是這一組與第 2 組之間唯一的磁鐵差異，進步分數 4.5 對 4
3. 它比較符合使用者音色理論的「明亮的吉他或音箱、以 bridge 為主」[inference]

如果使用者更在意輕破音的證據量，第 2 組同樣合理。

---

## 7. 建議步驟

### ⚠️ 開始前

- Pearson 保固不涵蓋更換拾音器、改線與焊接，也不涵蓋任何被改過的琴。官方條文沒有「事先同意就保留保固」的例外
- Lundgren 拾音器焊上之後就不能退貨
- 兩家線色相反：Pearson Green 是熱線，Lundgren Green 是接地

### 7.1 換裝前

1. **在保固期內檢查品質**：琴格、琴枕、異音。自費車主回報過不平的琴格、偏高的第 24 格、鬆螺絲 [independent]
2. **用原廠拾音器建立比較基準**：
   1. 把 neck 拾音器調低，低音側再低一點
   2. 用 JC-22 與 Imperial 各錄一組參考音檔
   3. 看 tone 電容上的標示。官方寫 0.22µF，很可能是 0.022µF 少一個 0 [inference]
3. **寫信給 Pearson**（support@pearsoninstruments.com），問四件事：
   1. 換了拾音器之後，琴的其他部分（琴頸、框架、五金）還有沒有保固
   2. 壓片能否接受 78mm 耳距與 3-48 螺絲
   3. bridge 拾音器後方的可用深度
   4. 原廠 toggle 切單時保留哪一顆線圈
4. **自己確認原廠切單保留哪一顆線圈**：在切單狀態下，用螺絲起子輕觸各排磁柱，有聲音的那排就是保留的線圈。這一步不用拆線
5. **選擇性：改接原廠 bridge toggle，試聽另一顆線圈。** 改接屬於改線與焊接，保固不涵蓋。請在品質檢查完成、取得 Pearson 回覆之後再做 [inference]

### 7.2 決定換裝時

1. **只從「50mm」商品頁下單。** 不要買「Vintage 49,2mm」版
   - Neck：`https://shop.lundgrenpickups.com/products/heaven-57%C2%AE-50mm`，Neck，€159
   - Bridge：`https://shop.lundgrenpickups.com/products/heaven-67%C2%AE-50mm`，Bridge，€159
2. **下單備註**：

   > 4-conductor cable required on both pickups (individual coil-split toggles). 50 mm spacing, short legs. Please confirm by email: wax potted? cable colour code (black or grey)? DCR? Include 3-48 height screws and springs.

3. **付款前取得 johan@lundgren.se 的書面回覆**
4. **另外準備 UNC 3-48 高度螺絲**（約 1–1.25 吋）與彈簧。原廠 M3 螺絲鎖不進 Lundgren 的耳孔
5. **不要訂 F-spaced。** 它不需要，而且客製品沒有鑑賞期
6. **分段做法**：可以先只換 Heaven 67 bridge，因為 bridge 是聲音變化最大的位置。混用 Lundgren 與原廠 A2 時，兩者的相位關係未知，裝好後要在中間檔做相位測試：聲音變薄、變空，就對調那一顆的熱線與接地 [inference]
7. **拾音器蓋（選配）**：Chrome 五金的 Omega 原廠可能是鍍鉻蓋版 [inference]。Lundgren 50mm 版可加 raw nickel 蓋，每顆 +€15 [official]。蓋子外觀接近原廠、能防撥片刮到，也會稍微收掉 Alnico 5 bridge 的高頻。neck 若已偏暗，建議維持開放式 [inference]

### 7.3 安裝時

1. **先試裝，不焊線。** 確認耳孔對得上壓片，並保留原包裝
2. **依功能對接**：
   - Lundgren Black（灰線版 Blue）→ 原廠 Green 的位置（熱線）
   - Lundgren Green + Bare → 原廠 Black + Bare 的位置（接地）
   - Lundgren White（灰線版 Yellow）+ Red → 切單 toggle
3. **兩顆切單時要保留相反極性的線圈**，兩顆都切單的中間檔才會抵消 hum。如果兩個 toggle 都把接點接地，兩顆會保留同一極性的線圈 [inference]，中間檔會有 hum
4. **一定要實測**：裝好後用指南針確認磁極，再做 hum 測試與相位測試。各 agent 對「logo 線圈是 screw 還是 slug」的判讀互相矛盾，所以不能只靠圖面
5. **保留原廠 A2**，保固維修或轉賣時會用到
6. **Horsemeat→Sweet Honey 疊加用 bridge 或中間檔**，不要用 neck

---

## 8. 未解問題

| 問題 | 誰能回答 |
|---|---|
| Heaven 57／67 的 50mm 版是否確定四芯線、是否浸蠟 | Lundgren |
| Omega 6 壓片能否接受 78mm 耳距與 3-48 螺絲 | Pearson，或實機量測 |
| Omega 6 bridge 拾音器後方的可用深度 | Pearson，或實機量測 |
| 原廠 toggle 切單時保留哪一顆線圈 | Pearson，或實機測試 |
| tone 電容實際是 0.22µF 還是 0.022µF | 看電容標示 |
| Heaven 57／67 切單聽起來如何 | Heaven 67 沒有任何公開資料；Heaven 57 只有一則廠商頁上的間接報告。只能實際試聽 |
| Nashville Split 的阻值、間距、腳長 | Lundgren |

---

## 9. 證據限制

- 沒有 agent 實際聽過任何聲音
- 在可搜尋的來源中，找不到任何 Omega 6 換裝拾音器的報告。Pearson 琴唯一有記錄的換裝是 2024 年一把 Hyper 系列換 DiMarzio Fusion Edge [independent]
- Omega 6 在 2026 年 4–5 月上市，評論不多。8 支評測影片中只有 Silent Rob 一支明確是自費購買；其餘多數由 Pearson 提供琴或附折扣碼
- 研究期間網路搜尋額度用完，The Gear Page、SevenString.org、Facebook 社團與 Instagram 無法搜尋。這些地方可能還有 Omega 車主或 Lundgren 切單的報告
- 研究中下載的證據檔（頁面、影片逐字稿、照片）放在暫存目錄，沒有保留進 repo。本報告的來源以網址為準

---

## 10. 來源

### Lundgren

- 商店全部 humbucker：https://shop.lundgrenpickups.com/collections/humbuckers
- Heaven 57 50mm：https://shop.lundgrenpickups.com/products/heaven-57%C2%AE-50mm
- Heaven 57 Vintage 49,2mm：https://shop.lundgrenpickups.com/products/heaven-57
- Heaven 67 50mm：https://shop.lundgrenpickups.com/products/heaven-67%C2%AE-50mm
- Heaven 77 50mm：https://shop.lundgrenpickups.com/products/heaven-77-50mm
- Smooth Operator 50mm：https://shop.lundgrenpickups.com/products/smooth-operator%E2%84%A2-50mm
- Modern Vintage：https://shop.lundgrenpickups.com/products/heaven-57%C2%AE-50mm-spacing-kopia
- BJFE HB：https://shop.lundgrenpickups.com/products/bjfe-medium-output
- Nashville Split：https://shop.lundgrenpickups.com/products/nashville-split
- Revolver：https://shop.lundgrenpickups.com/products/revolver
- 接線圖：https://shop.lundgrenpickups.com/pages/schematics
- 尺寸圖：https://shop.lundgrenpickups.com/pages/drawings-measurements
- 退貨政策：https://shop.lundgrenpickups.com/pages/return-policy-1
- 使用者頁（台灣經銷）：https://shop.lundgrenpickups.com/pages/lundgren-users
- 2024 年 Heaven 77 頁面存檔（兩芯與四芯同價）：https://web.archive.org/web/20240919065319/https://shop.lundgrenpickups.com/products/heaven-77
- 日本代理商 LEP（阻值）：https://lep-international.jp/products/lundgren-heaven-57-set
- Heaven 57 兩顆切單的間接報告（Suckerbucker 頁的買家評論）：https://shop.lundgrenpickups.com/products/sucker-bucker-1
- Heaven 57 實測阻值（Reverb）：https://reverb.com/item/100758578
- Heaven 67 四芯實測（Reverb）：https://reverb.com/item/52008814-lundgren-pickups-heaven-67-patent-number-paf
- BJFE 兩芯出貨（Reverb）：https://reverb.com/item/45946121-lundgren-bjfe-humbucker-pickup-set-medium-output-black
- Nashville Split 安裝 demo（Gitarrverket）：https://www.youtube.com/watch?v=c09r_EXVSxw
- Hagström Fantomen（Lundgren Design No.2／No.5）：https://www.hagstromguitars.com/electric-guitars/fantomen/hagstrom-fantomen
- Teddy's note（台灣代理）：https://www.threads.com/@teddysnote/post/DW6M6JYkZYN/

### Pearson Omega 6

來源清單見 `shared/equipment_database/guitars/specs/pearson_omega_6.yaml` 的 `sources`。

### ESP THROBBER-STD 檔位圖

- 產品頁：https://espguitars.co.jp/product/2873/、https://espguitars.co.jp/product/2874/
- 圖檔：https://espguitars.co.jp/wp-content/uploads/2018/04/THROBBER_PU-SELECTER.png

### 其他參考

- Strandberg OEM 拾音器規格：https://support.strandbergguitars.com/article/74-what-are-the-specifications-of-the-strandberg-oem-pickups
- Seymour Duncan 弦距說明：https://www.seymourduncan.com/blog/tips-and-tricks/string-spacing-explained-humbuckers-vs-trembuckers
- Bare Knuckle 扇形品格拾音器說明：https://www.bareknucklepickups.co.uk/news/article/multiscale-pickups
