## 7. Valuation

Finagle values the base case at $148.50 per share vs. a $28.30 share price on 14 November 2026, about 425% above (derived) [C25][A24][C24]. About 42% of that equity value is the terminal value (derived) [C24]. The bull is $176.82 and the bear $81.72 per share; their inputs, bridges and year rows are in Appendix A [C25].

### Method

Finagle discounts free cash flow to equity at the cost of equity [D24][S45]. It takes the explicit revenue and Adjusted EBITDA for FY2026E–FY2032E from the forecast file as given, compounding from FY2025A [C18]. That is seven explicit years, and Finagle extends them by three more, FY2033E–FY2035E, to a ten-year horizon [C25]. In those extra years, revenue starts from next-period growth of 11.5% and fades toward terminal growth, and EBITDA moves from the 54.9% starting margin with each extra dollar of revenue earning the 65.4% incremental margin [S43][S44][C25]. A terminal value is added at the end of FY2035E [C25]. Terminal growth is Finagle's default of 5.10%, the 10-year Treasury yield on the run date; it was not set or overridden by us [S45][A24]. Year-0 cash after the cash schedule is negative, so Finagle's FY2026E free cash flow to equity is an implied equity inflow of $41.5 that brings balance-sheet cash to zero, and no equity is issued to fill the gap [P9][C25].

### Balance Sheet Adjustments

Year-0 cash of −$41.5 and the share count of 37.23 million equal the opening $72.9 of cash and 37.23 million shares at 31 December 2025 plus the present values below and no new shares [A21][P5][C25]. The stated cash and shares do not already include these items, so the cash items are added once [C25]. No equity was sold for cash in 2026 through 14 November, and this run does not add a year-0 equity raise in any case [A22][P5][P9]. These dollars are outside EBITDA and are not in a later cash-flow year [S12][C19]. The TYRVAYA close cash is already paid, so its discount is 1 [C19].

<div class="fig" markdown="1">

**Balance Sheet Adjustments – base case (US$ millions unless noted)**

| Item | Amount | Timing | Probability | Discount | Present value | Shares issued (millions) |
|---|---:|---|---:|---:|---:|---:|
| TYRVAYA close cash paid | -30.00 | 2026-10-01 | 1.00 | 1.0000 | -30.00 | 0.0000 |
| Melt FDA-approval milestone payable | -87.17 | 2027-12-31 | 1.00 | 0.8925 | -77.80 | 0.0000 |
| Melt first commercial Annual Net Sales cash milestone | -10.02 | 2030-12-31 | 1.00 | 0.6596 | -6.61 | 0.0000 |
| **Total present value / new shares** | | | | | **-114.41** | **0.0000** |
| Opening cash / shares (31 Dec 2025) | | | | | 72.927 | 37.229159 |
| **Year-0 cash / shares used** | | | | | **-41.48** | **37.229159** |

*Source: worked schedule in the valuation result [D24][C25]; items from the forecast file [A23][A15][A18][S24][S25][S34][S35][C19][P9]; opening cash and shares [A21][P5]. Discount is at the 10.60% cost of equity from the 14 November 2026 price date. May not sum due to rounding.*

</div>

Figure 8 shows which inputs are Finagle defaults, which come from the forecast file, and which are our judgments; the judgments are the starting margin, incremental margin and next-period growth, while the rates and the debt policy are Finagle's defaults.

<div class="fig" markdown="1">

**Figure 8 – Valuation inputs, base case**

| Input | Base | Basis | Tags |
|---|---:|---|---|
| Cost of equity | 10.60% | Finagle default: 5.5% plus the 10-year yield | [S45][A24] |
| Cost of debt | 9.67% | Finagle default: year-0 interest of $24.2 divided by year-0 debt | [S45][D24] |
| Tax rate | 21.0% | Finagle default: U.S. federal statutory rate | [S45] |
| Terminal growth | 5.10% | Finagle default: equals the 10-year yield; not set by us | [S45][A24] |
| Terminal return on invested capital | 15.0% | Finagle default | [S45] |
| Shares (adjusted, millions) | 37.23 | Forecast-file input: 37.23 million at 31 Dec 2025; no new shares | [A21][P5][P9][C25] |
| Price (US$) | 28.30 | Fetched: previous close, 14 Nov 2026 | [A24] |
| Debt (year 0) | 250.0 | Fetched from the FY2025 10-K | [D24][C25] |
| Debt policy | 4.0x | Finagle default: year-0 Debt/EBITDA held as a target from FY2026E | [S45] |
| Cash (adjusted, year 0) | -41.48 | Forecast-file input plus the cash schedule; left negative | [A21][P5][P9][C25] |
| Starting margin | 54.9% | Forecast-file input: FY2032E Adj. EBITDA / revenue | [C18] |
| Incremental margin (mc) | 65.4% | Judgment | [S43] |
| Next-period growth (gsnext) | 11.5% | Judgment: one more year of the same build | [S44] |
| Terminal WACC | 9.26% | Finagle output | [C25] |

