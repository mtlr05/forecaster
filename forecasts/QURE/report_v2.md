# uniQure N.V. (Nasdaq: QURE)

## Company Update: FY2026E–FY2030E Revenue and EBITDA Forecast

*29 October 2026, report v2. US$ millions unless stated. This report includes a Finagle valuation but carries no rating or price target; Finagle itself states that the values in this run are still not a meaningful valuation (Section 8). Forecast file: `forecasts/QURE/forecast.json` (v1, unchanged; sha256 c706bf29…); numbered sources in Appendix B.*

## Changes from v1

**What David added (2026-10-29).** Two statements, carried as prompt inputs [D13]: [P1] "rerun and keep debt constant until the year when EBITDA is positive. Then target 1x EBITDA from that year onward." (base and bull: target 1.0x from FY2028E; bear: debt held constant) and [P2] "take rd as 10%" (cost of debt 10%, all cases). The forecast is unchanged [D13].

**What changed in the values.** Figure 0 compares the two result files side by side.

**Figure 0 – Value per share, v1 vs. v2**

| Scenario | v1 (US$) | v2 (US$) | Change (derived) |
|---|---|---|---|
| Base | -8,672.30 | -52.15 | +8,620.15 |
| Bull | -8,777.92 | -52.18 | +8,725.74 |
| Bear | -6,352.33 | -24.69 | +6,327.64 |

*Source: Finagle result files v1 [D10] and v2 [D12]; change (derived) [C56]. FCFE and DDM are equal in both runs.*

**Fixed from v1:** the default debt target of −0.325x (year-0 debt over negative year-0 EBITDA) and the default 124.7% cost of debt are both replaced by David's inputs [P1][P2][D10][D12]. Debt no longer grows to tens of billions; base peaks at $2,874M in FY2035E vs. $66,030M in v1 [D10][D12].

**Still wrong or new in v2 [D12]:**

- Default capex (method 1, 15% terminal ROIC) exceeds EBITDA every year, so FCF is negative throughout. This was already present in v1 but hidden by the debt problem.
- Cash is negative in all three cases (minimum −$394M base, −$824M bull, −$1,265M bear).
- The $478.7M royalty financing liability is still excluded from debt.
- The 1x target cannot hold in base: negative FCF is debt-funded, reaching 2.4x by FY2035E [C55].
- Bear's `hold` is Finagle's mapping of David's words, since bear EBITDA is never positive.

**The values are still not a meaningful valuation.** Only David can change that, by answering the open questions in Section 8: capex or ROIC policy, whether the royalty liability counts as debt and the starting debt, stock comp, tax and NOL, and how negative cash is funded.


## 1. Summary

**FORECAST UPDATE**

■ **We forecast FY2026E revenue of $24.9M, all Hemgenix royalties, and an EBITDA loss of $161M in every scenario [C3][C16].** No AMT-130 sales are possible before an approval, which cannot come before 2027 [S6]. The revenue figure is FY2026 consensus converted from euros, and it sits about 55% above FY2025A revenue of $16.1M [C3][A7][C49]. EBITDA (loss from operations plus D&A and stock comp, since uniQure reports no adjusted EBITDA) is H1 2026 actual plus twice the Q2 run-rate for H2 [C14][C16][C47].

■ **The scenario split is one binary event: BEAR assumes AMT-130 is not approved; BASE and BULL assume approval in mid-2027 [S6][S31].** In base, AMT-130 sales reach $900M in FY2030E from 450 patients at a $2.0M net price, and total revenue reaches $944M [S10][C11]. Bull reaches $1,734M on 650 patients at $2.6M [S24][C29]. Bear stays a royalty company at $44.0M of revenue in FY2030E [C41].

■ **EBITDA turns positive in FY2028E in base ($37.9M) and bull ($320M), and stays negative through FY2030E in bear (−$98.7M) [S13][S26][S35].** The FY2030E EBITDA margin is 55.8% in base and 67.9% in bull, driven by an assumed 85% product gross margin against cash opex of $280–300M [C25][C37][S11][S15][S28]. In bear, opex is cut to $140M after a restructuring, but royalties do not cover it [S35].

■ **Finagle's v2 valuation is still not meaningful, and Finagle says so: values per share are -52.15 (base), -52.18 (bull) and -24.69 (bear) vs. a $24.97 price [D12].** David's debt policy and 10% cost of debt replaced the defaults that broke v1 [P1][P2]. Finagle's default capex, set by its 15% terminal ROIC, now exceeds EBITDA in every year, so free cash flow is negative throughout and cash goes negative in all three cases [D12]. These numbers should not be read as a value for QURE.

**Figure 1 – Financial summary, base case**

| US$M | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E |
|---|---|---|---|---|---|---|---|
| Revenue | 27.1 [A6] | 16.1 [A7] | 24.9 [C3] | 114 [C8] | 335 [C9] | 640 [C10] | 944 [C11] |
| Revenue growth (derived) [C49] | – | -40.6% | 54.8% | 356.1% | 194.8% | 91.0% | 47.5% |
| Gross margin | – | 89.5% [C17] | 93.9% [C18] | 87.4% [C19] | 85.9% [C20] | 85.6% [C21] | 85.4% [C22] |
| EBITDA | -149 [C12] | -153 [C13] | -161 [C16] | -131 [S12] | 37.9 [S13] | 283 [S14] | 526 [S15] |
| EBITDA growth (derived) [C49] | – | n.m. | n.m. | n.m. | n.m. | 645.9% | 86.3% |
| EBITDA margin (derived) [C50] | -550.9% | -949.9% | -645.9% | -114.9% | 11.3% | 44.2% | 55.8% |

*Source: forecast.json totals [A6][A7][C2][C3][C8]–[C22]; growth and margins (derived) [C49][C50]. Growth on a negative base is shown as n.m.*

## 2. Business Description and Reporting Lines

uniQure is a gene-therapy company. Its revenue today comes almost entirely from royalties on Hemgenix, the haemophilia B gene therapy it licensed to CSL Behring [A2][A8]. Its lead asset, AMT-130 for Huntington's disease, is an investigational gene therapy with a Biologics License Application submitted to the FDA [A14][G2]. uniQure reports three revenue types:

- **License revenue (Hemgenix royalties).** CSL Behring sells Hemgenix and pays uniQure royalties; this was $15.9M in FY2025A, 99% of revenue [A2][A7][C1].
- **Collaboration revenue.** Services to CSL, $0.2M in FY2025A after winding down from $10.9M [A3][A4]; we forecast none [S5].
- **Contract manufacturing revenue.** Ended with the July 2024 divestment of commercial manufacturing; nil in FY2025A [A13][G1].
- **AMT-130 product revenue (forecast line).** Not yet approved; if approved, uniQure would sell it directly in the US. We do not model the UK separately [S6][S7].

