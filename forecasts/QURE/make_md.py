"""Write forecast.md and revision_log.md for QURE rev3."""
import json, os, importlib.util
H = os.path.dirname(os.path.abspath(__file__)); os.chdir(H)
import tables as T
spec = importlib.util.spec_from_file_location('qm', f'{H}/model.py'); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
F, D, I, O, Y = T.F, T.D, T.I, T.O, T.Y
ALT = {n: 0.30 * M.refill(n)[0] for n in ('base', 'bull')}
def cum_hit(n, **kw):
    c = 0
    for r in M.run(n, **kw):
        c += r['treated']
        if c >= 6000: return f"Q{r['q']} {r['y']}"
def clear(n, **kw):
    r = [r for r in M.run(n, **kw) if r['backlog'] < 1 and r['treated'] > 0][0]; return f"Q{r['q']} {r['y']}"
def peakc(n): return max(r['centers'] for r in M.run(n))
rb, ru = M.refill('base'), M.refill('bull')
i = lambda k: f"[{I[k]}]"
CLR = '\n'.join(f"| {n} | {lab} | {cum_hit(n, **kw)} | {clear(n, **kw)} |" for n in ('base', 'bull') for lab, kw in
               (('filed (approval 2027-07-01)', {}), ('approval Q4 2027', dict(delay=1)), ('Kapusta refill 30% of incidence', dict(refill_override=ALT[n]))))
