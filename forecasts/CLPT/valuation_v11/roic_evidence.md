# CLPT terminal ROIC (roict = 0.20): evidence

Sources:
- [A] SEC XBRL company facts for CIK 1285550 (10-K annual values, FY2015–FY2025): https://data.sec.gov/api/xbrl/companyfacts/CIK0001285550.json
- [F] Finagle v9 base run: /workspace/out/clpt_val_v9/finagle_template_table_v9.json
- [C] calculations below, from [A] and [F]

USD millions. EBITDA = operating income + D&A + SBC, the same definition as clpt_baseline.json. Invested capital (IC) = net PP&E + receivables + inventory − payables. Cash, the IRRAS goodwill/intangibles (FY2025) and lease ROU assets are excluded. ClearPoint discloses no capitalised software tag, so no capex + software series was possible.

## History [A][C]
| FY | Revenue | Op. income | EBITDA | Capex | R&D | IC | Revenue/IC |
|---|---|---|---|---|---|---|---|
| 2015 | 4.59 | −8.97 | −7.08 | 0.077 | 1.96 | 2.77 | 1.66 |
| 2016 | 5.75 | −7.49 | −6.15 | 0.101 | 2.63 | 1.42 | 4.06 |
| 2017 | 7.38 | −6.34 | −4.97 | 0.027 | 2.81 | 2.77 | 2.66 |
| 2018 | 7.35 | −5.25 | −3.91 | 0.063 | 2.31 | 3.22 | 2.29 |
| 2019 | 11.22 | −4.59 | −3.65 | 0.010 | 2.81 | 3.81 | 2.94 |
| 2020 | 12.83 | −6.22 | −4.80 | 0.041 | 4.69 | 5.14 | 2.50 |
| 2021 | 16.30 | −13.37 | −11.14 | 0.168 | 9.28 | 7.39 | 2.21 |
| 2022 | 20.55 | −16.33 | −11.96 | 0.253 | 10.89 | 12.50 | 1.64 |
| 2023 | 23.95 | −22.45 | −15.74 | 0.717 | 11.71 | 12.12 | 1.98 |
| 2024 | 31.39 | −19.73 | −11.85 | 0.275 | 12.39 | 12.24 | 2.56 |
| 2025 | 36.97 | −24.16 | −15.17 | 0.522 | 13.90 | 16.27 | 2.27 |

## Windows [C]
| Window | Revenue added | Cumulative capex | Revenue added per $ capex | Cumulative capex + R&D | Revenue added per $ (capex + R&D) | EBITDA change | IC change |
|---|---|---|---|---|---|---|---|
| FY15→20 | 8.23 | 0.24 | 34.0 | 15.5 | 0.53 | +2.28 | +2.37 |
| FY20→25 | 24.14 | 1.94 | 12.5 | 60.1 | 0.40 | −10.37 | +11.13 |
| FY15→25 | 32.38 | 2.18 | 14.9 | 75.6 | 0.43 | −8.09 | +13.50 |

EBITDA and operating income were negative in every year from FY2015 to FY2025. ROIC and the incremental EBITDA or NOPAT return on capex are therefore **not meaningful** from history. EBITDA fell while capital was being invested.

## Base forecast, FY2025→FY2031 [F][C]
- Revenue rises from 37.0 to 410.4, so 373.4 is added. Cumulative capex over FY2026–31 is 108.0, or 3.5 of revenue per $ of capex. History gave 12.5–34.
- Capex is about 10% of revenue in FY2031 (40.8 / 410.4), against about 1.4% in FY2025.
- NOPAT = (EBITDA − SBC − D&A) × (1 − 21%). It goes from about −24 (operating loss, FY2025) to 118.4 in FY2031, while net investment (capex − D&A) totals 81.7. The marginal return is about 175%, but this comes from the operating ramp, not from the capital.
- **Finagle's mechanism** (`company.forecast_capex` method 1): in the terminal year, capex + Δwc − D&A = (gt / roict) × NOPAT, so net reinvestment = 4.95% / 20% = 24.8% of NOPAT. Capex in the years between FY2025 and the terminal year is bridged in proportion to revenue.
- Result: FY2040 base capex is 105.1 against D&A of 22.2. Net investment of 82.9 is 24.8% of the 334.8 NOPAT, and capex is 10.4% of revenue.

## Reading
- **Physical capital:** ClearPoint has grown revenue on almost no capex. That means 12–34 of revenue added per $ of capex, revenue/IC of 1.6–4.1, and capex of 0.1–3% of revenue. On a physical-capital basis, 20% looks **low**. At, say, 35% EBITDA margins and revenue/IC of about 2, a mature operating ROIC would be well above 50%. That figure is an illustration, not a measured value.
- **Counting R&D as investment:** each $ of capex + R&D added only $0.40–0.53 of revenue, and none of it has yet earned a profit. History cannot show what the return on R&D will be.
- **What history supports:** roict from about 20% (if R&D is treated as capital that must keep growing with sales) up to 50% or more (physical capital only). Nothing in the filings supports going below 20%. The bigger point is that Finagle's roict sets capex. At 20%, forecast capex runs at about 10% of revenue, several times ClearPoint's history. A higher roict would lower terminal capex and raise value. I did not test this.
