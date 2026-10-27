# Copart, Inc. (NASDAQ: CPRT): forecast FY27E–FY28E

As of 2026-10-22. USD millions. Fiscal year ends July 31 (FY27 = Aug 2026–Jul 2027). Forecast only: no valuation, no Finagle. No quarter of FY27 has been reported yet (Q1 ends 2026-10-31), so there is no YTD period. Machine-readable file: `forecast.json` (passes `forecastcheck.validate`; see the period note). Every number carries a tag and a numbered source ID that resolves in the **Numbered sources** list below.

## Which reporting lines and why

Copart reports two segments, **United States** and **International**. Each segment note row shows **service revenues** and **vehicle sales** separately [A1]. We use all four cells as lines because the filings give a full history for each, and the two splits behave very differently:
- **Service revenue** is fee income on consigned cars, driven by units times fee per car.
- **Vehicle sales** is the gross price of cars Copart buys and resells. It is low margin and depends on mix.

The MD&A explains each cell's change in terms of volume, revenue per car and FX [A5][A6].

**ACV Auctions** closed on 2026-10-16 [A13] and is a fifth, acquisition-driven line. It covers 77 days of Q1 FY27 plus Q2–Q4. We show it separately from the organic Copart lines. Copart has not yet said how it will report ACV ("ACV will now operate as an independent subsidiary of Copart" [A13]).

**EBITDA definition.** Copart does not report adjusted EBITDA. We define it as operating income + D&A (excluding debt costs) + stock-based compensation [C2].
- FY26A = 1,652.6 + 229.4 + 38.8 = 1,920.8, a 41.2% margin.
- ACV's own adjusted EBITDA excludes the same items [A11].

**Gross margin** is Copart's reported gross profit, which is after facility D&A and facility SBC [A3].

## Line table (base case)

| Line | FY24A | FY25A | FY26A | FY26 YoY | Q4 FY26 YoY | FY27E | FY28E |
|---|---|---|---|---|---|---|---|
| U.S. service revenues | 3,126 [A1] | 3,452 [A1] | 3,388 [A1] | −1.8% [C1] | −0.8% [C1][A4] | 3,433 [S1][C5] | 3,707 [S1][C5] |
| U.S. vehicle sales | 338.6 [A1] | 403.5 [A1] | 419.1 [A1] | +3.9% [C1] | +10.9% [C1][A4] | 428.9 [S2][C5] | 463.0 [S2][C5] |
| International service revenues | 434.9 [A1] | 517.1 [A1] | 581.2 [A1] | +12.4% [C1] | +15.5% [C1][A4] | 629.4 [S3][C5] | 719.0 [S3][C5] |
| International vehicle sales | 337.2 [A1] | 274.8 [A1] | 277.5 [A1] | +1.0% [C1] | +4.4% [C1][A4] | 278.5 [S4][C5] | 294.8 [S4][C5] |
| ACV Auctions (from 2026-10-16) | – | – | – [A13] | – | – | 717.8 [S5][C6][C5] | 1,033 [S6][C5] |
| **Total revenue** | **4,237 [A2]** | **4,647 [A2]** | **4,666 [A2]** | +0.4% | +2.4% [A4] | **5,488 [E1]** | **6,217 [E1]** |
| Organic (ex-ACV) revenue | 4,237 | 4,647 | 4,666 | | | 4,770 [C10] | 5,183 [C10] |
| Gross margin (reported) | – | 45.2% [C7] | 44.7% [C7] | | Q4 41.8% [C7] | 45.5% [C7] | 45.7% [C7] |
| Adj. EBITDA | – | 1,951 [C2] | 1,921 [C2] | −1.5% | | 2,020 [S7][S8] | 2,247 [S7][S8] |
| of which ACV | – | – | – | | | 66.5 [S8] | 109.6 [S8] |
| Adj. EBITDA margin | – | 42.0% [C8] | 41.2% [C8] | | Q4 38.2% [C2] | 36.8% [C8] | 36.1% [C8] |

