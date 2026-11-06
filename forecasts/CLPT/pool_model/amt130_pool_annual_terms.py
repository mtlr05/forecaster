"""AMT-130 US treatable-pool model (quarterly stock-and-flow), annual terms of the pool identity. Same logic and inputs as the QURE v11 Appendix D base case (m = 0.62, 6,000 launch pool, CLPT capacity ramp 330 / 2,500 / 3,000)."""
import json
P=0.729;g=0.005;m=0.62
E0=1.22/1e5*340e6*.9; f=6000*(m+g)/E0; ud=P*(m+g)/(1-P)
S=6000.0; out={}
for i in range(34):
    y=2027+(i+2)//4
    cap=330/2 if y==2027 else (2500/4 if y==2028 else 750)
    E=E0*(1+g)**(y-2026)*f/4; D=ud/4*S; T=min(cap,D,S); L=m/4*S
    a=out.setdefault(y,dict(S=S,E=0,L=0,T=0,D=0,cap=0,qbind=[]))
    a['E']+=E;a['L']+=L;a['T']+=T;a['D']+=D;a['cap']+=cap;a['qbind'].append('capacity' if cap<=D else 'demand')
    S=S+E-L-T; a['end']=S
for y,a in out.items():
    a['P']=a['T']/a['E']; a['u']=a['T']/a['S']; a['g']=a['end']/a['S']-1; a['m_eff']=a['L']/a['S']
    a['identity_resid']=a['E']-a['L']-a['T']-(a['end']-a['S'])
    a['u_identity']=a['P']*(a['m_eff']+a['g'])/(1-a['P'])
    a['binds']='/'.join(sorted(set(a['qbind']))) ; a['half_year']=(y==2027)
json.dump(dict(m=m,f=f,u_d=ud,P_star=P,g_star=g,source='copy of scratch_m62/run16.py case A (run25.sim logic)',years=out),open('amt130_pool_annual_terms.json','w'),indent=1)
for y,a in out.items(): print(y,*['%s=%.4f'%(k,a[k]) if isinstance(a[k],float) else '%s=%s'%(k,a[k]) for k in ['S','E','L','T','end','P','u','g','m_eff','u_identity','identity_resid','cap','D','qbind']])
print('f',f,'ud',ud)
