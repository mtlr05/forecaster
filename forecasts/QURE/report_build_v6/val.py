"""Valuation section for report_v6: every number read from Finagle v6 (and v4 for comparison) files."""
import json
R = json.load(open('/workspace/out/QURE_run/valuation_result_v6.json'))
R4 = json.load(open('/workspace/out/QURE_run/valuation_result_v4.json'))
Q = json.load(open('/workspace/out/QURE_run/valuation_request_v6.json'))
S, S4 = R['scenarios'], R4['scenarios']; fx = R['fetched']; y0 = fx['year0']
SC = ('base', 'bull', 'bear')
def n(v, d=1):
    if v is None: return 'n/a'
    return f'{v:,.0f}' if abs(v) >= 100 else f'{v:,.{d}f}'
pct = lambda v: f'{v*100:.2f}%'
ps = lambda v: (f'-${-v:,.2f}' if v < 0 else f'${v:,.2f}')
col = lambda sc, k: list(S[sc]['per_year_from_notebook_replay']['cols'][k])
YRS = lambda sc: [f"FY{y['date'][:4]}{'A' if y['year']==0 else 'E'}" for y in S[sc]['years']]
def rows(sc, keys):
    ys = YRS(sc); t = ['| Row (US$M unless stated) | ' + ' | '.join(ys) + ' |', '|---|' + '---|' * len(ys)]
    for lab, k, src in keys:
        vals = [y.get(k) for y in S[sc]['years']] if src == 'y' else col(sc, k)[:len(ys)]
        f = ps if k == 'value_per_share' else (lambda v: f'{v*100:.1f}%') if k == 'wacc' else n
        t.append(f'| {lab} | ' + ' | '.join(f(v) if v is not None else 'n/a' for v in vals) + ' |')
    return '\n'.join(t)
FULL = [('Revenue', 'revenue', 'y'), ('EBITDA', 'ebitda', 'y'), ('SBC*', 'sbc', 'r'), ('D&A (derived)*', 'da', 'r'), ('Capex', 'capex', 'r'), ('Pre-tax income*', 'income_pretax', 'r'),
        ('NOL balance*', 'nol', 'r'), ('Cash taxes*', 'tax', 'r'), ('Debt', 'debt', 'r'), ('Cash', 'cash', 'r'), ('FCFE', 'fcfe', 'y'), ('Value per share (US$)*', 'value_per_share', 'r')]
KEY = [('Revenue', 'revenue', 'y'), ('EBITDA', 'ebitda', 'y'), ('D&A (derived)*', 'da', 'r'), ('Capex', 'capex', 'r'), ('NOL balance*', 'nol', 'r'), ('Debt', 'debt', 'r'), ('Cash', 'cash', 'r'), ('FCFE', 'fcfe', 'y')]
def fig_cmp():
    t = ['| Item (US$M unless stated) | Base v4 | Base v6 | Bull v4 | Bull v6 | Bear v4 | Bear v6 |', '|---|---|---|---|---|---|---|']
    for lab, k, f in (('Value per share (US$)', 'value_per_share', ps), ('Equity value', 'equity', n), ('Firm value', 'firm', n), ('Terminal-year FCFE', 'fcfet', n), ('Terminal WACC', 'terminal_wacc', pct)):
        t.append(f'| {lab} | ' + ' | '.join(f(X[s][k]) for s in SC for X in (S4, S)) + ' |')
    for lab, k in (('Minimum cash', 'min_cash'), ('Debt peak', 'debt_peak'), ('Max debt / EBITDA (x)', 'max_debt_to_ebitda')):
        t.append(f'| {lab} | ' + ' | '.join(n(X[s]['checks'].get(k), 2) for s in SC for X in (S4, S)) + ' |')
    t.append('| not_a_valuation | ' + ' | '.join(str(X[s]['not_a_valuation']) for s in SC for X in (S4, S)) + ' |')
    t.append('| Change in value per share v4 to v6 (US$) [C502] | | ' + ps(S['base']['value_per_share'] - S4['base']['value_per_share']) + ' | | ' + ps(S['bull']['value_per_share'] - S4['bull']['value_per_share']) + ' | | ' + ps(S['bear']['value_per_share'] - S4['bear']['value_per_share']) + ' |')
    return '\n'.join(t)
