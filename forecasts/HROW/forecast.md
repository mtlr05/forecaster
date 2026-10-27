# Harrow, Inc. (HROW)

Explicit window: FY2026 and FY2027. Year 0 is FY2025. Dollars are millions of USD. The tested figures are in `forecast.json` (recomputed by `build_forecast.py`). This note rounds some of them to three decimals.

Re-derived under the guidance-position method. An earlier pass haircut the guidance range by the average historical miss (FY26 revenue 333.7, EBITDA 72.5). That is not this method. FY25 guidance was a single point, so there is no coefficient. H1 2026 missed the low end of a real range, and a revenue consensus exists, so the revenue total is that consensus.

No value per share. Finagle was not run on this case. A value would also need the template leaves (`debt.mode` in particular), which are not asserted here.

## Base forecast

Lines are the ones Harrow reports: IHEEZO, VEVYE, other branded (other branded products plus other revenues; TYRVAYA sits here from Q4 2026), and ImprimisRx (the compounding segment).

| Line | FY25A | YoY | FY26 = H1A + H2 | FY27 |
|---|---:|---:|---:|---:|
| IHEEZO | 81.348 [A] | +65.0% | 17.535 + 55.608 = **73.143** [S] | **125.373** [S] |
| VEVYE | 88.688 [A] | +216.1% | 50.335 + 93.353 = **143.688** [S] | **205.031** [S] |
| Other branded | 25.720 [A] | −33.6% | 18.939 + 44.860 = **63.799** [S] | **132.685** [S] |
| ImprimisRx | 76.547 [A] | −8.3% | 28.055 + 41.459 = **69.514** [S] | **73.239** [S] |
| **Revenue** | **272.303** [A] | +36.4% | 114.864 + 235.280 = **350.144** [E] | **536.328** [E] |
| GAAP gross margin | 75.1% [C] | | 67.4% H1A, 78% H2 [S] → **74.5%** [C] | **78.0%** [S] |
| **Adj. EBITDA** | **61.923** [A] | +53.6% | −13.891 + 75.328 = **61.437** [C] | **185.101** [S] |
| Adj. EBITDA margin | 22.7% [C] | | **17.5%** [C] | **34.5%** [C] |

FY24, for the growth rates: IHEEZO 49.303, VEVYE 28.061, other branded 38.751, ImprimisRx 83.499, total 199.614. Adjusted EBITDA 40.327. All [A].

Other branded is the filing's "other branded products" plus "other revenues" (FY25 25.326 + 0.394). An earlier round of this case used 38.8 for FY24 other branded; the filing columns are 37.836 + 0.915 = 38.751. That difference is the filing, not a new assumption.

## Totals: why the coefficient was not used

FY25 revenue guidance was a single point, so `C` is undefined.

- "more than $280 million" in the May 8, 2025 stockholder letter, and "greater than $280 million" on August 11, 2025. [G]
- Actual FY25 revenue was 272.303, below that floor. [A]
- On November 10, 2025 the letter cut the outlook to "$270 million to $280 million". [G] A coefficient from a revised range is not applied to next year's original range. It is not used.

FY26 revenue guidance, original and never revised: "$350 million to $365 million, including $133 million to $153 million in the first half" and adjusted EBITDA "$80 million to $100 million", March 2, 2026. Reaffirmed May 11, 2026. Reiterated August 10, 2026. [G]

Completed windows against those original ranges:

| Window | Low | High | Actual | C = (Actual − Low) / (High − Low) |
|---|---:|---:|---:|---:|
| H1 2026 revenue | 133 | 153 | 114.864 | **−0.907** [C] |
| Q2 2026 revenue | 71 | 81 | 70.661 | **−0.034** [C] |

`C < 0` on the H1 window, which is the one that covers a full half of the year. Analyst revenue estimates exist, so the branch is consensus, not `Low + C × (High − Low)`.

Consensus, carried from a yfinance `revenue_estimate` pull on 2026-10-22. Not re-pulled for this file. The Yahoo page was opened and returns the analysis URL; the figures themselves are the carried pull, and the live page will have moved. [E]

