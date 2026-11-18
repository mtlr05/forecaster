# VHI revision log

C$ millions. This is the first case, so there is no prior forecast ("old" is n/a). Growth is versus FY2025A (FY26) and FY2026E (FY27). Built 17 November 2026 on method commit 3a46f0a, after the Q3 2026 report (12 Nov 2026) and call (13 Nov 2026).

| Line | Year | Old | New | Change | Growth | Why |
|---|---|---:|---:|---:|---|---|
| Term licences, maintenance and support | FY26 | n/a | 100.388 | n/a | +17.5% | 9M actual 74.253 + Q4 26.135: 0.985 × average ARR (S1), Q4 organic add 1.5 (S2), Buddy for a full quarter, scaled ×0.9825 to the Consensus remainder (C1). |
| Term licences, maintenance and support | FY27 | n/a | 110.084 | n/a | +9.7% | Organic ARR +8% (S3: TTM rate held while SHREWD is unresolved), Buddy unscaled (S17), scale 0.988. |
| Virtual care (Attend Anywhere) | FY26 | n/a | 9.316 | n/a | +79.7% | First full year after the June 2025 Induction close; Q4 held at Q3 (S24). |
| Virtual care (Attend Anywhere) | FY27 | n/a | 8.784 | n/a | −5.7% | −5% a year, moderate decline per management (S7, G9). |
| Perpetual licences | FY26 | n/a | 2.436 | n/a | +16.6% | Q4 0.5 (S8). |
| Perpetual licences | FY27 | n/a | 1.976 | n/a | −18.9% | 2.0 a year (S8). |
| Services, hardware and other | FY26 | n/a | 16.861 | n/a | +3.8% | Q4 4.6, more milestones in Q4 (S9, G7). |
| Services, hardware and other | FY27 | n/a | 18.155 | n/a | +7.7% | 16.5% of term revenue (S9). |
| Revenue | FY26 | n/a | 129.000 | n/a | +18.4% | Consensus E1 (no guidance). |
| Revenue | FY27 | n/a | 139.000 | n/a | +7.8% | Consensus E1_1. |
| Adj. EBITDA | FY26 | n/a | 34.000 | n/a | +28.0% | Consensus E2; cost build Q4 9.10 vs Consensus remainder 9.23 (C15). |
| Adj. EBITDA | FY27 | n/a | 39.000 | n/a | +14.7% | Consensus E2_1; cost build 38.13 on the same revenue (−0.9% cash cost gap). |

## Revision v2 – 17 November 2026, 10:05 ET (America/Toronto)

Trigger: David May (pt220u: "I think Palantirs contract was renewed. Probably have to assume that some of the shrewd contracts roll off in 2027.") and The Register, 17 Nov 2026, "MPs ask what the break clause was for as Palantir wins two more years in the NHS" (D23). The health minister told MPs on 16 Nov 2026 that the Palantir-led FDP contract continues to March 2029, so the February 2027 break clause is not exercised; a new FDP procurement starts in H2 2027 and runs about 18 months (G26–G28). Method commit unchanged (3a46f0a; `git fetch` + `merge --ff-only` said already up to date). v1 files archived in `v1/`.

What changed: SHREWD is now an explicit roll-off. Base loses 4.0 of SHREWD ARR straight-line during 2027 and nothing after (S26); underlying organic growth before SHREWD is 9% in FY2027 (was 8% net) so the Q3 drag is not counted twice (S3); lost SHREWD revenue saves only cash cost of sales (S27). The 17 Nov FactSet pull is taken to predate the announcement, so the base is Consensus plus the change in the bottom-up build from v1 to v2 (C36, override tagged P7). FY2026 is unchanged. Growth is versus the prior year of the same version.

