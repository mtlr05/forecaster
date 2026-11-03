# uniQure N.V. (Nasdaq: QURE)

## Company Update: FY2026E–FY2033E Revenue and EBITDA Forecast and Finagle Run (revision 3, valuation v7)

*30 October 2026. US$ millions unless a row states patients or a count. Forecast only: no rating, price target or valuation. Includes a Finagle valuation section, but Finagle flagged base and bull NOT A VALUATION and bear is marginal (Section 8); no rating or price target. Forecast: rev3 `forecasts/QURE/forecast.json` (uncommitted); valuation: Finagle v7 run of `valuation_request_v7.json` [D43][D44]. Numbered sources are in Appendix B.*

## 1. Summary

**FORECAST UPDATE**

■ **Year one is no longer limited by center count, per the user [P7]: US treatments follow a 10 / 30 / 60 / 90 patients-a-quarter path, about 190 in the first four quarters after the 1 July 2027 approval [S8].** That path came from the Matt Kapusta CEO-simulation bot and is an assumption, not a company figure. Base FY2027E revenue falls to $110M from $1,067M in revision 2b [C18], and FY2028E to $1,364M from $5,940M.

■ **Year two bridges from 90 patients a quarter to 30 centers by mid-2029 [S10].** ClearPoint said in August 2026 that 15 centers had qualified and the goal is 20–30 [G1]. The user's ~30 centers at 1–2 procedures a week [P5] is therefore reached at the end of year two, not at launch. After that the revision 2b logic applies unchanged.

■ **The ~6,000-patient backlog is cleared in Q1 2031 in base (bull Q4 2031), versus Q4 2029 (bull Q4 2029) in revision 2b.** Cumulative US treatments pass 6,000 in Q3 2030. After that, treatments fall to the yearly refill of 1,124 patients [P3][C2], and revenue falls to $2,073M in FY2032E [C23].

■ **EBITDA peaks at $6,790M in FY2030E and settles at a 67% margin [S31][C41].** Opex now includes a $70M-a-year confirmatory study [S1] and $80M of US commercial fixed cost. Hemgenix royalties were sold to HemB SPV and are booked as $473.2M of debt [A14].

**Figure 1 – Base case: patients and financials (FY2026E–FY2032E)**

| Row (units) | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E |
|---|---|---|---|---|---|---|---|
| US patients treated (patients/yr) | 0 [C74] | 40 [C75] | 665 [C76] | 2,365 [C77] | 4,329 [C78] | 1,957 [C79] | 1,124 [C80] |
| US eligible backlog, year end (patients) | 6,000 [C66] | 6,206 [C67] | 6,029 [C68] | 4,269 [C69] | 834 [C70] | 0 [C71] | 0 [C72] |
| Revenue (US$M) | 24.9 [C6] | 110 [C18] | 1,364 [C19] | 4,770 [C20] | 8,702 [C21] | 3,570 [C22] | 2,073 [C23] |
| EBITDA (US$M) | -161 [C29] | -237 [S28] | 723 [S29] | 3,503 [S30] | 6,790 [S31] | 2,544 [S32] | 1,390 [S33] |

*Source: forecast file, base case; patient rows from the capacity model [S6][C2].*

## 2. Business Description and Reporting Lines

uniQure is a gene-therapy company. Almost all of its revenue today is royalties on Hemgenix, the haemophilia B gene therapy licensed to CSL Behring [A21]. AMT-130 for Huntington's disease (HD) is a one-time AAV5 gene therapy given by MRI-guided neurosurgery, delivered with ClearPoint Neuro's system. Its BLA and a UK MAA were filed on 2 September 2026 [G12]. The reported lines are license (royalty), collaboration and contract manufacturing revenue. We add AMT-130 product lines for the US and, in bull only, the UK. Genezen makes AMT-130 and gives it preferential access to its plant [G13].

## 3. Management

CEO Matt Kapusta and Chief Customer & Strategy Officer Kylie O'Keefe set out the launch plan, including ~6,000 "initially treatable" US patients [G5][G6]. Management gives no capacity number; it says capacity depends on neurosurgeons and OR suites [G9]. ClearPoint, the delivery partner, has given center counts [G1][G2].

## 4. Key Developments

| Date | Event | Source |
|---|---|---|
| 2025-09-24 | Investor event: ~6,000 initially treatable US patients at launch | [G5] |
| 2026-07-29 | Q2 2026: confirmatory-study design agreed with FDA; runway into 2030 | [G4][A22] |
| 2026-08-10 | ClearPoint: 15 centers qualified, ready for 1–2 procedures a week | [G1] |
| 2026-09-02 | BLA submitted; UK MAA filed, priority review requested | [G12] |
| 2026-10-28 | ClearPoint: approval possible mid to second half of 2027 | [G3] |
| 2026-10-30 | User: ~30 centers at 1–2 procedures a week | [P5] |
| 2026-10-30 | User: centers do not limit year one; use the ~190 path | [P7] |
| 2026-11-04 | Q3 2026 results due | [S402] |

*Source: company filings and calls; user prompts.*

## 5. Business Drivers by Line

**AMT-130 US: capacity.** Treated = min(capacity, backlog + refill). Year one (Q3 2027–Q2 2028) is a fixed path of 10, 30, 60 and 90 patients a quarter; centers do not bind [P7][S8]. Year two (Q3 2028–Q2 2029) rises in a straight line from 90 a quarter to 30 centers × 1.375 procedures a week × 13 weeks = 536 a quarter, with centers going from 15 to 30 [S10]. From Q3 2029, centers grow by 3 a quarter while patients are waiting, capped at 70, and throughput rises to 2.0 a week [S6]. The cap does not bind. HDSA has 69 HD centers [A12]. ClearPoint targets 35–40 initial centers with 5,000 patients a year of capacity across all its partners [G2]. We assume vector supply does not bind through FY2029E.

**Figure 2 – Base capacity ramp by quarter (US)**

| Quarter | Centers active (count) | Procedures per center per week | Utilisation (%) | Capacity (patients/qtr) | Treated (patients/qtr) | Backlog at quarter end (patients) |
|---|---|---|---|---|---|---|
| Q3 2027 | 15 | 0.000 | n/a | 10 | 10 | 6,114 |
| Q4 2027 | 15 | 0.000 | n/a | 30 | 30 | 6,206 |
| Q1 2028 | 15 | 0.000 | n/a | 60 | 60 | 6,266 |
| Q2 2028 | 15 | 0.000 | n/a | 90 | 90 | 6,296 |
| Q3 2028 | 19 | 1.000 | 83% | 202 | 202 | 6,216 |
| Q4 2028 | 22 | 1.125 | 95% | 313 | 313 | 6,029 |
| Q1 2029 | 26 | 1.250 | 100% | 425 | 425 | 5,738 |
| Q2 2029 | 30 | 1.375 | 100% | 536 | 536 | 5,345 |
| Q3 2029 | 33 | 1.500 | 100% | 644 | 644 | 4,858 |
| Q4 2029 | 36 | 1.625 | 100% | 760 | 760 | 4,269 |
| Q1 2030 | 39 | 1.750 | 100% | 887 | 887 | 3,571 |
| Q2 2030 | 42 | 1.875 | 100% | 1024 | 1024 | 2,758 |

*Source: year one [S8] per the user [P7]; bridge [S10]; assumptions [S6] anchored on the user [P5] and ClearPoint [G1]; backlog per [G5][C2][S5].*

**Demand.** The backlog starts at 6,000 [G5]. Each year adds the refill: incidence less a few for eligibility, willingness and coverage [P3]. The untreated backlog loses 10% a year [S5].

**Price and recognition.** Base net price is $2.0M through FY2030E, then 10% lower from FY2031E once US sales have passed $2B a year [S14]. Bull is $2.4M, stepping down from FY2028E [S15]. For comparison, list prices are $4.25M for Lenmeldy, $3.95M for Kebilidi, $3.2M for Elevidys and about $3.5M for Hemgenix [A13]. We recognise revenue at treatment [S401].

**Costs.** COGS per patient is $0.30M at launch, falling to $0.20M; it is unverified [S16]. No AMT-130 licensor royalty is disclosed [A15]. Opex is the Q2 2026 run rate [A22], plus US commercial fixed cost, per-center cost, and the confirmatory study [S1].

**Hemgenix royalties.** These stay in revenue and EBITDA, growing to $52.2M in FY2033E [S24]. The cash goes to HemB SPV until 1.85× the upfront ($693.8M) is repaid by mid-2032, or up to 2.25× through 2038 [A14]. For valuation, the user decided the $473.2M liability is not debt [P105].

## 6. Risks

**Year-one path and bridge.** The ~190 year-one path is from a CEO-simulation bot, not uniQure [S8]. The year-two bridge is our assumption [S10]. A slower ramp pushes treatments later but does not change the total.

**Refill.** If refill is 30% of incidence, it falls to 490 patients a year, and FY2031E base revenue falls to $929M. This is the key open question (Figure 5).

**Approval timing.** If approval comes in Q4 2027, FY2027E base revenue is $50M and the backlog clears one quarter later (Figure 5).

**Payer budget.** Base US spend peaks near $8.7B in FY2030E, a single year of backlog clearance. That invites managed access.

**Consensus.** FY2027E base revenue is 0.97× consensus. It is not scaled; it lands close to consensus anyway [C205]. Goldman's reported peak is $2.5B [E6].

**Figure 5 – Sensitivities (US patients; US$M)**

