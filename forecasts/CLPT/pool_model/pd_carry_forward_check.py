"""Illustration only (not used in forecast or valuation): Parkinson's class pool from partners/pd_simple4_model.json
re-run with treated = min(forecast class volume, 6% of pool), so demand not served during the FY2029E-30E ramp stays in the pool."""
import json
d=json.load(open('../partners/pd_simple4_model.json'));X=d['inputs'];c=d['chain']
S=c['U0'];caps={2029:3919,2030:7594};rows=[]
for t in range(2026,2041):
    E=c['E0']*(1+X['G'])**(t-2026);D=0 if t<X['LAU'] else X['U']*S;T=min(D,caps.get(t,1e9))
    rows.append(dict(t=t,S=S,E=E,L=X['M']*S,demand=D,T=T,end=S+E-X['M']*S-T));S=rows[-1]['end']
base={r['t']:r['T'] for r in d['rows']}
json.dump(dict(rows=rows,base_class_demand=base),open('pd_carry_forward_check.json','w'),indent=1)
for r in rows:
    if r['t']>=2029: print(r['t'],round(r['demand']),round(r['T']),'base demand',round(base[r['t']]))