| | Point | Low | High |
|---|---:|---:|---:|
| FY26 revenue | 350.144 | 341 | 355 |
| FY27 revenue | 536.328 | 479 | 587 |

This pull is after the Q2 release. It is the forward anchor, not a pre-release score of the quarter. No pre-release consensus was in the source material, so none is shown.

EBITDA is separate, and the coefficient does not run:

- No original EBITDA range for a completed year is in the sources, so there is no EBITDA `C`.
- The carried Yahoo pull is revenue only. No EBITDA estimate is invented.
- The $80–100 million FY26 guide stays on the page as guidance. It is not the forecast.

FY26 and FY27 EBITDA are the cost build in the next section. Flagged, because the method would rather have used an estimate.

The "over $250 million in quarterly revenue by the end of 2027" line (CEO, March 2, 2026 release) is not a range and is not used. It implies a run rate far above the FY27 consensus. [G]

## Lines, then the scale

Unscaled H2, before it is forced to the consensus total:

| Line | Driver | Unscaled H2 |
|---|---|---:|
| IHEEZO | Q2 revenue 15.619 × 1.25 price, two quarters. Units held at the Q2 rate. | 39.048 |
| VEVYE | Q2 29.387, then +7.5% and +7.5% again. | 65.551 |
| Other branded | Q3 13.0, Q4 14.5, TYRVAYA 4.0 in Q4. | 31.500 |
| ImprimisRx | Flat at the Q2 actual 14.556, two quarters. | 29.112 |
| **H2** | | **165.211** |

H1 actual 114.864 plus that H2 is an unscaled FY26 of 280.075. Consensus H2 is 350.144 − 114.864 = 235.280. **Scale on H2 = 1.424.** [C]

Unscaled FY27 is 390.873 (IHEEZO 91.371, VEVYE 149.426, other branded 96.700, ImprimisRx 53.376). Consensus 536.328. **Scale = 1.372.** [C]

Both factors are more than 10% from 1. The skill's method is to scale the lines to the total, so the line dollars above are the consensus allocated by driver. The unscaled sums are a diagnostic of how far the line commentary is from the total, not an alternative forecast. Flagged, as 2c requires.

An earlier build used 14.5 as the ImprimisRx quarter instead of the Q2 actual 14.556. This file uses 14.556. Recomputed.

### What each line is doing

**IHEEZO, ramping, price times volume.** "Effective July 1, 2026, IHEEZO net price per unit improved by approximately 25%." [G] Q2 unit demand was 65,477, "+34% year-over-year", and "channel inventories have normalized." [G] Volume is held at that quarter [S]: the inventory swing is treated as done, so it does not get annualized again, and no unit guide was given. FY27 units +17%, half the Q2 unit growth [S], because a launch-year unit step is a weak thing to hold for a second year. Price and volume are multiplied, then the line is scaled.

**VEVYE, ramping.** "Momentum continues to build, supported by our recent coverage win that went into effect August 1." [G] The starting default for "momentum continues" is to hold the prior growth rate. +7.5% a quarter in H2 is a larger step than that default [S], listed below. FY27 is the Q4 run rate × 4 × 1.10 [S]. May 11, 2026: "on track to deliver 2026 revenue of over $100 million." [G] The base line is 143.7, above that floor. The Q1 gross-to-net item is one-time: reported VEVYE of $20.9 million was "approximately $8 million below" what management says it would have been, and they called it non-recurring (May 11, 2026). [G] It is not in the run rate. The run rate starts at Q2.

**Other branded, new lines plus a floor.** "BYOOVIZ launched in July 2026, and the Company expects revenue to build over the balance of the year." [G] Q3 13.0 and Q4 14.5 are judgments carried from the earlier line build. The filing does not give those dollars. [S] TYRVAYA "is expected to contribute modestly to 2026 revenue" [G]; $4 million in Q4 is 1.1% of the FY26 total, inside the 1–3% starting band for "modest." [S] "More than $30 million in revenue in 2027" is the FY27 floor, used as 30 before scaling. [G] The close was October 5, 2026, "paid $30 million in cash." [G]

