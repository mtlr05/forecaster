"""report.md for QURE (forecast + Finagle valuation). Forecast numbers from forecast.json/diag.json via tables.py; valuation numbers only from valuation_result_v11.json."""
import os, sys, re, json
H = '/workspace/out/QURE_run_v11'; sys.path.insert(0, H + '/build')
import tables as T
F, D, I, Y = T.F, T.D, T.I, T.Y
SRC = {s['id']: s for s in F['sources']}
i = lambda *k: "".join(f"[{x if x[0]=="P" and x[1:].isdigit() else I.get(x, x)}]" for x in k)
b, u = D['base'], D['bull']
def tg(n, k, y): return T.tid(T.SC[n]['totals'][k][y])
def pt(n, k, y): return T.SC[n]['patients'][k][y]
# ---------- valuation (Finagle numbers only) ----------
R = json.load(open(f'{H}/valuation_result_v11.json'))
S = R['scenarios']; fx = R['fetched']; y0 = fx['year0']; SC = ('base', 'bull', 'bear')
def n(v, d=1):
    if v is None: return 'n/a'
    return f'{v:,.0f}' if abs(v) >= 100 else f'{v:,.{d}f}'
pct = lambda v: f'{v*100:.2f}%'
ps = lambda v: (f'-${-v:,.2f}' if v < 0 else f'${v:,.2f}')
col = lambda sc, k, X=None: list((X or S)[sc]['per_year_from_notebook_replay']['cols'][k])
cv = lambda sc, *p, X=None: (lambda d: [d := d[k] for k in p][-1])((X or S)[sc]['case'])['value']
ys = [f"FY{y['date'][:4]}{'A' if y['year']==0 else 'E'}" for y in S['base']['years']]
def rows(sc, keys):
    t = ['| Row (US$M unless stated) | ' + ' | '.join(ys) + ' |', '|---|' + '---|' * len(ys)]
    for lab, k, src in keys:
        vals = [y.get(k) for y in S[sc]['years']] if src == 'y' else col(sc, k)[:len(ys)]
        f = ps if k == 'value_per_share' else (pct if k == 'wacc' else n)
        t.append(f'| {lab} | ' + ' | '.join(f(v) if v is not None else 'n/a' for v in vals) + ' |')
    return '\n'.join(t)
FULL = [('Revenue', 'revenue', 'y'), ('EBITDA', 'ebitda', 'y'), ('SBC*', 'sbc', 'r'), ('D&A (derived)*', 'da', 'r'), ('Capex', 'capex', 'r'), ('Interest*', 'interest', 'r'), ('Pre-tax income*', 'income_pretax', 'r'),
        ('NOL balance*', 'nol', 'r'), ('NOL used*', 'nol_used', 'r'), ('Tax expense*', 'tax', 'r'), ('Cash taxes*', 'tax_cash', 'r'), ('Debt', 'debt', 'r'), ('Cash', 'cash', 'r'), ('FCFE', 'fcfe', 'y'), ('WACC*', 'wacc', 'r'), ('Value per share (US$)*', 'value_per_share', 'r')]
KEY = [('Revenue', 'revenue', 'y'), ('EBITDA', 'ebitda', 'y'), ('D&A (derived)*', 'da', 'r'), ('Capex', 'capex', 'r'), ('NOL balance*', 'nol', 'r'), ('Cash taxes*', 'tax_cash', 'r'), ('Debt', 'debt', 'r'), ('Cash', 'cash', 'r'), ('FCFE', 'fcfe', 'y')]
def fig_cmp():
    S0 = None
    t = ['| Item (US$M unless stated) | Base | Bull | Bear |', '|---|---|---|---|']
    for lab, k, f in (('Value per share, FCFE (US$)', 'value_per_share', ps), ('Value per share, DDM (US$)', 'value_per_share_DDM', ps), ('Equity value', 'equity', n), ('Firm value', 'firm', n), ('Terminal-year FCFE', 'fcfet', n), ('Terminal WACC', 'terminal_wacc', pct)):
        t.append(f'| {lab} | ' + ' | '.join(f(X[s][k]) for s in SC for X in (S,)) + ' |')
    t.append('| Shares (M) | ' + ' | '.join(f"{cv(s,'market','shares',X=X):.2f}" for s in SC for X in (S,)) + ' |')
    t.append('| Year-0 cash | ' + ' | '.join(n(cv(s,'baseline','cash',X=X)) for s in SC for X in (S,)) + ' |')
    for lab, k in (('Minimum cash', 'min_cash'), ('Debt peak', 'debt_peak'), ('Max debt / EBITDA (x)', 'max_debt_to_ebitda')):
        t.append(f'| {lab} | ' + ' | '.join((f"{X[s]['checks'][k]:.1f}x" if 'max' in k and X[s]['checks'].get(k) is not None else n(X[s]['checks'].get(k), 2)) for s in SC for X in (S,)) + ' |')
    t.append('| Flagged not a valuation | ' + ' | '.join(('yes' if X[s]['not_a_valuation'] else 'no') for s in SC for X in (S,)) + ' |')
    t.append(f"| Value per share vs. price {ps(fx['price'])} [C509] | " + ' | '.join(f"{(S[s]['value_per_share']/fx['price']-1)*100:+,.0f}%" for s in SC) + ' |')
    return '\n'.join(t)
RA = {s: cv(s, 'baseline', 'cash') - y0['cash'] for s in SC}
NS = {s: cv(s, 'market', 'shares') - fx['shares'] for s in SC}
mcap = fx['price'] * fx['shares']
def fig_raise():
    t = ['| Scenario | Equity raise [S] | Price (US$) | New shares (M) [C504] | Total shares (M) | Year-0 cash | Minimum cash |', '|---|---|---|---|---|---|---|']
    for s in SC:
        t.append(f"| {s} | {n(RA[s])} | {fx['price']:.2f} | {NS[s]:.1f} | {cv(s,'market','shares'):.1f} | {n(cv(s,'baseline','cash'))} | {n(S[s]['checks']['min_cash'])} |")
    return '\n'.join(t)
