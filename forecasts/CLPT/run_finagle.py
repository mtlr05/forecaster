"""Hand the CLPT operating path to Finagle (read-only clone beside this repo). Run from repo root parent."""
import copy, json, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[2] / "finagle"))
from finagle.agent.validate import validate_case
from finagle.agent.runner import run_case

base = json.load(open(HERE / "clpt_baseline.json"))  # build_baseline('CLPT') output, 2026-10-23
fc = json.load(open(HERE / "forecast.json"))
Q10 = "Q2 2026 Form 10-Q"

def leaf(v, src, ev):
    return {"value": v, "source": src, "evidence": ev}

def case_for(block, label):
    c = copy.deepcopy(base["case"])
    f = block["finagle"]
    c["year"] = 20
    c["rates"]["rd"] = leaf(0.0825, "attachment", Q10 + ": notes bear SOFR(floor 4.30%) + 3.95%, minimum 8.25%")
    c["rates"]["t"] = leaf(0.21, "assumption", "US federal statutory rate (assumption)")
    c["baseline"]["nol"] = dict(leaf(258.2, "10k", "Federal NOL carryforwards approx $258.2M at Dec 31, 2025 (2025 10-K)"), basis="fiscal_year", period_end="2025-12-31", currency="USD")
    c["baseline"]["noa"] = dict(leaf(0.0, "assumption", "No non-operating assets identified; zero by choice"), basis="fiscal_year", period_end="2025-12-31", currency="USD")
    c["market"]["shares"] = leaf(30.503132, "attachment", Q10 + ": 30,503,132 shares outstanding at June 30, 2026")
    c["debt"] = {"mode": leaf("hold", "assumption", "Hold notes flat; no re-borrowing toward a negative Debt/EBITDA")}
    c["distribution"] = {"mode": leaf("none", "assumption", "No dividend/buyback program; negative FCFE treated as equity funding")}
    fo = c.setdefault("forecast", {})
    fo["ebitda_growth"] = leaf(f["ebitda_growth"]["value"], "assumption", "forecaster " + label)
    fo["sales_growth"] = leaf(f["sales_growth"]["value"], "assumption", "forecaster " + label)
    fo["margin_path"] = {"me": leaf(f["me"]["value"], "assumption", "forecaster FY32E EBITDA/revenue"),
                         "mc": leaf(f["mc"]["value"], "assumption", "forecaster S17"),
                         "gsnext": leaf(f["gsnext"]["value"], "assumption", "forecaster C29")}
    fo["dwc"] = {"mode": leaf("zero", "assumption", "No working-capital change (labelled assumption)")}
    fo["ebitda_basis"] = leaf("total", "assumption", "No deal after year 0")
    fo["acquisition_disclosure"] = {"status": leaf("none", "assumption", "No announced future deals")}
    return c

out = {}
for label, block in (("base", fc), ("bull", fc["scenarios"]["bull"]), ("bear", fc["scenarios"]["bear"])):
    c = case_for(block, label)
    v = validate_case(c)
    r = run_case(c) if not v.get("missing") and not v.get("errors") else None
    out[label] = {"validate": v, "result": r, "case": c}
    print(label, "missing", v.get("missing"), "errors", v.get("errors"), "warnings", v.get("warnings"))
    if r:
        print(json.dumps({k: r[k] for k in r if k not in ("notebook_code",)}, default=str)[:3000])
json.dump(out, open(HERE / "finagle_run.json", "w"), indent=1, default=str)
