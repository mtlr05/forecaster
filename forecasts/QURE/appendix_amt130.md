## Appendix D – AMT-130 US patient demand model

*This appendix sets out the US treatable-pool model behind the AMT-130 patient volumes in Section 7. Tags follow Appendix B: D document, G company statement, E external estimate, S assumption, C calculation. Statements marked "judgment" are the analyst's view, not sourced facts.*

### D.1 Summary

The model uses a leave rate of m = 0.62 a year for the US treatable pool: progression out of eligibility of 0.60 a year plus deaths of 0.02 a year, for an average stay in the treatable window of about 1.6 years [S601]. This is the analyst's choice because it is the most internally consistent option: it reconciles disease incidence with uniQure's own launch figure without any extra assumption.

The arithmetic is simple. Huntington's disease incidence of 1.22 per 100,000 a year across a US population of 340 million, times a 90% early-manifest share, gives about 3,750 to 3,770 new patients entering the treatable window each year [S602][C601]. A pool that gains that many a year and loses 0.62 of itself a year, plus population growth g of 0.5%, settles at 3,750 / (0.62 + 0.005), or about 5,970 [C601]. That matches uniQure's "~6,000 Initial Treatable Patients at Launch" [G601] with no filter needed.

This stay is shorter than the published duration evidence (D.6), which points to roughly 2.3 to 3 years. So m = 0.62 is a consistency choice, not a finding from the clinical data (judgment).

On this basis, with the ClearPoint (CLPT) capacity ramp, treated patients rise to the 3,000-a-year cap in FY2029. They hold there through FY2030, then ease to about 2,840 a year as demand from the pool becomes the limit [C602].

### D.2 What the 6,000 is

uniQure's September 2025 pivotal deck (slide 25) shows nested circles titled "Large anticipated total addressable US market at time of launch". They run from about 100,000 genetically identifiable people, to about 40,000 symptomatic, to about 20,000 diagnosed, to "~6,000\* Initial Treatable Patients at Launch", with the footnote "\*Management Estimate" [G601]. The September 24, 2025 prospectus says the same in words: "We estimate there will be 6,000 initial treatable patients addressable by AMT-130 in the U.S. at commercial launch, assuming approval" [G602]. A GEN report of the call paraphrases management as calling it about 30% of the roughly 20,000 diagnosed and symptomatic patients [D601].

No filing or call transcript reviewed says uniQure aims to *treat* 6,000 at launch [D607]. The wording "addressable" and "at time of launch" describes a stock of patients who would qualify on day one, so the model treats the 6,000 as a starting pool, not a treatment target. The criteria that produce the roughly 30% (functional score, age, CAG repeat length, brain volume) have not been disclosed [D607].

### D.3 Method

The model is a quarterly stock-and-flow pool [D605]. Each quarter the pool of treatable patients starts at some level, gains new entrants, loses leavers who progress past eligibility or die, and loses those who are treated: pool at end = pool at start + entrants − leavers − treated, with leavers = m × pool.

**Derivation of the demand formula.** Take any year. Let S be the pool at the start of the year, E the entrants during the year, m the leave rate, T the number treated, P = T/E the share of that year's entrants treated, u = T/S the treatment rate on the pool, and g the pool's actual growth rate over the year, so that the pool changes by gS. The pool accounting is an identity:

E − mS − T = gS.

Writing T = uS and rearranging gives E = (m + g + u)S. Since T = PE, it follows that uS = P(m + g + u)S, so u = P(m + g + u), and solving for u:

u = P(m + g) / (1 − P) [C603].

Nothing in this step assumes a steady state. The relationship holds exactly in every year for whatever P and g that year produces, and a different P implies a different g. Because the model runs quarterly, leavers each quarter are (m/4) × S_q, where S_q is the pool at the start of the quarter, and treated is T_q. The annual figures in Figure D1b are built from the sums of the quarterly flows and the pool at the start of the year; the annual leave rate is then the effective rate m_eff = (sum of quarterly leavers) / S, which is below 0.62 whenever the pool falls during the year [C610].

**How the model uses it.** The model sets a demand rate u_d = P\*(m + g\*)/(1 − P\*), with P\* = 0.729 and g\* = 0.5% a year (population growth), so u_d = 0.729 × 0.625 / 0.271 = 1.68 a year [C603]. Each quarter, demand is the ceiling (u_d/4) × S_q, and treated = min(capacity, (u_d/4) × S_q). In capacity-limited years the realised P is therefore set by capacity and the realised g is whatever the accounting produces, which is negative while the launch pool drains. In demand-limited years the realised P tends to 0.729 and pool growth tends to g\*. A rate u above 1 a year is not a contradiction: the pool is drained by leavers and treatment at the same time as it is refilled by entrants, and the quarterly steps mean no quarter treats more patients than are in the pool.

