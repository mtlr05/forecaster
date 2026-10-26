# US eligible PD pool: proposed base-case method (for agreement)

*One scenario, class level, 24 Oct 2026. Tags: A published, C calculated, S judgment (★), P David May's instruction. Model: pd_simple_model.xlsx (tabs Method, Inputs, Flow).*

**1. Who counts as medically eligible.** The criteria follow the DBS label:

- levodopa-responsive PD;
- at least 4 years since diagnosis;
- any motor complication;
- no dementia;
- medically fit;
- no age cap. Medtronic's label has none.

**2. Starting pool (FY2026), in thousands of patients.**

| Step | Patients | Source |
|---|---|---|
| US PD prevalent | 923k | C, cohort model |
| Alive, no dementia, ≥4 years since diagnosis (×0.38) | 347k | C; dementia rates vary by age (A, CamPaIGN; Sydney) |
| With motor complications (×0.66) | 230k | C (A, Ahlskog; Hely) |
| Levodopa-responsive (×0.81) | 186k | A, Rizzo 2016 |
| Medically fit (×0.90) = medically eligible | 167k | S ★ |
| Less patients already treated with DBS (3,990 ÷ m) | about −31k | C ★ |
| **Untreated eligible pool, start of FY2026** | **about 136k** | C |

The same screens give 140k eligible in 2019 (18% of PD). That is the 140k agreed as the starting point, before netting out DBS patients and rolled forward to FY2026.

**3. Funnel.** Medically eligible ⊃ referred ⊃ willing ⊃ covered ⊃ treated. P = referral 0.55 × willing 0.60 × covered 0.90 = **0.30** (S ★).

**4. Stock and flow each year.** Pool end = pool start + entrants − leavers − treated.

- **Entrants** are newly eligible patients: 26k in FY2026, growing 2.6% a year with the ageing population (C).
- **Leavers** = m × pool start, with **m = 0.13**. In the cohort, (deaths 13.7k + dementia onsets 7.8k) ÷ pool start 162.8k = 0.13. Mean time eligible is 1/m ≈ 7.5 years.
- **Treated.** Before launch, DBS only (3,990 a year, held flat; A, NIS 2019). From launch in FY2029, u × pool start, with **u = P(m + g) ÷ (1 − P) = 0.066**.
- **Why u includes g.** Without g, treated would settle at u ÷ (m + u + g), about 0.26 of entrants, not 0.30, because entrants keep growing. Adding g makes treated converge to exactly P × entrants (checked to 2100).

**5. Result: treated = class demand (thousands of patients a year).**

| FY2026 | FY2029 | FY2030 | FY2032 | FY2035 | FY2040 | FY2045 |
|---|---|---|---|---|---|---|
| 4.0 (DBS) | 9.8 | 9.7 | 9.7 | 10.1 | 11.1 | 12.5 |

- **Treated as a share of entrants:** 0.35 at launch (the backlog being drawn down), 0.32 in FY2032, 0.30 from FY2040.
- **Pool path:** 136k in FY2026, 149k at launch, 148k in FY2032, 169k in FY2040, 190k in FY2045.
- **Illustration only:** at $20k per patient, FY2040 demand is about $220M.

**6. Sanity check.** Today's DBS-implied P is 3,990 ÷ 21.6k entrants (2019) = 0.18. The class P of 0.30 is higher, as it should be, because the class includes DBS-type patients.

**Excluded on purpose:** allocation between therapies, therapy-specific willingness, capacity, and disease-modifying use.

**Judgment inputs to challenge**

1. P = 0.30. Its factors:
   - Referral 0.55 (evidence range 30–80%).
   - Willing 0.60 (published 35–43% is consent to referral; 58.7% of patients evaluated go on to implant).
   - Covered 0.90.
2. Medically fit 0.90, and no age cap. A cap of 75 would remove a large share of the pool.
3. Netting out patients already treated with DBS: about 31k assumes 3,990 a year in the past and the same leave rate as untreated patients.
4. Launch in FY2029, with treatment of the full u × pool from year one (no ramp-up).
5. DBS volume held flat at 3,990 before launch.