*Source: valuation result [D24][C25]; forecast file [C18][S43][S44][P5][P9]; fetched market data [A24]. Finagle defaults are listed in [S45].*

</div>

We set the incremental margin halfway between the FY2032E Adjusted EBITDA margin of 54.9% and that year's GAAP gross margin of 76.0%, because an extra dollar of revenue carries the product gross margin less some selling and variable cost [S43]. That 65.4% sits well above the reported history of low-20s Adjusted EBITDA margins, so it extends the long-window margin flag in the Forecast section into Finagle's extra years [S43][A3]. We set next-period growth as one more year of the same build: VEVYE continues the workbook through December 2033, IHEEZO and TRIESENCE add the same units again, G-MELT and YOCHIL take one more price step, and the Other branded components and compounding take their last steps [S44].

*Run record.* The prompt inputs are opening cash of $72.9 and 37,229,159 shares at 31 December 2025, applied to all three cases under David May's 2 November 2026 instruction, which reads: “year-0 cash is the last fiscal year-end cash plus short-term investments (e.g., FY2025), adjusted for equity raises made during the following year, and the share count is raised from the last fiscal-year figure to reflect those raises” [P5][A21]. The 14 November 2026 instruction removes every year-0 equity raise, including where cash would otherwise go negative [P9]. The VEVYE path is the workbook instruction of the same date [P8]. The 12 November 2026 request was “update the report as needed and run the finagle too” [P7]. Finagle filled defaults for net operating losses (zero), non-operating assets (zero), the cost of equity, terminal growth, terminal return on invested capital, the tax rate, the cost of debt, working capital (no change), the debt policy (target leverage from the first forecast year), and distributions (none) [S45][D24]. Every case carries the sanity flag “negative cash” [D24]. Each case has two validation warnings: “average EBITDA growth is 76.7% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero” (78.5% in the bull and 66.8% in the bear), and “forecast evidence mentions acquisitions but the case has none, so MnA stays zero” [D24]. Fetched market inputs were a $28.30 previous close and a 5.103% 10-year yield, both on 14 November 2026, and 37,229,705 shares from the 10-K, which the stated 37,229,159 replaces [A24][D24]. The run used Finagle commit 377f177b4013e713fe7c4603962e5f883a67e298 [D24]. For the base case, the warnings mean only that no purchase price is deducted: TYRVAYA is already inside the revenue and cost lines, its $30 close cash is on the cash schedule, and the high average growth is the FY2027E rebound from a low FY2026E base, not acquired EBITDA [C20][C19][C18]. The negative-cash flag is the adjusted year-0 cash of −$41.5, and it is left in place [P9][C25].

### Medium-term organic growth

Next-period growth is the medium-term organic growth forecast [S44]. The starting margin is FY2032E Adjusted EBITDA divided by revenue, 54.9% [C18]. The incremental margin is the contribution margin, set at 65.4%, and it did not move for the pipeline [S43]. The medium-term organic growth forecast of 11.5% is FY2033E from one more year of the same line build, with VEVYE extended on the workbook [S44][P8]. Figure 8a shows that VEVYE supplies about 62% of the $200 increase (derived) [S44][C26].

<div class="fig" markdown="1">

**Figure 8a – Medium-term organic growth, base case (US$ millions)**

| Line | FY2032E | FY2033E | Change |
|---|---:|---:|---:|
| VEVYE | 856 | 980 | 124.8 |
| IHEEZO | 201 | 218 | 17.0 |
| TRIESENCE | 296 | 340 | 43.2 |
| Other branded | 130 | 136 | 5.5 |
| Other revenues | 0.5 | 0.5 | 0.0 |
| ImprimisRx | 77.0 | 79.0 | 2.0 |
| G-MELT | 146 | 150 | 3.8 |
| YOCHIL | 32.2 | 35.8 | 3.6 |
| Continued path (none beyond the lines) | — | — | — |
| **Total revenue** | **1,739** | **1,939** | **199.8** |
| Growth (derived) | | | 11.5% |

