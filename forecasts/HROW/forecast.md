# HROW — seven-year revenue and EBITDA forecast

As of 12 November 2026 (America/Toronto). US$ millions unless noted. Calendar fiscal year ending 31 December. Baseline FY2025A; explicit FY2026E–FY2032E (a seven-year window is a task override of the usual two-year explicit period). A collaborative Finagle valuation was run on 12 November 2026 (`finagle_handoff`: true); the result is in `finagle-run-20261112/valuation_result_v01.json`. Units: US$ millions. The audit record is `forecast.json` in this folder, with line drivers in `drivers.csv`.

## Status

Bottom-up product forecast. Lines are not scaled to guidance or consensus. FY2026E revenue of 348.132 is 9M 2026A printed 214.161 plus Q4 2026E 133.971, and is 1.868 below the exact 350.000 low end of the reaffirmed 350–365 range. The shortfall is not closed by a plug. Q4 Other branded uses the rounded 15.0, not the 15.3 component sketch (delta disclosed). An unrounded 15.3 would still leave FY2026E below 350. Adjusted EBITDA is a fully costed build; the FY2026E base of 43.289 sits above the revised floor of more than 40 but is not forced to that floor. The bear case is allowed to miss it.

G-MELT (MELT-300) is a memo line. The base uses the company’s planned 2028 launch, which is itself conditional on approval, and does not assert that the NDA has been or will be approved. First shipments are assumed in mid-2028 after a Q4 2027 standard-review PDUFA. Revenue is units × net realization: 60,000 / 250,000 / 500,000 / 750,000 / 750,000 units in FY2028E–FY2032E at 175 / 180 / 185 / 190 / 195 dollars, or 10.5 / 45.0 / 92.5 / 142.5 / 146.25. The mature 750,000 unit rate from FY2031E is 15% of 5 million U.S. cataract surgeries, per the 11 November 2026 instruction [P4]; a 10% current annual MKO share is not a verified printed figure in the sources used. Compounded MKO Melt stays in ImprimisRx; the compounding path is not cut further for the higher G-MELT share, because current annual MKO volume is undisclosed. The bear case is approval delay or non-approval (no G-MELT revenue through FY2030E).

YOCHIL (MELT-210) is a second memo line, not mixed into Other branded. It is a 3 mg midazolam Zydis ODT for sedation, anxiolysis and amnesia, not the midazolam-plus-ketamine cataract combo. End-of-Phase 2 was completed in the quarter ended 30 June 2026; Phase 3 is still ahead, so a 2028 launch is tighter than G-MELT’s. Units = penetration × (1/3) × that year’s IHEEZO customer units, with the same penetration fractions as the G-MELT ramp, using the official IHEEZO unit identity (FY28 327,457, then +41,804 a year). Revenue is 1.528 / 7.385 / 16.899 / 28.682 / 32.154 in FY2028E–FY2032E at the same 175–195 assumed net price. Product GM is 72% on the same Catalent comparator. The broader diagnostic/endoscopic/anesthesia-induction market is not in the base.

VEVYE, IHEEZO and TRIESENCE follow the 11 November 2026 rule-based rebuild [P2]. VEVYE holds a reconstructed net add of 49,538.5 TRx per quarter (Q4 2026E TRx 386,953.5) and a held Q4 derived net price of about $129.42 per TRx, with no unquantified coverage increment and no invented later-year price. IHEEZO uses a constant annual unit add of 41,804 from a cleaned 2026 four-quarter rate of 243,849, allocated on 2025 seasonal weights; Q4 2026E demand is 75,811 and Q4 dollars use the Q3 realization of $406.64 per customer unit times the 2024 recognition lift of 1.242; later years are demand times that realization with no net full-year inventory. TRIESENCE holds a net add of 5,044 customer units per quarter (Q4 2026E 25,066) at the Q3 realization of $534.76 per customer unit. TRx is a reconstructed index. These are aggregate stock-flow proxies, not patient or prescriber cohorts. Percentage growth is an output of the unit path.

