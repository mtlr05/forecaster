"""Valuation detail from Finagle output: PV split and sensitivities (re-runs run_case; never sets gt)."""
import copy, json, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[2] / "finagle"))
from finagle.agent.runner import run_case
d = json.load(open(HERE / "finagle_run.json"))
out = {}
for k, v in d.items():
    r, c = v["result"], v["case"]
    re_ = c["rates"]["re"]["value"]; ys = r["years"]
    pv = sum(y["dividend"] / (1 + re_) ** y["year"] for y in ys if y["year"] >= 1)
    tv_pv = r["value_per_share"] - pv
    y10 = ys[-1]
    row = dict(vps=r["value_per_share"], pv_explicit=pv, pv_terminal=tv_pv, equity=r["equity"], firm=r["firm"],
               fcfet=r["fcfet"], twacc=r["terminal_wacc"], re=re_, gt=c["rates"]["gt"]["value"], rd=c["rates"]["rd"]["value"],
               mc=c["forecast"]["margin_path"]["mc"]["value"], gsnext=c["forecast"]["margin_path"]["gsnext"]["value"],
               me=c["forecast"]["margin_path"]["me"]["value"], shares=c["market"]["shares"]["value"],
               debt=ys[0]["debt"], cash=ys[0]["cash"], yN_rev=y10["revenue"], yN_ebitda=y10["ebitda"],
               min_cash=min(y["cash"] for y in ys), first_pos=next((y["year"] for y in ys if y["ebitda"] > 0), None),
               flags=r.get("sanity_flags"))
    sens = {}
    def rerun(mut):
        cc = copy.deepcopy(c); mut(cc); rr = run_case(cc); return rr["value_per_share"] if rr.get("ok") else None
    for dl in (-0.01, 0.01):
        sens["re%+.0f%%" % (dl * 100)] = rerun(lambda cc: cc["rates"]["re"].update(value=re_ + dl))
    for dl in (-0.10, 0.10):
        sens["mc%+.2f" % dl] = rerun(lambda cc: cc["forecast"]["margin_path"]["mc"].update(value=row["mc"] + dl))
    for dl in (-0.05, 0.05):
        sens["gsnext%+.0f%%" % (dl * 100)] = rerun(lambda cc: cc["forecast"]["margin_path"]["gsnext"].update(value=row["gsnext"] + dl))
    sens["year10 (v4 horizon)"] = rerun(lambda cc: cc.update(year=10))
    row["sens"] = sens
    row["growth_path"] = [dict(year=y["year"], revenue=y["revenue"], ebitda=y["ebitda"],
                               g=(y["revenue"] / ys[i - 1]["revenue"] - 1) if i > 1 else None) for i, y in enumerate(ys)]
    out[k] = row
json.dump(out, open(HERE / "finagle_valuation.json", "w"), indent=1)
for k, r in out.items():
    print(k, {a: (round(b, 3) if isinstance(b, float) else b) for a, b in r.items() if a != "sens"})
    print("  sens", {a: round(b, 2) for a, b in r["sens"].items()})
