"""AMT-130 pool model (same logic as amt130_pool_annual_terms.py) run on the CLPT bull and bear AMT-130 volume paths used as capacity."""
import json
P=0.729;g=0.005;m=0.62
E0=1.22/1e5*340e6*.9; f=6000*(m+g)/E0; ud=P*(m+g)/(1-P)
def run(caps):  # caps: annual capacity by FY from FY2027; FY2027 is a half year (Q3-Q4)
    S=6000.0; out={}
    for i in range(34):
        y=2027+(i+2)//4
        c=caps.get(y,caps['later']); cap=c/2 if y==2027 else c/4
        E=E0*(1+g)**(y-2026)*f/4; D=ud/4*S; T=min(cap,D,S); L=m/4*S
        out[y]=out.get(y,0)+T; S=S+E-L-T
    return {y:round(v) for y,v in out.items()}
cases={'base':{2027:330,2028:2500,'later':3000},
       'bull':{2027:880,2028:4500,'later':3500},
       'bear':{2027:0,2028:270,2029:1000,2030:1800,2031:2300,'later':3000}}
fc={'base':[330,2500,3170,3000,3000],'bull':[880,4500,4120,3500,3500],'bear':[0,270,1000,1800,2300]}
res={k:run(v) for k,v in cases.items()}
json.dump(dict(model=res,forecast_FY27_31=fc,capacity=cases|{} ),open('amt130_pool_cases.json','w'),indent=1,default=str)
for k in res: print(k,'model',[res[k][y] for y in range(2027,2036)],'forecast',fc[k])
