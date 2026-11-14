## Valuation

Finagle commit `377f177b4013e713fe7c4603962e5f883a67e298`.

Fetched price 28.3000 on 2026-11-14, risk-free rate 0.0510 on 2026-11-14, shares 37.2297 (10k).

### base

Value per share 148.4989.
Flag: negative cash
Warning: average EBITDA growth is 76.7% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.re, rates.gt, rates.roict, rates.t, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### bull

Value per share 176.8200.
Flag: negative cash
Warning: average EBITDA growth is 78.5% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.re, rates.gt, rates.roict, rates.t, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### bear

Value per share 81.7192.
Flag: negative cash
Warning: average EBITDA growth is 66.8% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.re, rates.gt, rates.roict, rates.t, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### Balance Sheet Adjustments

Year-0 cash -41.4840 equals opening 72.9270 plus present value -114.4110. Share count 37.2292 equals opening 37.2292 plus 0.0 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2027-12-31 | 1.0 | 0.8925 | -77.8015 | 0.0 |
| Melt first commercial Annual Net Sales cash milestone | -10.0200 | 2030-12-31 | 1.0 | 0.6596 | -6.6095 | 0.0 |

Year-0 cash -55.6737 equals opening 72.9270 plus present value -128.6007. Share count 37.2292 equals opening 37.2292 plus 0.0 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2027-12-31 | 1.0 | 0.8925 | -77.8015 | 0.0 |
| Melt first commercial Annual Net Sales cash milestone | -10.0200 | 2029-12-31 | 1.0 | 0.7295 | -7.3098 | 0.0 |
| Melt second commercial Annual Net Sales cash milestone | -25.0200 | 2032-12-31 | 1.0 | 0.5391 | -13.4894 | 0.0 |

Year-0 cash -14.5716 equals opening 72.9270 plus present value -87.4986. Share count 37.2292 equals opening 37.2292 plus 0.0 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2030-12-31 | 1.0 | 0.6596 | -57.4986 | 0.0 |

### Prompt inputs

- `baseline.cash` = 72.9270 [P] 2026-11-02. Standing instruction (recorded 2 November 2026): year-0 cash is the last fiscal year-end cash plus short-term investments (e.g., FY2025), adjusted for equity raises made during the following year, and the share count is raised from the last fiscal-year figure to reflect those raises. Applied: FY2025 year-end cash and cash equivalents $72.927 with no short-term investments, plus $0 of FY2026 equity raises (none through 12 November 2026); shares 37.229159 million at 31 December 2025, plus 0 raise shares. Harrow 10-Q for Q3 2026 balance sheet and equity statement.
- `market.shares` = 37.2292 [P] 2026-11-02. Standing instruction (recorded 2 November 2026): year-0 cash is the last fiscal year-end cash plus short-term investments (e.g., FY2025), adjusted for equity raises made during the following year, and the share count is raised from the last fiscal-year figure to reflect those raises. Applied: FY2025 year-end cash and cash equivalents $72.927 with no short-term investments, plus $0 of FY2026 equity raises (none through 12 November 2026); shares 37.229159 million at 31 December 2025, plus 0 raise shares. Harrow 10-Q for Q3 2026 balance sheet and equity statement.
