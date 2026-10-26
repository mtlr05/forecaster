"""Builds pd_pool_model.xlsx from pd_pool_model.json. Cohort values come from the Python cohort model; every scaling,
calibration and flow step is a live formula. Yellow cells are inputs."""
import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L
d=json.load(open('pd_pool_model.json')); p=d['inputs']; co=d['cohort']
wb=Workbook(); B=Font(bold=True); INP=PatternFill('solid',fgColor='FFF2CC'); HDR=PatternFill('solid',fgColor='DDEBF7')
def hdr(ws,row,vals):
    for i,v in enumerate(vals,1): c=ws.cell(row,i,v); c.font=B; c.fill=HDR; c.alignment=Alignment(wrap_text=True,vertical='top')
ws=wb.active; ws.title='Inputs'
hdr(ws,1,['Key','Input','Value','Unit','Tag','Source / note','Link'])
INPUTS=[
 ('inc','US PD diagnoses per year (FY2024)',p['inc_total'],'patients','A1',"Parkinson's Foundation",'https://www.parkinson.org/understanding-parkinsons/statistics/prevalence-incidence'),
 ('mr','Mortality ratio vs general population',p['mr'],'x','A5','Macleod 2014','https://doi.org/10.1002/mds.25898'),
 ('demo','Dementia at 10 yrs, diagnosis age ≥65',p['dem_old10'],'share','A6','CamPaIGN, Williams-Gray 2013','https://doi.org/10.1136/jnnp-2013-305277'),
 ('demy','Dementia among 15-yr survivors, diagnosis age <65',p['dem_young15'],'share','A15','Sydney, Hely 2005','https://doi.org/10.1002/mds.20324'),
 ('mc5','Motor fluctuations by 4–6 yrs levodopa',p['mc5'],'share','A7','Ahlskog & Muenter 2001','https://doi.org/10.1002/mds.1090'),
 ('mc15','Motor complications at 15 yrs',p['mc15'],'share','A15','Hely 2005','https://doi.org/10.1002/mds.20324'),
 ('dx','Levodopa-responsive idiopathic PD',p['dx'],'share','A9','Rizzo 2016','https://doi.org/10.1212/WNL.0000000000002350'),
 ('dur','Minimum disease duration',p['dur_min'],'years','A','Medtronic label, P960009/S478','https://www.accessdata.fda.gov/cdrh_docs/pdf/P960009S478B.pdf'),
 ('dis','Not adequately controlled share of motor complications (shape only)',p['dis'],'share','S1 ★','Sets cohort shape; level is set by eligibility scenario',''),
 ('fit','Medically fit (shape only)',p['fit'],'share','S2 ★','As above',''),
 ('cap','Upper age cap',p['cap'],'years','S3 ★','Label has no cap; practice ~70–75',''),
 ('dbs','PD DBS per year, 2019',p['dbs'],'procedures','A10','NIS 2019 weighted inpatient discharges, PD diagnosis, all ages (Venkatraman 2024, Table 1)','https://pmc.ncbi.nlm.nih.gov/articles/PMC10898494/'),
 ('dbsu','DBS share under the age cap',p['dbs_u'],'share','S5 ★','Range 75–95%; outpatient uplift tested via this cell (4.5k ⇒ 1.128)',''),
 ('caly','Calibration year',p['cal_year'],'FY','A10','Year of the DBS count',''),
 ('kf','Backlog draw-down per year after launch',p['kf'],'share','S6 ★','Range 25–100%',''),
 ('launch','First one-time therapy launch',p['launch'],'FY','S7 ★','',''),
 ('price','Revenue per procedure',0.02,'US$M','P','David May: $20k',''),
 ('r','Referral / evaluation (judgment, comparison only)',p['r'],'share','S9 ★','Range 30–80% (Part 3 notes)',''),
 ('w','Willing among referred (judgment, comparison only)',p['w'],'share','S10 ★','Range 40–85%; 35–43% published is consent-to-referral (A11, A12); 58.7% of fully evaluated implanted (A21)','https://pmc.ncbi.nlm.nih.gov/articles/PMC6183455/'),
 ('c','Covered (judgment, comparison only)',p['c'],'share','S4 ★','Range 80–95%',''),
 ('olm','Ever-DBS share of incident PD, Olmsted County',0.048,'share','A8','16% fluctuations × 29% DBS (Stang 2021, AAN abstract); product is a calculation','https://doi.org/10.1212/WNL.96.15_supplement.4377'),
]
REF={}
for i,(k,n,v,u,tag,src,link) in enumerate(INPUTS,2):
    ws.cell(i,1,k); ws.cell(i,2,n); c=ws.cell(i,3,v); c.fill=INP; ws.cell(i,4,u); ws.cell(i,5,tag); ws.cell(i,6,src); ws.cell(i,7,link); REF[k]=f"Inputs!$C${i}"
