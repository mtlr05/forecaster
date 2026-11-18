# Vitalhub Corp. (TSX: VHI)

**Company Update: FY2026E–FY2029E Revenue and EBITDA Forecast**

*17 November 2026, revised 18 November 2026 12:55 ET (America/Toronto), version 3; valuation added 18 November 2026 (v3.3, Finagle result v05). C$ millions unless noted. Version 2 added a partial roll-off of NHS SHREWD contracts in 2027 after the UK government extended the Palantir-led NHS Federated Data Platform contract to March 2029 [D23][G26][P7]. Version 3 forecasts organic ARR additions in dollars rather than as a percentage of an ARR base enlarged by acquisitions, based on the ARR bridge in the Dan Matlow CEO bot's term-licence product sheet, checked against the filings [D24][P8]. Earlier versions are archived in `v1/`, `v2/`, `v3/`, `v3.1/` and `v3.2/`, and `revision_log.md` lists every change. Section 7 adds a Finagle valuation of the v3 forecast, run by the Finagle bot on 18 November 2026 (result v05) with inputs David May stated that day [P9][P15][D25]. Values are in C$ per share against the C$6.73 Yahoo price; the report carries no rating or price target. The audit record is `forecast.md` / `forecast.json` in this folder. Numbered sources are in Appendix B.*

---

## 1. Estimate comparison

Vitalhub publishes no revenue or Adjusted EBITDA guidance. On the Q2 2026 call management said it was still comfortable with an organic run rate of about 10%–11% [G13]. That comfort was not repeated on the Q3 2026 call, where management put about 7%–8% of ARR in the SHREWD product line at risk [G2][G3]. We treat the 10%–11% as withdrawn. There is therefore no top-down or calibrated top-down view. The base starts from the FactSet consensus pulled on 17 November 2026, after the Q3 release [E1][E2].

That pull very probably predates the news behind version 2. On Monday 16 November the health minister told MPs that the Palantir-led FDP contract will run to March 2029, so the February 2027 break clause will not be used [G26]. The pull came about a day later. Our v1 build, which left SHREWD unresolved, matched FactSet to within 1.2% in FY2026E and FY2027E, so FactSet does not yet appear to carry a 2027 SHREWD loss. The forecaster skill has no specific rule for news after the Consensus pull, but it lets an instruction in the prompt override the default method. David's instruction to assume some SHREWD roll-off in 2027 is that override [P7].

The base is FactSet plus the effect of the SHREWD roll-off alone, measured on our build with and without the loss. That lowers revenue by 2.30 in FY2027E and 4.59 in each of FY2028E and FY2029E. It lowers Adjusted EBITDA by 1.84 and then 3.67 [C36].

Version 3 isolates that adjustment. In version 2 the adjustment also carried our change in the organic growth rate. That change rested on information analysts already had, so under the skill it moves the bottom-up view, not the base. FY2026E is unchanged. The unadjusted FactSet figures stay in Figure 1 and in the forecast file.

On the adjusted base, the bottom-up build is within 1.3% on revenue in FY2026E and FY2027E. It is 2.9% above in FY2028E and 2.2% below in FY2029E [C11]. On Adjusted EBITDA it matches in FY2026E and FY2027E. It falls 5% short in FY2028E and 10% short in FY2029E, because our slower dollar-based organic path and our cost build both sit below the Consensus margin path [C13]. FactSet's own revenue path is uneven, at +7.8%, +5.8% and +12.9% for FY2027–FY2029, which most likely reflects thin, rounded coverage in the later years [C34].

<div class="fig" markdown="1">

**Figure 1 – Estimate comparison, revenue (C$ millions)**

Each recorded view against the revenue base. The base is FactSet plus the SHREWD event adjustment. Top-down and calibrated top-down are absent because there is no guidance.

| | FY2025A | 9M 2026A | Q4 2026E | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bottom-up (v3) | — | — | 34.0 | 130 | 138 | 146 | 158 |
| Top-down | — | — | n/a | n/a | n/a | n/a | n/a |
| Calibrated top-down | — | — | n/a | n/a | n/a | n/a | n/a |
| Consensus, FactSet as pulled | — | — | 33.4 | 129 | 139 | 147 | 166 |
| SHREWD event adjustment | — | — | 0.00 | 0.00 | −2.30 | −4.59 | −4.59 |
| **Base (event-adjusted Consensus)** | **109** | **95.6** | **33.4** | **129** | **137** | **142** | **161** |
| Bottom-up / base | | | 1.017 | 1.005 | 1.013 | 1.029 | 0.978 |
| Top-down / base | | | n/a | n/a | n/a | n/a | n/a |
| Calibrated / base | | | n/a | n/a | n/a | n/a | n/a |
| Event-adjusted Consensus / base | | | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| FactSet as pulled / base | | | 1.000 | 1.000 | 1.017 | 1.032 | 1.028 |
| Bottom-up / calibrated | | | n/a | n/a | n/a | n/a | n/a |
| Bottom-up / Consensus (adjusted) | | | 1.017 | 1.005 | 1.013 | 1.029 | 0.978 |

*Source: [A1_1][A1_2][E1][E1_1][E1_2][E1_3][C5][C9][C11][C36]. Q4 2026E Consensus = FY2026 Consensus less nine-month actual. Totals of 100 and above are whole numbers. May not sum due to rounding.*

</div>

<div class="fig" markdown="1">

**Figure 1 (continued) – Estimate comparison, Adjusted EBITDA (C$ millions)**

FactSet's EBITDA history for 2025 equals Vitalhub's reported Adjusted EBITDA of 26.6, so the Consensus is on the company's adjusted basis.

| | FY2025A | 9M 2026A | Q4 2026E | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bottom-up (v3) | — | — | 9.39 | 34.2 | 37.2 | 39.1 | 43.4 |
| Top-down | — | — | n/a | n/a | n/a | n/a | n/a |
| Calibrated top-down | — | — | n/a | n/a | n/a | n/a | n/a |
| Consensus, FactSet as pulled | — | — | 9.23 | 34.0 | 39.0 | 45.0 | 52.0 |
| SHREWD event adjustment | — | — | 0.00 | 0.00 | −1.84 | −3.67 | −3.67 |
| **Base (event-adjusted Consensus)** | **26.6** | **24.8** | **9.23** | **34.0** | **37.2** | **41.3** | **48.3** |
| Bottom-up / base | | | 1.018 | 1.005 | 1.000 | 0.946 | 0.897 |
| Top-down / base | | | n/a | n/a | n/a | n/a | n/a |
| Calibrated / base | | | n/a | n/a | n/a | n/a | n/a |
| Event-adjusted Consensus / base | | | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| FactSet as pulled / base | | | 1.000 | 1.000 | 1.049 | 1.089 | 1.076 |
| Bottom-up / calibrated | | | n/a | n/a | n/a | n/a | n/a |
| Bottom-up / Consensus (adjusted) | | | 1.018 | 1.005 | 1.000 | 0.946 | 0.897 |

*Source: [A2_1][A2_2][E2][E2_1][E2_2][E2_3][C10][C13][C36]. May not sum due to rounding.*

</div>

---

## 2. Summary

**FORECAST UPDATE**

■ **We forecast FY2027E revenue of 137 (+6.0%) and Adjusted EBITDA of 37.2 (27.2%), because about half of Vitalhub's NHS SHREWD ARR rolls off during 2027 now that the government has kept the Palantir-led data platform to March 2029.** We take 4.0 of the roughly 7.5–8.6 of SHREWD ARR out evenly over 2027. Lost SHREWD revenue saves only its cost of sales, so most of it falls through to Adjusted EBITDA. FY2026E is unchanged at 129 and 34.0. See Estimate comparison and the term-licence subsection.

■ **Organic ARR additions are now forecast in dollars: 8.94 in FY2027, 9.83 in FY2028 and 10.8 in FY2029, because the filed ARR bridge shows dollar additions rising about 10% a year while the percentage fell only because acquisitions enlarged the base.** Printed organic additions were 6.39 in 2023, 6.48 in 2024 and 7.23 in 2025, and 8.12 in the four quarters to Q2 2026. Over the same period the organic rate fell from 17.7% to 14.5% to 10.2%, as 38 of acquired ARR joined the base without adding much organic growth. The new path is 8.2%–8.8% of opening ARR, against the 9%–10% in version 2. It moves the bottom-up view and the bull, but not the Consensus-based base. See How the evidence becomes the numbers and Figure 6.

■ **We forecast FY2029E revenue of 161 and Adjusted EBITDA of 48.3, a 29.9% margin, which is still above every year Vitalhub has reported.** The best full-year margin so far was 26.0% in FY2024, and the best quarter in the nine we track was 27.6% in Q3 2024. Our own build reaches 43.4 (27.5%) on 158 of revenue, 10% below the base. That gap is the main risk to the base. See the cash opex bridge and Appendix A.

■ **SHREWD and the pace of dollar additions are the swing factors.** The bear loses all SHREWD ARR in 2027 and holds organic additions flat at 7.23 a year, giving revenue of 131 in FY2027E and 146 in FY2029E and Adjusted EBITDA of 32.3 and 36.5. The bull loses 1.5 and grows additions 15% a year, giving revenue of 140 and 169 and Adjusted EBITDA of 41.2 and 57.5. The new FDP procurement would earn revenue mostly after FY2029 and is in no case. See Appendix A.

<div class="fig" markdown="1">

**Figure 2 – Financial summary (FY2024A–FY2029E, C$ millions)**

The base case, version 3. FY2025A includes the Induction and Novari acquisitions from mid-2025. FY2026E includes Buddy from 10 July 2026. FY2027E onward includes the SHREWD roll-off.

| | FY2024A | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|---:|---:|
| Revenue | 68.6 | 109 | 129 | 137 | 142 | 161 |
| Revenue growth | — | 58.9% | 18.4% | 6.0% | 4.2% | 13.3% |
| Gross margin | 81% | 80% | 80% | 80% | 80% | 80% |
| Adjusted EBITDA | 17.8 | 26.6 | 34.0 | 37.2 | 41.3 | 48.3 |
| EBITDA growth | — | 48.8% | 28.0% | 9.3% | 11.2% | 16.9% |
| EBITDA margin | 26.0% | 24.4% | 26.4% | 27.2% | 29.0% | 29.9% |
| *Change from v2: revenue* | | | 0.0 | −0.62 | −1.08 | −0.73 |
| *Change from v2: Adjusted EBITDA* | | | 0.0 | −0.31 | −0.54 | −0.37 |

*Source: FY2024A–FY2025A [A1][A1_1][A2][A2_1][A63][A72][C6][C7]; FY2026E–FY2029E [E1][E2][C36][S10][C22][C23][C40]. Gross margin for estimate years is the cash cost-build assumption. May not sum due to rounding.*

</div>

---

## 3. Business Description and Reporting Lines

Vitalhub sells software to health and human services providers, mainly hospitals, mental health and community care, in the United Kingdom, Canada, Australia, the United States and Western Asia [D16]. It reports one operating segment [D4]. The business grew mostly by acquisition. Revenue rose from 68.6 in FY2024 to 109 in FY2025 after the Induction Healthcare (June 2025) and Novari Health (July 2025) acquisitions [A1][A1_1][A58]. Buddy Healthcare in Finland closed on 10 July 2026 [A45]. In FY2025 the United Kingdom was 60.0 of revenue (55%), Canada 33.1, Australia 10.2 and the United States 3.34 [A53]. In Q3 2026 UK revenue fell to 14.6 from 16.6 a year earlier, the quarter in which NHS SHREWD suspensions hit, while Finland added 1.20 from Buddy [A54].

The filings report revenue in four types, which are the four forecast lines [A3_1][A4_1][A5_1][A1_1]. Term licences, maintenance and support is the recurring core: 78% of FY2025 revenue and 81% of Q3 2026 revenue [C35][A66]. Vitalhub defines ARR as annual renewable software licence fees and maintenance services. It splits ARR growth into organic additions net of churn, acquired ARR and foreign exchange, and it counts an acquired company's growth after close as organic [G24]. Virtual care is the Attend Anywhere video-consultation product that came with Induction [A4]. Perpetual licences are one-off sales, and services, hardware and other is implementation work, which is lumpy by milestone [D1].

<div class="fig" markdown="1">

**Figure 3 – FY2025A revenue by line (C$ millions)**

Term licences carry the business. Virtual care entered in mid-2025 with Induction, so FY2025 holds about half a year of it.

| Line | FY2024A | FY2025A | Share of FY2025A | Growth |
|---|---:|---:|---:|---:|
| Term licences, maintenance and support | 57.1 | 85.4 | 78.4% | 49.7% |
| Virtual care (Attend Anywhere) | — | 5.18 | 4.8% | n/a |
| Perpetual licences | 0.498 | 2.09 | 1.9% | 319% |
| Services, hardware and other | 11.0 | 16.2 | 14.9% | 47.4% |
| **Total revenue** | **68.6** | **109** | **100%** | **58.9%** |

*Source: [A3][A3_1][A4_1][A5][A5_1][A6][A6_1][A1][A1_1][C35]. May not sum due to rounding.*

</div>

Products in development are part of the term line, not separate lines. AI Scribe launched on 15 September 2026 into an installed base of about 22,000 practitioners [A70]. Management sizes AI add-ons at about 30–40 of total addressable market [G21]. Neither the filings nor the call give revenue for these products, so they enter only through the organic ARR growth rate.

---

## 4. Management

Dan Matlow has been President and Chief Executive Officer since May 2016 and a director since November 2016, and holds 726,862 shares [A55]. Before Vitalhub he ran Medworxx Solutions, which was sold to Aptean in 2015 [A55]. Directors and executive officers as a group own about 16% of the shares [A56].

The record since FY2024 is one of acquisition-led growth funded with equity. Vitalhub raised 34.5 in January 2025 at $10.90 a share and 74.8 in August 2025 at $12.70 [A57]. It added 14.6 of acquired ARR in Q4 2024, 3.87 in Q2 2025, 12.0 in Q3 2025 and 4.48 with Buddy in Q3 2026 [A28_1][A28_2][A28_3][A28_4]. No equity was raised in 2026 [A62]. The company had 129 of cash and short-term investments and no debt at 30 September 2026 [A44][A64]. It did not buy shares under its normal course issuer bid through September, which management linked to keeping room for larger acquisitions [G20].

