## Status and open items

**Current:** v11, as of 2026-10-26. Finagle `run_case` value per share (cost of equity 10.453% = 10-year 4.953% + 5.5% ERP; gt default 4.953%): base $65.20, bull $88.36, bear $14.56; after David's ×0.90 dilution estimate $58.68 / $79.52 / $13.10. Valuation inputs are David's (2026-10-26): +$50M Oberland draw in 2026, debt 2.0× EBITDA from the first positive-EBITDA year, SBC $8M until then and linear in dollars to 5% of FY2040E EBITDA, explicit EBITDA to FY2031E, gsnext 15% fading to terminal by FY2040E (year 15), roict 25%, rd 9.2%. Scripts and outputs are in `valuation_v11/`. The sections below this block still carry their earlier version label; `report.md` and the `partners/pd_simple4_*` and `partners/partners_v4_*` files are current.

**Presentation window (2026-10-26, David):** the report's explicit forecast ends at FY2031E (base revenue $410.4M, EBITDA $170.8M; bull $502.1M / $225.0M; bear $180.2M / $25.8M). forecast.json still runs to FY2032E (unchanged; model outputs unchanged), but FY2032E is not presented; the valuation fades growth with Finagle from FY2032E (15.0% → ~6.1% by FY2040E). Notes below for v8–v10 that mention FY2032E+ are history.

**Closed in v11:** bull at 8% treated share confirmed by David; cost of equity set to 10-year + ERP (no beta; David: med-tech beta is low); SBC fade artifact fixed (explicit dollar path replaces the ratio fade that produced negative SBC); $50M 2026 draw and 2× leverage modelled; rd 9.2% (no double count of the 11.3% effective rate).

**Open items**
1. Dilution is a flat ×0.90 outside Finagle; the borrowing an equity raise would replace stays in the model.
2. Bear cash reaches −$98M (FY2030E–32E) with no funding modelled.
3. Oberland revenue participation and prepayment premiums are approximated through the 9.2% rate; model starts from 10-K debt $49.077M vs. $50.2M at Q2 2026.
4. About 86% of base value comes after FY2031E and 54% from terminal value.
5. The Parkinson's capacity decomposition ($39.25) and the per-$20M add-on ($2.69/share) in the report are from Oct 25 runs and were not rerun on v11 inputs.
6. Report Appendix B: sources A41–A43 and D71–D76 are out of order.
7. `partners/partners_v4.md` has no PDF or Word version.
8. Epilepsy, FTD and glioblastoma funnels not rebuilt on the pool method.
9. ClearPoint platform share (100%) is an assumption.
10. Motor-complication share (50%) and surgical fitness (90%) in the PD pool are judgments.

**How to resume** (from `forecasts/CLPT/`, in order)
1. `python partners/pd_simple4_model.py` → `pd_simple4_model.json` (PD pool and class demand; inputs coded in the script, plus `partners/census_nc-est2024-agesex-res.csv`).
2. `python partners/partners_v4_model.py` → `partners_v4_model.json` (partner table; reads the PD model JSON).
3. `python build_forecast.py` → `forecast.json` and the `CLPT_base/bull/bear.xlsx` files (reads the PD model JSON).
4. `python run_finagle.py` → `finagle_run.json` (needs a read-only `finagle` checkout beside this repo; its input `clpt_baseline.json`, the `build_baseline('CLPT')` output of 2026-10-23, is in this folder). `finagle_perpetuity.py` reruns the perpetuity yardstick. The current valuation: `python valuation_v11/run_finagle_v11.py` and `python valuation_v11/sensitivity_v11.py` (paths inside point to the working output folder; adjust before rerunning).
5. `python render_report.py` → `report.pdf`; `python ../../tools/md2docx.py report.md report.docx` → Word.
6. `pytest` from the repo root.

finagle and ceochat are read-only inputs.