# Cohort
wc_=wb.create_sheet('Cohort')
wc_.cell(1,1,'Published-screen cohort (pd_pool_model.py). Eligible = alive, no dementia, under cap, ≥4 yrs, with motor complications × dx × S1 × S2.').font=B
hdr(wc_,2,['FY','Eligible stock (published screens)','Newly eligible','Exit rate μ','Deaths','Dementia','Aged past cap','PD prevalent','PD incidence'])
CR={}
for i,x in enumerate(co['rows'],3):
    for j,k in enumerate(['t','E','N','mu','death','dem','age','PD','inc'],1): wc_.cell(i,j,x[k])
    CR[x['t']]=i
for col in 'ABCDEFGHI': wc_.column_dimensions[col].width=15
r=len(INPUTS)+3; ws.cell(r,2,'Derived (live)').font=B
D=[('du','DBS under cap per year',f"={REF['dbs']}*{REF['dbsu']}",'C'),
   ('spub','Published-screen eligible share of PD, FY2026',f"=Cohort!B{CR[2026]}/Cohort!H{CR[2026]}",'C'),
   ('Ncal','Published-screen newly eligible in calibration year',f"=INDEX(Cohort!C:C,MATCH({REF['caly']},Cohort!A:A,0))",'C'),
   ('LFpub','Lifetime fraction ever eligible, published screens',co['LF'],'C (cohort)'),
   ('YE','Mean years eligible per entrant',co['YE'],'C (cohort)'),
   ('YD','Mean survival from diagnosis (yrs)',co['YD'],'C (cohort)'),
   ('rwc','Judgment product r×w×c',f"={REF['r']}*{REF['w']}*{REF['c']}",'C'),
   ('E2000','Published-screen eligible stock FY2000',co['E2000'],'C'),
   ('G','Incidence growth (Census 2020–24, age-weighted)',d['G'],'C1')]
for j,(k,n,f,tag) in enumerate(D,r+1):
    ws.cell(j,1,k); ws.cell(j,2,n); ws.cell(j,3,f); ws.cell(j,5,tag); REF[k]=f"Inputs!$C${j}"
rr=r+len(D)+2; ws.cell(rr,2,'Other published inputs used in the cohort model').font=B; rr+=1
for a,(f_,m) in d['HIR'].items(): ws.cell(rr,2,f'Hirsch 2016 incidence /100k, age {a}s (F, M)'); ws.cell(rr,3,f_); ws.cell(rr,4,m); ws.cell(rr,5,'A3'); ws.cell(rr,7,'https://doi.org/10.1159/000445751'); rr+=1
for a,v in d['QX'].items(): ws.cell(rr,2,f'SSA 2023 qx, age {a}'); ws.cell(rr,3,v); ws.cell(rr,5,'A4'); ws.cell(rr,7,'https://www.ssa.gov/oact/STATS/table4c6.html'); rr+=1
for col,w in zip('ABCDEFG',[8,55,12,10,9,70,55]): ws.column_dimensions[col].width=w
# Scenarios
sc=wb.create_sheet('Scenarios'); NAMES=['5%','8%','10%','15%']
sc.cell(1,1,'Eligibility scenarios (point prevalence of US PD meeting label-style criteria, cap 75). Product P = r×w×c is calibrated so DBS under cap = FY2019 volume. Central = 8% (★).').font=B
hdr(sc,2,['Row','Measure']+[f'Case {n}' for n in NAMES]+['Note'])
lab=['Eligible, point prevalence (input)','Scale on published screens g','Calibrated product P = r×w×c','Lifetime fraction ever eligible','Implied s ≈ LF × YE / YD (check)',
     'Eligible stock FY2026','Newly eligible FY2026','Olmsted-implied lifetime eligible = 4.8% ÷ P','Model ever-DBS share of incidence = LF × P','Judgment product r×w×c','DBS FY2019 implied at judgment product','Plausibility (P within 0.10–0.65; central 0.30)']