Integration has delivered margin. Quarterly cash opex has held at about 17 since Q4 2025 (17.2, 17.8, 16.8, 17.2) while R&D fell from 9.24 in Q3 2025 to 7.49 in Q3 2026 [C32][A59]. The CFO attributed the Q3 margin rise to lower R&D, Induction and Novari synergies and favourable FX [G17]. The guidance record is thinner. Vitalhub gives no formal guidance. The one forward comfort on record, the 10%–11% organic run rate from the Q2 call, was followed by a 0.816 organic add in Q3, the weakest of the nine quarters we track [G13][A27_8]. We weight management's directional comments, but we do not take them as targets.

---

## 5. Key Developments

The Q3 2026 report on 12 November showed revenue of 31.9, flat against 32.0 a year earlier, and Adjusted EBITDA of 8.62, a 27.0% margin [A20_8][A20_4][A21_8]. Closing ARR was 107.2. Of the 5.66 increase in the quarter, 0.816 was organic, 4.48 was Buddy and 0.366 was foreign exchange [A26_8][A27_8][A28_4][D1]. Services revenue fell to 3.65 from 5.48, which management put down to summer seasonality against a busy prior-year quarter [A25_8][A25_4][G25]. Excluding a 0.592 FX gain inside Adjusted EBITDA, the Q3 margin was 25.2%, down from 26.4% in Q2 on the same basis [C29].

On the 13 November call, management said about 7%–8% of ARR sits in SHREWD, the NHS England product affected by the move to the Palantir-based Federated Data Platform (FDP) [G2]. Some suspended accounts have already been taken out of ARR and others have not [G3]. Management pointed to the FDP break clause in February 2027 [G18]. It also said it expects margins to keep rising and to reach the Rule of 40 in 2027 [G5][G6].

On 16 November the health minister told MPs that the current FDP contract will continue until March 2029 while the government procures a new version [G26]. The formal procurement starts in the second half of 2027 and takes about 18 months. It is to welcome UK small and medium-sized companies and UK sovereign AI capability as well as international providers [G27]. The government will also work with other providers on new capabilities, starting with maternity systems. The minister said migration away from the platform was "possible in principle" [G28]. For Vitalhub, the break clause that might have reopened the market in early 2027 is gone. The platform that is displacing SHREWD now has more than two more years to bed in. That is the basis for the 2027 roll-off in this version.

<div class="fig" markdown="1">

**Figure 4 – Recent events and catalysts**

Events since the start of FY2025 that move the forecast, and the next dated catalysts.

| Date | Event | Effect on the forecast | Source |
|---|---|---|---|
| 9 Jan 2025 | Bought deal, 34.5 at $10.90 | Funds 2025 acquisitions; in FY2025 cash | A57 |
| 18 Jun / 4 Jul 2025 | Induction and Novari close | Virtual care line starts; 12.0 acquired ARR in Q3 2025 | A58, A28_3 |
| 20 Aug 2025 | Bought deal, 74.8 at $12.70 | In year-0 cash | A57 |
| 10 Jul 2026 | Buddy Healthcare closes; 12.4 cash, 75,000 shares | 4.48 acquired ARR held flat in the term line | A45, A46, A28_4 |
| 7 Aug 2026 | Q2 call: 10%–11% organic comfort | Treated as withdrawn after Q3 | G13 |
| 15 Sep 2026 | AI Scribe launch | Inside organic ARR growth; no separate line | A70 |
| 12–13 Nov 2026 | Q3 results and call: organic ARR 0.816; SHREWD 7%–8% of ARR at risk | SHREWD sized at 7.5–8.6 | A27_8, G2 |
| 16 Nov 2026 | FDP contract extended to March 2029; break clause not used | Base: 4.0 of SHREWD ARR rolls off in 2027 | G26, D23 |
| Mar 2027 | Attend Anywhere renewals; FY2026 results | Virtual care band; first read on SHREWD | G9 |
| 18 Nov 2026 | ARR bridge trend reviewed (CEO bot product sheet, checked to filings) | Organic adds forecast in dollars, +10% a year | D24, C38 |
| H2 2027 | New FDP procurement opens (about 18 months) | Upside outside the window; in no case | G27, S28 |
| Mar 2029 | Current FDP contract ends | Outside the window | G26 |

*Source: as listed.*

</div>

---

## 6. Forecast

### How the evidence becomes the numbers

The base revenue and Adjusted EBITDA are the FactSet totals plus the SHREWD event adjustment. The four lines are our bottom-up build scaled to those totals. The scale factors are 0.983 for Q4 2026, 0.987 for FY2027, 0.971 for FY2028 and 1.023 for FY2029, all within 10% of 1 [C1][C2]. Buddy's acquired ARR is not scaled [S17].

**The ARR bridge trend.** Vitalhub prints a quarterly ARR bridge: organic additions net of churn, acquired ARR and foreign exchange [G24]. Figure 6 sets it out by year.

- **Dollars vs. percentages:** Organic additions were 6.39 in 2023, 6.48 in 2024 and 7.23 in 2025, and 8.12 in the four quarters to Q2 2026 [A75][A77][C38]. Opening ARR more than doubled over the same period, from 36.2 to 96.1, mostly through acquisitions: 17.9 of acquired ARR in 2024, 15.9 in 2025 and 4.48 with Buddy in 2026 [A76][A77][A28_4]. The organic rate therefore fell from 17.7% to 14.5% to 10.2%, and to 7.7% in the twelve months to Q3 2026 [C38][A78].
- **Acquired books:** If the acquired ARR had grown at the legacy rate after close, dollar additions would have risen by about 5 a year. They rose by about 0.8. In aggregate the acquired books (Induction, Novari, Strata, MedCurrent, Buddy and others) add little net organic growth after close, or they add some while the legacy book slows. The filings do not split the two.
- **Seasonality:** Q4 is the strongest quarter, averaging 1.84 over 2022–2025, followed by Q1 at 1.57, Q2 at 1.35 and Q3 at 1.28 [C38]. The 0.816 in Q3 2026 is the weakest Q3 since 2022, consistent with the SHREWD suspensions.
- **FX:** Foreign exchange added 2.09 to ARR in 2024, 1.99 in 2025 and 1.22 in the first nine months of 2026, positive in nine of the last ten quarters [C38][A75][A78]. We hold it at zero.
- **Conversion to revenue:** Term revenue has run at 0.979–0.994 of average ARR in the four quarters since Q4 2025, which supports the 0.985 we use [C39][S1]. The ratio was 1.05–1.08 in 2024, and 1.14 in Q4 2024, when 14.6 of ARR arrived in the quarter. ARR excludes virtual care [A79], so the step down is not Attend Anywhere leaving the line. The filings do not explain it.

So we forecast organic additions in dollars, not as a percentage of a base that acquisitions inflate [S29]. Dollar additions grew about 10% a year from 2023 to the four quarters to Q2 2026, the last four before the Q3 SHREWD drag.

Management commentary does not move that trend either way. On one side are the Novari and Strata pipelines, AI add-ons, "margins will continue to increase" and the Rule of 40 in 2027 [G8][G21][G5]. On the other, the 10%–11% comfort was not repeated [G13]. The base therefore grows additions 10% a year from 8.12, giving 8.94 in FY2027, 9.83 in FY2028 and 10.8 in FY2029 [S3][S4][S5].

These figures are 8.2%, 8.7% and 8.8% of opening ARR. Version 2 used 9% and 10%, which meant 9.8–12.6 of additions a year, more than Vitalhub has ever added in dollars. The flat-dollar reading, about 7 a year or 6.5% of the base, is the bear: it would mean no growth in additions at all despite the pipelines management describes. Q4 2026 adds 1.5, below the 1.88–2.61 of the last two fourth quarters because SHREWD suspensions continue [S2].

**SHREWD roll-off.** We take 4.0 of SHREWD ARR out evenly over calendar 2027, and nothing in 2028 or 2029 [S26]. That is about half of the 7.5–8.6 implied by management's "7%, 8% of our ARR" [G2][C31].

- **For a 2027 loss:** The FDP extension to March 2029 removes the February 2027 exit point [G26], and some suspended accounts are still counted in ARR [G3].
- **Against losing all of it:** SHREWD is spread "in all different pockets" [G1], and a new FDP procurement from the second half of 2027 invites UK SMEs and new capability providers [G27][G28].
- **How the loss reaches EBITDA:** Lost revenue saves only the 20% cash cost of sales [S27][G14].

Closing ARR is 108.7 at the end of FY2026, 113.6 at the end of FY2027, 123.5 at the end of FY2028 and 134.3 at the end of FY2029 [C28].

The Dan Matlow CEO bot, asked on 17 November before the FDP news, put organic ARR growth at low-to-high single digits for Q4 2026 and early 2027 [S19]. That view is simulated and not company disclosure. Net FY2027 ARR growth of 4.5% sits inside it.

Margins come from a cash cost build. Gross margin is 80% [S10][G15]. Core cash opex is the Q3 2026 run rate of 17.2 a quarter, rising 2% a year [S11][S12]. Variable opex is 30% of revenue before the SHREWD loss above 127.65 [S13][S27]. Buddy savings are 0.5 a year from FY2027 [S14], and FX is zero [S15]. On base revenue this build gives 36.3 in FY2027E, 37.1 in FY2028E and 45.1 in FY2029E. The base implies cash costs 0.9%, 4.1% and 2.8% lower, inside the 10% tolerance [C15].

<div class="fig" markdown="1">

**Figure 5 – Evidence → judgements → impact**

How each main piece of evidence moves the base numbers.

| Evidence | Judgement | Impact |
|---|---|---|
| Organic adds 6.39 / 6.48 / 7.23 / 8.12 while opening ARR doubled through acquisitions [A75][A77][C38] | Forecast organic adds in dollars, +10% a year [S29] | Bottom-up FY2029E revenue 158 (v2 162); bull lower |
| FDP extended to March 2029; break clause not used [G26] | 4.0 of SHREWD ARR rolls off evenly in 2027 [S26] | Base revenue −2.30 / −4.59 / −4.59 vs FactSet [C36] |
| SHREWD "in all different pockets"; new FDP procurement from H2 2027 [G1][G27] | No further SHREWD loss in 2028–29; no procurement revenue [S26][S28] | Loss capped at about half |
| Q2 10%–11% comfort not restated; pipelines and Rule of 40 [G13][G8][G5] | No acceleration or deceleration of the dollar trend [S29] | Base = event-adjusted Consensus |
| Term revenue 0.979–0.994 of average ARR since Q4 2025 [C39] | Keep 0.985 [S1] | Term line conversion unchanged |
| Management: 1 of ARR is about a point of Adjusted EBITDA when no cost is added [G14] | Lost SHREWD revenue saves only cost of sales [S27] | About 80% fall-through |
| Attend Anywhere "theoretically" declining; March renewals [G9] | −5% a year [S7] | Virtual care about 8.2 by FY2029E |
| Margin to "sustain, if not improve"; Rule of 40 in 2027 [G6][G5] | Accept the Consensus margin path; band it in the bear [P2] | FY2029E margin 29.9% |

*Source: as tagged.*

</div>

<div class="fig" markdown="1">

**Figure 6 – ARR bridge trend (C$ millions)**

Organic additions rose in dollars while the organic percentage fell, because acquisitions enlarged the base. The twelve-month columns overlap.

| | 2023 | 2024 | 2025 | 12 months to Q2 2026 | 12 months to Q3 2026 |
|---|---:|---:|---:|---:|---:|
| Opening ARR | 36.2 | 44.6 | 71.1 | 79.6 | 93.7 |
| Organic net of churn | 6.39 | 6.48 | 7.23 | 8.12 | 7.23 |
| Organic % of opening ARR | 17.7% | 14.5% | 10.2% | 10.2% | 7.7% |
| Acquired ARR | 1.10 | 17.9 | 15.9 | 12.0 | 4.48 |
| Foreign exchange | 0.94 | 2.09 | 1.99 | 1.82 | 1.79 |
| Closing ARR | 44.6 | 71.1 | 96.1 | 102 | 107 |

*Source: FY2024 MD&A quarterly bridge for 2023–2024 [A75][A76]; FY2025 MD&A [A77]; Q3 2026 MD&A [A78][A26_8]; Q3 2025 to Q2 2026 quarters [A27_4]–[A27_7]; indexed by the CEO bot's product sheet [D24]; calculations [C38]. 2023 opening ARR rebuilt back from 107.2 through the printed bridge. May not sum due to rounding.*

</div>

### Term licences, maintenance and support

This line is 78% of revenue and is driven by ARR. SHREWD sits inside it. Its share of revenue was 83% in FY2024 [A80] and 78% in FY2025, after virtual care became a separate line from Q2 2025 [C35]. It was 81% in Q3 2026 [A66]. Term revenue was 25.8 in Q3 2026, up 9.1% from 23.6, helped by acquired ARR [A22_8][A22_4].

The line follows closing ARR (Figure 6) at 0.985 of the average balance [S1][C39]. The 4.0 SHREWD roll-off lowers it by about 2.0 in FY2027E and about 3.9 a year after that, before scaling [S26]. Buddy's 4.48 of acquired ARR is held flat at 4.41 of revenue a year (174/365 of that in FY2026), and its growth after close sits in the organic additions, as the company defines it [S17][G24][C4]. FY2029E grows 14.3% because the Consensus total rises sharply that year. The unscaled build grows 8.7%.

<div class="fig" markdown="1">

**Term licences, maintenance and support (C$ millions)**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|---:|
| Term licences, maintenance and support | 85.4 | 100 | 108 | 114 | 130 |
| Growth | 49.7% | 17.5% | 7.7% | 5.0% | 14.3% |
| Closing ARR (base) | 96.1 | 109 | 114 | 123 | 134 |
| Organic ARR additions before SHREWD | 7.23 | 6.85 | 8.94 | 9.83 | 10.8 |
| SHREWD ARR lost in the year | — | — | 4.0 | 0.0 | 0.0 |