**Where the reasoning lives:** `report.md` — Business Drivers by Line, Forecast (including Valuation), Appendix A (Bull and Bear Cases), Appendix C (Parkinson's eligible-pool model), Appendix D (Partner programs) and Appendix E (Method). Changes by version are in `revision_log.md`.

# ClearPoint Neuro (Nasdaq: CLPT) forecast, FY2026E–FY2032E (v8)

USD millions. As of 2026-10-23. Built with `.cursor/skills/forecaster` (forecaster b915ace). Numbers come from `build_forecast.py` → `forecast.json` (passes `forecastcheck.validate_payload`; 14 tests pass). Finagle: `run_finagle.py` → `finagle_run.json` (finagle bb39642, read-only). The v1 inputs are recorded in `revision_log.md`.

**Prompt [P1]:** uniQure's AMT-130 (Huntington's) and BlueRock/Bayer's bemdaneprocel (Parkinson's) are approved.
**Prompt [P2]** (David, 2026-10-23): every procedure is priced at $20k, for both therapies and in all cases. Volumes assume ClearPoint's capacity is fully used, ramping up, based on Burnett's Q2 2026 capacity comments [G7]. Volume and timing choices are judgments, marked ★.

## 1. Frame
- Lines (2025 10-K) [A2]: BDD, NNT, CES, plus a **scenario** line, Commercial drug delivery (AMT-130 + bemdaneprocel). FY2025A revenue $36.971M [A1]. H1 2026A $23.008M [A4].
- Explicit window **FY26E–FY30E** [P2], extended so both ramps are explicit. FY28E–FY30E rest mostly on judgments. Note: forecastcheck checks growth compounding only up to FY28E.
- Scenario levers: approval timing, ramp speed and utilisation (price is fixed by P2), core totals and growth, and costs.

## 2. Totals
Unchanged from v1. FY2025 position in the original range: C = 0.19 [C13]. 2026 guidance was revised on Aug 3, 2026, from $52.0–56.0M to $48.0–52.0M [G2]. Totals therefore follow consensus: FY26E $49.0M and FY27E core $56.55M (Equibles, 2 analysts) [E1]. The scale factor is 1.07 for H2 2026 [C4] and 1.04 for FY27 [C6] in the base case. The bull H2 2026 factor is 1.11, which is **above the 10% flag**: consensus-high H2 sits well above the line drivers. Consensus is assumed to **exclude** commercial drug delivery [S19][G3]. **Double-count risk** if analysts already model it. Core FY28E–FY30E grows +12%/yr (bear 8%, bull 15%) [S7][S26] ★.

## 3. Procedure line (the main change)

**Capacity source [G7]:** Burnett (Q2 2026 call): 15 centres "ready to do 1, if not 2" a week; 20–30 centres "50 to 100 cases a week".
**Ramp per therapy ★ [S20]:**
- Launch half-year: 10 centres × 1.5/wk × 22 wks ≈ 330.
- First full year: 20 × 2.5 × 50 ≈ 2,500.
- Second full year: 30 × 3 × 50 ≈ 4,500.
- Later years: held at that cap.

**AMT-130 pool:** uniQure's "~6,000 patients* Initial Treatable Patients at Launch" (*management estimate), out of ~20,000 diagnosed [G8].
**Newly eligible per year:** ~1,226 (derived) [C22] = US population 335M [S28 ★, approximate] × age-adjusted incidence 1.22/100k person-years [A7] × treatable/diagnosed 30% [C21]. This is a sourced rate combined with a derived eligibility share. No source gives a newly *eligible* count directly.

**Bemdaneprocel:**
- Bayer expects Phase 3 results in 2028–29. This comes from a Reuters report [D19] that I could read **only in search snippets**: the article is paywalled and was not opened.
- ClinicalTrials.gov lists primary completion as March 2027 [D10].
- Pool ~88k (derived) = 1.1M US PD [D20] × 16% with motor fluctuations [D21] × 50% for exPDite-2 age/duration/stage criteria [S27 ★]. **Not binding.**
- **Risk:** the therapies would share centres and neurosurgeons, so a separate bemdaneprocel ramp may be too high.

| Procedures | FY27E | FY28E | FY29E | FY30E | Rule |
|---|---|---|---|---|---|
| Base AMT-130 | 330 | 2,500 | 3,170 | 1,226 | Approval spring 2027, launch Q3 [S8]. FY29 = rest of the 6,000 pool. FY30 = new eligibles ★ |
| Base bemdaneprocel | 0 | 0 | 330 | 2,500 | Approval H2 2029 ★ |
| Bull AMT-130 | 880 | 4,500 | 3,072 | 1,226 | Launch half at 20 × 2/wk × 22. Cap in FY28. FY29 = rest of pool + 2 years of new eligibles ★ |
| Bull bemdaneprocel | 0 | 0 | 1,480 | 4,500 | Approval early 2029: 20 × 2/wk × 37 wks, then cap ★ |
| Bear AMT-130 | 0 | 948 | 2,100 | 2,700 | Ramp a half-year slower at 60% utilisation. Pool not binding by FY30 ★ |
| Bear bemdaneprocel | 0 | 0 | 0 | 198 | Approval 2030, launch half at 60% ★ |

