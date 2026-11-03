"""AMT-130 pool model: how many of the 6,000 launch-pool patients are treated before leaving (treatments drawn evenly from launch patients and later entrants), and the m = 0.40 (2.5-year stay) sensitivity. Same logic as amt130_pool_annual_terms.py."""
import json
def run(m,f,pool0,P=0.729,g=0.005,nq=36):
    u=P*(m+g)/(1-P); S=pool0; C=pool0; cum=0; ann={}
    for i in range(nq):
        y=2027+(i+2)//4
        cap={2027:165,2028:625}.get(y,750)
        E=1.22/1e5*340e6*(1+g)**(y-2026)*.9*f/4
        D=u/4*S; T=min(cap,D,S); share=C/S
        cum+=T*share; C=C-m/4*C-T*share; S=S+E-m/4*S-T; ann[y]=ann.get(y,0)+T
    return dict(launch_cohort_treated=cum,treated={y:round(v) for y,v in ann.items()})
E=1.22/1e5*340e6*.9
out={}
out['m062']=run(0.62,6000*0.625/E,6000)
f40=6000*0.405/E
out['m040_filter_stock_and_entrants']=run(0.40,f40,6000)|{'filter':f40}
out['m040_filter_stock_only']=run(0.40,1.0,6000)
out['m040_unfiltered_pool']=E/0.405
json.dump(out,open('amt130_launch_cohort.json','w'),indent=1)
for k,v in out.items(): print(k,v)
