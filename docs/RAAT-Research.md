<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# ProCo Rat 的 Ruetz Mod 是什麼

**Ruetz Mod** 是 ProCo RAT 上很經典、而且很簡單的改法：把失真級回授網路中的 **47 Ω 電阻移除、斷開或改成可切換**。它常被稱為「Ruetz RAT mod」，目的不是增加失真，而是讓 RAT 變得更低增益、更厚、更開放。[^1_1][^1_2]

## 電路上改了什麼

原版 RAT 的增益／低頻處理涉及兩組回授支路：47 Ω 搭配 2.2 µF，以及 560 Ω 搭配 4.7 µF。47 Ω 那一支會令中高頻得到非常高的增益，相對也形成 RAT 常見的低頻收緊感。[^1_1]

Ruetz Mod 把 **47 Ω／2.2 µF 支路退出作用**後，主要留下 560 Ω／4.7 µF 那一支，因此整體增益降低、各頻段的增益關係更平均。[^1_1]

## 聲音變化

- **Gain 明顯下降**：原本 RAT 從 overdrive 到接近 fuzz 的高失真範圍會縮小。[^1_2][^1_1]
- **低頻較完整、厚實**：原版 RAT 的低頻削減感減少，聽起來比較飽滿，甚至略帶 fuzz 感。[^1_3][^1_1]
- **動態和清晰度提升**：壓縮感、飽和感通常較少，撥弦強弱和吉他音量旋鈕的反應更容易聽出來。[^1_4]
- **更適合低到中增益用途**：可把 RAT 用成粗獷的 boost、overdrive，或較不尖銳的中增益 distortion。[^1_4]


## 和一般 RAT 的取向

| 項目 | 原版 RAT | Ruetz Mod RAT |
| :-- | :-- | :-- |
| 可達增益 | 高，失真到 fuzz 邊緣 | 較低，以 low／medium gain 為主 [^1_1] |
| 低頻 | 較緊、較削減 | 較完整、較厚 [^1_1][^1_2] |
| 手感 | 壓縮、兇、聚焦 | 開放、動態較大 [^1_4] |
| 適合用途 | Heavy riff、lead、grunge、厚失真 | Blues-rock、boost、bass、疊其他 drive [^1_1][^1_4] |

## 實作建議

不要直接永久剪掉電阻；較理想的做法是用 **SPST on/off 小開關**，在原版與 Ruetz 模式之間切換。更進一步可將固定的 47 Ω 換成電位器，讓你在原本的兇猛 RAT 與低增益、全頻段感較強的 Ruetz 風格之間連續調整。[^1_4]

若你是拿 RAT 推已經破音的 amp，或會彈貝斯／降調吉他，Ruetz 通常很有價值；但若你最愛的是 RAT 那種緊、刺、飽和的高增益主音，原版模式仍然更對味。

<span style="display:none">[^1_10][^1_5][^1_6][^1_7][^1_8][^1_9]</span>

<div align="center">⁂</div>

[^1_1]: https://forum.pedalpcb.com/threads/ruetz-mod-for-german-rat-clone-vs-adding-a-clean-blend.9754/

[^1_2]: https://en.wikipedia.org/wiki/ProCo_Rat

[^1_3]: https://www.keithhollandguitars.com/unlocking-the-secrets-behind-the-rat-distortion-pedal.html

[^1_4]: https://beavisaudio.com/projects/fkr/

[^1_5]: https://jhspedals.info/blogs/news/proco-rat-pedal-myths-history-and-timeline

[^1_6]: https://www.offsetguitars.com/forums/index.php?threads/anyone-ever-try-the-ruetz-rat-mod-clipped-resistor.81992/

[^1_7]: https://www.boostguitarpedals.co.uk/blogs/pedal-knowledge/classic-gear-proco-rat

[^1_8]: https://en.wikipedia.org/wiki/Pro_Co_RAT