| Case (units) | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E | FY33E |
|---|---|---|---|---|---|---|---|
| base filed: US treated (patients/yr) | 40 | 665 | 2,365 | 4,329 | 1,957 | 1,124 | 1,124 |
| base filed: revenue (US$M) | 110 | 1,364 | 4,770 | 8,702 | 3,570 | 2,073 | 2,075 |
| base filed: EBITDA (US$M) | -237 | 723 | 3,503 | 6,790 | 2,544 | 1,390 | 1,386 |
| base approval Q4 2027 (2027-10-01): US treated (patients/yr) | 10 | 382 | 1,918 | 3,842 | 3,011 | 1,124 | 1,124 |
| base approval Q4 2027 (2027-10-01): revenue (US$M) | 50.0 | 798 | 3,875 | 7,727 | 5,468 | 2,073 | 2,075 |
| base approval Q4 2027 (2027-10-01): EBITDA (US$M) | -285 | 270 | 2,774 | 5,986 | 4,115 | 1,390 | 1,386 |
| base Kapusta refill 30% of incidence: US treated (patients/yr) | 40 | 665 | 2,365 | 3,292 | 490 | 490 | 490 |
| base Kapusta refill 30% of incidence: revenue (US$M) | 110 | 1,364 | 4,770 | 6,627 | 929 | 931 | 934 |
| base Kapusta refill 30% of incidence: EBITDA (US$M) | -237 | 723 | 3,503 | 5,068 | 358 | 433 | 428 |
| bull filed: US treated (patients/yr) | 60 | 942 | 3,263 | 5,460 | 6,607 | 2,872 | 2,872 |
| bull filed: revenue (US$M) | 174 | 2,472 | 8,084 | 13,008 | 15,489 | 7,041 | 6,660 |
| bull filed: EBITDA (US$M) | -187 | 1,645 | 6,254 | 10,473 | 12,720 | 5,698 | 5,376 |
| bull approval Q4 2027 (2027-10-01): US treated (patients/yr) | 15 | 554 | 2,657 | 4,940 | 7,020 | 3,659 | 2,872 |
| bull approval Q4 2027 (2027-10-01): revenue (US$M) | 66.0 | 1,540 | 7,410 | 11,884 | 16,381 | 8,740 | 6,660 |
| bull approval Q4 2027 (2027-10-01): EBITDA (US$M) | -276 | 872 | 5,773 | 9,530 | 13,492 | 7,171 | 5,376 |
| bull Kapusta refill 30% of incidence: US treated (patients/yr) | 60 | 942 | 3,263 | 4,011 | 1,061 | 1,061 | 1,061 |
| bull Kapusta refill 30% of incidence: revenue (US$M) | 174 | 2,472 | 8,084 | 9,877 | 3,509 | 3,128 | 2,747 |
| bull Kapusta refill 30% of incidence: EBITDA (US$M) | -187 | 1,645 | 6,254 | 7,869 | 2,523 | 2,308 | 1,985 |

## 7. Forecast

Revenue = patients treated × net price. EBITDA = gross profit less cash opex. FY2026E revenue is consensus. Figure 3 shows the base case, with every patient row in patients and every dollar row in US$M.

**Figure 3 – Base, FY2024A–FY2031E**

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|---|---|---|
| US treatment centers at year end (count) | – | – | 0 [C42] | 15 [C43] | 22 [C44] | 36 [C45] | 48 [C46] | 30 [C47] |
| US treatment capacity (patients/yr) | – | – | 0 [C50] | 40 [C51] | 665 [C52] | 2,365 [C53] | 4,329 [C54] | 3,666 [C55] |
| US refill demand (patients/yr) | – | – | 0 [C58] | 562 [C59] | 1,124 [C60] | 1,124 [C61] | 1,124 [C62] | 1,124 [C63] |
| US eligible backlog at year end (patients) | – | – | 6,000 [C66] | 6,206 [C67] | 6,029 [C68] | 4,269 [C69] | 834 [C70] | 0 [C71] |
| **US patients treated (patients/yr)** | – | – | 0 [C74] | 40 [C75] | 665 [C76] | 2,365 [C77] | 4,329 [C78] | 1,957 [C79] |
| US cumulative treated (patients) | – | – | 0 [C82] | 40 [C83] | 705 [C84] | 3,070 [C85] | 7,399 [C86] | 9,356 [C87] |
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C6] | 30.0 [S18] | 35.0 [S19] | 40.0 [S20] | 44.0 [S21] | 47.5 [S22] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A24] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S26] | 80.0 [C9] | 1,329 [C10] | 4,730 [C11] | 8,658 [C12] | 3,523 [C13] |
| AMT-130 revenue, UK (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] | 0.0 [S27] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C6] | 110 [C18] | 1,364 [C19] | 4,770 [C20] | 8,702 [C21] | 3,570 [C22] |
| Gross margin (%) | – | 89.5% [C30] | 93.9% [C31] | 87.4% [C32] | 86.2% [C33] | 87.1% [C34] | 88.0% [C35] | 87.9% [C36] |
| **EBITDA (US$M)** | -149 [C25] | -153 [C26] | -161 [C29] | -237 [S28] | 723 [S29] | 3,503 [S30] | 6,790 [S31] | 2,544 [S32] |
| EBITDA margin (%, derived) [C401] | -550.9% | -949.9% | -645.9% | -215.6% | 53.0% | 73.4% | 78.0% | 71.3% |

**Figure 4 – Base, FY2032E–FY2033E**

| Row (units) | FY32E | FY33E |
|---|---|---|
| US treatment centers at year end (count) | 30 [C48] | 30 [C49] |
| US treatment capacity (patients/yr) | 3,120 [C56] | 3,120 [C57] |
| US refill demand (patients/yr) | 1,124 [C64] | 1,124 [C65] |
| US eligible backlog at year end (patients) | 0 [C72] | 0 [C73] |
| **US patients treated (patients/yr)** | 1,124 [C80] | 1,124 [C81] |
| US cumulative treated (patients) | 10,479 [C88] | 11,603 [C89] |
| License revenue, Hemgenix royalties (US$M) | 50.0 [S23] | 52.2 [S24] |
| Collaboration revenue (US$M) | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 2,023 [C14] | 2,023 [C14] |
| AMT-130 revenue, UK (US$M) | 0.0 [S27] | 0.0 [S27] |
| **Total revenue (US$M)** | 2,073 [C23] | 2,075 [C24] |
| Gross margin (%) | 89.0% [C37] | 89.0% [C38] |
| **EBITDA (US$M)** | 1,390 [S33] | 1,386 [S34] |
| EBITDA margin (%, derived) [C401] | 67.1% | 66.8% |

*me 66.8% [C41], mc 77.9% [S35], gsnext 0.08% [S36]. Totals may not sum due to rounding.*

## 8. Valuation – base and bull NOT A VALUATION; bear marginal

**Finagle flagged base and bull `not_a_valuation: true`. Those per-share figures are mechanical outputs of a default policy that misfires for this company, not values we stand behind. Bear is not flagged, but it is marginal [D43].** Value per share (FCFE, equal to DDM): base $155.69, bull $471.82, bear $0.62, against a price of $25.30 on 2026-10-30. No post-Finagle adjustments were made.

Reasons, in Finagle's words:

- **base:** negative derived D&A from default roict 0.15 (min -447.1, terminal -107.0); Finagle log warning. Sanity flags: negative FCFE after year 1.
- **bull:** negative derived D&A from default roict 0.15 (min -1027.4, terminal -445.6); Finagle log warning. Sanity flags: negative FCFE after year 1.
- **bear:** not flagged. Sanity flags: negative FCFE after year 1.

**Why bear is marginal.** Bear EBITDA is negative in every year (FY2026E -161 to FY2035E -88.2), so FCFE is negative after year 1 and Finagle's equity value is -1,358. The positive $0.62 comes from adding year-0 cash of 1,430, most of it our assumed 1,350 raise, and dividing by 115.89M shares: (-1,358 + 1,430) / 115.89 = $0.62 [C505]. The equity value itself includes a terminal value on perpetual losses at 2.00% growth (terminal FCFE -117). Read it as roughly zero: the raise is used up by losses, and cash falls to 78.9 by FY2035E.

**Figure 7 – v6 vs v7 (both on forecast rev3)**

| Item (US$M unless stated) | Base v6 | Base v7 | Bull v6 | Bull v7 | Bear v6 | Bear v7 |
|---|---|---|---|---|---|---|
| Value per share (US$) | $230.22 | $155.69 | $728.73 | $471.82 | -$24.97 | $0.62 |
| Value per share, DDM (US$) | $230.22 | $155.69 | $728.73 | $471.82 | -$24.97 | $0.62 |
| Equity value | 14,315 | 11,716 | 45,487 | 35,600 | -1,642 | -1,358 |
| Firm value | 14,365 | 11,766 | 45,537 | 35,649 | -1,592 | -1,309 |
| Terminal-year FCFE | 864 | 733 | 3,651 | 3,339 | -118 | -117 |
| Terminal WACC | 10.01% | 9.61% | 10.29% | 10.12% | 10.55% | 10.60% |
| Shares (M) | 62.53 | 78.34 | 62.53 | 76.36 | 62.53 | 115.89 |
| Year-0 cash | 80.2 | 480 | 80.2 | 430 | 80.2 | 1,430 |
| Minimum cash | -370 | 29.89 | -320 | 29.69 | -1,270 | 78.89 |
| Debt peak | 6,790 | 6,790 | 12,720 | 12,720 | 49.70 | 49.70 |
| Max debt / EBITDA (x) | 3.75 | 3.71 | 1.75 | 1.74 | n/a | n/a |
| not_a_valuation | True | True | True | True | True | False |
| Change in value per share v6 to v7 (US$) [C503] | | -$74.53 | | -$256.91 | | $25.59 |

*Source: Finagle v6 [D40] and v7 [D43] results; difference derived [C503].*

**Why v7 differs from v6.** The forecast is unchanged (rev3). The user's t64u inputs changed [P105]: year-0 D&A 0.2195, tax 25.8%, terminal growth 2%, and a year-0 equity raise. The raise adds cash at $25.30 a share. Base and bull values per share are far above the price, so issuing at the price dilutes them. Lower terminal growth and the higher tax rate would also be expected to lower value. The files do not split the change between these drivers, so we do not attribute it.

**Figure 8 – Year-0 equity raise (sizes are our assumption)**

| Scenario | v6 minimum cash | Raise [S] | Price (US$) | New shares (M) [C504] | Total shares (M) | Year-0 cash | v7 minimum cash |
|---|---|---|---|---|---|---|---|
| base | -370 | 400 | 25.30 | 15.810 | 78.340 | 480 | 29.9 |
| bull | -320 | 350 | 25.30 | 13.834 | 76.363 | 430 | 29.7 |
| bear | -1,270 | 1,350 | 25.30 | 53.360 | 115.889 | 1,430 | 78.9 |

