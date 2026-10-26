import json
d=json.load(open('pd_pool_model.json')); m=json.load(open('/tmp/xlsx_map.json')); p=d['inputs']; co=d['cohort']
S={k:{r['t']:r for r in v['rows']} for k,v in d['scen'].items()}; SC=d['scen']; C=S['8%']; NM=['5%','8%','10%','15%']
k=lambda x:f"{x/1e3:,.1f}"; pc=lambda x:f"{x*100:.0f}%"; pc1=lambda x:f"{x*100:.1f}%"
FR=m['FR']; du=p['dbs']*p['dbs_u']; rwc=p['r']*p['w']*p['c']; tb=d['tornado_base']
K1={r['t']:r for r in SC['8%']['k1']}
L=[];a=L.append
a("# US pool for a one-time restorative Parkinson's therapy: class-level demand\n")
a("*ClearPoint Neuro (CLPT) working paper, 24 Oct 2026. Scenario analysis, not guidance. Tags: A = published data, C = calculation, S = judgment (★), P = instruction from David May, D = document. Sources are listed at the end; every number traces to pd_pool_model.xlsx (sheet and cells shown under each table). Counts in tables are in thousands of patients.*\n")
a("## Summary\n")
a("- **Question.** How many US patients a year would have a one-time restorative PD procedure at class level if its label looked like DBS's? Not split across the four therapies and before ClearPoint's capacity. Disease-modifying use is excluded (section 7).")
a("- **Funnel.** Medically eligible ⊃ referred ⊃ willing ⊃ covered ⊃ treated. Eligibility is an explicit scenario input. The only calibrated number is the downstream product referral × willing × covered (P), set so that modelled DBS under age 75 matches the 2019 volume (3.4k a year) [A10, S5].")
a(f"- **Central eligibility: 8% of US PD (point prevalence) ★**, equal to {pc1(SC['8%']['LF'])} of incident patients becoming eligible at some point. At 8%, the implied P is {SC['8%']['P']:.2f}. That matches an independent judgment of the stages (referral {pc(p['r'])} × willing {pc(p['w'])} × covered {pc(p['c'])} = {rwc:.2f}).")
a(f"  - 5% needs P = {SC['5%']['P']:.2f}, which puts every stage near the top of its range.")
a(f"  - 15% (Aspen's 150k) needs P = {SC['15%']['P']:.2f}, near the bottom.")
a("  - This fits David's view: Aspen is optimistic, and 10% is not double the most likely figure.")
a(f"- **Class demand does not depend on the eligibility level once P is calibrated to DBS.** Eligible × P is pinned by DBS volume, so the four cases give the same demand. They differ only in the P they imply and how plausible it is. For eligibility to raise demand, the new class would need a better downstream funnel than DBS, which is outside scope.")
a(f"- **Demand.** If DBS keeps its volume (bound A): {k(C[2029]['one_A'])}k in the launch year (FY2029), {k(C[2032]['one_A'])}k in FY2032, {k(C[2040]['one_A'])}k in FY2040. If the therapy replaces DBS (bound B): {k(C[2029]['one_B'])}k, {k(C[2032]['one_B'])}k and {k(C[2040]['one_B'])}k. At $20k per procedure, FY2040 is ${C[2040]['rev_A']:.0f}M–{C[2040]['rev_B']:.0f}M.")
T=sorted(d['tornado'],key=lambda x:-abs(x['hi']['B2040']-x['lo']['B2040']))
a(f"- **Main drivers (tornado, FY2040)**:")
a(f"  - The DBS volume used for calibration: 3.0k–4.5k gives bound B {k(T[0]['lo']['B2040'])}k–{k(T[0]['hi']['B2040'])}k.")
a(f"  - The yearly draw-down of the backlog after launch: bound B {k(T[1]['lo']['B2040'])}k–{k(T[1]['hi']['B2040'])}k.")
a("  - Eligibility, launch year, age cap, mortality and duration floor each move FY2040 demand by 0.1k or less.\n")
a("## 1. Label and stage definitions\n")
a("**Figure 1. Funnel stages and what feeds each one**\n")
a("| Stage | Definition in this model | Input | Tag |\n|---|---|---|---|")
for r in [("1 Medically eligible","Levodopa-responsive idiopathic PD, ≥4 yrs, motor complications not adequately controlled (recent-onset included), no dementia, fit, age <75","Scenario 5 / 8 / 10 / 15% of PD","A [B1], S3 ★, S8 ★"),
 ("2 Referred / evaluated","Seen at a DBS-capable centre for assessment","Judgment 30–80% (comparison only)","S9 ★"),
 ("3 Willing","Accepts surgery after evaluation","Judgment 40–85%; published 35–43% is consent to referral","A11, A12, A21, S10 ★"),
 ("4 Covered","Payer approves","Judgment 80–95%","S4 ★"),
 ("2×3×4 product P","Lifetime share of eligible patients who are treated","Calibrated: DBS under 75 ÷ eligible inflow, FY2019","C"),
 ("5 Treated","DBS before launch; one-time therapy after launch","Flow model","C")]: a("| "+" | ".join(r)+" |")
