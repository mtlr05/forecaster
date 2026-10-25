"""Value per share of a flat $20M/yr revenue add-on (1,000 patients x $20k) to the base case, through Finagle run_case only.
Add-on: $20M revenue from FY30E, EBITDA at procedure margin 70% GM - 10% specialist cost = 60% (S23/S24); no fixed opex.
Explicit years FY30-32 get +20 revenue / +12 EBITDA; me recomputed; gsnext rescaled so the FY33 dollar increment is unchanged
(add-on flat into FY33). After FY33 Finagle fades growth on total revenue to its default gt, so the add-on grows with the fade. Never sets gt."""
import copy, json, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[2] / "finagle"))
from finagle.agent.runner import run_case
fc = json.load(open(HERE / "forecast.json"))
c0 = json.load(open(HERE / "finagle_run.json"))["base"]["case"]
YRS = ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E", "FY32E"]
rev0 = [fc["totals"]["revenue"][y]["value"] for y in YRS]; e0 = [fc["totals"]["ebitda"][y]["value"] for y in YRS]
R25, E25 = fc["totals"]["revenue"]["FY25A"]["value"], fc["totals"]["ebitda"]["FY25A"]["value"]
def run(add, start="FY30E", m=0.60):
    rev = [r + (add if YRS.index(y) >= YRS.index(start) else 0) for r, y in zip(rev0, YRS)]
    e = [x + (add * m if YRS.index(y) >= YRS.index(start) else 0) for x, y in zip(e0, YRS)]
    c = copy.deepcopy(c0); fo = c["forecast"]; mp = fo["margin_path"]
    fo["sales_growth"]["value"] = [rev[0] / R25 - 1] + [rev[i] / rev[i - 1] - 1 for i in range(1, 7)]
    fo["ebitda_growth"]["value"] = [e[0] / E25 - 1] + [e[i] / e[i - 1] - 1 for i in range(1, 7)]
    mp["me"]["value"] = e[-1] / rev[-1]
    mp["gsnext"]["value"] = mp["gsnext"]["value"] * rev0[-1] / rev[-1]
    r = run_case(c); return r["value_per_share"], [y["revenue"] for y in r["years"]], [y["ebitda"] for y in r["years"]]
b, rb, eb = run(0.0)
out = {"base_vps": b}
for add in (20.0, 200.0):
    v, rr, ee = run(add)
    out["add_%d" % add] = dict(vps=v, delta=v - b, rev_delta=[x - y for x, y in zip(rr, rb)], ebitda_delta=[x - y for x, y in zip(ee, eb)])
v, *_ = run(20.0, "FY34E" if False else "FY32E"); out["add_20_from_FY32"] = dict(vps=v, delta=v - b)
json.dump(out, open(HERE / "finagle_perpetuity.json", "w"), indent=1)
for k, x in out.items():
    print(k, x if not isinstance(x, dict) else {a: (round(z, 3) if isinstance(z, float) else [round(q, 1) for q in z]) for a, z in x.items()})