st = lambda sc: S[sc]['steps'][0]['args']
def fig_inputs():
    t = ['| Input | Base | Bull | Bear | Type and source |', '|---|---|---|---|---|']
    t.append(f"| Cost of equity | {pct(cv('base','rates','re'))} | {pct(cv('bull','rates','re'))} | {pct(cv('bear','rates','re'))} | Finagle default (rf {pct(fx['rf'])}, {fx['rf_date']}) [D45] |")
    t.append(f"| Cost of debt | {pct(cv('base','rates','rd'))} | same | same | analyst instruction, 2026-10-29 [P101] |")
    t.append(f"| Tax rate | {pct(cv('base','rates','t'))} | same | same | analyst instruction, Dutch statutory rate, 2026-10-30 [P105] |")
    t.append(f"| Terminal growth | {pct(cv('base','rates','gt'))} | same | same | analyst instruction, 2026-10-30 [P105] (Finagle's own default would be {pct(fx['gt'])}) |")
    t.append(f"| Terminal ROIC | {pct(cv('base','rates','roict'))} | same | same | Finagle default [D45] |")
    t.append(f"| Shares (M) | {cv('base','market','shares'):.1f} | {cv('bull','market','shares'):.1f} | {cv('bear','market','shares'):.1f} | 10-K {fx['shares']:.1f} + raise at price; judgment [S][P105] |")
    t.append(f"| Price ({fx['price_date']}) | {ps(fx['price'])} | same | same | Finagle fetch [D45] |")
    t.append(f"| Year-0 debt | {n(cv('base','baseline','debt'))} | same | same | 10-K; HemB liability not debt [P105] |")
    t.append(f"| Year-0 cash | {n(cv('base','baseline','cash'))} | {n(cv('bull','baseline','cash'))} | {n(cv('bear','baseline','cash'))} | 10-K {n(y0['cash'])} + raise; judgment [S][P105][P109] |")
    t.append(f"| Year-0 NOL | {n(cv('base','baseline','nol'))} | same | same | analyst instruction [P104] |")
    t.append(f"| Starting margin (me) | {st('base')['me']*100:.1f}% | {st('bull')['me']*100:.1f}% | {st('bear')['me']*100:.1f}% | forecast file [D46] |")
    t.append(f"| Incremental margin (mc) | {st('base')['mc']*100:.1f}% | {st('bull')['mc']*100:.1f}% | {st('bear')['mc']*100:.1f}% | forecast file [D46] |")
    t.append(f"| Next-period growth (gsnext) | {st('base')['gsnext']*100:.2f}% | {st('bull')['gsnext']*100:.2f}% | {st('bear')['gsnext']*100:.2f}% | forecast file [D46] |")
    t.append(f"| Terminal WACC | {pct(S['base']['terminal_wacc'])} | {pct(S['bull']['terminal_wacc'])} | {pct(S['bear']['terminal_wacc'])} | Finagle output [D45] |")
    t.append("| Capex | [0.439, 3.5, 3.5], then Finagle method 1 | same | base dollars, all 11 years | analyst instruction [P106][P107] |")
    t.append("| Debt policy | 1.0x EBITDA from FY2027E | same | hold | analyst instruction [P103]; start year follows the forecast |")
    t.append("| SBC | flat 17.7 until EBITDA is positive, then 5% of sales | same | flat 17.7 | analyst rule [P104]; 5% is our judgment [S] |")
    return '\n'.join(t)
B, U, X = S['base'], S['bull'], S['bear']
cxb, cxx, dab, dax = col('base','capex'), col('bear','capex'), col('base','da'), col('bear','da')
cb, cu, cx = col('base','cash'), col('bull','cash'), col('bear','cash')
rvx = col('bear','revenue')
cross = next(ys[k] for k in range(1, 11) if dax[k] > cxx[k] and k >= 3)
imin = lambda v: ys[v.index(min(v))]
def ytab(key):
    t = ['| Scenario | ' + ' | '.join(ys) + ' |', '|---|' + '---|' * len(ys)]
    for sc in SC: t.append(f"| {sc} | " + ' | '.join(n(v) for v in col(sc, key)) + ' |')
    return '\n'.join(t)