Figure 2 shows that revenue is now one royalty stream.

**Figure 2 – Revenue by line, FY2025A**

| Line | US$M | Share |
|---|---|---|
| License (Hemgenix royalties) | 15.9 [A2] | 99.0% [C52] |
| Collaboration | 0.2 [A4] | 1.0% [C52] |
| Contract manufacturing | 0.0 [A13] | 0.0% |
| AMT-130 | 0.0 [A14] | 0.0% |
| Total | 16.1 [A7] | 100% |

*Source: uniQure 10-K FY2025 [D1][A2][A4][A7][A13]; shares (derived) [C52].*

## 3. Management

uniQure's CEO is Matt Kapusta, who we understand has led the company since 2017 after serving as its CFO [S38]. The forecast file does not source his background, ownership or tenure, so this paragraph is not verified. The record we can see in the filings is a strategic one: the 2024 divestment of commercial manufacturing (the "Lexington Transaction") turned uniQure into a royalty-plus-pipeline company, and the AMT-130 BLA was filed in September 2026 [G1][S5][G2]. We do not have sourced evidence on capital-allocation history or insider ownership, so the record is thin here.

## 4. Key Developments

The dated events in Figure 3 set up a binary 2027 for the company.

**Figure 3 – Key developments**

| Date | Event | Source |
|---|---|---|
| Jul 2024 | Commercial manufacturing divested; collaboration services to CSL wound down | [G1][S5] |
| 2026-03-02 | FY2025 10-K filed: revenue $16.1M, EBITDA −$153M | [D1][A7][C13] |
| 2026-07-29 | Q2 2026 results: H1 license revenue $9.4M, H1 EBITDA −$80.0M | [D2][D3][A8][C14] |
| 2026-09-02 | AMT-130 BLA submitted to the FDA | [D4][G2] |
| 2026-09 | UK filing for AMT-130 reported | [D9] |
| 2026-09-29 | Four-year AMT-130 data: 48-month cUHDRS effect 44%, not statistically significant (p=0.144) | [D5][S39] |
| 2026-11-04 | Q3 2026 results due (not yet out) | [S40] |
| Early Nov 2026 | FDA filing-acceptance and priority-review decision expected | [S40] |

*Source: uniQure filings and press releases [D1]–[D5]; BioSpace [D9]; dates for upcoming events not verified [S40].*

What matters most is the FDA's filing decision and whether it grants priority review: only with priority review is a PDUFA date in late April or early May 2027 possible, which underpins our mid-2027 launch in base and bull [S6]. The non-significant four-year result is the main reason we keep base patient numbers below third-party capacity estimates [S7][S39].

## 5. Business Drivers by Line

**Hemgenix royalties (volume × royalty rate).** Royalties grew 57% in FY2025A as Hemgenix uptake continued [C1]. We assume growth slows from 20% to 10% a year as uptake matures, reaching $44.0M in FY2030E in all scenarios [S1]–[S4][S20]. We include no CSL milestones because we have no sourced probability for them [S1].

**AMT-130 (patients × net price).** Base assumes 40, 150, 300 and 450 patients in FY2027E–FY2030E at $2.0M net, between Leerink's $1.7M US net estimate and Clinaptis's $2.6M [S7]–[S10][D7][D8]. Bull assumes 60, 250, 450 and 650 patients at $2.6M [S21]–[S24]. Both sit below Clinaptis's capacity ramp of 120–250 patients in year 1 and 300–500 in year 2 [D8]. Base FY2027E is scaled up by about 3% to match FY2027 consensus [C8][C48].

**Costs.** We assume an 85% AMT-130 gross margin after COGS and licensor royalties (uniQure discloses none) and a 93.9% license gross margin from H1 2026 [S11][C6]. Cash opex is $230–280M in base and $240–300M in bull for launch and the confirmatory study, and falls to $140–170M in bear after a restructuring [S12]–[S15][S25]–[S28][S32]–[S35].

## 6. Risks

**Approval risk (company-specific).** AMT-130 approval is the whole difference between bear and base: base FY2030E revenue is $944M vs. $44.0M in bear [C11][C41]. A complete response letter would leave royalties as the only revenue.

**Timing and label risk.** Without priority review, launch slips beyond mid-2027 and FY2027E product revenue ($82.7M base) moves out [S6][S7]. The FDA may also want the confirmatory study well under way at approval [S39].

**Pricing and uptake risk.** Net price spans $1.7–2.6M across sources, and each $0.1M of net price on 450 patients is $45M of FY2030E revenue (derived) [C53][D7][D8]. Neurosurgical delivery capacity may limit uptake.

**Funding risk.** EBITDA is negative through FY2027E in base and through FY2030E in bear, and year-0 cash was $80.2M, with no short-term investments found by Finagle's fetch [C16][D10]. Funding needs are not modelled in the forecast.

**Royalty and financing risk.** Hemgenix royalties support a royalty financing liability that behaves like debt: Finagle reports $478.7M at FY2025 (our v1 note said about $495M) [D12][S41]. Its terms are not modelled.

## 7. Forecast

### How the evidence becomes the numbers

There is no company revenue or EBITDA guidance, so totals come from consensus where it exists and from the line build elsewhere [C3][C8]. FY2026E uses consensus in all three scenarios; FY2027E uses consensus only in base, because consensus blends approval and no-approval outcomes and fits neither bull nor bear [C8][C26][C38]. EBITDA has no consensus and is built from gross profit less cash opex [S12]. Figure 4 maps each piece of evidence to its effect.

**Figure 4 – Evidence → assumption → forecast impact**

| Evidence | Assumption | Impact |
|---|---|---|
| FY2026 consensus €21.1M [E2] | All FY2026E revenue is royalty, converted at 1.18 $/€ [C3][C46] | FY2026E revenue $24.9M in all scenarios [C3] |
| FY2027 consensus €96.2M [E3] | Base lines scaled about 3% up to match [C48] | Base FY2027E revenue $114M [C8] |
| BLA filed 2026-09-02 [G2] | Approval mid-2027 in base and bull, none in bear [S6][S31] | AMT-130 starts in FY2027E (base $82.7M, bull $156M) [S7][S21] |
| 48-month cUHDRS non-significant [S39] | Base patients below capacity estimates [S7] | Base FY2030E AMT-130 $900M vs. bull $1,690M [S10][S24] |
| Leerink $1.7M, Clinaptis $2.6M net price [D7][D8] | $2.0M base, $2.6M bull [S7][S21] | Sets revenue per patient |
| Q2 2026 cash opex $47.8M [C47] | H2 2026 = 2× Q2; launch build-up after [C16][S12] | FY2026E EBITDA −$161M [C16] |
| No pending deals [S19] | Organic = total [S18] | No acquisitions handed to Finagle |

