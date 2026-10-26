"""Report Figure D5: partner revenue chart FY2027E-FY2031E from partners_v4_model.json (report ends at FY2031E)."""
import json, os, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
H = os.path.dirname(os.path.abspath(__file__)); d = json.load(open(os.path.join(H, "partners_v4_model.json")))
Y = list(range(2027, 2032)); n = len(Y)
plt.figure(figsize=(10, 5.6))
for p, c in zip(["1.0", "0.7", "0.5", "0.3"], ["#0b3d91", "#2e7d32", "#f9a825", "#c62828"]):
    plt.plot(Y, d["totals"][p][:n], marker="o", ms=3.5, lw=2, color=c, label=f"{int(float(p)*100)}% avg. probability of approval")
plt.title("ClearPoint procedure revenue from slide-23 partner therapies (US, $20k per procedure), FY2027E-FY2031E", fontsize=11)
plt.ylabel("Revenue (US$M)"); plt.xlabel("Fiscal year"); plt.grid(alpha=.3); plt.xticks(Y); plt.legend(frameon=False); plt.ylim(0)
plt.figtext(0.01, 0.01, "Source: Figure D4 (partners_v4_model.json); price $20k [P2]. KEBILIDI held at 100%. Base-case volumes; scenario, not guidance.", fontsize=7, color="#444")
plt.tight_layout(rect=(0, 0.05, 1, 1)); plt.savefig(os.path.join(H, "partners_v4_revenue_chart_to2031.png"), dpi=160)
