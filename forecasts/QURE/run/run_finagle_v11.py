import json,copy,sys
sys.path.insert(0,'/workspace/finagle')
from finagle.agent import describe_inputs,build_baseline,update_case,validate_case,run_case
R=json.load(open('/workspace/out/QURE_run_v11/valuation_request_v11.json'))
paths={f['path'] for f in describe_inputs()['fields']}
bb=build_baseline('QURE',user_agent='David May davidmay44@hotmail.com')
json.dump(bb,open('/workspace/out/QURE_run_v11/run/baseline_v11.json','w'),indent=1,default=str)
if not bb.get('ok',True): sys.exit('build_baseline failed '+json.dumps(bb,default=str)[:2000])
case=bb.get('case') or {k:bb[k] for k in('ticker',) }
if 'case' not in bb:
  case=dict(path='ebitda',ticker='QURE',year=bb.get('year',10),market={'shares':bb['shares'],'price':bb['price']},rates=bb['rates'],baseline=bb['baseline'],forecast=bb['forecast'],debt=bb['debt'],distribution=bb['distribution'])
out={}
for sc in R['scenarios']:
  up={}
  for k,v in R['forecaster'][sc].items():
    print(sc,k,'in catalog' if k in paths or k.rsplit('.',1)[0] in paths else 'NOT IN CATALOG')
    p=k.split('.');t=up
    for q in p[:-1]: t=t.setdefault(q,{})
    t[p[-1]]={'value':v['value'],'source':'assumption','evidence':f"Forecaster [{v['tag']}] {v['cite_id']}: {v['evidence']}"}
  for pi in R['prompt_inputs']:
    if sc in pi['applies_to']:
      p=pi['path'].split('.');t=up
      for q in p[:-1]: t=t.setdefault(q,{})
      t[p[-1]]={'value':pi['value'],'source':'prompt','evidence':f"David {pi['date']}: \"{pi['quote']}\""+(' '+pi['note'].strip() if pi.get('note') else '')}
      if p[0]=='baseline': t[p[-1]].update(period_end='2025-12-31',basis='fiscal_year',currency='USD')
  if up.get('debt',{}).get('mode',{}).get('value')=='hold': case_s=copy.deepcopy(case); [case_s['debt'].pop(k,None) for k in ('leverage','start_year')]
  else: case_s=case
  u=update_case(copy.deepcopy(case_s),up,run=False)
  c=u.get('case',u)
  val=validate_case(c);json.dump(c,open(f'/workspace/out/QURE_run_v11/case_{sc}_v11.json','w'),indent=1,default=str)
  if val['errors'] or val['missing']: print(sc,'STOP',val);out[sc]={'stopped':True,'validation':val};continue
  assert abs(c['baseline']['da']['value']-0.2195)<1e-12, c['baseline']['da']
  r=run_case(c);out[sc]=r
  print(sc,'DA case',r['case']['baseline']['da'],'nb', [l for l in r['notebook_code'].splitlines() if 'da' in l.lower()][:6])
  print(sc,r['ok'],r['value_per_share'],r['value_per_share_DDM'],val['warnings'],r['log'],r['sanity_flags'])
json.dump({'bb':bb,'res':out},open('/workspace/out/QURE_run_v11/run/raw_v11.json','w'),indent=1,default=str)