*Source: [A3_1][A26_5][A77][C2][C28][S1]–[S5][S17][S26][S29]. FY2026E = nine-month actual 74.3 + Q4 26.1; FY2026E additions = nine-month actual 5.35 + Q4 1.5.*

</div>

### Virtual care (Attend Anywhere)

Virtual care ran at 2.28–2.40 a quarter through 2026 [A23_4][A23_5][A23_6]. Q3 was 2.34, down 6% from 2.48 a year earlier [A23_6][A23_2]. Management said a moderate decline is possible but some new deals may offset it, with renewals in March [G9]. We hold Q4 at the Q3 level and take 5% off each year from FY2027 [S24][S7]. FY2026E is 9.32, the first full year, against 5.18 in FY2025, which held about half a year [A4_1].

<div class="fig" markdown="1">

**Virtual care (C$ millions)**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|---:|
| Virtual care | 5.18 | 9.32 | 8.77 | 8.20 | 8.21 |
| Growth | n/a | 79.7% | −5.8% | −6.5% | 0.0% |

*Source: [A4_1][A4_2][S7][S24][C2].*

</div>

### Perpetual licences

Perpetual sales are small and uneven: 0.140 in Q3 2026 against 0.996 in Q1 [A24_8][A24_6]. We take 0.5 in Q4 2026 and 2.0 a year after that, close to the FY2025–FY2026 average [S8].

<div class="fig" markdown="1">

**Perpetual licences (C$ millions)**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|---:|
| Perpetual licences | 2.09 | 2.44 | 1.97 | 1.94 | 2.05 |

*Source: [A5_1][A5_2][S8][C2].*

</div>

### Services, hardware and other

Services fell to 3.65 in Q3 2026 from 5.48 a year earlier [A25_8][A25_4]. Management said the services backlog has "never been stronger" and expects more milestones in Q4 [G7]. We put Q4 at 4.6, about the Q1 2026 level of 4.58. After that, services run at 16.5% of term revenue, close to the nine-month 2026 ratio of 16.6% [A25_6][S9]. They therefore fall with the SHREWD roll-off.

<div class="fig" markdown="1">

**Services, hardware and other (C$ millions)**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|---:|
| Services, hardware and other | 16.2 | 16.9 | 17.8 | 18.7 | 21.4 |
| Growth | 47.4% | 3.8% | 5.8% | 5.0% | 14.5% |

*Source: [A6_1][S9][C2].*

</div>

### Base case

No future acquisition is in the base. Management hopes to close another deal before year-end and has two or three targets in market [G12], but none is announced, so none is forecast [C21]. Earn-outs owed on Novari and Buddy are cash items outside Adjusted EBITDA and are not in any line.

<div class="fig" markdown="1">

**Figure 7 – Base case by line (C$ millions)**

Lines scaled to the event-adjusted Consensus totals; Buddy unscaled inside the term line.

| Line | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|---:|
| Term licences, maintenance and support | 85.4 | 100 | 108 | 114 | 130 |
| Virtual care | 5.18 | 9.32 | 8.77 | 8.20 | 8.21 |
| Perpetual licences | 2.09 | 2.44 | 1.97 | 1.94 | 2.05 |
| Services, hardware and other | 16.2 | 16.9 | 17.8 | 18.7 | 21.4 |
| **Revenue** | **109** | **129** | **137** | **142** | **161** |
| **Adjusted EBITDA** | **26.6** | **34.0** | **37.2** | **41.3** | **48.3** |
| EBITDA margin | 24.4% | 26.4% | 27.2% | 29.0% | 29.9% |

*Source: [A1_1][A2_1][C2][E1][E2][C36]. May not sum due to rounding.*

</div>

<div class="fig" markdown="1">

**Figure 8 – Cash opex and margin bridge, base (C$ millions)**

The cost build on base revenue, compared with base Adjusted EBITDA. The gap is what the base implies beyond our build.

| | Q4 2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|
| Revenue (base) | 33.4 | 137 | 142 | 161 |
| Cash cost of sales (20%) | 6.69 | 27.3 | 28.5 | 32.3 |
| Gross profit | 26.8 | 109 | 114 | 129 |
| Core cash opex | 17.2 | 70.2 | 71.6 | 73.0 |
| Buddy cost saving | 0.00 | 0.50 | 0.50 | 0.50 |
| Variable opex (30% of pre-SHREWD-loss revenue above 127.65) | 0.459 | 3.40 | 5.80 | 11.5 |
| Cost-build Adjusted EBITDA | 9.10 | 36.3 | 37.1 | 45.1 |
| Base Adjusted EBITDA | 9.23 | 37.2 | 41.3 | 48.3 |
| Gap | 0.129 | 0.867 | 4.27 | 3.20 |
| Cash cost gap | −0.5% | −0.9% | −4.1% | −2.8% |

*Source: [S10]–[S14][S27][C14][C15][C36]. Q4 2026E core opex is one quarter; full years are annualized +2% a year. May not sum due to rounding.*

</div>

The bridge shows where the margin risk sits. In FY2027E the build and the base agree to within 1. In FY2028E and FY2029E the base needs 3–4 more of Adjusted EBITDA than the build. That is equivalent to a variable opex rate of about 8% in FY2028E and 22% in FY2029E, instead of 30%. It is possible if management holds cash opex flat, as it has for four quarters [C32]. It is a judgement on top of the reported cost base, so the bear tests it.

### Contingent payments

Vitalhub receives no royalty or milestone revenue that needs a separate path. It owes earn-outs: up to 4.5 on Novari through July 2027, with 3.8 accrued, and up to 7.25 on Buddy over 30 months from July 2026, with 3.21 accrued [A49][A51]. Changes in their fair value are excluded from Adjusted EBITDA [G23]. The cash amounts are in the forecast file's dated adjustments, probability-weighted at accrued over maximum [S20][S21].

---

## 7. Valuation

Finagle values the base case at C$9.23 a share against the C$6.73 share price read from Yahoo on 18 November 2026, about 37% above (derived) [C41][D26][C42]. About 53% of that value is terminal value (derived) [C42]. The bull case is C$11.22 and the bear case C$6.83 a share, about 1% above the price; Appendix A has those cases [C41]. The Finagle bot ran this valuation (result v05) from our request plus inputs David May stated on 18 November, including the reported FY2025 Adjusted EBITDA as the year-0 level [D25][P9][P15].

### Method

Finagle discounts free cash flow to equity at the cost of equity [D25].

- **Explicit years.** It takes the FY2026E–FY2029E revenue and Adjusted EBITDA growth from the forecast file as given, compounding from year 0, FY2025A [C22][C23].
- **Extension.** Finagle extends those four explicit years by six more, FY2030E–FY2035E, to a ten-year horizon. Revenue in those years starts at 8.0% next-period growth and fades toward terminal growth. EBITDA grows from the starting margin, with each extra dollar of revenue earning the 50% incremental margin [S6][S16][C41].
- **Terminal value.** A terminal value is added at the end of FY2035E.
- **Rates.** Terminal growth of 3.81% and the 9.31% cost of equity are Finagle's own defaults, derived from the 3.81% risk-free rate David chose. We did not set either [P10][S30].
- **Cash flow.** Free cash flow to equity is positive in every year of every case, so no year needs funding and no year-0 raise applies [C42][P3].

### Balance Sheet Adjustments

Year-0 cash of 99.79 equals the opening 106.81 plus the present value below. The share count of 63,307,054 equals the opening count, with no new shares [C41].

- **Openings.** These are David's stated figures [P12]:
  - **Cash:** FY2025 cash and short-term investments of 119.18, less the 12.37 Buddy closing cash.
  - **Shares:** 63,232,054 at FY2025, plus the 75,000 Buddy consideration shares.
- **No double count.** The Buddy closing cash and shares are already in those openings, so they were taken off the schedule and are not added again.
- **Outside EBITDA.** These dollars sit outside EBITDA and are not in a later cash-flow year.

The schedule is the same in all three cases.

<div class="fig" markdown="1">

**Balance Sheet Adjustments – all cases (C$ millions unless noted)**

| Item | Amount | Timing | Probability | Discount | Present value | Shares issued (millions) |
|---|---:|---|---:|---:|---:|---:|
| Contingent consideration paid in 9M 2026 | −0.781 | 2026-09-30 | 1.00 | 1.0000 | −0.781 | 0.000 |
| Novari earn-out (maximum) | −4.50 | 2027-07-04 | 0.844 | 0.9459 | −3.59 | 0.000 |
| Buddy earn-out (maximum) | −7.25 | 2029-01-10 | 0.442 | 0.8261 | −2.65 | 0.000 |
| **Total present value / new shares** | | | | | **−7.02** | **0.000** |
| Opening cash / shares | | | | | 106.81 | 63.307 |
| **Year-0 cash / shares used** | | | | | **99.79** | **63.307** |

*Source: worked schedule in the valuation result [D25][C41]; items from the forecast file [S25][A48][A49][A51][S20][S21]; openings [A40][A41][A45][A46][P12]. Discount at the 9.31% cost of equity from the 18 November 2026 price date. May not sum due to rounding.*

</div>

Figure 9 sets out each valuation input and who set it. David stated the rates, the debt treatment and the year-0 figures. The Forecaster's judgements are the growth paths, the starting and incremental margins and next-period growth. The rest are Finagle's defaults.

<div class="fig" markdown="1">

**Figure 9 – Valuation inputs, three cases (C$ millions unless noted)**

| Input | Bull | Base | Bear | Set by |
|---|---:|---:|---:|---|
| Revenue growth FY2026E–FY2029E | 18.5 / 8.4 / 6.0 / 14.0% | 18.4 / 6.0 / 4.2 / 13.3% | 18.3 / 1.9 / 0.2 / 11.3% | Forecaster [C22][C27] |
| EBITDA growth FY2026E–FY2029E | 29.1 / 20.3 / 17.1 / 19.1% | 28.0 / 9.3 / 11.2 / 16.9% | 27.1 / −4.3 / 0.0 / 13.0% | Forecaster [C23][C27] |
| Starting margin, FY2029E | 34.0% | 29.9% | 24.9% | Forecaster [C24][C27] |
| Incremental margin | 60% | 50% | 40% | Forecaster [S16] |
| Next-period growth, FY2030E | 9.2% | 8.0% | 5.2% | Forecaster [S6] |
| Year-0 revenue (Yahoo) / EBITDA (reported, before SBC) | 109.0 / 26.6 | 109.0 / 26.6 | 109.0 / 26.6 | Finagle / David [D26][P15] |
| Year-0 D&A for capex | 1.27 | 1.27 | 1.27 | David [P13] |
| Capex path | method 1 | method 1 | method 1 | Finagle default [C43] |
| Risk-free rate | 3.81% | 3.81% | 3.81% | David [P10] |
| Cost of equity | 9.31% | 9.31% | 9.31% | Finagle, derived [S30] |
| Terminal growth | 3.81% | 3.81% | 3.81% | Finagle, derived [S30] |
| Tax rate | 26.5% | 26.5% | 26.5% | David [P11] |
| Debt / policy | 0, held | 0, held | 0, held | David [P11] |
| Cost of debt | 2.8% | 2.8% | 2.8% | Forecaster proposal [P14] |
| Terminal ROIC | 15% | 15% | 15% | Finagle default [S30] |
| Working-capital change / distribution | zero / none | zero / none | zero / none | Finagle default [S30] |
| Price (C$ per share) | 6.73 | 6.73 | 6.73 | Finagle fetch [D26] |
| Year-0 cash after schedule / shares (millions) | 99.79 / 63.307 | 99.79 / 63.307 | 99.79 / 63.307 | David + schedule [P12][C41] |

*Source: valuation result [D25][C41]; forecast file leaves as tagged. Growth paths and margins in percent.*

</div>

The growth paths and margins are the Forecaster's leaves, set as described in Section 6 and Appendix A. The starting margin is the last explicit year's EBITDA divided by revenue, and Finagle carries the forecast's 29.9% past FY2029E because its year-0 EBITDA is now the reported 26.6 [C44]. The incremental margin is one minus the 20% cash cost of sales minus the 30% variable opex rate. The bull and bear move that rate to 20% and 40% [S16][S13].

**Run record.**

- **Prompt inputs**, each tagged [P] and dated 18 November 2026:
  - **Risk-free rate:** 3.81%, "3.81% use this" [P10].
  - **Debt and tax:** debt 0, held, with leases excluded, and a 26.5% tax rate. David's words: "Rerun VHI as v03 with capex at the FY25 ratio of revenue, no debt (leases excluded), 26.5% tax, and no cash from the Buddy consideration shares." [P11]
  - **Opening cash and shares:** cash 106.81 and 63,307,054 shares. David's words: "cash should be from the 2025 filling adjusted for the cash price of Buddy (+$12.37). shares should be from the 2025 filling (63.23M) adjusted for Buddy (+0.075M). Isn't that logical?" The Buddy cash is applied as an outflow, and the Buddy items were removed from the schedule [P12].
  - **Year-0 D&A:** 1.271558, which excludes amortization of acquired intangibles so that the method-1 capex rule runs on depreciation only. David's words: "remove the "amortization of intangible assets" when calculating capex using method 1." [P13]
  - **Year-0 EBITDA:** 26.554099, Vitalhub's reported FY2025 Adjusted EBITDA, with the EBITDA definition set to before stock-based compensation. This replaces Yahoo's 25.898. David's words: "Yes, do the quick fix" [P15][A2_1].
  - **Cost of debt:** 2.8%. This was proposed by the Forecaster, and David did not object; it is not his own figure. It has no effect, because debt is zero and forecast-year interest is zero [P14].
- **Defaults filled** (result list): baseline.noa, baseline.nol, debt.start_year, distribution.mode, forecast.dwc.mode, rates.gt, rates.re, rates.roict, year [S30]. Each case also lists the earlier build_baseline defaults for tax, cost of debt and debt policy, which the prompt inputs replaced.
- **Sanity flags:** none.
- **Validation warnings, in the result's words.** Base: "average EBITDA growth is 16.4% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero." The bull warning is the same at 21.4%; the bear has none.
- **What the warning means for the base case.** The FY2026E growth includes Buddy, which closed in July 2026. Its purchase price is already in the opening cash and the earn-out schedule, so leaving the deal out of Finagle's acquisitions does not drop its cost.
- **Result flags.** "rates.rd provenance: Forecaster proposal without an explicit David quote (applied as given; see rd_provenance)" and "year-0 capex remains Yahoo 0.423144 vs method-1 ratio on new D&A (1.271558 / revenue)" [C41].
- **Fetched inputs:** price C$6.73 from Yahoo, dated 18 November 2026 [D26]. The risk-free rate is the prompt figure, from the Bank of Canada [D27].
- **Run details:** Finagle commit 377f177b. Request v05, sha256 ba766900…9b6446. Run at 14:33 ET [D25].