May not sum due to rounding. The FY27E and FY28E totals are consensus [E1]. The lines are our build, scaled to that total [C5]:
- FY27: the build is 0.6% above consensus, so the lines are scaled down 0.7%.
- FY28: the build is 4.0% below consensus, so the lines are scaled up 4.1%.

Neither scale is more than 10% from 1. The unscaled build is a diagnostic only.

## Drivers by line

### U.S. service revenues (73% of FY26 revenue). Pattern: mature
- **Pattern.** Revenue was 3,126 in FY24, 3,452 in FY25 and 3,388 in FY26 [A1]. FY25 was inflated by hurricanes Helene and Milton. FY26 fell 1.8%, and Q4 FY26 fell 0.8% YoY [A4].
- **Volume.** Units fell in FY26. Insurance sellers supplied 79% of units processed in FY26, vs. 81% in FY25 [A9]. The long-term volume driver is total loss frequency [A8]. Catastrophe volume is lumpy: FY25 included "one-time revenue associated with hurricanes Helene and Milton" [A5]. We assume no major catastrophe in FY27. Winter seasonality adds 5–20% to volumes [A10].
- **Price/mix.** "Increase in revenue per car" offset part of the volume decline [A5]. Fees are partly percentage-of-ASP: "a significant amount of our service revenue is associated in some manner with the ultimate selling price of the vehicle" [A8]. ASP depends on used-car prices, scrap prices and FX for international buyers [A8].
- **Supporting quotes.**
  - "The decrease in service revenue in the U.S. was primarily related to the one-time revenue associated with hurricanes Helene and Milton recognized in fiscal year 2025 and a decrease in volume offset by an increase in revenue per car." [A5]
  - "We believe the long-term trend of increases in total loss frequency will continue." [A8]
- **Call.** +2% in FY27 [S1]. This is a flat-to-slightly-lower unit base, with low-single-digit revenue-per-car gains and no catastrophe. It cycles a clean FY26 base, since FY26 had no hurricane revenue. +3% in FY28 [S1]. Both are before the consensus scale.
- **What would change it.**
  - A major hurricane season in Aug–Oct 2026 or 2027 would add revenue (bull). Helene/Milton revenue was not quantified in the 10-K text we read; see the questions.
  - Units could keep falling as insurance share drops (79% from 81%) or as policy lapses and higher deductibles cut claims.
  - Used-car prices could fall, which lowers ASP and fee per car.
  - If units are reported in the Q1 FY27 10-Q (December 2026), we would re-base.

### U.S. vehicle sales (9%). Pattern: mature, mix-driven
- **Pattern.** Revenue was 338.6, 403.5 and 419.1 for FY24–FY26 (+3.9% in FY26) [A1]. Q4 grew 10.9% [A4].
- **Volume and price/mix.** "Primarily driven by an increase in revenue per car, which was due to a change in mix of vehicles sold, which was offset by a decrease in volume" [A6]. These are cars Copart owns. Cost of vehicle sales rose in step ("change in the mix of vehicles sold, offset by a decrease in volume" [A12]), so the line adds little gross profit. FY26 U.S. vehicle sales were 419.1 vs. cost of 391.0 [A1].
- **Call.** +3% a year [S2], below Q4's pace because mix gains are not durable.
- **What would change it.** A shift of sellers between purchase and consignment programs, or an ASP move. EBITDA impact is small either way.

### International service revenues (12%). Pattern: ramping (share gain abroad)
- **Pattern.** Revenue was 434.9, 517.1 and 581.2 (+12.4% in FY26). Q4 grew 15.5% [A1][A4]. FX added 21.9 in FY26, so the line grew about 8% ex-FX [A5].
- **Volume and price/mix.** "Driven primarily by an increase in revenue per car and increase in volume" [A5]. Sellers are switching to consignment: International vehicle-sales volume fell "related to sellers switching to a consignment model" [A6]. That move shifts revenue from vehicle sales to service fees.
- **Call.** +9% a year [S3]. This is roughly the ex-FX rate plus the consignment shift, with no further FX help assumed.
- **What would change it.** A stronger USD (FX was 21.9 of the 64.1 increase), the pace of the UK/Germany/Brazil consignment shift, and new-country rollouts.

