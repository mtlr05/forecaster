# Vitalhub Corp. (TSX: VHI)

## Status and open items

Version: **v3, 18 November 2026, 12:55 ET** (America/Toronto). v3 forecasts organic ARR additions in dollars after a review of the ARR bridge trend, prompted by the CEO bot's term-licence product sheet [D24] at David May's request [P8]. v2 (17 Nov, 10:05 ET) added the 2027 SHREWD roll-off after the FDP extension to March 2029 [D23][G26][P7]. v1 and v2 are archived in `v1/` and `v2/`; the change log is `revision_log.md`. Forecaster method commit 3a46f0a61f6b26de1a588acbc941120420d2ec41 (fetched again for v3: already up to date). Source mirror: read-only clone of mtlr05/ceochat at 25246c9 (pulled 18 Nov), companies/vhi/ only; every filing number re-checked against the original SEDAR PDF (via OTC Markets). Valuation: the Finagle bot ran the collaborative valuation on 18 Nov 2026 (finagle-run/valuation_result_v05.json, Finagle 377f177b) with David's stated inputs (P10-P15, including year-0 Adjusted EBITDA 26.554); value per share base C$9.226, bull 11.216, bear 6.827 vs C$6.73 (Yahoo, 18 Nov 2026) [C41]. v01-v03 stopped; v04 superseded (Yahoo year-0 EBITDA). The Forecaster wrote the request and the report section only.

Explicit window FY2026E–FY2029E [P1]; year 0 is FY2025A. **Currency: C$ millions** [P4]. Base FY2026E revenue 129 and Adjusted EBITDA 34.0; FY2029E revenue 161.4 and Adjusted EBITDA 48.3 (29.9% margin).

Open items:
- SHREWD (NHS England, 7–8% of ARR, about 7.5–8.6) [G2][C31]. Base: 4.0 rolls off straight-line in 2027, none after [S26]. Bull 1.5, bear 8.0 [S22].
- Consensus (FactSet via Markets Insider, pulled 17 Nov 2026) is taken to predate the 16 Nov announcement. The base is Consensus plus the SHREWD roll-off effect alone, measured on the v3 build with and without the loss (C36); the raw FactSet figure is kept under `unadjusted` in each total. Whole numbers, no analyst count (8 validator warnings).
- FY2029 base margin 29.9% is above every reported year (FY2024 26.0%, FY2025 24.4%, best quarter 27.6% in Q3 2024); flagged and banded by the bear (24.9%) [P2]. Bottom-up FY2029 EBITDA is 10.3% below the base (0.897), flagged.
- FDP re-procurement (from H2 2027, about 18 months) is upside outside the window and in no case [S28][G27].
- Questions for Dan Matlow (not sent; David relays): how much SHREWD ARR is already removed from the 107.2; which SHREWD modules overlap FDP; whether Vitalhub will bid in the new FDP procurement or the maternity work; net revenue retention; currency mix of ARR; organic growth of acquired books since close vs the legacy book; why term revenue / average ARR fell from about 1.05 to 0.985 after 2024.

Tests: `forecast.json` passes `forecastcheck.validate_payload` (0 errors, 8 warnings: consensus analyst count not recorded). Rebuild with `python3 build_forecast.py`. Every number carries a tag under **Numbered sources**; page numbers are PDF pages.

## Lines

Single operating segment; four reported revenue types that add to total revenue [A3_1][A4_1][A5_1][A1_1]. Buddy (closed 10 Jul 2026) sits inside the term line at its acquired 4.48 of ARR, unscaled [S17][A28_4]. SHREWD sits inside the term line (and the services that ride on it).

## Base forecast

| Line | FY24A | FY25A | 9M26A | Q4 26E | FY26E | FY27E | FY28E | FY29E |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Term licences, maintenance and support | 57.070 | 85.443 | 74.253 | 26.135 | 100.388 | 108.126 | 113.549 | 129.735 |
| Virtual care (Attend Anywhere) | 0.000 | 5.185 | 7.019 | 2.297 | 9.316 | 8.773 | 8.203 | 8.206 |
| Perpetual licences | 0.498 | 2.089 | 1.944 | 0.491 | 2.436 | 1.974 | 1.943 | 2.046 |
| Services, hardware and other | 11.026 | 16.250 | 12.341 | 4.519 | 16.861 | 17.831 | 18.715 | 21.423 |
| **Revenue** | **68.594** [A1] | **108.967** [A1_1] | **95.557** [A1_2] | **33.443** [C5] | **129** [E1] | **136.705** [C36] | **142.410** [C36] | **161.410** [C36] |
| **Adj. EBITDA** | **17.840** [A2] | **26.554** [A2_1] | **24.773** [A2_2] | **9.227** | **34** [E2] | **37.164** [C36] | **41.328** [C36] | **48.328** [C36] |
| Margin | 26.0% | 24.4% | 25.9% | 27.6% | 26.4% | 27.2% | 29.0% | 29.9% |

Growth: revenue +18.4% / +6.0% / +4.2% / +13.3%; Adjusted EBITDA +28.0% / +9.3% / +11.2% / +16.9% [C22][C23]. The FY2028 dip and FY2029 jump come from the FactSet path (+7.8% / +5.8% / +12.9%) [C34].

## Totals (four views)

- **No guidance.** The Q2 2026 10%–11% organic comfort [G13] was not restated on the Q3 call and is treated as withdrawn. Top-down and calibrated top-down are absent; the base is Consensus [E1][E2].
- **Post-pull event.** The skill has no explicit rule for news after the Consensus pull; its preamble lets a prompt instruction override the default method, tagged [P]. David's instruction [P7] plus the FDP extension [D23] is applied as an additive adjustment: base = FactSet + (v3 bottom-up with the 4.0 SHREWD loss − the same build with no loss) for FY2027–29, revenue −2.295 / −4.590 / −4.590 and Adjusted EBITDA −1.836 / −3.672 / −3.672 [C36]. v3 confines the adjustment to the post-pull event; v2 also carried our organic-rate change, which rests on information analysts already had and so belongs in the bottom-up view, not the base. FY2026 is unchanged. Reason the pull is treated as pre-event: it was taken about a day after a statement made to MPs, and the v1 build (SHREWD unresolved, no roll-off) already matched FactSet within 1.2% in FY2026–27, so FactSet does not embed a 2027 roll-off.
- **Bottom-up v3**: revenue 129.58 / 138.45 / 146.48 / 157.90; EBITDA 34.16 / 37.17 / 39.09 / 43.37 (v2 138.94 / 148.38 / 161.75 and 37.41 / 40.04 / 45.30). Bottom-up / base revenue 1.005 / 1.013 / 1.029 / 0.978; EBITDA 1.005 / 1.000 / 0.946 / 0.897. Scale factors on organic lines: Q4 0.9825, FY27 0.987, FY28 0.971, FY29 1.023 (all within 10% of 1).
- **Cash cost check** on base revenue: Q4 −0.5%, FY27 −0.9%, FY28 −4.1%, FY29 −2.8% [C15].

## ARR bridge trend and organic additions (v3)

Printed ARR bridge [A75]–[A78][C38]: organic additions net of churn 6.39 (2023), 6.48 (2024), 7.23 (2025), 8.12 (12 months to Q2 2026), 7.23 (12 months to Q3 2026, with the SHREWD drag). Opening ARR 36.2 / 44.6 / 71.1 / 79.6 / 93.7, so the organic rate fell 17.7% / 14.5% / 10.2% / 10.2% / 7.7%. Acquired ARR 1.10 / 17.9 / 15.9 (and 4.48 Buddy in Q3 2026). Dollar additions rose about 10% a year while 38 of acquired ARR joined the base with little net organic growth in aggregate. Seasonality, 2022–25 average: Q1 1.57, Q2 1.35, Q3 1.28, Q4 1.84; Q3 2026 0.816 was the weakest Q3 since 2022. FX +2.09 (2024), +1.99 (2025), +1.22 (9M 2026), held at zero [S15]. Term revenue / average ARR 0.994 / 0.980 / 0.979 / 0.988 for Q4 2025–Q3 2026, average 0.985, confirming S1; earlier quarters ran 1.01–1.14, highest in acquisition quarters; ARR excludes virtual care [A79][C39]. Term share of revenue 83% FY2024 [A80], 78% FY2025, 81% Q3 2026.

Driver [S29]: organic additions in dollars, base +10% a year from 8.12 = 8.94 / 9.83 / 10.8 (8.2% / 8.7% / 8.8% of opening ARR) [S3]–[S5]; bull +15% a year, bear flat 7.23 [S22]. Q4 2026 add 1.5 [S2]. v2's 9% / 10% of opening ARR implied 9.8–12.6 a year, above any year printed.

## SHREWD roll-off (v2, unchanged in v3)

Base 4.0 of ARR lost straight-line during 2027, about half of 7.5–8.6, none in 2028–29 [S26]. For a loss in 2027: the FDP that displaces SHREWD now runs to March 2029 [G26], and some suspended accounts are still in ARR [G3]. Against a larger loss: SHREWD is "in all different pockets" [G1], and a new FDP is procured from H2 2027, open to UK SMEs and new capability providers, starting with maternity [G27][G28]. Organic additions are measured before the SHREWD loss, so the Q3 drag is not counted twice [S29]. Lost revenue saves only cash cost of sales [S27][G14]. Closing ARR: 108.7 / 113.6 / 123.5 / 134.3 [C28].

## Costs

Cash gross margin 80% [S10]. Core cash opex 17.197 a quarter, +2% a year [S11][S12]. Variable opex 30% of revenue before the SHREWD loss above 127.65 [S13][S27]. Buddy saving 0.5 a year from FY2027 [S14]. FX at zero [S15].

## Scenarios

Levers [S18]: (1) SHREWD roll-off and organic dollar additions, (2) cost build, (3) Attend Anywhere. Scenario = base + (scenario bottom-up − base bottom-up).

- **Bull**: 1.5 SHREWD lost in 2027; Q4 add 2.5; organic additions +15% a year (9.34 / 10.7 / 12.4); VC flat; variable opex 20%; Buddy saving 1.0; no FDP procurement revenue [S22][S28]. Revenue 129.12 / 139.99 / 148.33 / 169.16; EBITDA 34.28 / 41.23 / 48.29 / 57.54.
- **Bear**: all 8.0 SHREWD lost during 2027; Q4 add 0.5; organic additions flat at 7.23; VC −15%; variable opex 40%; no saving [S22]. Revenue 128.88 / 131.35 / 131.54 / 146.40; EBITDA 33.74 / 32.29 / 32.30 / 36.51.
- v2→v3 changes are in C40 (v1→v2 in C37); unscaled bottom-up scenario totals in C33. The v3 bear headline rises vs v2 in FY2028–29 (+0.93 / +3.27 revenue) because the base bottom-up fell while base totals stay on Consensus.

## Operating-path leaves (written to the file; Finagle not run)

sales_growth and ebitda_growth on totals compound the base to FY2029E; me = 29.9% [C24]; mc 0.50 (bull 0.60, bear 0.40) [S16]; gsnext 8.00% (bull 9.21%, bear 5.20%) [S6]. No acquisition after Buddy [C21].