md = f"""# QURE (uniQure) forecast, rev3 as of 2026-10-30

## Status and open items

- Version **rev3** (supersedes rev2b of 2026-10-30; rev2b kept intact in /workspace/out/QURE_forecast_rev2b/), uncommitted. Rebuild: `python3 build_forecast.py` (needs `model.py`), `python3 make_md.py`.
- Driver of this revision, David May 2026-10-30 [{I['P7']}]: "We can say that centers don’t limits capacity in year one and use your 190". "Your 190" is the Matt Kapusta CEO-simulation bot's year-1 path of about 10 / 30 / 60 / 90 patients per quarter (a pointer, not a document).
- Year one (Q3 2027-Q2 2028): US treated = base 10/30/60/90 = 190 {i('Y1_base')}; bull 15/45/90/135 = 285 (1.5x base [S]) {i('Y1_bull')}. Centers do not bind.
- Year two (Q3 2028-Q2 2029) bridge [S] {i('BR_base')}{i('BR_bull')}: capacity rises linearly from the year-1 exit run-rate (90/qtr base, 135 bull) to 30 centers x throughput at Q2 2029 (base 536/qtr, bull 731); centers 15 -> 30. Which 30: ClearPoint said on its Q2 2026 call that 15 centers had qualified and the goal is 20-30 {i('CLP1')}; the Kapusta bot put ~30 by the end of year 2. David's earlier "around 30 centers that can do 1-2 procedures a week" [{I['P5']}] is therefore used as the end-of-year-2 network, not the launch network: that is the more defensible reading once year one is decoupled from centers (it matches the documented 15 today and the 20-30 goal).
- From Q3 2029: rev2b logic unchanged (centers +3/qtr base, +5 bull while a backlog exists, to 70/100; throughput rising to 2.0/week; then demand = backlog + refill per David's refill rule [{I['P3']}]).
- All other rev2b inputs kept: price, COGS, opex incl. confirmatory R&D $70M/yr, Hemgenix royalty treatment, bear.
- Open: (1) refill: David's incidence-less-a-few (base {rb[1]:,.0f}/yr) vs Kapusta's 30% of incidence ({ALT['base']:,.0f}/yr base, {ALT['bull']:,.0f} bull); (2) year-2 bridge shape [S]; (3) bull year-1 multiple [S]; (4) price step-down; (5) confirmatory-study cost; (6) royalty cash to HemB SPV; (7) Q3 2026 results 2026-11-04.

## Background: rev2b (kept unless changed above)

1. *(rev2b; superseded by rev3 for year one and year two, see above)* **Capacity at launch [{I['P5']}] (assumption [S] {i('CAP_base')}{i('CAP_bull')}).** 30 centers ready at approval (2027-07-01; ClearPoint expects a decision mid to 2H 2027 {i('CLP3')}). Throughput: base 1.0 procedure/center/week at launch rising 0.125/qtr to 2.0; bull 1.5 rising to 2.0. Capacity = centers x procedures/week x 13 weeks x utilisation.
2. *(rev2b; replaced in rev3 by the fixed year-1 path)* **Short-term limit (undisclosed, assumed [S]).** Utilisation of the ready capacity in the first quarters: base 50% / 67% / 83% / 100%, bull 67% / 83% / 100%. This stands for site activation, surgeon proctoring, the referral and prior-authorisation pipeline. Genezen vector supply is assumed not binding through FY29E (no disclosed dose capacity). ClearPoint says its own technology and support would not be the bottleneck; hospital scaling is {i('CLP1')}.
3. **Growth beyond 30 [S].** While a backlog exists, +3 centers/qtr (bull +5), capped at 70 (bull 100). Cross-checks: HDSA has 69 Centers of Excellence and partner sites {i('HDSA')}; ClearPoint targets "the first 35-40 specialized treatment centers which can add 5,000 patients a year in capacity" across all its partners {i('CLP2')} (about 2.4-2.75 procedures/center/week). The cap never binds before the backlog clears (peak: base {peakc('base'):.0f}, bull {peakc('bull'):.0f} centers). After clearing, the network falls back to the 30 launch centers with spare capacity (demand-limited).
4. **Demand unchanged from rev2.** Backlog ~6,000 {i('G6K')}; refill (David's rule [{I['P3']}]) base {rb[0]:,.0f} x 85% x 90% x 90% = **{rb[1]:,.0f}/yr**, bull {ru[0]:,.0f} x 90% x 95% x 95% = **{ru[1]:,.0f}/yr**; untreated backlog attrition 10%/yr.
5. **Price [S].** Base $2.0M net FY27E-FY30E, then -10% to $1.8M from FY31E (US sales pass $2B in FY28E; step applied not before FY31E). Bull $2.4M, $2.16M from FY28E (passes $2B in FY27E) {i('PR_base')}{i('PR_bull')}. Gross list analogues: Lenmeldy $4.25M, Kebilidi $3.95M, Elevidys $3.2M, Hemgenix ~$3.5M {i('PRAN')} (secondary compilation). Zolgensma ~$2.1M not opened (unverified).
6. **Costs [S].** COGS $0.30M/patient falling to $0.20M (bull $0.18M), **unverified**; no AMT-130 licensor royalty is disclosed (the royalty-bearing Regenxbio AAV9 licence is for AMT-260 {i('REGX')}), so none is modelled. Opex: Q2 2026 cash run rate x4 +3%/yr, US commercial fixed **$80M** (bull $90M), $1.5M/active center, 5% of AMT-130 revenue, UK $15M (bull), plus **confirmatory-study R&D $70M/yr FY27E-FY31E** {i('CONFR')} (FDA-aligned randomized standard-of-care-controlled study, TFC at 36 months {i('CONF')}).
7. **Hemgenix royalty (financing).** uniQure sold Hemgenix royalties to HemB SPV (May 2023), booked as debt: liability $473.2M at 2025-12-31, cap 1.85x upfront ($693.8M) by 2032-06-30, else up to 2.25x through 2038 {i('RFIN')}. License revenue stays in GAAP revenue and EBITDA, but the **cash goes to the SPV** until the cap is met; for valuation, treat the $473.2M as debt (or remove royalty cash). 
8. **FY27E not scaled to consensus.** David's capacity instruction overrides consensus: base FY27E revenue ${D['base']['rev']['FY27E']:,.0f}M vs consensus ${D['base']['rev']['FY27E']*D['base']['scale27']:,.0f}M (ratio {D['base']['scale27']:.3f}) [{F['bridge']['base_fy27_consensus_vs_build']['citation']['id']}]: flagged.
9. **Window FY26E-FY33E.** rev3: base backlog clears in 2031 and reaches steady state in FY32E, bull UK in FY33E; me is a steady-state margin.

**Time to work down the backlog (quarter when cumulative US treated passes 6,000 / quarter when the eligible US backlog is cleared):**

| Scenario | Case | Cumulative 6,000 treated | Backlog cleared |
|---|---|---|---|
{CLR}

Bull UK backlog (~2,250) is cleared in FY32E. Bear: not approved.

## Kapusta review: applied / not applied and why

| Item | Status | Why |
|---|---|---|
| (a) Confirmatory-study R&D ~$60-80M/yr FY27-31 | Applied, $70M/yr [S] {i('CONFR')} | Design confirmed in the Q2 2026 call {i('CONF')}; cost undisclosed |
| (b) US commercial fixed ~$80M | Applied, base $80M, bull $90M [S] | judgment, no disclosure |
| (c) Price $2.0M base, -10% past $2B/yr; bull $2.4M | Applied [S] {i('PR_base')}{i('PR_bull')} | analogue list prices cited {i('PRAN')} |
| (d) Vector not binding through FY29E; COGS unverified | Applied | Genezen preferential access {i('GENZ')}; no dose capacity disclosed |
| (e) Hemgenix royalties sold to HemB SPV; drop AMT-130 licensor royalty | Applied {i('RFIN')}{i('REGX')} | liability $473.2M confirmed in the 10-K |
| (f) Q4 2027 approval sensitivity | Applied as sensitivity; base stays 2027-07-01 | ClearPoint: mid to 2H 2027 {i('CLP3')} |
| (g) UK in bull from Q3 2028 | Kept | unchanged |
| (1) Refill 30% of incidence (~490 base / ~1,000 bull) | **Not applied to the filed case**; shown as a sensitivity | David's refill rule [{I['P3']}] takes precedence; key open question |
| (2) Center ceiling 70 base / 100 bull | Applied as cap [S] (non-binding) | HDSA 69 sites {i('HDSA')}, ClearPoint 35-40 initial centers {i('CLP2')}; launch count is David's 30 [{I['P5']}], not Kapusta's |

## base

{T.scen_table('base')}

{T.fin_line('base')}. May not sum due to rounding.

Base capacity ramp [{I['Y1_base']}], first 12 quarters after approval (rev3: Q3 2027-Q2 2028 fixed year-1 path, centers shown are the 15 qualified and do not bind; Q3 2028-Q2 2029 bridge) [{I['CAP_base']}]:

{T.ramp_table('base')}

## bull

{T.scen_table('bull')}

{T.fin_line('bull')}.

Bull capacity ramp [{I['CAP_bull']}][{I['Y1_bull']}]:

{T.ramp_table('bull')}

## bear

{T.scen_table('bear')}

{T.fin_line('bear')}. Bear adds the confirmatory study? No: bear is not approved, opex unchanged from rev2.

## Sensitivities

{T.sens_table()}

## rev2b -> rev3

{T.oldnew('base')}

{T.oldnew('bull')}

{T.oldnew('bear')}

## Verified vs assumed

Verified this revision (opened): ClearPoint Q2 2026 call (15 qualified centers, 1-2/week, 20-30 goal, hospital scaling is the constraint); ClearPoint Q3 2025 press release (35-40 centers, 5,000/yr); ClearPoint Q3 2026 call (approval mid to 2H 2027); ClearPoint 8-K 2026-10-28 (>175 active global centers, all indications); HDSA (69 sites); uniQure 10-K (HemB SPV royalty financing, $473.2M liability, caps; Regenxbio licence is AMT-260); uniQure Q2 2026 call (confirmatory study design); IntuitionLabs list prices (secondary).
Assumed [S]: launch utilisation, throughput path, center additions and cap, price and step-down, COGS, commercial fixed cost, confirmatory cost, approval date, refill haircuts, attrition, UK.

## Sources

See `sources` in forecast.json. Documents:
""" + '\n'.join(f"- {s['id']}: {s['text']}" for s in F['sources'] if s['id'].startswith('D')) + '\n'
md = md.replace("{T.fin_line('bear')}. Bear adds the confirmatory study? No: bear is not approved, opex unchanged from rev2.", "")
md = md.replace(". Bear adds the confirmatory study? No: bear is not approved, opex unchanged from rev2.", ". Bear (not approved): no confirmatory study or launch costs; lines unchanged from rev2b.")
open('forecast.md', 'w').write(md)
old = open('/workspace/out/QURE_forecast_rev2b/revision_log.md').read().rstrip('\n')
rows = []
why = {'lic': 'unchanged', 'amt': 'year one not limited by centers; ~190 path (bull 285) then bridge to 30 centers by Q2 2029 [P7 2026-10-30]',
       'rev': 'AMT-130 timing [P7 2026-10-30]', 'e': 'AMT-130 volume timing (year-1 path, later backlog clearance); costs unchanged [P7 2026-10-30]'}