def fig_inputs():
    rt = S['base']['case']['rates']; st = lambda sc: S[sc]['steps'][0]['args']
    t = ['| Input | Base | Bull | Bear | Source |', '|---|---|---|---|---|']
    t.append(f"| Cost of equity | {pct(fx['re'])} | same | same | Finagle default: {rt['re']['evidence']} [D40] |")
    t.append(f"| Cost of debt | {pct(rt['rd']['value'])} | same | same | user [P101] |")
    t.append(f"| Tax rate | {pct(rt['t']['value'])} | same | same | Finagle default: {rt['t']['evidence']} [D40] |")
    t.append(f"| Terminal growth | {pct(fx['gt'])} | same | same | **Finagle default: {rt['gt']['evidence']}** Not set by us [D40] |")
    t.append(f"| Terminal ROIC (roict) | {pct(rt['roict']['value'])} | same | same | Finagle default: {rt['roict']['evidence']} [D40] |")
    t.append(f"| Risk-free ({fx['rf_date']}) | {pct(fx['rf'])} | same | same | Finagle fetch [D40] |")
    t.append(f"| Shares (M) | {fx['shares']:.2f} | same | same | 10-K cover [D40] |")
    t.append(f"| Price ({fx['price_date']}) | {ps(fx['price'])} | same | same | Finagle fetch [D40] |")
    t.append(f"| Year-0 debt / cash (US$M) | {y0['debt']} / {y0['cash']} | same | same | 10-K via Finagle; HemB liability not included [D40] |")
    t.append(f"| Year-0 NOL (US$M) | {n(col('base','nol')[0])} | {n(col('bull','nol')[0])} | {n(col('bear','nol')[0])} | request v6, Dutch NOL EUR458.9M, 10-K p.160 [P104][D41] |")
    t.append(f"| me / mc / gsnext | {st('base')['me']*100:.1f}% / {st('base')['mc']*100:.1f}% / {st('base')['gsnext']*100:.2f}% | {st('bull')['me']*100:.1f}% / {st('bull')['mc']*100:.1f}% / {st('bull')['gsnext']*100:.2f}% | {st('bear')['me']*100:.1f}% / {st('bear')['mc']*100:.1f}% / {st('bear')['gsnext']*100:.2f}% | forecast rev3 [D41] |")
    t.append(f"| Debt policy | 1.0x EBITDA from FY2028E | same | hold | user [P103] |")
    return '\n'.join(t)