| Line | Year | Old | New | Change | Growth | Why |
|---|---|---:|---:|---:|---|---|
| Term licences, maintenance and support | FY27 | 110.084 | 108.651 | −1.433 | +8.2% | 4.0 SHREWD ARR rolls off in 2027 (average 2.0 lost); underlying organic 9% (S26, S3). |
| Term licences, maintenance and support | FY28 | 117.533 | 114.528 | −3.005 | +5.4% | Full-year effect of the 4.0 loss; organic 10% (S4). |
| Term licences, maintenance and support | FY29 | 133.864 | 130.549 | −3.315 | +14.0% | Same; Consensus path shape (C34). |
| Services, hardware and other | FY27 | 18.155 | 17.919 | −0.236 | +6.3% | 16.5% of the lower term line (S9). |
| Services, hardware and other | FY28 | 19.369 | 18.872 | −0.497 | +5.3% | Same. |
| Services, hardware and other | FY29 | 22.089 | 21.542 | −0.547 | +14.1% | Same. |
| Virtual care; Perpetual licences | FY27–29 | — | — | ≤0.002 | — | Scale-factor rounding only. |
| Revenue | FY27 | 139.000 | 137.329 | −1.671 | +6.5% | Event-adjusted Consensus (C36). |
| Revenue | FY28 | 147.000 | 143.490 | −3.510 | +4.5% | Event-adjusted Consensus (C36). |
| Revenue | FY29 | 166.000 | 162.139 | −3.861 | +13.0% | Event-adjusted Consensus (C36). |
| Adj. EBITDA | FY27 | 39.000 | 37.476 | −1.524 | +10.2% | Lost SHREWD revenue at 80% fall-through (S27). |
| Adj. EBITDA | FY28 | 45.000 | 41.868 | −3.132 | +11.7% | Same. |
| Adj. EBITDA | FY29 | 52.000 | 48.693 | −3.307 | +16.3% | Same; FY29 margin 30.0% (was 31.3%). |

Scenarios: bull now loses 1.5 of SHREWD ARR in 2027 (was none) and carries no FDP procurement revenue (S28); revenue FY27–29 141.1/150.7/171.9 (−0.86/−1.82/−2.02), Adjusted EBITDA 41.9/49.8/59.5 (−0.69/−1.43/−1.55). Bear now loses all 8.0 during 2027 with underlying organic 7%/6%/7% (was 2%/6%/7% net with about 7.5 lost); revenue 131.7/130.6/143.1 (−1.50/−3.09/−3.29), Adjusted EBITDA 32.4/31.9/34.9 (−2.44/−4.91/−4.99) (C37).

## Revision v3 – 18 November 2026, 12:55 ET (America/Toronto)

Trigger: David May (pt221u: "ask the Dan Matlow bot for his product sheet on licenses. Update the forecast if it provides any insight into trends"). The source is the CEO bot's term-licence product sheet, `companies/vhi/sources/products/term-licences-maintenance-and-support.md`, in the read-only ceochat clone at commit 25246c9 (D24). It is a simulated source and is used only as an index: every ARR bridge figure used was checked in the filing it names (A75–A80). The FY2023 MD&A download from OTC Markets returned "Temporarily Unavailable", so the 2023 quarters come from the FY2024 MD&A comparatives (A75). The method commit is unchanged (3a46f0a; fetched again and already up to date). The v2 files are archived in `v2/`.

Findings (C38, C39):

- **Organic additions in dollars.** Net of churn, organic ARR additions were 6.39 in 2023, 6.48 in 2024, 7.23 in 2025 and 8.12 in the 12 months to Q2 2026. That is about +10% a year.
- **Organic additions as a share of opening ARR.** The share fell from 17.7% to 14.5% to 10.2%, and to 7.7% in the 12 months to Q3 2026. The fall is largely a base effect: 38 of acquired ARR enlarged the base but added little net organic growth in aggregate.
- **Seasonality.** Q4 is the strongest quarter. The 2022–25 averages are Q4 1.84, Q1 1.57, Q2 1.35 and Q3 1.28.
- **FX.** FX added 2.09 in 2024, 1.99 in 2025 and 1.22 in 9M 2026.
- **Term/ARR ratio.** Term revenue / average ARR has been 0.979–0.994 since Q4 2025, averaging 0.985, which confirms S1.
- **Q4 2024 term revenue.** The 17.67 is printed in the FY2024 MD&A three-month column. The step-up came from 14.6 of ARR acquired in the quarter.
- **Flat-additions hypothesis.** The hypothesis of flat dollar additions (about 7 a year, about 6.5% of opening ARR) is only partly supported. The 12 months to Q3 2026 print 7.23, but that figure includes the SHREWD drag, and dollar additions were rising before SHREWD. Flat 7.23 becomes the bear.