for n in ['base', 'bull', 'bear']:
    for y in ['FY27E', 'FY28E', 'FY29E', 'FY30E', 'FY31E']:
        for lab, k in [('AMT-130', 'amt'), ('Revenue', 'rev'), ('EBITDA', 'e')]:
            o = O[n][k][y]; w = D[n][k][y]; ch = w - o
            rows.append(f"| {lab} ({n}) | {y} | {o:.1f} | {w:.1f} | {ch:+.1f} | {'unchanged' if abs(ch) < 0.05 else why[k]} |")
    if n != 'bear':
        for y in ['FY27E', 'FY28E', 'FY29E', 'FY30E', 'FY31E']:
            o = O[n]['pt']['treated'][y]; w = D[n]['pt']['treated'][y]
            rows.append(f"| US patients treated ({n}, patients/yr) | {y} | {o:,.0f} | {w:,.0f} | {w-o:+,.0f} | [P7 2026-10-30] |")
log = old + f"""

## rev3, 2026-10-30

P-tag item (David May, direct message, 2026-10-30, t62u):
- [{I['P7']}] "We can say that centers don’t limits capacity in year one and use your 190" ("your 190" = the Matt Kapusta CEO-simulation bot's ~10/30/60/90 patients per quarter in the first four quarters after the 2027-07-01 approval; pointer only, tagged [S] {I['Y1_base']}).

Year two bridges linearly from 90 patients/qtr (bull 135) to 30 centers by Q2 2029 [{I['BR_base']}]; rev2b logic after that. Bull year one = 1.5x base [S]. Window unchanged FY26E-FY33E. Filings checked: no new uniQure 10-Q/8-K since rev2b (Q3 2026 results due 2026-11-04).

| Line | Period | Old (rev2b) | New (rev3) | Change | Why |
|---|---|---|---|---|---|
""" + '\n'.join(rows) + '\n'
open('revision_log.md', 'w').write(log)
print('ok')