TYRVAYA, BYOOVIZ, OPUVIZ, BYQLOVI and legacy are components of Other branded and sum to that line in every year (see `drivers.csv`). G-MELT launch spend is an explicit assumed program ($12 / $20 / $16–19), not a disclosed budget and not zero. A modest YOCHIL program of $6.0 / $10.0 / $8.0 / $8.5 / $9.0 / $9.5 in FY2027E–FY2032E sits on the existing Surgical team (not a second sales force), with a ±40% band [S33]. No incremental 2026 YOCHIL cost is added on top of the existing Q4 filing allowance and accelerated R&D that already includes YOCHIL. Gross margin is a weighted product-level build, including a 40% central Samsung share of net sales (undisclosed; band 30–50%) and a 7% Catalent royalty comparator (undisclosed; product GM band 65–78%). Melt contingent cash and stock are not deducted from Adjusted EBITDA. The 87.2 FDA-approval cash is recorded under `cash_share_adjustments` (when 2027-12-31 in the base, amount −87.16794, probability 1 consistent with the unweighted 2028 launch) and remains a funding-risk flag around a Q4 2027 PDUFA. Combined G-MELT + YOCHIL sales first exceed 100 of Annual Net Sales in FY2030E (109.399), so the first commercial cash milestone of −10.02 is now on the base schedule at 2030-12-31, with the 75-day payment mechanic disclosed. It is not an EBITDA item. A second FDA-approval cash payment is not added for YOCHIL. Operating free cash flow after the 1 October TYRVAYA close payment has not been independently verified in this file. The valuation discounts the whole `cash_share_adjustments` schedule at the cost of equity (see Valuation below).

## Four views

**Revenue FY2026E.** Bottom-up 348.132 is the base. Top-down is the reaffirmed 350–365 range (midpoint 357.5). Calibrated top-down is absent: first-half 2026 revenue was below the original first-half range of 133–153, and that historical miss is recorded in the method appendix and is not applied to the reaffirmed full-year range. Consensus is absent (no post-Q3 2026 pull). Bottom-up / base = 1.00. Top-down midpoint / base is about 1.027. The base is about 1.87 below the 350 low end.

**EBITDA FY2026E.** Bottom-up 43.289 is the base. Top-down is the revised single-point floor of more than 40, including more than 33 in Q4. Calibrated top-down and consensus are absent. The base is the cost build; it is not forced to the floor. Top-down point / base is about 0.924.

**FY2027E–FY2032E.** No published guidance and no current consensus. Bottom-up is the base for revenue and Adjusted EBITDA in every later year. Top-down, calibrated top-down and consensus are absent.

## Base totals

| Period | Revenue | YoY | Adj. EBITDA | Margin | GAAP GM |
|---|---:|---:|---:|---:|---:|
| FY2024A | 199.614 | — | 40.327 | 20.2% | 75.0% |
| FY2025A | 272.303 | 36.4% | 61.923 | 22.7% | 75.0% |
| 9M 2026A | 214.161 | — | 7.327 | 3.4% | 71.0% |
| Q4 2026E | 133.971 | — | 35.962 | 26.8% | 73.6% |
| FY2026E | 348.132 | 27.8% | 43.289 | 12.4% | 72.1% |
| FY2027E | 612.684 | 76.0% | 177.177 | 28.9% | 72.5% |
| FY2028E | 803.450 | 31.1% | 297.868 | 37.1% | 73.8% |
| FY2029E | 1019.546 | 26.9% | 454.252 | 44.6% | 74.5% |
| FY2030E | 1249.797 | 22.6% | 613.517 | 49.1% | 75.0% |
| FY2031E | 1483.318 | 18.7% | 774.890 | 52.2% | 75.4% |
| FY2032E | 1660.779 | 12.0% | 895.576 | 53.9% | 75.8% |

FY2027E–FY2032E GAAP gross margin is (product gross profit − amortization) / revenue from the weighted product-level rates in S19, not a flat 75% assumption. Cash opex follows the bridge in C14 / S20 (core Q3 run rate inflated 4%, plus TYRVAYA 20 once from FY2027E, plus explicit G-MELT and YOCHIL programs, plus 4% of same-store revenue above the Q3 2026 annualized same-store revenue of 397.188). FY2032E Adjusted EBITDA margin of 53.9% is that fully costed central result applied to the constant-add product paths and the 15% G-MELT / YOCHIL memo lines. It sits well beyond the FY2024A 20.2% and FY2025A 22.7% history and beyond any management-described margin; it is flagged with the bridge shown and is not capped, and operating leverage is a named bear lever (S42).

## Lines (base)