*Source: as tagged.*

The line build and the totals agree in every year except base FY2027E, where the line build is scaled to consensus [C48].

### Base case

Figure 5 shows the base case by line: revenue grows from royalties alone to $944M by FY2030E, with EBITDA positive from FY2028E.

**Figure 5 – Base case by line**

| US$M | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E |
|---|---|---|---|---|---|---|---|
| License revenue (Hemgenix royalties from CSL Behring) | 10.1 [A1] | 15.9 [A2] | 24.9 [C3] | 31.0 [S1] | 35.0 [S2] | 40.0 [S3] | 44.0 [S4] |
| Collaboration revenue (CSL services) | 10.9 [A3] | 0.2 [A4] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] |
| Contract manufacturing revenue | 6.1 [A5] | 0.0 [A13] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] |
| AMT-130 product revenue (US launch; UK not modelled separately) | 0.0 [A14] | 0.0 [A14] | 0.0 [S6] | 82.7 [S7] | 300 [S8] | 600 [S9] | 900 [S10] |
| **Total revenue** | 27.1 [A6] | 16.1 [A7] | 24.9 [C3] | 114 [C8] | 335 [C9] | 640 [C10] | 944 [C11] |
| Revenue growth (derived) [C49] | – | -40.6% | 54.8% | 356.1% | 194.8% | 91.0% | 47.5% |
| Gross margin | – | 89.5% [C17] | 93.9% [C18] | 87.4% [C19] | 85.9% [C20] | 85.6% [C21] | 85.4% [C22] |
| EBITDA | -149 [C12] | -153 [C13] | -161 [C16] | -131 [S12] | 37.9 [S13] | 283 [S14] | 526 [S15] |
| EBITDA margin (derived) [C50] | -550.9% | -949.9% | -645.9% | -114.9% | 11.3% | 44.2% | 55.8% |

*Source: forecast.json base lines and totals [A1]–[A14][C3][C8]–[C22][S1]–[S15]; derived rows [C49][C50]. May not sum due to rounding.*

## 8. Valuation

**Read this first: Finagle reports that the v2 values are still not a meaningful valuation.** The run produced values per share of **-52.15 (base), -52.18 (bull) and -24.69 (bear)**, with FCFE and DDM equal, vs. a price of $24.97 on 2026-10-29 [D12]. There is no post-run adjustment (`post_finagle` is null) [D13].

**Prompt inputs (David, 2026-10-29), applied as stated [D12][D13]:**

- [P1] "rerun and keep debt constant until the year when EBITDA is positive. Then target 1x EBITDA from that year onward." Base and bull: debt target mode, leverage 1.0x, start year 3 (FY2028E, the first positive-EBITDA year), with debt flat at the year-0 balance before that. Bear: EBITDA is never positive, so debt is held constant (Finagle mode `hold`); Finagle removed its default leverage and start-year leaves for bear.
- [P2] "take rd as 10%". Cost of debt 10% in all three cases.

**Why the values are still not meaningful, in Finagle's words [D12]:** "default capex (method 1, roict 0.15) exceeds EBITDA every year, so FCF negative throughout; debt/cash absorb shortfall"; "base: debt above 1x target every year from FY28 (2.4x FY35) because negative FCF is debt-funded; bull ~1x FY28-35"; "negative cash all scenarios"; "year-0 debt 49.699 excludes Hemgenix royalty liability (478.7 at FY25)"; "value not meaningful".

- **Capex.** Finagle's default capex (method 1, driven by its 15% terminal ROIC) exceeds EBITDA every year: base capex rises from $277M in FY2028E to $1,624M in FY2035E, and bull from $597M to $3,168M [D12].
- **Base cannot hold the 1x target.** Because free cash flow is negative, base borrows to cover it: debt is $289.5M in FY2028E (7.6x EBITDA), $817.8M in FY2030E (1.6x) and $2,874M in FY2035E (2.4x) (ratios derived [C55]) [D12].
- **Bull** tracks 1.0x from FY2028E, but cash falls to −$824M by FY2035E [D12].
- **Bear** holds debt at $49.7M and cash falls to −$1,265M by FY2035E [D12].
- **Minimum cash** is −$394.0M (base), −$823.8M (bull) and −$1,265.1M (bear) (computed by Finagle outside `run_case`) [D12].
- **Royalty liability.** Year-0 debt of $49.7M is 10-K long-term debt only; the $478.7M Hemgenix royalty financing liability is not included, and no input overrode that [D12][S41].

**Run record.** Finagle commit `377f177b4013e713fe7c4603962e5f883a67e298`, run at 2026-10-29T22:20:02.462749-04:00 (Toronto time); all request hashes matched [D12]. Fetched inputs: price $24.97 (2026-10-29), 62.5M shares (10-K cover, 2026-02-26), 10-year yield 5.045%, cost of equity 10.545%, terminal growth 5.045%, year 0 = FY2025 [D12]. Validation: 0 errors and 0 missing fields in all three [D12]. One warning, on base only: "average EBITDA growth is 117.9% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero." [D12]. Sanity flags in all three: "negative cash", "negative FCFE after year 1" [D12].