### International vehicle sales (6%). Pattern: mature/declining, mix-driven
- **Pattern.** Revenue was 337.2, 274.8 and 277.5. Q4 grew 4.4% [A1][A4].
- **Volume and price/mix.** Higher revenue per car from mix was offset by lower volume as sellers switched to consignment. FX helped by 12.1 [A6].
- **Call.** +1% a year [S4].
- **What would change it.** A faster consignment shift would lower this line and raise International service revenue, a net gain in margin.

### ACV Auctions. Pattern: acquisition-driven (organic and deal shown separately)
- **Pattern.**
  - ACV revenue was 358, 422, 481, 637 and 760 for 2021–2025 [A15].
  - H1 CY26 revenue was 418.1, with adjusted EBITDA of 37.9 [A11].
  - CY26 guidance (pre-close) was revenue 845–855 and adjusted EBITDA 73–77 [G1]. Q3 CY26 guidance was 219–225 and 21–24 [G2].
- **Volume and price/mix.**
  - Q2 CY26 Marketplace Units were 211,472, "approximately flat year over year". Revenue grew 10% on Marketplace Services take-up [A11].
  - Growth comes from fee per unit and wallet share rather than units ("market share gains in dealer wholesale and strong adoption of our Marketplace Services" [A11]).
- **Build.**
  - Implied Q4 CY26 revenue is 209.9 and EBITDA 14.6 [C6].
  - The FY27 stub takes 77/92 of Q4 CY26 plus 7/12 of CY27 consensus 937.5 [E2]. That gives 722.5 before scale and 717.8 after [S5].
  - FY28 is 5/12 of CY27 plus 7/12 of CY27 × 1.10, giving 992.2 before scale and 1,033 after [S6].
  - EBITDA: the stub is at the guided Q4 margin (7.0%), then 10% in CY27 and 11% in CY28 [S8].
  - No synergies are in the base case. Copart says only "meaningful expected near-term cost synergies and revenue synergies" and gives no figure [G3].
- **Supporting quotes.**
  - "Expected to be neutral on EPS in the first full year of ownership and accretive in FY2028 and beyond" [G3].
  - "Transaction expected to accelerate revenue growth" [G3].
- **What would change it.**
  - Copart could quantify synergies.
  - Purchase accounting could change ACV's revenue recognition, for example gross vs. net customer assurance.
  - Integration costs could appear; we treat them as one-time and exclude them.
  - A dealer-wholesale downturn would hurt ACV volumes.
  - The seasonality split of CY27 (we use straight 7/12) could differ.
  - Yahoo's ACVA CY27 consensus [E2] may be stale after delisting.

### Costs → EBITDA
- **Organic.** We apply the trailing FY26 cash gross margin (gross profit plus facility D&A and SBC) of 49.2% [C3], then subtract G&A excluding D&A and SBC [C4].
  - G&A is held at the Q4 FY26 run rate of 4 × 97.8 = 391.3 in FY27, then grows 5% in FY28 (FY26 G&A grew 7.0% [A7b]) [S7].
  - Organic EBITDA is 1,954 in FY27 (41.0%) and 2,138 in FY28 (41.2%).
- **Recurring vs one-time.**
  - FY25 hurricane costs and revenue were one-time [A5][A7]. FY26 is a clean base.
  - The 20M-share CEO option granted on 2026-10-14 [A14] adds SBC but is excluded from adjusted EBITDA (recurring non-cash; flagged).
  - ACV deal costs are one-time and excluded.
- **Margin trend.** Q4 FY26 cash gross margin was 46.6% vs. 49.2% for the year [C3]. Q4 FY26 adjusted EBITDA margin was 38.2% vs. 42.2% in Q4 FY25 [C2]. If that persists, the bear case applies.

## Scenarios (scenario table)