warn = '; '.join(f'{sc}: "{w}"' for sc in SC for w in S[sc]['validation']['warnings']) or 'none'
flags = '; '.join(f'{sc}: "{f}"' for sc in SC for f in S[sc]['sanity_flags']) or 'none'
gs = {sc: st(sc)['gsnext'] for sc in SC}
VAL = f"""## 8. Valuation – Finagle

*This section turns the forecast into a value per share. Finagle is an external valuation model: it takes the revenue and EBITDA paths from Sections 1–7, the balance-sheet starting point and a set of rates and rules, and discounts free cash flow to equity (FCFE). All valuation numbers below are copied from Finagle's result file; none are recomputed here.*

**Finagle values QURE at {ps(B['value_per_share'])} a share in base, {ps(U['value_per_share'])} in bull and {ps(X['value_per_share'])} in bear, vs. a price of {ps(fx['price'])} on {fx['price_date']} [D45].** These are raw FCFE values; DDM gives the same figures, and no post-run adjustment was requested, so there is no adjusted value. No scenario is flagged not a valuation. We draw no rating or price target.

- **Validation warnings (Finagle's words):** {warn} [D45]. Base EBITDA growth is high because EBITDA turns from losses to about $4.6B over three years; there are no acquisitions in the forecast.
- **Sanity flags (Finagle's words):** {flags} [D45]. Base and bull have none. Finagle's log is empty in all three scenarios.
- **Analyst-instructed inputs:** rd 10% [P101] (2026-10-29); debt at 1x EBITDA once EBITDA is positive, held in bear [P103] (2026-10-29); NOL {n(cv('base','baseline','nol'))} and the SBC rule [P104] (2026-10-30); year-0 D&A {cv('base','baseline','da')}, HemB liability not debt, terminal growth 2%, Dutch tax rate 25.8%, and cash and shares raised so cash never goes negative [P105] (2026-10-30); base and bull capex [0.439, 3.5, 3.5] then method 1 [P106] (2026-10-30); bear capex equal to base [P107] (2026-10-30); bear raise sized so cash stays positive [P109] (2026-10-30); leave rate m = 0.62 and a valuation run on this forecast [P9][P8] (2026-10-30).
- **Defaults filled (Finagle's words):** {', '.join(B['defaults_filled'])} [D45]. Finagle also prints "forecast.sales_growth NOT IN CATALOG"; the revenue path still applies.
- **Fetched market inputs:** price {ps(fx['price'])} and risk-free rate {pct(fx['rf'])}, both as of {fx['price_date']}; 10-K shares {fx['shares']:.1f}M and cash {n(y0['cash'])} [D45].
- **Finagle commit** `{R['finagle_commit'][:8]}`, run {R['run_at'][:16].replace('T',' ')} (Toronto time). {(R['hash_check'][:1].upper()+R['hash_check'][1:]).replace('v11 ','').replace('prompt_inputs','instruction inputs')} [D45].

**Method.** Finagle discounts free cash flow to equity at the cost of equity ({pct(cv('base','rates','re'))}, Finagle's default). It takes our revenue and EBITDA for FY2026E–FY2033E as given (eight explicit years after FY2025A) and extends them two more years to FY2035E using the starting margin, the incremental margin and next-period growth, fading to terminal growth of 2.00%, then adds a terminal value. Terminal growth of 2% is an analyst instruction, not Finagle's default [P105]. Negative cash flow is funded from the opening cash balance: we sized the year-0 equity raise in each case so cash never goes negative, and Finagle values the raise through the extra cash and shares [D45].

**Figure 7 – Valuation inputs**

*Each row is one input Finagle used, its value in each scenario, and where it came from. "Finagle default" means the model filled it; "analyst instruction" means it was set deliberately; "judgment" means we chose it without a source.*

{fig_inputs()}

*Source: Finagle result [D45]; valuation request [D46]; analyst instructions [P101]–[P109].* **Judgment inputs.** The equity raises are our judgment: base and bull use $400M and $350M, which are more than needed because EBITDA is positive from FY2027E; the bear raise is the amount that keeps bear cash positive with base-sized capex [S]. SBC at 5% of sales applies the analyst's rule with a percentage we chose [S].

**Figure 8 – Value bridge**

*How firm value becomes value per share in each scenario. Read down a column: firm value, less debt plus cash, gives equity value, divided by shares.*

| Item (US$M unless stated) | Base | Bull | Bear |
|---|---|---|---|
| PV of explicit-period cash flows | not returned | not returned | not returned |
| Terminal value and share of total | not returned | not returned | not returned |
| Terminal-year FCFE | {n(B['fcfet'])} | {n(U['fcfet'])} | {n(X['fcfet'])} |
| Firm value | {n(B['firm'])} | {n(U['firm'])} | {n(X['firm'])} |
| Equity value | {n(B['equity'])} | {n(U['equity'])} | {n(X['equity'])} |
| Year-0 debt / cash | {n(cv('base','baseline','debt'))} / {n(cv('base','baseline','cash'))} | {n(cv('bull','baseline','debt'))} / {n(cv('bull','baseline','cash'))} | {n(cv('bear','baseline','debt'))} / {n(cv('bear','baseline','cash'))} |
| Shares (M) | {cv('base','market','shares'):.1f} | {cv('bull','market','shares'):.1f} | {cv('bear','market','shares'):.1f} |
| Value per share (US$) | {ps(B['value_per_share'])} | {ps(U['value_per_share'])} | {ps(X['value_per_share'])} |
| vs. price {ps(fx['price'])} [C509] | {(B['value_per_share']/fx['price']-1)*100:+,.0f}% | {(U['value_per_share']/fx['price']-1)*100:+,.0f}% | {(X['value_per_share']/fx['price']-1)*100:+,.0f}% |

*Source: Finagle result [D45]; upside derived [C509]. The result file does not split value into explicit-period and terminal PV, so those rows are left blank rather than recomputed.* **What this means:** the base and bull values rest on the cash flows from FY2028E onward, when AMT-130 volumes are at or near capacity, so they depend on approval and on the volume path holding (judgment).

**Figure 9a – Finagle valuation table, base case.** *The year-by-year build behind the base value: revenue and EBITDA from the forecast, then the items Finagle derives (D&A, interest, tax, debt, cash) down to FCFE. Rows marked * come from Finagle's notebook replay in the result file.*

*Ticker QURE; price {ps(fx['price'])}; shares {cv('base','market','shares'):.1f}M; cost of equity {pct(cv('base','rates','re'))}; cost of debt {pct(cv('base','rates','rd'))}; tax {pct(cv('base','rates','t'))}; terminal growth {pct(cv('base','rates','gt'))}.*

{rows('base', FULL[:8])}

*Source: Finagle result [D45].*

**Figure 9b – Finagle valuation table, base case (continued)**

{rows('base', FULL[8:])}

*Source: Finagle result [D45]. M&A and working-capital change are zero in every year (no acquisitions; Finagle's default working-capital mode). Debt is exactly 1.0x EBITDA from FY2027E.*

**Figure 10a – Key rows, bull**

*The same build for bull and bear, limited to the rows that move value most.*

{rows('bull', KEY)}

*Source: Finagle result [D45].*

**Figure 10b – Key rows, bear**

{rows('bear', KEY)}

*Source: Finagle result [D45].*

**Cash, debt and tax.** Cash never goes negative. Minimum year-end cash is base {n(B['checks']['min_cash'])} ({imin(cb)}), bull {n(U['checks']['min_cash'])} ({imin(cu)}) and bear {n(X['checks']['min_cash'])}, reached at the end in {imin(cx)} [D45]. No payout is modelled, so base cash builds to {n(cb[-1])} and bull to {n(cu[-1])} by FY2035E. Base and bull debt sit at exactly 1.0x EBITDA from FY2027E. Base debt peaks at {n(B['checks']['debt_peak'])} and bull at {n(U['checks']['debt_peak'])}; bear is held at {n(cv('bear','baseline','debt'))} [D45]. The opening NOL offsets 100% of pre-tax income with no Dutch cap, which is generous: base pays no cash tax through FY2027E, bull uses its NOL in FY2027E, and bear's NOL grows to {n(col('bear','nol')[-1])} [D45].

**Figure 11 – Year-0 equity raise (sizes are our judgment)**

*Finagle funds negative cash flow from opening cash, so each scenario carries an assumed equity raise at the start, priced at the current share price. This table shows the raise, the shares it creates and the lowest cash balance that results.*

{fig_raise()}

*Source: Finagle result [D45]. New shares issued at the fetched price with no discount or fees [S]. The bear raise is about {RA['bear']/mcap:.1f}x the current market cap of {n(mcap)} [C508].*

**Figure 12 – Scenarios vs. price**

*Headline valuation outputs and balance-sheet checks for the three scenarios side by side.*

{fig_cmp()}

*Source: Finagle result [D45]; upside derived [C509].* The spread between scenarios is driven by approval (bear assumes none) and, between base and bull, by price and capacity.

**Caveats.**

- **Bear.** EBITDA is negative in every year, so FCFE is negative after year 1 and equity value is {n(X['equity'])}. The {ps(X['value_per_share'])} rests on perpetual losses and on our assumed {n(RA['bear'])} raise. Bear D&A exceeds capex from {cross} and reaches {n(dax[-1])} vs capex {n(cxx[-1])} and revenue {n(rvx[-1])} in FY2035E, because base-sized capex sits on bear's small revenue. It is positive, so Finagle does not flag it, but it inflates bear's NOL build-up. Read bear as roughly zero.
- **Funding.** The base and bull raises are larger than needed; the bear raise implies heavy dilution ({NS['bear']:.0f}M new shares on {fx['shares']:.1f}M). Fees, discount and timing are not modelled.
- **Cash accumulation.** With no distribution, cash piles up from FY2028E; Finagle values it through FCFE, but the report makes no assumption about its use.
- **Terminal growth vs. gsnext.** Terminal growth is set at 2% by analyst instruction [P105]; the forecast's next-period growth is {gs['base']*100:.2f}% base, {gs['bull']*100:.2f}% bull and {gs['bear']*100:.2f}% bear. The two have not been reconciled.
- **Approval** is not probability-weighted; base and bull assume approval on 1 July 2027.
- **Demand.** The valuation inherits the pool model's m = 0.62, which is shorter-stay than the trial crossover evidence (Section 9 and Appendix D).
"""
# ---------- forecast sections ----------
def summ():
    t = ['| Row (units) | FY25A | ' + ' | '.join(Y[:7]) + ' |', '|---|' + '---|' * 8]
    s = T.SC['base']; tot = s['totals']
    t.append('| US patients treated (patients/yr) | – | ' + ' | '.join(T.cell(s['patients']['us_treated (patients/yr)'][y], T.pf) for y in Y[:7]) + ' |')
    t.append('| Revenue (US$M) | ' + ' | '.join(T.cell(tot['revenue'][y]) for y in ['FY25A'] + Y[:7]) + ' |')
    t.append('| Revenue growth (%, derived) [C401] | – | ' + ' | '.join(f"{(tot['revenue'][y]['value']/tot['revenue'][p]['value']-1)*100:,.1f}%" for p, y in zip(['FY25A'] + Y[:6], Y[:7])) + ' |')
    t.append('| Gross margin (%) | ' + ' | '.join(T.cell(tot['gross_margin'][y], lambda v: f'{v*100:.1f}%') for y in ['FY25A'] + Y[:7]) + ' |')
    t.append('| EBITDA (US$M) | ' + ' | '.join(T.cell(tot['ebitda'][y]) for y in ['FY25A'] + Y[:7]) + ' |')
    t.append('| EBITDA margin (%, derived) [C401] | ' + ' | '.join(f"{tot['ebitda'][y]['value']/tot['revenue'][y]['value']*100:.1f}%" for y in ['FY25A'] + Y[:7]) + ' |')
    return '\n'.join(t)
