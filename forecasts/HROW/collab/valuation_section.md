## Valuation

Finagle commit `377f177b4013e713fe7c4603962e5f883a67e298`.

Fetched price 29.3700 on 2026-11-12, risk-free rate 0.0500 on 2026-11-12, shares 37.2297 (10k).

### base

Value per share 132.6926.
Warning: average EBITDA growth is 68.1% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.re, rates.gt, rates.roict, rates.t, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### bull

Value per share 153.2803.
Flag: negative cash
Warning: average EBITDA growth is 68.9% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.re, rates.gt, rates.roict, rates.t, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### bear

Value per share 14.7099.
Flag: negative FCFE after year 1
Warning: average EBITDA growth is 30.2% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.re, rates.gt, rates.roict, rates.t, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### Balance Sheet Adjustments

Year-0 cash 8.4528 equals opening 72.9270 plus present value -64.4742. Share count 38.9316 equals opening 37.2292 plus 1.7024 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2027-12-31 | 1.0 | 0.8930 | -77.8423 | 0.0 |
| Melt first commercial Annual Net Sales cash milestone | -10.0200 | 2030-12-31 | 1.0 | 0.6619 | -6.6318 | 0.0 |
| Year-0 equity raise (David May rule, cash would otherwise be negative) | 50.0 | 2026-11-12 | 1.0 | 1.0 | 50.0 | 1.7024 |

Year-0 cash 44.1963 equals opening 72.9270 plus present value -28.7307. Share count 40.6340 equals opening 37.2292 plus 3.4048 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2027-12-31 | 1.0 | 0.8930 | -77.8423 | 0.0 |
| Melt first commercial Annual Net Sales cash milestone | -10.0200 | 2029-12-31 | 1.0 | 0.7313 | -7.3275 | 0.0 |
| Melt second commercial Annual Net Sales cash milestone | -25.0200 | 2032-12-31 | 1.0 | 0.5420 | -13.5608 | 0.0 |
| Year-0 equity raise (David May rule, cash would otherwise be negative) | 100.0 | 2026-11-12 | 1.0 | 1.0 | 100.0 | 3.4048 |

Year-0 cash 35.2340 equals opening 72.9270 plus present value -37.6930. Share count 38.9316 equals opening 37.2292 plus 1.7024 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2030-12-31 | 1.0 | 0.6619 | -57.6930 | 0.0 |
| Year-0 equity raise (David May rule, cash would otherwise be negative) | 50.0 | 2026-11-12 | 1.0 | 1.0 | 50.0 | 1.7024 |

### Prompt inputs

- `baseline.cash` = 72.9270 [P] 2026-11-02. Standing instruction (recorded 2 November 2026): year-0 cash is the last fiscal year-end cash plus short-term investments (e.g., FY2025), adjusted for equity raises made during the following year, and the share count is raised from the last fiscal-year figure to reflect those raises. Applied: FY2025 year-end cash and cash equivalents $72.927 with no short-term investments, plus $0 of FY2026 equity raises (none through 12 November 2026); shares 37.229159 million at 31 December 2025, plus 0 raise shares. Harrow 10-Q for Q3 2026 balance sheet and equity statement.
- `market.shares` = 37.2292 [P] 2026-11-02. Standing instruction (recorded 2 November 2026): year-0 cash is the last fiscal year-end cash plus short-term investments (e.g., FY2025), adjusted for equity raises made during the following year, and the share count is raised from the last fiscal-year figure to reflect those raises. Applied: FY2025 year-end cash and cash equivalents $72.927 with no short-term investments, plus $0 of FY2026 equity raises (none through 12 November 2026); shares 37.229159 million at 31 December 2025, plus 0 raise shares. Harrow 10-Q for Q3 2026 balance sheet and equity statement.