| | Bear FY27E | Base FY27E | Bull FY27E | Bear FY28E | Base FY28E | Bull FY28E |
|---|---|---|---|---|---|---|
| Revenue [E1] | 5,404 | 5,488 | 5,571 | 6,057 | 6,217 | 6,320 |
| of which ACV [S5][S6] | 706.8 | 717.8 | 728.7 | 1,007 | 1,033 | 1,050 |
| Gross margin [C7] | 43.0% | 45.5% | 45.9% | 43.3% | 45.7% | 46.1% |
| Adj. EBITDA [S7][S8] | 1,842 | 2,020 | 2,078 | 2,011 | 2,247 | 2,333 |
| EBITDA margin [C8] | 34.1% | 36.8% | 37.3% | 33.2% | 36.1% | 36.9% |

- **Bear:** consensus low [E1]; Q4 FY26 cash gross margin of 46.6% [C3]; G&A 3% above the run rate, then +7%; ACV margin 8%/9%.
- **Bull:** consensus high [E1]; FY25 cash gross margin of 49.5% [C3]; G&A flat at the run rate, then +3%; ACV margin 11%/13%, a proxy for synergies.

## Verified vs assumed
- **Verified** (A/G/E, quote-checked against EDGAR text or the yfinance pull):
  - all FY24–FY26 and Q4 line and total figures, gross profit, D&A, SBC and G&A
  - ACV H1 CY26 and its guidance
  - deal terms, close date and the CEO option
  - consensus
- **Assumed** (S): all line growth rates, the ACV stub, CY28 growth and margins, the G&A path, the scenario margins, the no-catastrophe assumption and gsnext.
- **Calculated** (C): EBITDA definition, margins, scale factors and the ACV implied Q4.
- **Not verified:**
  - Page numbers (all HTML, "page unverified").
  - Whether the CPRT consensus includes ACV. It almost certainly does: +17.6% FY27 growth vs. +0.4% FY26, but the number of analysts who have updated is unknown.
  - ACVA consensus freshness.
  - Unit counts. Copart does not disclose units in the 10-K text we searched beyond "more than 4 million units in the last year" [A16].

## Questions for David
1. Copart does not define adjusted EBITDA. Is operating income + D&A + SBC acceptable, or do you want SBC left in (EBITDA = 1,881.96 in FY26)?
2. Should ACV be modelled from Yahoo's ACVA CY27 consensus (possibly stale post-delisting), or held at CY26 guidance plus ~10%?
3. Should the base include ACV synergies once Copart quantifies them (none disclosed yet)?
4. Should we add a catastrophe overlay (e.g., a Helene/Milton-sized event) to the bull case? Copart's FY25 10-Qs quantified it; we did not pull them.
5. The FY28 consensus sits 4% above our build. Should the scale be applied to the organic lines only, leaving ACV unscaled?

## Suggested repo method changes
1. `validate.py` hard-codes `DOLLAR_PERIODS = {FY24A, FY25A, H1A, H2E, FY26E, FY27E}` and `_compounds` uses FY25A as the baseline. For a July fiscal year with FY26A actual and FY27E/FY28E forecasts, FY26A/FY28E sums and compounding go unchecked. Derive dollar periods from `baseline_period` + `explicit_periods` (anything not containing "YoY"/"growth"). For now `build_forecast.py` self-checks this.
2. Add an "acquired line" convention to the skill: a `organic.acquired` block, stub-period day counts, and a rule on whether consensus scaling applies to the acquired line.
3. Add an "EBITDA not reported by the company" rule: state the definition as a C-tag and keep it consistent with the target's adjusted EBITDA.
4. Add catastrophe/one-time revenue to the run-rate classification table (insurance-auction businesses).
5. Allow a `pattern` field on each line in the json (used here) and validate it against the skill's pattern list.

## Numbered sources