c27 = F['bridge']['base_fy27_consensus_vs_build']
md = f"""# uniQure N.V. (Nasdaq: QURE)

## Company Update: FY2026E–FY2033E Revenue and EBITDA Forecast and Finagle Valuation

*30 October 2026. US$ millions unless a row states patients or a count. Includes a Finagle valuation (Section 8) but carries no rating or price target. Numbered sources are in Appendix B; the forecast and valuation files are listed there [D45][D46].*

## About this report

**The company.** uniQure N.V. (QURE) is a Netherlands-based gene-therapy company listed on Nasdaq. Today almost all of its revenue is royalties on Hemgenix, a haemophilia B gene therapy licensed to CSL Behring {i('HGP')}. The single material driver of its value is AMT-130, a one-time gene therapy for Huntington's disease (HD), delivered by MRI-guided neurosurgery using ClearPoint Neuro's system. uniQure filed for US approval (a BLA) and UK approval (an MAA) in September 2026 {i('MHRA')}. If AMT-130 is approved, it would dwarf the royalty business; if it is not, uniQure is a small royalty company with a large cost base.

**What the report is.** It is a revenue and EBITDA forecast for FY2026E–FY2033E in three scenarios: **base** (approval on 1 July 2027, our central assumptions), **bull** (approval, faster capacity, higher price and larger demand) and **bear** (no approval). The forecast is then passed to Finagle, an external valuation model, which extends it to FY2035E and computes a value per share for each scenario. The report gives no rating or price target.

**How it was built, step by step.**

1. **History and guidance.** Reported years stay as reported (10-K FY2025 [D1]). FY2026E is analyst consensus, because the company gives no revenue guidance.
2. **Scenario assumptions.** For each scenario we set approval timing, capacity, price, demand and cost assumptions (Appendix A gives bull and bear).
3. **Volumes from an eligible-patient pool.** AMT-130 is a one-time treatment for patients in a narrow, early stage of HD. So patient numbers come from a "pool" of eligible patients: it starts at uniQure's estimate of ~6,000 at launch, is refilled each year by newly diagnosed patients, and is drained by treatment and by patients who progress out of eligibility or die (Appendix D).
4. **Capacity limits.** Each patient needs specialised neurosurgery, so in the early years the number treated is limited by how many procedures centres can do, not by demand. We use a ClearPoint capacity ramp of 330 / 2,500 / 3,000 a year [D32].
5. **Price.** Patients treated × net price per patient gives AMT-130 revenue.
6. **Costs and cash items.** Cost of goods, operating expenses, capex, D&A, stock-based compensation (SBC), debt, cash, tax losses (NOLs) and share count are set by rule or by analyst instruction (Section 8, Figure 7).
7. **Valuation.** Finagle discounts free cash flow to equity (FCFE) at the cost of equity, with 2% terminal growth, to give a value per share.

**How to read the source tags.** Every number carries a tag in square brackets that points to Appendix B. **A** is a reported actual; **G** is a company statement or guidance; **E** is an external estimate (analysts, papers); **D** is a document or data file; **S** is an assumption we made; **C** is a calculation from tagged inputs; **P** is an analyst instruction that sets a modelling choice. An entry marked "unverified" means the page or link was not reopened for this report. "Judgment" in the text marks the analyst's view rather than a sourced fact. In short: A, G, D and E are evidence; S and P are choices; C is arithmetic on the others.

**The assumptions that matter most.**

- **Approval on 1 July 2027 (base and bull)** – judgment, based on the filing date and priority-review timing; not probability-weighted {i('MHRA')}.
- **A launch pool of ~6,000 US patients** – evidence: a company management estimate of patients "addressable" at launch, not a treatment target {i('G6K')}.
- **Leave rate m = 0.62 a year** (an average stay in the eligible window of ~1.6 years) – judgment. It was chosen because it makes disease incidence consistent with the 6,000. The clinical evidence (duration studies and the trial's crossover data) points nearer 0.41 a year, a stay of ~2.4 years {i('XOVER')}[C510].
- **72.9% of eligible patients treated** (90% referred × 90% willing × 90% covered) – assumption {i('HAIR_base')}.
- **Capacity of 330 / 2,500 / 3,000 a year** – a ClearPoint forecast, judgment informed by management comments, not a company figure [D32].
- **Net price of $2.0M per patient** – assumption, below comparable list prices of $3.2M–$4.25M {i('PRAN','PR_base')}.
- **Valuation rules** (2% terminal growth, 1x EBITDA debt, equity raises so cash never goes negative) – analyst instructions and judgment [P103][P105][P109].

## Glossary

| Term | Meaning in this report |
|---|---|
| AMT-130 | uniQure's one-time AAV5 gene therapy for Huntington's disease |
| HD | Huntington's disease, an inherited neurodegenerative disease |
| TFC | Total Functional Capacity, a 0–13 score of daily functioning in HD; the trial enrolled TFC 9–13 |
| Early-manifest | The first symptomatic stage of HD; the pivotal trial defined it by TFC 9–13 [D602]; the treatable window in this report |
| Pool | US patients eligible for AMT-130 and not yet treated, at a point in time |
| Entrants | Patients who join the pool in a period (newly eligible) |
| Treated | Patients who receive AMT-130 in a period |
| Capacity | The maximum number of procedures centres can perform in a period |
| Leave rate m | The share of the pool that leaves each year by progressing out of eligibility or dying |
| P | The share of entrants that is treated (assumed 0.729 when demand, not capacity, limits) |
| u | The treatment rate on the pool: treated divided by the pool |
| g | The pool's growth rate; g\* = 0.5% a year is population growth |
| Consensus | The average of sell-side analyst forecasts |
| EBITDA | Earnings before interest, tax, depreciation and amortisation |
| D&A | Depreciation and amortisation |
| Capex | Capital expenditure |
| SBC | Stock-based compensation |
| NOL | Net operating loss carried forward, used to offset future taxable income |
| FCFE | Free cash flow to equity: cash available to shareholders after costs, tax, capex and debt flows |
| DDM | Dividend discount model; here it gives the same value as FCFE |
| WACC | Weighted average cost of capital; Finagle reports it alongside the cost of equity |
| Terminal growth | The growth rate assumed for cash flows after the last forecast year |
| CAGR | Compound annual growth rate |
| BLA / MAA | US Biologics License Application / UK Marketing Authorisation Application |

## 1. Summary

*The four points below give the forecast and valuation in brief; Figure 1 gives the base-case numbers.*

**FORECAST SUMMARY**

■ **US AMT-130 volumes come from an eligible-pool model at a leave rate of 0.62 a year, starting from uniQure's ~6,000 launch pool, and are capped by a ClearPoint capacity ramp: 330 patients in FY2027E, 2,500 in FY2028E and 3,000 a year from FY2029E {i('P9','CAP_base')}.** Treated patients stay at the 3,000 cap through FY2030E and ease to {pt('base','us_treated (patients/yr)','FY32E')['value']:,.0f} by FY2032E, when demand from the pool, not capacity, becomes the limit [{T.tid(pt('base','us_treated (patients/yr)','FY32E'))}].

■ **Base revenue is ${b['rev']['FY28E']:,.0f}M in FY2028E and about $6.0B in FY2029E–FY2030E [{tg('base','revenue','FY28E')}][{tg('base','revenue','FY30E')}],** and stays above $5B through FY2033E. Net price is $2.0M per patient, 10% lower from FY2031E {i('PR_base')}. This is far above the Street: FY2027E consensus is about one-sixth of our build (consensus divided by build is {c27['value']:.3f}) [{c27['citation']['id']}], and Goldman's reported peak is $2.5B {i('GS')}.

■ **EBITDA turns positive in FY2027E at ${b['e']['FY27E']:,.0f}M and settles near $4.0B, a margin of about {b['me']*100:.0f}% [{tg('base','ebitda','FY27E')}][C43].** Bull reaches ${u['rev']['FY28E']/1000:.1f}B of revenue in FY2028E on 4,500 patients, then runs at a 3,500 cap. Bear assumes no approval: royalties continue and costs are cut.

■ **Finagle values the shares at {ps(B['value_per_share'])} in base, {ps(U['value_per_share'])} in bull and {ps(X['value_per_share'])} in bear, against a price of {ps(fx['price'])} on {fx['price_date']} [D45].** The base value is about {B['value_per_share']/fx['price']:.0f}x the price [C509]. That gap reflects volumes far above consensus and an assumed approval; it should be read with the risks in Section 6 and the sensitivities in Section 9. The key open question is the leave rate: 0.62 a year is shorter-stay than the trial crossover data, which point to about 0.41 {i('XOVER')}.

**Figure 1 – Financial summary, base case**

{summ()}

*Source: forecast file, base case [D46]; growth and margins derived [C401]. FY2026E revenue is consensus.* **What this means:** revenue steps up by more than an order of magnitude in FY2027E–FY2028E as AMT-130 launches, and the EBITDA margin moves from losses to about three-quarters of revenue because a one-time therapy at $2.0M carries low per-patient costs.

## 2. Business Description and Reporting Lines

*What uniQure sells today and how the reported revenue lines map to the forecast.*

uniQure is a gene-therapy company. Almost all of its revenue today is royalties on Hemgenix, the haemophilia B gene therapy licensed to CSL Behring {i('HGP')}. AMT-130 for Huntington's disease (HD) is a one-time AAV5 gene therapy given by MRI-guided neurosurgery with ClearPoint Neuro's system; its BLA and a UK MAA were filed in September 2026 {i('MHRA')}. The reported lines are license (royalty), collaboration and contract manufacturing revenue; we add AMT-130 for the US and, in bull only, the UK. Genezen makes AMT-130 and gives uniQure preferential access to its plant {i('GENZ')}.

**Figure 2 – Revenue by line, FY2025A**

| Line | FY2025A (US$M) | Share of revenue | How uniQure earns |
|---|---|---|---|
| License (Hemgenix royalties) | {T.cell(F['lines'][0]['periods']['FY25A'])} | {F['lines'][0]['periods']['FY25A']['value']/F['totals']['revenue']['FY25A']['value']*100:.0f}% | royalty from CSL Behring |
| Collaboration | {T.cell(F['lines'][1]['periods']['FY25A'])} | {F['lines'][1]['periods']['FY25A']['value']/F['totals']['revenue']['FY25A']['value']*100:.0f}% | services to partners, wound down |
| Contract manufacturing | {T.cell(F['lines'][2]['periods']['FY25A'])} | 0% | divested to Genezen in 2024 {i('GENZ')} |
| **Total** | {T.cell(F['totals']['revenue']['FY25A'])} | 100% | |

*Source: 10-K FY2025 [D1]; shares derived [C401].*

## 3. Management

*Who sets the launch plan and what management has and has not said about capacity.*

CEO Matt Kapusta and Chief Customer & Strategy Officer Kylie O'Keefe set out the launch plan, including about 6,000 "initially treatable" US patients at launch {i('G6K','G6Kb')}. Management gives no capacity number; it says capacity depends on neurosurgeons and operating suites {i('CAPG')}. Its record on commercial launches is thin: Hemgenix was out-licensed, so AMT-130 would be uniQure's first own launch. We do not assess ownership or deal record in this update.

## 4. Key Developments

*The dated events that set the timeline in the forecast.*

**Figure 3 – Key developments**

| Date | Event | Source |
|---|---|---|
| 2025-09-24 | Investor event: ~6,000 initially treatable US patients at launch (management estimate) | {i('G6K')} |
| 2026-07-29 | Q2 2026: confirmatory-study design agreed with FDA; cash runway into 2030 | {i('CONF','OPX')} |
| 2026-08-10 | ClearPoint: 15 centers qualified for 1–2 procedures a week | {i('CLP1')} |
| 2026-09-02 | BLA submitted; UK MAA filed, priority review requested | {i('MHRA')} |
| 2026-10-28 | ClearPoint: approval possible mid to second half of 2027 | {i('CLP3')} |
| 2026-11-04 | Q3 2026 results due | [S402] |

*Source: company filings and calls; ClearPoint statements.*

What matters most is the size and turnover of the treatable pool. uniQure's 6,000 is an estimate of patients addressable at launch, not a target to treat, and the company has not said how quickly patients leave the treatable window {i('G6K','G6Kb')}.

## 5. Business Drivers by Line

*The assumptions behind each revenue and cost line. AMT-130 volume is the driver that matters; the others are small or mechanical.*

**Why a pool model.** AMT-130 is given once, and only to patients in the early stage of HD. A patient who is treated, progresses past the eligible stage or dies does not come back. So the number who can be treated in any year depends on how many eligible patients are waiting, how many newly become eligible, and how fast untreated patients age out. A pool model tracks exactly that. **Why capacity limits the early years.** Each treatment is an MRI-guided neurosurgical procedure at a qualified centre. At launch there are far more eligible patients waiting (~6,000) than centres can treat, so through FY2030E the number treated is set by capacity; only later, once the waiting pool is worked down, does patient demand set the number. **Why m = 0.62 is a judgment call.** At 0.62 a year, incidence alone produces a pool of about 6,000, matching uniQure's estimate with no extra assumption. But the clinical evidence points to patients staying eligible longer, nearer 0.41 a year (Appendix D.6). A slower leave rate would mean a larger pool than 6,000 unless some other eligibility filter applies, and the choice changes long-run demand.

**AMT-130 US: volume.** Treated patients each quarter are the lower of capacity and pool demand {i('CAP_base')}. The pool starts at 6,000 on 1 July 2027 {i('G6K')}. Each year about {pt('base','us_refill_demand (patients/yr)','FY28E')['value']:,.0f} new patients enter it from HD incidence, net of a referral share {i('REF_base')}. Untreated patients leave at 0.62 a year (progression 0.60 plus death 0.02), an average stay of about 1.6 years {i('P9')}. Of eligible patients, 72.9% are treated once demand, not capacity, sets volume: 90% referred, 90% willing and 90% covered, all our assumptions {i('HAIR_base')}. Capacity follows the ClearPoint forecast ramp of 330 / 2,500 / 3,000 a year [D32]{i('CAP_base')}.

**Price and recognition.** Base net price is $2.0M through FY2030E, then 10% lower once US sales pass $2B a year {i('PR_base')}. Bull is $2.4M, stepping down from FY2028E {i('PR_bull')}. List prices for comparable gene therapies run $3.2M–$4.25M {i('PRAN')}. We recognise revenue at treatment [S401].

**Costs.** COGS per patient is $0.30M at launch, falling to $0.20M; it is unverified {i('COGS_base')}. Opex is the Q2 2026 run rate {i('OPX')} plus US commercial fixed cost, $1.5M per center, a 5% variable cost and the $70M-a-year confirmatory study {i('CONFR')}. Centers for that cost line are derived from capacity at two procedures a week (about 29 in base), not from a company count {i('CAP_base')}.

**Hemgenix royalties.** These grow to ${b['lic']['FY33E']:.1f}M in FY2033E [{T.tid(F['lines'][0]['periods']['FY33E'])}]. The cash goes to HemB SPV under the royalty financing {i('RFIN')}; by analyst instruction, the $473.2M royalty-financing liability is not treated as debt in the valuation [P105].

## 6. Risks

*The main ways the forecast could be wrong, in rough order of importance. The valuation is about 11x the share price, so each of these matters.*

**Approval.** Base and bull assume US approval and launch on 1 July 2027; bear assumes no approval. The valuation is not probability-weighted, so the base value is conditional on approval {i('MHRA')}. The BLA has been submitted; FDA acceptance of the filing and the review outcome are both still open.

**Pool turnover.** The leave rate of 0.62 is the main lever. At about 0.40 a year (a 2.5-year stay), the 6,000 would need an unexplained eligibility filter, and base treated patients would fall to about 1,850 a year in the long run (scratch run, not in the forecast file) [P9]. If new entrants are only 30% of incidence, base treated falls to {D['sens']['base_kapusta_refill_30pct']['treated']['FY30E']:,.0f} in FY2030E and revenue to ${D['sens']['base_kapusta_refill_30pct']['rev']['FY30E']:,.0f}M (Figure 4).

**Capacity.** The 330 / 2,500 / 3,000 ramp is our ClearPoint forecast, not a company figure [D32]. Capacity binds through FY2030E in base and in every year in bull.

**Approval timing.** If approval slips to Q4 2027, base FY2027E revenue is ${D['sens']['base_q4_2027_approval']['rev']['FY27E']:,.0f}M (Figure 4).

**Payer budget.** US spend of about $6B a year from FY2029E invites managed access.

**Consensus.** FY2027E consensus is about one-sixth of our line build (consensus divided by build is {c27['value']:.3f}), well outside the 10% band in which we would scale; we do not scale it [{c27['citation']['id']}]. Goldman's reported peak is $2.5B {i('GS')}.

**Figure 4 – Sensitivities (US patients; US$M)**

*Each block shows one case against the filed forecast: approval slipping to Q4 2027, and new entrants at only 30% of incidence.*

{T.sens_table()}

*Source: forecast file sensitivities [D46].* **What this means:** an approval delay mainly moves FY2027E–FY2028E, while lower entrants cut long-run volume and revenue, which is what carries the valuation.

## 7. Forecast

*How the evidence becomes the forecast numbers, and the base case line by line.*

**How the evidence becomes the numbers.** The forecast is a quarterly line build. The US patient demand model is set out in full in Appendix D. FY2026E is consensus because there is no guidance. From FY2027E, US AMT-130 revenue is patients treated times net price; patients come from the pool model and the capacity ramp. Totals are the line build, not consensus.

**Figure 5 – Evidence → assumption → forecast impact**

*Read across each row: the evidence, the assumption we drew from it, and what that does to the forecast.*

| Evidence | Assumption | Forecast impact |
|---|---|---|
| ~6,000 initially treatable US patients at launch, management estimate {i('G6K','G6Kb')} | Start pool 6,000 on 2027-07-01 | Launch stock worked down to ~2,000 by FY2030E |
| Analyst choice of m = 0.62 as the most internally consistent leave rate {i('P9')} | Leave rate 0.62/yr (stay ~1.6 yr) | Steady pool ~6,000 with no extra filter; long-run treated ~2,840/yr |
| Crossover: 2 of 6 high-dose controls failed inclusion after ~12 months {i('XOVER')} | Not used; points to ~0.41/yr | Flagged as the main downside to demand |
| HD incidence {i('INC2')}; referral/willing/covered 90% each {i('HAIR_base')} | Entrants ~3,800/yr; treated share 72.9% | Sets long-run demand |
| ClearPoint capacity ramp [D32] | 330 / 2,500 / 3,000 cap | Binds FY2027E–FY2030E |
| Comparable list prices {i('PRAN')} | $2.0M net, −10% from FY2031E {i('PR_base')} | Revenue ~$6.0B FY2029E–FY2030E |
| Q2 2026 opex run rate {i('OPX')}; confirmatory study {i('CONFR')} | Opex build | EBITDA margin ~75–77% |
| FY2027E consensus [{c27['citation']['id']}] | Not scaled | Build far above consensus |

*Source: as tagged.*

**Base case.** Figure 6 shows the base case by line: reported years, consensus FY2026E, then the line build. Totals are the sum of the lines.

**Figure 6 – Base case by line, FY2024A–FY2033E**

{T.scen_table('base')}

*Source: forecast file [D46]. {T.fin_line('base')}. May not sum due to rounding.*

{VAL}

## 9. What Drives the Valuation: Key Assumptions and Sensitivities

*This section pulls together the assumptions that move the value most, what evidence supports each, and what happens if it is wrong. All numbers are from earlier sections and Appendix D.*

**Figure 13 – Key assumptions, evidence and sensitivity**

| Assumption | Value used | Evidence or judgment | Effect if wrong |
|---|---|---|---|
| Approval and launch | 1 July 2027 (base, bull) | Judgment from filing and review timing {i('MHRA')} | Q4 2027 approval: base FY2027E revenue ${D['sens']['base_q4_2027_approval']['rev']['FY27E']:,.0f}M (Figure 4); no approval is the bear case at {ps(X['value_per_share'])} [D45] |
| Launch pool | ~6,000 | Company management estimate {i('G6K')} | Criteria behind it undisclosed |
| Leave rate m | 0.62/yr (stay ~1.6 yr) | Judgment; evidence points nearer 0.41 {i('XOVER')}[C510] | At ~0.40 with a filter on all entrants, long-run treated ~1,850/yr [P9] |
| New entrants | ~3,800/yr | Incidence {i('INC2')} and 90% early-manifest share (assumption) | At 30% of incidence, base FY2030E treated {D['sens']['base_kapusta_refill_30pct']['treated']['FY30E']:,.0f} (Figure 4) |
| Treated share P | 0.729 | Assumption {i('HAIR_base')} | Scales long-run volume one-for-one |
| Capacity | 330 / 2,500 / 3,000 | ClearPoint forecast, judgment [D32] | Binds through FY2030E; bull's faster ramp front-loads volume |
| Net price | $2.0M, −10% from FY2031E | Assumption below comparable list prices {i('PRAN','PR_base')} | Revenue moves one-for-one |
| Terminal growth | 2% | Analyst instruction [P105] | Not reconciled with the forecast's next-period growth |
| Equity raises | $400M / $350M / ${RA['bear']:,.0f}M | Judgment [S] | Bear raise is about {RA['bear']/mcap:.1f}x market cap [C508] |

*Source: as tagged.* **What this means:** the base value is conditional on approval, and after approval the leave rate and treated share decide how many patients are treated once capacity stops binding. Those two are assumptions, not company figures.

**Demand-method caveats.**

- **m = 0.62 is a choice.** It was picked as the most internally consistent option, because at that leave rate incidence alone gives a steady pool of about 6,000 [P9]. It implies a 1.6-year stay, shorter than the duration evidence. In the trial, 2 of the 6 high-dose controls no longer met inclusion criteria after about 12 months {i('XOVER')}, which implies a leave rate of about 0.41 a year (derived; six patients, so the range is wide) [C510].
- **6,000 is not a treatment target.** uniQure calls it "Initial Treatable Patients at Launch", a management estimate of patients addressable at launch, about 30% of ~20,000 diagnosed patients {i('G6K','G6Kb')}. The criteria behind the 30% are not disclosed.
- **0.729 is an assumption.** The treated share is 90% referred × 90% willing × 90% covered; none is a company figure {i('HAIR_base')}.

**Valuation mechanics to note.**

- **Debt** is set at 1x EBITDA from FY2027E, the first year EBITDA is positive [P103][D46].
- **SBC** is 5% of sales once EBITDA is positive [P104][S].
- **Bear capex** equals base capex in dollars, which is large against bear's small revenue [P107].
- **Bear raise** is ${RA['bear']:,.0f}M, about {RA['bear']/mcap:.1f}x the ~${mcap/1000:.2f}B market cap, to keep bear cash positive [P109][C508].

**Open flags.**

- FY2027E is not scaled to consensus (consensus / build {c27['value']:.3f}, outside our 10% rule) [{c27['citation']['id']}].
- Base and bull raises ($400M / $350M) are larger than needed because EBITDA is positive from FY2027E [S].
- Cash accumulates with no distribution modelled [D45].
- Terminal growth of 2% is not reconciled with the forecast's next-period growth ({gs['base']*100:.2f}% base) [P105][D46].
- Centers are derived from capacity at two procedures a week, only for the opex line {i('CAP_base')}.

## Appendix A – Bull and Bear Cases

*The assumptions and line-by-line forecasts for the two alternative scenarios.*

**Bull.** Incidence of 1.59 per 100,000, a 95% referral share and an 85.7% treated share; the same 6,000 start pool with unfiltered entrants (a steady pool of ~8,200) {i('REF_bull')}. Capacity is 880 / 4,500 / 3,500 and binds every year {i('CAP_bull')}. Price is $2.4M, $2.16M from FY2028E {i('PR_bull')}. The UK launches from Q3 2028 at $1.5M {i('UKID')}.

**Figure A1 – Bull case by line**

{T.scen_table('bull')}

*Source: forecast file [D46]. {T.fin_line('bull')}.*

**Bear.** AMT-130 is not approved. Royalties continue and opex is cut to $140M.

**Figure A2 – Bear case by line**

{T.scen_table('bear')}

*Source: forecast file [D46]. {T.fin_line('bear')}.*

## Appendix B – Numbered sources

*Every tag cited in the report, grouped by type. File paths identify the data files the numbers were read from.*

SOURCES_HERE

## Appendix C – Method

We follow the forecaster method. Reported periods stay as reported. FY2026E is consensus, because there is no guidance. Later years are a quarterly line build: a pool of eligible patients is refilled by incidence and drained by treatment and by patients leaving the treatable window; treatment is capped by a capacity ramp; patients × net price set AMT-130 revenue. FY2027E is not scaled to consensus. Analyst instructions are tagged P and override the default method. Valuation numbers come only from Finagle's result file. Tags: A actual, G company statement, E external estimate, C calculation, S assumption, P analyst instruction, D document.
"""