**Defaults filled (Finagle's list, same in all three):** `baseline.noa`, `baseline.nol`, `distribution.mode`, `forecast.dwc.mode`, `rates.gt`, `rates.re`, `rates.roict`, `rates.t`, `year` [D12]. Debt mode, leverage, start year and cost of debt are no longer defaults; they come from David [P1][P2]. Our `me`, `mc` and `gsnext` replaced Finagle's margin defaults, applied with source "assumption" carrying our tags and left out of this list [D12].

### Method

Finagle discounts free cash flow to equity at the cost of equity. It takes our explicit revenue and EBITDA growth for FY2026E–FY2030E as given (5 explicit years) and extends them to its 10-year horizon (5 more years, to FY2035E) using the starting margin, incremental margin and next-period growth, fading to terminal growth, and then adds a terminal value [D12][D13]. Terminal growth is Finagle's default (the 10-year yield); we never set it [D12]. In v2, debt follows David's policy [P1]; any cash shortfall beyond that policy shows up as negative cash rather than new funding [D12]. Half of Finagle's horizon comes from its extension of our window.

### Valuation inputs

Figure 7 shows that debt policy and cost of debt now come from David, the margin path from us, and the remaining rates from Finagle's defaults.

**Figure 7 – Valuation inputs**

| Input | Base | Bull | Bear | Type |
|---|---|---|---|---|
| Cost of equity | 10.5% | same | same | Finagle default (0.055 + 10-yr yield) [D12] |
| Cost of debt | 10.0% | same | same | David [P2] |
| Tax rate | 21.0% | same | same | Finagle default [D12] |
| Terminal growth | 5.0% | same | same | Finagle default (= 10-yr yield; never set by us) [D12] |
| Terminal ROIC | 15.0% | same | same | Finagle default [D12] |
| Shares (M) | 62.5 | same | same | Finagle fetch, 10-K cover 2026-02-26 [D12] |
| Price (US$) | 24.97 | same | same | Finagle fetch, 2026-10-29 [D12] |
| Year-0 debt / cash (US$M) | 49.7 / 80.2 | same | same | Finagle fetch, 10-K [D12] |
| Debt policy | flat to FY2027E, then 1.0x EBITDA from FY2028E | same as base | hold at year-0 debt | David [P1] |
| Horizon (years) | 10 | same | same | Finagle default [D12] |
| Starting margin (me) | 55.8% [C25] | 67.9% [C37] | -224.2% [C45] | Forecast-file calculation |
| Incremental margin (mc) | 70.6% [S16] | 76.6% [S29] | 93.9% [S36] | Forecaster judgment |
| Next-period growth (gsnext) | 21.6% [S17] | 22.7% [S30] | 8.0% [S37] | Forecaster judgment |
| Terminal WACC | 12.0% | 11.9% | 10.6% | Finagle output [D12] |

*Source: Finagle result file v2 [D12]; David [P1][P2]; forecast.json [C25][C37][C45][S16][S17][S29][S30][S36][S37].*

How we chose the judgment inputs (unchanged from v1): the starting margin is FY2030E EBITDA over revenue [C25][C37][C45]. For base and bull, the incremental margin is the average of the starting margin and the FY2030E gross margin [S16][S29]; for bear it is the license gross margin, because opex is fixed after a restructuring [S36]. Next-period growth is FY2031E revenue from 550 (base) or 800 (bull) patients plus royalties, and royalties alone in bear [S17][S30][S37].

### Value bridge

Figure 8 shows equity value is negative in all three cases, driven by negative cash flows and a negative terminal FCFE.

**Figure 8 – Value bridge**

| US$M unless stated | Base | Bull | Bear |
|---|---|---|---|
| PV of explicit cash flows | not in result file | not in result file | not in result file |
| Terminal FCFE (fcfet, undiscounted) | -443 | -427 | -117 |
| Firm value | -3,291 | -3,293 | -1,575 |
| Less year-0 debt | 49.7 | 49.7 | 49.7 |
| Equity value | -3,341 | -3,343 | -1,624 |
| Value per share, FCFE (US$) | -52.15 | -52.18 | -24.69 |
| Value per share, DDM (US$) | -52.15 | -52.18 | -24.69 |
| Price (US$) | 24.97 | 24.97 | 24.97 |
| vs. price (derived) [C51] | -309% | -309% | -199% |

*Source: Finagle result file v2 [D12]; vs. price (derived) [C51]. The result file does not report the PV of explicit cash flows or the terminal value's share.*

### Finagle valuation table

Figure 9 shows Finagle's year-by-year output for base. Rows are Finagle's output as printed. The last three rows are labelled by Finagle as "computed outside run_case from result.years and case rates; approximate", and we show them as such. Finagle reports that interest per year, SBC per year (only year-0 17.679 passed to forecast_sbc), taxes per year, WACC per year (terminal_wacc only) are not returned by `run_case`, so they are not shown [D12].

**Figure 9 – Finagle valuation table, base case (FY2025A–FY2030E)**

*Header: QURE, price $24.97, 62.5M shares, cost of equity 10.545%, cost of debt 10% [P2], tax 21%, terminal growth 5.045%, terminal WACC 12.0% [D12].*

| US$M | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|---|
| Revenue | 16.1 | 24.9 | 114 | 335 | 640 | 944 |
| EBITDA | -153 | -161 | -131 | 37.9 | 283 | 526 |
| Capex | 0.4 | 8.1 | 85.1 | 277 | 542 | 806 |
| M&A | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Debt change | 0.0 | 0.0 | 0.0 | 240 | 255 | 273 |
| FCF | -239 | -193 | -236 | -240 | -255 | -273 |
| FCFE | -239 | -193 | -236 | 0.0 | 0.0 | 0.0 |
| FCFF | -190 | -189 | -232 | -236 | -233 | -230 |
| Debt | 49.7 | 49.7 | 49.7 | 290 | 545 | 818 |
| Cash | 80.2 | -112 | -348 | -348 | -348 | -348 |
| Cash (balance sheet) | 80.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Dividend / FCFE per share | -3.82 | -3.08 | -3.77 | -0.00 | 0.00 | 0.00 |
| Firm value | -3,291 | -3,451 | -3,584 | -3,728 | -3,896 | -4,091 |
| Equity | -3,341 | -3,501 | -3,634 | -4,017 | -4,441 | -4,909 |
| Debt / EBITDA (derived) [C55] | n.m. | n.m. | n.m. | 7.6x | 1.9x | 1.6x |
| Interest = rd × opening debt (outside run_case, approx.) | – | 5.0 | 5.0 | 5.0 | 29.0 | 54.5 |
| 1x EBITDA target debt (outside run_case) | 0.0 | 0.0 | 0.0 | 37.9 | 283 | 526 |
| Equity per share, US$ (outside run_case, approx.) | -53.43 | -55.98 | -58.12 | -64.24 | -71.02 | -78.51 |

*Source: Finagle result file v2, base years and per_year_extra [D12]; debt/EBITDA (derived) [C55].*

**Figure 9 (continued) – Finagle valuation table, base case (FY2031E–FY2035E)**

| US$M | 2031E | 2032E | 2033E | 2034E | 2035E |
|---|---|---|---|---|---|
| Revenue | 1,147 | 1,357 | 1,560 | 1,742 | 1,887 |
| EBITDA | 670 | 818 | 961 | 1,089 | 1,192 |
| Capex | 982 | 1,164 | 1,340 | 1,498 | 1,624 |
| M&A | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Debt change | 316 | 362 | 410 | 459 | 509 |
| FCF | -316 | -365 | -417 | -473 | -530 |
| FCFE | -0.2 | -3.1 | -7.5 | -13.5 | -21.6 |
| FCFF | -252 | -275 | -299 | -322 | -344 |
| Debt | 1,134 | 1,496 | 1,905 | 2,365 | 2,874 |
| Cash | -348 | -351 | -359 | -372 | -394 |
| Cash (balance sheet) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Dividend / FCFE per share | -0.00 | -0.05 | -0.12 | -0.22 | -0.35 |
| Firm value | -4,292 | -4,500 | -4,715 | -4,940 | -5,180 |
| Equity | -5,426 | -5,995 | -6,620 | -7,305 | -8,054 |
| Debt / EBITDA (derived) [C55] | 1.7x | 1.8x | 2.0x | 2.2x | 2.4x |
| Interest = rd × opening debt (outside run_case, approx.) | 81.8 | 113 | 150 | 191 | 236 |
| 1x EBITDA target debt (outside run_case) | 670 | 818 | 961 | 1,089 | 1,192 |
| Equity per share, US$ (outside run_case, approx.) | -86.78 | -95.88 | -105.87 | -116.82 | -128.80 |

*Source: Finagle result file v2 [D12]; debt/EBITDA (derived) [C55]. Note: FCFE is about zero in FY2028E–FY2030E because debt fills the gap; we flag this rather than correct it.*

Figure 10 shows bull holding 1x debt but running down cash, and bear holding debt flat while cash falls every year.

**Figure 10 – Key rows, bull case**

| US$M | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E | 2031E | 2032E | 2033E | 2034E | 2035E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 16.1 | 24.9 | 186 | 685 | 1,210 | 1,734 | 2,127 | 2,535 | 2,932 | 3,286 | 3,568 |
| EBITDA | -153 | -161 | -79.2 | 320 | 747 | 1,178 | 1,479 | 1,791 | 2,095 | 2,367 | 2,582 |
| Capex | 0.4 | 8.3 | 152 | 597 | 1,065 | 1,532 | 1,883 | 2,247 | 2,600 | 2,916 | 3,168 |
| FCFE | -239 | -193 | -245 | 26.3 | 163 | 138 | -49.3 | -83.8 | -139 | -214 | -308 |
| Debt | 49.7 | 49.7 | 49.7 | 320 | 747 | 1,178 | 1,479 | 1,791 | 2,095 | 2,367 | 2,582 |
| Cash | 80.2 | -113 | -358 | -332 | -168 | -30.6 | -79.9 | -164 | -302 | -516 | -824 |
| Debt / EBITDA (derived) [C55] | n.m. | n.m. | n.m. | 1.0x | 1.0x | 1.0x | 1.0x | 1.0x | 1.0x | 1.0x | 1.0x |

*Source: Finagle result file v2, bull years [D12]; debt/EBITDA (derived) [C55].*

**Figure 10 (continued) – Key rows, bear case**

| US$M | 2025A | 2026E | 2027E | 2028E | 2029E | 2030E | 2031E | 2032E | 2033E | 2034E | 2035E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 16.1 | 24.9 | 30.0 | 35.0 | 40.0 | 44.0 | 47.5 | 51.0 | 54.5 | 57.8 | 61.1 |
| EBITDA | -153 | -161 | -142 | -117 | -102 | -98.7 | -95.4 | -92.1 | -88.8 | -85.7 | -82.6 |
| Capex | 0.4 | 3.6 | 5.4 | 7.2 | 9.0 | 10.5 | 11.8 | 13.0 | 14.3 | 15.5 | 16.7 |
| FCFE | -239 | -188 | -169 | -143 | -128 | -126 | -123 | -121 | -118 | -116 | -114 |
| Debt | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 |
| Cash | 80.2 | -108 | -277 | -419 | -548 | -673 | -796 | -917 | -1,035 | -1,151 | -1,265 |

*Source: Finagle result file v2, bear years [D12].*

No sensitivity figure is included: David did not ask for one.

### Scenarios vs. price

Figure 12 places the three v2 values against the price; base and bull are almost equal because the capex default absorbs the extra bull EBITDA.

**Figure 12 – Scenarios vs. price**

| Scenario | AMT-130 | Value per share (US$) | Price (US$) |
|---|---|---|---|
| Bull | Approved | -52.18 [D12] | 24.97 [D12] |
| Base | Approved | -52.15 [D12] | 24.97 [D12] |
| Bear | Not approved | -24.69 [D12] | 24.97 [D12] |

*Source: Finagle result file v2 [D12]. Not meaningful (Finagle flag "value not meaningful").*

### Caveats

- **The values are not a valuation.** Finagle flags them as not meaningful; the capex default is the main remaining driver [D12].
- **Funding is not modelled.** Negative cash stands in for equity or debt raises that are not modelled [D12].
- **The royalty financing liability ($478.7M) is outside debt** [D12][S41].
- **Approval is not probability-weighted**: each scenario takes approval as 0 or 1 [S6][S31].
- **Window**: five of Finagle's ten years are its own extension of our five-year window [D12].
- **Bear**: negative EBITDA in every year; a cash-flow value says little about it [C41].

No rating or price target is drawn.

### Verified vs. assumed

Verified: actuals tie to the FY2025 10-K and Q2 2026 10-Q text (page numbers unverified) [D1][D2]; consensus pulled 2026-10-29 [D6]; every valuation number is copied from Finagle's result files [D10][D12]; David's statements are quoted as given [P1][P2]. Assumed: approval and timing, patients, net price, margins, opex and the margin path [S]; Finagle's mapping of [P1] to start year 3 and to `hold` for bear is an interpretation of David's words [D13]. Not verified: CEO profile, royalty liability size, upcoming-event dates [S38][S40][S41].

### Open questions for David

1. **Bear treatment.** Should bear be valued on cash or net assets rather than cash flow, given negative EBITDA in every year?
2. **Debt policy and cost of debt — answered** on 2026-10-29 [P1][P2]. Still open: should the $478.7M Hemgenix royalty financing liability count as debt, and what starting debt should Finagle use?
3. **Capex and ROIC.** Finagle's default capex comes from a 15% terminal ROIC and exceeds EBITDA every year. Do you want to state a capex policy or a ROIC?
4. **Stock comp and tax.** Only year-0 stock comp ($17.7M) is passed, and tax is Finagle's 21% default with no NOL. Do you want to state a stock-comp path, a tax rate or an NOL balance?
5. **Funding.** How should negative cash be treated: as an equity raise, as more debt, or left as is?
6. **Timing.** Should we wait for Q3 2026 results (2026-11-04) and the FDA's filing and priority-review decision (early November) before rerunning?

Method suggestions for the forecaster repo are in `/workspace/out/QURE_run/suggestions.md`; none were applied to the repo.

## Appendix A – Bull and Bear Cases

Figure 6 shows the bull and bear cases from the forecast file. Bull differs from base only in AMT-130 volume and price and in opex; bear removes AMT-130 entirely and cuts opex.

**Figure 6 – Bull case by line (AMT-130 approved)**

| US$M | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E |
|---|---|---|---|---|---|---|---|
| License revenue (Hemgenix royalties from CSL Behring) | 10.1 [A1] | 15.9 [A2] | 24.9 [C3] | 30.0 [S20] | 35.0 [S2] | 40.0 [S3] | 44.0 [S4] |
| Collaboration revenue (CSL services) | 10.9 [A3] | 0.2 [A4] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] |
| Contract manufacturing revenue | 6.1 [A5] | 0.0 [A13] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] |
| AMT-130 product revenue (US launch; UK not modelled separately) | 0.0 [A14] | 0.0 [A14] | 0.0 [S6] | 156 [S21] | 650 [S22] | 1,170 [S23] | 1,690 [S24] |
| **Total revenue** | 27.1 [A6] | 16.1 [A7] | 24.9 [C3] | 186 [C26] | 685 [C27] | 1,210 [C28] | 1,734 [C29] |
| Revenue growth (derived) [C49] | – | -40.6% | 54.8% | 646.5% | 268.3% | 76.6% | 43.3% |
| Gross margin | – | 89.5% [C17] | 93.9% [C30] | 86.4% [C31] | 85.5% [C32] | 85.3% [C33] | 85.2% [C34] |
| EBITDA | -149 [C12] | -153 [C13] | -161 [C16] | -79.2 [S25] | 320 [S26] | 747 [S27] | 1,178 [S28] |
| EBITDA margin (derived) [C50] | -550.9% | -949.9% | -645.9% | -42.6% | 46.8% | 61.7% | 67.9% |