**Documents**
- **D1** Copart, Form 10-K for FY ended 2026-07-31, filed 2026-09-29: https://www.sec.gov/Archives/edgar/data/900075/000119312526405731/cprt-20260731.htm (HTML; no page numbers)
- **D2** Copart, Q4 FY2026 earnings release (8-K Ex. 99.1), 2026-09-10: https://www.sec.gov/Archives/edgar/data/900075/000119312526387902/cprt-ex99_1.htm (HTML)
- **D3** Copart, ACV merger press release (8-K Ex. 99.1), 2026-09-10: https://www.sec.gov/Archives/edgar/data/900075/000119312526388064/d138322dex991.htm (HTML)
- **D4** Copart, ACV investor presentation (8-K Ex. 99.2), 2026-09-10: https://www.sec.gov/Archives/edgar/data/900075/000119312526388064/d138322dex992.htm (HTML; slide numbers unverified)
- **D5** Copart, ACV tender completion release (8-K Ex. 99.1), 2026-10-16: https://www.sec.gov/Archives/edgar/data/900075/000119312526423478/d129535dex991.htm (HTML)
- **D6** Copart, 8-K Item 5.02 (CEO option, event 2026-10-14), filed 2026-10-16: https://www.sec.gov/Archives/edgar/data/900075/000119312526424052/d177727d8k.htm (HTML)
- **D7** ACV Auctions, Q2 2026 earnings release (8-K Ex.), 2026-08-06: https://www.sec.gov/Archives/edgar/data/1637873/000163787326000031/q2-26earningspressrelease.htm (HTML)
- **D8** Yahoo Finance / yfinance, CPRT analysis, pulled 2026-10-22: https://finance.yahoo.com/quote/CPRT/analysis/
- **D9** Yahoo Finance / yfinance, ACVA analysis, pulled 2026-10-22: https://finance.yahoo.com/quote/ACVA/analysis/

**Actuals**
- **A1** Segment table, D1 (page unverified): U.S. / International, $000. FY2026 service revenues 3,388,287 / 581,233 and vehicle sales 419,143 / 277,546. FY2025: 3,451,558 / 517,104 and 403,546 / 274,750. FY2024: 3,126,102 / 434,900 and 338,633 / 337,188. "Depreciation and amortization, excluding debt costs" 194,749 / 34,624 (FY26) and 184,026 / 31,823 (FY25). U.S. vehicle sales 419,143 vs. cost of vehicle sales 391,028.
- **A2** Consolidated statements of income, D1 (page unverified): "Total service revenues and vehicle sales 4,666,209 | 4,646,958 | 4,236,823"; "Operating income 1,652,590 | 1,696,714 | 1,572,023".
- **A3** D2 income statement (page unverified):
  - FY26 / FY25: "Gross profit 2,083,858 | 2,099,643"; "Facility depreciation and amortization 201,669 | 191,775"; "Facility stock-based compensation 8,472 | 8,107"; "General and administrative 373,218 | 348,958" (ex D&A and SBC).
  - Q4 FY26: gross profit 481,449, facility D&A 53,759, facility SBC 2,275, G&A 97,813, G&A D&A 7,202, G&A SBC 7,530, operating income 368,904, revenue 1,152,439.
  - Cash flow: "Stock-based compensation 38,818 | 38,004".
