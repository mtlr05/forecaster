"""Apply the approved v4 robotics deltas to baseline_v3.json.

This is not a from-scratch forecast. It reads the retained v3 case beside this
file, allocates the Monogram and Helios amounts inside the existing consensus
totals, and writes forecast.json, robotics_model.csv and model_results.json in
the same directory. It does not set terminal growth. Rerunning replaces those
three outputs; it does not rewrite report.md or report.pdf.
"""
from pathlib import Path
import json,copy,csv
HERE = Path(__file__).resolve().parent
H = HERE
B = HERE
old=json.loads((B/'baseline_v3.json').read_text());p=copy.deepcopy(old);years=p['explicit_periods'];sources={s['id']:s for s in p['sources']}
def src(id,text,doc='D2',page='page unverified',inputs=None):
 s={'id':id,'text':text,'document':doc,'page':page}
 if inputs:s['inputs']=inputs
 sources[id]=s
src('D27','MAKO Surgical, FY2012 results, February 26, 2013: https://www.sec.gov/Archives/edgar/data/1411861/000089710113000244/mako130813_ex99-1.htm')
src('D28','Pro-Dex APM leases 8-K, October 30, 2026: https://www.sec.gov/Archives/edgar/data/788920/000107997326001415/pdex_8k.htm')
src('D29','SEC submissions, checked November 7, 2026; latest filing October30: https://data.sec.gov/submissions/CIK0000788920.json')
src('G20','"The average monthly utilization per system was 6.6 procedures during the fourth quarter of 2012"; "A total of 45 new RIO systems were sold worldwide in 2012". February26,2013. Historical analog, not Monogram guidance.','D27','Recent Business Developments')
src('A43','"next largest customer accounting for 8% of sales" FY26; "75% and 12%, respectively" FY25. Rounded percentages, not exact customer dollars.','D1','p.2')
src('A44','Customer 2: 2,487 thousand (12%) in quarter ended September30,2026; 1,091 thousand in prior-year quarter.','D2','Note10')
src('G21','"The base rent from November 1, 2026 through February 29, 2028 is $11,600 per month", then "$12,064" from March1,2028.','D28','Item1.01')
def stream_total(begin,n,prob,val,price,eng,rate,basket,util,stock,i):
 added=n*prob;spares=begin*4*.05;units=val+added*4+spares;hw=units*price/1e6
 active=added/8 if i==0 else begin+added/2;purchase=active*util*stock*basket/1e6
 return added,eng+hw+purchase*rate
def solve_n(begin,prob,price,eng,rate,basket,util,stock,target):
 lo,hi=1,64
 while stream_total(begin,hi,prob,0,price,eng,rate,basket,util,stock,1)[1]<target:hi*=2
 while lo<hi:
  mid=(lo+hi)//2
  if stream_total(begin,mid,prob,0,price,eng,rate,basket,util,stock,1)[1]>=target:hi=mid
  else:lo=mid+1
 return lo