What changed:

- **Organic driver.** Organic ARR additions are now forecast in dollars (S29).
  - Base: grow 10% a year from 8.12, giving 8.94 / 9.83 / 10.8.
  - Bull: grow 15% a year, giving 9.34 / 10.7 / 12.4.
  - Bear: flat at 7.23 (S22, S18).
  - v2's 9% / 10% of opening ARR implied 9.8–12.6 a year, above any year printed.
- **Event adjustment (C36).** It is now SHREWD-only: our build with the 4.0 roll-off minus the same build without it. That gives −2.295 / −4.590 / −4.590 on revenue and −1.836 / −3.672 / −3.672 on Adjusted EBITDA. The organic-driver change uses information analysts already had, so it moves the bottom-up view and the scenarios, not the base.
- **Unchanged.** The SHREWD roll-off (4.0 / 1.5 / 8.0 in 2027), fall-through, Q4 2026 and all other drivers are unchanged. FY2026 is unchanged.

| Line | Year | Old (v2) | New (v3) | Change | Why |
|---|---|---:|---:|---:|---|
| Term licences, maintenance and support | FY27 | 108.651 | 108.126 | −0.525 | Organic adds in dollars (8.94 / 9.83 / 10.8, +10% a year) replace 9% / 10% of opening ARR (S29, S3–S5); scale factor absorbs most of the change. |
| Term licences, maintenance and support | FY28 | 114.528 | 113.549 | −0.979 | Organic adds in dollars (8.94 / 9.83 / 10.8, +10% a year) replace 9% / 10% of opening ARR (S29, S3–S5); scale factor absorbs most of the change. |
| Term licences, maintenance and support | FY29 | 130.549 | 129.735 | −0.814 | Organic adds in dollars (8.94 / 9.83 / 10.8, +10% a year) replace 9% / 10% of opening ARR (S29, S3–S5); scale factor absorbs most of the change. |
| Virtual care term licences (Attend Anywhere) | FY27 | 8.783 | 8.773 | −0.010 | Scale-factor change only (S7 unchanged). |
| Virtual care term licences (Attend Anywhere) | FY28 | 8.158 | 8.203 | +0.045 | Scale-factor change only (S7 unchanged). |
| Virtual care term licences (Attend Anywhere) | FY29 | 8.042 | 8.206 | +0.164 | Scale-factor change only (S7 unchanged). |
| Perpetual licences | FY27 | 1.976 | 1.974 | −0.002 | Scale-factor change only (S8 unchanged). |
| Perpetual licences | FY28 | 1.932 | 1.943 | +0.011 | Scale-factor change only (S8 unchanged). |
| Perpetual licences | FY29 | 2.005 | 2.046 | +0.041 | Scale-factor change only (S8 unchanged). |
| Services, hardware and other | FY27 | 17.919 | 17.831 | −0.088 | 16.5% of the term line (S9). |
| Services, hardware and other | FY28 | 18.872 | 18.715 | −0.157 | 16.5% of the term line (S9). |
| Services, hardware and other | FY29 | 21.542 | 21.423 | −0.119 | 16.5% of the term line (S9). |
| Revenue | FY27 | 137.329 | 136.705 | −0.624 | Consensus + SHREWD-only event adjustment (C36); v2 was Consensus + whole v1→v2 build change. |
| Revenue | FY28 | 143.490 | 142.410 | −1.080 | Consensus + SHREWD-only event adjustment (C36); v2 was Consensus + whole v1→v2 build change. |
| Revenue | FY29 | 162.139 | 161.410 | −0.729 | Consensus + SHREWD-only event adjustment (C36); v2 was Consensus + whole v1→v2 build change. |
| Adj. EBITDA | FY27 | 37.476 | 37.164 | −0.312 | Consensus + SHREWD-only event adjustment (C36); v2 was Consensus + whole v1→v2 build change. |
| Adj. EBITDA | FY28 | 41.868 | 41.328 | −0.540 | Consensus + SHREWD-only event adjustment (C36); v2 was Consensus + whole v1→v2 build change. |
| Adj. EBITDA | FY29 | 48.693 | 48.328 | −0.365 | Consensus + SHREWD-only event adjustment (C36); v2 was Consensus + whole v1→v2 build change. |
Bottom-up:

- **Revenue:** 138.45 / 146.48 / 157.90 (v2 138.94 / 148.38 / 161.75).
- **Adjusted EBITDA:** 37.17 / 39.09 / 43.37 (v2 37.41 / 40.04 / 45.30).
- **Flag:** bottom-up / base EBITDA in FY2029 is 0.897, more than 10% below the base.

Scenarios (C40), FY27–29:

- **Bull:** revenue 139.99 / 148.33 / 169.16 (−1.07 / −2.40 / −2.72 vs v2); Adjusted EBITDA 41.23 / 48.29 / 57.54 (−0.63 / −1.52 / −1.94).
- **Bear:** revenue 131.35 / 131.54 / 146.40 (−0.31 / +0.93 / +3.27); Adjusted EBITDA 32.29 / 32.30 / 36.51 (−0.14 / +0.45 / +1.62).
- **Why the bear rises in FY2028–29:** the base bottom-up fell while the base totals stay on Consensus, which narrows the bear-minus-base build gap. On unscaled builds the bear is close to v2.
- **gsnext:** base 8.0%, bull 9.2%, bear 5.2%.

## Revision v3.1 – 18 November 2026, about 13:20 ET (America/Toronto): collaborative valuation request

Trigger: David May (pt223u: "do a finagle valuation."). It was revised the same day: the Finagle bot runs the valuation, so the Forecaster follows only steps 1–3 of `collaborative-run.md` (P9). The method commit is unchanged (3a46f0a; fetched again, up to date).

What changed:

- **`forecast.json`.** The bull and bear `finagle` blocks now carry `ebitda_basis` (total, C20) and `acquisition_disclosure.status` (none, C21), the same as the base. Without them the request could not match the forecast file for those cases. No revenue, EBITDA, line, scenario total or schedule value changed. C20's wording now points to P9, and P9 was added.
- **New `finagle-run/valuation_request_v01.json`.** Settings:
  - mode collaborative, scenarios base, bull and bear;
  - Forecaster leaves copied from `forecast.json`;
  - `cash_share_adjustments` copied unchanged (five base items);
  - `prompt_inputs` empty, `post_finagle` null.
- **Checks.** `check_request` and `forecast_mismatches` return no errors. Price, shares, the risk-free rate, the cost of equity, terminal growth and year-0 cash are absent.
- **Not run by us.** No valuation was run by the Forecaster. An earlier exploratory Finagle run made before the change of plan was discarded: it was moved to `work/discarded-finagle-run-20261118/` and is not used in any deliverable. The report is unchanged from v3.

## Revision v3.2 – 18 November 2026, about 14:30 ET (America/Toronto): Finagle valuation added

Trigger: David May (pt223u, "do a finagle valuation."). The Finagle bot ran the collaborative valuation. Result `finagle-run/valuation_result_v04.json`; request `valuation_request_v04.json`, sha256 add5ef2219e948adfadb000b539d98745c5ab92668188f4f1e3b1dcc9295971c. Finagle commit 377f177b; run at 14:12 ET. The forecaster method commit is unchanged (3a46f0a; fetched, up to date). The v3.1 report and files are archived in `v3.1/`.

