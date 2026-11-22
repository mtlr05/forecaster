## Valuation

Finagle commit `377f177b4013e713fe7c4603962e5f883a67e298`.

Fetched price 32.1300 on 2026-11-22, risk-free rate 0.0505 on 2026-11-22, inflation 0.0200 on None (assumption), shares 37.2297 (10k).

### base

Value per share 154.4967.
Flag: negative cash
Warning: average EBITDA growth is 80.2% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.roict, rates.lam, rates.t, rates.re, rates.gt, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### bull

Value per share 184.1497.
Flag: negative cash
Warning: average EBITDA growth is 78.0% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.roict, rates.lam, rates.t, rates.re, rates.gt, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### bear

Value per share 87.8538.
Flag: negative cash
Warning: average EBITDA growth is 68.7% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero.
Warning: forecast evidence mentions acquisitions but the case has none, so MnA stays zero
Defaults filled: baseline.nol, baseline.noa, rates.roict, rates.lam, rates.t, rates.re, rates.gt, rates.rd, forecast.dwc.mode, debt.mode, debt.leverage, debt.start_year, distribution.mode.

### Balance Sheet Adjustments

Year-0 cash -41.5603 equals opening 72.9270 plus present value -114.4873. Share count 37.2297 equals opening 37.2297 plus 0.0 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2027-12-31 | 1.0 | 0.8933 | -77.8634 | 0.0 |
| Melt first commercial Annual Net Sales cash milestone | -10.0200 | 2030-12-31 | 1.0 | 0.6611 | -6.6239 | 0.0 |

Year-0 cash -55.7901 equals opening 72.9270 plus present value -128.7171. Share count 37.2297 equals opening 37.2297 plus 0.0 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2027-12-31 | 1.0 | 0.8933 | -77.8634 | 0.0 |
| Melt first commercial Annual Net Sales cash milestone | -10.0200 | 2029-12-31 | 1.0 | 0.7308 | -7.3224 | 0.0 |
| Melt second commercial Annual Net Sales cash milestone | -25.0200 | 2032-12-31 | 1.0 | 0.5408 | -13.5314 | 0.0 |

Year-0 cash -14.6970 equals opening 72.9270 plus present value -87.6240. Share count 37.2297 equals opening 37.2297 plus 0.0 shares.

| Item | Amount | When | Probability | Discount | Present value | Shares |
| --- | --- | --- | --- | --- | --- | --- |
| TYRVAYA close cash paid | -30.0 | 2026-10-01 | 1.0 | 1.0 | -30.0 | 0.0 |
| Melt FDA-approval milestone payable | -87.1679 | 2030-12-31 | 1.0 | 0.6611 | -57.6240 | 0.0 |

### Prompt inputs

- `market.price` = 28.3000 [P] 2026-11-15. David May, 22 November 2026: rerun HROW with the v03 price, shares, risk-free rate and year-0 interest, and pin inflation to the FRED 10-year breakeven of 2.24 percent on 13 November 2026.
- `market.shares` = 37.2297 [P] 2026-11-22. David May, 22 November 2026: rerun HROW with the v03 price, shares, risk-free rate and year-0 interest, and pin inflation to the FRED 10-year breakeven of 2.24 percent on 13 November 2026.
- `rates.risk_free` = 0.0510 [P] 2026-11-22. David May, 22 November 2026: rerun HROW with the v03 price, shares, risk-free rate and year-0 interest, and pin inflation to the FRED 10-year breakeven of 2.24 percent on 13 November 2026.
- `baseline.interest` = 24.1800 [P] 2026-11-22. David May, 22 November 2026: rerun HROW with the v03 price, shares, risk-free rate and year-0 interest, and pin inflation to the FRED 10-year breakeven of 2.24 percent on 13 November 2026.
- `rates.inflation` = 0.0224 [P] 2026-11-22. David May, 22 November 2026: rerun HROW with the v03 price, shares, risk-free rate and year-0 interest, and pin inflation to the FRED 10-year breakeven of 2.24 percent on 13 November 2026.