[^1_9]: https://carltonmusic.com/blogs/gear-on-tap/the-ultimate-rat

[^1_10]: https://equipboard.com/posts/best-rat-style-pedals


---

# 如果改成 VR 會怎樣？

如果把 Ruetz Mod 原本要移除的 **47 Ω 電阻改成可變電阻（VR）**，你就能在「原版 RAT 的緊實高增益」與「Ruetz 的低增益、較全頻」之間**連續掃描**，而不是只能二選一。常見做法是以 **1 kΩ 線性 VR** 取代 47 Ω。[^2_1][^2_2]

## 旋鈕方向與聲音

以 VR 直接取代 47 Ω 而言：


| VR 阻值 | 等效狀態 | 聲音傾向 |
| :-- | :-- | :-- |
| 約 47 Ω | 接近原版 RAT | 高增益、低頻較緊、壓縮與中高頻咬勁較明顯 |
| 約 100–500 Ω | 過渡區 | 增益下降、毛邊與 fizz 減少、低頻逐漸放鬆 |
| 約 1 kΩ | 強烈 Ruetz 化 | 中低增益、頻響更平、低頻較完整、動態較開放 [^2_2][^2_3] |
| 接近開路／極高阻值 | 接近完全移除 47 Ω 支路 | 最接近傳統 Ruetz Mod，輸出與失真量都會進一步降低 [^2_4] |

關鍵是：**阻值愈大，越接近把 47 Ω 支路拿掉**；因此不會是「VR 越大、Gain 越大」，而是相反地逐步把 RAT 從高增益 distortion 拉向厚實的 overdrive。這類改法也常被認為能降低 RAT 的刺耳 fizz，但不會把它變成真正的低頻 boost。[^2_2]

## 元件建議

- **1 kΩ linear pot**：最常見、有效調整範圍也適合；許多 DIY RAT 佈局即以 1 kΩ 線性電位器作為 Ruetz 控制。[^2_1][^2_2]
- **47 Ω 固定電阻串聯 1 kΩ VR**：較保險的做法；可確保最小阻值永遠是 47 Ω，因此旋到底仍是原版 RAT，而不會低於原設計值。[^2_5]
- **接法**：VR 作為 rheostat（兩腳可變電阻），通常用中間腳與其中一個外側腳；未使用的外側腳可與中間腳相連，避免滑動端瞬斷時變成開路並產生爆音或不穩定。[^2_1]


## 實際取向

我會建議用：

$$
47\ \Omega \text{ 固定電阻} + 1\text{ k}\Omega\ \text{B taper VR}
$$

串聯安裝。這能保留原版 RAT 的最低阻值與高增益端，同時讓你往上調出不同程度的 Ruetz 味道；約在中段通常就能找到「低頻不會太鬆、失真仍有 RAT 個性、fizz 又比較少」的甜蜜點。固定 47 Ω 串聯也避免電位器歸零時令回授阻值低於原廠設計。[^2_5][^2_2]

如果你是想讓它更適合低調弦、bass 或已有破音的 amp，這個 VR 版本比純 Ruetz 開關更值得做；若主要是要經典 RAT lead／重 riff，則保留可切回原版的開關或上述串聯方案會更實用。