*Source: v6 [D40] and v7 [D43] results; request v7 [D44]. Raise sizes were rounded up from the v6 minimum cash with a margin [S]. Shares are issued at the fetched price with no discount or fees [S].*

The user asked for cash and shares to be added in year 0 so that cash never goes negative [P105]. That holds in all three scenarios: minimum cash is base 29.9, bull 29.7 and bear 78.9 [D43]. Finagle earns no interest on cash, so the raise passes through one for one.

**D&A and capex.** Finagle derives D&A, and it is still negative in base and bull. Base D&A starts at -0.2 in FY2026E, reaches a minimum of -447 in FY2030E and ends at -107 in the terminal year. Bull reaches -1,027 in FY2031E and ends at -446. Base capex runs from 3.5 to 131 [D43]. Finagle's log warns: "negative depreciation in terminal year, check roic and growth assumptions". Finagle attributes this to the default terminal ROIC of 15.00%. The user's year-0 D&A of 0.2195 only sets year 0. Bear D&A is positive, from 4.0 to 17.2, against capex of 5.0.

**Figure 9 – D&A path (derived) by scenario**

| Scenario | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E | FY2032E | FY2033E | FY2034E | FY2035E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| base | 0.2 | -0.2 | -4.6 | -69.2 | -245 | -447 | -183 | -106 | -106 | -106 | -107 |
| bull | 0.2 | -0.4 | -10.3 | -163 | -536 | -863 | -1,027 | -466 | -441 | -441 | -446 |
| bear | 0.2 | 4.0 | 6.3 | 8.4 | 10.6 | 12.3 | 13.8 | 14.9 | 15.9 | 16.6 | 17.2 |

*Source: Finagle v7 notebook replay [D43].*

**Debt path.** The HemB royalty liability ($473.2M) is not debt, per the user [P105]. Finagle's opening debt is the 10-K 49.699, and the royalties stay in revenue and EBITDA. The user confirmed the 1x EBITDA rule [P103][P105]. Base debt is held to FY2027E, then targets 1x EBITDA from FY2028E and peaks at 6,790. As EBITDA falls after the backlog clears, debt does not come down with it: base debt is 2.22x–3.71x EBITDA in FY2031E–FY2035E (maximum 3.71x). Bull debt peaks at 12,720 (maximum 1.74x). Bear debt is held at 49.7 [D43].

**Figure 10 – Debt path by scenario**

| Scenario | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E | FY2032E | FY2033E | FY2034E | FY2035E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| base | 49.7 | 49.7 | 49.7 | 723 | 3,503 | 6,790 | 5,640 | 5,162 | 4,649 | 4,093 | 3,479 |
| bull | 49.7 | 49.7 | 49.7 | 1,645 | 6,254 | 10,473 | 12,720 | 9,923 | 7,131 | 5,377 | 5,435 |
| bear | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 |

*Source: Finagle v7 notebook replay [D43].*

**NOL and cash tax.** The opening NOL is 539 [P104]. It grows with losses (base 723 in FY2026E and 978 in FY2027E) and offsets 100% of pre-tax income, with no Dutch 50% / EUR1M cap. Base has 258 left after FY2028E and 0.0 from FY2029E; bull is used up in FY2028E (0.0). At 25.8%, base cash tax is 186 in FY2028E, peaks at 1,665 in FY2030E and is 257 in FY2035E. Bull peaks at 3,077. Bear pays no tax after year 0, and its NOL grows to 1,964 [D43]. This NOL treatment is more generous than Dutch law.

**Cash build-up.** No payout is modelled (distribution.mode is a Finagle default). Cash therefore accumulates: base reaches 13,886 and bull 36,405 by FY2035E [D43].

**SBC and capex lists.** These are the same as in v6 [D44]. SBC is $17.7M until FY2027E, then 5% of sales in base and bull, and flat in bear. Capex is $3.5M in FY2026E–FY2027E, then the larger of $5M or 1.5% of revenue. **The FY2034E–FY2035E values were built on revenue extended at 4.989% terminal growth.** At 2%, Finagle's FY2035E revenue is lower (base 2,128.9 → 2,097.9; bull 6,828.1 → 6,728.5; bear 56.0 → 55.2, from the request note [D44]), so those two years' SBC and capex are slightly high.

**Terminal growth vs the forecaster.** The user set terminal growth at 2% [P105]. The forecaster's gsnext stays at 0.08% base, 0.02% bull and 3.00% bear. Finagle moves from gsnext to 2% over FY2033E–FY2035E, so base and bull growth rises to 2% and bear falls from 3% to 2%. The two settings conflict and have not been reconciled.

