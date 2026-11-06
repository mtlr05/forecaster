"""QURE rev3 quarterly patient model: capacity-limited short term, capacity scales to demand medium term."""
US_POP=340.0
INC={'base':0.48,'bull':1.04}           # per 100k person-yrs, Medina 2022 [A]
HAIR={'base':dict(elig=0.85,will=0.90,cov=0.90),'bull':dict(elig=0.90,will=0.95,cov=0.95)}  # David t55u "exclude a few" [P/S]
BACKLOG0=6000.0
ATTR=0.10   # share of untreated eligible backlog lost per year (progress past early-manifest stage, death) [S]                         # uniQure slide 25 [G]
def refill(n):
    h=HAIR[n]; new=INC[n]/1e5*US_POP*1e6
    return new, new*h['elig']*h['will']*h['cov']
# quarters: index 0 = Q3 2027 (approval 2027-07-01 assumed)
def qname(i):
    y=2027+(i+2)//4; q=(i+2)%4+1; return y,q
CAP={  # rev2b [P5]: ~30 centers able to do 1-2 procedures/week at launch (David, ClearPoint). Weekly throughput per center rises by thr_step/qtr;
       # util = share of that throughput actually used in the first quarters (site activation, surgeon proctoring, referral/prior-auth pipeline) [S];
       # centers grow by step/qtr while a backlog exists, to cmax [S; base 70 = Kapusta pointer, cross-checked HDSA 69 CoE sites and ClearPoint's first 35-40 centers]
 'base':dict(c0=30,step=3,cmax=70,thr0=1.0,thr_step=0.125,thr_max=2.0,util=[0.5,0.67,0.83,1.0]),
 'bull':dict(c0=30,step=5,cmax=100,thr0=1.5,thr_step=0.125,thr_max=2.0,util=[0.67,0.83,1.0]),
}
WEEKS_Q=13.0
# rev3 [P7 David t62u 2026-10-30]: centers do not limit capacity in year one; treated = Kapusta-bot ~190 path (pointer) [S].
Y1={'base':[10,30,60,90],'bull':[15,45,90,135]}   # bull = 1.5x base [S], same uplift as rev2b bull launch throughput (1.5 vs 1.0/center/week)
BRIDGE=4  # year 2 (Q3 2028-Q2 2029): capacity rises linearly from the year-1 exit run-rate to the rev2b engine (30 centers x throughput) [S]
UK=dict(start_q=4,backlog=0.30*7500,pop=69.0,centers=[3,6,9,12,15],thr=13/3.0,price=1.5)  # thr per month = 1/week [S]  # bull only
def run(n,nq=60,delay=0,refill_override=None):
    """delay = quarters of approval slip (sensitivity); refill_override = patients/yr (alternative refill case)."""
    if n=='bear': return []
    c=CAP[n]; _,rf=refill(n)
    if refill_override is not None: rf=refill_override
    q_ref=rf/4
    back=BACKLOG0; rows=[]; cen=0
    ukback=UK['backlog']; h=HAIR['bull']; ukrf=INC['base']/1e5*UK['pop']*1e6*h['elig']*h['will']*h['cov']
    for i in range(nq):
        y,q=qname(i)
        j=i-delay
        if j<0:
            back=(back+q_ref)*(1-ATTR/4)
            rows.append(dict(y=y,q=q,centers=0,thr=0,util=0,cap=0,refill=q_ref,demand=back,treated=0,backlog=back,uk=dict(cap=0,treated=0,back=0))); continue
        k=j-len(Y1[n])                                              # rev3: engine index after year one
        if k<0:                                                     # year one: fixed path, centers not binding [P7]
            thr=0.0; util=0.0; cen=c['c0']/2; cap=float(Y1[n][j])   # cen shown = 15 ClearPoint-qualified (not binding)
        else:
            thr=min(c['thr_max'],c['thr0']+c['thr_step']*k); util=1.0
            if k<BRIDGE:   # year 2 bridge [S]: centers 15 (ClearPoint qualified) -> 30 by Q2 2029 (Kapusta ~30 by end yr2; ClearPoint 20-30 goal; David's 30 at 1-2/wk);
                           # capacity linear from the year-1 exit run-rate to 30 centers x throughput at Q2 2029 (no step)
                cen=c['c0']/2+c['c0']/2*(k+1)/BRIDGE
                tgt=c['c0']*min(c['thr_max'],c['thr0']+c['thr_step']*(BRIDGE-1))*WEEKS_Q
                cap=Y1[n][-1]+(k+1)/BRIDGE*(tgt-Y1[n][-1]); util=cap/(cen*thr*WEEKS_Q)
            else:
                if back>0: cen=min(c['cmax'],cen+c['step'])
                cap=cen*thr*WEEKS_Q
        demand=back+q_ref
        treated=min(cap,demand)
        if back<=1e-6 and k>=BRIDGE:   # backlog gone: network shrinks to what refill needs, but not below the launch network of c0 centers (spare capacity, demand-limited) [S]
            cen_need=q_ref/(thr*WEEKS_Q); cen=min(cen,max(c['c0'],cen_need)); cap=cen*thr*WEEKS_Q; treated=min(cap,demand)
        back=(demand-treated)*(1-ATTR/4)
        if back<1e-6: back=0.0
        uk=dict(cap=0,treated=0,back=0)
        if n=='bull' and i>=UK['start_q']:
            k=min(i-UK['start_q'],len(UK['centers'])-1); ucap=UK['centers'][k]*UK['thr']*3
            ud=ukback+ukrf/4; ut=min(ucap,ud); ukback=(ud-ut)*(1-ATTR/4)
            if ukback<1e-6: ucap=ukrf/4; ut=min(ucap,ud); ukback=0.0
            uk=dict(cap=ucap,treated=ut,back=ukback)
        rows.append(dict(y=y,q=q,centers=cen,thr=thr,util=util,cap=cap,refill=q_ref,demand=demand,treated=treated,backlog=back,uk=uk))
    return rows
def annual(n,years=range(2026,2041),**kw):
    R=run(n,**kw); out={}
    cum=0
    for Y in years:
        rr=[r for r in R if r['y']==Y]
        d=dict(cap=sum(r['cap'] for r in rr),refill=sum(r['refill'] for r in rr),treated=sum(r['treated'] for r in rr),
               backlog_end=rr[-1]['backlog'] if rr else (BACKLOG0 if n!='bear' else 0),centers_end=rr[-1]['centers'] if rr else 0,
               uk_cap=sum(r['uk']['cap'] for r in rr),uk_treated=sum(r['uk']['treated'] for r in rr),uk_back=rr[-1]['uk']['back'] if rr else 0)
        cum+=d['treated']; d['cum']=cum; out[Y]=d
    return out
if __name__=='__main__':
    for n in ['base','bull']:
        print(n,'refill',refill(n))
        for Y,d in annual(n).items(): print(Y,{k:round(v) for k,v in d.items()})
        R=run(n); clr=[r for r in R if r['backlog']<1]; print('clear',clr[0]['y'],clr[0]['q'] if clr else None)
