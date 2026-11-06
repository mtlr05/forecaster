"""Write forecast.md, revision_log.md and diff_v10_v11.md for QURE v11 (rev4) under /workspace/out/QURE_run_v11/."""
import json, sys, os
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
import tables as T, model as M
H = T.H; F, D, I, O, Y = T.F, T.D, T.I, T.O, T.Y
REQ = json.load(open(f'{H}/valuation_request_v11.json')); SHA = json.load(open(f'{H}/valuation_request_v11.sha256.json'))
DRY = open(f'{H}/dry_v11_summary.txt').read()
i = lambda k: f"[{I[k]}]"
fl = [u for u in REQ['undecided_by_david'] if u['item'].startswith('v11')][0]['risk']
md = f"""# QURE (uniQure) forecast, v11 (rev4) as of 2026-10-30

## Status and open items

- Version **v11 / rev4**, supersedes v10 (rev3, kept intact in /workspace/out/QURE_run/ and forecasts/QURE/). Uncommitted. Rebuild from `/workspace/out/QURE_run_v11/build/`: `python3 build_forecast.py` (needs `model.py`), then `cd .. && python3 build_request_v11.py` (scratch dry check via `dry11.py`), then `python3 build/make_md_v11.py`.
- Driver, David May 2026-10-30 {i('P8')}: "Write is up with m=0.62 its the most internally consistent"; {i('P9')} "Redo the finagle too".
- US AMT-130 treated = min(CLPT capacity, pool demand) {i('CAP_base')}{i('Y1_base')}: start pool 6,000 at 2027-07-01 {i('G6K')}; leave rate m = 0.62/yr (progression 0.60 + death 0.02) {i('ATTR')}; P = 0.9 x 0.9 x 0.9 = 0.729 {i('HAIR_base')}; entrants 1.22/100k x 340M x 0.90 x 1.0045 (filter that holds the steady pool at 6,000), +0.5%/yr {i('REF_base')}; quarterly. Capacity: CLPT ramp 330 (FY27, half year) / 2,500 (FY28) / 3,000 cap from FY29 (bull 880 / 4,500 / 3,500) {i('CAP_bull')}.
- Bull: incidence 1.59, share 0.95, P = 0.95^3 = 0.857, same 6,000 start pool, entrants unfiltered (steady pool ~8,200) {i('REF_bull')}; capacity binds every year. UK unchanged from v10. Bear: not approved (unchanged).
- Unchanged from v10: price ($2.0M base, -10% from FY31E; bull $2.4M, $2.16M from FY28E), COGS/patient, opex rules (incl. $1.5M per center, now centers = capacity / 104 procedures/yr), confirmatory R&D $70M/yr, Hemgenix royalty and HemB SPV treatment, FY26E = consensus, FY27E not scaled to consensus (ratio {D['base']['scale27']:.3f}, flagged).
- Open: (1) m = 0.62 (stay ~1.6 yr) is shorter than the duration evidence; crossover data (2 of 6 high-dose controls failed inclusion after ~12 months {i('XOVER')}) point to ~0.41/yr; (2) bull start pool and unfiltered entrants [S]; (3) center count used for opex [S]; (4) raise sizes and bear raise (see flags); (5) Q3 2026 results 2026-11-04.

## base

{T.scen_table('base')}

{T.fin_line('base')}. Rows may not sum due to rounding.

## bull

{T.scen_table('bull')}

{T.fin_line('bull')}.

## bear

{T.scen_table('bear')}

{T.fin_line('bear')}. Bear (not approved): unchanged from v10.

## Sensitivities

{T.sens_table()}

## v10 -> v11

{T.oldnew('base')}

{T.oldnew('bull')}

{T.oldnew('bear')}

## Flags (volume-dependent v10 items)

{fl}

Scratch dry check (not a valuation):

```
{DRY}```

## Assumptions to revise

1. m = 0.62 [P] {i('ATTR')}: the main lever; at m = 0.40 base treated falls to ~1,850/yr long run if the 6,000 needs a filter on entrants.
2. CLPT capacity ramp [S] {i('CAP_base')}: binds through FY30E base, every year bull.
3. Price $2.0M and -10% step [S] {i('PR_base')}.
4. Bull start pool 6,000 with unfiltered entrants [S] {i('REF_bull')}.
5. COGS {i('COGS_base')}, commercial fixed and per-center opex [S].

## Sources

See `sources` in forecast.json. Documents:
""" + '\n'.join(f"- {s['id']}: {s['text']}" for s in F['sources'] if s['id'].startswith('D')) + '\n'
open(f'{H}/forecast.md', 'w').write(md)
rows = []
for n in ('base', 'bull', 'bear'):
    for y in ['FY27E', 'FY28E', 'FY29E', 'FY30E', 'FY31E']:
        for lab, k in [('AMT-130', 'amt'), ('Revenue', 'rev'), ('EBITDA', 'e')]:
            o = O[n][k][y]; w = D[n][k][y]
            rows.append(f"| {lab} ({n}) | {y} | {o:.1f} | {w:.1f} | {w-o:+.1f} | {'unchanged' if abs(w-o) < 0.05 else 'pool model m = 0.62 with CLPT ramp replaces rev3 year-1 path and center engine [P8 2026-10-30]'} |")
    if n != 'bear':
        for y in ['FY27E', 'FY28E', 'FY29E', 'FY30E', 'FY31E']:
            o = O[n]['pt']['treated'][y]; w = D[n]['pt']['treated'][y]
            rows.append(f"| US patients treated ({n}, patients/yr) | {y} | {o:,.0f} | {w:,.0f} | {w-o:+,.0f} | [P8 2026-10-30] |")
old = open(f'{B}/revision_log_v10.md').read().rstrip('\n')
open(f'{H}/revision_log.md', 'w').write(old + f"""

## rev4 / v11, 2026-10-30

P-tag items: [{I['P8']}] David May t97u "Write is up with m=0.62 its the most internally consistent"; [{I['P9']}] t98u "Redo the finagle too". Filings: no new uniQure 10-Q/8-K since rev3 (Q3 2026 results due 2026-11-04). Consensus unchanged (Yahoo pull 2026-10-29 [D6]).

| Line | Period | Old (v10) | New (v11) | Change | Why |
|---|---|---|---|---|---|
""" + '\n'.join(rows) + '\n')
# diff summary
L = ["# QURE v10 -> v11 diff (US$M; patients/yr)", ""]
for n in ('base', 'bull', 'bear'):
    L += [f"## {n}", "", T.oldnew(n), ""]
L += ["## Valuation request", "", f"- v11: {H}/valuation_request_v11.json", f"- whole_request sha256: {SHA['whole_request']}", f"- file_bytes sha256: {SHA['file_bytes']}", ""]
open(f'{H}/diff_v10_v11.md', 'w').write('\n'.join(L))
print('ok')