- **A4** D2 three-month segment table (page unverified): Q4 FY26 vs. Q4 FY25, U.S. service 817,822 vs. 824,813; U.S. vehicle sales 112,512 vs. 101,450; International service 151,722 vs. 131,396; International vehicle sales 70,383 vs. 67,438.
- **A5** D1 MD&A (page unverified): "The increase in service revenues for fiscal 2026 of $0.9 million, or 0.0 % as compared to fiscal 2025 came from (i) a decrease in the U.S. of $(63.3) million, and (ii) an increase in International of $64.1 million. The decrease in service revenue in the U.S. was primarily related to the one-time revenue associated with hurricanes Helene and Milton recognized in fiscal year 2025 and a decrease in volume offset by an increase in revenue per car. The growth in International, after excluding positive fluctuations in currency exchange rates of $21.9 million, was driven primarily by an increase in revenue per car and increase in volume."
- **A6** D1 MD&A (page unverified): "The increase in the U.S. was primarily driven by an increase in revenue per car, which was due to a change in mix of vehicles sold, which was offset by a decrease in volume. The increase in International, after excluding positive fluctuations in currency exchange rates of $12.1 million was primarily driven by an increase in revenue per car, which was due to a change in mix of vehicles sold, which was offset by a decrease in volume related to sellers switching to a consignment model."
- **A7** D1 MD&A (page unverified): "The decrease in the U.S. compared to the same period last year was related to one-time costs associated with hurricanes Helene and Milton recognized in fiscal year 2025..." **A7b**: "The increase in general and administrative expenses for fiscal 2026 of $28.3 million, or 7.0% as compared to fiscal 2025..."
- **A8** D1 MD&A overview (page unverified): "Our revenue is impacted by several factors, including total loss frequency and the average vehicle auction selling price, as a significant amount of our service revenue is associated in some manner with the ultimate selling price of the vehicle... We believe the long-term trend of increases in total loss frequency will continue."
- **A9** D1 Item 1 (page unverified): "We obtained 79%, 81%, and 81% of the total number of vehicles processed during fiscal 2026, 2025, and 2024, respectively, from insurance company sellers."
- **A10** D1 Liquidity (page unverified): "During the winter months, most of our facilities process 5% to 20% more vehicles than at other times of the year."
- **A11** D7: "Second quarter revenue of $214 million"; "Marketplace Units of 211,472, approximately flat year over year"; six months total revenue 418,133; Adjusted EBITDA (six months) 37,868; cost of revenue excl. D&A 165,324 + 40,702; "market share gains in dealer wholesale and strong adoption of our Marketplace Services". The Adjusted EBITDA definition excludes "depreciation and amortization; stock-based compensation expense..."
- **A12** D1 MD&A (page unverified): "The increase in the U.S. was primarily the result of a change in the mix of vehicles sold, offset by a decrease in volume." (cost of vehicle sales)
- **A13** D5: tender expired 2026-10-15 with 116,818,409 shares tendered; "ACV will now operate as an independent subsidiary of Copart".
- **A14** D6: "approved the grant to A. Jayson Adair, the Company's Chief Executive Officer ("CEO"), of a nonstatutory stock option to purchase 20,000,000 shares", in tranches at $26.27/$35.03/$43.78/$52.54, with 5-year cliff vesting.
- **A15** D4 (slide unverified): ACV revenue chart "$358 $422 $481 $637 $760" (2021A–2025A, $M; year labels read from the chart, unverified).
- **A16** D2: "Copart sold more than 4 million units in the last year."
- **A18** D1 notes (page unverified): "On October 6, 2023, the Company acquired an 80% controlling ownership in Purple Wave... equal to the $108.0 million acquisition price".
- **A19** D1 exhibit list (page unverified): "Transition and Separation Agreement and General Release, dated June 25, 2026, by and between the Company and Jeffrey Liaw".
- **A17** D3: "$10.50 per share in cash, representing an implied equity value of approximately $1.9 billion".

**Guidance and management statements**
- **G1** D7: "Reaffirms 2026 revenue guidance of $845 million to $855 million and Adjusted EBITDA of $73 million to $77 million" (ACV, pre-close).
- **G2** D7: "Third Quarter of 2026: Total revenue of $219 million to $225 million... Adjusted EBITDA of $21 million to $24 million".
- **G3** D3/D4: "expected to be neutral on Copart's earnings per share in the first full year of ownership and accretive in fiscal 2028 and beyond"; "Transaction expected to accelerate revenue growth"; "Meaningful expected near-term cost synergies and revenue synergies across dealer, commercial, and retail channels". No synergy figure is given. Copart itself gives no revenue or EBITDA guidance.