<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_6][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://www.sabrotone.com/proco-rat-w-lots-of-options/

[^2_2]: https://www.madbeanpedals.com/forum/index.php?topic=28475.0

[^2_3]: https://www.youtube.com/watch?v=Z9rCucD9CO4

[^2_4]: https://www.diystompboxes.com/smfforum/index.php?topic=95273.0

[^2_5]: https://www.reddit.com/r/diypedals/comments/at75sr/ruetz_rat_mod_with_switchable_pot_id_like_to/

[^2_6]: https://www.offsetguitars.com/forums/index.php?threads/anyone-ever-try-the-ruetz-rat-mod-clipped-resistor.81992/

[^2_7]: https://www.thegearpage.net/board/index.php?threads/ruetz-rat-mod-help.738418/

[^2_8]: https://www.youtube.com/watch?v=xoJIOf9E06U

[^2_9]: https://www.facebook.com/groups/guitarrepairsdiscussion/posts/2574906566293683/

[^2_10]: https://www.facebook.com/MichelleTaylor.Blackstar/posts/decided-to-do-a-simple-mod-to-my-rat-pedal-ive-never-attempted-to-mod-a-pedal-be/2334388546972415/

[^2_11]: https://www.harmonycentral.com/forums/topic/1603364-turbo-rat-ruetz-mod-finding-the-47-ohm-resistor/

[^2_12]: https://www.instagram.com/reel/DHJR5OliO31/

[^2_13]: https://forum.pedalpcb.com/threads/mod-byoc-mouse-to-standard-rat.29828/

[^2_14]: https://www.youtube.com/shorts/eIhBIbg-ZUw

[^2_15]: https://www.talkbass.com/threads/just-bought-a-rat-to-mod.851248/


---

# 那 Filter 旋鈕在調整什麼？

RAT 的 **Filter** 是失真後端的可變低通濾波器（high-cut）：它主要在削減高頻與削弱 clipping 後產生的毛刺泛音。**順時針會更暗，逆時針會更亮**，方向和多數標示為 Tone 的效果器相反。[^3_1][^3_2]

## 旋鈕實際效果

| Filter 位置 | 電路效果 | 聽感 |
| :-- | :-- | :-- |
| 全逆時針 | 幾乎不削高頻 | 最亮、最銳利、最有咬勁與穿透力 |
| 約 10–12 點鐘 | 適度衰減高頻 | 保留 RAT 的顆粒感，同時減少刺耳 fizz |
| 約 1–3 點鐘 | 明顯削減高頻 | 更厚、更平滑、lead 較不刺耳 |
| 全順時針 | 強烈 high-cut | 很暗、圓鈍、接近 woolly／fuzz 化的感覺 [^3_2][^3_3] |

原廠說明也直接把它定義為 tone control，並說明順時針轉動會降低 treble。[^3_2]

## 電路觀點

它是 clipping 二極體之後的被動 RC 低通濾波器；RAT 常見配置以 **約 1.5 kΩ 電阻、3.3 nF 電容與 100 kΩ Filter pot** 共同決定截止頻率。[^3_4][^3_5]

低通濾波器的截止頻率可概念化為：

$$
f_c = \frac{1}{2\pi RC}
$$

Filter 順時針時，濾波網路的有效電阻增加、截止頻率下降，因此越多高頻諧波被衰減；這就是為何它不是一般「加 treble」的 Tone，而是「加 high-cut」的 Filter。其全範圍大約可從接近全頻通過，掃到約 500 Hz 附近的明顯高頻切除。[^3_6][^3_4]

## 和 Ruetz VR 的搭配

Ruetz VR 主要改的是 **失真增益級裡的低頻／增益關係**；Filter 則是在失真完成後，修整高頻、fizz 與 attack。兩者不重複：

- **Ruetz VR 往大阻值調**：失真變少、低頻更完整、動態更開放。[^3_7]
- **Filter 順時針調**：把殘餘的高頻尖刺磨掉，聲音更暗、更順。[^3_2]
- **實用起點**：Ruetz VR 先設中段，再把 Filter 從全逆時針慢慢往順時針轉，到毛邊剛好消失的位置；通常比先把 Filter 調得很暗更容易保住清晰度。[^3_3][^3_7]

<span style="display:none">[^3_10][^3_11][^3_12][^3_13][^3_14][^3_15][^3_16][^3_8][^3_9]</span>

<div align="center">⁂</div>

[^3_1]: https://jhspedals.info/blogs/news/proco-rat-pedal-myths-history-and-timeline

[^3_2]: https://c3.zzounds.com/media/RAT2_Sheet-ce9684eff457b7bf6520f17e649c740b.pdf

[^3_3]: https://www.zzounds.com/item--PRCRAT2

[^3_4]: https://www.reddit.com/r/diypedals/comments/1822qvp/proco_rat_filter_circuit/

[^3_5]: http://guitar-fx-layouts.238.s1.nabble.com/Proco-Rat-Bass-td11098.html

[^3_6]: https://www.scribd.com/document/332459990/ElectroSmash-ProCo-Rat-Analysis

[^3_7]: https://www.madbeanpedals.com/forum/index.php?topic=28475.0

[^3_8]: https://en.wikipedia.org/wiki/Pro_Co_RAT

[^3_9]: https://forum.pedalpcb.com/threads/muroidea-proco-rat.12237/

[^3_10]: https://www.amplifiedparts.com/pedal-guides/build-project-proco-rat

[^3_11]: https://forum.seymourduncan.com/threads/what-does-the-filter-knob-on-a-rat-actually-do.328940/

[^3_12]: https://en.wikipedia.org/wiki/ProCo_Rat

[^3_13]: https://help.uaudio.com/hc/en-us/articles/33537175596564-Raw-Distortion-Manual

[^3_14]: https://tonestakr.com/guides/pro-co-rat-distortion-guide/

[^3_15]: https://vectree.io/c/proco-rat

[^3_16]: https://m.media-amazon.com/images/I/91nbn19w9KL.pdf


---

# Clipping 用 Ge/Si/LED 個有什麼不同？

在 RAT 這類**硬削波**電路裡，Ge／Si／LED 最核心的差異是正向導通電壓 $V_f$：\*\*越低越早開始削波、壓縮越多、輸出越低；越高則 headroom 越大、音量與動態越開放。\*\*RAT 原版使用的是一對對稱式 Si 二極體。[^4_1][^4_2]

## 三種聲音取向

| Clipping 類型 | 常見 $V_f$ | 在 RAT 的聽感 | 實際取向 |
| :-- | --: | :-- | :-- |
| **Ge 鍺二極體** | 約 0.25–0.35 V | 最早削波、壓縮最多、柔軟溫暖、較 fuzz／sag | 低增益也有飽和，適合 vintage、bluesy、fuzzy lead [^4_3][^4_4] |
| **Si 矽二極體** | 約 0.6–0.7 V | RAT 經典的緊、兇、清楚顆粒與中高頻咬勁 | 最均衡；riff、punk、grunge、rock lead 都適合 [^4_1][^4_2] |
| **紅 LED** | 約 1.5–2.0 V | 輸出更大、失真量較少、開放、動態清晰、crunch 感強 | 適合當較粗的 overdrive／amp-like distortion；Turbo RAT 的概念就是 LED clipping [^4_1][^4_5] |

## 為何會這樣

二極體的作用是將訊號峰值「限幅」。一對對稱二極體分別處理正、負半週，因此可大致看作可容許的峰對峰擺幅約是 $2V_f$：Ge 約 0.6 Vpp、Si 約 1.4 Vpp、紅 LED 約 3.4–4.0 Vpp。[^4_5]

所以同一個 RAT 的 Distortion 設定下：

- **Ge** 最快碰到天花板，最早飽和，訊號自然被壓平，因此更濃、更壓縮，音量也容易下降。[^4_3][^4_5]
- **Si** 保留更多訊號起伏後才開始削波，因此比 Ge 緊實、攻擊感更明確；這就是經典 RAT 的核心語彙。[^4_1][^4_2]
- **LED** 要更大的訊號才介入，故低到中等增益時最開放、撥弦反應更大，但若把 RAT Gain 開得很高，也可能顯得粗、硬與 gritty。[^4_5]


## 與 Ruetz VR 的搭配

若你會做先前的 **47 Ω + 1 kΩ Ruetz VR**：

- **Ruetz VR + Si**：最實用的通用方案；減少 fizz、保有 RAT 身分，適合當可調式中增益 drive。[^4_1][^4_6]
- **Ruetz VR + LED**：失真級增益已降低，再配高 $V_f$ LED，可能變成輸出很大但 clipping 不多的 boost／edge-of-breakup drive；很適合推已經開始破音的 tube amp。[^4_5][^4_6]
- **Ruetz VR + Ge**：即使回授增益較低，Ge 還是早介入，容易得到厚、軟、壓縮、帶些 fuzz 邊緣的聲音；但輸出餘裕最小。[^4_3][^4_4]


## 改裝建議

最值得的是做成 **三段 clipping switch**：

- Si：原版 RAT。
- LED：Turbo RAT 方向。
- Ge：低門檻、厚壓縮的替代聲音。

若空間與配線允許，採用 **on-on-on DPDT** 切換完整的「Ge／Si／LED 對稱二極體組」會比單純只換一顆可靠；並留意鍺二極體個體差異、漏電與溫度敏感度較高，實際 $V_f$ 最好先用萬用表配對。[^4_3][^4_7]

<span style="display:none">[^4_10][^4_11][^4_12][^4_13][^4_14][^4_15][^4_16][^4_8][^4_9]</span>

<div align="center">⁂</div>

[^4_1]: https://pedalbench.com/learn/clipping-diodes-101

[^4_2]: https://www.guitargear.net.au/articles/clipping-types-explained-diodes-drive-pedal-feel

[^4_3]: https://www.guitarpedalx.com/news/news/a-brief-hobbyist-primer-on-clipping-diodes

[^4_4]: https://uveffects.com/tonelab/clipping-diodes-guide/

[^4_5]: https://puget.audio/blog/germanium-vs-silicon-diodes/

[^4_6]: https://www.madbeanpedals.com/forum/index.php?topic=28475.0

[^4_7]: https://www.diystompboxes.com/smfforum/index.php?topic=57927.0

[^4_8]: https://www.youtube.com/watch?v=D1CUWGW2Yy4

[^4_9]: https://www.youtube.com/watch?v=6WppU72JWE0

[^4_10]: https://www.youtube.com/watch?v=bb_gmhgzLaA

[^4_11]: https://www.youtube.com/watch?v=teS1TK1ZaXI

[^4_12]: https://www.freestompboxes.org/viewtopic.php?t=32837

[^4_13]: https://www.facebook.com/groups/pedalboardsofdoom/posts/10160602512342865/

[^4_14]: https://guitargear.net.au/articles/clipping-diodes-explained-overdrive-tone

[^4_15]: https://forum.pedalpcb.com/threads/the-dreaded-diode-debate.16285/

[^4_16]: https://www.guitarpedalx.com/news/gpx-blog/a-brief-hobbyist-primer-on-clipping-diodes


---

# 非對稱削波 asymmetrical clipping 是什麼

**非對稱削波（asymmetrical clipping）**指訊號的正半週與負半週，被二極體在**不同電壓門檻**限制；因此波形上下兩側不再鏡像對稱。相對地，原版 RAT 的一對反向並聯 Si 二極體，約在正負 0.6–0.7 V 對稱地削波。[^5_1][^5_2]

## 怎麼做出來

最典型的作法是在一個方向放 **1 顆 Si**、另一方向放 **2 顆 Si 串聯**：

```text
正半週：1 × Si    → 約 0.6–0.7 V 開始削波
負半週：2 × Si 串聯 → 約 1.2–1.4 V 開始削波
```

因此一側先被壓平，另一側還能保留更大的擺幅。也能透過不同種類的二極體達成，例如一側 Si、另一側 Ge，或一側 Si、另一側 LED；關鍵不在二極體數量本身，而在正負兩側的總 $V_f$ 不同。[^5_1][^5_3][^5_4]

## 聲音上的改變

非對稱波形會增加**偶次諧波**，同時仍保有不少奇次諧波；玩家通常形容它更有層次、更溫暖、更接近 tube amp 的非線性，而不是對稱硬削波常見的緊、直、鋸齒感。實際差異的幅度仍取決於 gain、拾音器輸出、後級 amp 與 Filter 設定。[^5_5][^5_6][^5_7]


| 削波方式 | 波形與諧波傾向 | 常見聽感 |
| :-- | :-- | :-- |
| **對稱** | 上下削得相近，奇次諧波較突出 | 緊實、聚焦、明確、較 aggressive；原版 RAT 取向 [^5_3][^5_2] |
| **非對稱** | 上下削波門檻不同，增加偶次諧波 | 較開放、豐富、帶 tube-like 感，有時更粗糙或有更多 attack [^5_5][^5_8] |

## 放進 RAT 的實用版本

若改 RAT，我會先試這兩種：

- **1× 1N4148 對 2× 1N4148 串聯**：最可預期的非對稱 Si 選項。一側約 0.65 V、另一側約 1.3 V；保留 RAT 的核心顆粒，但輸出與動態通常比原版對稱 Si 多一點。[^5_3][^5_9]
- **1× Si 對 1× red LED**：不對稱更明顯；Si 端早削波，LED 端保留較高 headroom，會比純 Si 更開放、更有不均勻的粗獷感。[^5_9]

搭配你前面說的 Ruetz VR，建議先從 **1 Si / 2 Si** 開始：Ruetz 已經讓增益下降、低頻更完整，而這組非對稱 Si 能補回一些 RAT 的咬勁與複雜度，通常比直接 Si／LED 更容易控制。[^5_7][^5_3]

<span style="display:none">[^5_10][^5_11][^5_12][^5_13][^5_14][^5_15]</span>

<div align="center">⁂</div>

[^5_1]: https://crazychickenguitarpedals.com/guitar-pedal-blog/general-guitar-pedals/whats-the-difference-between-symmetrical-and-asymmetrical-clipping/

[^5_2]: https://note.com/fumav3/n/nf5ee97059fbd?hl=en

[^5_3]: https://pedalbench.com/learn/clipping-diodes-101

[^5_4]: https://www.guitarpedalx.com/news/news/a-brief-hobbyist-primer-on-clipping-diodes

[^5_5]: https://uveffects.com/tonelab/clipping-diodes-guide/

[^5_6]: https://github.com/cemergin/100x-audio-builder-guide/blob/main/part-1-guitar-pedals/06-gain-stages-clipping-circuits.md

[^5_7]: https://guitarpcb.com/wp-content/uploads/2026/08/How-Gain-Headroom-and-Clipping-Shape-Your-Tone.pdf

[^5_8]: https://www.guitargear.net.au/articles/clipping-types-explained-diodes-drive-pedal-feel

[^5_9]: https://www.reddit.com/r/diypedals/comments/19efzfh/i_need_a_sanity_check_will_this_setup_work_as/

[^5_10]: https://www.scribd.com/document/737376154/A-Clipping-Diode-Primer

[^5_11]: https://crazychickenguitarpedals.com/guitar-pedal-blog/guitar-pedal-components/ultimate-guide-to-diodes-in-guitar-pedals/

[^5_12]: https://guitargear.net.au/articles/clipping-diodes-explained-overdrive-tone

[^5_13]: https://en.wikipedia.org/wiki/ProCo_Rat

[^5_14]: https://www.flux.ai/example-user/modern-distortion-effects-pedal-or-intermediate-example~c1/files/project-architecture-and-design-review~dx

[^5_15]: https://www.reddit.com/r/diypedals/comments/q944nz/proco_rat_diodes_selection/


---

# 那像是 Boss OD-1 是哪種削波

\*\*Boss OD-1 是「非對稱、軟削波（asymmetrical soft clipping）」的 overdrive。\*\*它在 op-amp 的負回授迴路內使用二極體，而不是像 RAT 那樣在 op-amp 輸出端以對地二極體硬削波；這正是它較像 amp break-up、較有動態的原因。[^6_1][^6_2]

## 二極體配置

OD-1 的經典配置是 **一側 1 顆、另一側 2 顆串聯**的 Si 二極體組，常見原始料號是 **1S1588**；可用 1N4148／1N4149 作近似替代。[^6_1][^6_3][^6_4]

```text
一個半週：1 × Si      約 0.6–0.7 V 開始限制
另一半週：2 × Si 串聯  約 1.2–1.4 V 開始限制
```

所以它確實就是前面說的最典型非對稱削波：其中一個半週先被壓縮，反方向則能保留更多擺幅。[^6_5][^6_1]

## 為何不像 RAT

| 特性 | Boss OD-1 | ProCo RAT |
| :-- | :-- | :-- |
| 削波位置 | Op-amp 負回授迴路內 | Op-amp 輸出後、對地二極體網路 |
| 削波形式 | 非對稱 soft clipping | 對稱 hard clipping（原版 Si） |
| 典型感受 | 中頻較集中、自然壓縮、較有 pick dynamics、近 tube breakup | 緊實、兇、顆粒明確、飽和度與 distortion 感較強 [^6_1][^6_6][^6_2] |
| 諧波傾向 | 會產生較多偶次諧波 | 對稱削波下奇次諧波更突出 [^6_7][^6_2] |

BOSS 對 OD-1 的設計說法也正是：利用非對稱削波增加偶次諧波，追求接近已推到破音的真空管 amp 那種溫暖、自然的 breakup。[^6_2]

## 與 SD-1 的關係

SD-1 是 OD-1 概念的延續：同樣採非對稱軟削波，但多了獨立 Tone 控制，因此可更主動處理高頻。OD-1 則只有 **Level** 與 **Over Drive**，沒有 Tone 旋鈕，聲音取向較固定。[^6_8][^6_9]

<span style="display:none">[^6_10][^6_11][^6_12][^6_13][^6_14][^6_15][^6_16][^6_17]</span>

<div align="center">⁂</div>

[^6_1]: https://www.guitarpedalx.com/news/gpx-blog/a-brief-hobbyist-primer-on-clipping-diodes

[^6_2]: https://www.boss.info/us/products/box-40/

[^6_3]: https://www.jazzcaster.com/pedal/od1/lispice-boss-od1/

[^6_4]: https://www.freestompboxes.org/viewtopic.php?t=12176

[^6_5]: https://forum.pedalpcb.com/threads/diode-clipping-question.8040/

[^6_6]: https://note.com/fumav3/n/nf5ee97059fbd?hl=en

[^6_7]: https://uveffects.com/tonelab/clipping-diodes-guide/

[^6_8]: https://www.analogman.com/od1.htm

[^6_9]: https://www.guitarworld.com/features/boss-analog-overdrive-pedals

[^6_10]: https://www.effectsdatabase.com/model/boss/compact/od1

[^6_11]: https://guitarnuts2.proboards.com/thread/10278/comparison-asymmetrical-diodes-regard-clipping

[^6_12]: https://www.hobby-hour.com/electronics/s/od1-overdrive.php

[^6_13]: https://gears-vault.com/models/boss-od-1-overdrive

[^6_14]: http://www.bossareaforum.com/Forum/viewtopic.php?t=585\&start=10

[^6_15]: https://www.reddit.com/r/diypedals/comments/1isqles/asymmetric_clipping_via_using_different_diodes/

[^6_16]: https://www.tdpri.com/threads/asymmetrical-clipping-diode-circuits.4305/

[^6_17]: https://articles.boss.info/all-about-the-ds-1-the-benchmark-boss-distortion/