P is 0.729: the share of eligible patients who are referred to a treatment centre (90%), agree to treatment (90%) and have it paid for (90%), so 0.9 × 0.9 × 0.9 = 0.729 [S603]. About three in four eligible patients make it through to surgery. The 90% levels are model assumptions, not company figures.

### D.4 Capacity

Capacity follows the CLPT AMT-130 ramp [S604]. Launch is assumed on 1 July 2027. Capacity is 330 patients in the FY2027 half year, 2,500 in FY2028, and a cap of 3,000 a year from FY2029.

The ramp is built from about 10 centres doing 1.5 cases a week for 22 weeks, then about 20 centres doing 2.5 a week for 50 weeks. These figures are judgment, drawn from the ClearPoint CEO's capacity comments on the Q2 2026 call [D606]. On the same arithmetic 4,500 a year is a ceiling, not a cap. uniQure itself says only that capacity depends on neurosurgeons and operating suites per hospital, and that more detail will come [G603].

A bull ramp of 880 / 4,500 / 3,500 run with the same method [C604] reaches about 4,500 treated in FY2028, which draws the pool down to about 2,100. Treated then falls to about 3,070 in FY2029 and settles near 2,800 a year. Faster early capacity therefore produces a hump at this short stay, because demand rather than capacity sets the long-run level.

### D.5 Results at m = 0.62

