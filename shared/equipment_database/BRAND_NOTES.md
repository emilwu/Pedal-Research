# 品牌層級註記

**建立日期**：2026-09-12
**用途**：記錄查證某個品牌的官方規格時，**必須先知道否則會查錯**的事。

這裡不記設備規格。設備規格在各自的 spec YAML。這裡記的是「這個品牌的官方來源長什麼樣、哪些看起來像官方其實不是」。

---

## ESP

### 規則一：ESP JP 與 ESP USA 是兩間獨立公司

| 網域 | 公司 |
|---|---|
| `espguitars.co.jp` | ESP JP |
| `espguitars.com` | ESP USA |

**產品線不對應，產品只部分重疊。**

因此：**拿 ESP USA 的規格當 ESP JP 型號的佐證是無效的**，反之亦然。同名型號在兩邊可能是完全不同的琴。

本庫的設備都是 ESP JP 的型號，一律以 `espguitars.co.jp` 為準。

### 規則二：改版後的產品頁不用產品名稱

URL 形式分兩種，**單複數有意義**：

| 形式 | 用途 | 範例 |
|---|---|---|
| `/products/<slug>` （複數） | 品牌／系列／分類的彙整頁，用文字 slug | `/products/throbber`、`/products/discon-esp-guitar` |
| `/product/<數字 id>/` （單數） | 個別產品頁，用數字 id | `/product/2873/` |

**`/original/<系列>/<型號>.html` 是改版前的舊式路徑。**看到這種形式就當它是舊頁，不要拿來當現行規格依據。

### 停產品的去處

ESP JP 推出新產品時舊產品會下線，移到：

```
https://espguitars.co.jp/products/discon-esp-guitar
```

該頁每張產品卡帶一個 `DISCONTINUED` 徽章。

**注意兩件事**：

1. 該頁分頁載入。第 1 頁是靜態 HTML，後續頁要走 `/wp-json/esp/v1/brand-products?term=discon-esp-guitar&page=<n>`。直接在網址後加 `/page/2/` 無效，會拿到與第 1 頁相同的內容。只看第一頁會漏掉將近一半。
2. **下線不等於一定在停產頁上。**2026-09-12 查證時，`/original/throbber/throbber.html` 這個舊頁上的 THROBBER 型號**不在停產頁的 56 筆裡**（全文 `THROB` 零命中）。那一頁是沒被收進現行導覽與搜尋索引的孤兒頁。

### 查 ESP 規格的順序

1. 從 `/products/<系列>` 索引頁點進去，確認你要的型號在現行導覽裡
2. 現行導覽沒有 → 查停產頁 `/products/discon-esp-guitar`（記得翻頁）
3. 兩邊都沒有 → 該型號可能是孤兒頁或根本不存在於 ESP JP。**不要用搜尋引擎直接命中的 URL 當依據**，先確認它在站內導覽裡

### 同名不同品牌：ESP 集團有三個牌子

`espguitars.co.jp` 同時經營三個品牌，**型號名稱會互相撞名**：

| 品牌 | 範例 |
|---|---|
| ESP | `THROBBER-STD` |
| EDWARDS | `E-THROBBER-CTM` |
| GRASS ROOTS | `G-THROBBER-DX` |

規格完全不同（例如 E-THROBBER-CTM 的拾音器是 SP90-1n + TB-59，THROBBER-STD 是 APH-1n + TB-APH-1b）。

**麵包屑是判斷依據**：產品頁的麵包屑會寫 `ESP GUITARS > <品牌> > <系列> > <型號>`。

### ESP 沒有「THROBBER-CTM」這個型號

本庫的 `esp_throbber_ctm` 這個 id 與散在各處的「Throbber-CTM」寫法是舊稱。ESP JP 站內搜尋 `THROBBER` 只回傳 5 筆，分屬上面三個品牌，沒有一筆叫 THROBBER-CTM。

實機經使用者確認是 **ESP THROBBER-STD**。id 保留未改，理由見 `guitars/specs/esp_throbber_ctm.yaml` 的 `model_identity`。

### 已知污染：`guitars/reports/` 底下兩份報告引用了 ESP USA

`reports/` 是歷史記錄，依 repo 規則不改。但要知道裡面有這個問題：

| 檔案 | 問題 |
|---|---|
| `guitars/reports/esp_eclipse_ctm_report.md` | 「驗證來源」拿零售商 Pit Bull Audio 的 **ESP USA Eclipse** 商品頁，當這把 ESP JP 琴的硬體規格確認 |
| `guitars/reports/esp_throbber_ctm_report.md` | 兩處引用 Pit Bull Audio 的 **ESP USA Eclipse Semi-Hollow**，當 ESP JP Throbber 的設計佐證。**同時踩三個問題**：不同公司、不同型號、零售商頁而非官方頁 |

第二份報告的「驗證的關鍵資訊 ✓」清單有五項與現行 ESP JP 官方規格直接矛盾（琴身、琴頸、指板、音階、接合方式）。**讀那兩份報告的規格結論時要當成未驗證。**權威值在 `guitars/specs/` 的 YAML。

---

## 怎麼找出這類問題

單純 grep 網域**抓不到**。2026-09-12 的實例：整個 repo 沒有任何一個 `espguitars.com` 的 URL，但 ESP USA 的引用確實存在——它們以中文字串「ESP 美國官方站」「美國站」和零售商的 `esp-usa-*` 商品頁形式存在。

所以要同時 grep 三種形式：

```bash
cd /Users/emilwu/VSCode/PedalGuy/Pedal-Research/shared/equipment_database
grep -rn -E 'espguitars\.com|esp-usa|ESP USA|美國官方站|美國站' . --include='*.yaml' --include='*.md'
grep -rn 'espguitars\.co\.jp/original/' . --include='*.yaml' --include='*.md'
grep -rn 'original/[a-z]*/[a-z0-9_-]*\.html' . --include='*.yaml' --include='*.md'
```

第三條是必要的，因為有些引用不寫網域，只寫路徑片段。

---

## 其他品牌

### Fender

`guitars/reports/fender_tokyo_thinline_report.md` 同時引用 `jp.fender.com` 與 `au.fender.com`，而且 au 那條引的是**別的型號**（Heritage '60s Thinline）來當 Tokyo Edition 的規格參考。

這兩個是同一網域的區域站，**與 ESP 的情況不同**（ESP 是兩個獨立網域、兩間公司）。Fender JP 與 Fender AU 是否為獨立法人本庫未查證，**不做判斷**。但「拿別的型號當規格參考」這件事本身就要當成未驗證。

該報告在 `reports/` 底下，不改。

### Greco

所有來源都是零售商與原廠紙本目錄，**沒有官方網站**。1970 年代的 Greco 目錄規格欄位本身就不含檔位說明等細節。

### Roland

只有單一來源 `www.roland.com/us/`，未發現區域站分歧問題。

---

## 相關文件

- `PARAMETER_VOCABULARY.md` — 可調參數詞彙、資料限制，以及「查外部規格的三層查證」
- `CONTROLS_CONVENTION.md` — 控制項該進哪一個 controls 區塊的分類標準