Official reporting lines follow the Q3 2026 presentation, with TRIESENCE split out of the FY2025 10-K “Other branded” total and with G-MELT and YOCHIL as separate memo lines. FY2024 TRIESENCE is not a reported zero actual: it was not a separately disclosed line, and this file keeps a technical unallocated placeholder of 0 so official lines can sum to printed total revenue. Any Q4 2024 relaunch dollars remain inside Other branded 37.836. The report table shows N/D, not a factual zero.

| Line | FY24A | FY25A | 9MA | Q4E | FY26E | FY27E | FY28E | FY29E | FY30E | FY31E | FY32E |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VEVYE | 28.061 | 88.688 | 90.033 | 50.080 | 140.113 | 264.435 | 367.017 | 469.599 | 572.180 | 674.762 | 777.344 |
| IHEEZO | 49.303 | 81.348 | 42.833 | 38.287 | 81.120 | 116.158 | 133.157 | 150.156 | 167.155 | 184.154 | 201.153 |
| TRIESENCE | n/d (0 placeholder) | 9.900 | 20.134 | 13.404 | 33.538 | 80.591 | 123.748 | 166.906 | 210.063 | 253.220 | 296.378 |
| Other branded | 37.836 | 15.426 | 16.944 | 15.000 | 31.944 | 79.000 | 95.000 | 108.000 | 117.500 | 124.500 | 130.000 |
| Other revenues | 0.915 | 0.394 | 0.327 | 0.200 | 0.527 | 0.500 | 0.500 | 0.500 | 0.500 | 0.500 | 0.500 |
| ImprimisRx | 83.499 | 76.547 | 43.890 | 17.000 | 60.890 | 72.000 | 72.000 | 72.000 | 73.000 | 75.000 | 77.000 |
| G-MELT | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 10.500 | 45.000 | 92.500 | 142.500 | 146.250 |
| YOCHIL | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.528 | 7.385 | 16.899 | 28.682 | 32.154 |
| **Total** | **199.614** | **272.303** | **214.161** | **133.971** | **348.132** | **612.684** | **803.450** | **1019.546** | **1249.797** | **1483.318** | **1660.779** |

Q4 2026E Other branded uses the rounded 15.0 (not the 15.3 component sketch). Unrounded, Q4 would be 134.271 and FY2026E 348.432, still below the 350 low end. Other branded components (TYRVAYA, BYOOVIZ, OPUVIZ, BYQLOVI, legacy) sum to the line in every year; see `drivers.csv`. The Q4 / FY2026 grid in the report keeps a separate BYOOVIZ row (Q3 illustrative 2.92*, not independently measured; Q4 4.0; rest of Other branded 4.675* in Q3 and 11.0 in Q4, including TYRVAYA).

## Q4 2026E and FY2026E vs. guidance

Implied Q4 to hit 350–365: 135.839–150.839. Base Q4 133.971 / FY 348.132 is 1.868 below the exact low end and about 16.9 below the high end. This is a bottom-up build, not a back-solve. Management also described “reasonable scenarios” of a modest miss, mostly because of order timing and year-end purchasing. Base Q4 Adjusted EBITDA 35.962 and FY 43.289 sit above the floors of more than 33 and more than 40. They are not plugged to those floors.

## Cost build