*Source: FY2032E lines [C10][C12][C16][S21][S22][S23]; FY2033E next-year build [S44]; growth (derived) [C26]. G-MELT and YOCHIL FY2033E use a $200 net price per unit [S44]. May not sum due to rounding.*

</div>

Figure 9 shows that the present value of the ten forecast years supplies the larger part of the equity value, with the terminal value at about 42% (derived) [C24].

<div class="fig" markdown="1">

**Figure 9 – Value bridge, base case (US$ millions unless noted)**

| | Base |
|---|---:|
| PV of free cash flow to equity, FY2026E–FY2035E (derived) | 3,245 |
| PV of terminal value (derived) | 2,325 |
| Terminal value share of equity value (derived) | 41.7% |
| Firm value (Finagle) | 5,820 |
| Less year-0 debt | 250.0 |
| Equity value (Finagle) | 5,570 |
| Adjusted year-0 cash (not added again) | -41.48 |
| Shares (millions) | 37.23 |
| **Value per share (US$)** | **148.50** |
| Share price (US$, 14 Nov 2026) | 28.30 |
| Upside (derived) | 425% |

*Source: valuation result [D24][C25]; PV split, terminal share and upside (derived) [C24]; price [A24]. The PV split discounts Finagle's yearly free cash flow to equity and its terminal value (terminal cash flow of $350 divided by the cost of equity less terminal growth) at the 10.60% cost of equity; the two parts sum to Finagle's equity value. Adjusted year-0 cash is already the opening cash Finagle uses and is not added on top of equity. May not sum due to rounding.*

</div>

Figures 9a and 9b are the whole base-case Finagle statement, FY2025A through FY2035E; the value per share of $148.50 is the result for the case and is not a row in the statement [C25]. Two rows need a note. The debt row follows Finagle's default target of 4.0x Debt/EBITDA, so debt rises with EBITDA and the new borrowing is paid out in free cash flow to equity from FY2027E [S45][C25]. The cash row accumulates that free cash flow to equity because no distribution is set, while balance-sheet cash is zero after FY2026E; FY2025A cash is the adjusted −$41.5, and Finagle's values are printed as output and not corrected [C25]. Capex is Finagle's own reinvestment rule, not a forecast-file input; Harrow's nine-month 2026 capex was $1.06 [A6][C25]. The result file does not carry the SBC, interest, pre-tax income, NOL, cash tax, working-capital, EV, FCF-per-share or WACC rows of Finagle's report sheet, so they are not reproduced [D24].

<div class="fig" markdown="1">

**Figure 9a – Finagle base-case statement, FY2025A–FY2030E (US$ millions unless noted)**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|---:|
| Revenue | 272 | 345 | 634 | 852 | 1,077 | 1,310 |
| EBITDA | 61.9 | 40.6 | 193 | 335 | 498 | 659 |
| Capex | 0.9 | 15.2 | 72.1 | 115 | 159 | 205 |
| M&A | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Debt change | 0.0 | 48.4 | 481 | 574 | 656 | 652 |
| FCF | 20.6 | -7.0 | 39.3 | 48.9 | 66.7 | 75.8 |
| FCFE | 20.6 | 41.5 | 520 | 623 | 723 | 728 |
| FCFF | 39.7 | 12.1 | 62.2 | 108 | 170 | 229 |
| Debt | 250 | 298 | 779 | 1,353 | 2,009 | 2,661 |
| Cash (cumulative retained FCFE) | -41.5 | 0.0 | 520 | 1,143 | 1,865 | 2,594 |
| Balance-sheet cash | -41.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Shares (millions) | 37.23 | 37.23 | 37.23 | 37.23 | 37.23 | 37.23 |
| Dividend per share (US$) | 0.55 | 1.11 | 13.97 | 16.72 | 19.41 | 19.56 |
| Equity value | 5,570 | 6,119 | 6,248 | 6,288 | 6,232 | 6,164 |
| Firm value | 5,820 | 6,418 | 7,027 | 7,640 | 8,241 | 8,825 |