Revenue = procedures × $20k [P2]. Base: $6.6M / $50.0M / $70.0M / $74.5M.

## 4. Costs and EBITDA (EBITDA before SBC, Finagle basis)
- Core gross margin held at the H1 2026A level of 62.9% [S13]. **Procedure gross margin 70% ★ [S23]:** the 10-K says disposables produce "high margin revenue" but gives no percentage, so the 70% is a judgment.
- Core cash opex:
  - H1 2026A $27.46M [C2].
  - H2 2026E: H1 −2% [S14] (bear: flat).
  - FY27E: 2 × H2 +6% (bear +10%).
  - FY28E–FY30E: +5%/yr (bear +7%) [S15][S16].
- Procedure opex ★: 10% of procedure revenue for clinical specialists [S24], plus $2.0M/yr per launched therapy for field support [S25].

| Base | FY25A | FY26E | FY27E | FY28E | FY29E | FY30E |
|---|---|---|---|---|---|---|
| Revenue | 36.971 | 49.000 | 63.150 | 113.336 | 140.936 | 153.969 |
| Gross margin | 61.4% | 62.9% | 63.6% | 66.0% | 66.4% | 66.3% |
| Cash opex | – | 54.363 | 59.703 | 66.895 | 73.889 | 77.486 |
| EBITDA | −15.170 | −23.555 | −19.527 | 7.927 | 19.711 | 24.630 |
| EBITDA margin | −41.0% | −48.1% | −30.9% | 7.0% | 14.0% | 16.0% |

## 5. Scenarios

| | Bear | Base | Bull |
|---|---|---|---|
| Revenue FY26–30E | 48.0 / 56.0 / 79.4 / 107.3 / 128.5 | 49.0 / 63.2 / 113.3 / 140.9 / 154.0 | 50.0 / 74.7 / 155.7 / 166.6 / 201.4 |
| EBITDA FY26–30E | −24.7 / −25.2 / −17.2 / −4.9 / 1.1 | −23.6 / −19.5 / 7.9 / 19.7 / 24.6 | −22.9 / −12.6 / 33.4 / 35.2 / 53.3 |
| Procedures FY27–30E | 0 / 948 / 2,100 / 2,898 | 330 / 2,500 / 3,500 / 3,726 | 880 / 4,500 / 4,552 / 5,726 |
| Finagle mc / gsnext ★ | 0.45 / 20% | 0.50 / 10% | 0.55 / 5% |

gsnext reflects how much ramp is left after FY30: bear still ramping, bull already at cap with the AMT-130 pool exhausted.

## 6. Finagle (2026-10-23)

Run order: `build_baseline('CLPT')` → forecaster leaves → filled inputs → `validate_case` (missing [], errors []) → `run_case`. `gt` was **not set** (Finagle default 4.95% = 10-year yield). Defaults kept: re 10.45% and roict 15%.