base_target=77.548*.08;bull_target=2.487*4
base_n28=solve_n(10*.4,.7,6000,.10,.05,300,120,1.15,base_target)
bull_n28=solve_n(25,1,7500,.15,.08,500,180,1.2,bull_target)
src('S23',f'Monogram timing/volume. FY27 validation 0/10/10 and conditional commercial systems 0/10/25 stay the validation year. FY28 conditional systems are solved so Monogram revenue reaches the second-customer band: base {base_n28} at 70% realization, target 77.548*8%; bull {bull_n28} at 100%, target 2.487*4. The old 120/200 plans were not a company cap. Realization 40%/70% base and 100% bull; low commercial systems remain 0. FY27 active system-years = expected new systems /8; FY28 = prior expected systems + half current additions. Central 120 cases per active system-year; high 180.','D22')
src('S24','Hardware cost/price judgments: low materials1600 +8h*60 +overhead545 =2625 cost, price3500, GM25%; central materials2500 +10h*70 +overhead850 ~4050, rounded price6000 and TTM32.4516% GM; high materials3000 +12h*75 +overhead975 =4875, price7500, GM35%. Each priced kit includes one end effector plus gearing; 4 per new robot (one in use, backup/sterilization rotation), not a disclosed specification. Spares 5% of beginning installed fleet kits, no replacements of current-year kits, no repair revenue inside window. All prices and staffing are analyst estimates, not recovered redactions.','D25')
src('S25','Fee judgments: central eligible burr/blade purchases300 dollars per case-equivalent, rate5%; high500 and8%; low no commercial launch. Purchases/use inventory factor1.30FY27,1.15FY28 central /1.20FY28 high. Exclude standard Persona implants (not patient-specific custom implants), robotic arms, navigation cameras, drapes, taxes, freight, packaging. Fee GP95%, incremental EBITDA85% before shared launch support: allow5% direct processing and10% admin expense. Rates and basket costs unobservable; range is scenario judgment, not a statistical interval.','D25')
src('S26','Engineering revenue included within original NRE budget, not added twice: low0.05/0.05, central0.15/0.10, high0.20/0.15 US$M FY27/FY28; central FY27 about1000billable hours at150 dollars/hour, FY28 roughlytwo-thirds that workload as setup ends. GM25%/35%/40% low/central/high. Incremental shared launch support beyond current run rate0.04/0.06 low,0.04/0.10 central,0.10/0.25 high US$M. Covers QA/customer support/engineering contingency; permanent existing staff retained. No additional D&A assumed within existing capacity; risk if tooling/capex expands.','D18')
src('S27','Helios separated: central0.15/0.45 US$M already allocated within CMF line run-rate/growth (illustratively50/150 drivers at3000 each); high0.25/0.50; low0/0. No author50–65% GM adopted; apply respective case core margins. Label/software engineering remains in existing NRE, no second setup-fee uplift. Product released, no disclosed orders: sizing is modest channel trial judgment.','D21')
src('S28','Retain consensus base82.7/86.8, unknown product coverage; Monogram/Helios are explicit allocations inside total. Replace old bull0.5/1.0 combined allowance, do not stack. Bull/bear differences = unchanged core volume/repair shocks plus pipeline HIGH/LOW minus CENTRAL already in base. Acquired industrial line unscaled. Scale residual non-APM core only to preserve modeled pipeline amounts.','D13')
src('S29','FY28 explicit stop retained. Base and bull FY28 Monogram are the second-customer band, not a cross-check. The medium-term organic growth forecast keeps each other line on its own trajectory and adds one more year of the FY28 system cohort. Bear gsnext is the customer-1 renewal. mc stays 25% because the cohort is mostly hardware and the continuing lines are ordinary core business.','D22')
sources['S13']['text']='mc stays 25% in every case. The rank path is mostly hardware at an ordinary gross margin, so the fee stream does not reprice the company-wide contribution margin. See S29.'
sources['S15']['text']='Bull: core medical devices +1/+1 and repairs +0.5/+0.5 US$M vs base; core GM33.5%; replace embedded central Monogram/Helios with explicit high path, not old combined NRE allowance. See S23-S28.'
sources['S16']['text']='Bear: core medical devices -3/-8 and repairs -1/-1.5 US$M vs base; core GM31%; replace embedded central Monogram/Helios with low/delayed path. See S23-S28.'
sources['S6']['text']='Original unscaled NRE1.2 retained; contains central Monogram engineering0.15 FY27 and0.10 FY28 as an allocation. Validation hardware is in medical devices. See S26.'
sources['S3']['text'] += ' Clarification: 3% applies to total medical-device revenue; the dollar increase is attributed to CMF, not a claim that CMF itself grows only3%.'
newid=93
URL='https://www.sec.gov/Archives/edgar/data/1769759/000110465923107518/tm2328000d1_ex10-1.htm'
def fact(v,text,inputs=('S23','S24','S25','S26','S27','S28')):
 global newid
 id='C'+str(newid);newid+=1;src(id,text,inputs=list(inputs));return {'value':round(v,9),'tag':'C','citation':{'id':id,'text':text,'url':URL,'page_status':'unverified'}}
def setval(f,v,text=None,inputs=None):
 f['value']=round(v,9);id=f['citation']['id']
 if text:f['citation']['text']=text;sources[id]['text']=text
 if inputs:sources[id]['inputs']=inputs
