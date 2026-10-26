# US patients eligible for a one-time Parkinson's therapy: base-case model

*Class level, single scenario, FY2026–45. Model: pd_simple2_model.xlsx; chart: pd_simple2_chart.png. Inputs are either published statistics [n] or labelled judgments.*

## Method

**Starting prevalence.** The model starts from the Parkinson's Foundation prevalence project, which estimates at least 930,000 Americans aged 45 or over with Parkinson's disease (PD) in 2020 and 1,238,000 in 2030 [1].

- I interpolate log-linearly between these two points. That implies growth of 2.9% a year and about 1.10 million patients in FY2026.
- The authors call their figures minimum estimates, because they rely on diagnosed, recorded cases [1].
- The Parkinson's Foundation quotes the same 1.2 million for 2030 [2].

**Medical eligibility.** Eligibility follows the DBS label: levodopa-responsive PD of at least four years' duration, with motor complications, no dementia and fit for surgery. There is no age cap.

- **Duration.** Survival in PD falls by about 5% for each year of follow-up [3]. With prevalence growing 2.9% a year, about 73% of prevalent patients were diagnosed four or more years ago. As a check, the Foundation's roughly 90,000 new diagnoses a year [2] against 1.1 million prevalent cases implies an average of about 12 years lived with the diagnosis, which gives a similar share.
- **Dementia.** A systematic review puts the point prevalence of dementia in PD at 24.5% across all studies and 31.1% in the highest-quality ones [4]; I use 28%. I do not multiply dementia and duration as if they were independent. Dementia is rare in the first years after diagnosis, so I subtract it from the four-year group. That leaves 45% of all patients who have had PD for at least four years and do not have dementia.
- **Motor complications.** I assume half of that group have them. This is a judgment anchored to two cohorts:
  - In 3,343 UK patients, off periods affected 35% at 4–6 years and 59% at 8–10 years [5].
  - A population-based incident cohort found motor fluctuations in 54% by five years [6].
- **Diagnosis.** About 81% are taken to have true, levodopa-responsive idiopathic PD. This is the pooled accuracy of clinical diagnosis against pathology [7]. It is a proxy, not a measured response rate.
- **Fitness.** I assume 90% are fit for neurosurgery. This is a judgment; I found no population figure.

**Patients already treated.** About 3,990 PD patients receive DBS each year [8]. Those still alive are removed from the starting pool as annual DBS volume ÷ the leave rate m (42,000). This is a rough steady-state approximation.

| Step (FY2026) | Factor | Patients | Basis |
|---|---|---|---|
| US PD prevalence | — | 1,104,000 | Published [1], interpolated |
| Diagnosed ≥4 years and no dementia | 0.73 − 0.28 | 496,000 | Published [3][4], calculated |
| Motor complications | ×0.50 | 248,000 | Judgment anchored to [5][6] |
| Levodopa-responsive idiopathic PD | ×0.81 | 200,000 | Published proxy [7] |
| Fit for surgery = medically eligible | ×0.90 | 180,000 | Judgment |
| Less patients already treated with DBS | ÷ m | −42,000 | Calculated [8] |
| **Untreated eligible pool** | | **138,000** | |

**Checks on the eligible share.** Medically eligible patients make up 16% of PD, which agrees with the two published figures near 15%:

- Aspen Neuroscience's filing says roughly half of about 300,000 drug-refractory US patients may be eligible for cell-replacement surgery, about 15% of PD [9].
- A German conference abstract cites 10–15% [10].

Neither states its criteria, so both confirm a share, not a level. Clinic studies give a lower bound:

- 4.5% under flexible criteria in Italian movement-disorder clinics [11].
- 6.6% eligible for referral to any device-aided therapy in a Dutch general hospital [12].

Those studies use stricter, more clinical criteria (including age and severity), so a label-based pool should sit above them.

**Flows.** Each year, closing pool = opening pool + entrants − leavers − treated.

- **Leavers.** A share m of the pool leaves each year through death (5% a year [3]) or new dementia (4.45 per 100 person-years [13]). So m = 0.095, and patients stay eligible for about ten years on average.
- **Entrants.** I set first-year entrants so that the pool, with only DBS treatment, would grow at the same 2.9% as prevalence: (m + g) × pool + DBS = 21,000 in FY2026. They then grow at 2.9% a year.
- **Pool growth.** Entrants exceed leavers, so the pool grows unless treatment absorbs the gap.
- **Treated.** Before launch in FY2029, treatment is DBS only, held flat at 3,990. From launch, 7% of the opening pool is treated each year (a judgment).

## Results

