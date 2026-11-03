"""Write report.md for QURE rev3 (forecast-report structure, no valuation section)."""
import os, sys, re, json, importlib.util
V = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, V); from val import VAL
H = '/workspace/out/QURE_forecast_rev3'; sys.path.insert(0, H); os.chdir(H)
import tables as T
F, D, I, Y = T.F, T.D, T.I, T.Y
spec = importlib.util.spec_from_file_location('qm', f'{H}/model.py'); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
def hit(n):
    c = 0
    for r in M.run(n):
        c += r['treated']
        if c >= 6000: return f"Q{r['q']} {r['y']}"
def clr(n):
    r = [r for r in M.run(n) if r['backlog'] < 1 and r['treated'] > 0][0]; return f"Q{r['q']} {r['y']}"
i = lambda *k: ''.join(f"[{I[x]}]" for x in k)
b, u, x = D['base'], D['bull'], D['bear']
O = T.O
Y1, Y2 = Y[:6], Y[6:]
rv = lambda n, y: SC_tid(n, 'revenue', y)
def SC_tid(n, k, y): return T.tid(T.SC[n]['totals'][k][y])
def summ(n):
    s = T.SC[n]; P = ['FY25A'] + Y
    t = ['| Row (units) | ' + ' | '.join(P[1:8]) + ' |', '|---|' + '---|' * 7]
    pt = s['patients']
    t.append('| US patients treated (patients/yr) | ' + ' | '.join(T.cell(pt['us_treated (patients/yr)'][y], T.pf) for y in Y[:7]) + ' |')
    t.append('| US eligible backlog, year end (patients) | ' + ' | '.join(T.cell(pt['us_backlog_year_end (patients)'][y], T.pf) for y in Y[:7]) + ' |')
    t.append('| Revenue (US$M) | ' + ' | '.join(T.cell(s['totals']['revenue'][y]) for y in Y[:7]) + ' |')
    t.append('| EBITDA (US$M) | ' + ' | '.join(T.cell(s['totals']['ebitda'][y]) for y in Y[:7]) + ' |')
    return '\n'.join(t)
