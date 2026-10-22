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
| Gross margin | 75.1% [C] | | 73.3% LTM on H2 [C] | 73.3% [C] |
| **Adj. EBITDA** | **61.923** [A] | +53.6% | −13.891 + 66.226 = **52.335** [C] | **160.455** [S] |

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

Both factors are more than 10% from 1. The line commentary does not support the consensus total. The lines allocate it. Flagged.

An earlier build used 14.5 as the ImprimisRx quarter instead of the Q2 actual 14.556. This file uses 14.556. Recomputed.

### What each line is doing

**IHEEZO, ramping, price times volume.** "Effective July 1, 2026, IHEEZO net price per unit improved by approximately 25%." [G] Q2 unit demand was 65,477, "+34% year-over-year", and "channel inventories have normalized." [G] Volume is held at that quarter [S]: the inventory swing is treated as done, so it does not get annualized again, and no unit guide was given. FY27 units +17%, half the Q2 unit growth [S], because a launch-year unit step is a weak thing to hold for a second year. Price and volume are multiplied, then the line is scaled.

**VEVYE, ramping.** "Momentum continues to build, supported by our recent coverage win that went into effect August 1." [G] The starting default for "momentum continues" is to hold the prior growth rate. +7.5% a quarter in H2 is a larger step than that default [S], listed below. FY27 is the Q4 run rate × 4 × 1.10 [S]. May 11, 2026: "on track to deliver 2026 revenue of over $100 million." [G] The base line is 143.7, above that floor. The Q1 gross-to-net item is one-time: reported VEVYE of $20.9 million was "approximately $8 million below" what management says it would have been, and they called it non-recurring (May 11, 2026). [G] It is not in the run rate. The run rate starts at Q2.

**Other branded, new lines plus a floor.** "BYOOVIZ launched in July 2026, and the Company expects revenue to build over the balance of the year." [G] Q3 13.0 and Q4 14.5 are judgments carried from the earlier line build. The filing does not give those dollars. [S] TYRVAYA "is expected to contribute modestly to 2026 revenue" [G]; $4 million in Q4 is 1.1% of the FY26 total, inside the 1–3% starting band for "modest." [S] "More than $30 million in revenue in 2027" is the FY27 floor, used as 30 before scaling. [G] The close was October 5, 2026, "paid $30 million in cash." [G]

**ImprimisRx, mature.** Flat at the Q2 run rate [S]. FY27 then applies the FY25 decline of 8.3% [C from actuals]. No structural change was named for this segment.

## Costs

Trailing gross margin = (204.369 − 79.819 + 77.408) / (272.303 − 111.573 + 114.864) = **73.28%**. [C] Inputs are FY25 gross profit, H1 2025 gross profit, and H1 2026 gross profit, from the March 2 and August 10, 2026 releases. FY25 gross margin on the year is 204.369 / 272.303 = 75.1%; the release states 75%. Q2 gross margin is stated as 71% (50.363 / 70.661 = 71.3%).

Q2 cash operating cost = Q2 gross profit 50.363 − Q2 adjusted EBITDA (−1.232) = **51.595**. [C] This bridge is not GAAP opex. It is the cost that reconciles to the adjusted EBITDA the company guides. H1 adjusted EBITDA was −13.891. [A]

H2 cost = 2 × 51.595 + 3.0 assumed TYRVAYA stub cost = 106.190. [S on the 3.0]

H2 EBITDA = 235.280 × 73.28% − 106.190 = 66.226. FY26 EBITDA = −13.891 + 66.226 = **52.335**.

If FY26 EBITDA had been the guidance midpoint of 90, H2 operating cost would have had to be about 68.5, which is 35% below the 106.2 run rate. The gap is wider than 10%. There is no 2a EBITDA total to "keep" (no coefficient, no estimate), so the forecast keeps the cost build and shows the guide beside it. **Flag: FY26 adjusted EBITDA 52.3 versus guide $80–100 million.** This is the largest risk in the case. The sales force built in the first half is already inside the Q2 run rate; nothing further was quantified.

FY27 cost = 4 × 51.595 × 1.03 + 20 assumed TYRVAYA cost = 232.571. [S] EBITDA = 536.328 × 73.28% − 232.571 = **160.455** (29.9% margin).

That margin expansion is mostly the scale factor. Revenue was lifted 37% above the line build and operating cost was not. Management also said it expects "at least one new product every year through 2029, within its existing cost structure and commercial footprint" (August 10, 2026). [G] That sentence argues against a large organic cost step, and it is why the organic launches are not given their own opex add. It does not, by itself, justify a 30% EBITDA margin. Listed below.

The $20 million TYRVAYA cost is an assumption. The filing says 2027 revenue is "expected to exceed the incremental operating costs" and does not give the cost. [G][S]

## Scenarios