Runs v01–v03 are not valuations:
- **v01** stopped: no CAD 10-year quote from Yahoo (CA10Y=RR).
- **v02** completed but was ruled not a valuation: the default capex was anchored on year-0 D&A that was 89% amortization of acquired intangibles.
- **v03** stopped: two inputs could not be expressed. One was capex as a ratio of revenue, which was not a year-by-year list. The other was Buddy consideration shares with no cash proceeds.

v04 prompt inputs (all dated 2026-11-18):
- **Risk-free rate:** 3.81% (Bank of Canada 10-year).
- **Debt:** 0, held, with leases excluded.
- **Tax:** 26.5%.
- **Opening cash:** 106.81 = 119.18 − 12.37 for the Buddy close.
- **Shares:** 63,307,054 = 63,232,054 + 75,000 Buddy shares. The Buddy items were removed from the schedule.
- **Year-0 D&A:** 1.271558, which excludes amortization of acquired intangibles.
- **Cost of debt:** 2.8%. Proposed by the Forecaster; David did not object.

Result:
- **Value per share:** base C$9.070, bull C$11.031, bear C$6.708, against C$6.73 (Yahoo, 2026-11-18).
- **Rates:** cost of equity 9.31% and terminal growth 3.81%, both derived by Finagle.
- **Cash:** cash after the schedule 99.79.
- **Sanity flags:** none.
- **Warnings:** EBITDA growth of 16.4% (base) and 21.4% (bull) with no acquisitions.

What changed:
- **Report.** New Section 7 Valuation, with Figures 9–13 and the Balance Sheet Adjustments table. Risks is renumbered to Section 8, and Appendix A and C figures are renumbered to 14–19. The title-block note is updated. Appendix C gains the run history and the method suggestions.
- **forecast.json.** New sources only: D25–D27, P9 (revised) to P14, A81, A82, S30 and C41–C44. No forecast number changed.
- **forecast.md.** The status line now records the valuation.

## Revision v3.3 – 18 November 2026, about 14:45 ET (America/Toronto): Finagle valuation v05

Trigger: David May (t237u, "Yes, do the quick fix", 18 Nov 2026). The Finagle bot ran v05. It is the same as v04 except that year-0 EBITDA is stated as Vitalhub's reported FY2025 Adjusted EBITDA (26.554099, defined before stock-based compensation), replacing Yahoo's 25.898 (P15).

- **Result and request:** `finagle-run/valuation_result_v05.json`; request sha256 ba766900bf9dd16f1178d9a00f12325b518624426d9b84fca32e4a52509b6446; Finagle commit 377f177b.
- **Method read:** forecaster method read from origin/main 3a46f0a through git archive into /tmp. The local checkout was not touched.
- **Archive:** the v3.2 report and files are in `v3.2/`.

Result:
- **Value per share:** base C$9.226, bull 11.216, bear 6.827, against 6.73. In v04 they were 9.070 / 11.031 / 6.708.
- **EBITDA:** explicit-year EBITDA now equals the forecast (FY2026E base 34.000).
- **Stock comp:** year-0 stock comp is still Yahoo's 2.648, so the stock comp/EBITDA ratio is 0.0997.
- **Capex:** FY2035E base capex is 16.3, about 6.0x D&A and 19.4% of EBITDA.
- **Unchanged from v04:** rates, cash, shares and schedule.

What changed:
- **Report Section 7:** rewritten from v05. It adds the EBITDA prompt inputs and drops the Yahoo-EBITDA caveat.
- **Report Appendix C:** v04 is now listed as superseded, and a sixth method suggestion is added (send year-0 EBITDA and revenue as Forecaster leaves).
- **forecast.json:** sources updated (D25, P9 and the new P15, S30, C41–C44). No forecast number changed.
- **forecast.md:** status line updated.