md = md.rstrip() + '\n\n' + open(f'{H}/appendix_amt130.md').read()
APPX = {
 'D601': 'GEN StockWatch, 28 Sept 2025. Paraphrase: "About 6,000 patients, representing the initially treatable ~30% of the total ~20,000." https://www.genengnews.com/topics/translational-medicine/stockwatch-uniqure-shares-reach-five-year-high-on-game-changing-huntingtons-data/',
 'D602': 'ClinicalTrials.gov NCT04120493: early manifest HD, TFC 9 to 13, ages 25 to 65, CAG 40 or more, minimum putamen and caudate volumes. https://clinicaltrials.gov/study/NCT04120493',
 'D603': 'Medscape, 2026: the two other controls "no longer met eligibility criteria." https://www.medscape.com/viewarticle/huntington-therapy-faces-regulatory-roller-coaster-2026a1000k0l (search-result snippet)',
 'D604': 'EHDN Platform Meeting report, Nov 2025: "four were eligible and accepted the offer." https://ehdn.org/wp-content/uploads/2025/12/EHDN-Platform-Meeting-uniQure-Topline-Results-Report_Final_2-04-Dec-2025.pdf (search-result snippet)',
 'D605': 'Quarterly stock-and-flow pool structure, as used in the ClearPoint (CLPT) forecast; model files /workspace/out/AMT130_demand/scratch_m62/',
 'D606': 'ClearPoint Neuro CEO capacity comments, Q2 2026 call, as used in the CLPT forecast',
 'D607': 'Secondary review of uniQure filings and call transcripts (simulated-management research tool built on public sources; not an official uniQure statement): no treat-target language found; criteria behind the ~30% undisclosed',
 'G601': 'uniQure AMT-130 pivotal deck, 24 Sept 2025, slides 25 to 26: "~6,000\\* Initial Treatable Patients at Launch ... \\*Management Estimate". https://cdn.craft.cloud/fe68e1a2-b284-4f69-ba29-921f065edf17/assets/uploads/AMT-130-Pivotal-Sept-2025_final_09.24.25.pdf',
 'G602': 'uniQure 424B5 prospectus, 24 Sept 2025: "We estimate there will be 6,000 initial treatable patients addressable by AMT-130 in the U.S. at commercial launch, assuming approval." https://www.sec.gov/Archives/edgar/data/1590560/000110465925092995/tm2526258-1_424b5.htm (not reopened, unverified)',
 'G603': 'uniQure Q2 2026 call, 29 Jul 2026, K. O\'Keefe: capacity "depends on the number of neurosurgeons ... intraoperative OR suites"; more detail "in the coming months."',
 'G604': 'uniQure release on the Phase III update: "Four of the six control patients in the high-dose cohort were crossed over to treatment and the remaining two patients failed to meet the study\'s inclusion criteria." https://uniqure.gcs-web.com/news-releases/news-release-details/uniqure-announces-update-phase-iii-clinical-trials-amt-130-gene (search-result snippet)',
 'E601': '2CARE analysis: stay of about 2.3 to 2.9 years in the early-manifest window (paper not reopened, unverified)',
 'E602': 'Movement Disorders, 2024: early-manifest stay of 2 to 3 years (paper not reopened, unverified)',
 'E603': 'E070 dataset: 29-month mean, censored (not reopened, unverified)',
 'E604': 'Marder et al., Neurology 2000: about 0.97 TFC points a year. https://pubmed.ncbi.nlm.nih.gov/10668713/ (snippet only, unverified)',
 'E605': 'HDSA HD Roadmap: Stage I about 0 to 8 years. https://hdsa.org/wp-content/uploads/2015/07/HD-Roadmap2.pdf (snippet only, unverified)',
 'S601': 'Leave rate m = 0.62 a year (progression 0.60, death 0.02): analyst choice for internal consistency with the 6,000',
 'S602': 'HD incidence 1.22 per 100k, US population 340M, 90% early-manifest share, population growth 0.5% a year',
 'S603': 'Referral, willingness and coverage at 90% each, so P = 0.729',
 'S604': 'CLPT AMT-130 capacity ramp 330 / 2,500 / 3,000 cap; centre arithmetic is analyst judgment',
 'S605': 'Net price $2.0M per patient',
 'C601': '1.22e-5 x 340M x 0.9 = ~3,733 in 2026, ~3,750 to 3,770 in 2027 with growth; 3,733 / 0.625 = ~5,973',
 'C602': 'Quarterly simulation, /workspace/out/AMT130_demand/scratch_m62/run16.py (filter factor 1.0045)',
 'C603': 'Pool identity E - mS - T = gS with T = uS = PE gives u = P(m + g)/(1 - P), exact in any year; model ceiling u_d = 0.729 x (0.62 + 0.005)/(1 - 0.729) = 1.68 a year',
 'C610': 'Annual terms from a copy of scratch_m62/run16.py case A (/workspace/out/QURE_run_v11/amt130_annual_terms.py; results amt130_annual_terms.json): sums of quarterly entrants, leavers and treated; P = T/E, u = T/S, g = end/S - 1, m_eff = L/S',
 'D608': 'Wexler NS et al., Incidence of adult Huntington\'s disease in the UK: a UK-based primary care study and a systematic review, BMJ Open 2016;6:e009070: "overall rate of 7.2 (95% CI 6.5 to 7.9) per million person-years"; 393 incident cases, CPRD, adults 21+, 1990-2010. https://pmc.ncbi.nlm.nih.gov/articles/PMC4769413/ (abstract and methods only)',
 'C612': 'UK entrants = 0.72e-5 x 69M x 1.005^2 x 0.9 = ~452 a year at launch; start pool = entrants / (0.62 + 0.005) = 723; long-run demand = 0.729 x entrants = 329; capacity year 1 = max(2 x 52, 329/3) = 110, year 2 = 219, year 3+ = 329; centres = capacity / 52',
 'C613': 'UK quarterly simulation, /workspace/out/AMT130_demand/uk_dry_run/uk_pool.py (results uk_pool_results.json, run inc0.72_A_1pw); identity residual below 1e-12 in every year',
 'C614': 'uk_pool_results.json runs inc0.72_B_1pw (start pool 2,250), inc0.48_A_1pw and inc0.72_A_2pw',
 'C615': 'UK revenue = treated x $1.5M, e.g. 329 x 1.5 = 494',
 'C611': 'Identity check from amt130_annual_terms.json: |E - L - T - (end - S)| < 1e-9 and P(m_eff + g)/(1 - P) = u in every year FY2027 to FY2035',
 'C604': 'Bull ramp, scratch_m62/bull_chart.py: treated 880 / 4,498 / 3,073 / 2,786, then ~2,800 to 2,850',
 'C605': 'Cohort tracking with the even-draw rule: 2,232 of the launch 6,000 treated',
 'C606': '3,000 x $2.0M = $6.0B',
 'C607': '1.6 years x ~1 point a year = ~1.6 points; a 4-year window gives m = ~0.27 and a pool of 3,750 / 0.27 = ~13,800',
 'C608': 'scratch_m62/run25.py: unfiltered steady pool 9,218 at m = 0.40, filter factor 0.65',
 'C609': '-ln(1 - 1/3) = ~0.41 a year, so a stay of ~1 / 0.41 = ~2.4 years',
}
extra = {
 'D45': f"Finagle valuation result: /workspace/out/QURE_run_v11/valuation_result_v11.json, case_{{base,bull,bear}}_v11.json, QURE_{{base,bull,bear}}_v11.xlsx (Finagle commit {R['finagle_commit'][:8]}, run {R['run_at']})",
 'D46': 'Forecast file /workspace/out/QURE_run_v11/forecast.json and valuation request /workspace/out/QURE_run_v11/valuation_request_v11.json (file sha256 e6992a14...60e6; whole request f88d2805...cf93)',
 'P101': "Analyst instruction, dated 2026-10-29: \"take rd [cost of debt] as 10%\"",
 'P103': "Analyst instruction, dated 2026-10-29: \"keep debt constant until the year when EBITDA is positive. Then target 1x EBITDA from that year onward.\"",
 'P104': "Analyst instruction, dated 2026-10-30: \"Stock comp is held constant until EBITDA is positive and then is a fixed % of sales.\" Opening NOLs to be taken from the review of company filings.",
 'P105': "Analyst instruction, dated 2026-10-30: \"Take depreciation as half of capex in year 0. Liability isn\'t debt. Yes to 1xebitda rule. Add shares and cash in year 0 so cash doesn\'t go negative anywhere. 2% terminal growth. Dutch tax rate.\"",
 'P106': "Analyst instruction, dated 2026-10-30: \"use method=1 for capex. Capex can start in year 0 per [management] guidance but use the method after that.\"",
 'P107': "Analyst instruction, dated 2026-10-30: \"Take the exact same capex as the base case for the bear case.\"",
 'P109': "Analyst instruction, dated 2026-10-30: \"Raise the bear year-0 equity so cash never goes negative\"",
 'C401': 'Growth = revenue / prior revenue - 1; EBITDA margin = EBITDA / revenue; line share = line / total; from the forecast file',
 'C504': 'new shares = raise / fetched price US$25.30, from D45',
 'C508': 'bear raise / (fetched price x 10-K shares 62.53M) = 4,900 / 1,582, from D45',
 'C509': 'value per share / price - 1, from D45',
 'C510': 'leave rate = -ln(1 - 2/6) over ~1 year = ~0.41/yr, from A23',
 'S401': 'Revenue recognised at treatment (point in time), usual practice for one-time gene therapies; not a uniQure policy disclosure [S]',
 'S402': 'Q3 2026 results date 2026-11-04 (not reopened this revision) [S]',
 **APPX,
 'S': 'Judgment (untagged in the forecast file): raise sizes and SBC percentage'}