md = f"""# uniQure N.V. (Nasdaq: QURE)

## Company Update: FY2026E–FY2033E Revenue and EBITDA Forecast and Finagle Run (revision 3, valuation v6)

*30 October 2026. US$ millions unless a row states patients or a count. Forecast only: no rating, price target or valuation. Includes a Finagle valuation section, but Finagle flagged every scenario NOT A VALUATION (Section 8); no rating or price target. Forecast: rev3 `forecasts/QURE/forecast.json` (uncommitted); valuation: Finagle v6 run of `valuation_request_v6.json` [D40][D41]. Numbered sources are in Appendix B.*

## 1. Summary

**FORECAST UPDATE**

■ **Year one is no longer limited by center count, per the user {i('P7')}: US treatments follow a 10 / 30 / 60 / 90 patients-a-quarter path, about 190 in the first four quarters after the 1 July 2027 approval {i('Y1_base')}.** That path came from the Matt Kapusta CEO-simulation bot and is an assumption, not a company figure. Base FY2027E revenue falls to ${b['rev']['FY27E']:,.0f}M from ${O['base']['rev']['FY27E']:,.0f}M in revision 2b [{rv('base','FY27E')}], and FY2028E to ${b['rev']['FY28E']:,.0f}M from ${O['base']['rev']['FY28E']:,.0f}M.

■ **Year two bridges from 90 patients a quarter to 30 centers by mid-2029 {i('BR_base')}.** ClearPoint said in August 2026 that 15 centers had qualified and the goal is 20–30 {i('CLP1')}. The user's ~30 centers at 1–2 procedures a week {i('P5')} is therefore reached at the end of year two, not at launch. After that the revision 2b logic applies unchanged.

■ **The ~6,000-patient backlog is cleared in {clr('base')} in base (bull {clr('bull')}), versus Q4 2029 (bull Q4 2029) in revision 2b.** Cumulative US treatments pass 6,000 in {hit('base')}. After that, treatments fall to the yearly refill of {M.refill('base')[1]:,.0f} patients [P3]{i('REF_base')}, and revenue falls to ${b['rev']['FY32E']:,.0f}M in FY2032E [{rv('base','FY32E')}].

■ **EBITDA peaks at ${b['e']['FY30E']:,.0f}M in FY2030E and settles at a {b['me']*100:.0f}% margin [{SC_tid('base','ebitda','FY30E')}][{T.tid(F['finagle']['me'])}].** Opex now includes a $70M-a-year confirmatory study {i('CONFR')} and $80M of US commercial fixed cost. Hemgenix royalties were sold to HemB SPV and are booked as $473.2M of debt {i('RFIN')}.

**Figure 1 – Base case: patients and financials (FY2026E–FY2032E)**

{summ('base')}

*Source: forecast file, base case; patient rows from the capacity model [{I['CAP_base']}][{I['REF_base']}].*

## 2. Business Description and Reporting Lines

uniQure is a gene-therapy company. Almost all of its revenue today is royalties on Hemgenix, the haemophilia B gene therapy licensed to CSL Behring {i('HGP')}. AMT-130 for Huntington's disease (HD) is a one-time AAV5 gene therapy given by MRI-guided neurosurgery, delivered with ClearPoint Neuro's system. Its BLA and a UK MAA were filed on 2 September 2026 {i('MHRA')}. The reported lines are license (royalty), collaboration and contract manufacturing revenue. We add AMT-130 product lines for the US and, in bull only, the UK. Genezen makes AMT-130 and gives it preferential access to its plant {i('GENZ')}.

## 3. Management

CEO Matt Kapusta and Chief Customer & Strategy Officer Kylie O'Keefe set out the launch plan, including ~6,000 "initially treatable" US patients {i('G6K','G6Kb')}. Management gives no capacity number; it says capacity depends on neurosurgeons and OR suites {i('CAPG')}. ClearPoint, the delivery partner, has given center counts {i('CLP1','CLP2')}.

## 4. Key Developments

| Date | Event | Source |
|---|---|---|
| 2025-09-24 | Investor event: ~6,000 initially treatable US patients at launch | {i('G6K')} |
| 2026-07-29 | Q2 2026: confirmatory-study design agreed with FDA; runway into 2030 | {i('CONF','OPX')} |
| 2026-08-10 | ClearPoint: 15 centers qualified, ready for 1–2 procedures a week | {i('CLP1')} |
| 2026-09-02 | BLA submitted; UK MAA filed, priority review requested | {i('MHRA')} |
| 2026-10-28 | ClearPoint: approval possible mid to second half of 2027 | {i('CLP3')} |
| 2026-10-30 | User: ~30 centers at 1–2 procedures a week | {i('P5')} |
| 2026-10-30 | User: centers do not limit year one; use the ~190 path | {i('P7')} |
| 2026-11-04 | Q3 2026 results due | [S402] |

*Source: company filings and calls; user prompts.*

## 5. Business Drivers by Line

**AMT-130 US: capacity.** Treated = min(capacity, backlog + refill). Year one (Q3 2027–Q2 2028) is a fixed path of 10, 30, 60 and 90 patients a quarter; centers do not bind {i('P7','Y1_base')}. Year two (Q3 2028–Q2 2029) rises in a straight line from 90 a quarter to 30 centers × 1.375 procedures a week × 13 weeks = 536 a quarter, with centers going from 15 to 30 {i('BR_base')}. From Q3 2029, centers grow by 3 a quarter while patients are waiting, capped at 70, and throughput rises to 2.0 a week {i('CAP_base')}. The cap does not bind. HDSA has 69 HD centers {i('HDSA')}. ClearPoint targets 35–40 initial centers with 5,000 patients a year of capacity across all its partners {i('CLP2')}. We assume vector supply does not bind through FY2029E.

**Figure 2 – Base capacity ramp by quarter (US)**

{T.ramp_table('base')}

*Source: year one [{I['Y1_base']}] per the user [{I['P7']}]; bridge [{I['BR_base']}]; assumptions [{I['CAP_base']}] anchored on the user [{I['P5']}] and ClearPoint {i('CLP1')}; backlog per [{I['G6K']}][{I['REF_base']}][{I['ATTR']}].*

**Demand.** The backlog starts at 6,000 {i('G6K')}. Each year adds the refill: incidence less a few for eligibility, willingness and coverage [P3]. The untreated backlog loses 10% a year {i('ATTR')}.

**Price and recognition.** Base net price is $2.0M through FY2030E, then 10% lower from FY2031E once US sales have passed $2B a year {i('PR_base')}. Bull is $2.4M, stepping down from FY2028E {i('PR_bull')}. For comparison, list prices are $4.25M for Lenmeldy, $3.95M for Kebilidi, $3.2M for Elevidys and about $3.5M for Hemgenix {i('PRAN')}. We recognise revenue at treatment [S401].

**Costs.** COGS per patient is $0.30M at launch, falling to $0.20M; it is unverified {i('COGS_base')}. No AMT-130 licensor royalty is disclosed {i('REGX')}. Opex is the Q2 2026 run rate {i('OPX')}, plus US commercial fixed cost, per-center cost, and the confirmatory study {i('CONFR')}.

**Hemgenix royalties.** These stay in revenue and EBITDA, growing to ${b['lic']['FY33E']:.1f}M in FY2033E [{T.tid(F['lines'][0]['periods']['FY33E'])}]. The cash goes to HemB SPV until 1.85× the upfront ($693.8M) is repaid by mid-2032, or up to 2.25× through 2038 {i('RFIN')}. For valuation, treat the $473.2M liability as debt.

## 6. Risks

**Year-one path and bridge.** The ~190 year-one path is from a CEO-simulation bot, not uniQure {i('Y1_base')}. The year-two bridge is our assumption {i('BR_base')}. A slower ramp pushes treatments later but does not change the total.

**Refill.** If refill is 30% of incidence, it falls to {0.3*M.refill('base')[0]:,.0f} patients a year, and FY2031E base revenue falls to ${D['sens']['base_kapusta_refill_30pct']['rev']['FY31E']:,.0f}M. This is the key open question (Figure 5).

**Approval timing.** If approval comes in Q4 2027, FY2027E base revenue is ${D['sens']['base_q4_2027_approval']['rev']['FY27E']:,.0f}M and the backlog clears one quarter later (Figure 5).

**Payer budget.** Base US spend peaks near ${b['us']['FY30E']/1000:.1f}B in FY2030E, a single year of backlog clearance. That invites managed access.

**Consensus.** FY2027E base revenue is {1/b['scale27']:.2f}× consensus. It is not scaled; it lands close to consensus anyway [{F['bridge']['base_fy27_consensus_vs_build']['citation']['id']}]. Goldman's reported peak is $2.5B {i('GS')}.

**Figure 5 – Sensitivities (US patients; US$M)**

{T.sens_table()}

## 7. Forecast

Revenue = patients treated × net price. EBITDA = gross profit less cash opex. FY2026E revenue is consensus. Figure 3 shows the base case, with every patient row in patients and every dollar row in US$M.

**Figure 3 – Base, FY2024A–FY2031E**

{T.scen_table('base', Y1)}

**Figure 4 – Base, FY2032E–FY2033E**

{T.scen_table('base', Y2, actuals=False)}

*{T.fin_line('base')}. Totals may not sum due to rounding.*

{VAL}

## Appendix A – Bull and Bear Cases

**Bull.** Year one is 1.5× the base path: 15, 45, 90 and 135 patients a quarter, 285 in total (our assumption) {i('Y1_bull')}. Year two bridges to 30 centers at 1.875 procedures a week (731 a quarter) by Q2 2029 {i('BR_bull')}. After that, bull adds 5 centers a quarter, up to 100, with throughput rising to 2.0 {i('CAP_bull')}. Refill is {M.refill('bull')[1]:,.0f} a year {i('REF_bull')}. The UK launches from Q3 2028 at $1.5M {i('UKID','UKG')}. Cumulative US treatments pass 6,000 by {hit('bull')}, and the backlog clears in {clr('bull')}.

**Figure A1 – Bull, FY2024A–FY2031E**

{T.scen_table('bull', Y1)}

**Figure A2 – Bull, FY2032E–FY2033E**

{T.scen_table('bull', Y2, actuals=False)}

*{T.fin_line('bull')}.*

**Bear.** AMT-130 is not approved. Royalties continue, and opex is cut to $140M.

**Figure A3 – Bear, FY2024A–FY2031E**

{T.scen_table('bear', Y1)}

**Figure A4 – Bear, FY2032E–FY2033E**

{T.scen_table('bear', Y2, actuals=False)}

*{T.fin_line('bear')}.*

## Appendix B – Numbered sources

SOURCES_HERE

## Appendix C – Method

We follow the forecaster method. Reported periods stay as reported. FY2026E is consensus, because there is no guidance. Later years are a quarterly line build: capacity, backlog and refill set patients, and patients × net price set AMT-130 revenue. FY2027E is not scaled to consensus, because the user's capacity instruction overrides it. The user's instructions are tagged P with their dates and override the default method. A CEO-simulation bot's review was used only as a pointer, and every figure is tagged to a document we opened. Tags: A actual or reported, G company statement, E external estimate, C calculation, S assumption, P user instruction, D document.
"""
S = {s['id']: s for s in F['sources']}
extra = {'D40': 'Finagle v6 result: /workspace/out/QURE_run/valuation_result_v6.json, case_{base,bull,bear}_v6.json, QURE_{base,bull,bear}_v6.xlsx (Finagle commit '+json.load(open('/workspace/out/QURE_run/valuation_result_v6.json'))['finagle_commit'][:7]+', run '+json.load(open('/workspace/out/QURE_run/valuation_result_v6.json'))['run_at']+')', 'D41': 'Valuation request v6: /workspace/out/QURE_run/valuation_request_v6.json (sha256 4a61b649...bddab)', 'D42': 'Finagle v4 result: /workspace/out/QURE_run/valuation_result_v4.json (rev2b forecast, request v4)', 'P101': 'David May 2026-10-29: "take rd as 10%"', 'P102': 'David May 2026-10-29: "set the year 0 depreciation and amortization to 3% of revenue and rerun"', 'P103': 'David May 2026-10-29: "rerun and keep debt constant until the year when EBITDA is positive. Then target 1x EBITDA from that year onward."', 'P104': 'David May 2026-10-30 (t60u): "Stock comp is held constant until EBITDA is positive and then is a fixed % of sales. Check if Matt gives more color on capex, otherwise treat as resolved. Keep bear capex the same as base. Figure out the NOL\'s from Matt."', 'C501': 'value per share / price - 1, from D40', 'C502': 'v6 minus v4 value per share, from D40 and D42', 'C401': 'EBITDA margin = EBITDA / revenue, derived from the forecast file', 'S401': 'Revenue recognised at treatment (point in time), usual practice for one-time gene therapies; not a uniQure policy disclosure [S]', 'S402': 'Q3 2026 results date 2026-11-04 (not reopened this revision) [S]'}
used = sorted(set(re.findall(r'\[([A-Z]\d+)\]', md)), key=lambda k: (k[0], int(k[1:])))
lines = ['**Documents**', ''] + [f"- **{s['id']}** {s['text']}. {s.get('url','')}" for s in F['sources'] if s['id'].startswith('D')] + ['', '**Facts cited**', '']
for k in used:
    if k.startswith('D') and k not in extra: continue
    if k in extra and k not in S: lines.append(f"- **{k}** {extra[k]}"); continue
    s = S.get(k)
    if s is None: lines.append(f"- **{k}** MISSING"); continue
    lines.append(f"- **{k}** {s['text']}")
md = md.replace('SOURCES_HERE', '\n'.join(lines))
open('/workspace/out/QURE_run/report_v6.md', 'w').write(md)
print('missing', [l for l in lines if 'MISSING' in l][:10])