## Year 0, cash and shares

Unchanged from v1. Year-0 cash 57.630 + 61.551 + 0 = **119.181** [C16]; shares **63.232054** million [C17]. Dated items: Buddy cash −12.368 and 75,000 shares (10 Jul 2026); earn-outs paid −0.781; Novari earn-out up to 4.5 at 0.844 (4 Jul 2027); Buddy earn-out up to 7.249 at 0.442 (10 Jan 2029) [S20][S21]. No case goes cash-negative; no raise [C18].

## Assumptions to revise

1. SHREWD roll-off 4.0 in 2027 (band 1.5–8.0) and its timing [S26][S22].
2. Organic ARR additions growing 10% a year in dollars (band 0%–15%; 7.23 flat to 12.4 by FY2029) [S29][S3]–[S5].
3. Variable opex 30% (band 20%–40%) [S13]; fall-through of lost SHREWD revenue 80% [S27].
4. Attend Anywhere −5% a year (band 0% to −15%) [S7].
5. Term revenue / average ARR 0.985 (0.975–0.995) [S1]; services 16.5% of term (15%–19%) [S9].

## Numbered sources

### Documents

- **D1** Vitalhub Corp., Interim MD&A for the three and nine months ended September 30, 2026, filed 2026-11-12 (SEDAR, PDF via OTC Markets; PDF page numbers) (https://www.otcmarkets.com/filing/607877/content)
- **D2** Vitalhub Corp., Interim condensed consolidated financial statements, three and nine months ended September 30, 2026, filed 2026-11-12 (PDF page numbers) (https://www.otcmarkets.com/filing/607876/content)
- **D3** Vitalhub Corp., Annual MD&A for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers) (https://www.otcmarkets.com/filing/538307/content)
- **D4** Vitalhub Corp., Audited consolidated financial statements for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers) (https://www.otcmarkets.com/filing/538304/content)
- **D5** Vitalhub Corp., Annual MD&A for the year ended December 31, 2024, filed 2025-03-27 (PDF page numbers) (https://www.otcmarkets.com/filing/449868/content)
- **D6** Vitalhub Corp., Interim MD&A, three and nine months ended September 30, 2025, filed 2025-11-06 (PDF page numbers) (https://www.otcmarkets.com/filing/505549/content)
- **D7** Vitalhub Corp., Interim MD&A, three and six months ended June 30, 2026, filed 2026-08-06 (PDF page numbers) (https://www.otcmarkets.com/filing/583610/content)
- **D8** Vitalhub Corp., Interim MD&A, three months ended March 31, 2026, filed 2026-05-07 (PDF page numbers) (https://www.otcmarkets.com/filing/560702/content)
- **D9** Vitalhub Corp., Interim MD&A, three and six months ended June 30, 2025, filed 2025-08-07 (PDF page numbers) (https://www.otcmarkets.com/filing/485101/content)
- **D10** Vitalhub Corp., Interim MD&A, three months ended March 31, 2025, filed 2025-05-08 (PDF page numbers) (https://www.otcmarkets.com/filing/462830/content)
- **D11** Vitalhub Corp., Interim MD&A, three and nine months ended September 30, 2024, filed 2024-11-13 (PDF page numbers) (https://www.otcmarkets.com/filing/424935/content)
- **D14** Vitalhub Corp., news release "VitalHub Announces Acquisition of Buddy Healthcare", 2026-07-13 (PDF) (https://www.otcmarkets.com/filing/578190/content)
- **D15** Vitalhub Corp., news release "VitalHub Reports Third Quarter 2026 Results", 2026-11-12 (PDF) (https://www.otcmarkets.com/filing/607875/content)
- **D16** Vitalhub Corp., Annual Information Form for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers) (https://www.otcmarkets.com/filing/538308/content)
- **D19** Vitalhub Corp., news release "VitalHub Announces Expansion of AI Capabilities with Launch of AI Scribe", 2026-09-15 (PDF) (https://www.otcmarkets.com/filing/593890/content)
- **D12** Seeking Alpha, "Vitalhub Corp. (VHI:CA) Q3 2026 Earnings Call Transcript", call held 2026-11-13 (HTML; no page numbers; text read from the ceochat mirror companies/vhi/sources/calls/seeking-alpha/2026-Q3.md at commit 8f8b44f; Seeking Alpha link unverified) (https://seekingalpha.com/article/4967874-vitalhub-corp-vhi-ca-q3-2026-earnings-call-transcript)
- **D13** Seeking Alpha, "Vitalhub Corp. (VHI:CA) Q2 2026 Earnings Call Transcript", call held 2026-08-07 (HTML; no page numbers; text read from the ceochat mirror 2026-Q2.md; link unverified) (https://seekingalpha.com/article/4933144-vitalhub-corp-vhi-ca-q2-2026-earnings-call-transcript)
- **D17** Markets Insider, "Vitalhub Estimates in CAD" (source: FactSet), pulled 2026-11-17; the Q3 2026 column shows as reported, so the pull is post-release (HTML; no page numbers) (https://markets.businessinsider.com/stocks/vhibf-stock)
- **D18** StockAnalysis, "Vitalhub (TSX:VHI) Stock Forecast" (S&P Global Market Intelligence), last updated 2026-11-17 (HTML) (https://stockanalysis.com/quote/tsx/VHI/forecast/)
- **D21** MarketBeat via Yahoo Finance, "What Vitalhub (VHI) Said on Its Q3 Earnings Call", 2026-11-13 (HTML; secondary cross-check of D12) (https://finance.yahoo.com/healthcare/articles/vitalhub-vhi-said-q3-earnings-221424315.html)
- **D23** The Register (Lindsay Clark), "MPs ask what the break clause was for as Palantir wins two more years in the NHS", published 17 Nov 2026 10:15 UTC (HTML; no page numbers; fetched 17 Nov 2026) (https://www.theregister.com/public-sector/2026/11/17/mps-ask-what-the-break-clause-was-for-as-palantir-wins-two-more-years-in-the-nhs/5310348)
- **D24** Dan Matlow CEO bot product sheet "Term licences, maintenance and support" (ceochat companies/vhi/sources/products/term-licences-maintenance-and-support.md at commit 25246c9, read 18 Nov 2026): TLMS revenue 2019 Q1-2026 Q3 and the ARR bridge by quarter, each row citing the printed SEDAR filing (OTC Markets URL). Used as an index; figures cited here were checked in the filings D1, D3, D5 (link unverified) (https://github.com/mtlr05/ceochat/blob/main/companies/vhi/sources/products/term-licences-maintenance-and-support.md)
- **D25** Finagle valuation result v05 for VHI.TO (finagle-run/valuation_result_v05.json; request valuation_request_v05.json, sha256 ba766900bf9dd16f1178d9a00f12325b518624426d9b84fca32e4a52509b6446), run by the Finagle bot on 18 Nov 2026 14:33 ET with mtlr05/finagle at commit 377f177b4013e713fe7c4603962e5f883a67e298; notebooks notebook_base/bull/bear_v05.py in the same folder (https://github.com/mtlr05/finagle)
- **D26** Yahoo Finance quote for VHI.TO as fetched by Finagle (results v04/v05, price_date 2026-11-18, v04 and v05): C$6.73, Yahoo previous close (HTML/API) (https://finance.yahoo.com/quote/VHI.TO/)
- **D27** Bank of Canada Valet, BD.CDN.10YR.DQ.YLD, Government of Canada 10-year benchmark bond yield: 3.81% on 16 Nov 2026 (JSON, read 18 Nov 2026) (https://www.bankofcanada.ca/valet/observations/BD.CDN.10YR.DQ.YLD/json?recent=5)
- **D22** Dan Matlow CEO bot (David May's CEO-simulation bot for Vitalhub), answers relayed 17 Nov 2026; simulated view built from public material, not company disclosure (link unverified) (https://github.com/mtlr05/ceochat/tree/main/companies/vhi)

### Actuals

- **A3** Term licences, maintenance and support, FY2024: C$57,070,350 (reported). (D5; p.6)
- **A3_1** Term licences, maintenance and support, FY2025: C$85,442,864 (reported). (D3; p.6)
- **A3_2** Term licences, maintenance and support, nine months to 30 Sep 2026: C$74,252,927 (reported). (D1; p.6)
- **A4** No virtual care revenue before the Induction acquisition (June 2025); FY2025 MD&A shows prior-year virtual care of 0. (D3; p.7)
- **A4_1** Virtual care term licences (Attend Anywhere), FY2025: C$5,184,921 (reported). (D3; p.7)
- **A4_2** Virtual care term licences (Attend Anywhere), nine months to 30 Sep 2026: C$7,018,965 (reported). (D1; p.7)
- **A5** Perpetual licences, FY2024: C$498,274 (reported). (D5; p.7)
- **A5_1** Perpetual licences, FY2025: C$2,089,242 (reported). (D3; p.7)
- **A5_2** Perpetual licences, nine months to 30 Sep 2026: C$1,944,450 (reported). (D1; p.7)
- **A6** Services, hardware and other, FY2024: C$11,025,686 (reported). (D5; p.7)
- **A6_1** Services, hardware and other, FY2025: C$16,249,891 (reported). (D3; p.7)
- **A6_2** Services, hardware and other, nine months to 30 Sep 2026: C$12,341,147 (reported). (D1; p.7)
- **A1** Revenue FY2024: C$68,594,310. (D5; p.5)
- **A1_1** Revenue FY2025: C$108,966,918. (D3; p.5)
- **A1_2** Revenue nine months to 30 Sep 2026: C$95,557,489. (D1; p.5)
- **A2** Adjusted EBITDA FY2024: C$17,840,272. (D5; p.5)
- **A2_1** Adjusted EBITDA FY2025: C$26,554,099. (D3; p.5)
- **A2_2** Adjusted EBITDA nine months to 30 Sep 2026: C$24,772,636. (D1; p.5)
- **A63** Gross profit FY2024 C$55,494,433, 81% of revenue. (D5; p.6)
- **A63_1** Gross profit FY2025 C$87,588,361, 80% of revenue. (D3; p.6)
- **A63_2** Gross profit nine months 2026 C$76,400,633, 80% of revenue. (D1; p.6)
- **A20** Q3FY24 revenue: C$16,509,135. (D11; p.5)
- **A21** Q3FY24 Adjusted EBITDA: C$4,554,597. (D11; p.5)
- **A22** Q3FY24 term licences, maintenance and support: C$13,892,323. (D11; p.5)
- **A23** Q3FY24 virtual care: C$0. (D11; page unverified)
- **A24** Q3FY24 perpetual licences: C$293,397. (D11; p.7)
- **A25** Q3FY24 services, hardware and other: C$2,323,415. (D11; p.7)
- **A26** Q3FY24 closing ARR: C$53,452,108 (ARR bridge, non-IFRS section). (D6; p.5)
- **A27** Q3FY24 organic ARR net of churn: C$1,081,181 (ARR bridge, non-IFRS section). (D6; p.11)
- **A28** Q3FY24 acquired ARR: C$0 (ARR bridge, non-IFRS section). (D6; p.11)
- **A29** Q3FY24 foreign currency loss (gain) inside Adjusted EBITDA: C$-323,458. (D11; p.6)
- **A20_1** Q4FY24 revenue: C$20,590,779. (D5; p.5)
- **A21_1** Q4FY24 Adjusted EBITDA: C$5,046,758. (D5; p.5)
- **A22_1** Q4FY24 term licences, maintenance and support: C$17,673,596. (D5; p.6)
- **A24_1** Q4FY24 perpetual licences: C$60,875. (D5; p.7)
- **A25_1** Q4FY24 services, hardware and other: C$2,856,308. (D5; p.7)
- **A26_1** Q4FY24 closing ARR: C$71,054,210 (ARR bridge, non-IFRS section). (D1; p.10)
- **A27_1** Q4FY24 organic ARR net of churn: C$2,609,657 (ARR bridge, non-IFRS section). (D1; p.10)
- **A28_1** Q4FY24 acquired ARR: C$14,600,000 (ARR bridge, non-IFRS section). (D1; p.10)
- **A29_1** Q4FY24 foreign currency loss (gain) inside Adjusted EBITDA: C$384,805. (D5; p.6)
- **A20_2** Q1FY25 revenue: C$21,674,966. (D10; p.5)
- **A21_2** Q1FY25 Adjusted EBITDA: C$5,614,686. (D10; p.5)
- **A22_2** Q1FY25 term licences, maintenance and support: C$18,343,566. (D10; p.6)
- **A24_2** Q1FY25 perpetual licences: C$157,183. (D10; p.7)
- **A25_2** Q1FY25 services, hardware and other: C$3,174,217. (D10; p.7)
- **A26_2** Q1FY25 closing ARR: C$73,687,666 (ARR bridge, non-IFRS section). (D1; p.10)
- **A27_2** Q1FY25 organic ARR net of churn: C$1,777,442 (ARR bridge, non-IFRS section). (D1; p.10)
- **A29_2** Q1FY25 foreign currency loss (gain) inside Adjusted EBITDA: C$-694,407. (D10; p.6)
- **A20_3** Q2FY25 revenue: C$23,857,548. (D9; p.5)
- **A21_3** Q2FY25 Adjusted EBITDA: C$6,304,647. (D9; p.5)
- **A22_3** Q2FY25 term licences, maintenance and support: C$19,894,544. (D9; p.6)
- **A23_1** Q2FY25 virtual care: C$324,477. (D9; p.7)
- **A24_3** Q2FY25 perpetual licences: C$965,281. (D9; p.7)
- **A25_3** Q2FY25 services, hardware and other: C$2,673,246. (D9; p.7)
- **A26_3** Q2FY25 closing ARR: C$79,589,081 (ARR bridge, non-IFRS section). (D1; p.10)
- **A27_3** Q2FY25 organic ARR net of churn: C$1,860,849 (ARR bridge, non-IFRS section). (D1; p.10)
- **A28_2** Q2FY25 acquired ARR: C$3,870,000 (ARR bridge, non-IFRS section). (D1; p.10)
- **A29_3** Q2FY25 foreign currency loss (gain) inside Adjusted EBITDA: C$-353,294. (D9; p.6)
- **A20_4** Q3FY25 revenue: C$32,044,030. (D6; p.5)
- **A21_4** Q3FY25 Adjusted EBITDA: C$7,206,257. (D6; p.5)
- **A22_4** Q3FY25 term licences, maintenance and support: C$23,627,391. (D6; p.6)
- **A23_2** Q3FY25 virtual care: C$2,479,354. (D6; p.7)
- **A24_4** Q3FY25 perpetual licences: C$454,565. (D6; p.7)
- **A25_4** Q3FY25 services, hardware and other: C$5,482,720. (D6; p.7)
- **A26_4** Q3FY25 closing ARR: C$93,693,789 (ARR bridge, non-IFRS section). (D1; p.5)
- **A27_4** Q3FY25 organic ARR net of churn: C$1,711,335 (ARR bridge, non-IFRS section). (D1; p.10)
- **A28_3** Q3FY25 acquired ARR: C$12,000,000 (ARR bridge, non-IFRS section). (D1; p.10)
- **A29_4** Q3FY25 foreign currency loss (gain) inside Adjusted EBITDA: C$69,042. (D6; p.6)
- **A20_5** Q4FY25 revenue: C$31,390,374. (D3; p.5)
- **A21_5** Q4FY25 Adjusted EBITDA: C$7,428,508. (D3; p.5)
- **A22_5** Q4FY25 term licences, maintenance and support: C$23,577,363. (D3; p.6)
- **A23_3** Q4FY25 virtual care: C$2,381,090. (D3; p.7)
- **A24_5** Q4FY25 perpetual licences: C$512,213. (D3; p.7)
- **A25_5** Q4FY25 services, hardware and other: C$4,919,708. (D3; p.7)
- **A26_5** Q4FY25 closing ARR: C$96,149,750 (ARR bridge, non-IFRS section). (D1; p.10)
- **A27_5** Q4FY25 organic ARR net of churn: C$1,881,405 (ARR bridge, non-IFRS section). (D1; p.10)
- **A29_5** Q4FY25 foreign currency loss (gain) inside Adjusted EBITDA: C$316,191. (D3; p.6)
- **A20_6** Q1FY26 revenue: C$31,906,402. (D8; p.5)
- **A21_6** Q1FY26 Adjusted EBITDA: C$7,989,761. (D8; p.5)
- **A22_6** Q1FY26 term licences, maintenance and support: C$23,927,139. (D8; p.6)
- **A23_4** Q1FY26 virtual care: C$2,398,653. (D8; p.7)
- **A24_6** Q1FY26 perpetual licences: C$995,851. (D8; p.7)
- **A25_6** Q1FY26 services, hardware and other: C$4,584,759. (D8; p.7)
- **A26_6** Q1FY26 closing ARR: C$99,078,809 (ARR bridge, non-IFRS section). (D1; p.10)
- **A27_6** Q1FY26 organic ARR net of churn: C$2,729,378 (ARR bridge, non-IFRS section). (D1; p.10)
- **A29_6** Q1FY26 foreign currency loss (gain) inside Adjusted EBITDA: C$238,091. (D8; p.6)
- **A20_7** Q2FY26 revenue: C$31,737,512. (D7; p.5)
- **A21_7** Q2FY26 Adjusted EBITDA: C$8,162,917. (D7; p.5)
- **A22_7** Q2FY26 term licences, maintenance and support: C$24,542,042. (D7; p.6)
- **A23_5** Q2FY26 virtual care: C$2,282,218. (D7; p.7)
- **A24_7** Q2FY26 perpetual licences: C$808,087. (D7; p.7)
- **A25_7** Q2FY26 services, hardware and other: C$4,105,165. (D7; p.7)
- **A26_7** Q2FY26 closing ARR: C$101,533,157 (ARR bridge, non-IFRS section). (D1; p.5)
- **A27_7** Q2FY26 organic ARR net of churn: C$1,802,495 (ARR bridge, non-IFRS section). (D1; p.10)
- **A20_8** Q3FY26 revenue: C$31,913,575. (D1; p.5)
- **A21_8** Q3FY26 Adjusted EBITDA: C$8,619,958. (D1; p.5)
- **A22_8** Q3FY26 term licences, maintenance and support: C$25,783,746. (D1; p.6)
- **A23_6** Q3FY26 virtual care: C$2,338,094. (D1; p.7)
- **A24_8** Q3FY26 perpetual licences: C$140,512. (D1; p.7)
- **A25_8** Q3FY26 services, hardware and other: C$3,651,223. (D1; p.7)
- **A26_8** Q3FY26 closing ARR: C$107,194,390 (ARR bridge, non-IFRS section). (D1; p.5)
- **A27_8** Q3FY26 organic ARR net of churn: C$815,535 (ARR bridge, non-IFRS section). (D1; p.5)
- **A28_4** Q3FY26 acquired ARR: C$4,480,000 (ARR bridge, non-IFRS section). (D1; p.5)
- **A29_7** Q3FY26 foreign currency loss (gain) inside Adjusted EBITDA: C$-592,126. (D1; p.6)
- **A40** Cash and cash equivalents 31 Dec 2025: C$57,629,569. (D4; p.9)
- **A41** Short-term investments 31 Dec 2025: C$61,551,056. (D4; p.9)
- **A62** No equity offering in 2026: nine-month 2026 financing cash flow of C$167,507 "relates primarily to proceeds from the exercise of options, net of principal payments on lease liabilities"; the prior-year period held the January and August 2025 offerings. (D1; p.9)
- **A42** 63,232,054 common shares issued and outstanding at 31 Dec 2025 (shown as the comparative in the Q3 2026 MD&A). (D1; p.9)
- **A43** 63,472,236 common shares at 30 Sep 2026 (option exercises and 75,000 Buddy shares). (D1; p.9)
- **A44** Cash and cash equivalents and short-term investments at 30 Sep 2026: C$129,007,023; no debt. (D1; p.5)
- **A64** As at September 30, 2026 the Company "has no debt outstanding"; Scotia C$5 operating line and C$60 revolving facility undrawn. (D1; p.10)
- **A45** Buddy acquired July 10, 2026; cash consideration on closing C$12,367,916 (after the 31 Dec 2025 year-0 balance). (D2; p.8)
- **A45_1** Buddy cash consideration on closing C$12,367,916, recorded as -12.368. (D2; p.8)
- **A46** 75,000 shares issued at $7.36/share on the Buddy close. (D2; p.8)
- **A46_1** 75,000 shares issued at $7.36/share. (D2; p.8)
- **A47** Issue price $7.36 per share (filing price). (D2; p.8)
- **A48** Payments of contingent consideration (781,053) in the nine months to 30 Sep 2026. (D2; p.6)
- **A49** Novari: "remaining potential performance-based consideration payable of up to $4,500,000 ... in the 24-month period following the acquisition. A balance of $3,800,000 is accrued". (D2; p.8)
- **A51** Buddy: "remaining potential performance-based consideration payable of up to $7,248,555, if certain revenue targets are met in the 30-month period following the acquisition"; fair value at close C$3,205,624. (D2; p.9)
- **A53** FY2025 revenue by geography: United Kingdom 60,045,988; Canada 33,145,120; Australia 10,243,026; United States 3,336,556; Western Asia 1,522,928; rest of the world 673,300 (C$). (D4; p.26)
- **A54** Q3 2026 revenue by geography: United Kingdom 14,643,256 vs 16,571,510 in Q3 2025; Finland 1,200,877 (Buddy, new) (C$). (D2; p.12)
- **A55** AIF: Dan Matlow, President and Chief Executive Officer since May 2016, director since November 28, 2016, holds 726,862 common shares; previously CEO of Medworxx Solutions, sold to Aptean in 2015. (D16; p.18)
- **A56** AIF: directors and executive officers as a group own 10,231,462 common shares (about 16% of shares outstanding). (D16; p.18)
- **A57** Equity raises in 2025: 9 Jan 2025 bought deal of 3,165,145 shares at $10.90, gross $34,500,080; 20 Aug 2025 bought deal of 5,885,828 shares at $12.70, gross $74,750,016. No share issue for cash in 2026. (D2; p.10)
- **A58** Acquisitions in 2025: Induction Healthcare Group (closed June 18, 2025) and Novari Health (closed July 4, 2025). (D4; p.20)
- **A59** Q3 2026 cash opex lines: G&A 6,327,731; S&M 3,378,727; R&D 7,490,494 (vs 9,237,648 in Q3 2025); 9M 2026 G&A 17,181,503, S&M 9,618,629 and R&D 24,994,218. (D1; p.6)
- **A60** Cash from operating activities, nine months to 30 Sep 2026: 23,903,389. (D1; p.9)
- **A61** Q3 2026 SBC 443,746; depreciation and amortization 4,016,116; business acquisition, restructuring and integration costs 1,368,107; net income 2,589,013. (D1; p.8)
- **A65** Deferred revenue 50,553,871 at 30 Sep 2026. (D1; p.6)
- **A66** Term licences, maintenance and support were 81% of revenues in Q3 2026. (D1; p.7)
- **A67** Q4 2025 cash opex: G&A 6,024,677; S&M 2,672,840; R&D 8,459,901. (D3; p.6)
- **A68** Q1 2026 cash opex: G&A 5,764,464; S&M 3,015,286; R&D 9,037,069. (D8; p.6)
- **A69** Buddy release: up-front consideration of approximately EUR 8.6 million, plus an earn-out of up to EUR 4.5 million. (D14; p.1)
- **A70** AI Scribe launch release (15 Sep 2026): serviceable base of about 22,000 practitioners in the installed base. (D19; p.1)
- **A71** Credit facilities: Scotiabank operating line and a $60,000,000 revolving acquisition facility; no amount drawn at 30 Sep 2026. (D1; p.10)
- **A72** FY2025 gross profit 87,588,361, 80% of revenue (FY2024 81%); Q3 2026 gross margin 79%, nine months 2026 80%. (D3; p.6)
- **A73** Q3 2026 release: VitalHub is headquartered in Toronto with over 700 employees globally. (D15; p.3)
- **A74** FY2025 cash opex: G&A 22,458,560; S&M 10,281,531; R&D 28,950,760. (D3; p.6)
- **A75** Organic net of churn in ARR by year: 2024 6,475,919 (15%) and acquisition growth 17,911,500 (40%); 2023 quarters 1,462,767 / 1,491,003 / 1,475,975 / 1,959,986 (sum 6,389,731); FX effect 2023 926,600 / (116,818) / 127,489 / 1,587 and 2024 652,250 / (39,000) / 1,087,357 / 392,445. (D5; p.11)
- **A76** ARR at December 31, 2024 was 71,054,210 against 44,573,739 at December 31, 2023 (+59%), with organic growth 6,475,919 and acquisitions 17,911,500. (D5; p.5)
- **A77** FY2025 organic growth 7,231,031 (10%) and acquisition growth 15,870,000 (22%) for the movement from December 31, 2024. (D3; p.5)
- **A78** Organic ARR growth September 30, 2025 to September 30, 2026: 7,228,813, printed as 8%; quarterly FX effects Q4 2025-Q3 2026 574,556 / 199,681 / 651,853 / 365,698. (D1; p.5)
- **A79** ARR excludes perpetual license and virtual care revenue. (D6; p.11)
- **A80** Term licenses, maintenance and support represented 83% of revenues for the year ended December 31, 2024. (D5; p.7)
- **A81** FY2025 depreciation and amortization 11,081,525 = depreciation of property and equipment 713,788 + depreciation of right-of-use assets 557,770 + amortization of intangible assets 9,809,967. (D4; p.10)
- **A82** FY2025 purchase of property and equipment 423,144 (FY2024 883,719). (D4; p.12)

### Guidance and management statements

- **G1** Matlow (Q3 2026 call): "I still think there's close to about $10 million or so-ish of SHREWD revenue that's still out there to a degree in all different pockets of it that are there. But it's hard to say which ones are not at risk or at risk". (D12; page unverified)
- **G2** Matlow (Q3 2026 call): "Take that back, Paul. 7%, 8% of our ARR number, not our revenue number." (D12; page unverified)
- **G3** Matlow (Q3 2026 call), on whether suspended SHREWD accounts were removed from ARR: "In some of the cases, yes, in some of the cases, no." and "I think we'll know more in another quarter or so how that comes out". (D12; page unverified)
- **G4** Matlow (Q3 2026 call): "I do believe if we didn't have the suspensions or the reversals on some of those SHREWD cuts, we would have been very close to our Rule of 40 base level". (D12; page unverified)
- **G5** Matlow (Q3 2026 call), asked about a path to Rule of 40 in 2027: "Yes, we think so. We do believe that's the case. Margins will continue to increase, and we're seeing real pipelines". (D12; page unverified)
- **G6** Matlow (Q3 2026 call): "We're comfortable that we're going to sustain, if not improve that number on a quarter-over-quarter basis at this stage." (D12; page unverified)
- **G7** Matlow (Q3 2026 call): "our backlog for our services revenue has never been stronger" and "we do think there's a lot more milestones that should be hit in Q4 than in Q3." (D12; page unverified)
- **G8** Matlow (Q3 2026 call): "I think we should be able to get that Novari product well over the $20 million in ARR numbers. And Strata ... we see another $3 million to $5 million in the pipeline of some stuff that could happen over the next couple of years." (D12; page unverified)
- **G9** Matlow (Q3 2026 call), on Attend Anywhere declining moderately: "Theoretically, yes. ... we also see some new deals cooking on it that maybe offset some of that stuff. ... all that stuff gets renewed in the March time frame". (D12; page unverified)
- **G10** Matlow (Q3 2026 call), on Buddy margins: "It will be through both a combination of a little bit of cost reduction and revenue generation ... Typically, we say it takes 6 months to 1 year and probably that would be the same here." (D12; page unverified)
- **G11** Goffenberg (Q3 2026 call), on R&D: "we're constantly trying to reduce R&D ... some areas we're going to be adding as we do more work on AI ... Probably continue in the same level going forward." (D12; page unverified)
- **G12** Matlow (Q3 2026 call): "with any luck, we'll be able to get another one over the finish line before the end of the year ... there are 2 or 3 companies that we have earmarked since the very beginning that are now in market". (D12; page unverified)
- **G13** Matlow (Q2 2026 call, 7 Aug 2026), replying to an analyst who noted no formal ARR guidance and a 10%-11% run rate: "we still feel comfortable with the rest of our business that we -- even with that headwind that we should still be in the range where we were this quarter and above it for sure ... we're still getting 10%, 11% organic growth." Not restated on the Q3 2026 call (D12). (D13; page unverified)
- **G14** Matlow (Q2 2026 call): "every $1 million of ARR theoretically if we don't add more costs, that's a point of adjusted EBITDA, right? And we're still not completed on the other side of some reductions." (D13; page unverified)
- **G15** Goffenberg (Q2 2026 call), on gross margin: "I think we're still, I think, continue to be probably to be the 80% line." (D13; page unverified)
- **G16** Buddy release (13 Jul 2026): "As at June 30, 2026, Buddy Healthcare had Annual Recurring Revenue of approximately EUR 2.8 million and is approximately Adjusted EBITDA breakeven." (D14; page unverified)
- **G17** Goffenberg (Q3 2026 call): "The increase was primarily due to lower research and development expenses, synergies from the integration of Induction and Novari and a favorable foreign exchange impact in the quarter." (D12; page unverified)
- **G18** Matlow (Q3 2026 call): "They have a break clause in their contract for February of 2027 that they can exercise on the Palantir product." (D12; page unverified)
- **G19** Matlow (Q3 2026 call), on Ontario: "The imaging world ... has gone live ... We expect to continue that work through 2027." (D12; page unverified)
- **G20** Matlow (Q3 2026 call), on no NCIB purchases through September: "I think it's more of the latter" (preserving flexibility for larger M&A). (D12; page unverified)
- **G21** Matlow (Q3 2026 call): "we believe just by adding AI products into our installed base, there's probably about $30 million, $40 million of TAM just on top of that." (D12; page unverified)
- **G22** Matlow (Q2 2026 call), on larger deals: "I think meaningful larger than Novare to a degree, not that much larger but meaningful larger". (D13; page unverified)
- **G23** Q3 2026 MD&A: Adjusted EBITDA = EBITDA + share-based and deferred share-based compensation + business acquisition, restructuring and integration costs + change in fair value of contingent consideration; foreign currency gains and losses stay inside Adjusted EBITDA. "The increase in Adjusted EBITDA was primarily attributable to lower research and development expenses and a favourable foreign exchange impact". (D1; page unverified)
- **G24** Q3 2026 MD&A: ARR "is defined as annual renewable software licence fees and maintenance services"; acquisition revenue is "the annual contract value of recurring revenues of the acquired companies at the time of acquisition"; organic growth is "the revenue over and above the acquisition revenues". (D1; page unverified)
- **G25** Goffenberg (Q3 2026 call): "Services revenue is seasonally lighter over the summer against elevated projected activity in the prior year period." (D12; page unverified)
- **G26** The Register (17 Nov 2026): "Health minister James Frith told MPs on Monday that the current contract would continue until March 2029 as the government procures a new version of the Federated Data Platform (FDP)." The February 2027 break clause is therefore not exercised. (D23; page unverified)
- **G27** The Register (17 Nov 2026): "The formal process is set to start during the second half of next year and take around 18 months"; the new iteration would "welcome international and UK capability alike - whether that is UK small and medium-sized enterprises that want a crack at NHS contracts, sovereign AI-backed capability in the UK or any international provider worth merit." (D23; page unverified)
- **G28** The Register (17 Nov 2026), Frith: "We will also start work, alongside the new procurement, with different providers on developing new capabilities and expertise starting with systems used in maternity care." Frith also said migration was "possible in principle" under the contracts' exit and transition provisions. (D23; page unverified)

### Estimates

- **E1** FactSet consensus revenue FY26E: 129 (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page. (D17; page unverified)
- **E2** FactSet consensus EBITDA FY26E: 34 (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown. (D17; page unverified)
- **E1_1** FactSet consensus revenue FY27E: 139 (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page. (D17; page unverified)
- **E2_1** FactSet consensus EBITDA FY27E: 39 (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown. (D17; page unverified)
- **E1_2** FactSet consensus revenue FY28E: 147 (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page. (D17; page unverified)
- **E2_2** FactSet consensus EBITDA FY28E: 45 (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown. (D17; page unverified)
- **E1_3** FactSet consensus revenue FY29E: 166 (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page. (D17; page unverified)
- **E2_3** FactSet consensus EBITDA FY29E: 52 (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown. (D17; page unverified)

### Assumptions

- **S1** Term revenue = 0.985 x average closing ARR. Basis: Q2 2026 term 24.542 x 4 / average ARR (99.079, 101.533) = 0.979; Q3 2026 25.784 x 4 / average (101.533, 107.194) = 0.988; average 0.984 rounded to 0.985. Band 0.975-0.995.
- **S2** Q4 2026 organic net ARR add of 1.5 (base). Q4 is a stronger selling quarter than Q3 (Q4 2024 +2.61, Q4 2025 +1.88) but SHREWD suspensions continue (G1, G3); the FDP extension (G26) puts the SHREWD roll-off in 2027 rather than Q4 2026. Bull 2.5, bear 0.5.
- **S3** FY2027 organic ARR adds 8.94 before the SHREWD roll-off (base): the 8.123 of organic adds in the four quarters to Q2 2026 (the last four before the Q3 SHREWD drag, A27_4-A27_7) grown 10%, the trend in dollar adds (S29). As a share of opening ARR this is 8.2%; net of the 4.0 roll-off FY2027 closing ARR grows 4.5%. v2 used 9% of opening ARR (9.8 of adds), above any year Vitalhub has printed. Band 7.23 (bear, flat at FY2025) to 9.34 (bull, +15%).
- **S4** FY2028 organic ARR adds 9.83 (base), the dollar trend continued at +10% (S29); 8.7% of opening ARR. The Novari and Strata pipelines and AI add-ons (G8, G21) and the Rule of 40 aim (G5) support continued growth in dollar adds; the withdrawn 10%-11% comfort (G13) argues against a step-up beyond the trend, so the trend rate is used unchanged. No further SHREWD loss (S26). Band 7.23 (bear) to 10.74 (bull).
- **S5** FY2029 organic ARR adds 10.81 (base), +10% again; 8.8% of opening ARR. Band 7.23 (bear) to 12.35 (bull).
- **S6** FY2030 (gsnext year) organic ARR adds 11.89 base (bull 14.21, bear 7.23), one more year of the same dollar-add build; no management phrase reaches 2030.
- **S7** Virtual care (Attend Anywhere) declines 5% a year from FY2027: management expects a moderate decline offset by some new deals, renewals in March (G9); Q3 2026 was -6% YoY. Band 0% (bull) to -15% (bear).
- **S8** Perpetual licences 0.5 in Q4 2026 (Q4 2025 0.512) and 2.0 a year thereafter, about the FY2025-FY2026 average; term licences are the preferred model (D1).
- **S9** Services, hardware and other: Q4 2026 4.6 (back to the Q1 2026 level of 4.585; management expects more Q4 milestones, G7) and 16.5% of term revenue thereafter (9M 2026 ratio 16.6%; FY2025 19.0%). Band 15%-19%.
- **S10** Cash gross margin 80% (9M 2026 80%; CFO "80% line", G15). Cost of sales holds no D&A or SBC (D1). Band 78%-82%.
- **S11** Core cash opex = Q3 2026 G&A 6.328 + S&M 3.379 + R&D 7.490 = 17.197 a quarter (ex SBC, D&A, FX, one-time), annualized 68.79; includes Buddy for 82 of 92 days.
- **S12** Core opex inflation 2.0% a year: the Bank of Canada inflation-control target midpoint (no company rate stated). Band 1%-3%.
- **S13** Variable cash opex 30% of revenue above Q3 2026 annualized revenue (127.65). The incremental rate cannot be measured from FY2025-26 because integration synergies cut opex while revenue grew; management says $1 of ARR is "a point of adjusted EBITDA" if no costs are added (G14) and R&D holds level with AI spend (G11). Band 20% (bull) to 40% (bear).
- **S14** Buddy cost saving 0.5 a year from FY2027 (Buddy was about breakeven, G16; margin through "a little bit of cost reduction and revenue generation" in 6-12 months, G10). Band 0 (bear) to 1.0 (bull).
- **S15** Foreign exchange gains and losses, which sit inside Adjusted EBITDA (G23), are forecast at zero; FX on ARR is held at zero.
- **S16** Contribution margin mc = 1 - 20% cash cost of sales - 30% variable opex = 0.50 (bull 0.60, bear 0.40).
- **S17** Buddy component inside the term line is held at the acquired ARR of 4.48 x 0.985 a year (stub 174/365 in FY2026); Vitalhub counts post-close growth as organic (G24), so Buddy growth sits in the organic ARR rate. Not scaled to Consensus.
- **S18** Scenario levers: (1) SHREWD roll-off size and organic ARR adds in dollars, (2) the cost build (variable opex rate, Buddy saving), (3) Attend Anywhere. Bull and bear differ from base by the bottom-up difference of those levers, added to the base lines and EBITDA.
- **S19** Dan Matlow CEO bot view: treat the 10-11% organic comfort as withdrawn until the NHS FDP decision; low-to-high single-digit organic ARR growth in Q4 2026 and early 2027. simulated CEO view (Dan Matlow CEO bot), 17 Nov 2026; not company disclosure; link unverified. Used only as a cross-check of S2-S3, which rest on the filings and the Q3 call. (D22)
- **S20** Earn-out probabilities = accrued fair value / maximum: Novari 3.8 / 4.5 = 0.844; Buddy 3.205624 / 7.248555 = 0.442 (D2).
- **S21** Earn-out dates are the end of each earn-out window: Novari 24 months after 4 Jul 2025 close (2027-07-04); Buddy 30 months after 10 Jul 2026 close (2029-01-10). The filings give windows, not payment dates.
- **S22** Bear: all SHREWD ARR (8.0, the midpoint of 7.5-8.6, G2) rolls off straight-line during 2027 as trusts migrate onto FDP (G26); organic adds stay flat at the FY2025 printed 7.23 a year (A75), so organic growth falls to about 6.5% of opening ARR. Bull: only 1.5 rolls off (suspended accounts still in ARR, G3) and organic adds grow 15% a year (the 2024-to-TTM-Q1 2026 pace, S29) as the Strata pipeline and AI add-ons convert. A place in the new FDP procurement is not in bull revenue (S28).
- **S23** Business acquisition, restructuring and integration costs (Q3 2026 1.368) are outside Adjusted EBITDA by the company definition (G23); Induction and Novari integration is "pretty well" done with "a little bit of work to do" and Buddy integration is underway (D12). They are not forecast inside Adjusted EBITDA.
- **S26** Base SHREWD roll-off: 4.0 of ARR, about half of the 7.5-8.6 SHREWD ARR (G2, C31), straight-line during calendar 2027, none in 2028-29. Why half: the FDP extension to March 2029 (G26) means the platform displacing SHREWD stays and trusts keep migrating onto it, and some suspended accounts are still in ARR (G3), so a 2027 loss is more likely than not; but SHREWD sits "in all different pockets" and management cannot say which are at risk (G1), a new FDP iteration is procured from H2 2027 that invites UK SMEs and new capability providers (G27, G28), and trusts mid-procurement have reason to keep tools that work. The evidence does not identify losses beyond 2027. Band 1.5 (bull) to 8.0 (bear, all of it).
- **S27** Lost SHREWD revenue (average ARR lost x 0.985 term ratio x 1.165 for the services that ride on term revenue) saves only the 20% cash cost of sales; opex is not cut (G14: "every $1 million of ARR theoretically if we don't add more costs, that's a point of adjusted EBITDA"). Variable opex is charged on revenue before the SHREWD loss.
- **S28** FDP re-procurement upside is excluded from every case: the formal process starts in H2 2027 and takes about 18 months (G27), so an award lands around early 2029 at the earliest and its revenue mostly after FY2029; Vitalhub has not announced a consortium or bid.
- **S29** Organic adds are forecast in dollars. Printed organic net of churn was 6.39 in 2023, 6.48 in 2024 and 7.23 in 2025 (A75) while acquisitions took opening ARR from 36.2 to 71.1 (A76); organic growth fell from 17.7% to 14.5% to 10.2% (and 7.7% TTM Q3 2026) because the acquired ARR (17.9 in 2024, 15.9 in 2025, 4.48 in 2026) added little net organic growth after close in aggregate, not because dollar adds shrank (C38). Dollar adds grew about 10% a year from 2023 (6.39) to the four quarters to Q2 2026 (8.12), about 2.5 years apart. Base keeps that 10% trend; management commentary is mixed (pipelines and Rule of 40 vs the withdrawn 10%-11%), so no acceleration or deceleration is applied.
- **S24** Q4 2026 virtual care held at the Q3 2026 level (2.338); renewals fall in March (G9).
- **S17_1** Buddy component inside the term line is held at the acquired ARR of 4.48 x 0.985 a year (stub 174/365 in FY2026); Vitalhub counts post-close growth as organic (G24), so Buddy growth sits in the organic ARR rate. Not scaled to Consensus.
- **S17_2** Buddy component inside the term line is held at the acquired ARR of 4.48 x 0.985 a year (stub 174/365 in FY2026); Vitalhub counts post-close growth as organic (G24), so Buddy growth sits in the organic ARR rate. Not scaled to Consensus.
- **S25** Payments of contingent consideration C$781,053 in the nine months to 30 Sep 2026; exact date not given, dated at the quarter end. (D2)
- **S21_1** Earn-out dates are the end of each earn-out window: Novari 24 months after 4 Jul 2025 close (2027-07-04); Buddy 30 months after 10 Jul 2026 close (2029-01-10). The filings give windows, not payment dates.
- **S20_1** Earn-out probabilities = accrued fair value / maximum: Novari 3.8 / 4.5 = 0.844; Buddy 3.205624 / 7.248555 = 0.442 (D2).
- **S16_1** Contribution margin mc = 1 - 20% cash cost of sales - 30% variable opex = 0.50 (bull 0.60, bear 0.40).
- **S6_1** bull gsnext: FY2030 one more year of the bull build (organic ARR adds 14.21).
- **S16_2** Contribution margin mc = 1 - 20% cash cost of sales - 30% variable opex = 0.50 (bull 0.60, bear 0.40).
- **S6_2** bear gsnext: FY2030 one more year of the bear build (organic ARR adds 7.23).
- **S30** Finagle defaults filled on the v05 case that ran (result defaults_filled, unchanged from v04): baseline.noa, baseline.nol, debt.start_year, distribution.mode, forecast.dwc.mode, rates.gt, rates.re, rates.roict, year. Values: noa 0, nol 0, debt policy start year 1, distribution none, working-capital change zero, terminal growth 3.81% (= the 10-year yield), cost of equity 9.31% (0.055 + the 10-year yield), terminal ROIC 15%, ten-year horizon. Each scenario also lists the build_baseline defaults rates.t, rates.rd, debt.mode and debt.leverage, which the prompt inputs P11 and P14 replaced. Capex and SBC paths were not set: forecast_capex method 1 and forecast_sbc ran from year-0 capex 0.423144 and SBC 2.647812 (Yahoo). (D25)

### Calculations

- **C1** Term licences, maintenance and support Q4 2026E = bottom-up Q4 (26.581) scaled by the Q4 organic factor 0.9825 to the Consensus remainder; Buddy component not scaled. (inputs: E1, S1, S2, S8, S9, S17, S24)
- **C2** Term licences, maintenance and support FY26E = bottom-up 100.834 x organic scale factor 0.9825 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_1** Term licences, maintenance and support FY27E = bottom-up 109.495 x organic scale factor 0.9870 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_2** Term licences, maintenance and support FY28E = bottom-up 116.766 x organic scale factor 0.9714 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_3** Term licences, maintenance and support FY29E = bottom-up 126.931 x organic scale factor 1.0229 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C3** Term licences, maintenance and support FY2025A / FY2024A - 1. (inputs: A3, A3)
- **C3_1** Term licences, maintenance and support FY26E growth. (inputs: C2)
- **C3_2** Term licences, maintenance and support FY27E growth. (inputs: C2)
- **C3_3** Term licences, maintenance and support FY28E growth. (inputs: C2)
- **C3_4** Term licences, maintenance and support FY29E growth. (inputs: C2)
- **C4** Days from 10 Jul 2026 close to 31 Dec 2026 (174) / 365. (inputs: A45)
- **C1_1** Virtual care term licences (Attend Anywhere) Q4 2026E = bottom-up Q4 (2.338) scaled by the Q4 organic factor 0.9825 to the Consensus remainder; Buddy component not scaled. (inputs: E1, S1, S2, S8, S9, S17, S24)
- **C2_4** Virtual care term licences (Attend Anywhere) FY26E = bottom-up 9.357 x organic scale factor 0.9825 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_5** Virtual care term licences (Attend Anywhere) FY27E = bottom-up 8.889 x organic scale factor 0.9870 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_6** Virtual care term licences (Attend Anywhere) FY28E = bottom-up 8.445 x organic scale factor 0.9714 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_7** Virtual care term licences (Attend Anywhere) FY29E = bottom-up 8.023 x organic scale factor 1.0229 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C3_5** Virtual care term licences (Attend Anywhere) had no FY2024 revenue; growth not meaningful, recorded as 0. (inputs: A4)
- **C3_6** Virtual care term licences (Attend Anywhere) FY26E growth. (inputs: C2)
- **C3_7** Virtual care term licences (Attend Anywhere) FY27E growth. (inputs: C2)
- **C3_8** Virtual care term licences (Attend Anywhere) FY28E growth. (inputs: C2)
- **C3_9** Virtual care term licences (Attend Anywhere) FY29E growth. (inputs: C2)
- **C1_2** Perpetual licences Q4 2026E = bottom-up Q4 (0.5) scaled by the Q4 organic factor 0.9825 to the Consensus remainder; Buddy component not scaled. (inputs: E1, S1, S2, S8, S9, S17, S24)
- **C2_8** Perpetual licences FY26E = bottom-up 2.444 x organic scale factor 0.9825 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_9** Perpetual licences FY27E = bottom-up 2.0 x organic scale factor 0.9870 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_10** Perpetual licences FY28E = bottom-up 2.0 x organic scale factor 0.9714 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_11** Perpetual licences FY29E = bottom-up 2.0 x organic scale factor 1.0229 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C3_10** Perpetual licences FY2025A / FY2024A - 1. (inputs: A5, A5)
- **C3_11** Perpetual licences FY26E growth. (inputs: C2)
- **C3_12** Perpetual licences FY27E growth. (inputs: C2)
- **C3_13** Perpetual licences FY28E growth. (inputs: C2)
- **C3_14** Perpetual licences FY29E growth. (inputs: C2)
- **C1_3** Services, hardware and other Q4 2026E = bottom-up Q4 (4.6) scaled by the Q4 organic factor 0.9825 to the Consensus remainder; Buddy component not scaled. (inputs: E1, S1, S2, S8, S9, S17, S24)
- **C2_12** Services, hardware and other FY26E = bottom-up 16.941 x organic scale factor 0.9825 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_13** Services, hardware and other FY27E = bottom-up 18.067 x organic scale factor 0.9870 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_14** Services, hardware and other FY28E = bottom-up 19.266 x organic scale factor 0.9714 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C2_15** Services, hardware and other FY29E = bottom-up 20.944 x organic scale factor 1.0229 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs: E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C3_15** Services, hardware and other FY2025A / FY2024A - 1. (inputs: A6, A6)
- **C3_16** Services, hardware and other FY26E growth. (inputs: C2)
- **C3_17** Services, hardware and other FY27E growth. (inputs: C2)
- **C3_18** Services, hardware and other FY28E growth. (inputs: C2)
- **C3_19** Services, hardware and other FY29E growth. (inputs: C2)
- **C5** Q4 2026E revenue = FY2026 Consensus 129 (E1) - 9M 2026 reported 95.557 (A1). (inputs: E1, A1)
- **C6** FY2025A / FY2024A - 1 (+58.9%, acquisitions plus organic). (inputs: A1, A1_1)
- **C5_1** Q4 2026E Adjusted EBITDA = FY2026 Consensus EBITDA 34 (E2) - 9M 2026 reported 24.773 (A2). (inputs: E2, A2)
- **C6_1** FY2025A / FY2024A - 1. (inputs: A2, A2_1)
- **C36** Event-adjusted Consensus revenue FY27E = FactSet 139 (E1) -2.295 for the 16 Nov 2026 FDP extension (P7): the effect of the 4.0 SHREWD roll-off alone on the v3 bottom-up build (with vs without the loss). The 17 Nov pull is taken to predate the announcement. v3 isolates the event: the organic-driver change (S29) uses information analysts already had and does not move the base. (inputs: E1, P7, S26, S27, D23)
- **C36_1** Event-adjusted Consensus Adjusted EBITDA FY27E = FactSet 39 (E2) -1.836 for the same SHREWD roll-off; lost revenue saves only cash cost of sales (S27). (inputs: E2, P7, S26, S27, D23)
- **C36_2** Event-adjusted Consensus revenue FY28E = FactSet 147 (E1) -4.590 for the 16 Nov 2026 FDP extension (P7): the effect of the 4.0 SHREWD roll-off alone on the v3 bottom-up build (with vs without the loss). The 17 Nov pull is taken to predate the announcement. v3 isolates the event: the organic-driver change (S29) uses information analysts already had and does not move the base. (inputs: E1, P7, S26, S27, D23)
- **C36_3** Event-adjusted Consensus Adjusted EBITDA FY28E = FactSet 45 (E2) -3.672 for the same SHREWD roll-off; lost revenue saves only cash cost of sales (S27). (inputs: E2, P7, S26, S27, D23)
- **C36_4** Event-adjusted Consensus revenue FY29E = FactSet 166 (E1) -4.590 for the 16 Nov 2026 FDP extension (P7): the effect of the 4.0 SHREWD roll-off alone on the v3 bottom-up build (with vs without the loss). The 17 Nov pull is taken to predate the announcement. v3 isolates the event: the organic-driver change (S29) uses information analysts already had and does not move the base. (inputs: E1, P7, S26, S27, D23)
- **C36_5** Event-adjusted Consensus Adjusted EBITDA FY29E = FactSet 52 (E2) -3.672 for the same SHREWD roll-off; lost revenue saves only cash cost of sales (S27). (inputs: E2, P7, S26, S27, D23)
- **C6_2** Revenue growth FY26E. (inputs: E1)
- **C6_3** Adjusted EBITDA growth FY26E. (inputs: E2)
- **C6_4** Revenue growth FY27E. (inputs: E1)
- **C6_5** Adjusted EBITDA growth FY27E. (inputs: E2)
- **C6_6** Revenue growth FY28E. (inputs: E1)
- **C6_7** Adjusted EBITDA growth FY28E. (inputs: E2)
- **C6_8** Revenue growth FY29E. (inputs: E1)
- **C6_9** Adjusted EBITDA growth FY29E. (inputs: E2)
- **C7** Adjusted EBITDA / revenue, FY24A. (inputs: A1, A2, E1, E2)
- **C7_1** Adjusted EBITDA / revenue, FY25A. (inputs: A1, A2, E1, E2)
- **C7_2** Adjusted EBITDA / revenue, 9MA. (inputs: A1, A2, E1, E2)
- **C7_3** Adjusted EBITDA / revenue, Q4E. (inputs: A1, A2, E1, E2)
- **C7_4** Adjusted EBITDA / revenue, FY26E. (inputs: A1, A2, E1, E2)
- **C7_5** Adjusted EBITDA / revenue, FY27E. (inputs: A1, A2, E1, E2)
- **C7_6** Adjusted EBITDA / revenue, FY28E. (inputs: A1, A2, E1, E2)
- **C7_7** Adjusted EBITDA / revenue, FY29E. (inputs: A1, A2, E1, E2)
- **C8** Q2 2026 FX loss = 9M 2026 gain (0.130585) - Q1 loss 0.238091 - Q3 gain (0.592126) solved for Q2 = 0.222984. (inputs: A29)
- **C9** Bottom-up revenue FY26E: sum of unscaled lines (term from the ARR path, virtual care, perpetual, services). (inputs: S1, S2, S3, S4, S5, S7, S8, S9, S17)
- **C10** Bottom-up Adjusted EBITDA FY26E: unscaled revenue - 20% cash cost of sales - core opex (Q3 2026 annualized, +2%/yr) + Buddy saving - 30% variable opex on revenue above 127.65. (inputs: S10, S11, S12, S13, S14, S15)
- **C11** Bottom-up / base (event-adjusted Consensus) revenue FY26E. (inputs: C9, E1)
- **C12** Event-adjusted Consensus is the base, ratio 1. (inputs: E1)
- **C13** Bottom-up / base (event-adjusted Consensus) Adjusted EBITDA FY26E. (inputs: C10, E2)
- **C9_1** Bottom-up revenue FY27E: sum of unscaled lines (term from the ARR path, virtual care, perpetual, services). (inputs: S1, S2, S3, S4, S5, S7, S8, S9, S17)
- **C10_1** Bottom-up Adjusted EBITDA FY27E: unscaled revenue - 20% cash cost of sales - core opex (Q3 2026 annualized, +2%/yr) + Buddy saving - 30% variable opex on revenue above 127.65. (inputs: S10, S11, S12, S13, S14, S15)
- **C11_1** Bottom-up / base (event-adjusted Consensus) revenue FY27E. (inputs: C9, E1)
- **C13_1** Bottom-up / base (event-adjusted Consensus) Adjusted EBITDA FY27E. (inputs: C10, E2)
- **C9_2** Bottom-up revenue FY28E: sum of unscaled lines (term from the ARR path, virtual care, perpetual, services). (inputs: S1, S2, S3, S4, S5, S7, S8, S9, S17)
- **C10_2** Bottom-up Adjusted EBITDA FY28E: unscaled revenue - 20% cash cost of sales - core opex (Q3 2026 annualized, +2%/yr) + Buddy saving - 30% variable opex on revenue above 127.65. (inputs: S10, S11, S12, S13, S14, S15)
- **C11_2** Bottom-up / base (event-adjusted Consensus) revenue FY28E. (inputs: C9, E1)
- **C13_2** Bottom-up / base (event-adjusted Consensus) Adjusted EBITDA FY28E. (inputs: C10, E2)
- **C9_3** Bottom-up revenue FY29E: sum of unscaled lines (term from the ARR path, virtual care, perpetual, services). (inputs: S1, S2, S3, S4, S5, S7, S8, S9, S17)
- **C10_3** Bottom-up Adjusted EBITDA FY29E: unscaled revenue - 20% cash cost of sales - core opex (Q3 2026 annualized, +2%/yr) + Buddy saving - 30% variable opex on revenue above 127.65. (inputs: S10, S11, S12, S13, S14, S15)
- **C11_3** Bottom-up / base (event-adjusted Consensus) revenue FY29E. (inputs: C9, E1)
- **C13_3** Bottom-up / base (event-adjusted Consensus) Adjusted EBITDA FY29E. (inputs: C10, E2)
- **C14** Base revenue for the bridge (Q4E). (inputs: E1, A1)
- **C14_1** Revenue x 80% cash gross margin. (inputs: S10)
- **C14_2** Q3 2026 cash opex 17.197 a quarter, annualized and grown 2%/yr. (inputs: S11, S12)
- **C14_3** Buddy cost saving (S14). (inputs: S14)
- **C14_4** 30% of revenue (before the SHREWD loss, S27) above Q3 2026 annualized revenue 127.65. (inputs: S13)
- **C14_5** Cost-build Adjusted EBITDA on base revenue. (inputs: S10, S11, S12, S13, S14)
- **C14_6** Base Adjusted EBITDA (Consensus; Q4 = FY less 9M). (inputs: E2, A2)
- **C15** Consensus-implied cash cost / cost-build cash cost on the same revenue - 1; inside the 10% rule. (inputs: E1, E2, S10, S11, S13)
- **C14_7** Base revenue for the bridge (FY27E). (inputs: E1, A1)
- **C14_8** Revenue x 80% cash gross margin. (inputs: S10)
- **C14_9** Q3 2026 cash opex 17.197 a quarter, annualized and grown 2%/yr. (inputs: S11, S12)
- **C14_10** Buddy cost saving (S14). (inputs: S14)
- **C14_11** 30% of revenue (before the SHREWD loss, S27) above Q3 2026 annualized revenue 127.65. (inputs: S13)
- **C14_12** Cost-build Adjusted EBITDA on base revenue. (inputs: S10, S11, S12, S13, S14)
- **C14_13** Base Adjusted EBITDA (Consensus; Q4 = FY less 9M). (inputs: E2, A2)
- **C15_1** Consensus-implied cash cost / cost-build cash cost on the same revenue - 1; inside the 10% rule. (inputs: E1, E2, S10, S11, S13)
- **C14_14** Base revenue for the bridge (FY28E). (inputs: E1, A1)
- **C14_15** Revenue x 80% cash gross margin. (inputs: S10)
- **C14_16** Q3 2026 cash opex 17.197 a quarter, annualized and grown 2%/yr. (inputs: S11, S12)
- **C14_17** 30% of revenue (before the SHREWD loss, S27) above Q3 2026 annualized revenue 127.65. (inputs: S13)
- **C14_18** Cost-build Adjusted EBITDA on base revenue. (inputs: S10, S11, S12, S13, S14)
- **C14_19** Base Adjusted EBITDA (Consensus; Q4 = FY less 9M). (inputs: E2, A2)
- **C15_2** Consensus-implied cash cost / cost-build cash cost on the same revenue - 1; inside the 10% rule. (inputs: E1, E2, S10, S11, S13)
- **C14_20** Base revenue for the bridge (FY29E). (inputs: E1, A1)
- **C14_21** Revenue x 80% cash gross margin. (inputs: S10)
- **C14_22** Q3 2026 cash opex 17.197 a quarter, annualized and grown 2%/yr. (inputs: S11, S12)
- **C14_23** 30% of revenue (before the SHREWD loss, S27) above Q3 2026 annualized revenue 127.65. (inputs: S13)
- **C14_24** Cost-build Adjusted EBITDA on base revenue. (inputs: S10, S11, S12, S13, S14)
- **C14_25** Base Adjusted EBITDA (Consensus; Q4 = FY less 9M). (inputs: E2, A2)
- **C15_3** Consensus-implied cash cost / cost-build cash cost on the same revenue - 1; inside the 10% rule. (inputs: E1, E2, S10, S11, S13)
- **C16** Year-0 cash = FY2025 cash 57.630 + short-term investments 61.551 + 2026 equity raises 0 = 119.181 (P3). (inputs: A40, A41, A62, P3)
- **C17** Year-0 shares = FY2025 63.232054 + 2026 equity raises 0 (P3). The 75,000 Buddy consideration shares are on cash_share_adjustments. (inputs: A42, A62, P3)
- **C18** No year-0 equity raise: opening cash 119.181 less the dated Buddy and earn-out items (about 26 undiscounted in the base) stays positive in every case, and EBITDA is positive in every year of every case (P3). (inputs: C16, P3)
- **C19** Paid at close; probability 1. (inputs: A45)
- **C20** Leaves are on totals: Buddy (closed 10 Jul 2026) sits inside the term line and the cost build; no acquisition after it is forecast. The same basis goes to Finagle for every case (P9). (inputs: A45, P9)
- **C21** No future acquisition is forecast. Management hopes to close another deal before year-end (G12) but none is announced; announced-but-unclosed deals are excluded. (inputs: G12)
- **C22** Revenue growth FY2026E-FY2029E on totals; compounds to the base revenue. (inputs: E1, A1)
- **C23** Adjusted EBITDA growth FY2026E-FY2029E on totals; compounds to the base EBITDA. (inputs: E2, A2)
- **C24** me = FY2029E Adjusted EBITDA 48.328 / revenue 161.410 = 29.9% (event-adjusted Consensus). (inputs: C36)
- **C25** bull Term licences, maintenance and support Q4 2026E = base + (bull bottom-up - base bottom-up). (inputs: C1, S18, S22)
- **C25_1** bull Term licences, maintenance and support FY26E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_2** bull Term licences, maintenance and support FY27E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_3** bull Term licences, maintenance and support FY28E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_4** bull Term licences, maintenance and support FY29E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_5** bull Virtual care term licences (Attend Anywhere) Q4 2026E = base + (bull bottom-up - base bottom-up). (inputs: C1, S18, S22)
- **C25_6** bull Virtual care term licences (Attend Anywhere) FY26E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_7** bull Virtual care term licences (Attend Anywhere) FY27E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_8** bull Virtual care term licences (Attend Anywhere) FY28E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_9** bull Virtual care term licences (Attend Anywhere) FY29E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_10** bull Perpetual licences Q4 2026E = base + (bull bottom-up - base bottom-up). (inputs: C1, S18, S22)
- **C25_11** bull Perpetual licences FY26E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_12** bull Perpetual licences FY27E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_13** bull Perpetual licences FY28E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_14** bull Perpetual licences FY29E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_15** bull Services, hardware and other Q4 2026E = base + (bull bottom-up - base bottom-up). (inputs: C1, S18, S22)
- **C25_16** bull Services, hardware and other FY26E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_17** bull Services, hardware and other FY27E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_18** bull Services, hardware and other FY28E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_19** bull Services, hardware and other FY29E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C26** bull Q4 2026E revenue. (inputs: C5, S18)
- **C26_1** bull Q4 2026E Adjusted EBITDA. (inputs: C5, S18)
- **C26_2** bull revenue FY26E = base 129.000 + bottom-up lever difference. (inputs: E1, S18, S22)
- **C26_3** bull Adjusted EBITDA FY26E = base 34.000 + bottom-up lever difference. (inputs: E2, S18, S13, S14)
- **C26_4** bull revenue FY27E = base 136.705 + bottom-up lever difference. (inputs: E1, S18, S22)
- **C26_5** bull Adjusted EBITDA FY27E = base 37.164 + bottom-up lever difference. (inputs: E2, S18, S13, S14)
- **C26_6** bull revenue FY28E = base 142.410 + bottom-up lever difference. (inputs: E1, S18, S22)
- **C26_7** bull Adjusted EBITDA FY28E = base 41.328 + bottom-up lever difference. (inputs: E2, S18, S13, S14)
- **C26_8** bull revenue FY29E = base 161.410 + bottom-up lever difference. (inputs: E1, S18, S22)
- **C26_9** bull Adjusted EBITDA FY29E = base 48.328 + bottom-up lever difference. (inputs: E2, S18, S13, S14)
- **C27** bull revenue growth on totals. (inputs: C26)
- **C27_1** bull EBITDA growth on totals. (inputs: C26)
- **C27_2** bull me = FY2029E EBITDA / revenue. (inputs: C26)
- **C25_20** bear Term licences, maintenance and support Q4 2026E = base + (bear bottom-up - base bottom-up). (inputs: C1, S18, S22)
- **C25_21** bear Term licences, maintenance and support FY26E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_22** bear Term licences, maintenance and support FY27E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_23** bear Term licences, maintenance and support FY28E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_24** bear Term licences, maintenance and support FY29E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_25** bear Virtual care term licences (Attend Anywhere) FY27E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_26** bear Virtual care term licences (Attend Anywhere) FY28E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_27** bear Virtual care term licences (Attend Anywhere) FY29E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_28** bear Services, hardware and other FY27E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_29** bear Services, hardware and other FY28E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C25_30** bear Services, hardware and other FY29E = base line + lever difference (S18). (inputs: C2, S18, S22)
- **C26_10** bear Q4 2026E revenue. (inputs: C5, S18)
- **C26_11** bear Q4 2026E Adjusted EBITDA. (inputs: C5, S18)
- **C26_12** bear revenue FY26E = base 129.000 + bottom-up lever difference. (inputs: E1, S18, S22)
- **C26_13** bear Adjusted EBITDA FY26E = base 34.000 + bottom-up lever difference. (inputs: E2, S18, S13, S14)
- **C26_14** bear revenue FY27E = base 136.705 + bottom-up lever difference. (inputs: E1, S18, S22)
- **C26_15** bear Adjusted EBITDA FY27E = base 37.164 + bottom-up lever difference. (inputs: E2, S18, S13, S14)
- **C26_16** bear revenue FY28E = base 142.410 + bottom-up lever difference. (inputs: E1, S18, S22)
- **C26_17** bear Adjusted EBITDA FY28E = base 41.328 + bottom-up lever difference. (inputs: E2, S18, S13, S14)
- **C26_18** bear revenue FY29E = base 161.410 + bottom-up lever difference. (inputs: E1, S18, S22)
- **C26_19** bear Adjusted EBITDA FY29E = base 48.328 + bottom-up lever difference. (inputs: E2, S18, S13, S14)
- **C27_3** bear revenue growth on totals. (inputs: C26)
- **C27_4** bear EBITDA growth on totals. (inputs: C26)
- **C27_5** bear me = FY2029E EBITDA / revenue. (inputs: C26)
- **C29** Q3 2026 Adjusted EBITDA excluding the FX gain: (8.620 - 0.592) / 31.914 = 25.2%; Q2 2026 excluding the FX loss: (8.163 + 0.223) / 31.738 = 26.4%. (inputs: A21_8, C8, A59)
- **C30** Organic ARR growth by year = sum of quarterly organic adds / opening ARR: FY2025 10.2%; trailing twelve months to Q3 2026 8% (company-stated 8%). (inputs: A26, A27)
- **C31** SHREWD ARR = 7-8% (G2) x closing ARR 107.194 = 7.5 to 8.6. (inputs: G2, A26)
- **C32** Cash opex per quarter (G&A + S&M + R&D): Q4 2025 17.157; Q1 2026 17.817; Q2 2026 16.781 (9M less Q1 and Q3); Q3 2026 17.197. (inputs: A59, A67, A68)
- **C33** Unscaled bottom-up scenario totals (Appendix A sensitivity) from model.py v3: bull revenue 129.70/141.73/152.40/165.65, EBITDA 34.44/41.24/46.06/52.58; bear revenue 129.45/133.09/135.61/142.89, EBITDA 33.90/32.30/30.07/31.55. (inputs: S18, S22, S26, S29)
- **C38** ARR bridge trend from the printed series (A75-A78, A27 series): organic adds 6.39 (2023), 6.48 (2024), 7.23 (2025), 8.12 (four quarters to Q2 2026), 7.23 (TTM Q3 2026); organic growth on opening ARR 17.7%, 14.5%, 10.2%, 10.2%, 7.7%. Opening ARR (rebuilt back from 107.194 through the bridge): 36.15 (2023), 44.57 (2024), 71.05 (2025), 96.15 (2026). Organic adds per dollar of opening ARR including acquired ARR fell by more than half while dollar adds rose about 13% from 2023 to 2025. Seasonality, 2022-2025 average adds: Q1 1.57, Q2 1.35, Q3 1.28, Q4 1.84. FX added 2.09 (2024), 1.99 (2025) and 1.22 (9M 2026), positive in 9 of the last 10 quarters. (inputs: A75, A76, A77, A78, A27_8)
- **C39** TLMS revenue x 4 / average ARR by quarter: 1.01-1.06 in 2023, 1.05-1.08 in Q1-Q3 2024, 1.14 in Q4 2024 (14.6 acquired in the quarter, so the average understates the ARR earning revenue), 1.01-1.09 in 2025 (acquisition quarters Q2 and Q3 high), then 0.994 / 0.980 / 0.979 / 0.988 in Q4 2025-Q3 2026 (average 0.985). ARR excludes virtual care (A79), so the step down is not Attend Anywhere leaving the TLMS line; the cause is not disclosed. The 0.985 conversion matches the four clean quarters since Q4 2025. (inputs: A22_8, A26_8, A79, S1)
- **C40** Change from v2 (17 Nov 2026) to v3 (18 Nov 2026): organic adds in dollars (S29) and the event adjustment limited to the SHREWD effect (C36). See revision_log.md for figures. (inputs: S29, C36)
- **C37** Change from v1 (17 Nov 2026, before the FDP extension) to v2: base revenue FY27-29 -1.67/-3.51/-3.86 and Adjusted EBITDA -1.52/-3.13/-3.31; bull revenue -0.86/-1.82/-2.02, EBITDA -0.69/-1.43/-1.55; bear revenue -1.50/-3.09/-3.29, EBITDA -2.44/-4.91/-4.99. FY2026 unchanged. (inputs: C36, S26, S22)
- **C34** Consensus revenue growth path: FY2027 +7.8%, FY2028 +5.8%, FY2029 +12.9%; the FY2028 dip and FY2029 jump reflect thinner, rounded later-year coverage (E-series). (inputs: E1)
- **C35** Revenue shares FY2025 by line: term 78.4%, virtual care 4.8%, perpetual 1.9%, services 14.9%. (inputs: A3_1, A4_1, A5_1, A6_1, A1_1)
- **C41** Finagle v05 result (D25): value per share (free cash flow to equity; DDM identical) base 9.226, bull 11.216, bear 6.827 vs price 6.73 (Yahoo, 2026-11-18); cost of equity 9.31% and terminal growth 3.81%, both derived by Finagle from the 3.81% risk-free rate (P10); tax 26.5%, cost of debt 2.8%, debt 0 held; year-0 EBITDA 26.554 before SBC (P15); opening cash 106.813 and shares 63.307054; cash after schedule 99.789 (present value -7.023); ten-year horizon FY2026E-FY2035E; no sanity flags; validation warning base "average EBITDA growth is 16.4% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero." (bull 21.4%, bear none); result flags: "rates.rd provenance: Forecaster proposal without an explicit David quote (applied as given; see rd_provenance)" and "year-0 capex remains Yahoo 0.423144 vs method-1 ratio on new D&A (1.271558 / revenue)". (inputs: D25, P10, P11, P12, P13, P14, P15, S30)
- **C42** Value bridge (derived): FCFE each year = Finagle EBITDA - capex - SBC - cash tax - interest, which equals the yearly change in the result cash path; discounted at the 9.31% cost of equity. Base 99.79 cash + 71.18 PV FY2026E-FY2029E + 104.34 PV FY2030E-FY2035E + 308.76 terminal (residual) = 584.08 = 9.226 x 63.307; bull 99.79 + 78.52 + 131.50 + 400.23 = 710.04; bear 99.79 + 61.29 + 71.20 + 199.89 = 432.18. Terminal share of value 52.9% base, 56.4% bull, 46.3% bear. Value vs 6.73: base +37%, bull +67%, bear +1.4%. (inputs: C41)
- **C43** Finagle capex path (v05 result paths, method 1 on year-0 D&A 1.271558): base capex 0.42 (FY2025A), 3.00, 3.99, 4.73, 7.17 (FY2029E), 16.28 (FY2035E) against D&A 2.71 in FY2035E (about 6.0x, derived; bull 6.9x, bear 4.9x); FY2035E capex / EBITDA 19.4% base, 19.0% bull, 20.1% bear vs FY2025 actual 0.423 / 26.554 = 1.6% (derived). Mechanism: terminal capex = D&A x (1 - C) + C x (EBITDA - SBC) with C = 3.81% / 15% x (1 - 26.5%) = 0.187, so about 14.1 of the 16.3 base terminal capex is growth reinvestment at the 15% terminal ROIC (derived). (inputs: D25, A81, A82, S30)
- **C44** Finagle v05 EBITDA path: year-0 EBITDA is the stated 26.554 (P15), so the forecast growth compounds to the forecast dollars: base 34.000 / 37.164 / 41.328 / 48.328 for FY2026E-FY2029E, equal to the forecast (C23), and the starting margin passed past FY2029E is 29.9%. Year-0 SBC is still Yahoo's 2.648, so the SBC/EBITDA ratio Finagle holds moves from 0.1022 (v04) to 0.0997; SBC dollars in FY2026E-FY2029E are unchanged and slightly lower from FY2030E. (inputs: D25, P15, A2_1, C23)
- **C28** base closing ARR FY26E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_1** base closing ARR FY27E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_2** base closing ARR FY28E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_3** base closing ARR FY29E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_4** bull closing ARR FY26E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_5** bull closing ARR FY27E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_6** bull closing ARR FY28E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_7** bull closing ARR FY29E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_8** bear closing ARR FY26E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_9** bear closing ARR FY27E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_10** bear closing ARR FY28E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)
- **C28_11** bear closing ARR FY29E from organic adds (S2-S5, S22); FX zero. (inputs: A26, S2, S3, S4, S5, S22)

### Prompt

- **P1** David May, 17 Nov 2026 (t213u): "Create a forecast for VHI.TO ... Have 4 explicit years." Window FY2026E-FY2029E including the current year, per the brief.
- **P2** David May standing preferences (brief, 17 Nov 2026): base case accelerates or decelerates current trends on management commentary, no conservative haircut; a later-year margin well beyond history is flagged and banded in the bear, not capped.
- **P3** David May standing preference: year-0 cash = FY2025 cash plus short-term investments adjusted for 2026 equity raises; shares raised likewise; add a year-0 raise rounded up to the next C$50 only if a case goes cash-negative.
- **P4** Brief, 17 Nov 2026: Vitalhub reports in CAD; keep CAD throughout. Dollar figures carry no repeated word "million".
- **P5** Brief, 17 Nov 2026: do NOT run Finagle or any valuation.
- **P7** David May, 17 Nov 2026 (revision, pt220u): "I think Palantirs contract was renewed. Probably have to assume that some of the shrewd contracts roll off in 2027." Base assumes a partial SHREWD roll-off in 2027; the base stays Consensus-anchored but is adjusted for this post-pull event (C36).
- **P9** David May, 18 Nov 2026 (pt223u): "do a finagle valuation." The Finagle bot runs the valuation; the Forecaster wrote the collaborative request (v01) and writes the report section from the result only. v01-v03 stopped; v04 was superseded by v05 (D25), which is the valuation.
- **P15** David May, 2026-11-18 (t237u): "Yes, do the quick fix". Applied in v05 as year-0 EBITDA 26.554099 (Vitalhub reported FY2025 Adjusted EBITDA, A2_1) and EBITDA definition before stock-based compensation, replacing Yahoo's 25.898.
- **P10** David May, 2026-11-18, risk-free rate for the Finagle run: "3.81% use this" (Bank of Canada 10-year benchmark, 3.81% on 16 Nov 2026, D27, because Yahoo CA10Y=RR has no quote).
- **P11** David May, 2026-11-18: "Rerun VHI as v03 with capex at the FY25 ratio of revenue, no debt (leases excluded), 26.5% tax, and no cash from the Buddy consideration shares." Applied in v04 as year-0 debt 0, debt policy hold, tax rate 26.5%.
- **P12** David May, 2026-11-18: "cash should be from the 2025 filling adjusted for the cash price of Buddy (+$12.37). shares should be from the 2025 filling (63.23M) adjusted for Buddy (+0.075M). Isn't that logical?" Applied as opening cash 106.812709 = 119.180625 - 12.367916 (the Buddy closing cash is an outflow) and shares 63,307,054 = 63,232,054 + 75,000; the Buddy closing cash and consideration shares were removed from the schedule so they are not counted twice.
- **P13** David May, 2026-11-18: "remove the "amortization of intangible assets" when calculating capex using method 1." Applied as year-0 D&A 1.271558 = depreciation of property and equipment 0.713788 + right-of-use assets 0.557770 (A81); capex stays on Finagle method 1.
- **P14** Cost of debt 2.8% for the Finagle run: proposed by the Forecaster on 2026-11-18 (Finagle's own earlier default was 0.027976); David did not object. Not a direct David quote. Immaterial: debt is held at zero and forecast-year interest is zero.
- **P8** David May, 18 Nov 2026 (pt221u): "ask the Dan Matlow bot for his product sheet on licenses. Update the forecast if it provides any insight into trends". v3 forecasts organic ARR adds in dollars from the sheet's ARR bridge (S29).
- **P6** Brief and David May (t214u, 17 Nov 2026): Dan Matlow CEO bot may be used; his own views are tagged [S] "simulated CEO view (Dan Matlow CEO bot), 17 Nov 2026" and never shown as company disclosure.

## Not verified

- D12/D13 (Seeking Alpha transcripts) read from the ceochat mirror; links not opened.
- D23 (The Register) is press reporting of a ministerial statement to MPs; Hansard was not checked.
- D22 / S19 (Dan Matlow CEO bot) is a simulated view, not company disclosure. D24 (CEO bot product sheet) was used only as an index; each figure was checked in the filing it names.
- The FY2023 MD&A could not be downloaded (OTC Markets "Temporarily Unavailable"); 2023 quarters come from the FY2024 MD&A comparatives [A75].
- Consensus (D17) shows whole numbers and no analyst count; whether any analyst revised after 16 Nov is unknown.