a("\n*Source: pd_pool_model.xlsx, Inputs and Scenarios.*\n")
a("- **The label does not require patients to be refractory.** Medtronic's label covers levodopa-responsive PD of at least 4 years that is not adequately controlled, including motor complications of recent onset (4 months to 3 years). It has no age cap [B1]. EARLYSTIM showed benefit in patients with early complications (age ≤60, H&Y <3, complications ≤3 years) [B7].")
a("- **Age and prior DBS.** An upper age of 75 is a practice judgment (★ S3). All four restorative trials in ClearPoint's partner set exclude patients who have had DBS [D1–D4], so DBS recipients leave the pool permanently.")
a("- **What each willingness figure measures.** The 35% [A11] and 43.2% [A12] figures are willingness among patients flagged as candidates, before referral. Of patients who complete a full evaluation, 58.7% go on to implant at one US centre [A21].\n")
a("## 2. Medical eligibility: point prevalence and lifetime fraction\n")
a(f"- **How the pool is built.** US diagnoses (90,000 a year [A1]) are spread by age using Hirsch incidence [A3] on Census 2024 population [A17]. They grow {d['G']*100:.1f}% a year (C1). Each cohort is followed through:")
a("  - survival: SSA 2023 life table [A4] × mortality ratio 1.52 [A5];")
a(f"  - dementia: {pc1(co['hz']['ho'])} a year if diagnosed at 65 or older [A6], {pc1(co['hz']['hy'])} a year if younger [A15];")
a(f"  - motor complications: {pc(co['hz']['h1'])} a year in years 2–5 and {pc(co['hz']['h2'])} a year after [A7, A15];")
a("  - the label's 4-year floor [B1].")
a(f"- **Published screens alone.** Applying levodopa response 80.6% [A9], not adequately controlled 70% (★ S1) and fit 90% (★ S2) gives {pc1(co['share'])} of PD in FY2026. That share sets the age mix of the pool. The eligibility scenario then sets the level: published-screen counts are scaled uniformly by g = scenario ÷ {pc1(co['share'])}.")
a(f"- **Relationship between the two measures.** Point prevalence s ≈ lifetime fraction (LF) × mean years eligible ÷ mean survival from diagnosis. In the cohort, an entrant stays eligible for {co['YE']:.1f} years on average, against {co['YD']:.1f} years of survival after diagnosis. So s ≈ LF × {co['YE']/co['YD']:.2f}. The small gap to the scenario value (row 7 below) comes from incidence growth and age mix (C).")
a("- **Olmsted floor.** In Olmsted County, 16% of incident PD developed fluctuations and 29% of those had DBS. That is about 4.8% ever-DBS [A8], so LF ≥ 4.8%. If ever-DBS = LF × P, then LF = 4.8% ÷ P (row 10).")
a(f"- **What the Olmsted check does and does not show.** The model's ever-DBS share is {pc1(SC['8%']['LF']*SC['8%']['P'])} in every case, close to Olmsted's 4.8%. That supports the DBS calibration, but it cannot tell the eligibility cases apart, because P adjusts to offset eligibility.\n")
a("**Figure 2. Eligibility scenarios and implied downstream product**\n")
a("| Row | Measure | 5% (clinic studies) | 8% (central ★) | 10% (abstract) | 15% (Aspen 150k) |\n|---|---|---|---|---|---|")
rows=[("3","Eligible, point prevalence of US PD",lambda s:pc1(SC[s]['elig'])),("4","Scale on published screens g",lambda s:f"{SC[s]['g']:.2f}×"),
 ("5","Implied P = referral × willing × covered",lambda s:f"{SC[s]['P']:.2f}"),("6","Lifetime fraction of incident PD ever eligible",lambda s:pc1(SC[s]['LF'])),
 ("7","Check: LF × years eligible ÷ survival",lambda s:pc1(SC[s]['LF']*co['YE']/co['YD'])),("8","Eligible stock, FY2026 ('000)",lambda s:k(SC[s]['met']['cand26'])),
 ("9","Newly eligible a year, FY2026 ('000)",lambda s:k(SC[s]['met']['N26'])),("10","Olmsted-implied LF = 4.8% ÷ P",lambda s:pc1(0.048/SC[s]['P'])),
 ("11","P with DBS target 3.4k / 4.0k / 4.5k",lambda s:" / ".join(f"{SC[s]['dbs_tests'][t]:.2f}" for t in ('3400','3990','4500'))),
 ("13","DBS volume implied at judgment P = 0.30 ('000)",lambda s:k(rwc*SC[s]['g']*{r['t']:r for r in co['rows']}[2019]['N'])),
 ("14","Plausibility of P",lambda s:{'5%':'top of range','8%':'central','10%':'plausible','15%':'bottom of range'}[s])]
