# Cipher Pharmaceuticals Inc. (TSX: CPH)

## Status and open items

Version: operating path dated 22 October 2026, rechecked 29 October 2026. Base case is unchanged: FY2026E revenue 52.010 and adjusted EBITDA 31.064; FY2027E revenue 59.721 and adjusted EBITDA 36.484. Yahoo revenue consensus was pulled again on 29 October 2026 and matches E1. No financial filing has been posted since the Q2 report.

Open: the 1 September 2026 court confirmation of the Sun arbitration award (CAD 4.242 million of damages, plus a 15% royalty on Absorica LD net sales in Canada from 2026 through 2040) is not in the revenue or EBITDA path. Cipher had not recognized it at 30 June 2026, and Absorica LD Canada sales are not disclosed, so there is no base to phase the royalty. A joint valuation request is in `collab/valuation_request_v01.json`. It carries the operating leaves only. It does not set a horizon, a tax rate, a cost of debt, working capital, a debt policy, or a distribution policy, because those were not stated in the request. Rebuild the forecast with `build_forecast.py`. Run the joint case with `templates/run_collaborative.py` on the Finagle checkout beside this repo. The report is `report.md`.

Explicit window FY2026 and FY2027; year 0 is FY2025. **Currency: USD millions.** Cipher reports in U.S. dollars [A1]; the only CAD figure is the Yahoo consensus, converted at C3. Tests: `forecast.json` passes `forecastcheck.validate_payload`; it is built by `build_forecast.py`.