md = md.replace('[S]', '[S403]'); extra['S403'] = extra.pop('S')
used = set(re.findall(r'\[([A-Z]\d+)\]', md)) | {x for a, z in re.findall(r'\[([A-Z])(\d+)\]–\[', md) for x in []}
used |= {'P102', 'P108'} - {'P102', 'P108'}
order = 'DAGEPSC'
key = lambda k: (order.index(k[0]), int(k[1:]))
groups = [('Documents', 'D'), ('Actuals', 'A'), ('Guidance and management statements', 'G'), ('Estimates', 'E'), ('Analyst instructions', 'P'), ('Assumptions', 'S'), ('Calculations', 'C')]
OVR = {
 'P8': 'Analyst instruction, dated 2026-10-30: run the Finagle valuation on this forecast',
 'P9': 'Analyst instruction, dated 2026-10-30: use the pool model with m = 0.62, described as "the most internally consistent" leave rate',
 'D17': 'Analyst instructions, dated 2026-10-30 (capacity-limited in the short term; yearly refill equals incidence less patients excluded for eligibility, willingness and coverage). Written instruction; no page numbers',
 'D31': 'Analyst instructions, dated 2026-10-30 (pool model; leave rate m = 0.62; valuation run). Written instruction; no page numbers',
 'S9': 'Bull UK: MHRA approval and NHS access from Q3 2028; initial backlog 30% x 7,500 = 2250; refill 0.48/100k x 69M x bull haircut, 10%/yr attrition; centers [3, 6, 9, 12, 15]; 1 procedure/center/week (4.33/month); net price $1.5M [S]',
}
used |= {'D33'}
used |= {SRC[k]['document'] for k in list(used) if k in SRC and SRC[k].get('document') and k[0] != 'D'}
lines, notv = [], []
for title, L in groups:
    ks = sorted([k for k in used if k[0] == L], key=key)
    if not ks: continue
    lines += [f'**{title}**', '']
    for k in ks:
        s = SRC.get(k)
        if s is not None and k in OVR: s = dict(s, text=OVR[k])
        if k in extra and (s is None or k.startswith(('D45', 'D46', 'D47'))): lines.append(f'- **{k}** {extra[k]}'); continue
        if s is None: lines.append(f'- **{k}** MISSING'); continue
        txt = s['text']; doc = s.get('document'); pg = s.get('page') or s.get('page_status', '')
        if L == 'D': lines.append(f"- **{k}** {txt}: {s.get('url','')}")
        else: lines.append(f"- **{k}** {txt}" + (f" ({doc}{', ' + str(pg) if pg else ''})" if doc else ''))
        if 'unverified' in (txt + str(pg)).lower(): notv.append(k)
lines += ['', '**Not verified**', '', '- ' + ', '.join(sorted(set(notv), key=key)) + ': page or link unverified as marked in the forecast file. The crossover quote (A23, D33) is from a search result; the full release was not reopened. The ClearPoint ramp (D32) is our own uncommitted forecast case.']
md = md.replace('SOURCES_HERE', '\n'.join(lines))
open(f'{H}/report_v11.md', 'w').write(md)
print('missing', [l for l in lines if 'MISSING' in l])