b, u, x = S['base'], S['bull'], S['bear']
dab, dau = col('base', 'da'), col('bull', 'da'); cxb = col('base', 'capex'); dax, cxx = col('bear', 'da'), col('bear', 'capex')
db, eb = col('base', 'debt'), col('base', 'ebitda'); cb = col('base', 'cash')
ratios = [db[i] / eb[i] for i in range(6, 11)]
nb, nu, nx = col('base', 'nol'), col('bull', 'nol'), col('bear', 'nol')
logw = sorted({l['message'] for l in b['log'] if l.get('level') == 'WARNING'})
VAL = f"""## 8. Valuation – NOT A VALUATION

**Finagle flagged all three scenarios `not_a_valuation: true`. The per-share figures are mechanical outputs of default policies that misfire for this company, not values we stand behind [D40].** Value per share (FCFE, equal to DDM): base {ps(b['value_per_share'])}, bull {ps(u['value_per_share'])}, bear {ps(x['value_per_share'])}, against a price of {ps(fx['price'])} on {fx['price_date']}. No post-Finagle adjustments were made.

Reasons, in Finagle's words:

""" + '\n'.join(f"- **{sc}:** " + '; '.join(S[sc]['not_a_valuation_reason']) + f". Sanity flags: {', '.join(S[sc]['sanity_flags'])}." for sc in SC) + f"""

**Figure 7 – v4 (rev2b) vs v6 (rev3)**

{fig_cmp()}

*Source: Finagle v4 [D42] and v6 [D40] results; difference derived [C502].*

**Why v6 differs from v4.** The forecast moved from rev2b to rev3 (the year-one ~190-patient path): treatments shift later, and peak EBITDA moves from FY2029E to FY2030E. Base and bull values per share rise despite the later volume. v6 also adds the user's SBC, capex and NOL inputs [P104]. The per-scenario drivers are not separated in the files, so we do not attribute the change between them.

**D&A and capex.** Finagle derives D&A, and it is negative in base and bull from FY2026E: base minimum {n(min(dab))} (terminal {n(dab[-1])}), bull minimum {n(min(dau))} (terminal {n(dau[-1])}), against base capex of {n(cxb[1])} to {n(max(cxb))} [D40]. Finagle's log warns: "{logw[0] if logw else 'n/a'}". The cause **appears to be** Finagle's default terminal ROIC of {pct(b['case']['rates']['roict']['value'])} applied against our small capex list. The result files show the default and the warning but not the calculation, so this is not verified. Bear D&A is positive (terminal {n(dax[-1])}) against capex of {n(cxx[-1])}.

**Debt path.** The user asked to hold debt until EBITDA is positive, then target 1x EBITDA [P103]; that is FY2028E in rev3. Base debt is 1.0x EBITDA in FY2028E–FY2030E, peaking at {n(b['checks']['debt_peak'])} in FY2030E. It then falls more slowly than EBITDA, so debt is {min(ratios):.2f}x–{max(ratios):.2f}x EBITDA in FY2031E–FY2035E, while cash stays near {n(cb[6])} [D40]. Bull debt peaks at {n(u['checks']['debt_peak'])} (max {u['checks']['max_debt_to_ebitda']:.2f}x), with cash reaching {n(col('bull','cash')[-1])} by FY2035E. Bear debt is held at {n(col('bear','debt')[0])}. The $473.2M HemB royalty liability is not in debt.

**Cash.** Cash is negative and unfunded in FY2026E–FY2027E in base (minimum {n(b['checks']['min_cash'])}) and bull ({n(u['checks']['min_cash'])}), and in every year in bear (minimum {n(x['checks']['min_cash'])}) [D40]. No equity raise or dilution is modelled.

**NOL.** The opening NOL is {n(nb[0])} (Dutch NOL, 10-K) [P104][D41]. In Finagle the balance grows with losses (base {n(nb[1])} FY2026E, {n(nb[2])} FY2027E). It offsets 100% of pre-tax income, with no Dutch 50% / EUR1M cap, and is almost all used in FY2028E (base {n(nb[3])} left, {n(nb[4])} by FY2029E; bull {n(nu[3])}). Bear never uses it and ends at {n(nx[-1])}. This is more generous than Dutch law; with the cap, part of the shield would move about a year later.

**SBC and capex.** Both lists landed as requested [D41]. SBC is $17.7M until FY2027E, then 5% of sales in base and bull, and flat in bear. It is never negative. Capex is $3.5M in FY2026E–FY2027E, then the larger of $5M or 1.5% of revenue.

**Defaults filled (Finagle's words):** {', '.join(b['defaults_filled'])} [D40].

**Prompt inputs (user):** """ + '; '.join(sorted({f"{p['path']} (\"{p['quote']}\", {p['date']})" for p in Q['prompt_inputs']})) + f""" [P101][P102][P103][P104].

**Figure 8 – Valuation inputs**

{fig_inputs()}

*Source: Finagle v6 result [D40]; request v6 [D41].*

**Figure 9a – Finagle table, base case.** Rows marked * come from Finagle's notebook replay.

{rows('base', FULL[:6])}

*Source: Finagle v6 result [D40].*

**Figure 9b – Finagle table, base case (continued)**

{rows('base', FULL[6:])}

*Source: Finagle v6 result [D40].*

**Figure 10a – Key rows, bull**

{rows('bull', KEY)}

*Source: Finagle v6 result [D40].*

**Figure 10b – Key rows, bear**

{rows('bear', KEY)}

*Source: Finagle v6 result [D40].*

**Not yet decided by the user** (each changes the value):

- **Terminal ROIC / capex–D&A policy.** The default ROIC of {pct(b['case']['rates']['roict']['value'])} gives negative D&A in base and bull.
- **HemB royalty liability ($473.2M) as debt.** Currently excluded; Finagle uses 10-K debt of {y0['debt']}.
- **Debt rule after the backlog clears.** Base debt runs at {min(ratios):.2f}x–{max(ratios):.2f}x EBITDA in FY2031E–FY2035E, not 1x.
- **Funding for negative cash.** All scenarios; bear in every year.
- **Terminal growth.** Finagle's default is {pct(fx['gt'])} versus the forecast's gsnext ({b['steps'][0]['args']['gsnext']*100:.2f}% base, {u['steps'][0]['args']['gsnext']*100:.2f}% bull, {x['steps'][0]['args']['gsnext']*100:.2f}% bear).
- **Tax rate.** Finagle uses {pct(b['case']['rates']['t']['value'])}; the Dutch statutory rate is 25.8% (10-K).

From the request [D41]: """ + '; '.join(u_['item'] for u_ in Q['undecided_by_david']) + f""".

**Market inputs and commit.** Finagle commit `{R['finagle_commit']}`, run {R['run_at']}. Hash check: {R['hash_check']} [D40].
"""
