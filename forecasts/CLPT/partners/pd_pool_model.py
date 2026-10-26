"""US pool for a one-time restorative PD therapy (class level, DBS-style label).
Stage-consistent funnel: medically eligible > referred > willing > covered > treated.
Cohort model (single age at diagnosis x disease duration) gives the SHAPE of the medically eligible stock and its inflow
under published screens; the eligibility LEVEL is an explicit scenario input (point-prevalence share of US PD), applied as a
uniform scale on the published-screen cohort. The downstream product referral x willing x covered (P) is the only calibrated
quantity: P = DBS under cap (FY2019) / eligible inflow (FY2019). Writes pd_pool_model.json."""
import csv, json, math
BASE=dict(
 inc_total=90000,   # A1 US diagnoses/yr
 mr=1.52,           # A5 mortality ratio (Macleod 2014)
 dem_old10=0.46,    # A6 CamPaIGN dementia 46% at 10 yrs, diagnosis age >=65
 dem_young15=0.48,  # A15 Sydney 48% of 15-yr survivors demented, diagnosis age <65
 mc5=0.40,          # A8 motor fluctuations ~40% by 4-6 yrs
 mc15=0.95,         # A15 ~95% at 15 yrs
 dx=0.806,          # A9 levodopa-responsive idiopathic PD share (diagnostic accuracy)
 dis=0.70,          # S1 disabling / not adequately controlled share of motor complications (shape only; level set by elig)
 fit=0.90,          # S2 medically fit (shape only)
 cap=75,            # S3 age cap
 dur_min=4,         # A label: >=4 yrs duration (Medtronic label)
 elig=0.08,         # S8 medically eligible, point prevalence share of all US PD (scenarios 5/8/10/15%)
 dbs=3990,          # A10 PD DBS 2019, NIS inpatient, all ages
 dbs_u=0.85,        # S5 share of DBS patients under the cap
 cal_year=2019,
 kf=0.50,           # S6 yearly draw-down of the backlog above DBS-equivalent capacity after launch
 launch=2029,       # S7
 r=0.55, w=0.60, c=0.90)  # S9-S11 judgment decomposition for comparison only (not used in flows)
HIR={40:(3.26,3.57),50:(10.32,12.58),60:(30.32,58.22),70:(93.32,162.58),80:(103.48,258.47)}   # A3
QX={40:.00238,45:.00306,50:.00408,55:.00601,60:.00913,65:.01332,70:.01884,75:.02882,80:.04841,85:.08222,90:.1443,95:.2396,100:.348,110:0.6}  # A4
PRING={40:41,50:107,60:428,70:1601,80:1903}  # A18 prevalence /100k (70-79 = N America/Europe/Australia)
def qx(a):
    a=min(max(a,40),110); lo=max(x for x in QX if x<=a); hi=min(x for x in QX if x>=a)
    if lo==hi: return QX[lo]
    f=(a-lo)/(hi-lo); return math.exp(math.log(QX[lo])*(1-f)+math.log(QX[hi])*f)
POP={y:{} for y in range(2020,2025)}
for r in csv.DictReader(open('census_nc-est2024-agesex-res.csv')):
    s,a=int(r['SEX']),int(r['AGE'])
    if s in(1,2) and a<=100:
        for y in POP: POP[y][(s,a)]=int(r[f'POPESTIMATE{y}'])