model={};raw={};csvrows=[]
for case in ['bear','base','bull']:
 begin=0;rows={}
 for i,y in enumerate(years):
  if case=='base': n=[10,base_n28][i];prob=[.4,.7][i];val=[10,0][i];price=6000;cg=.324516;eng=[.15,.10][i];eg=.35;rate=.05;basket=300;util=120;stock=[1.3,1.15][i];support=[.04,.1][i];helios=[.15,.45][i]
  elif case=='bull':n=[25,bull_n28][i];prob=1;val=[10,0][i];price=7500;cg=.35;eng=[.2,.15][i];eg=.4;rate=.08;basket=500;util=180;stock=[1.3,1.2][i];support=[.1,.25][i];helios=[.25,.5][i]
  else:n=0;prob=0;val=[0,10][i];price=3500;cg=.25;eng=.05;eg=.25;rate=.02;basket=150;util=60;stock=1.3;support=[.04,.06][i];helios=0
  added=n*prob;spares=begin*4*.05;units=val+added*4+spares;hw=units*price/1e6;active=added/8 if i==0 else begin+added/2;cases=active*util;purchase=cases*stock*basket/1e6;fee=purchase*rate;gp=hw*cg+eng*eg+fee*.95;eb=gp-fee*.10-support
  r=dict(conditional_new_systems=n,shipment_realization=prob,expected_new_systems=added,begin_systems=begin,validation_units=val,units_per_new_system=4,spare_units=spares,total_kit_units=units,kit_price_USD=price,hardware_gross_margin=cg,active_system_years=active,procedures_per_system_year=util,procedure_equivalents=cases,purchase_inventory_factor=stock,eligible_basket_USD=basket,fee_rate=rate,eligible_purchases_M=purchase,engineering_revenue_M=eng,engineering_gross_margin=eg,hardware_revenue_M=hw,fee_revenue_M=fee,fee_gross_margin=.95,fee_ebitda_margin=.85,total_monogram_revenue_M=eng+hw+fee,gross_profit_M=gp,fee_admin_M=fee*.1,shared_launch_support_M=support,incremental_ebitda_M=eb,helios_revenue_M=helios)
  rows[y]=r;begin+=added;csvrows.append({'case':case,'year':y,**r})
  assumptions={'conditional_new_systems':'S23','shipment_realization':'S23','validation_units':'S23','units_per_new_system':'S24','kit_price_USD':'S24','hardware_gross_margin':'S24','procedures_per_system_year':'S23','purchase_inventory_factor':'S25','eligible_basket_USD':'S25','fee_rate':'S25','engineering_revenue_M':'S26','engineering_gross_margin':'S26','fee_gross_margin':'S25','fee_ebitda_margin':'S25','shared_launch_support_M':'S26','helios_revenue_M':'S27'}
  rowfacts={}
  for k,v in r.items():
   f=fact(v,f'{case} {y}: {k}; calculation in robotics_model.csv / build_v4.py.')
   if k in assumptions:
    oldid=f['citation']['id'];sid='S'+str(30+len([x for x in sources if x.startswith('S') and int(x[1:])>=30]));sources.pop(oldid)
    reason=assumptions[k];src(sid,f'{case} {y}: {k} = {v}. Analyst judgment, not disclosed contract terms; rationale and bounds in {reason}.',sources[reason]['document']);f['tag']='S';f['citation']['id']=sid
   rowfacts[k]=f
  dep={'expected_new_systems':['conditional_new_systems','shipment_realization'],'spare_units':['begin_systems','units_per_new_system'],'total_kit_units':['validation_units','expected_new_systems','units_per_new_system','spare_units'],'active_system_years':['begin_systems','expected_new_systems'],'procedure_equivalents':['active_system_years','procedures_per_system_year'],'eligible_purchases_M':['procedure_equivalents','purchase_inventory_factor','eligible_basket_USD'],'hardware_revenue_M':['total_kit_units','kit_price_USD'],'fee_revenue_M':['eligible_purchases_M','fee_rate'],'total_monogram_revenue_M':['engineering_revenue_M','hardware_revenue_M','fee_revenue_M'],'gross_profit_M':['hardware_revenue_M','hardware_gross_margin','engineering_revenue_M','engineering_gross_margin','fee_revenue_M','fee_gross_margin'],'fee_admin_M':['fee_revenue_M','fee_gross_margin','fee_ebitda_margin'],'incremental_ebitda_M':['gross_profit_M','fee_admin_M','shared_launch_support_M']}
  for k,keys in dep.items():sources[rowfacts[k]['citation']['id']]['inputs']=[rowfacts[q]['citation']['id'] for q in keys]
  model.setdefault(case,{})[y]=rowfacts
 raw[case]=rows
