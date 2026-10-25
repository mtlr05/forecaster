"""Appendix C Figure C3: from partners/pd_simple4_model.json (180k pool, DBS not deducted)."""
import json, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
d = json.load(open("partners/pd_simple4_model.json")); r = d["rows"]
t = [x["t"] for x in r]; k = lambda f: [f(x) / 1e3 for x in r]
share = {2029: 1/3, 2030: 2/3}
fig, ax = plt.subplots(figsize=(10, 5.3), dpi=150)
ax.plot(t, k(lambda x: x["S"]), lw=2.2, color="#1f3b73", label="Eligible pool, start of year (DBS patients included)")
ax.plot(t, k(lambda x: x["E"]), "--", color="grey", label="Entrants (newly eligible)")
ax.plot(t, k(lambda x: x["T"]), color="#c0392b", lw=2, label="One-time therapy class demand (6% of pool from FY2029)")
ax.plot(t, k(lambda x: x["T"] * share.get(x["t"], 1)), ":", color="#e67e22", lw=2.2, label="Class volume on ClearPoint (three-year ramp)")
ax.plot(t, k(lambda x: 3990), color="#7f8c8d", lw=1, label="DBS 3,990 a year (context; not deducted)")
ax.axvline(2028.5, color="k", lw=0.8); ax.text(2028.6, 120, "Launch FY2029", fontsize=8)
ax.set_ylabel("'000 patients"); ax.set_ylim(0); ax.set_xticks(range(2026, 2046, 2)); ax.grid(alpha=0.3)
ax.set_title("US eligible Parkinson's pool and one-time therapy class demand, base case")
ax.legend(loc="center right", fontsize=8); fig.text(0.01, 0.01, "Source: eligible-pool model; class level, before allocation between therapies.", fontsize=7)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig("pd_pool_chart.png")