def band10(a): return 80 if a>=80 else (a//10)*10
def raw_inc(y): return {a:sum(POP[y].get((s,a),0)*HIR[band10(a)][1 if s==1 else 0]/1e5 for s in(1,2)) for a in range(40,96)}
R24,R20=raw_inc(2024),raw_inc(2020)
G=(sum(R24.values())/sum(R20.values()))**0.25-1     # C1
BANDS=[(0,50,'<50'),(50,60,'50–59'),(60,65,'60–64'),(65,70,'65–69'),(70,75,'70–74'),(75,80,'75–79'),(80,200,'80+')]
def bname(a): return next(n for lo,hi,n in BANDS if lo<=a<hi)
A0=range(40,96); DMAX=45
INC_SHARE={a:R24[a]/sum(R24.values()) for a in A0}
def cohort(p):
    """published-screen cohort (gap=1). Returns per-year E,N,mu,PD,inc plus exits, lifetime fraction, bands."""
    scale=p['inc_total']/sum(R24.values())
    I=lambda t,a0: R24[a0]*scale*(1+G)**(t-2024)
    hy=1-(1-p['dem_young15'])**(1/15); ho=1-(1-p['dem_old10'])**(1/10)
    h1=1-(1-p['mc5'])**(1/4); h2=1-((1-p['mc15'])/(1-p['mc5']))**(1/10)
    const=p['dis']*p['dx']*p['fit']
    S={};D={};F={}
    for a0 in A0:
        s=1;dd=1
        for d in range(DMAX):
            S[a0,d]=s; D[a0,d]=dd
            s*=1-min(1,p['mr']*qx(a0+d)); dd*=1-(hy if a0<65 else ho)
    f=1.0
    for d in range(DMAX):
        F[d]=1-f
        if d>=1: f*=1-(h1 if d<5 else h2)
    ok=lambda a0,d: a0+d<p['cap'] and d>=p['dur_min']
    def snap(t):
        o=dict(PD=0,cand=0,inc=sum(I(t,a0) for a0 in A0),bands={})
        for a0 in A0:
            for d in range(DMAX):
                n=I(t-d,a0); a=a0+d; b=o['bands'].setdefault(bname(a),dict(PD=0,nodem=0,mc=0,cand=0))
                pd=n*S[a0,d]; b['PD']+=pd; o['PD']+=pd
                if ok(a0,d):
                    nd=pd*D[a0,d]; b['nodem']+=nd; b['mc']+=nd*F[d]; c=nd*F[d]*const; b['cand']+=c; o['cand']+=c
        return o
    def flows(t):
        stay=death=dem=age=0
        for a0 in A0:
            for d in range(1,DMAX):
                if not ok(a0,d-1): continue
                c=I(t-d,a0)*S[a0,d-1]*D[a0,d-1]*F[d-1]*const
                q=min(1,p['mr']*qx(a0+d-1)); hd=(hy if a0<65 else ho)
                death+=c*q
                if ok(a0,d): dem+=c*(1-q)*hd; stay+=c*(1-q)*(1-hd)
                else: age+=c*(1-q)
        return stay,death,dem,age
    # lifetime fraction of an incident cohort (FY2024 age mix) who ever become eligible, and mean years eligible per entrant
    LF=0; YE=0; YD=0
    for a0 in A0:
        w=INC_SHARE[a0]; ent=0; yrs=0
        for d in range(DMAX):
            if ok(a0,d):
                prev = S[a0,d-1]*D[a0,d-1]*F[d-1] if (d>=1 and ok(a0,d-1)) else 0
                surv_prev = prev*(1-min(1,p['mr']*qx(a0+d-1)))*(1-(hy if a0<65 else ho)) if prev else 0
                ent+=max(0,S[a0,d]*D[a0,d]*F[d]-surv_prev)
                yrs+=S[a0,d]*D[a0,d]*F[d]
        LF+=w*ent*const; YE+=w*yrs*const; YD+=w*sum(S[a0,d] for d in range(DMAX))
    Y=list(range(2000,2046)); sn={t:snap(t) for t in Y}; rows=[]
    for t in Y[1:]:
        stay,death,dem,age=flows(t); E=sn[t]['cand']; N=E-stay
        rows.append(dict(t=t,E=E,N=N,mu=(sn[t-1]['cand']-stay)/sn[t-1]['cand'],death=death,dem=dem,age=age,PD=sn[t]['PD'],inc=sn[t]['inc']))
    return dict(rows=rows,snaps={str(t):sn[t] for t in(2019,2026,2030,2045)},E2000=sn[2000]['cand'],LF=LF,YE_entrant=YE/LF,YD=YD,
                hz=dict(hy=hy,ho=ho,h1=h1,h2=h2),const=const,share=sn[2026]['cand']/sn[2026]['PD'])
def run(p,C=None):
    C=C or cohort(p); g=p['elig']/C['share']; R={x['t']:x for x in C['rows']}
    du=p['dbs']*p['dbs_u']; P=p.get('P_fix') or du/(g*R[p['cal_year']]['N'])
    W={'A':0.0,'B':0.0}; W0=P*g*C['E2000']*0  # start 2000 with no backlog (DBS absorbed funnel)
    out=[]
    for x in C['rows']:
        t=x['t']; N=g*x['N']; mu=x['mu']; r=dict(t=t,E=g*x['E'],N=N,mu=mu,death=g*x['death'],dem=g*x['dem'],age=g*x['age'],PD=x['PD'],inc=x['inc'],fN=P*N)
        for k in 'AB':
            Wa=W[k]*(1-mu)+P*N; base=min(du,Wa)
            if t<p['launch']: dbs=base; one=0
            elif k=='A': dbs=base; one=p['kf']*(Wa-base)
            else: dbs=0; one=base+p['kf']*(Wa-base)
            W[k]=Wa-dbs-one
            r.update({f'Wa_{k}':Wa,f'dbs_{k}':dbs,f'one_{k}':one,f'W_{k}':W[k],f'rev_{k}':one*0.02})
        out.append(r)
    RR={x['t']:x for x in out}; L=RR[2045]
    return dict(rows=out,P=P,g=g,du=du,LF=C['LF']*g,share_pub=C['share'],
        conv_k1=L['fN'], conv_kf=None, cand26=RR[2026]['E'], N26=RR[2026]['N'])
YRS=[2029,2030,2032,2035,2040,2045]
def met(p,C=None):
    o=run(p,C); R={x['t']:x for x in o['rows']}
    m=dict(P=o['P'],LF=o['LF'],cand26=o['cand26'],N26=o['N26'])
    for y in YRS: m[f'A{y}']=R[y]['one_A']; m[f'B{y}']=R[y]['one_B']
    return m
if __name__=='__main__':
    p=dict(BASE); C=cohort(p)
    print('pub share',round(C['share'],4),'LF_pub',round(C['LF'],4),'YE',round(C['YE_entrant'],2),'YD',round(C['YD'],2),'G',round(G,4))
    SC={'5%':0.05,'8%':0.08,'10%':0.10,'15%':0.15}; scen={}
    for nm,s in SC.items():
        q=dict(p,elig=s); o=run(q,C); k1=run(dict(q,kf=1.0),C)
        scen[nm]=dict(elig=s,out=o,k1=k1['rows'],met=met(q,C),
            fixP=met(dict(q,P_fix=q['r']*q['w']*q['c']),C),dbs_tests={str(T):met(dict(q,dbs_u=T/p['dbs']),C)['P'] for T in (3400,3990,4500)})
        m=scen[nm]['met']; print(nm,'P',round(m['P'],3),'LF',round(m['LF'],3),'cand',round(m['cand26']),'N',round(m['N26']),{y:(round(m[f'A{y}']),round(m[f'B{y}'])) for y in YRS},{k:round(v,3) for k,v in scen[nm]['dbs_tests'].items()})
    # tornado on central 8%
    TOR=[('Eligibility share (5% / 15%)','elig',0.05,0.15,False),('DBS under-cap target, FY2019 (3.0k / 4.5k)','dbs_u',0.75,4500/3990,False),
         ('Backlog draw-down after launch (25% / 100%)','kf',0.25,1.0,False),('Launch year (FY2031 / FY2028)','launch',2031,2028,False),
         ('Age cap, shape only (70 / 80)','cap',70,80,True),('Mortality ratio (1.86 / 1.29)','mr',1.86,1.29,True),
         ('Disease duration floor (5 / 0 yrs)','dur_min',5,0,True)]
    base=met(p,C); tor=[]
    for lab,k,lo,hi,rec in TOR:
        f=lambda v: met(dict(p,**{k:v}), None if rec else C)
        tor.append(dict(label=lab,key=k,lo_v=lo,hi_v=hi,lo=f(lo),hi=f(hi)))
        print(lab,round(tor[-1]['lo']['B2040']),round(tor[-1]['hi']['B2040']),round(tor[-1]['lo']['A2040']),round(tor[-1]['hi']['A2040']),round(tor[-1]['lo']['P'],3),round(tor[-1]['hi']['P'],3))
    # Olmsted reconciliation: lifetime eligible = ever-DBS / product
    olm={str(Pv):0.048/Pv for Pv in (0.10,0.15,0.20,0.25,0.30,0.40,0.50,0.65)}
    # model ever-DBS fraction of incidence (DBS under cap / incidence, FY2019)
    R19={x['t']:x for x in C['rows']}[2019]
    json.dump(dict(inputs=p,G=G,cohort=dict(share=C['share'],LF=C['LF'],YE=C['YE_entrant'],YD=C['YD'],hz=C['hz'],const=C['const'],E2000=C['E2000'],
        rows=C['rows'],snaps=C['snaps']),scen={k:dict(elig=v['elig'],rows=v['out']['rows'],P=v['out']['P'],g=v['out']['g'],LF=v['out']['LF'],k1=v['k1'],met=v['met'],fixP=v['fixP'],dbs_tests=v['dbs_tests']) for k,v in scen.items()},
        tornado=tor,tornado_base=base,olmsted=olm,dbs_over_inc19=p['dbs']*p['dbs_u']/R19['inc'],inc19=R19['inc'],
        HIR=HIR,QX=QX,PRING=PRING),open('pd_pool_model.json','w'),indent=1)
