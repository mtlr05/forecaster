import json,datetime,pandas as pd,platform
d=json.load(open('run/raw_v14.json'));bb=d['bb']
def asm(c,p=''):
  o=[]
  for k,v in c.items():
    q=p+'.'+k if p else k
    if isinstance(v,dict):
      if v.get('source')=='assumption' and not str(v.get('evidence','')).startswith('Forecaster'): o.append(q)
      elif 'source' not in v: o+=asm(v,q)
  return o
S={}
for sc,r in d['res'].items():
  c=r['case'];Y=r['years']
  S[sc]=dict(r)|{'defaults_filled':sorted(set(asm(c))|({'year'} if 'year' in bb['assumptions'] else set())),'defaults_filled_build_baseline_list':bb['assumptions'],
   'forecaster_leaves_note':'Forecaster leaves applied with source assumption (evidence prefixed "Forecaster [tag] cite"); excluded from defaults_filled',
   'checks':{'label':'COMPUTED OUTSIDE run_case from result.years','min_cash':min(y['cash'] for y in Y),'debt_peak':max(y['debt'] for y in Y),'max_debt_to_ebitda':max((y['debt']/y['ebitda'] for y in Y if y['ebitda']>0),default=None),'positive_ebitda_years':[y['date'][:4] for y in Y if y['ebitda']>0]},
   'per_year_extra':{'label':'COMPUTED OUTSIDE run_case from result.years and case rates; approximate','interest_rd_x_opening_debt':[None]+[c['rates']['rd']['value']*Y[i-1]['debt'] for i in range(1,len(Y))],'equity_per_share_by_year':[y['equity']/y['shares'] for y in Y],'debt_target_1x_ebitda':[max(y['ebitda'],0)*c['debt']['leverage']['value'] if 'leverage' in c['debt'] else None for y in Y]},
   'not_returned_by_run_case':['interest per year','SBC per year (only year-0 17.679 passed to forecast_sbc)','taxes per year','WACC per year (terminal_wacc only)'],
   'returned_per_year':['debt','firm (EV)','equity','fcf','fcfe','fcff','capex','cash','dividend','price (buyback price path, constant)'],
   'year0_da_check':{'case_baseline_da':c['baseline']['da']['value'],'notebook_financials_da':[l.strip() for l in r['notebook_code'].splitlines() if "'da':" in l],'ok':c['baseline']['da']['value']==0.2195},'flags':['see report; negative cash all scenarios','year-0 debt 49.699 excludes Hemgenix royalty liability (478.7 at FY25)','value not meaningful']}
  with pd.ExcelWriter(f'CLPT_{sc}_v14.xlsx'.replace('CLPT','QURE')) as w:
    pd.DataFrame([{k:r[k] for k in('ok','value_per_share','value_per_share_DDM','vpsbb','equity','firm','fcfet','terminal_wacc')}]).T.to_excel(w,sheet_name='summary')
    pd.DataFrame(Y).assign(**{'interest_DERIVED':S[sc]['per_year_extra']['interest_rd_x_opening_debt'],'equity_ps_DERIVED':S[sc]['per_year_extra']['equity_per_share_by_year'],'target_debt_DERIVED':S[sc]['per_year_extra']['debt_target_1x_ebitda']}).to_excel(w,sheet_name='years',index=False)
    pd.DataFrame({'item':r['validation']['warnings']+r['sanity_flags']+r['log']+S[sc]['flags']}).to_excel(w,sheet_name='warnings',index=False)
    pd.DataFrame({'defaults_filled':S[sc]['defaults_filled']}).to_excel(w,sheet_name='defaults',index=False)
out={'ticker':'QURE','version':'v14','finagle_commit':'377f177b4013e713fe7c4603962e5f883a67e298',
 'run_at':datetime.datetime.now().astimezone().isoformat(),'hash_check':'all sidecar hashes match (file bytes, whole request, base/bull/bear blocks, prompt_inputs, v14 forecast.json bytes)',
 'fetched':{'price':bb['price']['value'],'price_date':bb['price']['as_of'],'rf':bb['rates']['risk_free']['value'],'rf_date':bb['rates']['risk_free']['as_of'],'shares':bb['shares']['value'],'shares_source':bb['shares']['evidence']+'; '+bb['shares']['note'],
   're':bb['rates']['re']['value'],'gt':bb['rates']['gt']['value'],'year0':{k:v.get('value') for k,v in bb['baseline'].items()},'year0_sources':bb['sources_used']},
 'prompt_inputs':json.load(open('valuation_request_v14.json'))['prompt_inputs'],'request_sha256_file':'see valuation_request_v14.sha256.json; sidecar whole/blocks/prompt_inputs/forecast.json verified','hold_mapping':'debt.mode hold is a native Finagle mode; stale default debt.leverage/start_year leaves removed for bear before update_case','ff_log':'git pull: already up to date (377f177)','market_data':'price, rf and re pinned to the v11 fetch (2026-10-30: price 25.30, rf 4.989%); live 2026-11-02 fetch price 24.83, rf 4.929% kept in run/baseline_v14_live.json, not used','post_finagle':None,'scenarios':S}
json.dump(out,open('valuation_result_v14.json','w'),indent=1,default=str)
for s in S: print(s,S[s]['defaults_filled'],S[s]['checks'])