**ImprimisRx, mature.** Flat at the Q2 run rate [S]. FY27 then applies the FY25 decline of 8.3% [C from actuals]. No structural change was named for this segment.

## Costs

Revised October 22, 2026 to follow the bridge management gave on the Q2 2026 call (August 2026; Seeking Alpha transcript, https://seekingalpha.com/article/4934770-harrow-inc-hrow-q2-2026-earnings-call-transcript, read from David's ceochat copy). Quotes checked against that transcript: [G]

- "GAAP gross margin was 71%. For the second half, we expect gross margins to trend back towards the high 70s supported by IHEEZO's return to a normal revenue cycle, increased overall revenue, continued VEVYE growth, and more favorable product mix."
- "Excluding the additional headcount expected to be added through the TYRVAYA transaction at closing, we expect base SG&A dollars to remain approximately flat with second quarter levels for the balance of the year."
- "The adjusted EBITDA bridge follows directly from the revenue bridge, substantially higher revenue, increasing gross margins into the high 70s, and a base operating expense structure that remains approximately flat."
- TYRVAYA: "increasing SG&A expenses by approximately $20 million on an annualized basis once fully integrated." The October 5, 2026 close release says Harrow "expects to onboard these new colleagues during the fourth quarter of 2026" and "expects TYRVAYA to contribute more than $30 million in revenue in 2027." [G]

**Q2 adjusted opex = 57.122** [C] = total operating expenses 61.370 − stock-based compensation 3.788 − depreciation 0.460 (Q2 release income statement and adjusted EBITDA reconciliation). [A inputs]

**Where amortization and SBC sit.** Amortization of intangibles (Q2 5.527 [A]) is in cost of sales: the Q2 letter attributes the gross-margin decline partly to "amortization of acquired NDAs", and the reconciliation closes only that way: gross profit 50.363 + amortization 5.527 − 57.122 = −1.232, the reported Q2 adjusted EBITDA. [C] SBC (3.788) and depreciation are treated as opex. The release does not split SBC by line; the exact reconciliation is consistent with all of it in opex. [C, flagged]

**Margin basis: GAAP.** Management's 71% and "high 70s" are GAAP gross margin, so the ramp is applied on GAAP and amortization is added back to reach adjusted EBITDA. Q2 cash gross margin (before amortization) was 79.1%. Using "high 70s" as a cash margin would double-count nothing but would understate EBITDA by about 11 in H2 (no amortization add-back). "High 70s" is read as 77–79% by analogy with the wording table's "high single-digit" 7–9%; base 78%, bear 77%, bull 79%. [S]

H2 adjusted EBITDA = H2 revenue 235.280 × 78% + 2 × 5.527 amortization − (2 × 57.122 + 5.0 TYRVAYA Q4 cost) = **75.328**. FY26 = −13.891 + 75.328 = **61.437** (17.5%). The 5.0 is David's estimate of a Q4 partial of the ~$20M annual run rate. [P]

FY27 = 536.328 × 78% + 4 × 5.527 − (4 × 57.122 × 1.03 + 20.0) = **185.101** (34.5%). The 78% is held from H2 [S]; amortization is held at Q2 [S] (TYRVAYA intangibles will add amortization, but it is added back, so adjusted EBITDA is unaffected on this basis); base opex +3% [S]; TYRVAYA 20 [G/P].

**Cross-check against David's source** ($67–72M at midpoint revenue, $73–78M at the top, both below the $80M low end). Same bridge, other revenues: [C]

| FY26 revenue | GM 77% | GM 78% | GM 79% | 78%, no TYRVAYA cost |
|---|---:|---:|---:|---:|
| 357.5 (guide midpoint) | 64.7 | 67.2 | 69.6 | 72.2 |
| 365.0 (guide top) | 70.5 | 73.0 | 75.5 | 78.0 |

At 78% the build reproduces David's ranges: the low end with the $5M TYRVAYA cost, the high end without it. It agrees. The base here is lower, 61.4, only because revenue is consensus 350.1 rather than the 357.5 guide midpoint: 7.4 less revenue × 78% ≈ 5.8. Even the bull (79%, 355 revenue) gives 67.6. **Flag: every scenario stays below the $80–100M guide**; reaching $80M on this bridge needs roughly 365 revenue at 79%+ with no TYRVAYA cost, or opex below the Q2 level.

FY27 margin expansion still comes mostly from the revenue scale (1.37×) against flat base opex. That is now consistent with management's stated intent ("our objective is to grow revenue against that expense base"), but no FY27 margin was guided. Listed below.

## Scenarios

Three levers: where in the consensus range revenue sits, GAAP gross margin within "high 70s" (H2 and FY27), and FY27 base-opex inflation. The line drivers, the Q2 opex base and the TYRVAYA costs (5 / 20) do not change.

| | Revenue | GAAP GM (H2, FY27) | FY27 opex infl. | FY26 rev | FY26 GM | FY26 EBITDA | FY27 rev | FY27 GM | FY27 EBITDA |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | consensus low | 77% | +8% | 341.0 | 73.8% | 52.044 (15.3%) | 479.0 | 77% | 124.171 (25.9%) |
| Base | consensus point | 78% | +3% | 350.144 | 74.5% | 61.437 (17.5%) | 536.328 | 78% | 185.101 (34.5%) |
| Bull | consensus high | 79% | 0% | 355.0 | 75.2% | 67.626 (19.0%) | 587.0 | 79% | 237.350 (40.4%) |

Bear H2 scale 1.369, FY27 scale 1.225. Bull 1.454 and 1.502.

## Finagle leaves (base, organic)

TYRVAYA is not in these rates. Year 0 is already organic.

| Leaf | Value | Tag |
|---|---|---|
| `forecast.ebitda_basis` | organic | [C] |
| `forecast.ebitda_growth` | +0.0011, +1.7905 | [C] |
| `forecast.sales_growth` | +0.2649, +0.4376 | [C] |
| `me` | 0.3494 | [C] |
| `mc` | 0.5647 | [S] |
| `gsnext` | 0.20 | [S] |
| `deal_spend` | [0, 30] | [G] |

Organic dollars: see `forecast.json` `organic` (recomputed with the revised cost build). These leaves are carried for the file's tests only; Finagle was not run.

`me` is FY27 organic EBITDA / FY27 organic revenue. That is the margin `forecast_ebitda` uses when sales growth reaches the last explicit year. It is not the year-0 margin (61.923 / 272.303 = 22.7%).

`mc` is the average of that ending margin and the 78% gross margin [S]. Finagle's filler would have averaged the year-0 margin instead. This sets the one the fade should use.

`gsnext` 20% [S]. FY25 revenue grew 36%. Launches are still described through 2029, and there is no FY28 dollar. 20% fades the FY27 step-up instead of repeating it. The fade from 20% down to terminal growth is Finagle's. `gt` is not set.

Acquisition, all seven fields: year 1 [G], deal value 30 [G], multiple 2.48 [S] (30 / FY27 TYRVAYA EBITDA of about 12.1), leverage 0 [G] (cash at close), next growth 0.15 [S], capex fraction 0.02 [S], `pay_from_cash` false [C] because that flag only touches year-0 cash and the close is in year 1. Milestones of up to $70 million are excluded [G]; they are contingent and not in the base.

Template leaves (horizon, cost of debt, tax, NOL, non-operating assets, working capital, distribution, debt policy, terminal growth) are not filled. The FY2025 10-K does say federal NOL carryforwards were about $37.124 million. That is a filing fact a person can put in the template. It is not a forecast output.

## Assumptions to revise

The moves that change the answer:

1. Revenue is the Yahoo consensus (re-pulled 2026-10-22, unchanged), because H1 `C` is −0.91. Lines are scaled to it (H2 1.42×, FY27 1.37×); that is the method, and the unscaled build is a diagnostic only.
2. GAAP gross margin 78% in H2 and FY27, reading "high 70s" as 77–79%. Each point is about 2.4 of FY26 EBITDA and 5.4 of FY27.
3. Base adjusted opex flat at Q2's 57.122 a quarter through Q4, then +3% in FY27. The flat-through-2026 part is management's; the FY27 inflation is mine.
4. TYRVAYA SG&A 5 in Q4 2026 [P] and 20 in FY27 ("approximately $20 million on an annualized basis once fully integrated" [G]).
5. Amortization held at Q2's 5.527 a quarter and added back (GAAP margin basis). `gsnext` 20%.

Other judgments, each tagged `[S]` in the file: IHEEZO units flat then +17%; VEVYE +7.5% a quarter and FY27 × 1.10; other branded Q3 13 and Q4 14.5; TYRVAYA Q4 revenue stub of 4; ImprimisRx flat then the FY25 decline; SBC treated as entirely in opex; scenario GM 77/79 and inflation 8%/0%; `mc`; acquisition next growth 0.15 and capex fraction 0.02; milestones left out.

## Links

- Q2 2026 stockholder letter: https://www.sec.gov/Archives/edgar/data/1360214/000149315226036865/ex99-2.htm
- Q2 2026 call transcript (Seeking Alpha; read from ceochat `companies/hrow/sources/calls/seeking-alpha/2026-Q2.md`, read-only): https://seekingalpha.com/article/4934770-harrow-inc-hrow-q2-2026-earnings-call-transcript

Opened and read for this case. Each `[A]` and `[G]` above uses one of these.

- FY2025 10-K, filed 2026-03-02: https://www.sec.gov/Archives/edgar/data/1360214/000149315226008562/form10-k.htm
- FY2025 earnings release, 2026-03-02: https://www.sec.gov/Archives/edgar/data/1360214/000149315226008552/ex99-1.htm
- FY2025 stockholder letter (product table): https://www.sec.gov/Archives/edgar/data/1360214/000149315226008552/ex99-2.htm
- Q2 2026 10-Q, filed 2026-08-10: https://www.sec.gov/Archives/edgar/data/1360214/000162828026055271/hrow-20260630.htm
- Q2 2026 earnings release, 2026-08-10: https://www.sec.gov/Archives/edgar/data/1360214/000149315226036865/ex99-1.htm
- Q1 2026 earnings release, 2026-05-11: https://www.sec.gov/Archives/edgar/data/1360214/000149315226022227/ex99-1.htm
- Q1 2026 stockholder letter: https://www.sec.gov/Archives/edgar/data/1360214/000149315226022227/ex99-2.htm
- May 8, 2025 letter ("more than $280 million"): https://www.sec.gov/Archives/edgar/data/1360214/000164117225009247/ex99-2.htm
- August 11, 2025 release ("greater than $280 million"): https://www.sec.gov/Archives/edgar/data/1360214/000164117225022971/ex99-1.htm
- November 10, 2025 letter (outlook cut to $270–280 million): https://www.sec.gov/Archives/edgar/data/1360214/000149315225021555/ex99-2.htm
- TYRVAYA close, 8-K exhibit, filed 2026-10-05: https://www.sec.gov/Archives/edgar/data/1360214/000162828026064749/hrow-20261001xex991.htm
- Consensus page (figures carried, not re-pulled): https://finance.yahoo.com/quote/HROW/analysis/

## Not verified

- Consensus re-pulled via yfinance on 2026-10-22: FY26 350.144 (341–355), FY27 536.328 (479–587). Unchanged.
- No EBITDA consensus was available to carry, so none is used.
- Ceochat was read only for the Q2 2026 call transcript, which David supplied. No other ceochat content was used.
- Finagle was not run. No value per share.
- Q3 13 and Q4 14.5 for other branded, the VEVYE +7.5% step, the FY27 × 1.10, the 78% margin point inside "high 70s", FY27 opex inflation, and `gsnext` of 0.20 are assumptions. The quotes they hang on were checked; the magnitudes were not in the filings.