**Estimates**
- **E1** D8, revenue_estimate: FY27 ('0y') average 5,487.76, low 5,403.78, high 5,571.00 (yearAgoRevenue 4,666.21 confirms the fiscal-year mapping); FY28 ('+1y') average 6,216.54, low 6,056.78, high 6,319.85. Q1 FY27 average 1,188.88. No EBITDA consensus is available.
- **E2** D9: ACVA CY2027 ('+1y') revenue average 937.51 (CY26 847.60). This may be stale after the delisting.

**Assumptions** (reasoning + quote)
- **S1** U.S. service +2% FY27, +3% FY28. Clean post-hurricane base, slight volume decline offset by revenue per car (A5, A8), no catastrophe.
- **S2** U.S. vehicle sales +3%/yr. Mix-driven (A6); below Q4's +10.9% (A4).
- **S3** International service +9%/yr. About 8% ex-FX in FY26 (A5) plus the consignment shift (A6).
- **S4** International vehicle sales +1%/yr. Consignment shift offsets mix (A6).
- **S5** ACV FY27 = 209.9 × 77/92 + 937.5 × 7/12 = 722.5 before scale (C6, E2; close date A13).
- **S6** ACV FY28 = 937.5 × 5/12 + 937.5 × 1.10 × 7/12 = 992.2 before scale. CY28 +10% is about ACV's guided CY26 growth (G1: "increase of 11% to 13%").
- **S7** Organic EBITDA = cash GM (C3) × organic revenue − G&A (C4). G&A is flat in FY27 and +5% in FY28 (A7b +7.0% in FY26). Bear: +3%/+7%. Bull: 0%/+3%.
- **S8** ACV adjusted EBITDA: stub at the Q4 CY26 implied margin of 7.0% (C6), then 10% in CY27 and 11% in CY28 (base), 8%/9% (bear) and 11%/13% (bull). CY26 guided margin is 8.8% (G1); synergies are unquantified (G3).
- **S9** gsnext 5%: organic growth after FY28, mid-single digit, consistent with the FY24–26 organic CAGR of 5.0% (A2).
- **S10** mc = average of me and organic reported GM.

**Calculations**
- **C1** YoY = period / prior period − 1 (A1, A4).
- **C2** Adjusted EBITDA = operating income (A2) + D&A excl. debt costs (A1) + SBC (A3). FY26 1,920.78; FY25 1,950.57; Q4 FY26 = 368.9 + 53.8 + 7.2 + 2.3 + 7.5 = 439.7 (38.2%); Q4 FY25 475.3 (42.2%).
- **C3** Cash gross margin = (gross profit + facility D&A + facility SBC) / revenue (A3): FY26 49.16%, FY25 49.48%, Q4 FY26 46.64%.
- **C4** G&A run rate = 4 × 97.813 = 391.25 (A3).
- **C5** Scale = E1 / (sum of unscaled Copart lines S1–S4 + ACV S5/S6). FY27 5,487.76 / 5,524.17 = 0.9934; FY28 6,216.54 / 5,970.29 = 1.0412.
- **C6** ACV Q4 CY26 = G1 mid 850 − A11 418.13 − G2 mid 222 = 209.87; EBITDA 75 − 37.87 − 22.5 = 14.63.
- **C7** Gross margin = gross profit / revenue (A3); forecast = organic revenue × case organic GM (FY26 44.66%, Q4 41.78%, FY25 45.18%) + ACV × C9.
- **C8** EBITDA margin = EBITDA / revenue.
- **C9** ACV gross margin = 1 − (165.32 + 40.70) / 418.13 = 50.7% (A11). Cost excludes D&A, so it is not like-for-like with Copart's GM (flag).
- **C10** Organic revenue = sum of the four Copart lines after scale.
- **C11** Organic growth series (finagle leaves): sales +2.2%, +8.7%; EBITDA +1.7%, +9.4%.
- **C12** me = FY28 organic EBITDA / revenue = 41.24%.

**Not verified**
- All page numbers (HTML filings): page unverified.
- A15 chart year labels; E2 freshness; whether all E1 contributors include ACV.
- CEO history beyond the 10-K signatures and the June 25, 2026 Liaw transition agreement (D1 exhibit list).