![Treated patients, capacity and year-end pool at m = 0.62](file:///workspace/out/AMT130_demand/amt130_demand_chart_m062.png)

**Figure D1 – Treated patients and pool, base case**

| Fiscal year | Capacity | Treated | Pool at year end | Cumulative treated |
|---|---:|---:|---:|---:|
| FY2027 (half year) | 330 | 330 | 5,718 | 330 |
| FY2028 | 2,500 | 2,500 | 3,933 | 2,830 |
| FY2029 | 3,000 | 3,000 | 2,643 | 5,830 |
| FY2030 | 3,000 | 3,000 | 2,000 | 8,830 |
| FY2031 | 3,000 | 2,984 | 1,703 | 11,814 |
| FY2032 | 3,000 | 2,840 | 1,680 | 14,654 |
| FY2033 | 3,000 | 2,832 | 1,687 | 17,486 |
| FY2035 | 3,000 | 2,859 | 1,704 | 23,190 |

*Source: 6,000 starting pool, filter factor 1.0045, CLPT ramp [C602].*

**Figure D1b – Annual terms of the identity, base case**

| Fiscal year | Pool at start S | Entrants E | Leavers L | Treated T | Pool at end | m_eff = L/S | P = T/E | u = T/S | g | Binding limit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| FY2027 (half year)¹ | 6,000 | 1,884 | 1,836 | 330 | 5,718 | 0.306¹ | 0.175¹ | 0.055¹ | -4.7%¹ | Capacity |
| FY2028 | 5,718 | 3,788 | 3,072 | 2,500 | 3,933 | 0.537 | 0.660 | 0.44 | -31.2% | Capacity |
| FY2029 | 3,933 | 3,807 | 2,097 | 3,000 | 2,643 | 0.533 | 0.788 | 0.76 | -32.8% | Capacity |
| FY2030 | 2,643 | 3,826 | 1,468 | 3,000 | 2,000 | 0.556 | 0.784 | 1.14 | -24.3% | Capacity |
| FY2031 | 2,000 | 3,845 | 1,157 | 2,984 | 1,703 | 0.579 | 0.776 | 1.49 | -14.8% | Capacity Q1–Q3, demand Q4 |
| FY2032 | 1,703 | 3,864 | 1,047 | 2,840 | 1,680 | 0.615 | 0.735 | 1.67 | -1.4% | Demand |
| FY2033 | 1,680 | 3,883 | 1,044 | 2,832 | 1,687 | 0.622 | 0.729 | 1.69 | 0.4% | Demand |
| FY2034 | 1,687 | 3,903 | 1,049 | 2,845 | 1,696 | 0.622 | 0.729 | 1.69 | 0.5% | Demand |
| FY2035 | 1,696 | 3,922 | 1,054 | 2,859 | 1,704 | 0.622 | 0.729 | 1.69 | 0.5% | Demand |

*Source: quarterly simulation, m = 0.62, 6,000 launch pool, filter factor 1.0045, CLPT ramp [C602][C610]. E − L − T equals pool end − pool start to rounding in every year, and P(m_eff + g)/(1 − P) reproduces u in every year [C611]. The demand-ceiling rate u_d is 1.68 a year throughout [C603]. ¹FY2027 covers Q3–Q4 only (launch 1 July 2027); its values are raw half-year figures and are not annualised. Annual u is annual treated over the start-of-year pool, so it differs from the quarterly rate: in demand-limited years it comes out at about 1.69 rather than 1.68 because the pool is re-measured each quarter.*

**Reading the table.** Through FY2030 capacity binds in every quarter, so capacity sets P and the accounting sets g. P rises from 0.18 in the half year to 0.66 in FY2028 and about 0.78 to 0.79 in FY2029 and FY2030, above 0.729, because the 3,000 slots are filled from a pool still larger than the long-run level. The pool shrinks fast, by 31% in FY2028 and 33% in FY2029, as leavers and treatment together exceed entrants. Demand first binds in the last quarter of FY2031 and in every quarter from FY2032; from then on referral, willingness and coverage set P. The pool reaches its low of about 1,680 at the end of FY2032 and turns up in FY2033, when g becomes positive (0.4%). Realised P reaches 0.729 in FY2033 and g reaches the 0.5% population growth rate in FY2034, so the long-run path is reached about six years after launch [C610].

Capacity is the limit through FY2030 and almost to the end of FY2031. After that, demand is the limit. Treated settles at about 2,840 a year, which is 0.729 × the roughly 3,900 entrants a year by then. Cumulative treated, counting new entrants, passes 6,000 early in FY2030.

Only about 2,230 of the 6,000 patients in the pool at launch are treated before they leave the window [C605], assuming each quarter's treatments are drawn evenly from launch patients and newer entrants. At m = 0.62 more than half of any group has progressed out within about a year, and capacity in the first 18 months is only 2,830, so most of the launch pool is lost to progression whatever capacity does.

While capacity binds, the treated path is the same for any m, because more patients are waiting than there are slots. What m changes is the leftover pool and how many launch patients are lost (judgment, consistent with the sensitivity runs in D.6).

As an illustration, at $2.0 million per patient, 3,000 patients a year is about $6.0 billion a year [S605][C606].

### D.6 Duration evidence and sensitivity

The published evidence suggests patients stay in the early-manifest window longer than 1.6 years:

- A 2CARE analysis implies about 2.3 to 2.9 years [E601].
- A 2024 *Movement Disorders* paper implies 2 to 3 years [E602].
- An E070 dataset has a mean of 29 months, biased by censoring [E603].
- Marder et al. (2000) found a loss of about 0.97 TFC points a year from TFC 7 to 13, about 5 years from TFC 13 to below 9 [E604].
- The HDSA roadmap puts Stage I at roughly 0 to 8 years after motor diagnosis [E605].

At about one TFC point a year, a 1.6-year stay means a band only about 1.6 TFC points wide, for example 13 down to about 11.4, or about 11 down to 9.4 [C607]. That is a subset of the trial's TFC 9 to 13 window [D602]. The full window would mean a stay of about 4 years, m of about 0.27 and an unfiltered pool of about 13,800 [C607]. Reconciling that with 6,000 needs other eligibility filters (judgment).

**Sensitivity: 2.5-year stay.** At m = 0.40, holding the pool at 6,000 needs an extra filter that removes about 35% of patients [C608]. If the filter applies to both the launch stock and new entrants, treated peaks at about 2,900 in FY2029 and falls to about 1,850 a year. If it applies only to the launch stock, treated holds at 3,000 through FY2031 and settles near 2,850.

**Crossover evidence.** The US trial had 4 sham-surgery controls in the low-dose cohort and 6 in the high-dose cohort. After the blinded 12 months, 4 of the 6 high-dose controls crossed over to treatment; the other two "failed to meet the study's inclusion criteria" [G604][D603]. EHDN's November 2025 report says "four were eligible and accepted the offer" [D604]. Losing two of six in roughly a year implies a leave rate of about 0.41 a year, or a stay nearer 2.4 years [C609]. The sample is tiny, the failed criterion isn't stated, and the outcome for the low-dose controls was not found.

### D.7 Limitations

- m = 0.62 (stay ~1.6 years) is shorter than the duration studies and the crossover evidence, which imply about 0.41 a year. A longer stay lowers long-run demand if the 6,000 reflects a filter on new entrants.
- The 6,000 is the company's addressable-at-launch management estimate, not a treatment target, and the criteria behind the roughly 30% are undisclosed.
- P = 0.729 is an assumption, not a company figure.
- The bull ramp produces a hump at this stay, because demand, not capacity, sets the long-run level.

**Figure D2 – Verified vs assumed**

| Item | Status |
|---|---|
| ~6,000 "Initial Treatable Patients at Launch", Management Estimate | Verified, slide read directly [G601] |
| Prospectus wording on 6,000 | Quoted from secondary research, not reopened [G602] |
| ~30% of ~20,000 | Press paraphrase only [D601] |
| Crossover 4 of 6, 2 failed criteria | Search results and release snippets [G604][D603][D604] |
| Incidence 1.22/100k, 90% early-manifest share | Assumption [S602] |
| P = 0.729, $2.0M price, CLPT ramp | Assumptions [S603][S604][S605] |
| m = 0.62 | Analyst's choice; shorter than the evidence [S601] |
| Duration studies E601 to E605 | Snippets; papers not reopened |


### D.8 UK patient demand (illustrative)

*This section applies the same pool model to the UK. The forecast's UK volumes (bull case only) come from a simple centre engine with a fixed backlog [S9]; the model here shows what an incidence-based pool gives instead. It is illustrative only and is not used in the forecast or the valuation.*

**Incidence.** The UK rate is taken from Wexler et al. (2016), a study of UK primary-care records (the CPRD database): "the incidence of HD has remained constant between 1990 and 2010 with an overall rate of 7.2 (95% CI 6.5 to 7.9) per million person-years", which is 0.72 per 100,000 [D608]. It counts 393 new diagnoses recorded in general-practice records over 1990–2010, is not age-standardised, and its denominator is adults aged 21 and over. Only the abstract and methods were read. The bull case's UK assumption uses 0.48 per 100,000, which is the worldwide pooled rate of Pringsheim et al. (2012), not a UK figure [A16][S9]. The UK rate is about 40% below the US 1.22 used in D.1, although the US figure is from insurance claims, all ages and age-standardised, so part of the gap may reflect case counting rather than disease frequency (judgment).

**Method.** The structure and code logic are the same as the US model in D.3: a quarterly pool, entrants E = incidence × population × 0.90 early-manifest share, leavers (m/4) × pool, a demand ceiling u_d = P\*(m + g\*)/(1 − P\*) = 1.68 a year, and treated each quarter = min(capacity, (u_d/4) × pool, pool). Capacity starts at two treating centres and ramps to long-run demand in thirds: in the first launch year (Q3 2028 to Q2 2029) capacity is the higher of two centres' throughput and one third of long-run demand; in the second year two thirds; from the third year all of it. Long-run demand is 0.729 × launch-year entrants [C612].

**Figure D3 – UK model inputs**

| Input | Value | Type |
|---|---|---|
| UK population | 69M, growing 0.5% a year | Assumption, as in the bull case's UK assumption [S9] |
| Incidence | 0.72 per 100,000 (adults 21+) | Published study [D608] |
| Early-manifest share of entrants | 90% | Assumption, as for the US [S602] |
| Leave rate m | 0.62 a year (progression 0.60, death 0.02) | Judgment, as for the US [S601] |
| Treated share P\* | 0.729 | Assumption, as for the US [S603] |
| Launch | Q3 2028 | Assumption, as in the bull case's UK assumption [S9] |
| Net price | $1.5M per patient | Assumption, from the bull case's UK assumption [S9] |
| Throughput | 1 procedure per centre per week (~52 a year) | Assumption, as in the bull case's UK assumption [S9] |
| Capacity | Two centres at launch, then 1/3, 2/3 and 3/3 of long-run demand | Analyst rule [C612] |

*Source: as tagged.*

**Starting pool.** No company figure exists for the UK. The model starts from the incidence-implied pool E/(m + g) = 723 patients at launch, the same construction that reproduces uniQure's ~6,000 for the US [C612]. The bull case's UK assumption uses a backlog of 2,250 (30% × 7,500) [S9], about three times the incidence-implied pool, with no UK source. Starting from 2,250 instead leaves treated patients unchanged in every year, because capacity binds throughout; it only leaves a larger untreated pool that mostly ages out (1,764 at the end of FY2028 against 674) [C614].

**Results.** Long-run demand is 329 patients a year. Two centres at one procedure a week give 104 a year, slightly below one third of long-run demand (110), so the one-third level sets first-year capacity and the two-centre start never binds. Centres implied are 2.1, 4.2 and 6.3 in launch years one, two and three onward [C612]. Figure D4 reads like Figure D1b: each row is a year, with the pool at the start, the flows during the year and the realised terms of the identity in D.3.

**Figure D4 – UK pool model, incidence 0.72, incidence-implied start pool, 1 procedure per centre per week**

| Fiscal year | Pool at start S | Entrants E | Leavers L | Treated T | Pool at end | P = T/E | u = T/S | g | Binding limit | Centres implied | Revenue at $1.5M (US$M) | Bull case UK: treated / revenue (US$M) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| FY2028 (half year)¹ | 723 | 226 | 220 | 55 | 674 | 0.24¹ | 0.08¹ | -6.8%¹ | Capacity | 2.1 | 82 | 117 / 176 |
| FY2029 | 674 | 454 | 398 | 165 | 565 | 0.36 | 0.24 | -16.1% | Capacity | 3.2 | 247 | 663 / 994 |
| FY2030 | 565 | 456 | 322 | 274 | 424 | 0.60 | 0.49 | -24.9% | Capacity | 5.3 | 412 | 780 / 1,170 |
| FY2031 | 424 | 458 | 235 | 329 | 319 | 0.72 | 0.78 | -25.0% | Capacity | 6.3 | 494 | 780 / 1,170 |
| FY2032 | 319 | 461 | 184 | 329 | 266 | 0.71 | 1.03 | -16.4% | Capacity | 6.3 | 494 | 524 / 787 |
| FY2033 | 266 | 463 | 159 | 329 | 242 | 0.71 | 1.24 | -9.3% | Capacity | 6.3 | 494 | 269 / 404 |
| FY2034 | 242 | 465 | 147 | 329 | 231 | 0.71 | 1.36 | -4.5% | Capacity | 6.3 | 494 | – |
| FY2035 | 231 | 468 | 142 | 329 | 227 | 0.70 | 1.43 | -1.6% | Capacity | 6.3 | 494 | – |

*Source: UK quarterly simulation [C613]; revenue = treated × $1.5M, illustrative only [C615]; bull case UK volumes and revenue from Appendix A [C209]–[C214][C111]–[C115]. E − L − T equals pool end − pool start to rounding in every year [C613]. ¹FY2028 covers Q3–Q4 only (launch 1 July 2028); its values are raw half-year figures and are not annualised, except centres implied, which is annualised capacity over per-centre throughput.*

**What this means.** Capacity binds in every year. Treated rises to 329 a year from FY2031 and holds there, about 42% of the bull case's UK peak of 780; the pool falls from 723 to about 227 by FY2035. Because the capacity rule fixes the long-run level at launch-year demand while entrants grow 0.5% a year, realised P drifts down to about 0.70 rather than settling at 0.729. The bull case's UK assumption treats more because it starts from a 2,250 backlog and lets untreated patients leave at only 10% a year [S9].

**Sensitivities** [C614].

- **Incidence 0.48 per 100,000** (the worldwide pooled rate): start pool 482, long-run demand 219 a year; at one procedure a week the two-centre start (104) exceeds one third of demand (73) and sets first-year capacity; centres implied 2.0, 2.8 and 4.2.
- **Two procedures per centre per week** (incidence 0.72): two centres give 208 a year, above one third of long-run demand and close to two thirds (219); centres implied 2.0, 2.1 and 3.2. Long-run treated is unchanged at 329 a year.

**Main caveat.** The Wexler rate is per adult aged 21 and over, but it is applied here to the total UK population of 69M. That overstates entrants, and so long-run demand, by roughly a quarter to a third (judgment); the model does not correct for it, because no UK adult population share has been sourced.

**Figure D5 – UK model: verified vs assumed**

| Item | Status |
|---|---|
| Incidence 0.72 per 100,000, adults 21+ | Published study; abstract and methods read, full paper not reopened [D608] |
| Pringsheim 0.48 as a worldwide pooled rate | Forecast source entry, not reopened [A16] |
| UK population 69M | Taken from the bull case's UK assumption, not checked [S9] |
| 90% early-manifest share, P\* = 0.729 | Assumptions [S602][S603] |
| m = 0.62 | Judgment [S601] |
| $1.5M price, Q3 2028 launch, 1 procedure per centre per week | Assumptions from the bull case's UK assumption [S9] |
| Capacity ramp in thirds from a two-centre start | Analyst rule [C612] |