Q3 2026 cash opex 59.258; Q4 68.258 (Q3 + 5.0 partial TYRVAYA + 4.0 G-MELT filing allowance, already in the FY2026E path). FY2026E cash opex 229.470. FY2027E 290.893 = 59.258×4×1.04 core (246.513; 4% is a named rate, S40, from the BLS Employment Cost Index, band 3–5%) + 20.0 TYRVAYA + 12.0 G-MELT pre-launch + 6.0 YOCHIL program + 6.380 same-store variable (4%, S41, central in a 2–8% band, of same-store VEVYE, IHEEZO, TRIESENCE, legacy, compounding and other revenues above the Q3 2026 annualized same-store revenue of 397.188, C17; not also 4% of TYRVAYA, BYOOVIZ, OPUVIZ, BYQLOVI, G-MELT or YOCHIL). The Q3 run rate already pays for the Q3 revenue pace; FY2026E is only the base for YoY growth. Printed Q3 Other branded includes unseparated BYOOVIZ and is used as printed; removing the illustrative 2.92 would cut EBITDA by about 0.47 a year. Later years: core +4%; TYRVAYA 20 continues (once); G-MELT program 20 / 16 / 17 / 18 / 19 and YOCHIL program 10.0 / 8.0 / 8.5 / 9.0 / 9.5 in FY2028E–FY2032E; variable is 4% of the same-store increment over the Q3 annualized base. Cash opex FY2027E–FY2032E: 290.893 / 319.303 / 330.067 / 348.802 / 367.983 / 387.648. Product gross margins before amortization: VEVYE 80%, IHEEZO 82%, TRIESENCE 80%, TYRVAYA 79%, BYOOVIZ/OPUVIZ 52% (40% Samsung share + about 8% other COGS; sensitivity 30% share ≈ 62% GM, 50% ≈ 42%), legacy/BYQLOVI 78%, compounding 55%, G-MELT and YOCHIL 72% (band 65–78%). Amortization 21.8 / 24 / 24.5 / 25 / 25 / 25 / 25. Q4 inventory step-up of 2.5 hits GAAP and Adjusted gross profit (not an add-back under the letter definition).

## Cash and share adjustments (not EBITDA)

Melt FDA-approval cash of 87.16794 (contract $87,167,940) is on the base schedule at 2027-12-31 with probability 1, consistent with the unweighted 2028 launch already in the revenue path. It is outside revenue, EBITDA, and later cash-flow years. The CMS J-code / pass-through stock milestone is omitted from the schedule because award timing is uncertain. Combined base G-MELT + YOCHIL sales first exceed 100 of Annual Net Sales in FY2030E (109.399), so the first commercial cash milestone of −10.02 is on the base schedule at 2030-12-31 (payment within 75 days after year-end). The path does not reach 250 in the explicit window. The bull schedule brings the first 10.02 milestone forward to 2029-12-31 and adds the second 25.02 milestone at 2032-12-31. The bear schedule has no commercial cash in the window. A second FDA-approval cash payment is not added for YOCHIL. TYRVAYA close cash of −30.0 (paid 1 October 2026 from cash on hand) is the first item on every schedule, because year-0 cash is the 31 December 2025 balance (P5); its discount is 1. A year-0 equity raise is appended under David May's P6 rule because opening cash plus the schedule's present value would otherwise be negative: base 50, bull 100, bear 50, dated 12 November 2026 at the share price (probability 1). Remaining TYRVAYA sales milestones are not expected on anticipated 2027 revenue.

Melt Schedule A detail (for reference, also in the report Appendix B): FDA-approval cash 87,167,940; CMS pass-through AND J-code stock 47,942,367 at a contractual 43.13/share ≈ 1,111,578 fixed shares (not cash, about 3.0% vs. 37,533,160 shares as of 5 November 2026 if issued); commercial cash milestones 10.02 / 25.02 / 50.03 / 74.96 / 99.98 at Annual Net Sales of 100 / 250 / 500 / 750 / 1,000, once each, stackable in the same year, sum 260,021,965.02. Total if all hit 395,132,272.02. Deadline 31 December 2035. Recipients are non-Harrow former holders. Closing IPR&D 8.450 was expensed in FY2025.

## Valuation (Finagle, 12 November 2026)

Collaborative run at Finagle commit 377f177b4013e713fe7c4603962e5f883a67e298; price 29.37 and 10-year yield 4.998% fetched 12 November 2026. Seven explicit years (FY2026E–FY2032E) plus three Finagle extension years to FY2035E. Terminal growth is Finagle's default (equals the 10-year yield) and was not set. Opening cash 72.927 and 37,229,159 shares at 31 December 2025 (P5, A21); no 2026 equity sale (A22).

| Case | Value per share | Equity | Firm | Year-0 cash (adj.) | Shares (adj., m) | me | mc | gsnext | Terminal WACC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bear | 14.71 | 537.4 | 787.4 | 35.234 | 38.9316 | 0.2245 | 0.4901 | 0.0086 | 0.0875 |
| base | 132.69 | 5,157.5 | 5,407.5 | 8.453 | 38.9316 | 0.5393 | 0.6484 | 0.1069 | 0.0920 |
| bull | 153.28 | 6,184.2 | 6,434.2 | 44.196 | 40.6340 | 0.5653 | 0.6650 | 0.1188 | 0.0921 |