with (H/'robotics_model.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=csvrows[0].keys());w.writeheader();w.writerows(csvrows)
p['robotics']=model
p['robotics_checks']={
 'customer2_FY26_approx':fact(77.548*.08,'FY26 customer2 approximate = FY26 sales77.548M * rounded8% share; not exact dollar disclosure.',('A17','A43')),
 'customer2_latest_annualized':fact(2.487*4,'Q1FY27 customer2 2.487M *4 = annualized rank comparator, not guidance.',('A44',)),
 'mako_utilization_annualized':fact(6.6*12,'MAKO Q42012 monthly utilization6.6 *12 =79.2 annualized; old-platform analog only.',('G20',))}

leases=[.0116*8,.0116*8+.012064*4]
p['bridge']['new_apm_lease_fy27']=fact(leases[0],'New APM manufacturing rent FY27 =8months*0.0116M, COGS step beyond Q1; not integration cost.',('G21',))
p['bridge']['new_apm_lease_fy28']=fact(leases[1],'New APM manufacturing rent FY28 =8months*0.0116M+4months*0.012064M; existing renewed rents absorbed in normal inflation, no second blanket adjustment.',('G21',))
unscaled=[ [69.572,2.96,1.2,8.528,.2], [71.65916,3.108,1.2,7,.2] ];result={}
for i,y in enumerate(years):
 b=raw['base'][y];u=unscaled[i];new_un=sum(u)+b['hardware_revenue_M']+b['fee_revenue_M'];baseR=old['totals']['revenue'][y]['value'];M=b['total_monogram_revenue_M'];h=b['helios_revenue_M'];factor=(baseR-u[1]-M-h)/(sum(u)-u[1]-b['engineering_revenue_M']-h)
 # residual core excludes existing allocated engineering and Helios, adds incremental hardware/fee only
 vals=[(u[0]-h)*factor+h+b['hardware_revenue_M'],u[1],(u[2]-b['engineering_revenue_M'])*factor+b['engineering_revenue_M'],u[3]*factor,u[4]*factor+b['fee_revenue_M']]
 assert abs(sum(vals)-baseR)<1e-7
 for l,v in zip(p['lines'],vals):setval(l['periods'][y],v,'v4 residual-core consensus allocation; APM and explicit Monogram/Helios amounts unscaled. See S28.',['S28','S23','S24','S25','S26','S27'])
 setval(p['views']['revenue'][y]['bottom_up'],new_un,'Unscaled core lines plus Monogram hardware and purchase fees; engineering and Helios allocated within prior budgets.',['S2','S3','S6','S23','S24','S25','S26','S27'])
 setval(p['bridge']['scale_fy'+str(27+i)],factor,'(Consensus - APM - central Monogram - Helios)/(unscaled core excluding APM, allocated Monogram engineering, Helios).',['S28','E1','E2','S23'])
 for case,obj in [('base',p),('bull',p['scenarios']['bull']),('bear',p['scenarios']['bear'])]:
  r=raw[case][y];caseM=r['total_monogram_revenue_M'];coreGM={'base':.324516,'bull':.335,'bear':.31}[case]
  if case!='base':
   shock=(1 if case=='bull' else [-3,-8][i]);repair=(.5 if case=='bull' else [-1,-1.5][i]);change=[shock+r['hardware_revenue_M']-b['hardware_revenue_M']+r['helios_revenue_M']-h,0,r['engineering_revenue_M']-b['engineering_revenue_M'],repair,r['fee_revenue_M']-b['fee_revenue_M']]
   for l,v,d in zip(obj['lines'],vals,change):setval(l['periods'][y],v+d,'v4 base line plus core shock and explicit case-minus-central pipeline allocation.',['S15','S16','S28'])
  R=sum(l['periods'][y]['value'] for l in obj['lines']);GP=(R-caseM)*coreGM+r['gross_profit_M']-leases[i];E=GP-p['bridge']['opex_fy'+str(27+i)]['value']+p['bridge']['dasbc_fy'+str(27+i)]['value']-r['fee_admin_M']-r['shared_launch_support_M']
  if case!='base':setval(obj['totals']['revenue'][y],R,'Case revenue = base total + core volume/repair shocks + case Monogram/Helios minus central already included.',['S15','S16','S28'])
  setval(obj['totals']['ebitda'][y],E,'(Revenue-Monogram)*coreGM + MonogramGP - newAPMmanufacturingrent - opex + D&A+SBC - feeadmin - incremental launchsupport.',['S23','S24','S25','S26','C5','C6','C7','C8','G21'])
  obj['totals']['gross_margin'][y]=fact(GP/R,'Blended GAAP gross margin =(core revenue*coreGM+MonogramGP-newAPMrent)/total revenue.')
  setval(obj['totals']['ebitda_margin'][y],E/R,'EBITDA / revenue after robotics stream costs and new lease.',['S28','S26','G21'])
  obj['organic']['revenue'][y]=copy.deepcopy(obj['totals']['revenue'][y]);obj['organic']['ebitda'][y]=copy.deepcopy(obj['totals']['ebitda'][y]);result.setdefault(case,{})[y]={'revenue':R,'ebitda':E,'gross_margin':GP/R}
  if case=='base':
   setval(p['views']['ebitda'][y]['bottom_up'],E)
   unE=(new_un-M)*coreGM+r['gross_profit_M']-leases[i]-p['bridge']['opex_fy'+str(27+i)]['value']+p['bridge']['dasbc_fy'+str(27+i)]['value']-r['fee_admin_M']-r['shared_launch_support_M']
   setval(p['views']['ebitda_bottom_up_on_unscaled_revenue'][y],unE,'Unscaled revenue cost build with stream-specific robotics GP, launch support and APM lease.',['S23','S24','S25','S26','G21'])
   for key in ['bottom_up_over_base','bottom_up_over_consensus']:setval(p['views']['ratios'][y]['revenue'][key],new_un/baseR)
for case,obj in [('base',p),('bull',p['scenarios']['bull']),('bear',p['scenarios']['bear'])]:
 for metric in ['revenue','ebitda']:
  prior=obj['totals'][metric]['FY26A']['value'];growth=[]
  for y in years:v=obj['totals'][metric][y]['value'];growth.append(v/prior-1);prior=v
  obj['finagle']['sales_growth' if metric=='revenue' else 'ebitda_growth']['value']=growth
 setval(obj['finagle']['me'],obj['totals']['ebitda']['FY28E']['value']/obj['totals']['revenue']['FY28E']['value'])
 obj['finagle']['note']='Operating leaves only; no Finagle or terminal growth. The medium-term organic growth forecast keeps each line on its trajectory and adds one more FY28 Monogram cohort.'
def next_monogram(r):
 begin=r['begin_systems']+r['expected_new_systems'];added=r['expected_new_systems'];spares=begin*4*.05
 hw=(added*4+spares)*r['kit_price_USD']/1e6;active=begin+added/2
 fee=active*r['procedures_per_system_year']*r['purchase_inventory_factor']*r['eligible_basket_USD']/1e6*r['fee_rate']
 return r['engineering_revenue_M']+hw+fee
def trajectory(case,obj):
 '''One more year of each line, with the FY28 Monogram path replaced by the next cohort.'''
 r27,r28=raw[case]['FY27E'],raw[case]['FY28E']
 def amt(y,name):
  return next(l['periods'][y]['value'] for l in obj['lines'] if l['name']==name)
 med28=amt('FY28E','Medical devices')-r28['hardware_revenue_M']
 ind28=amt('FY28E','Industrial and scientific')
 nre28=amt('FY28E','NRE and prototype services')-r28['engineering_revenue_M']
 rep27,rep28=amt('FY27E','Repairs'),amt('FY28E','Repairs')
 disc27=amt('FY27E','Discounts and other')-r27['fee_revenue_M']
 disc28=amt('FY28E','Discounts and other')-r28['fee_revenue_M']
 rows=[
  ('Medical devices ex hardware',med28,med28*1.03),
  ('Industrial and scientific',ind28,ind28*1.05),
  ('NRE ex engineering',nre28,nre28),
  ('Repairs',rep28,rep28*(rep28/rep27)),
  ('Discounts ex fee',disc28,disc28+(disc28-disc27)),
  ('Monogram cohort',r28['total_monogram_revenue_M'],next_monogram(r28)),
 ]
 fy29=sum(b for _,_,b in rows)
 rev=result[case]['FY28E']['revenue']
 return rows,fy29,fy29/rev-1
bridges={}
for case,obj,evidence in [('base',p,['S3','S5','S7','S9','S23','G3']),('bull',p['scenarios']['bull'],['S3','S5','S7','S9','S15','S23'])]:
 rows,fy29,g=trajectory(case,obj);bridges[case]=(obj,rows,fy29,g)
 parts='; '.join('%s %.6f to %.6f'%(n,a,b) for n,a,b in rows)
 setval(obj['finagle']['gsnext'],g,f'{case} medium-term organic growth = FY29 {fy29} / FY28 revenue - 1. Lines keep their trajectory and the Monogram cohort is one more year: {parts}. Not a round rate.',evidence)
setval(p['scenarios']['bear']['finagle']['gsnext'],-0.1,'Bear gsnext stays -10%. That is the customer-1 renewal after calendar 2028, and it does not set the base.',['G3'])
# Show the effect of inherited SBC addback explicitly, without changing EBITDA definition.
p['bridge']['sbc_fy27']=fact(.135*4,'Forecast SBC = Q1FY27 0.135M *4; D2 cash flow statement.',('D2',))
p['bridge']['sbc_fy28']=fact(.135*4*1.03,'Forecast SBC = FY27 SBC *1.03 inflation.',('D2','S1'))
for case,obj in [('base',p),('bull',p['scenarios']['bull']),('bear',p['scenarios']['bear'])]:
 obj['totals']['ebitda_including_sbc_expense']={y:fact(obj['totals']['ebitda'][y]['value']-p['bridge']['sbc_fy'+y[2:4]]['value'],'EBITDA without stock-comp addback = headline EBITDA less forecast SBC.',[obj['totals']['ebitda'][y]['citation']['id'],p['bridge']['sbc_fy'+y[2:4]]['citation']['id']])for y in years}
row_inputs={'Medical devices ex hardware':['S3','G3'],'Industrial and scientific':['S5'],'NRE ex engineering':['S7'],'Repairs':['S8','S9'],'Discounts ex fee':['S10'],'Monogram cohort':['S23','G17']}
for case,(obj,rows,fy29,g) in bridges.items():
 recorded=[]
 for name,a,b in rows:
  ins=row_inputs[name]
  recorded.append({'name':name,'fy28':fact(a,f'{case} FY28 {name}, medium-term organic growth bridge.',ins),'fy29':fact(b,f'{case} FY29 {name}, medium-term organic growth bridge.',ins)})
 cite='S14' if case=='base' else 'S18'
 obj['gsnext_bridge']={'rows':recorded,'fy29_revenue':fact(fy29,f'{case} FY29 revenue = sum of the medium-term organic growth bridge.',[cite]),'growth':fact(g,f'{case} medium-term organic growth = FY29 bridge revenue / FY28 revenue - 1.',[cite])}
# Refresh all citation descriptions and as-of metadata; every reused calculation id means same current fact.
def refresh(o):
 if isinstance(o,dict):
  if 'citation' in o and o['citation'].get('id') in sources:o['citation']['text']=sources[o['citation']['id']]['text']
  if o.get('citation',{}).get('id') in ['E1','E2']:o['as_of']='2026-11-07';o['provider_capture_date']='2026-10-30';o['estimate_publication_date_status']='not stated'
  for v in o.values():refresh(v)
 elif isinstance(o,list):
  for v in o:refresh(v)
refresh(p)
# Fix primary citations for new lease calculations and judgment facts.
import re
urls={id:re.search(r'https?://\S+',ss['text']).group(0) for id,ss in sources.items() if id.startswith('D') and re.search(r'https?://\S+',ss['text'])}
def cite_primary(o):
 if isinstance(o,dict):
  if o.get('citation',{}).get('id') in sources:
   sid=o['citation']['id'];d=sources[sid].get('document');u=urls.get(d)
   if sid in [p['bridge']['new_apm_lease_fy27']['citation']['id'],p['bridge']['new_apm_lease_fy28']['citation']['id']]:u=urls['D28']
   if u and (sid.startswith('S') and int(sid[1:])>=30 or sid.startswith('C') and int(sid[1:])>=93):o['citation']['url']=u
  for v in o.values():cite_primary(v)
 elif isinstance(o,list):
  for v in o:cite_primary(v)
cite_primary(p)
p['views']['note']='Revenue consensus held; central robotics/Helios explicitly allocated within it. EBITDA stream-mix cost build plus launch costs and new disclosed APM lease; no EBITDA consensus. Consensus one analyst, capture Oct30, unknown analyst publication date.'
p['sources']=list(sources.values());p['article_review']['v4_disposition']='David authorized reasoned analyst estimates t166u; v3 optional-assumption posture superseded. Actual contract prices remain unverified; v4 judgments explicitly integrated.'
(H/'forecast.json').write_text(json.dumps(p,indent=2)+'\n');(H/'model_results.json').write_text(json.dumps({'results':result,'raw':raw},indent=2)+'\n')
print(json.dumps(result,indent=2));print('unscaled',[(y,p['views']['revenue'][y]['bottom_up']['value'],p['views']['ebitda_bottom_up_on_unscaled_revenue'][y]['value'])for y in years])