### Medium-term organic growth

The medium-term organic growth forecast (gsnext) is 8.0% for FY2030E in the base. It is one more year of the same build:

- **Term licences:** organic ARR additions grow another 10% to 11.9 [S6][S29].
- **Virtual care:** falls 5%.
- **Perpetual licences:** flat.
- **Services:** 16.5% of term revenue.

The three leaves are set this way:

- **Starting margin (me):** the FY2029E EBITDA margin.
- **Incremental margin (mc):** the contribution margin. It did not move in this update.
- **Next-period growth (gsnext):** comes from section 2f of the forecaster method.

Management's commentary stops before 2030, so no phrase sets the year. The bull grows additions 15% to 14.2, giving 9.2%. The bear keeps them flat at 7.23, giving 5.2% [S6].

<div class="fig" markdown="1">

**Figure 10 – Medium-term organic growth, base case (C$ millions)**

| Line | FY2029E | FY2030E | Growth |
|---|---:|---:|---:|
| Term licences, maintenance and support | 130 | 141 | 8.8% |
| Virtual care | 8.21 | 7.80 | −5.0% |
| Perpetual licences | 2.05 | 2.05 | 0.0% |
| Services, hardware and other | 21.4 | 23.3 | 8.8% |
| **Revenue** | **161** | **174** | **8.0%** |

*Source: [S6][C2]. FY2030E is a Finagle input (next-period growth), not an explicit forecast year. May not sum due to rounding.*

</div>

<div class="fig" markdown="1">

**Figure 11 – Value bridge, three cases (C$ millions unless noted)**

| | Bull | Base | Bear |
|---|---:|---:|---:|
| Year-0 cash after schedule | 99.8 | 99.8 | 99.8 |
| PV of free cash flow to equity, FY2026E–FY2029E (derived) | 78.5 | 71.2 | 61.3 |
| PV of free cash flow to equity, FY2030E–FY2035E (derived) | 132 | 104 | 71.2 |
| PV of terminal value (derived, residual) | 400 | 309 | 200 |
| **Equity value (derived)** | **710** | **584** | **432** |
| Shares (millions) | 63.307 | 63.307 | 63.307 |
| **Value per share (C$)** | **11.22** | **9.23** | **6.83** |
| Share price (C$) | 6.73 | 6.73 | 6.73 |
| Value vs price (derived) | +67% | +37% | +1.4% |
| Terminal share of value (derived) | 56% | 53% | 46% |

*Source: value per share, shares, cash and the year paths from the valuation result [D25][C41]; present values derived at the 9.31% cost of equity [C42]. May not sum due to rounding.*

</div>

The spread comes from the operating path. The bull adds EBITDA from faster dollar additions and a smaller SHREWD loss, and the bear removes it. Cash and the rates are the same in every case.

The value per share is the result for the case, not a row of the statement below. Free cash flow to equity is EBITDA less capex, stock comp, cash tax and interest. It equals the yearly change in Finagle's cash balance (derived).

<div class="fig" markdown="1">

**Figure 12 – Finagle base-case statement, FY2025A–FY2030E (C$ millions)**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E |
|---|---:|---:|---:|---:|---:|---:|
| Revenue | 109 | 129 | 137 | 142 | 161 | 174 |
| EBITDA | 26.6 | 34.0 | 37.2 | 41.3 | 48.3 | 54.8 |
| EBITDA margin | 24.4% | 26.4% | 27.2% | 29.0% | 29.9% | 31.4% |
| Stock-based compensation | 2.65 | 3.39 | 3.71 | 4.12 | 4.82 | 5.46 |
| D&A (excl. acquired intangibles) | 1.27 | 1.51 | 1.60 | 1.66 | 1.88 | 2.03 |
| Capex | 0.42 | 3.00 | 3.99 | 4.73 | 7.17 | 8.83 |
| Cash tax | −0.21 | 7.71 | 8.44 | 9.42 | 11.0 | 12.5 |
| Interest | 0.07 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Free cash flow to equity (derived) | — | 19.9 | 21.0 | 23.1 | 25.3 | 28.0 |
| Debt | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| Cash balance | 99.8 | 120 | 141 | 164 | 189 | 217 |

*Source: result paths and notebook replay [D25][C41][C42]. FY2025A cash is after the schedule. Year-0 tax is Yahoo's provision (a small credit). May not sum due to rounding.*

</div>

<div class="fig" markdown="1">

**Figure 12 (continued) – Finagle base-case statement, FY2031E–FY2035E (C$ millions)**

| | FY2031E | FY2032E | FY2033E | FY2034E | FY2035E |
|---|---:|---:|---:|---:|---:|
| Revenue | 187 | 199 | 211 | 222 | 232 |
| EBITDA | 61.2 | 67.3 | 73.2 | 78.7 | 83.7 |
| EBITDA margin | 32.7% | 33.8% | 34.7% | 35.4% | 36.1% |
| Stock-based compensation | 6.10 | 6.71 | 7.30 | 7.85 | 8.35 |
| D&A (excl. acquired intangibles) | 2.18 | 2.33 | 2.46 | 2.59 | 2.71 |
| Capex | 10.5 | 12.1 | 13.6 | 15.0 | 16.3 |
| Cash tax | 14.0 | 15.4 | 16.8 | 18.1 | 19.3 |
| Free cash flow to equity (derived) | 30.6 | 33.1 | 35.5 | 37.8 | 39.8 |
| Cash balance | 248 | 281 | 316 | 354 | 394 |

*Source: result paths and notebook replay [D25][C41][C42]. Debt and interest are zero throughout. May not sum due to rounding.*

</div>

Three points about the statement:

- **EBITDA matches the forecast.** The explicit-year EBITDA now equals our forecast (FY2026E base 34.000), because Finagle compounds the forecast growth from the stated year-0 Adjusted EBITDA of 26.554 [C44][P15].
- **Stock comp.** Year-0 stock comp is still Yahoo's 2.648. The stock comp to EBITDA ratio that Finagle holds therefore moves to 0.0997, from 0.1022 in v04. Stock comp dollars are unchanged through FY2029E and slightly lower after [C44].
- **Cash build-up.** Cash builds to 394 by FY2035E because distribution is "none". The value counts each year's free cash flow to equity once, so this is not double counted.

<div class="fig" markdown="1">

**Figure 13 – Capex path by case (C$ millions unless noted)**

| | FY2025A | FY2026E | FY2027E | FY2028E | FY2029E | FY2035E | FY2035E capex / D&A | FY2035E capex / EBITDA |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bull | 0.42 | 3.24 | 4.75 | 5.92 | 8.82 | 20.5 | 6.9x | 19.0% |
| Base | 0.42 | 3.00 | 3.99 | 4.73 | 7.17 | 16.3 | 6.0x | 19.4% |
| Bear | 0.42 | 2.97 | 3.28 | 3.31 | 5.20 | 11.0 | 4.9x | 20.1% |
| Reported FY2025A capex / EBITDA | 1.6% | | | | | | | |

*Source: result capex and D&A paths [D25][C43]; FY2025 purchase of property and equipment [A82]; ratios derived. Capex/D&A in multiples, capex/EBITDA in percent.*

</div>

### Caveats

- **Capex is the largest judgement inside this value.** Vitalhub spent 0.42 on property and equipment in FY2025, about 1.6% of EBITDA [A82][C43].
  - Finagle's method-1 rule ends at terminal capex of 16.3 in the base, about 6x terminal D&A of 2.71, and 19%–20% of EBITDA by FY2035E in every case.
  - The rule sets terminal capex as depreciation plus growth reinvestment at a 15% terminal return on invested capital. With 3.81% growth and a 26.5% tax rate, about 14.1 of the 16.3 is growth capex.
  - For a software company that grows through R&D, which is expensed inside EBITDA, and through acquisitions, which this value does not model, that reinvestment counts the cost of growth a second time. It probably understates value.
  - David's year-0 D&A input already removed the larger distortion of v02, a rule anchored on acquired-intangible amortization [P13]. The growth-capex term remains.
  - We did not resize it. A stated capex path would need a year-by-year list from David.
- **Terminal value.** About 53% of the base value (46%–56% across cases) is terminal value at 3.81% growth (derived) [C42].
- **Stock comp and working capital.** Stock comp is deducted at about 10% of EBITDA throughout. Working capital is held flat.
- **What is not in the value:**
  - acquisitions beyond Buddy, although management is in market [G12];
  - the funding of any such deal;
  - any SHREWD loss beyond the case assumptions;
  - FX.
- **Earn-outs.** These are weighted at accrued over maximum. The maximum Buddy earn-out would cost a further 4.04 undiscounted (derived) [S20].
- **Price date.** The C$6.73 price is the Yahoo price dated 18 November 2026 [D26].
- **No rating.** This report draws no rating or price target.

---

## 8. Risks

- **NHS SHREWD.** About 7.5–8.6 of ARR depends on NHS England decisions around the FDP, which now runs to March 2029 [C31][G26]. The base loses 4.0 in 2027 and the bear loses all of it. A faster switch by trusts, or a 2028 tail the evidence does not yet show, would push results toward the bear.
- **UK concentration and FX.** 55% of FY2025 revenue was in the United Kingdom [A53]. Revenue is reported in C$ but earned largely in GBP and AUD. FX gains and losses sit inside Adjusted EBITDA, and the Q3 2026 gain of 0.592 lifted the margin by 1.9 points [G23][C29]. We found no hedging programme in the filings reviewed.
- **Margin path.** The base margins of 29.0%–29.9% in FY2028–29 exceed anything reported. They need flat costs on rising revenue (Figure 8).
- **Organic additions.** The base assumes dollar additions keep growing about 10% a year. The twelve months to Q3 2026 printed 7.23, the same as FY2025, with the SHREWD drag included [A78][C38]. If additions stay flat once SHREWD is out of the numbers, the outcome moves toward the bear.
- **Attend Anywhere renewals** in March each year [G9].
- **Acquisitions.** Management is in market for further deals [G12]. A deal changes the revenue path, and an equity-funded one changes the share count. Neither is forecast.
- **Consensus quality and timing.** The FactSet figures are whole numbers with no analyst count, and they probably predate the FDP news [D17]. When analysts update, the base should move back toward their numbers, not ours.

---

## Appendix A – Bull and bear cases

The three cases differ in three levers: the SHREWD roll-off together with organic ARR additions in dollars, the cost build, and Attend Anywhere [S18]. Each scenario total is the base plus the difference between the scenario's bottom-up build and the base build. The cases therefore differ only by those levers, and they inherit the shape of the Consensus path. The unscaled bottom-up totals are shown as a sensitivity [C33].

**Why the bands are where they are.**

- **Bear: flat additions and all SHREWD lost.** Organic additions stay at 7.23 a year, the FY2025 printed figure [A77]. That is the flat-dollar reading of the ARR bridge, and it puts organic growth at about 6.5%–6.7% of opening ARR. On top of that, all 8.0 of SHREWD ARR rolls off evenly in 2027 as trusts move onto the extended FDP [S22][G26]. A loss before 2027 is possible, but the March renewal cycle and management's "another quarter or so" point to 2027.
- **Bull: faster additions and a limited SHREWD loss.** Additions grow 15% a year, from 9.34 in FY2027 to 12.4 in FY2029. That is about the pace from 2024 to the four quarters to Q1 2026 (6.48 to 8.18), and it requires the Strata pipeline and AI add-ons to convert [G8][G21]. Only 1.5 of SHREWD rolls off: the accounts already suspended but still counted [G3].
- **No procurement win in any case.** A role in the new FDP procurement would earn revenue mostly after FY2029 [S28][G27].
- **Cost band.** The band follows management's rule that 1 of ARR is about a point of Adjusted EBITDA when no cost is added [G14]. The bull charges 20% of each new dollar to opex and doubles the Buddy savings to 1.0. The bear charges 40% and gets no Buddy saving. Lost SHREWD revenue saves only cost of sales in every case [S27].
- **Attend Anywhere.** Flat in the bull and down 15% a year in the bear [S7].
- **Bear margin.** The bear's FY2029 margin is 24.9%, about the FY2025 level, and it bands the above-history base margin [P2]. On its own unscaled build the bear margin is about 22%.
- **Why the v3 bear sits above the v2 bear in FY2028–29.** The base stays on Consensus while our base build came down, so the bear-minus-base lever gap narrowed. On unscaled builds the bear is almost unchanged from version 2.
- **Variables held fixed across cases.** Gross margin 80%, core opex inflation 2%, term/ARR 0.985 and services at 16.5% of term. Their bands (78%–82%, 1%–3%, 0.975–0.995, 15%–19%) each move FY2029 EBITDA by less than the two main levers.

<div class="fig" markdown="1">

**Figure 14 – Headline scenarios (C$ millions)**

| | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|
| Revenue – bull | 129 | 140 | 148 | 169 |
| Revenue – base | 129 | 137 | 142 | 161 |
| Revenue – bear | 129 | 131 | 132 | 146 |
| Adj. EBITDA – bull | 34.3 | 41.2 | 48.3 | 57.5 |
| Adj. EBITDA – base | 34.0 | 37.2 | 41.3 | 48.3 |
| Adj. EBITDA – bear | 33.7 | 32.3 | 32.3 | 36.5 |
| Margin – bull | 26.6% | 29.5% | 32.6% | 34.0% |
| Margin – base | 26.4% | 27.2% | 29.0% | 29.9% |
| Margin – bear | 26.2% | 24.6% | 24.6% | 24.9% |
| Organic adds – bull / base / bear | — | 9.34 / 8.94 / 7.23 | 10.7 / 9.83 / 7.23 | 12.4 / 10.8 / 7.23 |
| SHREWD ARR lost in 2027 – bull / base / bear | — | 1.5 / 4.0 / 8.0 | — | — |
| Closing ARR – bull / base / bear | 110 / 109 / 108 | 118 / 114 / 107 | 128 / 123 / 114 | 141 / 134 / 121 |
| Change from v2, revenue – bull / base / bear | 0 / 0 / 0 | −1.07 / −0.62 / −0.31 | −2.40 / −1.08 / +0.93 | −2.72 / −0.73 / +3.27 |
| Change from v2, EBITDA – bull / base / bear | 0 / 0 / 0 | −0.63 / −0.31 / −0.14 | −1.52 / −0.54 / +0.45 | −1.94 / −0.37 / +1.62 |
| Sensitivity: unscaled bottom-up revenue, bull / bear | 130 / 129 | 142 / 133 | 152 / 136 | 166 / 143 |
| Sensitivity: unscaled bottom-up EBITDA, bull / bear | 34.4 / 33.9 | 41.2 / 32.3 | 46.1 / 30.1 | 52.6 / 31.5 |

*Source: scenarios in `forecast.json` [S18][S22][S26][S29][C28][C33][C40]. May not sum due to rounding.*

</div>

<div class="fig" markdown="1">

**Figure 15 – Key assumptions and bands**

| Driver | Bear | Base | Bull | Basis |
|---|---|---|---|---|
| Organic ARR adds before SHREWD, FY27 / FY28 / FY29 | 7.23 flat | 8.94 / 9.83 / 10.8 | 9.34 / 10.7 / 12.4 | Dollar adds 6.39 → 8.12, about +10% a year [S29][C38] |
| Growth in dollar adds a year | 0% | 10% | 15% | 2023–2026 trend; 2024–Q1 2026 pace [S29] |
| SHREWD ARR lost, evenly over 2027 | 8.0 (all) | 4.0 (about half) | 1.5 | 7%–8% of ARR; FDP to March 2029 [S26][S22][G26] |
| SHREWD ARR lost in 2028–29 | 0 | 0 | 0 | No evidence of a later tail [S26] |
| FDP procurement revenue | 0 | 0 | 0 | Award around 2029 at the earliest [S28][G27] |
| Q4 2026 organic ARR add | 0.5 | 1.5 | 2.5 | Q3 0.816; Q4 average 1.84 [S2][C38] |
| Fall-through of lost SHREWD revenue | 80% | 80% | 80% | Saves only cost of sales [S27][G14] |
| Virtual care growth a year | −15% | −5% | 0% | Q3 −6% YoY; March renewals [S7] |
| Variable opex on pre-loss revenue above 127.65 | 40% | 30% | 20% | 1 of ARR ≈ 1 point of margin [S13][G14] |
| Buddy cost saving a year | 0 | 0.5 | 1.0 | Breakeven at close; 6–12 months [S14] |
| Contribution margin mc | 0.40 | 0.50 | 0.60 | 1 − 20% COGS − variable opex [S16] |
| Next-year growth (gsnext) | 5.2% | 8.0% | 9.2% | One more year of the build [S6] |
| Held fixed: GM 80%; inflation 2%; term/ARR 0.985; services 16.5% of term | — | — | — | Bands 78–82%, 1–3%, 0.975–0.995, 15–19% [S10][S12][S1][S9] |

*Source: as tagged; `drivers.csv`.*

</div>

<div class="fig" markdown="1">

**Figure 16 – Bull and bear line builds (C$ millions)**

| Line | Case | FY2026E | FY2027E | FY2028E | FY2029E |
|---|---|---:|---:|---:|---:|
| Term licences, maintenance and support | Bull | 101 | 111 | 118 | 135 |
| | Bear | 100 | 104 | 106 | 119 |
| Virtual care | Bull | 9.32 | 9.24 | 9.12 | 9.54 |
| | Bear | 9.32 | 7.84 | 6.52 | 5.93 |
| Perpetual licences | Bull | 2.44 | 1.97 | 1.94 | 2.05 |
| | Bear | 2.44 | 1.97 | 1.94 | 2.05 |
| Services, hardware and other | Bull | 16.9 | 18.2 | 19.4 | 22.3 |
| | Bear | 16.9 | 17.2 | 17.4 | 19.6 |
| **Revenue** | Bull | **129** | **140** | **148** | **169** |
| | Bear | **129** | **131** | **132** | **146** |

*Source: scenario lines in `forecast.json` [S18][C25]. May not sum due to rounding.*

</div>

<div class="fig" markdown="1">

**Figure 17 – Cash opex bridge, bull (bottom-up, C$ millions)**

| | Q4 2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|
| Revenue (bull bottom-up) | 34.1 | 142 | 152 | 166 |
| Cash cost of sales (20%) | 6.83 | 28.3 | 30.5 | 33.1 |
| Core cash opex | 17.2 | 70.2 | 71.6 | 73.0 |
| Buddy cost saving | 0.00 | 1.00 | 1.00 | 1.00 |
| Variable opex (20% of pre-loss revenue above 127.65) | 0.45 | 2.99 | 5.29 | 7.94 |
| Adjusted EBITDA (bottom-up) | 9.67 | 41.2 | 46.1 | 52.6 |
| Margin | 28.3% | 29.1% | 30.2% | 31.7% |

*Source: [S13][S14][S16][S18][S27][C33]. Headline bull EBITDA in Figure 14 adds the base Consensus-minus-build gap. May not sum due to rounding.*

</div>

<div class="fig" markdown="1">

**Figure 18 – Cash opex bridge, bear (bottom-up, C$ millions)**

| | Q4 2026E | FY2027E | FY2028E | FY2029E |
|---|---:|---:|---:|---:|
| Revenue (bear bottom-up) | 33.9 | 133 | 136 | 143 |
| Cash cost of sales (20%) | 6.78 | 26.6 | 27.1 | 28.6 |
| Core cash opex | 17.2 | 70.2 | 71.6 | 73.0 |
| Buddy cost saving | 0.00 | 0.00 | 0.00 | 0.00 |
| Variable opex (40% of pre-loss revenue above 127.65) | 0.79 | 4.01 | 6.85 | 9.77 |
| Adjusted EBITDA (bottom-up) | 9.13 | 32.3 | 30.1 | 31.5 |
| Margin | 26.9% | 24.3% | 22.2% | 22.1% |

*Source: [S13][S14][S16][S22][S27][C33]. May not sum due to rounding.*

</div>

---

## Appendix B – Numbered sources

Tags in the text resolve here; the full list, including every quarterly figure, is in `forecast.md` and `forecast.json`. Page numbers are PDF pages of the original SEDAR filing (via OTC Markets).

**Documents**