Finagle defaults filled: NOL 0, NOA 0, cost of equity 10.498% (5.5% + 10-year yield), terminal growth 4.998%, terminal ROIC 15%, tax 21%, cost of debt 9.672% (interest 24.18 / debt 250), working capital zero, debt target leverage 4.04x from year 1, no distribution. Sanity flags: base none; bull "negative cash" (a floating-point residue of about −7e-15 in FY2026E); bear "negative FCFE after year 1". Validation warnings (all cases): average EBITDA growth with no acquisitions, and acquisitions mentioned but none in the case; TYRVAYA is in the lines and its close cash is on the schedule (C18, C20). Caveats: the default debt policy re-levers to 4.0x and pays the borrowing out, which raises value materially; Finagle's capex rule lifts capex far above Harrow's reported level; year-0 debt 250 excludes the March 2026 add-on notes.

## Assumptions (changeable)

Load-bearing tags: S1–S7 (Q4 and TYRVAYA / biosimilar presentation), S11 (Q4 step-up), S12 and S24–S39 (milestone accounting and cash-share dates and probabilities), S13 (compounding / legacy after MKO conversion), S14 / S23 (TRIESENCE patents and units), S15 / C12 / P4 (G-MELT 15% volume × price), S32 / C16 / P4 (YOCHIL IHEEZO-third build), S33 (YOCHIL program opex), S16 (Catalent comparator), S17 / S20 / C14 (opex bridge and Melt programs), S18 / S19 / C13 (product GM and Samsung share), S21 / S22 (VEVYE and IHEEZO unit–NPP math), P2 (the authorized product-rebuild rules), P4 (the 15% G-MELT / YOCHIL instruction). Bands are in those entries. See the report Appendix B for the full text of each tag.

## Scenarios

Named levers: (1) Q4 / FY2026 mix and IHEEZO recognition vs. the 350–365 range, (2) Novaliq consent on TYRVAYA, (3) BYOOVIZ / OPUVIZ ramp and the Samsung share, (4) G-MELT and YOCHIL approval / launch timing and penetration, (5) VEVYE net-price step and how soon net adds fade, (6) TRIESENCE post-2029 patents, (7) product gross margins under undisclosed profit-share / royalty takes, (8) operating leverage: the bear inflates core cash opex at 5% and takes 8% variable opex on same-store growth above the Q3 2026 annualized base (S42), which lowers bear FY2032E Adjusted EBITDA from 167.358 to 142.781. Bear FY2026E revenue 335.849 / Adjusted EBITDA 34.015 (misses the 40 floor). Bull FY2026E 358.459 / 51.086 (above the 350 low end, not plugged to 365, and still below the withdrawn 80–100 EBITDA range). Bear later years fade VEVYE net adds after FY2028E, use half the IHEEZO and TRIESENCE adds, drop IHEEZO Q4 recognition, take G-MELT as delayed past 2030, give YOCHIL no revenue in the window, haircut the other lines, and cut product margins about 3 points. Combined bear Melt sales do not reach 100. Bull later years keep the base unit rules, apply an 8% VEVYE coverage increment above the held Q4 exit, ramp G-MELT faster than the 15% base (to about 25% of the 5 million cataract target by FY2032E), and use a faster YOCHIL penetration of the same IHEEZO one-third, so combined Melt sales reach 100 in FY2029E and 250 in FY2032E.

## Revision log

See `revision_log.md`. The 12 November 2026 update re-measures same-store variable opex from the Q3 2026 annualized base, adds the operating-leverage bear lever and runs Finagle; revenue and FY2026E are unchanged. The 11 November version replaced the prior retained chat product bases with the 11 November 2026 rule-based rebuild. FY2026E revenue and Adjusted EBITDA move because the three product Q4s change. Later-year totals move because the same volume rules are extended through FY2032E.

## Sources

Numbered D / A / G / S / C / P entries live in `forecast.json`. Canonical IDs include D1–D23, A1–A23, G1–G26, S1–S44, C1–C21, P1–P7. Instance suffixes such as C10_1 distinguish different year/line values that share a calculation template so the validator can separate facts. The report appendix lists the canonical entries. D3, D14 and D15 point at the SEC letter, the GitHub transcript mirror (plus the original Seeking Alpha recording), and the SEC November 2026 deck, respectively — not at the IR homepage.