*Source: forecast.json bull scenario [S20]–[S30][C26]–[C37]; derived [C49][C50].*

**Figure 6 (continued) – Bear case by line (AMT-130 not approved)**

| US$M | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E |
|---|---|---|---|---|---|---|---|
| License revenue (Hemgenix royalties from CSL Behring) | 10.1 [A1] | 15.9 [A2] | 24.9 [C3] | 30.0 [S20] | 35.0 [S2] | 40.0 [S3] | 44.0 [S4] |
| Collaboration revenue (CSL services) | 10.9 [A3] | 0.2 [A4] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] | 0.0 [S5] |
| Contract manufacturing revenue | 6.1 [A5] | 0.0 [A13] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] | 0.0 [G1] |
| AMT-130 product revenue (US launch; UK not modelled separately) | 0.0 [A14] | 0.0 [A14] | 0.0 [S31] | 0.0 [S31] | 0.0 [S31] | 0.0 [S31] | 0.0 [S31] |
| **Total revenue** | 27.1 [A6] | 16.1 [A7] | 24.9 [C3] | 30.0 [C38] | 35.0 [C39] | 40.0 [C40] | 44.0 [C41] |
| Revenue growth (derived) [C49] | – | -40.6% | 54.8% | 20.4% | 16.7% | 14.3% | 10.0% |
| Gross margin | – | 89.5% [C17] | 93.9% [C42] | 93.9% [C42] | 93.9% [C42] | 93.9% [C42] | 93.9% [C42] |
| EBITDA | -149 [C12] | -153 [C13] | -161 [C16] | -142 [S32] | -117 [S33] | -102 [S34] | -98.7 [S35] |
| EBITDA margin (derived) [C50] | -550.9% | -949.9% | -645.9% | -472.7% | -334.6% | -256.1% | -224.2% |