- **D1** Vitalhub Corp., Interim MD&A for the three and nine months ended September 30, 2026, filed 2026-11-12 (SEDAR, PDF via OTC Markets; PDF page numbers) (https://www.otcmarkets.com/filing/607877/content)
- **D2** Vitalhub Corp., Interim condensed consolidated financial statements, three and nine months ended September 30, 2026, filed 2026-11-12 (PDF page numbers) (https://www.otcmarkets.com/filing/607876/content)
- **D3** Vitalhub Corp., Annual MD&A for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers) (https://www.otcmarkets.com/filing/538307/content)
- **D4** Vitalhub Corp., Audited consolidated financial statements for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers) (https://www.otcmarkets.com/filing/538304/content)
- **D5** Vitalhub Corp., Annual MD&A for the year ended December 31, 2024, filed 2025-03-27 (PDF page numbers) (https://www.otcmarkets.com/filing/449868/content)
- **D6** Vitalhub Corp., Interim MD&A, three and nine months ended September 30, 2025, filed 2025-11-06 (PDF page numbers) (https://www.otcmarkets.com/filing/505549/content)
- **D7** Vitalhub Corp., Interim MD&A, three and six months ended June 30, 2026, filed 2026-08-06 (PDF page numbers) (https://www.otcmarkets.com/filing/583610/content)
- **D8** Vitalhub Corp., Interim MD&A, three months ended March 31, 2026, filed 2026-05-07 (PDF page numbers) (https://www.otcmarkets.com/filing/560702/content)
- **D11** Vitalhub Corp., Interim MD&A, three and nine months ended September 30, 2024, filed 2024-11-13 (PDF page numbers) (https://www.otcmarkets.com/filing/424935/content)
- **D12** Seeking Alpha, "Vitalhub Corp. (VHI:CA) Q3 2026 Earnings Call Transcript", call held 2026-11-13 (HTML; no page numbers; text read from the ceochat mirror companies/vhi/sources/calls/seeking-alpha/2026-Q3.md at commit 8f8b44f; Seeking Alpha link unverified) (https://seekingalpha.com/article/4967874-vitalhub-corp-vhi-ca-q3-2026-earnings-call-transcript)
- **D13** Seeking Alpha, "Vitalhub Corp. (VHI:CA) Q2 2026 Earnings Call Transcript", call held 2026-08-07 (HTML; no page numbers; text read from the ceochat mirror 2026-Q2.md; link unverified) (https://seekingalpha.com/article/4933144-vitalhub-corp-vhi-ca-q2-2026-earnings-call-transcript)
- **D15** Vitalhub Corp., news release "VitalHub Reports Third Quarter 2026 Results", 2026-11-12 (PDF) (https://www.otcmarkets.com/filing/607875/content)
- **D16** Vitalhub Corp., Annual Information Form for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers) (https://www.otcmarkets.com/filing/538308/content)
- **D17** Markets Insider, "Vitalhub Estimates in CAD" (source: FactSet), pulled 2026-11-17; the Q3 2026 column shows as reported, so the pull is post-release (HTML; no page numbers) (https://markets.businessinsider.com/stocks/vhibf-stock)
- **D18** StockAnalysis, "Vitalhub (TSX:VHI) Stock Forecast" (S&P Global Market Intelligence), last updated 2026-11-17 (HTML) (https://stockanalysis.com/quote/tsx/VHI/forecast/)
- **D19** Vitalhub Corp., news release "VitalHub Announces Expansion of AI Capabilities with Launch of AI Scribe", 2026-09-15 (PDF) (https://www.otcmarkets.com/filing/593890/content)
- **D22** Dan Matlow CEO bot (David May's CEO-simulation bot for Vitalhub), answers relayed 17 Nov 2026; simulated view built from public material, not company disclosure (link unverified) (https://github.com/mtlr05/ceochat/tree/main/companies/vhi)
- **D23** The Register (Lindsay Clark), "MPs ask what the break clause was for as Palantir wins two more years in the NHS", published 17 Nov 2026 10:15 UTC (HTML; no page numbers; fetched 17 Nov 2026) (https://www.theregister.com/public-sector/2026/11/17/mps-ask-what-the-break-clause-was-for-as-palantir-wins-two-more-years-in-the-nhs/5310348)
- **D24** Dan Matlow CEO bot product sheet "Term licences, maintenance and support" (ceochat companies/vhi/sources/products/term-licences-maintenance-and-support.md at commit 25246c9, read 18 Nov 2026): TLMS revenue 2019 Q1-2026 Q3 and the ARR bridge by quarter, each row citing the printed SEDAR filing (OTC Markets URL). Used as an index; figures cited here were checked in the filings D1, D3, D5 (link unverified) (https://github.com/mtlr05/ceochat/blob/main/companies/vhi/sources/products/term-licences-maintenance-and-support.md)
- **D25** Finagle valuation result v05 for VHI.TO (finagle-run/valuation_result_v05.json; request valuation_request_v05.json, sha256 ba766900bf9dd16f1178d9a00f12325b518624426d9b84fca32e4a52509b6446), run by the Finagle bot on 18 Nov 2026 14:33 ET with mtlr05/finagle at commit 377f177b4013e713fe7c4603962e5f883a67e298; notebooks notebook_base/bull/bear_v05.py in the same folder (https://github.com/mtlr05/finagle)
- **D26** Yahoo Finance quote for VHI.TO as fetched by Finagle (results v04/v05, price_date 2026-11-18, v04 and v05): C$6.73, Yahoo previous close (HTML/API) (https://finance.yahoo.com/quote/VHI.TO/)
- **D27** Bank of Canada Valet, BD.CDN.10YR.DQ.YLD, Government of Canada 10-year benchmark bond yield: 3.81% on 16 Nov 2026 (JSON, read 18 Nov 2026) (https://www.bankofcanada.ca/valet/observations/BD.CDN.10YR.DQ.YLD/json?recent=5)

**Actuals**

- **A1** Revenue FY2024: C$68,594,310. (D5; p.5)
- **A1_1** Revenue FY2025: C$108,966,918. (D3; p.5)
- **A1_2** Revenue nine months to 30 Sep 2026: C$95,557,489. (D1; p.5)
- **A2** Adjusted EBITDA FY2024: C$17,840,272. (D5; p.5)
- **A2_1** Adjusted EBITDA FY2025: C$26,554,099. (D3; p.5)
- **A2_2** Adjusted EBITDA nine months to 30 Sep 2026: C$24,772,636. (D1; p.5)
- **A3** Term licences, maintenance and support, FY2024: C$57,070,350 (reported). (D5; p.6)
- **A3_1** Term licences, maintenance and support, FY2025: C$85,442,864 (reported). (D3; p.6)
- **A4** No virtual care revenue before the Induction acquisition (June 2025); FY2025 MD&A shows prior-year virtual care of 0. (D3; p.7)
- **A4_1** Virtual care term licences (Attend Anywhere), FY2025: C$5,184,921 (reported). (D3; p.7)
- **A4_2** Virtual care term licences (Attend Anywhere), nine months to 30 Sep 2026: C$7,018,965 (reported). (D1; p.7)
- **A5** Perpetual licences, FY2024: C$498,274 (reported). (D5; p.7)
- **A5_1** Perpetual licences, FY2025: C$2,089,242 (reported). (D3; p.7)
- **A5_2** Perpetual licences, nine months to 30 Sep 2026: C$1,944,450 (reported). (D1; p.7)
- **A6** Services, hardware and other, FY2024: C$11,025,686 (reported). (D5; p.7)
- **A6_1** Services, hardware and other, FY2025: C$16,249,891 (reported). (D3; p.7)
- **A20** Q3FY24 revenue: C$16,509,135. (D11; p.5)
- **A20_4** Q3FY25 revenue: C$32,044,030. (D6; p.5)
- **A20_8** Q3FY26 revenue: C$31,913,575. (D1; p.5)
- **A21_8** Q3FY26 Adjusted EBITDA: C$8,619,958. (D1; p.5)
- **A22_4** Q3FY25 term licences, maintenance and support: C$23,627,391. (D6; p.6)
- **A22_8** Q3FY26 term licences, maintenance and support: C$25,783,746. (D1; p.6)
- **A23_2** Q3FY25 virtual care: C$2,479,354. (D6; p.7)
- **A23_4** Q1FY26 virtual care: C$2,398,653. (D8; p.7)
- **A23_5** Q2FY26 virtual care: C$2,282,218. (D7; p.7)
- **A23_6** Q3FY26 virtual care: C$2,338,094. (D1; p.7)
- **A24_6** Q1FY26 perpetual licences: C$995,851. (D8; p.7)
- **A24_8** Q3FY26 perpetual licences: C$140,512. (D1; p.7)
- **A25_4** Q3FY25 services, hardware and other: C$5,482,720. (D6; p.7)
- **A25_6** Q1FY26 services, hardware and other: C$4,584,759. (D8; p.7)
- **A25_8** Q3FY26 services, hardware and other: C$3,651,223. (D1; p.7)
- **A26_5** Q4FY25 closing ARR: C$96,149,750 (ARR bridge, non-IFRS section). (D1; p.10)
- **A26_8** Q3FY26 closing ARR: C$107,194,390 (ARR bridge, non-IFRS section). (D1; p.5)
- **A27_4** Q3FY25 organic ARR net of churn: C$1,711,335 (ARR bridge, non-IFRS section). (D1; p.10)
- **A27_7** Q2FY26 organic ARR net of churn: C$1,802,495 (ARR bridge, non-IFRS section). (D1; p.10)
- **A27_8** Q3FY26 organic ARR net of churn: C$815,535 (ARR bridge, non-IFRS section). (D1; p.5)
- **A28_1** Q4FY24 acquired ARR: C$14,600,000 (ARR bridge, non-IFRS section). (D1; p.10)
- **A28_2** Q2FY25 acquired ARR: C$3,870,000 (ARR bridge, non-IFRS section). (D1; p.10)
- **A28_3** Q3FY25 acquired ARR: C$12,000,000 (ARR bridge, non-IFRS section). (D1; p.10)
- **A28_4** Q3FY26 acquired ARR: C$4,480,000 (ARR bridge, non-IFRS section). (D1; p.5)
- **A40** Cash and cash equivalents 31 Dec 2025: C$57,629,569. (D4; p.9)
- **A41** Short-term investments 31 Dec 2025: C$61,551,056. (D4; p.9)
- **A44** Cash and cash equivalents and short-term investments at 30 Sep 2026: C$129,007,023; no debt. (D1; p.5)
- **A45** Buddy acquired July 10, 2026; cash consideration on closing C$12,367,916 (after the 31 Dec 2025 year-0 balance). (D2; p.8)
- **A46** 75,000 shares issued at $7.36/share on the Buddy close. (D2; p.8)
- **A48** Payments of contingent consideration (781,053) in the nine months to 30 Sep 2026. (D2; p.6)
- **A49** Novari: "remaining potential performance-based consideration payable of up to $4,500,000 ... in the 24-month period following the acquisition. A balance of $3,800,000 is accrued". (D2; p.8)
- **A51** Buddy: "remaining potential performance-based consideration payable of up to $7,248,555, if certain revenue targets are met in the 30-month period following the acquisition"; fair value at close C$3,205,624. (D2; p.9)
- **A53** FY2025 revenue by geography: United Kingdom 60,045,988; Canada 33,145,120; Australia 10,243,026; United States 3,336,556; Western Asia 1,522,928; rest of the world 673,300 (C$). (D4; p.26)
- **A54** Q3 2026 revenue by geography: United Kingdom 14,643,256 vs 16,571,510 in Q3 2025; Finland 1,200,877 (Buddy, new) (C$). (D2; p.12)
- **A55** AIF: Dan Matlow, President and Chief Executive Officer since May 2016, director since November 28, 2016, holds 726,862 common shares; previously CEO of Medworxx Solutions, sold to Aptean in 2015. (D16; p.18)
- **A56** AIF: directors and executive officers as a group own 10,231,462 common shares (about 16% of shares outstanding). (D16; p.18)
- **A57** Equity raises in 2025: 9 Jan 2025 bought deal of 3,165,145 shares at $10.90, gross $34,500,080; 20 Aug 2025 bought deal of 5,885,828 shares at $12.70, gross $74,750,016. No share issue for cash in 2026. (D2; p.10)
- **A58** Acquisitions in 2025: Induction Healthcare Group (closed June 18, 2025) and Novari Health (closed July 4, 2025). (D4; p.20)
- **A59** Q3 2026 cash opex lines: G&A 6,327,731; S&M 3,378,727; R&D 7,490,494 (vs 9,237,648 in Q3 2025); 9M 2026 G&A 17,181,503, S&M 9,618,629 and R&D 24,994,218. (D1; p.6)
- **A62** No equity offering in 2026: nine-month 2026 financing cash flow of C$167,507 "relates primarily to proceeds from the exercise of options, net of principal payments on lease liabilities"; the prior-year period held the January and August 2025 offerings. (D1; p.9)
- **A63** Gross profit FY2024 C$55,494,433, 81% of revenue. (D5; p.6)
- **A64** As at September 30, 2026 the Company "has no debt outstanding"; Scotia C$5 operating line and C$60 revolving facility undrawn. (D1; p.10)
- **A66** Term licences, maintenance and support were 81% of revenues in Q3 2026. (D1; p.7)
- **A70** AI Scribe launch release (15 Sep 2026): serviceable base of about 22,000 practitioners in the installed base. (D19; p.1)
- **A72** FY2025 gross profit 87,588,361, 80% of revenue (FY2024 81%); Q3 2026 gross margin 79%, nine months 2026 80%. (D3; p.6)
- **A73** Q3 2026 release: VitalHub is headquartered in Toronto with over 700 employees globally. (D15; p.3)
- **A75** Organic net of churn in ARR by year: 2024 6,475,919 (15%) and acquisition growth 17,911,500 (40%); 2023 quarters 1,462,767 / 1,491,003 / 1,475,975 / 1,959,986 (sum 6,389,731); FX effect 2023 926,600 / (116,818) / 127,489 / 1,587 and 2024 652,250 / (39,000) / 1,087,357 / 392,445. (D5; p.11)
- **A76** ARR at December 31, 2024 was 71,054,210 against 44,573,739 at December 31, 2023 (+59%), with organic growth 6,475,919 and acquisitions 17,911,500. (D5; p.5)
- **A77** FY2025 organic growth 7,231,031 (10%) and acquisition growth 15,870,000 (22%) for the movement from December 31, 2024. (D3; p.5)
- **A78** Organic ARR growth September 30, 2025 to September 30, 2026: 7,228,813, printed as 8%; quarterly FX effects Q4 2025-Q3 2026 574,556 / 199,681 / 651,853 / 365,698. (D1; p.5)
- **A79** ARR excludes perpetual license and virtual care revenue. (D6; p.11)
- **A80** Term licenses, maintenance and support represented 83% of revenues for the year ended December 31, 2024. (D5; p.7)
- **A81** FY2025 depreciation and amortization 11,081,525 = depreciation of property and equipment 713,788 + depreciation of right-of-use assets 557,770 + amortization of intangible assets 9,809,967. (D4; p.10)
- **A82** FY2025 purchase of property and equipment 423,144 (FY2024 883,719). (D4; p.12)

**Guidance and management statements**

- **G1** Matlow (Q3 2026 call): "I still think there's close to about $10 million or so-ish of SHREWD revenue that's still out there to a degree in all different pockets of it that are there. But it's hard to say which ones are not at risk or at risk". (D12)
- **G2** Matlow (Q3 2026 call): "Take that back, Paul. 7%, 8% of our ARR number, not our revenue number." (D12)
- **G3** Matlow (Q3 2026 call), on whether suspended SHREWD accounts were removed from ARR: "In some of the cases, yes, in some of the cases, no." and "I think we'll know more in another quarter or so how that comes out". (D12)
- **G5** Matlow (Q3 2026 call), asked about a path to Rule of 40 in 2027: "Yes, we think so. We do believe that's the case. Margins will continue to increase, and we're seeing real pipelines". (D12)
- **G6** Matlow (Q3 2026 call): "We're comfortable that we're going to sustain, if not improve that number on a quarter-over-quarter basis at this stage." (D12)
- **G7** Matlow (Q3 2026 call): "our backlog for our services revenue has never been stronger" and "we do think there's a lot more milestones that should be hit in Q4 than in Q3." (D12)
- **G8** Matlow (Q3 2026 call): "I think we should be able to get that Novari product well over the $20 million in ARR numbers. And Strata ... we see another $3 million to $5 million in the pipeline of some stuff that could happen over the next couple of years." (D12)
- **G9** Matlow (Q3 2026 call), on Attend Anywhere declining moderately: "Theoretically, yes. ... we also see some new deals cooking on it that maybe offset some of that stuff. ... all that stuff gets renewed in the March time frame". (D12)
- **G12** Matlow (Q3 2026 call): "with any luck, we'll be able to get another one over the finish line before the end of the year ... there are 2 or 3 companies that we have earmarked since the very beginning that are now in market". (D12)
- **G13** Matlow (Q2 2026 call, 7 Aug 2026), replying to an analyst who noted no formal ARR guidance and a 10%-11% run rate: "we still feel comfortable with the rest of our business that we -- even with that headwind that we should still be in the range where we were this quarter and above it for sure ... we're still getting 10%, 11% organic growth." Not restated on the Q3 2026 call (D12). (D13)
- **G14** Matlow (Q2 2026 call): "every $1 million of ARR theoretically if we don't add more costs, that's a point of adjusted EBITDA, right? And we're still not completed on the other side of some reductions." (D13)
- **G15** Goffenberg (Q2 2026 call), on gross margin: "I think we're still, I think, continue to be probably to be the 80% line." (D13)
- **G17** Goffenberg (Q3 2026 call): "The increase was primarily due to lower research and development expenses, synergies from the integration of Induction and Novari and a favorable foreign exchange impact in the quarter." (D12)
- **G18** Matlow (Q3 2026 call): "They have a break clause in their contract for February of 2027 that they can exercise on the Palantir product." (D12)
- **G20** Matlow (Q3 2026 call), on no NCIB purchases through September: "I think it's more of the latter" (preserving flexibility for larger M&A). (D12)
- **G21** Matlow (Q3 2026 call): "we believe just by adding AI products into our installed base, there's probably about $30 million, $40 million of TAM just on top of that." (D12)
- **G23** Q3 2026 MD&A: Adjusted EBITDA = EBITDA + share-based and deferred share-based compensation + business acquisition, restructuring and integration costs + change in fair value of contingent consideration; foreign currency gains and losses stay inside Adjusted EBITDA. "The increase in Adjusted EBITDA was primarily attributable to lower research and development expenses and a favourable foreign exchange impact". (D1)
- **G24** Q3 2026 MD&A: ARR "is defined as annual renewable software licence fees and maintenance services"; acquisition revenue is "the annual contract value of recurring revenues of the acquired companies at the time of acquisition"; organic growth is "the revenue over and above the acquisition revenues". (D1)
- **G25** Goffenberg (Q3 2026 call): "Services revenue is seasonally lighter over the summer against elevated projected activity in the prior year period." (D12)
- **G26** The Register (17 Nov 2026): "Health minister James Frith told MPs on Monday that the current contract would continue until March 2029 as the government procures a new version of the Federated Data Platform (FDP)." The February 2027 break clause is therefore not exercised. (D23)
- **G27** The Register (17 Nov 2026): "The formal process is set to start during the second half of next year and take around 18 months"; the new iteration would "welcome international and UK capability alike - whether that is UK small and medium-sized enterprises that want a crack at NHS contracts, sovereign AI-backed capability in the UK or any international provider worth merit." (D23)
- **G28** The Register (17 Nov 2026), Frith: "We will also start work, alongside the new procurement, with different providers on developing new capabilities and expertise starting with systems used in maternity care." Frith also said migration was "possible in principle" under the contracts' exit and transition provisions. (D23)

**Estimates**

- **E1** FactSet consensus revenue FY26E: 129 (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page. (D17)
- **E1_1** FactSet consensus revenue FY27E: 139 (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page. (D17)
- **E1_2** FactSet consensus revenue FY28E: 147 (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page. (D17)
- **E1_3** FactSet consensus revenue FY29E: 166 (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page. (D17)
- **E2** FactSet consensus EBITDA FY26E: 34 (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown. (D17)
- **E2_1** FactSet consensus EBITDA FY27E: 39 (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown. (D17)
- **E2_2** FactSet consensus EBITDA FY28E: 45 (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown. (D17)
- **E2_3** FactSet consensus EBITDA FY29E: 52 (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown. (D17)

**Assumptions**

- **S1** Term revenue = 0.985 x average closing ARR. Basis: Q2 2026 term 24.542 x 4 / average ARR (99.079, 101.533) = 0.979; Q3 2026 25.784 x 4 / average (101.533, 107.194) = 0.988; average 0.984 rounded to 0.985. Band 0.975-0.995.
- **S2** Q4 2026 organic net ARR add of 1.5 (base). Q4 is a stronger selling quarter than Q3 (Q4 2024 +2.61, Q4 2025 +1.88) but SHREWD suspensions continue (G1, G3); the FDP extension (G26) puts the SHREWD roll-off in 2027 rather than Q4 2026. Bull 2.5, bear 0.5.
- **S3** FY2027 organic ARR adds 8.94 before the SHREWD roll-off (base): the 8.123 of organic adds in the four quarters to Q2 2026 (the last four before the Q3 SHREWD drag, A27_4-A27_7) grown 10%, the trend in dollar adds (S29). As a share of opening ARR this is 8.2%; net of the 4.0 roll-off FY2027 closing ARR grows 4.5%. v2 used 9% of opening ARR (9.8 of adds), above any year Vitalhub has printed. Band 7.23 (bear, flat at FY2025) to 9.34 (bull, +15%).
- **S4** FY2028 organic ARR adds 9.83 (base), the dollar trend continued at +10% (S29); 8.7% of opening ARR. The Novari and Strata pipelines and AI add-ons (G8, G21) and the Rule of 40 aim (G5) support continued growth in dollar adds; the withdrawn 10%-11% comfort (G13) argues against a step-up beyond the trend, so the trend rate is used unchanged. No further SHREWD loss (S26). Band 7.23 (bear) to 10.74 (bull).
- **S5** FY2029 organic ARR adds 10.81 (base), +10% again; 8.8% of opening ARR. Band 7.23 (bear) to 12.35 (bull).
- **S6** FY2030 (gsnext year) organic ARR adds 11.89 base (bull 14.21, bear 7.23), one more year of the same dollar-add build; no management phrase reaches 2030.
- **S7** Virtual care (Attend Anywhere) declines 5% a year from FY2027: management expects a moderate decline offset by some new deals, renewals in March (G9); Q3 2026 was -6% YoY. Band 0% (bull) to -15% (bear).
- **S8** Perpetual licences 0.5 in Q4 2026 (Q4 2025 0.512) and 2.0 a year thereafter, about the FY2025-FY2026 average; term licences are the preferred model (D1).
- **S9** Services, hardware and other: Q4 2026 4.6 (back to the Q1 2026 level of 4.585; management expects more Q4 milestones, G7) and 16.5% of term revenue thereafter (9M 2026 ratio 16.6%; FY2025 19.0%). Band 15%-19%.
- **S10** Cash gross margin 80% (9M 2026 80%; CFO "80% line", G15). Cost of sales holds no D&A or SBC (D1). Band 78%-82%.
- **S11** Core cash opex = Q3 2026 G&A 6.328 + S&M 3.379 + R&D 7.490 = 17.197 a quarter (ex SBC, D&A, FX, one-time), annualized 68.79; includes Buddy for 82 of 92 days.
- **S12** Core opex inflation 2.0% a year: the Bank of Canada inflation-control target midpoint (no company rate stated). Band 1%-3%.
- **S13** Variable cash opex 30% of revenue above Q3 2026 annualized revenue (127.65). The incremental rate cannot be measured from FY2025-26 because integration synergies cut opex while revenue grew; management says $1 of ARR is "a point of adjusted EBITDA" if no costs are added (G14) and R&D holds level with AI spend (G11). Band 20% (bull) to 40% (bear).
- **S14** Buddy cost saving 0.5 a year from FY2027 (Buddy was about breakeven, G16; margin through "a little bit of cost reduction and revenue generation" in 6-12 months, G10). Band 0 (bear) to 1.0 (bull).
- **S15** Foreign exchange gains and losses, which sit inside Adjusted EBITDA (G23), are forecast at zero; FX on ARR is held at zero.
- **S16** Contribution margin mc = 1 - 20% cash cost of sales - 30% variable opex = 0.50 (bull 0.60, bear 0.40).
- **S17** Buddy component inside the term line is held at the acquired ARR of 4.48 x 0.985 a year (stub 174/365 in FY2026); Vitalhub counts post-close growth as organic (G24), so Buddy growth sits in the organic ARR rate. Not scaled to Consensus.
- **S18** Scenario levers: (1) SHREWD roll-off size and organic ARR adds in dollars, (2) the cost build (variable opex rate, Buddy saving), (3) Attend Anywhere. Bull and bear differ from base by the bottom-up difference of those levers, added to the base lines and EBITDA.
- **S19** Dan Matlow CEO bot view: treat the 10-11% organic comfort as withdrawn until the NHS FDP decision; low-to-high single-digit organic ARR growth in Q4 2026 and early 2027. simulated CEO view (Dan Matlow CEO bot), 17 Nov 2026; not company disclosure; link unverified. Used only as a cross-check of S2-S3, which rest on the filings and the Q3 call. (D22)
- **S20** Earn-out probabilities = accrued fair value / maximum: Novari 3.8 / 4.5 = 0.844; Buddy 3.205624 / 7.248555 = 0.442 (D2).
- **S21** Earn-out dates are the end of each earn-out window: Novari 24 months after 4 Jul 2025 close (2027-07-04); Buddy 30 months after 10 Jul 2026 close (2029-01-10). The filings give windows, not payment dates.
- **S22** Bear: all SHREWD ARR (8.0, the midpoint of 7.5-8.6, G2) rolls off straight-line during 2027 as trusts migrate onto FDP (G26); organic adds stay flat at the FY2025 printed 7.23 a year (A75), so organic growth falls to about 6.5% of opening ARR. Bull: only 1.5 rolls off (suspended accounts still in ARR, G3) and organic adds grow 15% a year (the 2024-to-TTM-Q1 2026 pace, S29) as the Strata pipeline and AI add-ons convert. A place in the new FDP procurement is not in bull revenue (S28).
- **S24** Q4 2026 virtual care held at the Q3 2026 level (2.338); renewals fall in March (G9).
- **S25** Payments of contingent consideration C$781,053 in the nine months to 30 Sep 2026; exact date not given, dated at the quarter end. (D2; p.6)
- **S26** Base SHREWD roll-off: 4.0 of ARR, about half of the 7.5-8.6 SHREWD ARR (G2, C31), straight-line during calendar 2027, none in 2028-29. Why half: the FDP extension to March 2029 (G26) means the platform displacing SHREWD stays and trusts keep migrating onto it, and some suspended accounts are still in ARR (G3), so a 2027 loss is more likely than not; but SHREWD sits "in all different pockets" and management cannot say which are at risk (G1), a new FDP iteration is procured from H2 2027 that invites UK SMEs and new capability providers (G27, G28), and trusts mid-procurement have reason to keep tools that work. The evidence does not identify losses beyond 2027. Band 1.5 (bull) to 8.0 (bear, all of it).
- **S27** Lost SHREWD revenue (average ARR lost x 0.985 term ratio x 1.165 for the services that ride on term revenue) saves only the 20% cash cost of sales; opex is not cut (G14: "every $1 million of ARR theoretically if we don't add more costs, that's a point of adjusted EBITDA"). Variable opex is charged on revenue before the SHREWD loss.
- **S28** FDP re-procurement upside is excluded from every case: the formal process starts in H2 2027 and takes about 18 months (G27), so an award lands around early 2029 at the earliest and its revenue mostly after FY2029; Vitalhub has not announced a consortium or bid.
- **S29** Organic adds are forecast in dollars. Printed organic net of churn was 6.39 in 2023, 6.48 in 2024 and 7.23 in 2025 (A75) while acquisitions took opening ARR from 36.2 to 71.1 (A76); organic growth fell from 17.7% to 14.5% to 10.2% (and 7.7% TTM Q3 2026) because the acquired ARR (17.9 in 2024, 15.9 in 2025, 4.48 in 2026) added little net organic growth after close in aggregate, not because dollar adds shrank (C38). Dollar adds grew about 10% a year from 2023 (6.39) to the four quarters to Q2 2026 (8.12), about 2.5 years apart. Base keeps that 10% trend; management commentary is mixed (pipelines and Rule of 40 vs the withdrawn 10%-11%), so no acceleration or deceleration is applied.
- **S30** Finagle defaults filled on the v05 case that ran (result defaults_filled, unchanged from v04): baseline.noa, baseline.nol, debt.start_year, distribution.mode, forecast.dwc.mode, rates.gt, rates.re, rates.roict, year. Values: noa 0, nol 0, debt policy start year 1, distribution none, working-capital change zero, terminal growth 3.81% (= the 10-year yield), cost of equity 9.31% (0.055 + the 10-year yield), terminal ROIC 15%, ten-year horizon. Each scenario also lists the build_baseline defaults rates.t, rates.rd, debt.mode and debt.leverage, which the prompt inputs P11 and P14 replaced. Capex and SBC paths were not set: forecast_capex method 1 and forecast_sbc ran from year-0 capex 0.423144 and SBC 2.647812 (Yahoo). (D25)

**Calculations**

- **C1** Term licences, maintenance and support Q4 2026E = bottom-up Q4 (26.581) scaled by the Q4 organic factor 0.9825 to the Consensus remainder; Buddy component not scaled. (inputs E1, S1, S2, S8, S9, S17, S24)
- **C2** Term licences, maintenance and support FY26E = bottom-up 100.834 x organic scale factor 0.9825 to event-adjusted Consensus revenue (Buddy component unscaled). (inputs E1, S1, S3, S7, S8, S9, S17, S26, C36)
- **C4** Days from 10 Jul 2026 close to 31 Dec 2026 (174) / 365. (inputs A45)
- **C5** Q4 2026E revenue = FY2026 Consensus 129 (E1) - 9M 2026 reported 95.557 (A1). (inputs E1, A1)
- **C6** FY2025A / FY2024A - 1 (+58.9%, acquisitions plus organic). (inputs A1, A1_1)
- **C7** Adjusted EBITDA / revenue, FY24A. (inputs A1, A2, E1, E2)
- **C9** Bottom-up revenue FY26E: sum of unscaled lines (term from the ARR path, virtual care, perpetual, services). (inputs S1, S2, S3, S4, S5, S7, S8, S9, S17)
- **C10** Bottom-up Adjusted EBITDA FY26E: unscaled revenue - 20% cash cost of sales - core opex (Q3 2026 annualized, +2%/yr) + Buddy saving - 30% variable opex on revenue above 127.65. (inputs S10, S11, S12, S13, S14, S15)
- **C11** Bottom-up / base (event-adjusted Consensus) revenue FY26E. (inputs C9, E1)
- **C13** Bottom-up / base (event-adjusted Consensus) Adjusted EBITDA FY26E. (inputs C10, E2)
- **C14** Base revenue for the bridge (Q4E). (inputs E1, A1)
- **C15** Consensus-implied cash cost / cost-build cash cost on the same revenue - 1; inside the 10% rule. (inputs E1, E2, S10, S11, S13)
- **C16** Year-0 cash = FY2025 cash 57.630 + short-term investments 61.551 + 2026 equity raises 0 = 119.181 (P3). (inputs A40, A41, A62, P3)
- **C17** Year-0 shares = FY2025 63.232054 + 2026 equity raises 0 (P3). The 75,000 Buddy consideration shares are on cash_share_adjustments. (inputs A42, A62, P3)
- **C18** No year-0 equity raise: opening cash 119.181 less the dated Buddy and earn-out items (about 26 undiscounted in the base) stays positive in every case, and EBITDA is positive in every year of every case (P3). (inputs C16, P3)
- **C21** No future acquisition is forecast. Management hopes to close another deal before year-end (G12) but none is announced; announced-but-unclosed deals are excluded. (inputs G12)
- **C22** Revenue growth FY2026E-FY2029E on totals; compounds to the base revenue. (inputs E1, A1)
- **C23** Adjusted EBITDA growth FY2026E-FY2029E on totals; compounds to the base EBITDA. (inputs E2, A2)
- **C24** me = FY2029E Adjusted EBITDA 48.328 / revenue 161.410 = 29.9% (event-adjusted Consensus). (inputs C36)
- **C25** bull Term licences, maintenance and support Q4 2026E = base + (bull bottom-up - base bottom-up). (inputs C1, S18, S22)
- **C27** bull revenue growth on totals. (inputs C26)
- **C28** base closing ARR FY26E from organic adds (S2-S5, S22); FX zero. (inputs A26, S2, S3, S4, S5, S22)
- **C29** Q3 2026 Adjusted EBITDA excluding the FX gain: (8.620 - 0.592) / 31.914 = 25.2%; Q2 2026 excluding the FX loss: (8.163 + 0.223) / 31.738 = 26.4%. (inputs A21_8, C8, A59)
- **C31** SHREWD ARR = 7-8% (G2) x closing ARR 107.194 = 7.5 to 8.6. (inputs G2, A26)
- **C32** Cash opex per quarter (G&A + S&M + R&D): Q4 2025 17.157; Q1 2026 17.817; Q2 2026 16.781 (9M less Q1 and Q3); Q3 2026 17.197. (inputs A59, A67, A68)
- **C33** Unscaled bottom-up scenario totals (Appendix A sensitivity) from model.py v3: bull revenue 129.70/141.73/152.40/165.65, EBITDA 34.44/41.24/46.06/52.58; bear revenue 129.45/133.09/135.61/142.89, EBITDA 33.90/32.30/30.07/31.55. (inputs S18, S22, S26, S29)
- **C34** Consensus revenue growth path: FY2027 +7.8%, FY2028 +5.8%, FY2029 +12.9%; the FY2028 dip and FY2029 jump reflect thinner, rounded later-year coverage (E-series). (inputs E1)
- **C35** Revenue shares FY2025 by line: term 78.4%, virtual care 4.8%, perpetual 1.9%, services 14.9%. (inputs A3_1, A4_1, A5_1, A6_1, A1_1)
- **C36** Event-adjusted Consensus revenue FY27E = FactSet 139 (E1) -2.295 for the 16 Nov 2026 FDP extension (P7): the effect of the 4.0 SHREWD roll-off alone on the v3 bottom-up build (with vs without the loss). The 17 Nov pull is taken to predate the announcement. v3 isolates the event: the organic-driver change (S29) uses information analysts already had and does not move the base. (inputs E1, P7, S26, S27, D23)
- **C38** ARR bridge trend from the printed series (A75-A78, A27 series): organic adds 6.39 (2023), 6.48 (2024), 7.23 (2025), 8.12 (four quarters to Q2 2026), 7.23 (TTM Q3 2026); organic growth on opening ARR 17.7%, 14.5%, 10.2%, 10.2%, 7.7%. Opening ARR (rebuilt back from 107.194 through the bridge): 36.15 (2023), 44.57 (2024), 71.05 (2025), 96.15 (2026). Organic adds per dollar of opening ARR including acquired ARR fell by more than half while dollar adds rose about 13% from 2023 to 2025. Seasonality, 2022-2025 average adds: Q1 1.57, Q2 1.35, Q3 1.28, Q4 1.84. FX added 2.09 (2024), 1.99 (2025) and 1.22 (9M 2026), positive in 9 of the last 10 quarters. (inputs A75, A76, A77, A78, A27_8)
- **C39** TLMS revenue x 4 / average ARR by quarter: 1.01-1.06 in 2023, 1.05-1.08 in Q1-Q3 2024, 1.14 in Q4 2024 (14.6 acquired in the quarter, so the average understates the ARR earning revenue), 1.01-1.09 in 2025 (acquisition quarters Q2 and Q3 high), then 0.994 / 0.980 / 0.979 / 0.988 in Q4 2025-Q3 2026 (average 0.985). ARR excludes virtual care (A79), so the step down is not Attend Anywhere leaving the TLMS line; the cause is not disclosed. The 0.985 conversion matches the four clean quarters since Q4 2025. (inputs A22_8, A26_8, A79, S1)
- **C40** Change from v2 (17 Nov 2026) to v3 (18 Nov 2026): organic adds in dollars (S29) and the event adjustment limited to the SHREWD effect (C36). See revision_log.md for figures. (inputs S29, C36)
- **C41** Finagle v05 result (D25): value per share (free cash flow to equity; DDM identical) base 9.226, bull 11.216, bear 6.827 vs price 6.73 (Yahoo, 2026-11-18); cost of equity 9.31% and terminal growth 3.81%, both derived by Finagle from the 3.81% risk-free rate (P10); tax 26.5%, cost of debt 2.8%, debt 0 held; year-0 EBITDA 26.554 before SBC (P15); opening cash 106.813 and shares 63.307054; cash after schedule 99.789 (present value -7.023); ten-year horizon FY2026E-FY2035E; no sanity flags; validation warning base "average EBITDA growth is 16.4% and there are no acquisitions. If that growth includes acquired EBITDA, use an organic path and book the purchase price with acquisitions, or MnA stays zero." (bull 21.4%, bear none); result flags: "rates.rd provenance: Forecaster proposal without an explicit David quote (applied as given; see rd_provenance)" and "year-0 capex remains Yahoo 0.423144 vs method-1 ratio on new D&A (1.271558 / revenue)". (inputs D25, P10, P11, P12, P13, P14, P15, S30)
- **C42** Value bridge (derived): FCFE each year = Finagle EBITDA - capex - SBC - cash tax - interest, which equals the yearly change in the result cash path; discounted at the 9.31% cost of equity. Base 99.79 cash + 71.18 PV FY2026E-FY2029E + 104.34 PV FY2030E-FY2035E + 308.76 terminal (residual) = 584.08 = 9.226 x 63.307; bull 99.79 + 78.52 + 131.50 + 400.23 = 710.04; bear 99.79 + 61.29 + 71.20 + 199.89 = 432.18. Terminal share of value 52.9% base, 56.4% bull, 46.3% bear. Value vs 6.73: base +37%, bull +67%, bear +1.4%. (inputs C41)
- **C43** Finagle capex path (v05 result paths, method 1 on year-0 D&A 1.271558): base capex 0.42 (FY2025A), 3.00, 3.99, 4.73, 7.17 (FY2029E), 16.28 (FY2035E) against D&A 2.71 in FY2035E (about 6.0x, derived; bull 6.9x, bear 4.9x); FY2035E capex / EBITDA 19.4% base, 19.0% bull, 20.1% bear vs FY2025 actual 0.423 / 26.554 = 1.6% (derived). Mechanism: terminal capex = D&A x (1 - C) + C x (EBITDA - SBC) with C = 3.81% / 15% x (1 - 26.5%) = 0.187, so about 14.1 of the 16.3 base terminal capex is growth reinvestment at the 15% terminal ROIC (derived). (inputs D25, A81, A82, S30)
- **C44** Finagle v05 EBITDA path: year-0 EBITDA is the stated 26.554 (P15), so the forecast growth compounds to the forecast dollars: base 34.000 / 37.164 / 41.328 / 48.328 for FY2026E-FY2029E, equal to the forecast (C23), and the starting margin passed past FY2029E is 29.9%. Year-0 SBC is still Yahoo's 2.648, so the SBC/EBITDA ratio Finagle holds moves from 0.1022 (v04) to 0.0997; SBC dollars in FY2026E-FY2029E are unchanged and slightly lower from FY2030E. (inputs D25, P15, A2_1, C23)

**Prompt and brief**

- **P2** David May standing preferences (brief, 17 Nov 2026): base case accelerates or decelerates current trends on management commentary, no conservative haircut; a later-year margin well beyond history is flagged and banded in the bear, not capped.
- **P3** David May standing preference: year-0 cash = FY2025 cash plus short-term investments adjusted for 2026 equity raises; shares raised likewise; add a year-0 raise rounded up to the next C$50 only if a case goes cash-negative.
- **P6** Brief and David May (t214u, 17 Nov 2026): Dan Matlow CEO bot may be used; his own views are tagged [S] "simulated CEO view (Dan Matlow CEO bot), 17 Nov 2026" and never shown as company disclosure.
- **P7** David May, 17 Nov 2026 (revision, pt220u): "I think Palantirs contract was renewed. Probably have to assume that some of the shrewd contracts roll off in 2027." Base assumes a partial SHREWD roll-off in 2027; the base stays Consensus-anchored but is adjusted for this post-pull event (C36).
- **P8** David May, 18 Nov 2026 (pt221u): "ask the Dan Matlow bot for his product sheet on licenses. Update the forecast if it provides any insight into trends". v3 forecasts organic ARR adds in dollars from the sheet's ARR bridge (S29).
- **P9** David May, 18 Nov 2026 (pt223u): "do a finagle valuation." The Finagle bot runs the valuation; the Forecaster wrote the collaborative request (v01) and writes the report section from the result only. v01-v03 stopped; v04 was superseded by v05 (D25), which is the valuation.
- **P10** David May, 2026-11-18, risk-free rate for the Finagle run: "3.81% use this" (Bank of Canada 10-year benchmark, 3.81% on 16 Nov 2026, D27, because Yahoo CA10Y=RR has no quote).
- **P11** David May, 2026-11-18: "Rerun VHI as v03 with capex at the FY25 ratio of revenue, no debt (leases excluded), 26.5% tax, and no cash from the Buddy consideration shares." Applied in v04 as year-0 debt 0, debt policy hold, tax rate 26.5%.
- **P12** David May, 2026-11-18: "cash should be from the 2025 filling adjusted for the cash price of Buddy (+$12.37). shares should be from the 2025 filling (63.23M) adjusted for Buddy (+0.075M). Isn't that logical?" Applied as opening cash 106.812709 = 119.180625 - 12.367916 (the Buddy closing cash is an outflow) and shares 63,307,054 = 63,232,054 + 75,000; the Buddy closing cash and consideration shares were removed from the schedule so they are not counted twice.
- **P13** David May, 2026-11-18: "remove the "amortization of intangible assets" when calculating capex using method 1." Applied as year-0 D&A 1.271558 = depreciation of property and equipment 0.713788 + right-of-use assets 0.557770 (A81); capex stays on Finagle method 1.
- **P14** Cost of debt 2.8% for the Finagle run: proposed by the Forecaster on 2026-11-18 (Finagle's own earlier default was 0.027976); David did not object. Not a direct David quote. Immaterial: debt is held at zero and forecast-year interest is zero.
- **P15** David May, 2026-11-18 (t237u): "Yes, do the quick fix". Applied in v05 as year-0 EBITDA 26.554099 (Vitalhub reported FY2025 Adjusted EBITDA, A2_1) and EBITDA definition before stock-based compensation, replacing Yahoo's 25.898.

**Not verified**

- D12 and D13 (Seeking Alpha transcripts): text read from the ceochat mirror; Seeking Alpha links not opened (link unverified).
- D22 and S19 (Dan Matlow CEO bot): simulated CEO view, not company disclosure; link unverified.
- E-series: whole-number consensus with no analyst count on the page.

---

## Appendix C – Method

This forecast follows the repository's forecaster skill at commit 3a46f0a. The repository was fetched again for versions 2 and 3 and had not moved. With no company guidance, the base totals start from FactSet consensus, pulled from Markets Insider on 17 November 2026 after the Q3 release [D17]. StockAnalysis (S&P Global) shows FY2026 revenue of 128.81 from nine analysts and FY2027 of 139.28, which supports the unadjusted path [D18]. The Markets Insider page rounds to whole numbers and shows no analyst count.

**Event adjustment (versions 2 and 3).** The FactSet pull is treated as predating the 16 November FDP announcement [D23]. The skill gives no specific rule for news after the Consensus pull. It does allow a prompt instruction to override the default method, tagged [P], and David May's request is that instruction [P7]. FY2027E–FY2029E totals are FactSet plus the effect of the 4.0 SHREWD roll-off alone, measured as the v3 bottom-up build with the loss minus the same build without it. Lost revenue saves only cost of sales. The adjustment is recorded in each total, with the raw FactSet figure kept beside it in the forecast file [C36]. Version 2 measured the adjustment as the v1-to-v2 change in the whole build, which also carried our organic-rate change. Version 3 confines it to the post-pull event. When FactSet updates after the announcement, this adjustment should be dropped and the new pull used.

The bottom-up build (`model.py`) works from closing ARR, the four reported revenue types, an 80% cash gross margin and core cash opex at the Q3 2026 run rate. It is scaled to the base line by line, with acquired Buddy ARR left unscaled. The history window is the nine quarters from Q3 2024 to Q3 2026, each read from that quarter's MD&A (Figure 19). For the ARR bridge trend, version 3 also uses 2023 and 2024 quarters from the FY2024 MD&A [A75]. It uses the CEO bot's term-licence product sheet as an index to the filings [D24]: every bridge figure used here was checked in the filing the sheet names. The FY2023 MD&A could not be downloaded (the OTC Markets mirror was temporarily unavailable), so 2023 quarters come from the comparative columns of the FY2024 MD&A. Every filing figure was checked against the original SEDAR PDF and cited to its page. Call quotes are from the Seeking Alpha transcripts as mirrored in the ceochat repository; the Seeking Alpha links themselves were not opened. The FDP facts are from The Register's report of the minister's statement to MPs. Hansard was not checked.

The forecast file also holds the year-0 cash and share schedule, unchanged in this version. Year-0 cash is FY2025 cash plus short-term investments, with no 2026 equity raise. Year-0 shares are the FY2025 count. Dated items cover the Buddy close and the Novari and Buddy earn-outs. No case goes cash-negative, so no raise is added [C16][C17][C18].

The Dan Matlow CEO bot is a simulation built from public material. Its views are tagged S and never carry a number on their own [S19][P6]. Questions that would sharpen the next update, for relay to the CEO bot or to management:

1. How much of the SHREWD ARR has already been taken out of the 107.2, and how much is suspended but still counted?
2. Which SHREWD modules overlap FDP functions, and which do not?
3. Will Vitalhub bid in the new FDP procurement or the maternity work, alone or in a consortium?
4. What is net revenue retention, excluding SHREWD?
5. What are headcount and R&D headcount after Buddy, against the "over 700" in the release [A73]?
6. What is the currency mix of ARR?
7. How much organic ARR growth have the acquired books (Induction, Novari, Buddy) added since close, against the legacy book?
8. Why did term revenue fall from about 1.05× to 0.985× of average ARR after 2024?

**Valuation run history.** Runs v01–v04 of the Finagle bot are not the valuation in this report.

- **v01** stopped: Finagle's Yahoo symbol for the Canadian 10-year yield returned no quote, which left the cost of equity and terminal growth empty.
- **v02** completed, but the bot ruled it not a valuation. Its default capex was anchored on year-0 D&A that was 89% amortization of acquired intangibles [A81].
- **v03** stopped because two of David's inputs could not be expressed:
  - capex as a ratio of revenue, which was not a year-by-year list;
  - Buddy consideration shares with no cash proceeds.

- **v04** ran with David's risk-free rate, debt, tax, D&A and opening cash and share inputs [P10]–[P14], and is superseded. Finagle uses its own year-0 EBITDA unless one is stated, so v04 compounded our growth from Yahoo's 25.9 rather than the reported 26.6.

v05 adds the reported year-0 EBITDA [P15] and is the valuation in Section 7 [D25].

**Method suggestions** (not made as repository edits):

1. Add a non-cash consideration-share item type to the cash and share schedule, so that shares issued for an acquisition add to the count without adding proceeds to cash.
2. Give Finagle a working Canadian risk-free source, such as the Bank of Canada 10-year series, since the Yahoo symbol returns no quote.
3. Set a lease-versus-debt default, so that Yahoo's total debt, which includes leases, does not create a leverage target for a company with no borrowings.
4. Set a cost-of-debt default when year-0 debt is zero, so that validation does not stop on a missing cost of debt.
5. State plainly in the forecaster skill that the Finagle bot runs collaborative valuations and the Forecaster writes the request and the report section only.
6. Have the collaborative handoff send year-0 EBITDA and revenue as Forecaster leaves, so the forecast's level always supersedes Finagle's sources. Finagle has no SEDAR+ source: for Canadian tickers it reads the prompt, the article, the attachments and then yfinance.

<div class="fig" markdown="1">

**Figure 19 – Quarterly history, Q3 2024–Q3 2026 (C$ millions)**

| | Q3'24 | Q4'24 | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | Q3'26 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Revenue | 16.5 | 20.6 | 21.7 | 23.9 | 32.0 | 31.4 | 31.9 | 31.7 | 31.9 |
| Adjusted EBITDA | 4.55 | 5.05 | 5.61 | 6.30 | 7.21 | 7.43 | 7.99 | 8.16 | 8.62 |
| Margin | 27.6% | 24.5% | 25.9% | 26.4% | 22.5% | 23.7% | 25.0% | 25.7% | 27.0% |
| Closing ARR | 53.5 | 71.1 | 73.7 | 79.6 | 93.7 | 96.1 | 99.1 | 102 | 107 |
| Organic ARR add | 1.08 | 2.61 | 1.78 | 1.86 | 1.71 | 1.88 | 2.73 | 1.80 | 0.816 |
| Acquired ARR | — | 14.6 | — | 3.87 | 12.0 | — | — | — | 4.48 |

*Source: quarterly MD&As D1, D3, D5–D11; [A20]–[A28_4] series in `forecast.json`. May not sum due to rounding.*

</div>