Three levers only: where in the carried consensus range the revenue total sits, the gross margin, and FY27 operating-cost inflation. The line drivers do not change. Scaling does, because the total does.

| | Revenue | Gross margin | FY27 opex inflation | FY26 rev | FY26 EBITDA | FY27 rev | FY27 EBITDA |
|---|---|---|---:|---:|---:|---:|---:|
| Bear | consensus low | 71% (Q2, as stated) | +8% | 341.0 | 40.476 | 479.0 | 97.200 (20.3%) |
| Base | consensus point | 73.3% LTM | +3% | 350.144 | 52.335 | 536.328 | 160.455 (29.9%) |
| Bull | consensus high | 75% (FY25, as stated) | 0% | 355.0 | 60.021 | 587.0 | 213.870 (36.4%) |

Bear H2 scale 1.369, FY27 scale 1.225. Bull 1.454 and 1.502. All still more than 10% from 1.

## Finagle leaves (base, organic)

TYRVAYA is not in these rates. Year 0 is already organic.

| Leaf | Value | Tag |
|---|---|---|
| `forecast.ebitda_basis` | organic | [C] |
| `forecast.ebitda_growth` | −0.1738, +1.9376 | [C] |
| `forecast.sales_growth` | +0.2649, +0.4376 | [C] |
| `me` | 0.3035 | [C] |
| `mc` | 0.5182 | [S] |
| `gsnext` | 0.20 | [S] |
| `deal_spend` | [0, 30] | [G] |

Organic dollars those rates compound: revenue 272.303 → 344.448 → 495.164; adjusted EBITDA 61.923 → 51.160 → 150.290.

`me` is FY27 organic EBITDA / FY27 organic revenue. That is the margin `forecast_ebitda` uses when sales growth reaches the last explicit year. It is not the year-0 margin (61.923 / 272.303 = 22.7%).

`mc` is the average of that ending margin and the 73.3% gross margin [S]. Finagle's filler would have averaged the year-0 margin instead. This sets the one the fade should use.

`gsnext` 20% [S]. FY25 revenue grew 36%. Launches are still described through 2029, and there is no FY28 dollar. 20% fades the FY27 step-up instead of repeating it. The fade from 20% down to terminal growth is Finagle's. `gt` is not set.

Acquisition, all seven fields: year 1 [G], deal value 30 [G], multiple 2.95 [S] (30 / FY27 TYRVAYA EBITDA of about 10.2), leverage 0 [G] (cash at close), next growth 0.15 [S], capex fraction 0.02 [S], `pay_from_cash` false [C] because that flag only touches year-0 cash and the close is in year 1. Milestones of up to $70 million are excluded [G]; they are contingent and not in the base.

Template leaves (horizon, cost of debt, tax, NOL, non-operating assets, working capital, distribution, debt policy, terminal growth) are not filled. The FY2025 10-K does say federal NOL carryforwards were about $37.124 million. That is a filing fact a person can put in the template. It is not a forecast output.

## Assumptions to revise

The moves that change the answer:

1. Revenue is the October 22, 2026 Yahoo consensus, because H1 `C` is −0.91. H2 scale is 1.42 and FY27 scale is 1.37. Replacing the consensus with the unscaled build (FY26 about 280, FY27 about 391) is the whole forecast.
2. FY26 EBITDA is the cost build, 52.3, not the $80–100 million guide. Holding H2 operating cost at 106 instead of the roughly 69 a midpoint guide would need is the largest single risk.
3. FY27 operating cost is the Q2 run rate +3% plus $20 million for TYRVAYA. The $20 million is assumed. The "existing cost structure" sentence pulls the other way for organic launches.
4. Gross margin stays at the 73.3% trailing level.
5. `gsnext` is 20%. It is a fade, not a sourced FY28.

Other judgments, each tagged `[S]` in the file: IHEEZO units flat then +17%; VEVYE +7.5% a quarter (above the "hold" default) and FY27 × 1.10; other branded Q3 13 and Q4 14.5; TYRVAYA Q4 stub of 4; ImprimisRx flat then the FY25 decline; TYRVAYA costs of 3 and 20; scenario inflation of 8% / 3% / 0%; `mc`; acquisition next growth 0.15 and capex fraction 0.02; milestones left out.

## Links

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

- The consensus dollars were not pulled again. They are the yfinance figures dated 2026-10-22 from the source note (FY26 350.144, range 341–355; FY27 536.328, range 479–587).
- No EBITDA consensus was available to carry, so none is used.
- Ceochat was not read. The public clone was not available.
- Finagle was not run. No value per share.
- Q3 13 and Q4 14.5 for other branded, the VEVYE +7.5% step, the FY27 × 1.10, the TYRVAYA costs of 3 and 20, and `gsnext` of 0.20 are assumptions. The quotes they hang on were checked; the magnitudes were not in the filings.
