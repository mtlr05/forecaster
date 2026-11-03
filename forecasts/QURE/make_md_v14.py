"""Write forecast.md and append the rev5 / v12 entry to revision_log.md (QURE, /workspace/out/QURE_run_v14)."""
import json, sys, os
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B + '/build')
import tables as T
H = T.H; F, D, I, Y = T.F, T.D, T.I, T.Y
D11 = json.load(open('/workspace/out/QURE_run_v13/diag.json'))
R = json.load(open(f'{H}/valuation_result_v14.json'))['scenarios']; R11 = json.load(open('/workspace/out/QURE_run_v13/valuation_result_v13.json'))['scenarios']
BL = {b: json.load(open(f'/workspace/out/QURE_run_v14_band_{b}/valuation_result_v14.json'))['scenarios'] for b in ('lower','upper')}
CONFY = dict(zip(['FY27E','FY28E','FY29E','FY30E','FY31E'], [30, 45, 32, 17, 5]))
Q = json.load(open(f'{H}/valuation_request_v14.json')); SHA = json.load(open(f'{H}/valuation_request_v14.sha256.json'))
cv = lambda r, *p: (lambda d: [d := d[k] for k in p][-1])(r['case'])['value']
CY = ['FY27E', 'FY28E', 'FY29E', 'FY30E', 'FY31E']
i = lambda k: f"[{I[k]}]"
C0 = 865.222; RAN = {k: cv(R[k],'baseline','cash') - C0 for k in R}; RAO = {k: cv(R11[k],'baseline','cash') - 80.24 for k in R}; BLR = {b: BL[b]['bear']['case']['baseline']['cash']['value'] - C0 for b in BL}
bo = '| Bear cash opex (US$M) | ' + ' | '.join(Y[1:]) + ' |\n|---|' + '---|' * (len(Y) - 1) + '\n'
bo += '| Restructured opex [S] | ' + ' | '.join(f"{D['bear']['opex'][y] - CONFY.get(y, 0):,.0f}" for y in Y[1:]) + ' |\n'
bo += f"| Confirmatory study {i('CONFR')} | " + ' | '.join(f"{CONFY.get(y, 0):,.0f}" for y in Y[1:]) + ' |\n'
bo += '| Total | ' + ' | '.join(f"{D['bear']['opex'][y]:,.0f}" for y in Y[1:]) + ' |'
md = f"""# QURE (uniQure) forecast, v14 (rev7) as of 2026-11-02

## Status and open items

- Version **v14 / rev7**, built on v13 / rev6 (kept intact in /workspace/out/QURE_run_v13/). Uncommitted. Rebuild: `python3 build_forecast.py`, `python3 build_request_v14.py`, `python3 run/run_finagle_v14.py`, `python3 run/write_v14.py`, `python3 run/replay_v14.py`, `python3 make_md_v14.py`, `python3 report_build_v14/make_report_v14.py`, then copy report_v14.md to report.md and `python3 report_build_v14/render_report.py`. Bands: same pipeline in /workspace/out/QURE_run_v14_band_lower and _band_upper with env CONF_BAND=lower/upper.
- Driver, David May 2026-11-02 (t124u): "Check the Aspen s-1 for more data. They will run a trial similar in size to AskBio and BlueRock. So this gives another data point. Bull, Base and Bear can use the same cost but include a detailed section in the report explaining analysis and upper and lower cost bands. Make it self contained and use prose to explain."
- Confirmatory-study cost: one separate opex line in bear, base and bull, US$M FY27E-FY31E 30/45/32/17/5 (total 129) {i('CONFR')} = gross study cost 40/55/42/27/15 less ~$10M/yr already in the Q2 2026 run rate [S]. Bands: lower 15/25/16/7/0 (63), upper 50/75/55/30/12 (222). Analysis: /workspace/out/QURE_trial_cost/ (research.md, numbers.csv, report_section.md) and report Section 10. Was $70M/yr flat ($350M, unsourced) in all cases.
- Year-0 (David t129u, 2026-11-02: "Year-0 should be 2025 cash+short term. And then adjust for any equity raises during the 2026 year. Then increase sharecount from 2025 to account for the equity raises."): cash = 80.240 + 542.301 (10-K 12/31/2025) + 242.681 (June 2026 offering net) = 865.222; shares = 62.529408 + 5.686813 = 68.216221. Employee option/ESPP cash ($6.985M) and ~1.15M plan shares excluded [S]. Hercules debt 49.699; HemB royalty liability not debt.
- Extra year-0 raises (only to keep cash >= 0, $50M steps at $25.30): base ${RAN['base']:,.0f}M, bull ${RAN['bull']:,.0f}M, bear ${RAN['bear']:,.0f}M; band runs bear lower ${BLR['lower']:,.0f}M, upper ${BLR['upper']:,.0f}M.
- Value per share central / lower / upper: base {R['base']['value_per_share']:.2f} / {BL['lower']['base']['value_per_share']:.2f} / {BL['upper']['base']['value_per_share']:.2f}; bull {R['bull']['value_per_share']:.2f} / {BL['lower']['bull']['value_per_share']:.2f} / {BL['upper']['bull']['value_per_share']:.2f}; bear {R['bear']['value_per_share']:.2f} / {BL['lower']['bear']['value_per_share']:.2f} / {BL['upper']['bear']['value_per_share']:.2f}.
- Valuation request /workspace/out/QURE_run_v14/valuation_request_v14.json (whole_request sha256 {SHA['whole_request']}). Market data pinned to the 2026-10-30 fetch (price $25.30, rf 4.989%, re 10.489%).
- Open: Q3 2026 results 2026-11-04 may narrow the cost range; AdCom date; FY27E not scaled to consensus.

## base

{T.scen_table('base')}

{T.fin_line('base')}.

## bull

{T.scen_table('bull')}

{T.fin_line('bull')}.

## bear

{T.scen_table('bear')}

{T.fin_line('bear')}.

{bo}

## Sensitivities

{T.sens_table()}
"""
open(f'{H}/forecast.md', 'w').write(md)
rows = []
for k in ('base','bull','bear'):
    rows.append(f"| Year-0 cash ({k}) | FY25A | {cv(R11[k],'baseline','cash'):,.3f} | {cv(R[k],'baseline','cash'):,.3f} | {cv(R[k],'baseline','cash')-cv(R11[k],'baseline','cash'):+,.3f} | 10-K cash + current investments + June 2026 offering net 865.222, + extra raise {RAN[k]:,.0f} [P t129u] |")
    rows.append(f"| Shares ({k}, M) | FY25A | {cv(R11[k],'market','shares'):.6f} | {cv(R[k],'market','shares'):.6f} | {cv(R[k],'market','shares')-cv(R11[k],'market','shares'):+.6f} | 62.529408 + 5.686813 offering + extra raise / 25.30 |")
    rows.append(f"| Extra year-0 raise ({k}) [S] | FY25A | {RAO[k]:,.0f} | {RAN[k]:,.0f} | {RAN[k]-RAO[k]:+,.0f} | only to keep cash >= 0 |")
    rows.append(f"| Minimum year-end cash ({k}) | - | {R11[k]['checks']['min_cash']:,.2f} | {R[k]['checks']['min_cash']:,.2f} | {R[k]['checks']['min_cash']-R11[k]['checks']['min_cash']:+,.2f} | Finagle |")