Filled inputs (same as v1):
- shares 30.503M (10-Q, Jun 30, 2026)
- horizon 10 years
- rd 8.25% (notes' minimum coupon, 10-Q; effective rate 11.3%)
- tax 21%
- NOL $258.2M (2025 10-K)
- noa 0
- dwc zero
- distribution none
- debt held flat

| | Bear | Base | Bull |
|---|---|---|---|
| Value per share | $12.28 | $15.39 | $20.87 |
| vs. $9.25 (derived) | +33% | +66% | +126% |
| Equity ($M) | 328.8 | 423.6 | 590.7 |
| Minimum cash in model ($M) | −114.3 | −38.6 | −26.5 |

- **Flags (all cases):** "negative cash" and "negative FCFE after year 1". Funding needs are treated as costless equity, so **dilution is not modelled**.
- **Warnings:** an acquisitions-evidence warning, which is harmless. In the base case only, "average EBITDA growth is 14.2%", an artefact of the sign changes.
- **Why bull is only modestly above base:** the 6,000-patient AMT-130 pool is used up by FY29, so the terminal year carries only new eligibles.

## 6b. v3 changes (2026-10-23)

- AMT-130 steady state 3,000/yr from FY30E (bull 3,500): 73% of US HD incidence 4,087 (335M × 1.22/100k), 66% of US+UK 4,543 (UK 0.67/100k × 68M) [S30][C23–C25] ★. FY29 still = rest of 6,000 pool (3,170).
- Bemdaneprocel steady state 4% of US PD incidence (90,000/yr, Parkinson's Foundation) ≈ 3,600/yr; bear 2%, bull 5% (= 4,500 cap). Anchor: 3,990 PD DBS in 2019 (NIS, Venkatraman 2024 Table 4) = 4.4% of incidence [S31][C26] ★. Reached after FY30 (FY30 = 2,500 capacity-limited).
- Bear = slow launch: AMT-130 0/270/1,000/2,000 FY27–30.
- gsnext fixed: base 12%, bull 15%, bear 8% (was inverted).
- Base revenue FY26–30 49.0/63.2/113.3/140.9/189.4; EBITDA −23.6/−19.5/7.9/19.7/45.9.
- Finagle: base $22.44, bull $41.56, bear −$1.19 (price $9.25). Detail, PV split and sensitivities in finagle_valuation.json (finagle_valuation.py) and report.md section 7.

## 6c. v4 changes (2026-10-23, David t350u)

- Explicit window extended to FY32E so bemdaneprocel reaches steady state in all cases: base 3,600 from FY31E, bull 4,500 from FY30E, bear 1,500 (FY31E) → 1,800 (FY32E) [S32]. AMT-130 3,000 (bull 3,500); bear AMT-130 2,500 → 3,000. Core growth and opex growth continue at S26/S16.
- Base revenue FY31/FY32 221.0 / 231.7, EBITDA 61.8 / 65.1. Bull 259.9 / 274.8 and 85.5 / 91.4. Bear 156.2 / 178.3 and 12.7 / 20.6.
- gsnext now derived (C29): FY32 core x core growth / FY32 revenue = 5.2% base, 6.3% bull, 3.7% bear (procedures flat at steady state). me = FY32E margin.
- Finagle (year = 10, gt default, 7 explicit years): base $19.58, bull $29.86, bear $4.83 (price $9.25).
- Template table: finagle_template_table.py re-executes saved notebook code (finagle_notebook_<case>.py) and fills company_template.xlsx -> CLPT_<case>.xlsx; report Figures 9-10.

## 6d. v5 changes (2026-10-23, David t352u)
- **CAL** = ClearPoint Advanced Laboratories: 30,171 sq ft preclinical CRO lab, Torrey Pines, San Diego; lease June 2025, final phase available Jul 13, 2026 (Q2 10-Q). First GLP SOW "multi-million", recognised by end H1 2027; capacity ">$60 million" vs ~$8M before; large studies from H2 2027; one large GLP study $15–20M (Q2/Q4 calls) [G9–G11]. Modelled as an uplift line on top of core growth (reported inside BDD): base 0/6/12/18/24/30, bull 3/10/18/27/36/45, bear 0/2/4/6/8/10 ($M FY27–32) [S37] ★; core GM less 20% incremental opex [S38] ★.
- **PD funnel** replaces 4% of incidence: bottom-up 90,000 × 12.5% candidates × 70% exPDite-2 × 40% willing × 60% fit = 1,890/yr [C31] (floor); DBS-calibrated 3,990 × expansion (1.0/1.4/2.0) × access (60/70/80%) × share (35/50/65%) = 838 / 1,955 / 4,150 → steady 800 / 2,000 / 4,000 (0.9% / 2.2% / 4.4% of incidence) [S33–S36][C32][C33]. Ramps: base 330/1,200/1,800/2,000 FY29–32; bull 1,000/2,400/3,300/4,000; bear 100/400/650 FY30–32 (800 FY33). Bear AMT-130 now 0/270/1,000/1,800/2,300/2,700 (3,000 FY33).
- **Fade**: Finagle year = 20 (validate_case accepts any integer ≥1; gsnext interpolated linearly to default gt at year 20). gsnext (C29) = FY33 growth with core at S26, one more CAL increment, procedures stepping to steady state: 7.8% base, 8.5% bull, 11.0% bear. Base growth path FY29–FY45: 28.2, 18.6, 15.2, 9.9, 7.8, 7.6 … 5.2%. gt never set.
- Base revenue FY30/31/32 181.4 / 209.0 / 229.7, EBITDA 38.0 / 50.5 / 58.7 (25.6%). Bull 231.8 / 271.9 / 309.8 and 66.9 / 86.5 / 104.7. Bear 114.5 / 138.2 / 159.3 and −8.3 / 0.6 / 7.5.
- Finagle: base $24.77, bull $43.84, bear $9.67 (v4 $19.58 / $29.86 / $4.83). At year = 10: $19.28 / $35.13 / $3.45.

## 6e. v6 changes (2026-10-23, David t353u: base must be central, not conservative)

- Bemdaneprocel rebuilt as demand = displaced DBS-type demand (3,990 × 85% window × 80% switch × 90% access) + expansion into the 7,260 candidates a year not getting DBS (× 30% × 80%) = 4,184 a year (bull 5,840, bear 2,234) [C36, C37; S39–S42 ★]. A prevalent backlog of about 42,000 at launch [A15, C38] means capacity, not demand, binds in base and bull.
- Capacity [S43 ★]: base S20 ramp 330 / 2,500 / 4,500, expanding to 5,000 in FY2032E (top of Burnett's G7 quote); bull 1,000 / 3,000 / 5,000 / 6,500 → 7,500; bear demand-bound 200 / 1,200 / 2,000 → 2,500 (below DBS volume: weaker efficacy, reimbursement).
- Other bias review: core growth base 12%→15%, bull 15%→18% (G12; FY2027E consensus 15.4%); CAL base FY2032E $30M→$36M (60% of capacity). Unchanged after review: AMT-130 (3,000 is already 73% of US incidence), mc 0.50/0.55/0.45, procedure GM 70%, specialist 10% + $2M, bear core growth 8%.
- Revenue FY30–32E: base 218.0 / 277.9 / 309.7; bull 250.8 / 316.7 / 375.6; bear 116.5 / 154.2 / 186.3. EBITDA: base 59.5 / 91.3 / 106.1; bull 78.5 / 113.7 / 144.6; bear -7.1 / 10.2 / 23.7.
- Finagle (20 yrs, gt default never set): $39.25 / $77.99 / $18.66 (v5 $24.77 / $43.84 / $9.67); gsnext 7.8% / 14.0% / 13.2%.

## 6f. v7 changes (2026-10-25, David t396)
- PD demand: v5/v6 funnel (displacement + expansion + backlog, S39–S42, C36–C38) replaced by the pd_simple2 eligible-pool model (partners/pd_simple2_model.json): class demand = treated − 3,990 DBS = 6,545 / 6,415 / 6,353 / 6,349 FY29–32E, 6,395 FY33E, 7,672 FY40E (C40, A30–A40, S44–S47).
- Bemdaneprocel: capacity ramp capped at class demand; capacity base 5,000 / bull 7,500 / bear 4,500 (S43). Bull binds at 6,349 FY32E; bear approval 2030, base ramp one year later.
- HD (AMT-130) unchanged: 3,000/yr from FY30E, consistent with partners table.
- Finagle rerun: 39.25 / 57.67 / 16.72 (v6 39.25 / 77.99 / 18.66). New finagle_perpetuity.py: +$20M/yr from FY30E at 60% EBITDA = +$2.60/share (C43, S48).
- Report: new Appendix C (PD pool) and D (partner programs, not in forecast); Method → Appendix E.
- Tags added: A21–A40, D33–D62, S44–S48, S52–S58, C40–C45, C50–C54. Removed: D28, D30, A11, A13, S18, S27, S33–S36, S39–S42, C22, C26, C31, C32, C36–C38.

## 6g. v8 changes (2026-10-25, David t400u)
- Bull PD: same pool structure, u = 9% (S59) and 50% of DBS 3,990 displaced to the class (S60): class demand 11,550 / 11,112 / 10,814 / 10,634 FY29–32E, 10,550 FY33E, 11,646 FY40E (C46). Bull capacity 10,000 (~67 centres x 3/wk, aggressive, S61); ramp 1,000 / 4,000 / 7,000 / 10,000 FY29–32E, steady state 10,000 from FY32E.
- Reached within explicit years because Finagle's gsnext would compound a post-FY32 step (C29, C47).
- Bull: revenue FY32E 445.6, EBITDA 186.6, me 41.9%, gsnext 7.3%; value $65.25 (was $57.67). Base $39.25 and bear $16.72 unchanged.
- Bear examined: v6-style 2,500 path gives $18.66 only through an 8.6-pt one-year step in gsnext (C47); kept 4,500.
- New pool chart pd_pool_chart.png (pd_pool_chart.py) with legend "treated includes DBS"; partners/ originals untouched.

## 6h. v9 changes (2026-10-25, David t404u, t405u, t407u)
- Base treated share u 7% → 6% of the opening untreated eligible pool from FY2029E (S45), anchored on DBS: 3,990 / 137,813 = 2.9% (FY2026E start), 2.7% (FY2028E start) (C49); 6% ≈ twice DBS. Judgment, no published support.
- Class demand (treated − 3,990): 5,040 / 5,019 / 5,041 / 5,100 (FY29E–32E), 5,193 (FY33E), 6,511 (FY40E) (C40). Pool model partners/pd_simple3_model.py.
- Class lumping (S62): PD line = all one-time PD cell/gene therapy procedures; capacity ramp to FY32E, class demand from FY33E phased 1/3 per year FY33E–35E (C48). FY33E volume: base 5,064, bull 10,183, bear 4,731.
- ClearPoint 100% of class procedures (S63, David view; D1 10-K names Brainlab/Renishaw as competitive).
- Finagle: base 40.26 / bull 68.39 / bear 19.81 (gsnext 8.2 / 8.1 / 8.1%). Without lumping 39.25 / 65.25 / 16.72. Perpetuity +$20M from FY30E +$2.58.
- Bull unchanged mechanism (9%, 50% DBS displaced, cap 10,000). Partners split partners_v3 (illustrative).

## 6i. v10 changes (2026-10-25, David t414u, t415u, t416u)
- Eligible pool 137,813 → 179,813: patients who have had DBS stay in the pool (not mutually exclusive; trials exclude them as an entry rule only, A41–A43, S44). DBS 3,990 is context only, not deducted (2.2% of the pool, C49). Pool model partners/pd_simple4_model.py; E0 = (m + g) × pool = 22,300.
- u = 6% of the pool from FY2029E applies to one-time therapy only (≈2.7× DBS, S45). Class demand 11,756 / 11,391 / 11,126 / 10,945 (FY29E–32E), 10,837 (FY33E), 11,454 (FY40E) (C40).
- Three-year ramp to demand (S64, David): 1/3, 2/3, then 100% from FY2031E; no FY33E phase-in (C48 removed). Base volume 3,919 / 7,594 / 11,126 / 10,945; rationale "gives time for other therapies to get approved" is David's judgment (other PD launches FY2033–34E, after the ramp). Implied centres 74 base / 95 bull vs management 20–30 (aggressive, S43).
- Bull u = 8% (S59, to be confirmed by David), same ramp: 5,225 / 9,917 / 14,272 / 13,833. Bear: trial-style exclusion (pool ~138k, C55), approval 2030, capacity 4,500 binds every year. S60, S61, C47 removed.
- Finagle: base 54.29 / bull 72.68 / bear 16.72 (was 40.26 / 68.39 / 19.81). Bridge base: 40.26 − 1.01 (phase-in removed) = 39.25; pool alone +0; ramp to demand +15.03. gsnext 5.1% base. Perpetuity +$20M from FY30E +2.69.
- Partners partners_v4 (illustrative split; 15,986 procedures / $319.7M at 100% by FY2036E).

## 7. Assumptions to revise (★)
1. Ramp and capacity [S20–S22]: the biggest driver. Burnett's figures describe capacity, not demand.
2. AMT-130 pool of 6,000 [G8] and new eligibles of ~1,226/yr [C22].
3. Bemdaneprocel approval timing (Reuters snippet only) and shared-centre risk.
4. Procedure gross margin 70%, specialists 10%, $2M fixed per therapy [S23–S25].
5. Consensus excludes procedure revenue [S19].
6. Core growth 12% for FY29–30 [S26]. mc / gsnext [S17][C29].
7. CAL uplift path and margin [S37][S38]; PD funnel expansion/access/share [S34–S36]; 20-year fade horizon [S29].

## 8. Sources
The tag and document list is in `report.md` Appendix B (D1–D32). Fact tags A1–A15, G1–G12, E1–E2, P1–P2, S1–S43 and C1–C38 are as used there and in `forecast.json`.