*Source: forecast.json bear scenario [S31]–[S37][C38]–[C45]; derived [C49][C50].*

In bull, faster uptake (60 to 650 patients) at a $2.6M net price drives FY2030E revenue to $1,734M [S21]–[S24][C29]. In bear, a complete response letter leads to a restructuring and opex of $140M by FY2029E, but royalties of $44.0M do not cover it [S32]–[S35][C41]. The scenario stories beyond these numbers (e.g. pipeline continuing after a CRL) are qualitative.

## Appendix B – Numbered sources

### Documents, Actuals, Guidance and Estimates

- **D1**: uniQure Form 10-K FY2025 (filed 2026-03-02). https://www.sec.gov/Archives/edgar/data/1590560/000110465926021898/qure-20251231x10k.htm. HTML; no page numbers
- **D2**: uniQure Form 10-Q Q2 2026 (filed 2026-07-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926087815/qure-20260630x10q.htm. HTML; no page numbers
- **D3**: uniQure Q2 2026 results press release, 8-K Ex.99.1 (2026-07-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926087808/qure-20260729xex99d1.htm. HTML; no page numbers
- **D4**: uniQure BLA submission press release, 8-K Ex.99.1 (2026-09-02). https://www.sec.gov/Archives/edgar/data/1590560/000110465926104463/qure-20260902xex99d1.htm. HTML; no page numbers
- **D5**: uniQure four-year AMT-130 data press release, 8-K Ex.99.2 (2026-09-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926111654/tm2626514d1_ex99-2.htm. HTML; no page numbers
- **D6**: Yahoo Finance / yfinance analyst revenue estimates for QURE, pulled 2026-10-29 (shown in EUR). https://finance.yahoo.com/quote/QURE/analysis/. HTML; no page numbers
- **D7**: GEN StockWatch, Leerink net-price estimates and O'Keefe pricing/TAM comments (2025). https://www.genengnews.com/topics/translational-medicine/stockwatch-uniqure-shares-reach-five-year-high-on-game-changing-huntingtons-data/. HTML; no page numbers
- **D8**: Clinaptis research, AMT-130 capacity ramp and net-price model. https://www.clinaptisresearch.com/research/amt-130-huntingtons-uniqure-bla. HTML; no page numbers
- **D9**: BioSpace, uniQure files for FDA, UK approval (2026-09). https://www.biospace.com/fda/uniqure-files-for-fda-uk-approval-of-first-gene-therapy-for-huntingtons-disease. HTML; no page numbers
- **A1**: "License revenues $ 15,934 $ 10,133 $ 2,758" (D1, page unverified)
- **A2**: "License revenues $ 15,934 $ 10,133 $ 2,758" (D1, page unverified)
- **A3**: "Collaboration revenues 164 10,872 2,250" (D1, page unverified)
- **A4**: "Collaboration revenues 164 10,872 2,250" (D1, page unverified)
- **A5**: "Contract manufacturing revenues — 6,114 10,835" (D1, page unverified)
- **A6**: "Total revenues $ 16,098 $ 27,119 $ 15,843" (D1, page unverified)
- **A7**: "Total revenues $ 16,098 $ 27,119 $ 15,843" (D1, page unverified)
- **A8**: "License revenues $ 5,841 $ 5,262 $ 9,403 $ 6,829" (D2, page unverified)
- **A9**: "Depreciation and amortization 14,759 12,641 ... Share-based compensation expense 17,679 22,258" (D1, page unverified)
- **A10**: "Loss from operations ( 52,203 ) ( 43,865 ) ( 97,923 ) ... Depreciation and amortization 7,863 ... Share-based compensation expense 10,106" (D2, page unverified)
- **A11**: "Segment reconciliation Q2 2026: Depreciation and amortization expense ( 4,907 ) Share-based compensation expense ( 5,016 )" (D2, page unverified)
- **E1**: "0y yearAgoRevenue 13623740 EUR" (D6, page unverified)
- **E2**: "0y avg 21086420 EUR, 12 analysts" (D6, page unverified)
- **E3**: "+1y avg 96184000 EUR, low 12653000, high 299146000, 11 analysts" (D6, page unverified)
- **A12**: "License revenues $ 5,841 $ 5,262 $ 9,403 $ 6,829 Total revenues 5,841 5,262 9,403 6,829" (D2, page unverified)
- **A13**: "Contract manufacturing revenues — 6,114" (D1, page unverified)
- **G1**: "divestment of our commercial manufacturing activities in July 2024" (D1, page unverified)
- **A14**: "investigational gene therapy" (D1, page unverified)
- **G2**: "today announced the submission of a Biologics License Application" (D4, page unverified)
- **D10**: Finagle (Stock Valuation Bot), `valuation_result_v1.json` with `case_{base,bull,bear}_v1.json` and `QURE_{base,bull,bear}_v1.xlsx`, run 2026-10-29, commit 377f177: /workspace/out/QURE_run/valuation_result_v1.json (local file; no URL)
- **D11**: Forecaster, `valuation_request_v1.json`, mode collaborative, empty `prompt_inputs`, `post_finagle` null, 2026-10-29: /workspace/out/QURE_run/valuation_request_v1.json (local file; no URL)
- **D12**: Finagle (Stock Valuation Bot), `valuation_result_v2.json` with `case_{base,bull,bear}_v2.json` and `QURE_{base,bull,bear}_v2.xlsx`, run 2026-10-29, commit 377f177: /workspace/out/QURE_run/valuation_result_v2.json (local file; no URL)
- **D13**: Forecaster, `valuation_request_v2.json`, mode collaborative, David's statements in `prompt_inputs`, `post_finagle` null, 2026-10-29: /workspace/out/QURE_run/valuation_request_v2.json (local file; no URL)

### User statements (prompt inputs)

- **P1**: David May, 2026-10-29: "rerun and keep debt constant until the year when EBITDA is positive. Then target 1x EBITDA from that year onward." Mapped in D13 to debt mode target, leverage 1.0, start year 3 (FY2028E) for base and bull, and mode hold for bear.
- **P2**: David May, 2026-10-29: "take rd as 10%". Mapped in D13 to rates.rd 0.10 for all three scenarios.

### Assumptions

- **S1**: Hemgenix royalty build: growth slows 20%->10% as Hemgenix uptake matures [S] x base scale to FY27 consensus (D2, page unverified)
- **S2**: Hemgenix royalty build: growth slows 20%->10% as Hemgenix uptake matures [S] (D2, page unverified)
- **S3**: Hemgenix royalty build: growth slows 20%->10% as Hemgenix uptake matures [S] (D2, page unverified)
- **S4**: Hemgenix royalty build: growth slows 20%->10% as Hemgenix uptake matures [S] (D2, page unverified)
- **S5**: Collaboration services to CSL wound down after the 2024 Lexington Transaction; none in H1 2026 [S] (D1, page unverified)
- **S6**: No AMT-130 product revenue: no approval before 2027 (PDUFA late Apr/early May 2027 only if priority review). (D9, page unverified)
- **S7**: base: 40 patients x $2.0M net price x scale to FY27 consensus [S] (D8, page unverified)
- **S8**: base: 150 patients x $2.0M net price [S] (D8, page unverified)
- **S9**: base: 300 patients x $2.0M net price [S] (D8, page unverified)
- **S10**: base: 450 patients x $2.0M net price [S] (D8, page unverified)
- **S11**: Gene-therapy product gross margin after COGS and licensor royalties; no uniQure disclosure [S] (D8, page unverified)
- **S12**: base: license GP + AMT-130 GP - cash opex 230 [S: launch build + confirmatory study] (D3, page unverified)
- **S13**: base: license GP + AMT-130 GP - cash opex 250 [S: launch build + confirmatory study] (D3, page unverified)
- **S14**: base: license GP + AMT-130 GP - cash opex 265 [S: launch build + confirmatory study] (D3, page unverified)
- **S15**: base: license GP + AMT-130 GP - cash opex 280 [S: launch build + confirmatory study] (D3, page unverified)
- **S16**: Average of me and FY30 gross margin (Finagle's own default rule), no positive-EBITDA history to set it against [S] (D2, page unverified)
- **S17**: FY31 growth: royalty 47.5 + 550 AMT-130 patients x $2.0M vs FY30 revenue [S] (D8, page unverified)
- **S18**: No acquisitions in the window; organic = total (D2, page unverified)
- **S19**: No pending deals disclosed in the Q2 2026 10-Q or later 8-Ks (D2, page unverified)
- **S20**: Hemgenix royalty build: growth slows 20%->10% as Hemgenix uptake matures [S] (D2, page unverified)
- **S21**: bull: 60 patients x $2.6M net price [S] (D8, page unverified)
- **S22**: bull: 250 patients x $2.6M net price [S] (D8, page unverified)
- **S23**: bull: 450 patients x $2.6M net price [S] (D8, page unverified)
- **S24**: bull: 650 patients x $2.6M net price [S] (D8, page unverified)
- **S25**: bull: license GP + AMT-130 GP - cash opex 240 [S: launch build + confirmatory study] (D3, page unverified)
- **S26**: bull: license GP + AMT-130 GP - cash opex 265 [S: launch build + confirmatory study] (D3, page unverified)
- **S27**: bull: license GP + AMT-130 GP - cash opex 285 [S: launch build + confirmatory study] (D3, page unverified)
- **S28**: bull: license GP + AMT-130 GP - cash opex 300 [S: launch build + confirmatory study] (D3, page unverified)
- **S29**: Average of me and FY30 gross margin (Finagle's own default rule), no positive-EBITDA history to set it against [S] (D2, page unverified)
- **S30**: FY31 growth: royalty 47.5 + 800 AMT-130 patients x $2.6M vs FY30 revenue [S] (D8, page unverified)
- **S31**: No AMT-130 product revenue: bear case, AMT-130 not approved. (D5, page unverified)
- **S32**: bear: license GP + AMT-130 GP - cash opex 170 [S: restructuring after a CRL; pipeline continues] (D3, page unverified)
- **S33**: bear: license GP + AMT-130 GP - cash opex 150 [S: restructuring after a CRL; pipeline continues] (D3, page unverified)
- **S34**: bear: license GP + AMT-130 GP - cash opex 140 [S: restructuring after a CRL; pipeline continues] (D3, page unverified)
- **S35**: bear: license GP + AMT-130 GP - cash opex 140 [S: restructuring after a CRL; pipeline continues] (D3, page unverified)
- **S36**: Bear: opex is fixed after restructuring, so an incremental royalty dollar drops through at the license gross margin; the default (me+GM)/2 is negative and meaningless when me < 0 [S] (D2, page unverified)
- **S37**: FY31 growth: Hemgenix royalty only, 44 -> 47.5 [S] (D8, page unverified)

### Calculations

- **C1**: FY25/FY24 - 1 license revenues = f(A1, A2) (D1)
- **C2**: FY26E consensus - H1A = f(E2, E1, A8) (D6)
- **C3**: FY26 consensus EUR x fx; all royalty/license, no AMT-130 sales before approval = f(E2, E1, A7) (D6)
- **C4**: FY25/FY24 - 1 collaboration revenues = f(A3, A4) (D1)
- **C5**: FY25/FY24 - 1 contract manufacturing = f(A5) (D1)
- **C6**: 1 - cost of license revenues 569 / license revenues 9,403, H1 2026 = f(A10, A8) (D2)
- **C7**: FY25/FY24 - 1 total revenue = f(A6, A7) (D1)
- **C8**: FY27 mean consensus EUR 96.184M x fx; base lines scaled to it = f(E3, E1, A7) (D6)
- **C9**: Sum of base lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C10**: Sum of base lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C11**: Sum of base lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C12**: EBITDA = loss from operations -184,294 + D&A 12,641 + SBC 22,258 (2024) = f(A9) (D1)
- **C13**: EBITDA = loss from operations -185,349 + D&A 14,759 + SBC 17,679 (2025) = f(A9, A7) (D1)
- **C14**: EBITDA = loss from operations -97,923 + D&A 7,863 + SBC 10,106 (H1 2026) = f(A10, A11) (D2)
- **C15**: FY25/FY24 - 1 EBITDA (both negative: a larger loss) = f(A9, A7) (D1)
- **C16**: H1A EBITDA + H2 revenue x license GM - 2 x Q2 cash opex net of other income/expense (47.771) [S run rate] = f(A10, A11) (D3)
- **C17**: (revenue - cost of license revenues 1,686)/revenue 2025 = f(A9, A7) (D1)
- **C18**: Revenue-weighted line gross margins base = f(A10, A11) (D2)
- **C19**: Revenue-weighted line gross margins base = f(A10, A11) (D2)
- **C20**: Revenue-weighted line gross margins base = f(A10, A11) (D2)
- **C21**: Revenue-weighted line gross margins base = f(A10, A11) (D2)
- **C22**: Revenue-weighted line gross margins base = f(A10, A11) (D2)
- **C23**: Organic revenue growth FY26-FY30, base = f(A7, E2, E3) (D6)
- **C24**: Organic EBITDA ratio E_t/E_t-1 - 1 FY26-FY30, base = f(A9, A7) (D3)
- **C25**: FY30E EBITDA / FY30E revenue, base = f(A9, A7) (D3)
- **C26**: Sum of bull lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C27**: Sum of bull lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C28**: Sum of bull lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C29**: Sum of bull lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C30**: Revenue-weighted line gross margins bull = f(A10, A11) (D2)
- **C31**: Revenue-weighted line gross margins bull = f(A10, A11) (D2)
- **C32**: Revenue-weighted line gross margins bull = f(A10, A11) (D2)
- **C33**: Revenue-weighted line gross margins bull = f(A10, A11) (D2)
- **C34**: Revenue-weighted line gross margins bull = f(A10, A11) (D2)
- **C35**: Organic revenue growth FY26-FY30, bull = f(A7, E2, E3) (D6)
- **C36**: Organic EBITDA ratio E_t/E_t-1 - 1 FY26-FY30, bull = f(A9, A7) (D3)
- **C37**: FY30E EBITDA / FY30E revenue, bull = f(A9, A7) (D3)
- **C38**: Sum of bear lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C39**: Sum of bear lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C40**: Sum of bear lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C41**: Sum of bear lines (no consensus beyond FY27 / not applicable to this scenario) = f(E3, E1) (D8)
- **C42**: Revenue-weighted line gross margins bear = f(A10, A11) (D2)
- **C43**: Organic revenue growth FY26-FY30, bear = f(A7, E2, E3) (D6)
- **C44**: Organic EBITDA ratio E_t/E_t-1 - 1 FY26-FY30, bear = f(A9, A7) (D3)
- **C45**: FY30E EBITDA / FY30E revenue, bear = f(A9, A7) (D3)
- **C46**: USD per EUR implied: reported FY25 revenue 16.098 / Yahoo FY25 year-ago revenue EUR 13.624 = f(A7, E1) (D6)
- **C47**: Q2 2026 gross profit (5.841-0.350) - Q2 EBITDA (-52.203+4.907+5.016) = f(A10, A11) (D3)
- **C48**: FY27 consensus / unscaled base line build = f(E3, E1) (D6)
- **C49**: Growth (derived) = value_t / value_t−1 − 1 from Figure 1/5/6 totals; n.m. when either value is negative.
- **C50**: EBITDA margin (derived) = EBITDA / revenue, same tags as the totals.
- **C51**: vs. price (derived) = Finagle value per share / $24.97 − 1 [D10][D12].
- **C52**: Revenue share (derived) = line / total FY2025A [A2][A4][A7].
- **C53**: $0.1M × 450 base FY2030E patients = $45M (derived) [S10].
- **C54**: FY2035E base capex 1,624 / EBITDA 1,192 (derived) [D10][D12].
- **C55**: Debt / EBITDA (derived) = Finagle year-end debt / Finagle EBITDA, same year [D12].
- **C56**: Change v1 → v2 value per share (derived) = v2 − v1 [D10][D12].

### Not verified

- **S38**: CEO Matt Kapusta, CEO since 2017, previously CFO: general knowledge, link unverified, date unknown.
- **S39**: 48-month cUHDRS 44%, p=0.144, and FDA wanting the confirmatory study under way: from the forecast's assumption notes citing D5; page unverified.
- **S40**: Q3 2026 results 2026-11-04 and FDA filing decision in early November: from forecast.md open items; link unverified.
- **S41**: Hemgenix royalty financing liability: about $495M in the Forecaster's v1 notes; $478.7M at FY2025 in Finagle's v2 flags [D12]. Neither figure is tied to a filing page in the forecast file; page unverified.
- All A, E and S entries above: HTML filings, page unverified.

## Appendix C – Method

We built the forecast line by line from uniQure's reported revenue types plus a new AMT-130 line. With no company guidance, FY2026E totals use consensus in all scenarios and FY2027E uses consensus in base only; other years use the line build. AMT-130 revenue is patients times net price; royalties follow a slowing growth path; EBITDA is gross profit by line less cash opex. Each scenario is defined by whether AMT-130 is approved. The explicit window runs five years to FY2030E so that the hand-off to Finagle starts from a steady-state launch margin rather than a pre-launch loss. The forecast passed the repo's validator and request check with 0 errors.