for rn,lbl,f in rows: a(f"| {rn} | {lbl} | "+" | ".join(f(s) for s in NM)+" |")
a("\n*Source: pd_pool_model.xlsx, Scenarios rows 3–14 (row 11 from pd_pool_model.py, dbs_tests; target 4.0k = all 3,990 treated as under 75). Plausible range for P: 0.10–0.65, central 0.30 (★; referral 30–80%, willing 40–85%, covered 80–95%).*\n")
a("- **Why 8% is central (★).**")
a(f"  - It is the only case where the calibrated P ({SC['8%']['P']:.2f}) matches a stage-by-stage judgment ({rwc:.2f}).")
a("  - It lies between the measured clinic studies (Morgante 4.5% flexible, D-DATS 6.6% for any device therapy [B10]) and the 10–15% figures.")
a("  - The 10–15% figures are a survey abstract [A16] and Aspen's unsourced company belief [D5].")
a("- **The 5% case is possible but demanding.**")
a("  - It needs about 80% referral × 65% willing × 92% covered.")
a("  - Aspen itself says only 10–15% of eligible patients are referred [D5]. That claim is unsourced, but it points the other way.")
a("- **The 15% case needs P = 0.16.** That is consistent with poor referral (for example 30% × 60% × 90%), but it sits uneasily with Olmsted's finding that DBS was planned for 78% of untreated early-onset patients with fluctuations [A8].")
a("- **Testing a higher DBS target** (4.5k, for outpatient implants) raises every P by about a third. The central case would then imply P = 0.40, still plausible.\n")
a("![Funnel](pd_pool_funnel_chart.png)\n")
a("**Figure 3. Central 8% case by age band, FY2026 ('000)**\n")
a("| Age band | PD prevalent | Alive, no dementia, ≥4 yrs | + motor complications | Eligible (central) | Eligible % of band PD | In funnel (× P) |\n|---|---|---|---|---|---|---|")
b26=co['snaps']['2026']['bands']; g8=SC['8%']['g']; P8=SC['8%']['P']
for b in ['<50','50–59','60–64','65–69','70–74','75–79','80+']:
    x=b26[b]; a(f"| {b} | {k(x['PD'])} | {k(x['nodem'])} | {k(x['mc'])} | {k(x['cand']*g8)} | {pc1(x['cand']*g8/x['PD'])} | {k(x['cand']*g8*P8)} |")