Yb = R['base']['years']; Yo = R11['base']['years']
for j in (1, 2, 3):
    rows.append(f"| FCF (base, Finagle) | FY{Yb[j]['date'][:4]}E | {Yo[j]['fcf']:,.1f} | {Yb[j]['fcf']:,.1f} | {Yb[j]['fcf']-Yo[j]['fcf']:+,.1f} | Finagle |")
for s_ in ('base', 'bull', 'bear'):
    rows.append(f"| Value per share ({s_}, US$) | - | {R11[s_]['value_per_share']:.4f} | {R[s_]['value_per_share']:.4f} | {R[s_]['value_per_share']-R11[s_]['value_per_share']:+.4f} | Finagle FCFE (= DDM) |")
log = open(f'{H}/revision_log.md').read().rstrip('\n')
if '## rev7 / v14' not in log:
    open(f'{H}/revision_log.md', 'w').write(log + f"""

## rev7 / v14, 2026-11-02

P-tag item: David May t129u, 2026-11-02: "Year-0 should be 2025 cash+short term. And then adjust for any equity raises during the 2026 year. Then increase sharecount from 2025 to account for the equity raises." Forecast (revenue, EBITDA, confirmatory line) unchanged; only year-0 cash, shares and the extra raises changed.

| Line | Period | Old (v13) | New (v14) | Change | Why |
|---|---|---|---|---|---|
""" + '\n'.join(rows) + '\n')
print('ok')
