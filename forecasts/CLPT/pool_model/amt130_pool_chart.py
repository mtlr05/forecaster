"""Figure E2: AMT-130 pool model, base case (from amt130_pool_annual_terms.json) vs. forecast volumes."""
import json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
d=json.load(open('amt130_pool_annual_terms.json'))['years']; ys=[int(y) for y in d]
fc={2027:330,2028:2500,2029:3170,2030:3000,2031:3000}
fig,ax=plt.subplots(figsize=(9,4))
ax.plot(ys,[d[str(y)]['T'] for y in ys],marker='o',label='Pool model: treated')
ax.plot(ys,[d[str(y)]['end'] for y in ys],marker='s',label='Pool model: pool at year end')
ax.plot(ys,[d[str(y)]['E'] for y in ys],ls=':',label='Entrants')
ax.plot(list(fc),list(fc.values()),marker='^',ls='--',label='Forecast AMT-130 procedures (to FY2031E)')
ax.set_xticks(ys); ax.set_xticklabels([f'FY{y}E' for y in ys]); ax.set_ylabel('Patients'); ax.grid(alpha=.3); ax.legend(fontsize=8)
fig.tight_layout(); fig.savefig('../amt130_pool_chart.png',dpi=150)