SR={}
for i,l in enumerate(lab,3): sc.cell(i,1,i); sc.cell(i,2,l)
for j,nm in enumerate(NAMES,3):
    c=L(j); v=d['scen'][nm]['elig']; x=sc.cell(3,j,v); x.fill=INP
    sc.cell(4,j,f"={c}3/{REF['spub']}"); sc.cell(5,j,f"={REF['du']}/({c}4*{REF['Ncal']})"); sc.cell(6,j,f"={REF['LFpub']}*{c}4")
    sc.cell(7,j,f"={c}6*{REF['YE']}/{REF['YD']}"); sc.cell(8,j,f"={c}4*Cohort!B{CR[2026]}"); sc.cell(9,j,f"={c}4*Cohort!C{CR[2026]}")
    sc.cell(10,j,f"={REF['olm']}/{c}5"); sc.cell(11,j,f"={c}6*{c}5"); sc.cell(12,j,f"={REF['rwc']}"); sc.cell(13,j,f"={REF['rwc']}*{c}4*{REF['Ncal']}")
    sc.cell(14,j,f'=IF(OR({c}5>0.65,{c}5<0.1),"implausible",IF(OR({c}5>0.45,{c}5<0.18),"edge of range","plausible"))')
    SR[nm]=dict(g=f"Scenarios!${c}$4",P=f"Scenarios!${c}$5")
sc.cell(5,7,'Only calibrated quantity'); sc.cell(7,7,'Differs from row 3 by growth and age mix'); sc.cell(11,7,'Same for every case: it is pinned by DBS volume ÷ incidence')
for col,w in zip('ABCDEFG',[5,52,13,13,13,13,50]): sc.column_dimensions[col].width=w
# Flows
FR={}
for nm in NAMES:
    w=wb.create_sheet(f'Flow {nm}'); g,P=SR[nm]['g'],SR[nm]['P']
    w.cell(1,1,f'Eligibility case {nm}. Eligible = Cohort × g; funnel inflow = newly eligible × P. Pre-launch DBS = MIN(DBS under cap, pool). After launch: A keeps DBS and the one-time therapy draws kf of the backlog; B replaces DBS (DBS-equivalent volume + kf of backlog). Rows before FY2026 grouped.').font=B
    H=['FY','Eligible stock','Newly eligible','Exit μ','Deaths','Dementia','Aged past cap','Funnel inflow (×P)',
       'A: pool available','A: DBS','A: one-time','A: backlog end','A: $M','B: pool available','B: DBS','B: one-time','B: backlog end','B: $M','PD prevalent','Eligible % of PD']
    hdr(w,2,H); fr={}
    r0=3; w.cell(r0,1,2000); w.cell(r0,12,0); w.cell(r0,17,0)
    for k,x in enumerate(co['rows']):
        r=r0+1+k; c=CR[x['t']]; fr[x['t']]=r
        w.cell(r,1,x['t'])
        for col,src in ((2,'B'),(3,'C'),(5,'E'),(6,'F'),(7,'G')): w.cell(r,col,f"=Cohort!{src}{c}*{g}")
        w.cell(r,4,f"=Cohort!D{c}"); w.cell(r,8,f"=C{r}*{P}")
        w.cell(r,9,f"=L{r-1}*(1-D{r})+H{r}"); w.cell(r,10,f"=MIN({REF['du']},I{r})")
        w.cell(r,11,f"=IF(A{r}<{REF['launch']},0,{REF['kf']}*(I{r}-J{r}))"); w.cell(r,12,f"=I{r}-J{r}-K{r}"); w.cell(r,13,f"=K{r}*{REF['price']}")
        w.cell(r,14,f"=Q{r-1}*(1-D{r})+H{r}"); w.cell(r,15,f"=IF(A{r}<{REF['launch']},MIN({REF['du']},N{r}),0)")
        w.cell(r,16,f"=IF(A{r}<{REF['launch']},0,MIN({REF['du']},N{r})+{REF['kf']}*(N{r}-MIN({REF['du']},N{r})))")
        w.cell(r,17,f"=N{r}-O{r}-P{r}"); w.cell(r,18,f"=P{r}*{REF['price']}"); w.cell(r,19,f"=Cohort!H{c}"); w.cell(r,20,f"=B{r}/S{r}")
        if x['t']<2026: w.row_dimensions[r].outlineLevel=1; w.row_dimensions[r].hidden=True
    for j in range(1,21): w.column_dimensions[L(j)].width=12
    w.freeze_panes='B3'; FR[nm]=fr
# Summary
sm=wb.create_sheet('Summary',1)
sm.cell(1,1,"Class demand for a one-time therapy, patients ('A' DBS keeps volume / 'B' replaces DBS) and $M at $20k").font=B
YRS=[2029,2030,2032,2035,2040,2045]
hdr(sm,2,['Case','Measure']+[f'FY{y}' for y in YRS]); i=3
for nm in NAMES:
    for lbl,col in (('A: one-time','K'),('B: one-time','P'),('A: $M','M'),('B: $M','R')):
        sm.cell(i,1,nm); sm.cell(i,2,lbl)
        for j,y in enumerate(YRS,3): sm.cell(i,j,f"='Flow {nm}'!{col}{FR[nm][y]}")
        i+=1
