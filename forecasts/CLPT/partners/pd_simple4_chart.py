import json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
d=json.load(open('pd_simple4_model.json')); R=d['rows']; t=[r['t'] for r in R]
f,ax=plt.subplots(figsize=(9,4.8))
ax.plot(t,[r['S']/1e3 for r in R],lw=2.5,color='#0b3d91',label='Eligible pool, DBS patients included (start of year)')
ax.plot(t,[r['E']/1e3 for r in R],lw=1.5,ls='--',color='#777',label='Entrants (newly eligible)')
ax.plot(t,[r['T']/1e3 for r in R],lw=2.5,color='#e67e22',label='One-time therapy class demand (6% of pool)')
ax.plot(t,[r['DBS']/1e3 for r in R],lw=1.2,color='#555',label='DBS 3,990 a year (context; not deducted)')
ax.plot(t,[d['chain']['Pss']*r['E']/1e3 for r in R],lw=1,ls=':',color='#c62828',label='Steady state: u/(m+u+g) × entrants')
ax.axvline(d['inputs']['LAU']-0.5,color='k',lw=0.8); ax.text(d['inputs']['LAU']-0.4,60,'launch FY2029',fontsize=8)
ax.set_ylabel("'000 patients"); ax.set_ylim(0); ax.grid(alpha=.3); ax.legend(frameon=False,fontsize=8,loc='center right')
ax.set_title('US eligible PD pool and one-time therapy class demand\nbase case: 6% of pool treated a year from FY2029',fontsize=11); ax.set_xticks(t[::2])
plt.figtext(0.01,0.01,'Source: eligible-pool model (pool flows). Class level; before allocation between therapies and capacity.',fontsize=7,color='#444')
plt.tight_layout(rect=(0,0.04,1,1)); plt.savefig('pd_simple4_chart.png',dpi=150)