tot=lambda f:sum(x[f] for x in b26.values())
a(f"| **Total** | **{k(tot('PD'))}** | **{k(tot('nodem'))}** | **{k(tot('mc'))}** | **{k(tot('cand')*g8)}** | **{pc1(tot('cand')*g8/tot('PD'))}** | **{k(tot('cand')*g8*P8)}** |")
a(f"\n*Source: pd_pool_model.xlsx, 'Age-band funnel' rows 3–{m['FT']}. 'In funnel' is the stock equivalent and is shown for scale only; the flow model applies P to inflow.*\n")
a("## 3. Calibration and checks\n")
a("**Figure 4. Checks**\n")
a("| Check | Published | Model | Result |\n|---|---|---|---|")
R=C
a(f"| US PD prevalent 2020 ('000) | 930.0 minimum [A19] | {k(R[2020]['PD'])} | model 15% low |")
a(f"| US PD prevalent 2030 ('000) | 1,238.0 [A19] | {k(R[2030]['PD'])} | model 17% low |")
a(f"| DBS under 75, FY2019 ('000) | {k(du)} [A10, S5] | {k(R[2019]['dbs_A'])} | matched by construction |")
a(f"| Ever-DBS share of incident PD | 4.8% all ages [A8] | {pc1(SC['8%']['LF']*SC['8%']['P'])} under 75 | consistent |")
a(f"| Bound B, kf = 100%, FY2045 vs funnel inflow ('000) | identity | {k(K1[2045]['one_B'])} vs {k(K1[2045]['fN'])} | equal |")
a(f"| xlsx flows vs Python, FY2001–45, all cases | — | max relative difference below 1e-12 | pass |")
a("\n*Source: pd_pool_model.xlsx, Checks and Summary; LibreOffice recalculation compared with pd_pool_model.json.*\n")
a("**What the 3,990 covers [A10].** It is weighted NIS discharges in 2019 with a PD diagnosis and a DBS procedure code. That has three consequences:")
a("- **Inpatient only.** Outpatient implants are missed, so true volume is likely higher.")
a("- **All ages.** S5 assumes 85% are under 75; this is unverified.")
a("- **May not be one patient per discharge.** Staged second-side procedures could be counted twice.")
a("The calibration is therefore tested from 3.0k to 4.5k (Figure 2 row 11, Figure 7). The PD prevalence gap against Marras is inherited from the incidence inputs. Marras calls its own figures minimums.\n")
a("## 4. Yearly flow, FY2026–2045\n")
a(f"- **Pool.** Pool(t) = pool(t−1) × (1 − μ) + newly eligible × P − treated. The exit rate μ (death, dementia, ageing past 75) is about {pc(C[2030]['mu'])} a year.")
a(f"- **Before launch.** DBS treats min(3.4k, pool) each year. Calibrating to FY2019 means DBS absorbs the whole funnel up to 2019. Inflow then grows {d['G']*100:.1f}% a year while DBS is held flat, so a backlog of willing, covered patients builds, reaching {k(C[2028]['W_A'])}k by FY2028.")
a(f"- **After launch (FY{p['launch']}, ★ S7).**")
a(f"  - **Bound A**: DBS keeps its volume, and the one-time therapy treats {pc(p['kf'])} of the remaining pool each year (★ S6).")
a("  - **Bound B**: the one-time therapy takes over DBS's volume and also draws down the backlog at the same rate. B minus A therefore equals the DBS volume.")
a("  - **Tornado anomaly, fixed and explained.** Bound B now moves with DBS volume only because P is calibrated to that volume: more DBS implies a larger funnel. It no longer moves for any other reason.\n")
a("**Figure 5. Class demand, central 8% case ('000 patients; revenue $M at $20k)**\n")
a("| FY | Newly eligible | Funnel inflow (× P) | Deaths | Dementia | Aged past 75 | Pool available | A: DBS | A: one-time | A: $M | B: one-time | B: $M | Backlog end, B |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for y in [2026,2027,2028,2029,2030,2031,2032,2034,2035,2036,2038,2040,2042,2045]:
    r=C[y]; a(f"| {y} | {k(r['N'])} | {k(r['fN'])} | {k(r['death'])} | {k(r['dem'])} | {k(r['age'])} | {k(r['Wa_B'])} | {k(r['dbs_A'])} | {k(r['one_A'])} | {r['rev_A']:.1f} | {k(r['one_B'])} | {r['rev_B']:.1f} | {k(r['W_B'])} |")
a(f"\n*Source: pd_pool_model.xlsx, 'Flow 8%' rows {FR['8%']['2026']}–{FR['8%']['2045']} (columns C, H, E–G, N, J, K, M, P, R, Q). Exits are before treatment.*\n")
a("**Figure 6. Class demand by eligibility case ('000 patients; $M at $20k)**\n")
a("| Case | Implied P | Eligible FY2026 | Newly eligible FY2026 | Bound | FY2029 | FY2030 | FY2032 | FY2035 | FY2040 | FY2045 | $M FY2040 |\n|---|---|---|---|---|---|---|---|---|---|---|---|")
for s in NM:
    mt=SC[s]['met']
    for bd in 'AB': a(f"| {s} | {SC[s]['P']:.2f} | {k(mt['cand26'])} | {k(mt['N26'])} | {bd} | "+" | ".join(k(mt[f'{bd}{y}']) for y in (2029,2030,2032,2035,2040,2045))+f" | {mt[f'{bd}2040']*0.02:.1f} |")
a("\n*Source: pd_pool_model.xlsx, Summary rows 3–18 and Scenarios rows 5, 8, 9. Demand is identical across cases because P offsets eligibility.*\n")
a("![Demand](pd_pool_demand_chart.png)\n")
a(f"**Convergence.** When yearly uptake is 100% (kf = 1, the rerun), bound B equals the funnel inflow every year after launch: {k(K1[2045]['one_B'])}k against {k(K1[2045]['fN'])}k in FY2045. Bound A equals the inflow minus DBS, {k(K1[2045]['one_A'])}k. At the base kf of 50%, bound B in FY2045 is {k(C[2045]['one_B'])}k, or {pc(C[2045]['one_B']/C[2045]['fN'])} of inflow. The gap is patients who leave the pool before they are treated.\n")
a("## 5. Sensitivity\n")
a("**Figure 7. One-at-a-time sensitivity, central case: FY2040 one-time demand ('000)**\n")
a("| Input (first / second value) | Bound A | Bound B | Implied P |\n|---|---|---|---|")
a(f"| Base | {k(tb['A2040'])} | {k(tb['B2040'])} | {tb['P']:.2f} |")
for x in T: a(f"| {x['label']} | {k(x['lo']['A2040'])} / {k(x['hi']['A2040'])} | {k(x['lo']['B2040'])} / {k(x['hi']['B2040'])} | {x['lo']['P']:.2f} / {x['hi']['P']:.2f} |")
a("\n*Source: pd_pool_model.xlsx, Sensitivity. The age cap, mortality and duration floor are rerun through the cohort with the 8% eligibility level held fixed.*\n")
a("![Tornado](pd_pool_tornado.png)\n")
a("## 6. Judgment inputs (★)\n")
for s in ["S8 Eligibility, point prevalence: 8% central; scenarios 5%, 10%, 15%.","S1 / S2 Not adequately controlled 70% and medically fit 90%. These shape the age mix only; the level comes from S8.",
 "S3 Age cap 75 (the label has none; tested 70–80).","S5 Share of DBS patients under 75: 85% (tested via a 3.0k–4.5k target).","S6 Backlog draw-down after launch: 50% a year (25–100%).","S7 Launch FY2029 (tested FY2028–31).",
 f"S9–S11 and S4 Referral {pc(p['r'])} (30–80%), willing {pc(p['w'])} (40–85%), covered {pc(p['c'])} (80–95%). Used only to judge whether the calibrated P is plausible.",
 "The uniform scale g assumes that higher eligibility has the same age and duration mix as the published-screen pool."]: a(f"- {s}")
a("\n## 7. Why DBS-style eligibility understates a disease-modifying therapy's pool (qualitative; excluded from numbers)\n")
a("- **Which patients qualify.** DBS treats symptoms, so it is offered late, once complications are no longer adequately controlled; for many it is a last resort. A therapy that slowed or reversed degeneration would make most sense early, before motor complications, which the label-style pool here excludes.")
a("- **How willing they are.** The risk–benefit trade-off differs. Patients and neurologists may accept surgery earlier for a durable or disease-modifying benefit, so the 35–43% willingness to accept DBS would not carry over.")
a("- **Why it is excluded.** None of the four partner therapies has shown disease modification, and exPDite-2 and REGENERATE-PD enrol patients with established motor fluctuations [D1, D2]. Any such upside belongs to a separate scenario with its own evidence.\n")
a("## 8. Not verified or open\n")
a("- No population-based study applies the label or EARLYSTIM criteria, so all four eligibility levels rest on clinic studies, surveys or company statements.")
a("- The Olmsted figures (16%, 29%, 78%) come from an AAN abstract. 4.8% is our product of the two published figures (C).")
a("- The share of DBS patients under 75, the outpatient share of implants, and double counting of staged procedures in the NIS are all unverified.")
a("- Referral, willingness and coverage are separate judgments. Published figures map to them only loosely: PARADISE (device therapy 'not considered' for 26.6%), Aspen's unsourced 10–15% referral figure, and 58.7% implanted after evaluation [B10, D5, A21].")
a("- DBS volume is held flat at the 2019 level throughout. Before 2019 the model's DBS is capped by the funnel, so it is lower than 3.4k.")
a("- Dementia and motor complications are assumed independent within each age × duration cell. Modelled PD prevalence runs 15–17% below Marras.\n")
a("## Sources\n")
for s in ["D1 exPDite-2, NCT06944522: https://clinicaltrials.gov/study/NCT06944522","D2 REGENERATE-PD, NCT06285643: https://clinicaltrials.gov/study/NCT06285643",
 "D3 ASPIRO, NCT06344026: https://clinicaltrials.gov/study/NCT06344026","D4 REPLACE, NCT07106021: https://clinicaltrials.gov/study/NCT07106021",
 "D5 Aspen Neuroscience S-1, Oct 2026: https://www.sec.gov/Archives/edgar/data/2124080/000119312526419104/na-20261009.htm",
 "B1 FDA P960009/S478 (Medtronic DBS indication), Feb 2025: https://www.accessdata.fda.gov/cdrh_docs/pdf/P960009S478B.pdf",
 "B7 Schüpbach et al., EARLYSTIM, NEJM 2013: https://www.nejm.org/doi/full/10.1056/NEJMoa1205158",
 "B10 Moes et al. 2023 review (Morgante, D-DATS, PARADISE, Malaty): https://pmc.ncbi.nlm.nih.gov/articles/PMC10645650/",
 "A1 Parkinson's Foundation statistics: https://www.parkinson.org/understanding-parkinsons/statistics/prevalence-incidence",
 "A3 Hirsch et al., Neuroepidemiology 2016: https://doi.org/10.1159/000445751","A4 SSA Period Life Table 2023: https://www.ssa.gov/oact/STATS/table4c6.html",
 "A5 Macleod et al., Mov Disord 2014: https://doi.org/10.1002/mds.25898","A6 Williams-Gray et al., JNNP 2013: https://doi.org/10.1136/jnnp-2013-305277",
 "A8 Stang et al., Rochester Epidemiology Project, Neurology 2021 suppl (abstract): https://doi.org/10.1212/WNL.96.15_supplement.4377",
 "A9 Rizzo et al., Neurology 2016: https://doi.org/10.1212/WNL.0000000000002350","A10 Venkatraman et al., J Neurosurg 2024 (NIS): https://pmc.ncbi.nlm.nih.gov/articles/PMC10898494/",
 "A11 DBS, developing world's perspective, MDCP 2023 (35%): https://pmc.ncbi.nlm.nih.gov/articles/PMC10715347/","A12 Dinkelbach et al., BMC Neurology 2017 (43.2%): https://doi.org/10.1186/s12883-017-0820-7",
 "A15 Hely et al., Mov Disord 2005: https://doi.org/10.1002/mds.20324","A16 GMS 2012 abstract (10–15%): https://doi.org/10.3205/12dgnc047",
 "A17 US Census Vintage 2024: https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/national/asrh/nc-est2024-agesex-res.csv",
 "A19 Marras et al., npj Parkinson's Disease 2018: https://doi.org/10.1038/s41531-018-0058-0","A21 Multidisciplinary DBS screening, MDCP 2018 (58.7%): https://pmc.ncbi.nlm.nih.gov/articles/PMC6183455/",
 "A7 Ahlskog & Muenter, Mov Disord 2001 (motor fluctuations): https://doi.org/10.1002/mds.1090",
 "P $20k per procedure: instruction from David May."]: a(f"- **{s.split(' ',1)[0]}** {s.split(' ',1)[1]}")
open('pd_pool_report.md','w').write("\n".join(L)+"\n")