i+=1; sm.cell(i,1,'Convergence (central 8%)').font=B; i+=1
sm.cell(i,2,'FY2045 funnel inflow = newly eligible × P (B demand → this as kf → 1)'); sm.cell(i,3,f"='Flow 8%'!H{FR['8%'][2045]}"); i+=1
sm.cell(i,2,'FY2045 B demand at base kf'); sm.cell(i,3,f"='Flow 8%'!P{FR['8%'][2045]}"); i+=1
sm.cell(i,2,'Ratio'); sm.cell(i,3,f"=C{i-1}/C{i-2}"); i+=1
sm.cell(i,2,'kf=1 run, FY2045 B demand (from pd_pool_model.py; set Inputs kf=1 to reproduce live)'); sm.cell(i,3,{r['t']:r for r in d['scen']['8%']['k1']}[2045]['one_B'])
sm.column_dimensions['A'].width=8; sm.column_dimensions['B'].width=70
for col in 'CDEFGH': sm.column_dimensions[col].width=12
# Age-band funnel (central)
wf=wb.create_sheet('Age-band funnel')
wf.cell(1,1,'FY2026 by age band, central 8% case. B–D from the cohort model; E onward live.').font=B
hdr(wf,2,['Age band','PD prevalent','Alive, no dementia, under cap, ≥4 yrs','… with motor complications','Eligible, published screens (× dx × S1 × S2)','Eligible, central (× g)','Funnel (× P)','Eligible % of band PD'])
bands=co['snaps']['2026']['bands']; i=3
for bnm in ['<50','50–59','60–64','65–69','70–74','75–79','80+']:
    b=bands[bnm]; wf.cell(i,1,bnm); wf.cell(i,2,b['PD']); wf.cell(i,3,b['nodem']); wf.cell(i,4,b['mc'])
    wf.cell(i,5,f"=D{i}*{REF['dx']}*{REF['dis']}*{REF['fit']}"); wf.cell(i,6,f"=E{i}*{SR['8%']['g']}"); wf.cell(i,7,f"=F{i}*{SR['8%']['P']}"); wf.cell(i,8,f"=IF(B{i}>0,F{i}/B{i},0)"); i+=1
wf.cell(i,1,'Total').font=B
for j in range(2,8): wf.cell(i,j,f"=SUM({L(j)}3:{L(j)}{i-1})")
wf.cell(i,8,f"=F{i}/B{i}"); FT=i
for col in 'ABCDEFGH': wf.column_dimensions[col].width=17
# Sensitivity
wsn=wb.create_sheet('Sensitivity')
wsn.cell(1,1,'One-at-a-time sensitivity, central 8% case (values from pd_pool_model.py). FY2040 class one-time demand, patients; P = calibrated product.').font=B
hdr(wsn,2,['Input','First value','Second value','A first','A second','B first','B second','P first','P second']); i=3
tb=d['tornado_base']; wsn.cell(i,1,'Base'); wsn.cell(i,4,tb['A2040']); wsn.cell(i,6,tb['B2040']); wsn.cell(i,8,tb['P']); i+=1
for x in d['tornado']:
    for j,v in enumerate([x['label'],x['lo_v'],x['hi_v'],x['lo']['A2040'],x['hi']['A2040'],x['lo']['B2040'],x['hi']['B2040'],x['lo']['P'],x['hi']['P']],1): wsn.cell(i,j,v)
    i+=1
wsn.column_dimensions['A'].width=50
# Calibration checks
cal=wb.create_sheet('Checks')
hdr(cal,1,['Check','Target / published','Model','Note'])
rows=[('PD prevalent 2020',930000,f"=Cohort!H{CR[2020]}",'Marras 2018 minimum [A19]'),('PD prevalent 2030',1238000,f"=Cohort!H{CR[2030]}",'Marras 2018 [A19]'),
 ('DBS under cap FY2019 vs central A: DBS',f"={REF['du']}",f"='Flow 8%'!J{FR['8%'][2019]}",'Calibration identity'),
 ('Funnel inflow FY2019 (central)',f"={REF['du']}",f"='Flow 8%'!H{FR['8%'][2019]}",'Equals DBS under cap by construction'),
 ('Ever-DBS share of incidence',f"={REF['olm']}",'=Scenarios!D11','Olmsted 4.8% all ages vs model under cap'),
 ('Central eligible % of PD FY2026','=Scenarios!D3',f"='Age-band funnel'!H{FT}",'Should match')]
for i,rw in enumerate(rows,2):
    for j,v in enumerate(rw,1): cal.cell(i,j,v)
cal.column_dimensions['A'].width=45; cal.column_dimensions['D'].width=50
wb.save('pd_pool_model.xlsx')
json.dump(dict(FR=FR,FT=FT,CR=CR),open('/tmp/xlsx_map.json','w')); print('saved')
