"""Shared table builders for forecast.md and report.md (v11). Every cell carries its tag."""
import json, os
H = '/workspace/out/QURE_run_v14'
B = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(f'{H}/forecast.json')); D = json.load(open(f'{H}/diag.json')); I = json.load(open(f'{H}/ids.json'))
O = json.load(open(f'{B}/diag_v10.json'))
Y = F['explicit_periods']
SC = {'base': F, 'bull': F['scenarios']['bull'], 'bear': F['scenarios']['bear']}
def m(v): return f'{v:,.0f}' if abs(v) >= 100 else f'{v:,.1f}'
def tid(x): return x['citation']['id']
def cell(f, fmt=m): return f"{fmt(f['value'])} [{tid(f)}]"
PROWS = [('us_centers_active_year_end (count)', 'US centers implied by capacity at 2/week (count)'),
         ('us_capacity (patients/yr)', 'US treatment capacity (patients/yr)'),
         ('us_refill_demand (patients/yr)', 'US entrants to eligible pool (patients/yr)'),
         ('us_pool_demand (patients/yr)', 'US pool demand (patients/yr)'),
         ('us_pool_leavers (patients/yr)', 'US untreated pool leavers (patients/yr)'),
         ('us_backlog_year_end (patients)', 'US eligible pool at year end (patients)'),
         ('us_treated (patients/yr)', '**US patients treated (patients/yr)**'),
         ('us_cumulative_treated (patients)', 'US cumulative treated (patients)'),
         ('uk_capacity (patients/yr)', 'UK capacity (patients/yr)'),
         ('uk_treated (patients/yr)', '**UK patients treated (patients/yr)**'),
         ('uk_backlog_year_end (patients)', 'UK eligible backlog at year end (patients)')]
pf = lambda v: f'{v:,.0f}'
def scen_table(n, years=None, actuals=True):
    b = SC[n]; ys = years or Y; P = (['FY24A', 'FY25A'] if actuals else []) + ys
    t = ['| Row (units) | ' + ' | '.join(P) + ' |', '|---|' + '---|' * len(P)]
    if 'patients' in b:
        for k, lab in PROWS:
            if k in b['patients']:
                t.append(f'| {lab} | ' + ' | '.join(('–' if p.endswith('A') else cell(b['patients'][k][p], pf)) for p in P) + ' |')
    L = b['lines']
    names = [('License revenue, Hemgenix royalties (US$M)', 0), ('Collaboration revenue (US$M)', 1), ('Contract manufacturing revenue (US$M)', 2), ('AMT-130 revenue, US (US$M)', 3), ('AMT-130 revenue, UK (US$M)', 4)]
    for lab, i in names:
        t.append(f'| {lab} | ' + ' | '.join(cell(L[i]['periods'][p]) for p in P) + ' |')
    tot = b['totals']
    t.append('| **Total revenue (US$M)** | ' + ' | '.join(cell(tot['revenue'][p]) for p in P) + ' |')
    t.append('| Gross margin (%) | ' + ' | '.join((cell(tot['gross_margin'][p], lambda v: f'{v*100:.1f}%') if p in tot['gross_margin'] else '–') for p in P) + ' |')
    t.append('| **EBITDA (US$M)** | ' + ' | '.join(cell(tot['ebitda'][p]) for p in P) + ' |')
    t.append(f'| EBITDA margin (%, derived from the two rows above) | ' + ' | '.join(f"{tot['ebitda'][p]['value']/tot['revenue'][p]['value']*100:.1f}%" for p in P) + ' |')
    return '\n'.join(t)
def fin_line(n):
    f = SC[n]['finagle']
    return f"me {f['me']['value']*100:.1f}% [{tid(f['me'])}], mc {f['mc']['value']*100:.1f}% [{tid(f['mc'])}], gsnext {f['gsnext']['value']*100:.2f}% [{tid(f['gsnext'])}]"
def oldnew(n):
    ys = [y for y in Y]
    t = ['| ' + n + ' (units) | ' + ' | '.join(ys) + ' |', '|---|' + '---|' * len(ys)]
    op = O[n]['pt']['treated'] if 'pt' in O[n] else {}
    if n != 'bear':
        t.append('| US patients treated, v10 (patients/yr) | ' + ' | '.join(pf(op[y]) if y in op else 'n/a' for y in ys) + ' |')
        t.append('| US patients treated, v11 (patients/yr) | ' + ' | '.join(pf(D[n]['pt']['treated'][y]) for y in ys) + ' |')
    for k, lab in [('rev', 'Revenue'), ('e', 'EBITDA')]:
        t.append(f'| {lab}, v10 (US$M) | ' + ' | '.join(m(O[n][k][y]) if y in O[n][k] else 'n/a' for y in ys) + ' |')
        t.append(f'| {lab}, v11 (US$M) | ' + ' | '.join(m(D[n][k][y]) for y in ys) + ' |')
    return '\n'.join(t)
def ramp_table(n, q=12):
    import importlib.util
    spec = importlib.util.spec_from_file_location('qm', f'{B}/model.py'); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
    R = M.run(n)[:q]
    t = ['| Quarter | Centers active (count) | Procedures per center per week | Utilisation (%) | Capacity (patients/qtr) | Treated (patients/qtr) | Backlog at quarter end (patients) |', '|---|---|---|---|---|---|---|']
    for r in R: t.append(f"| Q{r['q']} {r['y']} | {r['centers']:.0f} | {r['thr']:.3f} | {('n/a' if r['util']==0 else format(r['util']*100,'.0f')+'%')} | {r['cap']:.0f} | {r['treated']:.0f} | {r['backlog']:,.0f} |")
    return '\n'.join(t)
def sens_table():
    S = D['sens']; ys = [y for y in Y if y != 'FY26E']
    t = ['| Case (units) | ' + ' | '.join(ys) + ' |', '|---|' + '---|' * len(ys)]
    for n in ('base', 'bull'):
        for lab, k in (('filed', None), ('approval Q4 2027 (2027-10-01)', n + '_q4_2027_approval'), ('entrants = 30% of incidence', n + '_kapusta_refill_30pct')):
            src = D[n] if k is None else S[k]; tr = D[n]['pt']['treated'] if k is None else S[k]['treated']
            t.append(f'| {n} {lab}: US treated (patients/yr) | ' + ' | '.join(pf(tr[y]) for y in ys) + ' |')
            t.append(f'| {n} {lab}: revenue (US$M) | ' + ' | '.join(m(src['rev'][y]) for y in ys) + ' |')
            t.append(f'| {n} {lab}: EBITDA (US$M) | ' + ' | '.join(m(src['e'][y]) for y in ys) + ' |')
    return '\n'.join(t)