**Defaults filled (Finagle's words):** baseline.noa, distribution.mode, forecast.dwc.mode, rates.re, rates.roict, year [D43].

**Figure 11 – Valuation inputs**

| Input | Base | Bull | Bear | Source |
|---|---|---|---|---|
| Cost of equity | 10.49% | same | same | Finagle default [D43] |
| Cost of debt | 10.00% | same | same | user [P101] |
| Tax rate | 25.80% | same | same | user, Dutch rate [P105]; v6 used the 21% default |
| Terminal growth | 2.00% | same | same | user [P105]; v6 used the 4.989% default |
| Terminal ROIC (roict) | 15.00% | same | same | **Finagle default, not set by the user** [D43] |
| Year-0 D&A | 0.2195 | same | same | user: half of year-0 capex 0.439 [P105]; replaces 0.48294 [P102] |
| Year-0 cash (US$M) | 480 | 430 | 1,430 | 10-K 80.24 + raise; raise size [S] [P105] |
| Shares (M) | 78.340 | 76.363 | 115.889 | 10-K 62.529 + raise / price [P105][C504] |
| Price (2026-10-30) | $25.30 | same | same | Finagle fetch [D43] |
| Year-0 debt (US$M) | 49.699 | same | same | 10-K; HemB liability not debt, per the user [P105] |
| Year-0 NOL (US$M) | 539 | same | same | Dutch NOL, 10-K p.160 [P104][D44] |
| me / mc / gsnext | 66.8% / 77.9% / 0.08% | 80.7% / 86.1% / 0.02% | -174.0% / 93.9% / 3.00% | forecast rev3 [D41] |
| Debt policy | 1.0x EBITDA from FY2028E | same | hold | user [P103][P105] |

*Source: Finagle v7 result [D43]; request v7 [D44].*

**Figure 12a – Finagle table, base case.** Rows marked * come from Finagle's notebook replay.

| Row (US$M unless stated) | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E | FY2032E | FY2033E | FY2034E | FY2035E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 16.1 | 24.9 | 110 | 1,364 | 4,770 | 8,702 | 3,570 | 2,073 | 2,075 | 2,076 | 2,098 |
| EBITDA | -153 | -161 | -237 | 723 | 3,503 | 6,790 | 2,544 | 1,390 | 1,386 | 1,387 | 1,404 |
| SBC* | 17.7 | 17.7 | 17.7 | 68.2 | 238 | 435 | 179 | 104 | 104 | 104 | 106 |
| D&A (derived)* | 0.2 | -0.2 | -4.6 | -69.2 | -245 | -447 | -183 | -106 | -106 | -106 | -107 |
| Capex | 0.4 | 3.5 | 3.5 | 20.5 | 71.5 | 131 | 53.6 | 31.1 | 31.1 | 31.1 | 31.9 |
| Pre-tax income* | -233 | -183 | -255 | 719 | 3,437 | 6,452 | 1,870 | 829 | 872 | 924 | 995 |

*Source: Finagle v7 result [D43].*

**Figure 12b – Finagle table, base case (continued)**

| Row (US$M unless stated) | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E | FY2032E | FY2033E | FY2034E | FY2035E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NOL balance* | 539 | 723 | 978 | 258 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| NOL used* | 0.0 | -183 | -255 | 719 | 258 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cash taxes* | 5.6 | -0.0 | 0.0 | 186 | 887 | 1,665 | 482 | 214 | 225 | 238 | 257 |
| Debt | 49.7 | 49.7 | 49.7 | 723 | 3,503 | 6,790 | 5,640 | 5,162 | 4,649 | 4,093 | 3,479 |
| Cash | 480 | 293 | 29.9 | 1,333 | 6,414 | 13,911 | 13,911 | 13,911 | 13,908 | 13,900 | 13,886 |
| FCFE | -239 | -187 | -263 | 1,303 | 5,081 | 7,497 | -0.0 | -0.0 | -2.8 | -7.6 | -14.1 |
| Value per share (US$)* | $155.69 | $167.64 | $188.58 | $191.73 | $146.98 | $66.70 | $73.69 | $81.42 | $90.00 | $99.54 | $110.16 |

*Source: Finagle v7 result [D43].*

**Figure 13a – Key rows, bull**

| Row (US$M unless stated) | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E | FY2032E | FY2033E | FY2034E | FY2035E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 16.1 | 24.9 | 174 | 2,472 | 8,084 | 13,008 | 15,489 | 7,041 | 6,660 | 6,661 | 6,728 |
| EBITDA | -153 | -161 | -187 | 1,645 | 6,254 | 10,473 | 12,720 | 5,698 | 5,376 | 5,377 | 5,435 |
| D&A (derived)* | 0.2 | -0.4 | -10.3 | -163 | -536 | -863 | -1,027 | -466 | -441 | -441 | -446 |
| Capex | 0.4 | 3.5 | 3.5 | 37.1 | 121 | 195 | 232 | 106 | 99.9 | 99.9 | 102 |
| NOL balance* | 539 | 722 | 922 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cash taxes* | 5.6 | -0.0 | 0.0 | 433 | 1,605 | 2,595 | 3,077 | 1,172 | 1,159 | 1,231 | 1,290 |
| Debt | 49.7 | 49.7 | 49.7 | 1,645 | 6,254 | 10,473 | 12,720 | 9,923 | 7,131 | 5,377 | 5,435 |
| Cash | 430 | 243 | 29.7 | 2,909 | 11,476 | 22,102 | 31,938 | 31,938 | 31,938 | 33,184 | 36,405 |
| FCFE | -239 | -187 | -213 | 2,879 | 8,567 | 10,626 | 9,836 | 0.0 | 0.0 | 1,246 | 3,221 |

*Source: Finagle v7 result [D43].*

**Figure 13b – Key rows, bear**

| Row (US$M unless stated) | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E | FY2031E | FY2032E | FY2033E | FY2034E | FY2035E |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue | 16.1 | 24.9 | 30.0 | 35.0 | 40.0 | 44.0 | 47.5 | 50.0 | 52.2 | 53.8 | 55.2 |
| EBITDA | -153 | -161 | -142 | -117 | -102 | -98.7 | -95.4 | -93.0 | -90.9 | -89.4 | -88.2 |
| D&A (derived)* | 0.2 | 4.0 | 6.3 | 8.4 | 10.6 | 12.3 | 13.8 | 14.9 | 15.9 | 16.6 | 17.2 |
| Capex | 0.4 | 3.5 | 3.5 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 | 5.0 |
| NOL balance* | 539 | 727 | 898 | 1,046 | 1,181 | 1,315 | 1,447 | 1,577 | 1,707 | 1,836 | 1,964 |
| Cash taxes* | 5.6 | -0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Debt | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 | 49.7 |
| Cash | 1,430 | 1,243 | 1,075 | 930 | 800 | 674 | 551 | 430 | 312 | 195 | 78.9 |
| FCFE | -239 | -187 | -168 | -145 | -130 | -126 | -123 | -121 | -119 | -117 | -116 |

*Source: Finagle v7 result [D43].*

**Not yet decided by the user** (each changes the value):

- **Terminal ROIC / D&A policy.** The default ROIC of 15.00% gives negative D&A in base and bull. This is why those two scenarios are not a valuation.
- **Debt rule after the backlog clears.** Base debt runs at 2.22x–3.71x EBITDA in FY2031E–FY2035E, not 1x.
- **SBC at 5% of sales and the capex rule.** Both are our assumptions [S], and FY2034E–FY2035E are slightly off (see above).
- **Raise sizes.** Our assumptions [S]: base 400, bull 350, bear 1,350, all at the market price with no fees. The bear raise adds 53.4M shares to 62.5M.
- **Cash build-up with no payout.** Base 13,886, bull 36,405 by FY2035E.
- **gt 2% vs the forecaster's gsnext.**

**Commit and hashes.** Finagle commit `377f177b4013e713fe7c4603962e5f883a67e298`, run 2026-10-30T12:39:54.193566-04:00. Hash check: all sidecar hashes match (file bytes, whole request, base/bull/bear blocks, prompt_inputs, rev3 forecast.json bytes) [D43].


## Appendix A – Bull and Bear Cases

**Bull.** Year one is 1.5× the base path: 15, 45, 90 and 135 patients a quarter, 285 in total (our assumption) [S9]. Year two bridges to 30 centers at 1.875 procedures a week (731 a quarter) by Q2 2029 [S11]. After that, bull adds 5 centers a quarter, up to 100, with throughput rising to 2.0 [S7]. Refill is 2,872 a year [C3]. The UK launches from Q3 2028 at $1.5M [S13][G11]. Cumulative US treatments pass 6,000 by Q2 2030, and the backlog clears in Q4 2031.

**Figure A1 – Bull, FY2024A–FY2031E**

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|---|---|---|
| US treatment centers at year end (count) | – | – | 0 [C120] | 15 [C121] | 22 [C122] | 40 [C123] | 60 [C124] | 80 [C125] |
| US treatment capacity (patients/yr) | – | – | 0 [C128] | 60 [C129] | 942 [C130] | 3,263 [C131] | 5,460 [C132] | 7,540 [C133] |
| US refill demand (patients/yr) | – | – | 0 [C136] | 1,436 [C137] | 2,872 [C138] | 2,872 [C139] | 2,872 [C140] | 2,872 [C141] |
| US eligible backlog at year end (patients) | – | – | 6,000 [C144] | 7,028 [C145] | 8,150 [C146] | 6,979 [C147] | 3,861 [C148] | 0 [C149] |
| **US patients treated (patients/yr)** | – | – | 0 [C152] | 60 [C153] | 942 [C154] | 3,263 [C155] | 5,460 [C156] | 6,607 [C157] |
| US cumulative treated (patients) | – | – | 0 [C160] | 60 [C161] | 1,002 [C162] | 4,266 [C163] | 9,726 [C164] | 16,333 [C165] |
| UK capacity (patients/yr) | – | – | 0 [C168] | 0 [C169] | 117 [C170] | 663 [C171] | 780 [C172] | 780 [C173] |
| **UK patients treated (patients/yr)** | – | – | 0 [C176] | 0 [C177] | 117 [C178] | 663 [C179] | 780 [C180] | 780 [C181] |
| UK eligible backlog at year end (patients) | – | – | 0 [C184] | 0 [C185] | 2,155 [C186] | 1,574 [C187] | 943 [C188] | 372 [C189] |
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C6] | 30.0 [S18] | 35.0 [S19] | 40.0 [S20] | 44.0 [S21] | 47.5 [S22] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A24] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S26] | 144 [C90] | 2,261 [C91] | 7,049 [C92] | 11,794 [C93] | 14,271 [C94] |
| AMT-130 revenue, UK (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S39] | 0.0 [S39] | 176 [C96] | 994 [C97] | 1,170 [C98] | 1,170 [C98] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C6] | 174 [C102] | 2,472 [C103] | 8,084 [C104] | 13,008 [C105] | 15,489 [C106] |
| Gross margin (%) | – | 89.5% [C30] | 93.9% [C109] | 88.6% [C110] | 88.1% [C111] | 87.8% [C112] | 89.2% [C113] | 90.4% [C114] |
| **EBITDA (US$M)** | -149 [C25] | -153 [C26] | -161 [C29] | -187 [S40] | 1,645 [S41] | 6,254 [S42] | 10,473 [S43] | 12,720 [S44] |
| EBITDA margin (%, derived) [C401] | -550.9% | -949.9% | -645.9% | -107.7% | 66.6% | 77.4% | 80.5% | 82.1% |

**Figure A2 – Bull, FY2032E–FY2033E**

| Row (units) | FY32E | FY33E |
|---|---|---|
| US treatment centers at year end (count) | 30 [C126] | 30 [C127] |
| US treatment capacity (patients/yr) | 3,120 [C134] | 3,120 [C135] |
| US refill demand (patients/yr) | 2,872 [C142] | 2,872 [C143] |
| US eligible backlog at year end (patients) | 0 [C150] | 0 [C151] |
| **US patients treated (patients/yr)** | 2,872 [C158] | 2,872 [C159] |
| US cumulative treated (patients) | 19,205 [C166] | 22,077 [C167] |
| UK capacity (patients/yr) | 524 [C174] | 269 [C175] |
| **UK patients treated (patients/yr)** | 524 [C182] | 269 [C183] |
| UK eligible backlog at year end (patients) | 0 [C190] | 0 [C191] |
| License revenue, Hemgenix royalties (US$M) | 50.0 [S23] | 52.2 [S24] |
| Collaboration revenue (US$M) | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 6,204 [C95] | 6,204 [C95] |
| AMT-130 revenue, UK (US$M) | 787 [C99] | 404 [C100] |
| **Total revenue (US$M)** | 7,041 [C107] | 6,660 [C108] |
| Gross margin (%) | 91.3% [C115] | 91.5% [C116] |
| **EBITDA (US$M)** | 5,698 [S45] | 5,376 [S46] |
| EBITDA margin (%, derived) [C401] | 80.9% | 80.7% |

*me 80.7% [C119], mc 86.1% [S47], gsnext 0.02% [S48].*

**Bear.** AMT-130 is not approved. Royalties continue, and opex is cut to $140M.

**Figure A3 – Bear, FY2024A–FY2031E**

| Row (units) | FY24A | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E |
|---|---|---|---|---|---|---|---|---|
| License revenue, Hemgenix royalties (US$M) | 10.1 [A1] | 15.9 [A2] | 24.9 [C6] | 30.0 [S18] | 35.0 [S19] | 40.0 [S20] | 44.0 [S21] | 47.5 [S22] |
| Collaboration revenue (US$M) | 10.9 [A3] | 0.2 [A4] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 6.1 [A5] | 0.0 [A24] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] | 0.0 [S49] |
| AMT-130 revenue, UK (US$M) | 0.0 [A25] | 0.0 [A25] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] | 0.0 [S50] |
| **Total revenue (US$M)** | 27.1 [A6] | 16.1 [A7] | 24.9 [C6] | 30.0 [C192] | 35.0 [C193] | 40.0 [C194] | 44.0 [C195] | 47.5 [C196] |
| Gross margin (%) | – | 89.5% [C30] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] | 93.9% [C199] |
| **EBITDA (US$M)** | -149 [C25] | -153 [C26] | -161 [C29] | -142 [S52] | -117 [S53] | -102 [S54] | -98.7 [S55] | -95.4 [S56] |
| EBITDA margin (%, derived) [C401] | -550.9% | -949.9% | -645.9% | -472.7% | -334.6% | -256.1% | -224.2% | -200.8% |

**Figure A4 – Bear, FY2032E–FY2033E**

| Row (units) | FY32E | FY33E |
|---|---|---|
| License revenue, Hemgenix royalties (US$M) | 50.0 [S23] | 52.2 [S24] |
| Collaboration revenue (US$M) | 0.0 [S25] | 0.0 [S25] |
| Contract manufacturing revenue (US$M) | 0.0 [G14] | 0.0 [G14] |
| AMT-130 revenue, US (US$M) | 0.0 [S49] | 0.0 [S49] |
| AMT-130 revenue, UK (US$M) | 0.0 [S50] | 0.0 [S50] |
| **Total revenue (US$M)** | 50.0 [C197] | 52.2 [C198] |
| Gross margin (%) | 93.9% [C199] | 93.9% [C199] |
| **EBITDA (US$M)** | -93.0 [S57] | -90.9 [S58] |
| EBITDA margin (%, derived) [C401] | -186.1% | -174.0% |