| FY | 2026 | 2029 | 2030 | 2032 | 2035 | 2040 | 2045 |
|---|---|---|---|---|---|---|---|
| Untreated pool, start of year (k) | 138 | 151 | 149 | 148 | 151 | 167 | 189 |
| Entrants (k) | 21 | 23 | 24 | 25 | 27 | 31 | 36 |
| Treated (k) | 4.0 | 10.5 | 10.4 | 10.3 | 10.6 | 11.7 | 13.2 |
| Treated ÷ entrants | 0.19 | 0.46 | 0.44 | 0.41 | 0.39 | 0.37 | 0.36 |

**Launch.** Treatment rises from DBS's 4,000 to about 10,500 in the launch year. The extra comes from the backlog that built up in the pool before launch. Over the next few years the pool is drawn down slightly, then grows again with entrants.

**Settling.** The treated count does not stop growing; it settles at a constant share of entrants. That share is u/(m + u + g) = 0.07/0.194 ≈ 36%.

**Two different shares.** The share above is a different quantity from the share of any single group of entrants who are eventually treated, u/(m + u) ≈ 42%. Because each year's entrants outnumber the previous year's, the treated count in a given year is compared with a larger, newer group of entrants. The two shares describe different groups; there is no second wave.

**Plausibility check.** A judgment funnel gives about 30% treated (referral 0.55 × willing 0.60 × coverage 0.90). Referral and coverage are judgments, and willingness is anchored to published consent and implant rates [14][15]. A 7% treatment rate therefore implies somewhat more uptake than that funnel.

**Illustration.** At $20,000 per patient, FY2040 treatment is worth about $230 million.

## Weak points

1. The motor-complication share and medical fitness are judgments, and together they move the pool more than any published input.
2. The diagnosis factor is a proxy for levodopa response.
3. The dementia midpoint and the assumption that dementia sits almost entirely in patients diagnosed four or more years ago are simplifications.
4. The 5% death rate comes from all PD patients; patients without dementia probably die less often, which would lengthen the time spent in the pool.
5. Removing patients already treated with DBS (42,000) is approximate.
6. The 3,990 counts inpatient procedures only.
7. Prevalence is a published minimum, so the pool is more likely too low than too high.
8. The 7% treatment rate and the FY2029 launch are assumptions.

## Sources
1. Marras et al. Prevalence of Parkinson's disease across North America. npj Parkinson's Dis 2018. https://doi.org/10.1038/s41531-018-0058-0
2. Parkinson's Foundation. Prevalence & incidence. https://www.parkinson.org/understanding-parkinsons/statistics/prevalence-incidence
3. Macleod et al. Mortality in Parkinson's disease: systematic review and meta-analysis. Mov Disord 2014. https://doi.org/10.1002/mds.25898
4. Aarsland et al. Systematic review of prevalence studies of dementia in PD. Mov Disord 2005. https://doi.org/10.1002/mds.20527
5. Motor complications in Parkinson's disease: results from 3,343 patients followed for up to 12 years. PMC11145112. https://pmc.ncbi.nlm.nih.gov/articles/PMC11145112/
6. Motor complications in Parkinson's disease: 13-year follow-up of the CamPaIGN cohort. PMC7063985. https://pmc.ncbi.nlm.nih.gov/articles/PMC7063985/
7. Rizzo et al. Accuracy of clinical diagnosis of PD. Neurology 2016. https://doi.org/10.1212/WNL.0000000000002350
8. Venkatraman et al. DBS utilization in the US, NIS 2012–19 (Table 1). https://pmc.ncbi.nlm.nih.gov/articles/PMC10898494/
9. Aspen Neuroscience, Form S-1, Oct 2026. https://www.sec.gov/Archives/edgar/data/2124080/000119312526419104/na-20261009.htm
10. Reasons for underutilisation of DBS. GMS abstract 2012. https://doi.org/10.3205/12dgnc047
11. Morgante et al. Parkinsonism Relat Disord 2007. https://pubmed.ncbi.nlm.nih.gov/17347021/
12. Moes et al. (D-DATS). Parkinsonism Relat Disord 2023. https://doi.org/10.1016/j.parkreldis.2023.105359
13. Gibson et al. Risk of dementia in PD: systematic review and meta-analysis. Mov Disord 2024. https://doi.org/10.1002/mds.29918
14. Dinkelbach et al. Willingness to undergo DBS among Parkinson's patients. BMC Neurology 2017 (43.2% consent to referral). https://doi.org/10.1186/s12883-017-0820-7
15. Multidisciplinary DBS screening. Mov Disord Clin Pract 2018 (58.7% of patients evaluated proceeded to implant). https://pmc.ncbi.nlm.nih.gov/articles/PMC6183455/