*Source: valuation result [D24][C25]. FY2025A is year 0. Revenue and EBITDA through FY2032E are the forecast file [C18]. May not sum due to rounding.*

</div>

<div class="fig" markdown="1">

**Figure 9b – Finagle base-case statement, FY2031E–FY2035E (US$ millions unless noted)**

| | FY2031E | FY2032E | FY2033E | FY2034E | FY2035E |
|---|---:|---:|---:|---:|---:|
| Revenue | 1,549 | 1,739 | 1,939 | 2,120 | 2,274 |
| EBITDA | 825 | 955 | 1,086 | 1,204 | 1,305 |
| Capex | 253 | 290 | 329 | 365 | 395 |
| M&A | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Debt change | 669 | 526 | 528 | 479 | 405 |
| FCF | 86.8 | 83.1 | 88.9 | 90.3 | 89.0 |
| FCFE | 756 | 609 | 617 | 570 | 494 |
| FCFF | 290 | 338 | 384 | 425 | 461 |
| Debt | 3,330 | 3,856 | 4,383 | 4,863 | 5,268 |
| Cash (cumulative retained FCFE) | 3,349 | 3,958 | 4,575 | 5,144 | 5,638 |
| Balance-sheet cash | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Shares (millions) | 37.23 | 37.23 | 37.23 | 37.23 | 37.23 |
| Dividend per share (US$) | 20.30 | 16.35 | 16.56 | 15.30 | 13.27 |
| Equity value | 6,062 | 6,096 | 6,126 | 6,206 | 6,370 |
| Firm value | 9,392 | 9,952 | 10,509 | 11,069 | 11,638 |

*Source: valuation result [D24][C25]. FY2033E–FY2035E are Finagle's extension from the starting margin, incremental margin and next-period growth [S43][S44]. May not sum due to rounding.*

</div>

Figure 13 shows a wide spread: every case is above the share price, and the bear is the lowest because it freezes VEVYE share after December 2028, delays G-MELT, and gives YOCHIL no revenue in the window, so FY2032E Adjusted EBITDA is $537 against $955 in the base [C25][A24][C14].

<div class="fig" markdown="1">

**Figure 13 – Scenarios vs. price**

| | Bear | Base | Bull |
|---|---:|---:|---:|
| Value per share (US$) | 81.72 | 148.50 | 176.82 |
| Share price (US$, 14 Nov 2026) | 28.30 | 28.30 | 28.30 |
| vs. price (derived) | 189% | 425% | 525% |
| FY2032E Adj. EBITDA | 537 | 955 | 1,109 |

*Source: valuation result [D24][C25]; price [A24]; vs. price (derived) [C24]; EBITDA from the forecast file scenarios [C14][S42].*

</div>

### Caveats

Finagle's default debt policy is the largest input we did not choose. It holds year-0 Debt/EBITDA of 4.0x from FY2026E, so base debt rises from $250 to about $5,270 by FY2035E and that borrowing is paid out to equity; a policy that held debt flat would lower the value, and this run does not size by how much [S45][C25]. Year-0 debt of $250 is the FY2025 10-K figure and excludes the $50 of add-on notes issued in March 2026, while year-0 cash likewise excludes their proceeds [A6][D24]. The 8.625% coupon, the 2030 maturity and any refinancing terms are not modelled beyond Finagle's 9.67% cost of debt [A6][S45]. Adjusted year-0 cash is negative in every case, about −$41.5 in the base, −$55.7 in the bull and −$14.6 in the bear, and the share count stays at 37.23 million because no equity raise is added to fill that gap [P9][C25]. G-MELT and YOCHIL revenue and the Melt approval cash are unweighted and conditional on approval [S15][S32][S25]. The CMS pass-through and J-code stock milestone of about 1.11 million shares is undated and is not in the share count, and Samsung's net-sales milestones and the up to $70 of TYRVAYA milestones are not in cash [S12][C7][A8][C19]. Terminal value is about 42% of the base equity value at a terminal growth rate equal to a 5.10% 10-year yield, and the 65.4% incremental margin keeps margins rising after FY2032E [C24][S45][S43]. Finagle's capex rule lifts capex from $0.9 in FY2025A to $290 in FY2032E, far above Harrow's reported capex, which lowers the value [C25][A6]. This report draws no rating or price target.

---
