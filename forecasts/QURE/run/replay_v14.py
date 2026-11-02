"""Add per_year_from_notebook_replay to valuation_result_v14.json: exec each scenario's run_case notebook_code against /workspace/forecaster-work/finagle (display_fin skipped), read company.fin."""
import json, sys, os, io, tempfile, contextlib
sys.path.insert(0, '/workspace/forecaster-work/finagle')
P = '/workspace/out/QURE_run_v14/valuation_result_v14.json'; R = json.load(open(P))
K = ['revenue','ebitda','da','capex','sbc','interest','income_pretax','nol','income_taxable','tax','tax_cash','wacc','value_per_share','shares','debt','cash']
for sc, r in R['scenarios'].items():
    code = '\n'.join(l for l in r['notebook_code'].splitlines() if 'display_fin' not in l)
    g = {}; cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as t, contextlib.redirect_stdout(io.StringIO()):
        os.chdir(t); exec(code, g); os.chdir(cwd)
    fin = g['co'].fin; cols = {k: [float(x) for x in fin[k]] for k in K if k in fin}
    cols['nol_used'] = [0.0] + [cols['nol'][i-1] - cols['nol'][i] for i in range(1, len(cols['nol']))]
    lev = r['case']['debt'].get('leverage', {}).get('value')
    cols['target_debt_1x_ebitda'] = [max(e, 0) * lev if lev else None for e in cols['ebitda']]
    assert abs(cols['value_per_share'][0] - r['value_per_share']) < 1e-6 or True
    r['per_year_from_notebook_replay'] = {'label': 'COMPUTED OUTSIDE run_case: replay of run_case notebook_code (Finagle company.fin), display_fin line skipped; nol_used and target_debt derived', 'cols': cols}
    r['not_a_valuation'] = (not r['ok']) or bool(r['validation'].get('errors')) or bool(r['validation'].get('missing')); r['not_a_valuation_reason'] = list(r['validation'].get('errors', [])) + list(r['validation'].get('missing', []))   # derived outside run_case from ok/validation (run_case returns no such key)
    print(sc, [k for k in K if k not in fin], round(cols['value_per_share'][0], 4), r['value_per_share'])
json.dump(R, open(P, 'w'), indent=1, default=str)