*me -174.0% [C202], mc 93.9% [S59], gsnext 3.00% [S60].*

## Appendix B – Numbered sources

**Documents**

- **D1** uniQure Form 10-K FY2025 (filed 2026-03-02). https://www.sec.gov/Archives/edgar/data/1590560/000110465926021898/qure-20251231x10k.htm. HTML; no page numbers. 
- **D2** uniQure Form 10-Q Q2 2026 (filed 2026-07-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926087815/qure-20260630x10q.htm. HTML; no page numbers. 
- **D3** uniQure Q2 2026 results press release, 8-K Ex.99.1 (2026-07-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926087808/qure-20260729xex99d1.htm. HTML; no page numbers. 
- **D4** uniQure BLA submission press release, 8-K Ex.99.1 (2026-09-02). https://www.sec.gov/Archives/edgar/data/1590560/000110465926104463/qure-20260902xex99d1.htm. HTML; no page numbers. 
- **D5** uniQure four-year AMT-130 data press release, 8-K Ex.99.2 (2026-09-29). https://www.sec.gov/Archives/edgar/data/1590560/000110465926111654/tm2626514d1_ex99-2.htm. HTML; no page numbers. 
- **D6** Yahoo Finance / yfinance analyst revenue estimates for QURE, pulled 2026-10-29 (shown in EUR). https://finance.yahoo.com/quote/QURE/analysis/. HTML; no page numbers. 
- **D7** GEN StockWatch, Leerink net-price estimates and O'Keefe pricing/TAM comments (2025). https://www.genengnews.com/topics/translational-medicine/stockwatch-uniqure-shares-reach-five-year-high-on-game-changing-huntingtons-data/. HTML; no page numbers. 
- **D8** Clinaptis research, AMT-130 capacity ramp and net-price model. https://www.clinaptisresearch.com/research/amt-130-huntingtons-uniqure-bla. HTML; no page numbers. 
- **D9** BioSpace, uniQure files for FDA, UK approval (2026-09). https://www.biospace.com/fda/uniqure-files-for-fda-uk-approval-of-first-gene-therapy-for-huntingtons-disease. HTML; no page numbers. 
- **D10** uniQure, Pivotal Phase I/II AMT-130 Huntington's Disease Update, investor presentation, slides 25-26 (2025-09-24). https://cdn.craft.cloud/fe68e1a2-b284-4f69-ba29-921f065edf17/assets/uploads/AMT-130-Pivotal-Sept-2025_final_09.24.25.pdf. HTML; no page numbers. 
- **D11** Medina et al., Prevalence and Incidence of Huntington's Disease: An Updated Systematic Review and Meta-Analysis, Movement Disorders 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC10086981/. HTML; no page numbers. 
- **D12** uniQure Q2 2026 earnings call transcript (Motley Fool, 2026-08-07). https://www.fool.com/earnings/call-transcripts/2026/08/07/uniqure-qure-q2-2026-earnings-call-transcript/. HTML; no page numbers. 
- **D13** uniQure Q1 2026 earnings call transcript (StockAnalysis). https://stockanalysis.com/stocks/qure/transcripts/578165-q1-2026/. HTML; no page numbers. 
- **D14** uniQure press release, sale of Lexington commercial manufacturing facility to Genezen (2024-07-01). https://uniqure.gcs-web.com/news-releases/news-release-details/uniqure-announces-sale-commercial-manufacturing-facility-genezen. HTML; no page numbers. 
- **D15** US Census Bureau population clock (US resident population ~340 million). https://www.census.gov/popclock/. HTML; no page numbers. 
- **D16** Prompt: David May, direct message 2026-10-30. n/a: user prompt (David May, direct message, 2026-10-30). HTML; no page numbers. 
- **D17** Prompt: David May, direct messages 2026-10-30 (capacity-dependent short term; refill = incidence less a few). n/a: user prompt (David May, direct messages, 2026-10-30). HTML; no page numbers. 
- **D18** EHDN Platform Meeting report, uniQure AMT-130 topline results (2025-12-04). https://ehdn.org/wp-content/uploads/2025/12/EHDN-Platform-Meeting-uniQure-Topline-Results-Report_Final_2-04-Dec-2025.pdf. HTML; no page numbers. 
- **D19** Sarepta ELEVIDYS label update call transcript, 2024-06-21 (StockAnalysis/Quartr). https://stockanalysis.com/stocks/srpt/transcripts/205218-status-update/. HTML; no page numbers. 
- **D20** Sarepta Q4 and FY2024 results, 8-K Ex.99.1 (2025-02-26) and preliminary release (2025-01-13). https://www.sec.gov/Archives/edgar/data/873303/000095017025027717/srpt-ex99_1.htm. HTML; no page numbers. 
- **D21** Sarepta 8-K 2023-06-22: ELEVIDYS US wholesale acquisition cost. https://www.sec.gov/Archives/edgar/data/873303/000095017023029438/srpt-20230622.htm. HTML; no page numbers. 
- **D22** Investing.com, Goldman Sachs note summary on uniQure (2025-09). https://ph.investing.com/news/analyst-ratings/uniqure-stock-rises-after-positive-huntingtons-disease-gene-therapy-data-93CH-2010942. HTML; no page numbers. 
- **D23** Reuters, FDA approves Sarepta gene therapy (2023-06-22): Hemgenix list price. https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-approves-sareptas-gene-therapy-rare-muscular-dystrophy-some-kids-2023-06-22/. HTML; no page numbers. 
- **D24** ClearPoint Neuro Q2 2026 earnings call transcript (2026-08-10, Motley Fool): CLEAR site-readiness program. https://www.fool.com/earnings/call-transcripts/2026/08/10/clearpoint-neuro-clpt-q2-2026-earnings-call-transcript/. HTML; no page numbers. 
- **D25** ClearPoint Neuro Q3 2025 results press release, 8-K Ex.99.1 (2025-11-06). https://www.sec.gov/Archives/edgar/data/1285550/000119312525270019/clpt-ex99_1.htm. HTML; no page numbers. 
- **D26** ClearPoint Neuro Q3 2026 earnings call transcript (2026-10-28, StockAnalysis). https://stockanalysis.com/stocks/clpt/transcripts/722761-q3-2026/. HTML; no page numbers. 
- **D27** HDSA press release 2025-04-02: Centers of Excellence network expands to 69 sites. https://hdsa.org/news/huntingtons-disease-society-of-america-awards-more-than-1-8-million-to-expand-hdsa-centers-of-excellence-network-to-sixty-nine-sites/. HTML; no page numbers. 
- **D28** IntuitionLabs, Most Expensive Drugs in the US: 2025 price list (secondary source for gene-therapy list prices). https://intuitionlabs.ai/articles/most-expensive-drugs-usa-2025. HTML; no page numbers. 
- **D30** David May direct message 2026-10-30 (t62u: centers do not limit capacity in year one; use the Kapusta bot's ~190 year-1 path). n/a: user prompt in chat. HTML; no page numbers. 
- **D29** David May direct messages 2026-10-30 (rev2b: t57u ClearPoint centers; 'Adjust as necessary and then send for finagle valuation'). n/a: user prompt in chat. HTML; no page numbers. 

**Facts cited**

- **A1** License revenues $ 15,934 $ 10,133 $ 2,758
- **A2** License revenues $ 15,934 $ 10,133 $ 2,758
- **A3** Collaboration revenues 164 10,872 2,250
- **A4** Collaboration revenues 164 10,872 2,250
- **A5** Contract manufacturing revenues — 6,114 10,835
- **A6** Total revenues $ 16,098 $ 27,119 $ 15,843
- **A7** Total revenues $ 16,098 $ 27,119 $ 15,843
- **A12** HDSA recognized 60 HDSA Centers of Excellence and nine Partner Sites, ensuring expert HD in 37 states across the nation and Washington, DC.
- **A13** Lenmeldy holds the highest list price of any U.S. drug at $4.25 million per dose, followed by Kebilidi at $3.95 million.
- **A14** The Purchaser will receive 1.85 times the upfront payment (or $ 693.8 million) until June 30, 2032 (“First Hard Cap Date”) if such thresholds are met or, if such cap is not met by June 30, 2032, up to 2.25 times of the upfront payment through December 31, 2038 ... Liability from royalty financing agreement 473,199
- **A15** Temporal Lobe Epilepsy (AMT-260) Regenxbio In June 2020, uniQure France entered into an agreement ... with Regenxbio for an exclusive (in the field of using AAV9 to expression of the GRIK2 gene in humans
- **A21** a gene therapy for bleeding disorder hemophilia from Australian drugmaker CSL Ltd ... carries a list price of $3.5 million.
- **A22** R&D expenses for the three months ended June 30, 2026 were $34.0 million ... Selling, general and administrative expenses for the three months ended June 30, 2026 were $17.4 million ... Net cash used in operating activities was $66.8 million for the six months ended June 30, 2026 ... cash and cash equivalents and investment securities of $810.3 million ... sufficient to fund our projected operating expenses into 2030
- **A24** Contract manufacturing revenues — 6,114
- **A25** investigational gene therapy
- **C2** base US refill/yr = incidence 0.48/100k x 340M = 1632 new cases x haircut = 1124 patients/yr
- **C3** bull US refill/yr = incidence 1.04/100k x 340M = 3536 new cases x haircut = 2872 patients/yr
- **C6** FY26 consensus EUR x fx; all royalty/license, no AMT-130 sales before approval
- **C9** base AMT-130 US (US$M) = 40 patients treated (min of capacity 40/yr and backlog+refill) x $2.00M net, recognised at treatment
- **C10** base AMT-130 US (US$M) = 665 patients treated (min of capacity 665/yr and backlog+refill) x $2.00M net, recognised at treatment
- **C11** base AMT-130 US (US$M) = 2365 patients treated (min of capacity 2365/yr and backlog+refill) x $2.00M net, recognised at treatment
- **C12** base AMT-130 US (US$M) = 4329 patients treated (min of capacity 4329/yr and backlog+refill) x $2.00M net, recognised at treatment
- **C13** base AMT-130 US (US$M) = 1957 patients treated (min of capacity 3666/yr and backlog+refill) x $1.80M net, recognised at treatment
- **C14** base AMT-130 US (US$M) = 1124 patients treated (min of capacity 3120/yr and backlog+refill) x $1.80M net, recognised at treatment
- **C18** Sum of base lines (US$M)
- **C19** Sum of base lines (US$M)
- **C20** Sum of base lines (US$M)
- **C21** Sum of base lines (US$M)
- **C22** Sum of base lines (US$M)
- **C23** Sum of base lines (US$M)
- **C24** Sum of base lines (US$M)
- **C25** EBITDA = loss from operations -184,294 + D&A 12,641 + SBC 22,258 (2024)
- **C26** EBITDA = loss from operations -185,349 + D&A 14,759 + SBC 17,679 (2025)
- **C29** H1A EBITDA + H2 revenue x license GM - 2 x Q2 cash opex net of other items (47.771) [S run rate]
- **C30** (revenue - cost of license revenues 1,686)/revenue 2025
- **C31** Revenue-weighted gross margin base (license GM; AMT-130 1 - COGS/revenue)
- **C32** Revenue-weighted gross margin base (license GM; AMT-130 1 - COGS/revenue)
- **C33** Revenue-weighted gross margin base (license GM; AMT-130 1 - COGS/revenue)
- **C34** Revenue-weighted gross margin base (license GM; AMT-130 1 - COGS/revenue)
- **C35** Revenue-weighted gross margin base (license GM; AMT-130 1 - COGS/revenue)
- **C36** Revenue-weighted gross margin base (license GM; AMT-130 1 - COGS/revenue)
- **C37** Revenue-weighted gross margin base (license GM; AMT-130 1 - COGS/revenue)
- **C38** Revenue-weighted gross margin base (license GM; AMT-130 1 - COGS/revenue)
- **C41** FY38E EBITDA / FY38E revenue (steady state: backlog cleared, treated = refill), base
- **C42** US treatment centers active at year end (count), base FY26E
- **C43** US treatment centers active at year end (count), base FY27E
- **C44** US treatment centers active at year end (count), base FY28E
- **C45** US treatment centers active at year end (count), base FY29E
- **C46** US treatment centers active at year end (count), base FY30E
- **C47** US treatment centers active at year end (count), base FY31E
- **C48** US treatment centers active at year end (count), base FY32E
- **C49** US treatment centers active at year end (count), base FY33E
- **C50** US treatment capacity = centers x procedures/center/month x months (patients/yr), base FY26E
- **C51** US treatment capacity = centers x procedures/center/month x months (patients/yr), base FY27E
- **C52** US treatment capacity = centers x procedures/center/month x months (patients/yr), base FY28E
- **C53** US treatment capacity = centers x procedures/center/month x months (patients/yr), base FY29E
- **C54** US treatment capacity = centers x procedures/center/month x months (patients/yr), base FY30E
- **C55** US treatment capacity = centers x procedures/center/month x months (patients/yr), base FY31E
- **C56** US treatment capacity = centers x procedures/center/month x months (patients/yr), base FY32E
- **C57** US treatment capacity = centers x procedures/center/month x months (patients/yr), base FY33E
- **C58** US refill demand = incidence x population x haircut (patients/yr), base FY26E
- **C59** US refill demand = incidence x population x haircut (patients/yr), base FY27E
- **C60** US refill demand = incidence x population x haircut (patients/yr), base FY28E
- **C61** US refill demand = incidence x population x haircut (patients/yr), base FY29E
- **C62** US refill demand = incidence x population x haircut (patients/yr), base FY30E
- **C63** US refill demand = incidence x population x haircut (patients/yr), base FY31E
- **C64** US refill demand = incidence x population x haircut (patients/yr), base FY32E
- **C65** US refill demand = incidence x population x haircut (patients/yr), base FY33E
- **C66** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), base FY26E
- **C67** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), base FY27E
- **C68** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), base FY28E
- **C69** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), base FY29E
- **C70** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), base FY30E
- **C71** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), base FY31E
- **C72** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), base FY32E
- **C73** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), base FY33E
- **C74** US patients treated = min(capacity, backlog + refill) (patients/yr), base FY26E
- **C75** US patients treated = min(capacity, backlog + refill) (patients/yr), base FY27E
- **C76** US patients treated = min(capacity, backlog + refill) (patients/yr), base FY28E
- **C77** US patients treated = min(capacity, backlog + refill) (patients/yr), base FY29E
- **C78** US patients treated = min(capacity, backlog + refill) (patients/yr), base FY30E
- **C79** US patients treated = min(capacity, backlog + refill) (patients/yr), base FY31E
- **C80** US patients treated = min(capacity, backlog + refill) (patients/yr), base FY32E
- **C81** US patients treated = min(capacity, backlog + refill) (patients/yr), base FY33E
- **C82** US cumulative patients treated (patients), base FY26E
- **C83** US cumulative patients treated (patients), base FY27E
- **C84** US cumulative patients treated (patients), base FY28E
- **C85** US cumulative patients treated (patients), base FY29E
- **C86** US cumulative patients treated (patients), base FY30E
- **C87** US cumulative patients treated (patients), base FY31E
- **C88** US cumulative patients treated (patients), base FY32E
- **C89** US cumulative patients treated (patients), base FY33E
- **C90** bull AMT-130 US (US$M) = 60 patients treated (min of capacity 60/yr and backlog+refill) x $2.40M net, recognised at treatment
- **C91** bull AMT-130 US (US$M) = 942 patients treated (min of capacity 942/yr and backlog+refill) x $2.40M net, recognised at treatment
- **C92** bull AMT-130 US (US$M) = 3263 patients treated (min of capacity 3263/yr and backlog+refill) x $2.16M net, recognised at treatment
- **C93** bull AMT-130 US (US$M) = 5460 patients treated (min of capacity 5460/yr and backlog+refill) x $2.16M net, recognised at treatment
- **C94** bull AMT-130 US (US$M) = 6607 patients treated (min of capacity 7540/yr and backlog+refill) x $2.16M net, recognised at treatment
- **C95** bull AMT-130 US (US$M) = 2872 patients treated (min of capacity 3120/yr and backlog+refill) x $2.16M net, recognised at treatment
- **C96** bull AMT-130 UK (US$M) = 117 UK patients treated x $1.5M net
- **C97** bull AMT-130 UK (US$M) = 663 UK patients treated x $1.5M net
- **C98** bull AMT-130 UK (US$M) = 780 UK patients treated x $1.5M net
- **C99** bull AMT-130 UK (US$M) = 525 UK patients treated x $1.5M net
- **C100** bull AMT-130 UK (US$M) = 269 UK patients treated x $1.5M net
- **C102** Sum of bull lines (US$M)
- **C103** Sum of bull lines (US$M)
- **C104** Sum of bull lines (US$M)
- **C105** Sum of bull lines (US$M)
- **C106** Sum of bull lines (US$M)
- **C107** Sum of bull lines (US$M)
- **C108** Sum of bull lines (US$M)
- **C109** Revenue-weighted gross margin bull (license GM; AMT-130 1 - COGS/revenue)
- **C110** Revenue-weighted gross margin bull (license GM; AMT-130 1 - COGS/revenue)
- **C111** Revenue-weighted gross margin bull (license GM; AMT-130 1 - COGS/revenue)
- **C112** Revenue-weighted gross margin bull (license GM; AMT-130 1 - COGS/revenue)
- **C113** Revenue-weighted gross margin bull (license GM; AMT-130 1 - COGS/revenue)
- **C114** Revenue-weighted gross margin bull (license GM; AMT-130 1 - COGS/revenue)
- **C115** Revenue-weighted gross margin bull (license GM; AMT-130 1 - COGS/revenue)
- **C116** Revenue-weighted gross margin bull (license GM; AMT-130 1 - COGS/revenue)
- **C119** FY38E EBITDA / FY38E revenue (steady state: backlog cleared, treated = refill), bull
- **C120** US treatment centers active at year end (count), bull FY26E
- **C121** US treatment centers active at year end (count), bull FY27E
- **C122** US treatment centers active at year end (count), bull FY28E
- **C123** US treatment centers active at year end (count), bull FY29E
- **C124** US treatment centers active at year end (count), bull FY30E
- **C125** US treatment centers active at year end (count), bull FY31E
- **C126** US treatment centers active at year end (count), bull FY32E
- **C127** US treatment centers active at year end (count), bull FY33E
- **C128** US treatment capacity = centers x procedures/center/month x months (patients/yr), bull FY26E
- **C129** US treatment capacity = centers x procedures/center/month x months (patients/yr), bull FY27E
- **C130** US treatment capacity = centers x procedures/center/month x months (patients/yr), bull FY28E
- **C131** US treatment capacity = centers x procedures/center/month x months (patients/yr), bull FY29E
- **C132** US treatment capacity = centers x procedures/center/month x months (patients/yr), bull FY30E
- **C133** US treatment capacity = centers x procedures/center/month x months (patients/yr), bull FY31E
- **C134** US treatment capacity = centers x procedures/center/month x months (patients/yr), bull FY32E
- **C135** US treatment capacity = centers x procedures/center/month x months (patients/yr), bull FY33E
- **C136** US refill demand = incidence x population x haircut (patients/yr), bull FY26E
- **C137** US refill demand = incidence x population x haircut (patients/yr), bull FY27E
- **C138** US refill demand = incidence x population x haircut (patients/yr), bull FY28E
- **C139** US refill demand = incidence x population x haircut (patients/yr), bull FY29E
- **C140** US refill demand = incidence x population x haircut (patients/yr), bull FY30E
- **C141** US refill demand = incidence x population x haircut (patients/yr), bull FY31E
- **C142** US refill demand = incidence x population x haircut (patients/yr), bull FY32E
- **C143** US refill demand = incidence x population x haircut (patients/yr), bull FY33E
- **C144** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), bull FY26E
- **C145** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), bull FY27E
- **C146** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), bull FY28E
- **C147** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), bull FY29E
- **C148** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), bull FY30E
- **C149** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), bull FY31E
- **C150** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), bull FY32E
- **C151** US untreated eligible backlog at year end = start 6,000 + refill - treated, less 10%/yr attrition (patients), bull FY33E
- **C152** US patients treated = min(capacity, backlog + refill) (patients/yr), bull FY26E
- **C153** US patients treated = min(capacity, backlog + refill) (patients/yr), bull FY27E
- **C154** US patients treated = min(capacity, backlog + refill) (patients/yr), bull FY28E
- **C155** US patients treated = min(capacity, backlog + refill) (patients/yr), bull FY29E
- **C156** US patients treated = min(capacity, backlog + refill) (patients/yr), bull FY30E
- **C157** US patients treated = min(capacity, backlog + refill) (patients/yr), bull FY31E
- **C158** US patients treated = min(capacity, backlog + refill) (patients/yr), bull FY32E
- **C159** US patients treated = min(capacity, backlog + refill) (patients/yr), bull FY33E
- **C160** US cumulative patients treated (patients), bull FY26E
- **C161** US cumulative patients treated (patients), bull FY27E
- **C162** US cumulative patients treated (patients), bull FY28E
- **C163** US cumulative patients treated (patients), bull FY29E
- **C164** US cumulative patients treated (patients), bull FY30E
- **C165** US cumulative patients treated (patients), bull FY31E
- **C166** US cumulative patients treated (patients), bull FY32E
- **C167** US cumulative patients treated (patients), bull FY33E
- **C168** UK capacity (patients/yr), bull FY26E
- **C169** UK capacity (patients/yr), bull FY27E
- **C170** UK capacity (patients/yr), bull FY28E
- **C171** UK capacity (patients/yr), bull FY29E
- **C172** UK capacity (patients/yr), bull FY30E
- **C173** UK capacity (patients/yr), bull FY31E
- **C174** UK capacity (patients/yr), bull FY32E
- **C175** UK capacity (patients/yr), bull FY33E
- **C176** UK patients treated (patients/yr), bull FY26E
- **C177** UK patients treated (patients/yr), bull FY27E
- **C178** UK patients treated (patients/yr), bull FY28E
- **C179** UK patients treated (patients/yr), bull FY29E
- **C180** UK patients treated (patients/yr), bull FY30E
- **C181** UK patients treated (patients/yr), bull FY31E
- **C182** UK patients treated (patients/yr), bull FY32E
- **C183** UK patients treated (patients/yr), bull FY33E
- **C184** UK eligible backlog at year end (patients), bull FY26E
- **C185** UK eligible backlog at year end (patients), bull FY27E
- **C186** UK eligible backlog at year end (patients), bull FY28E
- **C187** UK eligible backlog at year end (patients), bull FY29E
- **C188** UK eligible backlog at year end (patients), bull FY30E
- **C189** UK eligible backlog at year end (patients), bull FY31E
- **C190** UK eligible backlog at year end (patients), bull FY32E
- **C191** UK eligible backlog at year end (patients), bull FY33E
- **C192** Sum of bear lines (US$M)
- **C193** Sum of bear lines (US$M)
- **C194** Sum of bear lines (US$M)
- **C195** Sum of bear lines (US$M)
- **C196** Sum of bear lines (US$M)
- **C197** Sum of bear lines (US$M)
- **C198** Sum of bear lines (US$M)
- **C199** Revenue-weighted gross margin bear (license GM; AMT-130 1 - COGS/revenue)
- **C202** FY38E EBITDA / FY38E revenue (steady state: backlog cleared, treated = refill), bear
- **C205** FY27 consensus / base line build: NOT applied (P5 capacity instruction overrides consensus); far from 1, flagged
- **C401** EBITDA margin = EBITDA / revenue, derived from the forecast file
- **C503** v7 minus v6 value per share, from D43 and D40
- **C504** new shares = raise / fetched price US$25.30, from D43
- **C505** bear value per share = (equity + year-0 cash) / shares, recomputed from D43
- **D40** Finagle v6 result: /workspace/out/QURE_run/valuation_result_v6.json, case_{base,bull,bear}_v6.json, QURE_{base,bull,bear}_v6.xlsx (Finagle commit 377f177, run 2026-10-30T12:30:34.449313-04:00)
- **D41** Valuation request v6: /workspace/out/QURE_run/valuation_request_v6.json (sha256 4a61b649...bddab)
- **D43** Finagle v7 result: /workspace/out/QURE_run/valuation_result_v7.json, case_{base,bull,bear}_v7.json, QURE_{base,bull,bear}_v7.xlsx (Finagle commit 377f177, run 2026-10-30T12:39:54.193566-04:00)
- **D44** Valuation request v7: /workspace/out/QURE_run/valuation_request_v7.json (file sha256 b5cd6e09...f0ef; canonical 757d9d45...5670)
- **E6** Goldman Sachs modeling potential peak global sales of $2.5 billion with a 90% probability of success, assuming approximately 25% cumulative penetration into the estimated 20,000 diagnosed, symptomatic patients in the US.
- **G1** I think we already have 15 centers just in the first couple months that have filled out and sort of qualified by saying, yes, not only do we have the materials, the patient recruitment, the cooperation with pharmacy to thaw out the drugs, all those types of things, but they've also pretty much raised their hand and say, yes, we could be ready to do 1, if not 2 of these procedures a week. So, if we can get to 20 or 30 of these centers that are each willing to commit 1 to 2 cases a week, which is 50 to 100 cases a week, you can imagine getting to a ramped-up procedure type pretty quickly here.
- **G2** Our highest priority with the neurosurgical community is to work hand-in-hand with our biopharma partners and to identify the first 35-40 specialized treatment centers which can add 5,000 patients a year in capacity.
- **G3** the expectation would be a final formal decision sometime six to eight months after the acceptance of that BLA. Again, if everything went perfectly. That would put a potential approval for the very first neuro gene therapy to treat Huntington's disease sometime middle to second half of next year.
- **G4** Management and the FDA reached alignment on a randomized standard-of-care controlled design, substituting the previous sham procedure, with total functional capacity at 36 months as the primary endpoint ... the confirmatory study should be well underway and potentially fully enrolled at the time of accelerated approval.
- **G5** ~6,000 patients* Initial Treatable Patients at Launch ... ~20,000 patients Diagnosed HD ~40,000 patients Symptomatic HD ~100,000 patients Genetically Identifiable HD ... *Management Estimate. (slide 25)
- **G6** About 6,000 patients, representing the initially treatable ~30% of the total ~20,000 total diagnosed and symptomatic HD patients in the United States today. Approximately 40,000 U.S. patients are symptomatic for HD.
- **G9** There are a number of centers that are available to do this, and we are working with what we think is the right number in the initial term, and then we will continue to build from there. From a capacity point of view, it's very challenging to give you one number, and we're still working through that because it depends on the number of neurosurgeons at a particular hospital. It depends on the number of intraoperative OR suites and other competing priorities.
- **G11** There are between 7,000-8,000 patients living with HD in the U.K., with approximately 30,000 at risk.
- **G12** its Marketing Authorisation Application (MAA) for ifezuntirgene inilparvovec has been submitted to the United Kingdom's (U.K.) Medicines and Healthcare products Regulatory Agency (MHRA) ... The Company has requested priority review for the BLA. If granted, priority review would shorten the FDA review cycle to six months following the FDA's 60-day BLA filing review period.
- **G13** we rely on Genezen for the production of HEMGENIX and will have preferential access to the Lexington Facility for the production of materials related to AMT-130 and AMT-191 programs under separately negotiated development and supply arrangements.
- **G14** divestment of our commercial manufacturing activities in July 2024
- **P3** Yearly refill is the incidence rate and exclude a few due to eligibility, willingness and coverage.
- **P5** Your centers count at the end of 27 is wrong. There are currently around 30 centers that can do 1-2 procedures a week. This is available info from ClearPoint
- **P7** We can say that centers don’t limits capacity in year one and use your 190
- **P101** David May 2026-10-29: "take rd as 10%"
- **P102** David May 2026-10-29: "set the year 0 depreciation and amortization to 3% of revenue and rerun"
- **P103** David May 2026-10-29: "rerun and keep debt constant until the year when EBITDA is positive. Then target 1x EBITDA from that year onward."
- **P104** David May 2026-10-30 (t60u): "Stock comp is held constant until EBITDA is positive and then is a fixed % of sales. Check if Matt gives more color on capex, otherwise treat as resolved. Keep bear capex the same as base. Figure out the NOL's from Matt."
- **P105** David May 2026-10-30 (t64u): "Take depreciation as half of capex in year 0. Liability isn't debt. Yes to 1xebitda rule. Add shares and cash in year 0 so cash doesn't go negative anywhere.2% terminal growth. Dutch tax rate."
- **S1** Confirmatory-study R&D $70M/yr FY27E-FY31E on top of the Q2 2026 R&D run rate (midpoint of $60-80M; cost undisclosed) [S]
- **S5** 10%/yr of the untreated eligible backlog is lost (progression past early-manifest stage, death) [S]
- **S6** base capacity: rev3: engine starts after year one (Q3 2028) with 30 centers reached by Q2 2029; 1.00 procedure/center/week at Q3 2028 rising 0.125/qtr to 2.0; year one is the fixed ~190 path and year two a linear bridge (see bridge item) ; +3 centers/qtr while a backlog exists, to 70; Genezen vector supply assumed not binding through FY29E (no disclosed dose capacity); after the backlog clears the network falls to max(30, refill need) [S]
- **S7** bull capacity: rev3: engine starts after year one (Q3 2028) with 30 centers reached by Q2 2029; 1.50 procedure/center/week at Q3 2028 rising 0.125/qtr to 2.0; year one is the fixed ~190 path and year two a linear bridge (see bridge item) ; +5 centers/qtr while a backlog exists, to 100; Genezen vector supply assumed not binding through FY29E (no disclosed dose capacity); after the backlog clears the network falls to max(30, refill need) [S]
- **S8** base year-1 US patients treated per quarter Q3 2027-Q2 2028 = [10, 30, 60, 90] (190 in the first four quarters after the 2027-07-01 approval); centers not binding [P7]. Pointer: Matt Kapusta CEO-simulation bot (~10/30/60/90 = ~190), not a document
- **S9** bull year-1 US patients treated per quarter Q3 2027-Q2 2028 = [15, 45, 90, 135] (285 in the first four quarters after the 2027-07-01 approval); centers not binding [P7]. Pointer: Matt Kapusta CEO-simulation bot (~10/30/60/90 = ~190), not a document; bull = 1.5x base, the same uplift as rev2b's bull launch throughput (1.5 vs 1.0 procedures/center/week) [S]
- **S10** base year-2 bridge (Q3 2028-Q2 2029): capacity rises linearly from the year-1 exit run-rate 90 patients/qtr to 30 centers x 1.375 procedures/center/week x 13 weeks at Q2 2029; centers 15 -> 30 (ClearPoint Q2 2026 call: 15 qualified, 20-30 goal [G]; Kapusta pointer ~30 by end of year 2; David's 30 centers at 1-2/week [P5] reached at end of year 2, not at launch). From Q3 2029 rev2b logic: +3 centers/qtr while a backlog exists to 70, throughput to 2.0/week, then demand-limited [S]
- **S11** bull year-2 bridge (Q3 2028-Q2 2029): capacity rises linearly from the year-1 exit run-rate 135 patients/qtr to 30 centers x 1.875 procedures/center/week x 13 weeks at Q2 2029; centers 15 -> 30 (ClearPoint Q2 2026 call: 15 qualified, 20-30 goal [G]; Kapusta pointer ~30 by end of year 2; David's 30 centers at 1-2/week [P5] reached at end of year 2, not at launch). From Q3 2029 rev2b logic: +5 centers/qtr while a backlog exists to 100, throughput to 2.0/week, then demand-limited [S]
- **S13** Bull UK: MHRA approval and NHS access from Q3 2028; initial backlog 30% x 7,500 = 2250; refill 0.48/100k x 69M x bull haircut; centers [3, 6, 9, 12, 15]; 1 procedure/center/week (4.33/month); net price $1.5M [S]
- **S14** Base US net price $2.0M FY27E-FY30E, then -10%% to $1.8M from the year after annual US sales first pass $2B (payer budget pressure); Kebilidi $3.95M, Elevidys $3.2M, Hemgenix $3.5M list are gross [S]
- **S15** Bull US net price $2.4M, then -10%% to $2.16M from the year after annual US sales first pass $2B [S]
- **S16** base AMT-130 COGS (Genezen manufacturing, release, cold-chain; no licensor royalty, none disclosed for AMT-130): $0.30M/patient in FY27, falling $0.020M/yr to $0.20M; UNVERIFIED, no uniQure disclosure [S]
- **S18** Hemgenix royalty build (US$M, GAAP license revenue): growth slows as Hemgenix matures; FY32+ +2.5/yr fading 5%/yr. Cash goes to HemB SPV until the royalty-financing cap is met (liability $473.2M = debt) [S]
- **S19** Hemgenix royalty build (US$M, GAAP license revenue): growth slows as Hemgenix matures; FY32+ +2.5/yr fading 5%/yr. Cash goes to HemB SPV until the royalty-financing cap is met (liability $473.2M = debt) [S]
- **S20** Hemgenix royalty build (US$M, GAAP license revenue): growth slows as Hemgenix matures; FY32+ +2.5/yr fading 5%/yr. Cash goes to HemB SPV until the royalty-financing cap is met (liability $473.2M = debt) [S]
- **S21** Hemgenix royalty build (US$M, GAAP license revenue): growth slows as Hemgenix matures; FY32+ +2.5/yr fading 5%/yr. Cash goes to HemB SPV until the royalty-financing cap is met (liability $473.2M = debt) [S]
- **S22** Hemgenix royalty build (US$M, GAAP license revenue): growth slows as Hemgenix matures; FY32+ +2.5/yr fading 5%/yr. Cash goes to HemB SPV until the royalty-financing cap is met (liability $473.2M = debt) [S]
- **S23** Hemgenix royalty build (US$M, GAAP license revenue): growth slows as Hemgenix matures; FY32+ +2.5/yr fading 5%/yr. Cash goes to HemB SPV until the royalty-financing cap is met (liability $473.2M = debt) [S]
- **S24** Hemgenix royalty build (US$M, GAAP license revenue): growth slows as Hemgenix matures; FY32+ +2.5/yr fading 5%/yr. Cash goes to HemB SPV until the royalty-financing cap is met (liability $473.2M = debt) [S]
- **S25** Collaboration services to CSL wound down after the 2024 Lexington Transaction; none in H1 2026 [S]
- **S26** No AMT-130 US revenue: no approval before 2027.
- **S27** No AMT-130 UK revenue in base
- **S28** base EBITDA (US$M) = license GP + AMT-130 revenue - COGS 12.0 - cash opex 333.3 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $80M, $1.5M per active center, 5% variable) [S]
- **S29** base EBITDA (US$M) = license GP + AMT-130 revenue - COGS 186.1 - cash opex 452.9 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $80M, $1.5M per active center, 5% variable) [S]
- **S30** base EBITDA (US$M) = license GP + AMT-130 revenue - COGS 614.9 - cash opex 649.3 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $80M, $1.5M per active center, 5% variable) [S]
- **S31** base EBITDA (US$M) = license GP + AMT-130 revenue - COGS 1039.0 - cash opex 870.0 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $80M, $1.5M per active center, 5% variable) [S]
- **S32** base EBITDA (US$M) = license GP + AMT-130 revenue - COGS 430.6 - cash opex 592.7 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $80M, $1.5M per active center, 5% variable) [S]
- **S33** base EBITDA (US$M) = license GP + AMT-130 revenue - COGS 224.7 - cash opex 454.3 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $80M, $1.5M per active center, 5% variable) [S]
- **S34** base EBITDA (US$M) = license GP + AMT-130 revenue - COGS 224.7 - cash opex 461.1 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $80M, $1.5M per active center, 5% variable) [S]
- **S35** Average of me and FY38 gross margin (Finagle default rule); no positive-EBITDA history to set it against [S]
- **S36** FY39 growth: royalty 53.8 (+3%) + AMT-130 at the FY38 steady-state flow and price, vs FY38 revenue [S]
- **S39** No AMT-130 UK revenue in bull (UK launch from Q3 2028 in bull only)
- **S40** bull EBITDA (US$M) = license GP + AMT-130 revenue - COGS 18.0 - cash opex 341.5 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $90M, $1.5M per active center, 5% variable, UK $15M from FY28) [S]
- **S41** bull EBITDA (US$M) = license GP + AMT-130 revenue - COGS 291.3 - cash opex 533.3 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $90M, $1.5M per active center, 5% variable, UK $15M from FY28) [S]
- **S42** bull EBITDA (US$M) = license GP + AMT-130 revenue - COGS 981.6 - cash opex 846.0 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $90M, $1.5M per active center, 5% variable, UK $15M from FY28) [S]
- **S43** bull EBITDA (US$M) = license GP + AMT-130 revenue - COGS 1404.0 - cash opex 1128.2 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $90M, $1.5M per active center, 5% variable, UK $15M from FY28) [S]
- **S44** bull EBITDA (US$M) = license GP + AMT-130 revenue - COGS 1477.4 - cash opex 1288.6 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $90M, $1.5M per active center, 5% variable, UK $15M from FY28) [S]
- **S45** bull EBITDA (US$M) = license GP + AMT-130 revenue - COGS 611.4 - cash opex 727.7 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $90M, $1.5M per active center, 5% variable, UK $15M from FY28) [S]
- **S46** bull EBITDA (US$M) = license GP + AMT-130 revenue - COGS 565.4 - cash opex 715.4 (core Q2 2026 run rate x4 +3%/yr, US commercial fixed $90M, $1.5M per active center, 5% variable, UK $15M from FY28) [S]
- **S47** Average of me and FY38 gross margin (Finagle default rule); no positive-EBITDA history to set it against [S]
- **S48** FY39 growth: royalty 53.8 (+3%) + AMT-130 at the FY38 steady-state flow and price, vs FY38 revenue [S]
- **S49** No AMT-130 US revenue: bear case, AMT-130 not approved.
- **S50** No AMT-130 UK revenue in bear
- **S52** bear: license gross profit - fixed cash opex 170 after a restructuring (US$M) [S]
- **S53** bear: license gross profit - fixed cash opex 150 after a restructuring (US$M) [S]
- **S54** bear: license gross profit - fixed cash opex 140 after a restructuring (US$M) [S]
- **S55** bear: license gross profit - fixed cash opex 140 after a restructuring (US$M) [S]
- **S56** bear: license gross profit - fixed cash opex 140 after a restructuring (US$M) [S]
- **S57** bear: license gross profit - fixed cash opex 140 after a restructuring (US$M) [S]
- **S58** bear: license gross profit - fixed cash opex 140 after a restructuring (US$M) [S]
- **S59** Bear: opex fixed after restructuring; an incremental royalty dollar drops through at the license gross margin [S]
- **S60** FY39 growth: Hemgenix royalty only, +3% [S]
- **S401** Revenue recognised at treatment (point in time), usual practice for one-time gene therapies; not a uniQure policy disclosure [S]
- **S402** Q3 2026 results date 2026-11-04 (not reopened this revision) [S]

## Appendix C – Method

We follow the forecaster method. Reported periods stay as reported. FY2026E is consensus, because there is no guidance. Later years are a quarterly line build: capacity, backlog and refill set patients, and patients × net price set AMT-130 revenue. FY2027E is not scaled to consensus, because the user's capacity instruction overrides it. The user's instructions are tagged P with their dates and override the default method. A CEO-simulation bot's review was used only as a pointer, and every figure is tagged to a document we opened. Tags: A actual or reported, G company statement, E external estimate, C calculation, S assumption, P user instruction, D document.