Every number has a skill tag letter plus a number (A1, G1, E1, S1, C1...) pointing to the **Numbered sources** list at the end. Page numbers are PDF page numbers (the Q2 2026 report's MD&A pages match its printed page numbers; the notes do not).

## Lines

Cipher reports one segment but discloses revenue by geography and type [A2][A6]. That gives three lines, which add up to the total: **Natroba (U.S. product revenue: Natroba plus its authorized generic Spinosad)**, the **Canadian product portfolio** (Epuris plus Actikerall, Brinavess, Aggrastat, Vaniqa and Durela), and **U.S. licensing** (Absorica and Lipofen royalties and shipments). Line gross margins are disclosed for Natroba and Canada [A9]; the licensing margin is the residual [C8].

## Base forecast

| Line | FY24A | FY25A | YoY | H1 2026A | H2 2026E | FY26E | FY27E | GM used (H2, FY27) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Natroba (U.S.) | 11.950 [A2] | 29.990 [A2] | +151.0% [C1] | 13.187 [A6] | 15.789 [S1] | 28.976 [C6] | 32.689 [S2] | 86% [A9] |
| Canadian portfolio | 14.790 [A2] | 16.907 [A2] | +14.3% [C1] | 9.121 [A6] | 10.157 [S3] | 19.278 [C6] | 23.271 [S4] | 71% [A9] |
| Licensing (U.S.) | 6.623 [A2] | 3.554 [A2] | −46.3% [C1] | 2.264 [A6] | 1.492 [S5] | 3.756 [C6] | 3.761 [S6] | 96.3% [C8] |
| **Revenue** | **33.363** [A1] | **50.451** [A1] | +51.2% [C1] | **24.572** [A5] | **27.438** [C4] | **52.010** [E1] | **59.721** [E1] | |
| Gross margin | 72.2% [C9] | 80.1% [C9] | | 81.4% [A5] | | **81.2%** [C10] | **80.8%** [C10] | |
| **Adj. EBITDA** | **15.684** [A4] | **28.057** [A4] | +78.9% [C1] | **14.552** [A7] | **16.512** [C11] | **31.064** [C11] | **36.484** [S7] | |
| Adj. EBITDA margin | 47.0% [C12] | 55.6% [C12] | | 59.2% [C12] | | **59.7%** [C12] | **61.1%** [C12] | |

FY26 base growth: revenue +3.1%, adjusted EBITDA +10.7%. FY27: revenue +14.8%, adjusted EBITDA +17.4% [C13].

## Totals (step 2a)

- **No guidance.** Cipher gave no revenue or EBITDA range for 2026 [G1]. The only statements about the future are directional: "Our expectations for the product have not changed... We expect performance of the product to improve in future quarters" for Natroba [G2], "we believe the Canadian portfolio will continue its growth" and pCPA listing agreements "expected to be finalized over the next 30 to 60 days" [G3].
- **No coefficient.** With no range, `C` is undefined. The skill's branch for no guidance is to use estimates where they exist. **Revenue total = analyst consensus [E1]**, then the lines are scaled to it (2c). The unscaled line build is only a diagnostic.
- **Consensus [E1]** (Yahoo via yfinance, pulled 2026-10-22, after the Q2 release; 4 analysts on EPS): FY26 CAD 70.849M (range 70.297–71.264), FY27 CAD 81.353M (74.945–92.376). Converted at **1.3622 CAD/USD [C3]**, which is Yahoo's own FY25 CAD "year-ago revenue" (68.725) divided by reported FY25 USD revenue (50.451). In USD that is FY26 **52.010** (51.605–52.315) and FY27 **59.721** (55.017–67.813). No pre-release consensus was available, so the Q2 print is not scored against one. Rechecked 2026-10-29 [E2]: the same CAD averages, lows and highs. The path is not revised.
- **EBITDA:** no guidance and no EBITDA consensus (Yahoo gives revenue and EPS only). EBITDA is the cost build (2e). Flagged.

## Lines, then the scale (2b–2d)

| Line | Pattern | Unscaled H2 | Unscaled FY27 |
|---|---|---:|---:|
| Natroba | Mature/declining, plus the commercial programs management named | H2 2025 15.546 × (1 − 8.7%) = 14.193 [S1] | FY26 27.380 × 1.03 = 28.202 [S2] |
| Canadian portfolio | Ramping (pCPA public coverage) | H2 2025 8.164 × 1.118 = 9.131 [S3] | FY26 18.252 × 1.10 = 20.077 [S4] |
| Licensing | Mature/declining | Flat at H2 2025, 1.341 [S5] | FY26 3.605 × 0.90 = 3.245 [S6] |
| **Total** | | **24.665** | **51.523** |

- **Scale H2 2026 = 27.438 / 24.665 = 1.112 [C5].** Scale FY27 = 59.721 / 51.523 = **1.159 [C7]**. Both are more than 10% from 1: the lines' own commentary does not reach the consensus total, and the lines allocate it. Flagged under 2c.
- **Run rate (2d):** the Q2 Natroba miss (−19% YoY) is treated as **recurring**, because the company attributes it to "a reduction in number of patients covered by Medicaid programs" [A10], a structural change. That is why H2 uses the H1 decline (−8.7%) and not a rebound. The Q2 licensing dip is treated as **one-time timing**, because shipments to partners "are subject to variability from period to period" [G4]. The $0.259M of acquisition costs in Q2 SG&A is a company-flagged one-time item and is excluded from the run rate [A8].

## Costs (2e)

- **Gross margin:** line margins held at H1 2026 levels: Natroba 86%, Canada 71% [A9]. Licensing is the residual, 96.3% [C8]. The total margin moves only with mix. The FY25 total was 80.1% [C9]; H1 2026 was 81.4% [A5].
- **Cash operating cost** = Q2 SG&A 3.439 − share-based compensation 0.323 − acquisition/restructuring 0.259 = **2.857 per quarter [C2]**. R&D is nil and amortization is below gross profit [A8]. Check: Q2 gross profit 9.699 − 2.857 = 6.842, the reported Q2 adjusted EBITDA [A7]. This is the cost that reconciles to adjusted EBITDA, not a GAAP opex line.
- No announced cost step was found. Management is "investing in" the direct-to-patient channel and the Walmart program [G2] but gave no dollars, so none are added (listed as a risk).
- H2 EBITDA = H2 gross profit 22.226 − 2 × 2.857 = 16.512; FY26 = 14.552 + 16.512 = **31.064 [C11]**. FY27 = gross profit 48.255 − 4 × 2.857 × 1.03 = **36.484 [S7]**.
- **There is no 2a EBITDA total to compare against (no guidance, no estimate), so the >10% gap test does not run.** For comparison, the H2 2025 adjusted EBITDA margin was 57.0% (6.968 + 7.317 on 25.051) [A3]; the base H2 2026 margin is 60.2%. The gap is the lower SG&A run rate [A8].

## Scenarios

Three levers: where revenue sits in the consensus range [E1], the line gross margins (bear uses the Q2 line margins of 84% and 70% [A9]), and FY27 cash-opex inflation.

| | Revenue | Line GM | FY27 opex | FY26 rev | FY26 GM | FY26 adj. EBITDA (margin) | FY27 rev | FY27 GM | FY27 adj. EBITDA (margin) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Bear | consensus low | Q2 (84/70) | +8% | 51.605 | 80.4% | 30.325 (58.8%) | 55.017 | 79.3% | 31.295 (56.9%) |
| **Base** | consensus mean | H1 (86/71) | +3% | **52.010** | **81.2%** | **31.064 (59.7%)** | **59.721** | **80.8%** | **36.484 (61.1%)** |
| Bull | consensus high | H1 (86/71) | 0% | 52.315 | 81.2% | 31.311 (59.9%) | 67.813 | 80.8% | 43.366 (63.9%) |

Bear scales 1.096 / 1.068; bull 1.125 / 1.316. All are [C], with inputs E1, A9 and C2.

## Operating-path leaves (written to the file; Finagle not run)

The skill requires these in `forecast.json`, and the validator checks them. They were **not** handed to Finagle and no value was computed. Organic equals total, since no deal is in the window.

| Leaf | Value | Tag |
|---|---|---|
| `ebitda_growth` | +0.1072, +0.1745 | [C13] |
| `sales_growth` | +0.0309, +0.1482 | [C13] |
| `me` | 0.6109 | [C14] |
| `mc` | 0.7095 | [S8] |
| `gsnext` | 0.05 | [S9] |
| `ebitda_basis` | organic | [S10] |
| acquisition status | none | [G5] |

## Assumptions to revise

The moves that change the answer:

1. **Revenue = consensus (E1)** because there is no guidance. It is converted from CAD at 1.3622 (C3); a different rate moves every number proportionally. FY27 scale is 1.16 (bull 1.32).
2. **Natroba H2 −8.7% YoY (S1)**, treating the Medicaid loss as recurring and giving no credit yet for Walmart/direct-to-patient. FY27 +3% (S2) is the only credit for "expect performance... to improve."
3. **Canada +11.8% in H2 (S3) and +10% in FY27 (S4)** from pCPA public listing. No volume or price was given; the FX is assumed constant.
4. **Cash opex flat at 2.857 a quarter (C2), +3% in FY27 (S7)**, with no cost added for the U.S. commercial programs.
5. **Line gross margins at H1 levels (A9)**; licensing at the 96% residual (C8).

Other judgments: licensing flat in H2 (S5) and −10% in FY27 (S6); `mc` (S8); `gsnext` (S9); scenario inflation of 8% / 0%.

## Joint run

The operating leaves above are what the forecast hands to Finagle. The joint request does not add a horizon, tax rate, cost of debt, net operating loss, non-operating assets, working-capital mode, debt policy, or distribution policy. Those are filled only when the request states them. See `collab/valuation_request_v01.json` and the result beside it.

## Numbered sources

**Documents**
- [D1] Cipher Pharmaceuticals, 2025 Annual Report (MD&A and audited financial statements), March 2026: https://www.cipherpharma.com/wp-content/uploads/2026/03/Cipher-Annual-Report-2025.pdf
- [D2] Cipher Pharmaceuticals, Quarterly Report Q2 2026 (MD&A and interim financial statements), filed August 12, 2026: https://www.cipherpharma.com/wp-content/uploads/2026/08/Cipher-Quarterly-Report-Q2-2026.pdf. The same filing is on SEDAR+ (mirror: https://newsfile.futunn.com/public/NN-PersistNoticeAttachment/7781/20260812/SEDAR_PLUS/CSA_SEDAR_PLUS_NOTICE_RECORD_ID_2474478.pdf, mirror not opened).
- [D3] Q2 2026 results press release, August 12, 2026: https://www.newswire.ca/news-releases/cipher-pharmaceuticals-reports-second-quarter-2026-results-817186565.html (HTML; no page numbers)
- [D4] Q2 2026 earnings call transcript, August 12, 2026 (stockanalysis.com): https://stockanalysis.com/quote/tsx/CPH/transcripts/663762-q2-2026/ (HTML; no page numbers)
- [D5] Yahoo Finance analysis page for CPH.TO, figures pulled via yfinance on 2026-10-22 and again on 2026-10-29: https://finance.yahoo.com/quote/CPH.TO/analysis/
- [D6] Q2 2026 earnings call transcript, August 12, 2026 (Alpha Spread): https://www.alphaspread.com/security/tsx/cph/investor-relations/earnings-call/q2-2026 (HTML; no page numbers). Used for the abandoned-acquisition quote (G5). D4 remains the transcript cited for G2–G4.

**Actuals**
- **A1** "Net revenue 50,451 / 33,363" (2025 / 2024, thousands USD); "Total net revenue of $50.5 million for the year ended December 31, 2025 increased by $17.1 million or 51%". D1, p.8. All amounts are "IN THOUSANDS OF U.S. DOLLARS".
- **A2** Segment note 19: "Canada Product revenue 16,907 / 14,790; U.S. Product revenue 29,990 / 11,950; Licensing revenue 3,554 / 6,623; Total net revenue 50,451 / 33,363". D1, p.83.
- **A3** "Cost of products sold 10,029 / 9,260" (2025 / 2024). D1, p.9. Also the quarterly Adjusted EBITDA for Q3 2025 of 7,317 and Q4 2025 of 6,968, and net revenue of 12,833 and 12,218: D2, p.5 ("Key Performance Measures").
- **A4** "Adjusted EBITDA 28,057 / 15,684 / 12,719" (2025 / 2024 / 2023). D1, p.14.
- **A5** YTD Q2 2026: "Net revenue 24,572", "Gross profit 19,996" (gross margin 81%). D2, p.5.
- **A6** Segment note 15, six months to June 30, 2026 (2025): "Canada Product revenue 9,121 (8,743); U.S. Product revenue 13,187 (14,444); Licensing revenue 2,264 (2,213)"; Q2: Canada 4,628 (4,138), U.S. product 6,289 (7,765). D2, p.39.
- **A7** "Adjusted EBITDA 6,842 / 7,586 / 14,552 / 13,772" (Q2 2026 / Q2 2025 / YTD 2026 / YTD 2025). D2, p.13.
- **A8** SG&A breakdown, Q2 2026: "Share-based compensation 323", "Acquisition, restructuring and other costs 259", "Total selling, general and administrative 3,439". D2, p.10. Operating-expense table: "Research and development —", "Depreciation and amortization 1,785". D2, p.8.
- **A9** "Gross margin on Natroba and its authorized generic Spinosad was 86% for the six months ended June 30, 2026"; "was 84% for the three months ended June 30, 2026"; "Gross margin on the Company's Canadian product portfolio was 71% for the six months ended June 30, 2026"; "remained consistent year-over-year at 70% for the three months". D2, p.9.
- **A10** Natroba "decrease... was due to lower sales volumes to Medicaid covered patients in 2026 compared to 2025, arising from a reduction in number of patients covered by Medicaid programs." D2, p.8.

**Guidance and management statements**
- **G1** No numeric 2026 outlook: the Q2 release's "Business Strategy & Outlook" lists only focus areas ("Driving market share growth of Natroba™...", "Acquiring or in-licensing complementary products..."). D3, August 12, 2026. The Q2 MD&A has no outlook range either: D2, pp.1–22, searched.
- **G2** CFO: "Our expectations for the product have not changed despite market dynamics that may emerge over time. We expect performance of the product to improve in future quarters as the implementation of our strategy related to Natroba... takes effect, including an expanded focus on commercial channels." CEO: "investing in and building new business verticals... direct-to-patient platform... a program to have the product available at Walmart." D4, August 12, 2026.
- **G3** CEO: "we believe the Canadian portfolio will continue its growth"; product listing agreements "which we expect to be finalized over the next 30 to 60 days"; "We expect our market share to grow meaningfully in time." D4, August 12, 2026. Also: "Market share of Epuris has decreased to 47.1% at June 30, 2026, from 51.3%... market share has increased throughout the current year-to-date". D2, p.8.
- **G4** CFO: licensing was affected by "reduced product shipments to Cipher's distribution partners, which are subject to variability from period to period." D4, August 12, 2026.
- **G5** Interim CEO, Q2 2026 call: "During the second quarter, we were in advanced stages of a process for an acquisition target. However, ultimately -- we ultimately determined that not continuing with the process was the right decision at this time. Cipher -- and therefore, the deal did not materialize." D6, August 12, 2026. HTML; no page numbers.

**Estimates**
- **E1** Yahoo Finance revenue consensus for CPH.TO, in CAD, pulled via yfinance 2026-10-22: current year avg 70,849,480 (low 70,297,000, high 71,263,950); next year avg 81,352,800 (low 74,944,680, high 92,376,380); "yearAgoRevenue" 68,725,360. D5. The page shows CAD; the conversion is C3.
- **E2** Same Yahoo series, pulled via yfinance 2026-10-29: current year avg 70,849,480 (low 70,297,000, high 71,263,950); next year avg 81,352,800 (low 74,944,680, high 92,376,380). D5. Unchanged from E1.

**Assumptions**
- **S1** Natroba H2 2026 = H2 2025 (A2 − A6 H1 2025 = 15.546) × (1 + H1 2026 YoY of −8.7%), then × C5. Why: the Medicaid volume loss is structural (A10), so H2 does not rebound to flat. The H1 rate rather than Q2's −19% gives some credit to "expect performance... to improve in future quarters" (G2). Price/volume split: the decline is volume (patients), A10.
- **S2** Natroba FY27 = FY26 unscaled × 1.03, then × C7. Why: G2's "improve" plus the Walmart and direct-to-patient programs; "growing" does not set a rate in the wording table, so a low-single-digit step is assumed.
- **S3** Canada H2 2026 = H2 2025 (8.164) × (1 + Q2 YoY +11.8%), then × C5. Why: "momentum continues" reads as holding the latest growth; Q2 was driven by Epuris volume (+8%) and mix (D2 p.8; D4), with pCPA listing ahead (G3). Constant FX (Epuris is sold in CAD, D1 p.9).
- **S4** Canada FY27 = FY26 unscaled × 1.10, then × C7. Why: the first full year of pCPA public listings, where management expects market share "to grow meaningfully in time" (G3). Low-double-digit step; volume effect.
- **S5** Licensing H2 2026 flat at H2 2025 (1.341), then × C5. Why: Q2's dip is shipment timing (G4); H1 2026 was +2% YoY (D2 p.7).
- **S6** Licensing FY27 −10%. Why: Absorica faces a "competitive landscape" that "has contributed to lower" volumes, and its market share fell to 3.4% (D2 p.7; D1 p.8).
- **S7** FY27 adjusted EBITDA = Σ FY27 line revenue × A9/C8 margins − 4 × C2 × 1.03. Why +3%: wage and price inflation on a cost base that management says it is "continuously monitoring" (D4); no cost step was announced.
- **S8** `mc` = average of `me` (C14) and FY27 gross margin (C10) = 0.7095. A judgment for the fade margin; not used here.
- **S9** `gsnext` = 5%. Why: FY27 growth is lifted by scaling (C7); Canada coverage gains and Natroba channel programs (G2, G3) support mid-single-digit growth, but there is no FY28 evidence.
- **S10** `ebitda_basis` = organic. Why: the explicit EBITDA is the existing business. The only process that reached an advanced stage in the quarter did not close (G5), and the path includes no acquired EBITDA.

**Calculations**
- **C1** YoY = current period / prior period − 1 (inputs A1, A2, A4).
- **C2** Cash opex = A8 SG&A 3.439 − SBC 0.323 − acquisition 0.259 = 2.857. Check: A5/A7 Q2 gross profit 9.699 − 2.857 = 6.842 = A7.
- **C3** FX = E1 yearAgoRevenue CAD 68.725 / A1 FY25 USD 50.451 = 1.3622 CAD per USD.
- **C4** H2 2026 revenue = E1 FY26 in USD (70.849 / C3 = 52.010) − A5 24.572 = 27.438.
- **C5** H2 scale = C4 / Σ(S1, S3, S5 unscaled) = 27.438 / 24.665 = 1.112.
- **C6** Line FY26 = A6 H1 + scaled H2.
- **C7** FY27 scale = E1 FY27 in USD (59.721) / Σ(S2, S4, S6 unscaled) = 51.523 → 1.159.
- **C8** Licensing GM = (A5 gross profit 19.996 − 13.187 × 0.86 − 9.121 × 0.71) / 2.264 = 96.3%. Uses rounded A9 margins; flagged.
- **C9** Gross margin = (A1 − A3) / A1: FY25 40.422 / 50.451 = 80.1%; FY24 24.103 / 33.363 = 72.2% (FY24 includes acquired-inventory fair-value charges, D1 p.14).
- **C10** Forecast gross margin = (A5 H1 gross profit + Σ H2 line revenue × A9/C8) / FY26 revenue; FY27 = Σ line revenue × margin / revenue.
- **C11** H2 EBITDA = H2 gross profit − 2 × C2; FY26 = A7 14.552 + H2.
- **C12** EBITDA margin = adjusted EBITDA / revenue.
- **C13** Growth rates from A1, A4, E1, C11, S7.
- **C14** `me` = S7 / E1 FY27.

## Not verified

- E1 is the yfinance pull of Yahoo's page; the analyst names and the as-of date per estimate are not shown. The conversion (C3) relies on Yahoo's own year-ago figure.
- D4 is a third-party transcript (stockanalysis.com), not the company webcast. The quotes for G2–G4 come from that text.
- D6 is a third-party transcript (Alpha Spread), not the company webcast. G5 is taken from that text. The same call is D4.
- The SEDAR+ mirror link in D2 was found in search but not opened; the cipherpharma.com PDF was opened and read.
