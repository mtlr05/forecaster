import json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
d=json.load(open('pd_pool_model.json')); yy=list(range(2026,2046))
S={k:{r['t']:r for r in v['rows']} for k,v in d['scen'].items()}; C=S['8%']
f,ax=plt.subplots(figsize=(10,5.2))
ax.plot(yy,[C[y]['one_B']/1e3 for y in yy],lw=2.5,color='#0b3d91',label='B: one-time therapy replaces DBS')
ax.plot(yy,[C[y]['one_A']/1e3 for y in yy],lw=2.5,ls='--',color='#0b3d91',label="A: DBS keeps its volume")
ax.plot(yy,[C[y]['fN']/1e3 for y in yy],lw=1.5,ls=':',color='#555',label='Funnel inflow (newly eligible × referral × willing × covered)')
ax.plot(yy,[C[y]['dbs_A']/1e3 for y in yy],lw=1.2,color='#c62828',label='DBS under 75 (bound A)')
ax.set_ylabel("'000 patients a year"); ax.set_title('US class demand for a one-time PD therapy, same for all four eligibility cases (product calibrated to DBS)',fontsize=10)
ax.grid(alpha=.3); ax.set_xticks(yy); ax.tick_params(axis='x',rotation=45); ax.legend(frameon=False,fontsize=8,loc='upper left'); ax.set_ylim(0)
sec=ax.secondary_yaxis('right',functions=(lambda x:x*20,lambda x:x/20)); sec.set_ylabel('Revenue equivalent at $20k (US$M)')
plt.figtext(0.01,0.01,"Source: pd_pool_model.xlsx, 'Flow 8%' columns H, J, K, P (identical in the 5%, 10%, 15% sheets). Scenario, not guidance.",fontsize=7,color='#444')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig('pd_pool_demand_chart.png',dpi=160); plt.close()
# stage funnel FY2026 for each case
names=['5%','8%','10%','15%']; R26={k:S[k][2026] for k in names}; PD=R26['8%']['PD']
f,ax=plt.subplots(figsize=(10,4.6)); x=range(len(names)); wd=0.25
ax.bar([i-wd for i in x],[R26[k]['E']/1e3 for k in names],wd,label='Medically eligible stock',color='#90caf9')
ax.bar(list(x),[R26[k]['N']/1e3 for k in names],wd,label='Newly eligible a year',color='#1976d2')
ax.bar([i+wd for i in x],[R26[k]['fN']/1e3 for k in names],wd,label='… × referral × willing × covered',color='#0b3d91')
for i,k in enumerate(names): ax.text(i+wd,R26[k]['fN']/1e3+2,f"P={d['scen'][k]['P']:.2f}",ha='center',fontsize=8)
ax.set_xticks(list(x)); ax.set_xticklabels([f'Eligible {k} of PD' for k in names]); ax.set_ylabel("'000 patients, FY2026"); ax.legend(frameon=False,fontsize=8); ax.grid(alpha=.3,axis='y')
ax.set_title('Stage-consistent funnel, FY2026: more eligibility means a lower implied downstream product',fontsize=10)
plt.figtext(0.01,0.01,"Source: pd_pool_model.xlsx, Scenarios rows 5, 8, 9 and Flow sheets column H.",fontsize=7,color='#444')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig('pd_pool_funnel_chart.png',dpi=160); plt.close()
tb=d['tornado_base']; tor=sorted(d['tornado'],key=lambda x:abs(x['hi']['B2040']-x['lo']['B2040']))
f,axs=plt.subplots(1,2,figsize=(11,4.6),sharey=True)
for ax,key,ttl in ((axs[0],'A2040','Bound A: DBS keeps volume'),(axs[1],'B2040','Bound B: replaces DBS')):
    base=tb[key]
    for i,x in enumerate(tor):
        ax.barh(i,(x['lo'][key]-base)/1e3,left=base/1e3,color='#c62828'); ax.barh(i,(x['hi'][key]-base)/1e3,left=base/1e3,color='#2e7d32')
    ax.axvline(base/1e3,color='k',lw=1); ax.set_title(ttl,fontsize=10); ax.set_xlabel("FY2040 one-time demand ('000)")
axs[0].set_yticks(range(len(tor))); axs[0].set_yticklabels([x['label'] for x in tor],fontsize=8)
f.suptitle('Tornado, central 8% case (red = first value, green = second value)',fontsize=11)
plt.figtext(0.01,0.01,'Source: pd_pool_model.xlsx, Sensitivity.',fontsize=7,color='#444')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig('pd_pool_tornado.png',dpi=160)
