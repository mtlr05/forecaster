"""Steady-state funnels, ramps, revenue and probability chart for ClearPoint partners on slide 23 (2Q26 deck)."""
import json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
PRICE=0.020; YRS=list(range(2027,2041))
BIRTHS=3_628_934; MALE=0.512
# ---- funnels (value, label, tag)
F={}
def fun(k,steps): 
    v=1.0; rows=[]
    for lab,x,tag in steps:
        v = x if not rows else v*x; rows.append((lab,x,round(v,1),tag))
    F[k]=rows; return v
# PD shared pool (from CLPT v6 forecast C37/C38)
pd_flow=fun('PD class (shared)',[('Restorative one-time PD demand, new patients (CLPT v6)',4184,'C37'),
    ('× class expansion: 4 products, gene therapy needs no immunosuppression ★',1.2,'S50')])
pd_back=42000/10   # C38 backlog drawn over 10 yrs ★ S51
pd_class=pd_flow+pd_back
SS={'BRT-DA01':5000,'AMT-130':3000}
alloc={'AB-1005':0.52,'ANPD001':0.24,'RNDP-001':0.24}  # S52: split of residual after bemdaneprocel
resid=pd_class-SS['BRT-DA01']
for k,a in alloc.items(): SS[k]=round(resid*a/100)*100
SS['NRTX-1001']=round((fun('NRTX-1001',[('DR-MTLE incidence (3.1–3.4/100k × 324M)',10500,'A21'),
  ('× adults in trial age range ★',0.85,'S53'),('× identified/referred at epilepsy centre ★',0.50,'S53'),
  ('× willing (non-destructive one-time vs resection/LITT) ★',0.50,'S53'),('× access/reimbursement ★',0.80,'S53'),
  ('× share vs resection, LITT, RNS ★',0.70,'S53')])*(1+0.119*160000/10/1250*0+1))/100)*100   # flow + backlog (C52)
F['NRTX-1001'].append(('+ prevalent backlog 143k–191k × same screens (11.9%) ÷ 10 yrs',None,round(0.119*167000/10),'A21, C52'))
SS['NRTX-1001']=round((F['NRTX-1001'][-2][2]+0.119*167000/10)/100)*100
v=fun('AVB-101',[('FTD incidence ages 45–64, ~3.4/100k × ~83M',2800,'A22, C53'),('× GRN mutation share 5%',0.05,'A23'),
  ('× genetically diagnosed ★',0.60,'S54'),('× early-stage, age 30–75 per trial ★',0.70,'S54, A24'),('× willing ★',0.60,'S54'),
  ('× access ★',0.80,'S54'),('× share vs other GRN therapies ★',0.50,'S54')])
F['AVB-101'].append(('+ backlog 1,000–1,500 prevalent × same screens ÷ 5 yrs',None,round(1250*v/140/5),'A23, C53'))
SS['AVB-101']=round((v+1250*v/140/5)/5)*5
v=fun('KEBILIDI',[('US births × 1/90,000',BIRTHS/90000,'A25, A26'),('× diagnosed ★',0.60,'S55'),('× eligible per label ★',0.90,'S55'),
  ('× willing ★',0.80,'S55'),('× access ★',0.80,'S55'),('× share (only approved therapy)',1.0,'S55')]); SS['KEBILIDI']=round(v)
v=fun('RGX-121',[('Male births × 1/162,000',BIRTHS*MALE/162000,'A26, A27'),('× neuronopathic ~2/3 ★',0.67,'S56'),
  ('× diagnosed young enough ★',0.70,'S56'),('× willing ★',0.80,'S56'),('× access ★',0.80,'S56'),('× share vs ERT/brain-penetrant ERT ★',0.60,'S56')]); SS['RGX-121']=max(1,round(v))
v=fun('SRN-101',[('Glioblastoma incidence (CBTRUS)',13450,'A28'),('× recurrence ★',0.90,'S57'),('× resectable at recurrence ★',0.30,'S57'),
  ('× willing ★',0.70,'S57'),('× access ★',0.70,'S57'),('× share vs other recurrent-GBM options ★',0.30,'S57')]); SS['SRN-101']=round(v/10)*10
# ---- ramps (S58) : year -> procedures, 100% approval
def ramp(start,steps,ss): 
    d={y:0 for y in YRS}
    for i,y in enumerate(YRS):
        if y>=start: d[y]=steps[y-start] if y-start<len(steps) else ss
    return d
R={'BRT-DA01':ramp(2029,[330,2500,4500],5000),'AMT-130':ramp(2027,[330,2500,3170],3000),
   'AB-1005':ramp(2033,[300,1200],SS['AB-1005']),'ANPD001':ramp(2034,[200,600],SS['ANPD001']),'RNDP-001':ramp(2034,[200,600],SS['RNDP-001']),
   'NRTX-1001':ramp(2030,[300,1200,2200],SS['NRTX-1001']),'AVB-101':ramp(2031,[10,25],SS['AVB-101']),
   'KEBILIDI':ramp(2027,[12],SS['KEBILIDI']),'RGX-121':ramp(2029,[1],SS['RGX-121']),'SRN-101':ramp(2034,[100,300],SS['SRN-101'])}
rev={k:{y:R[k][y]*PRICE for y in YRS} for k in R}
P=[1.0,0.7,0.5,0.3]
tot={p:[sum(rev[k][y]*(1.0 if k=='KEBILIDI' else p) for k in rev) for y in YRS] for p in P}
json.dump({'SS':SS,'funnels':F,'ramps':R,'totals':{str(p):[round(x,1) for x in tot[p]] for p in P},'pd_class':pd_class},open('partners_model.json','w'),indent=1)
plt.figure(figsize=(10,5.6))
for p,c in zip(P,['#0b3d91','#2e7d32','#f9a825','#c62828']):
    plt.plot(YRS,tot[p],marker='o',ms=3.5,lw=2,color=c,label=f'{int(p*100)}% avg. probability of approval')
plt.title('ClearPoint procedure revenue from slide-23 partner therapies (US, $20k per procedure)',fontsize=11)
plt.ylabel('Revenue (US$M)'); plt.xlabel('Fiscal year'); plt.grid(alpha=.3); plt.xticks(YRS,rotation=45); plt.legend(frameon=False)
plt.ylim(0); plt.figtext(0.01,0.01,"Source: ClearPoint 2Q26 corporate presentation slide 23 (D40); partner funnels S50–S58, C37–C53; price $20k [P2]. KEBILIDI (approved Nov 2024) held at 100%.\nUndisclosed Parkinson's (×2) and Friedreich's ataxia programs not quantified. Base-case volumes; scenario, not guidance.",fontsize=7,color='#444')
plt.tight_layout(rect=(0,0.06,1,1)); plt.savefig('partners_revenue_chart.png',dpi=160)
print(SS, round(pd_class)); [print(p,[round(x,1) for x in tot[p]]) for p in P]
