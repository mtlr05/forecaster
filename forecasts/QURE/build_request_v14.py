"""Build valuation_request_v14.json = v12 request + rev6 forecast (one confirmatory-study cost profile in bear, base and bull; David t124u 2026-11-02). Bear raise re-sized from zero by the cash-never-negative rule (smallest $50M multiple) via scratch dry compile (dry13.py, not a valuation)."""
import hashlib, json, math, pathlib, sys, copy
REPO = pathlib.Path("/workspace/forecaster-work/forecaster-main"); sys.path.insert(0, str(REPO))
from forecastcheck.collaborative import check_request
from forecastcheck.validate import validate_payload
HERE = pathlib.Path(__file__).parent; V11 = pathlib.Path("/workspace/out/QURE_run_v13"); sys.path.insert(0, str(HERE))
from dry14 import run as dry
fc = json.loads((HERE / "forecast.json").read_text()); assert validate_payload(fc)["ok"]
def leaf(f):
    c = f["citation"]; return {"value": f["value"], "tag": f["tag"], "cite_id": c["id"], "evidence": c["text"] + " (" + c["url"] + ")"}
def block(fin):
    return {"forecast.sales_growth": leaf(fin["sales_growth"]), "forecast.ebitda_growth": leaf(fin["ebitda_growth"]), "forecast.margin_path.me": leaf(fin["me"]), "forecast.margin_path.mc": leaf(fin["mc"]),
            "forecast.margin_path.gsnext": leaf(fin["gsnext"]), "forecast.ebitda_basis": leaf(fin["ebitda_basis"]), "forecast.acquisition_disclosure.status": leaf(fin["acquisition_disclosure"]["status"])}
SCN = {"base": fc, "bull": fc["scenarios"]["bull"], "bear": fc["scenarios"]["bear"]}
r11 = json.loads((V11 / "valuation_request_v13.json").read_text()); req = copy.deepcopy(r11)
req["version"], req["parent_version"] = "v14", "v13"
req["forecast_commit"] = "uncommitted (v13 forecast at /workspace/out/QURE_run_v14/forecast.json)"
req["forecaster"] = {n: block(SCN[n]["finagle"]) for n in ("base", "bull", "bear")}
for n in ("base", "bull"): print(n, "block changed vs v13:", req["forecaster"][n] != r11["forecaster"][n])
def case(n, cash=None, shares=None):
    c = json.loads((V11 / ("case_%s_v13.json" % n)).read_text())
    for k, v in req["forecaster"][n].items():
        node = c
        for p in k.split(".")[:-1]: node = node[p]
        node[k.split(".")[-1]]["value"] = v["value"]
    if cash is not None: c["baseline"]["cash"]["value"] = cash
    if shares is not None: c["market"]["shares"]["value"] = shares
    return c
PI = {(tuple(p["applies_to"]), p["path"]): p for p in req["prompt_inputs"]}
PRICE = 25.3
CASH10K, INV10K, OFFER_NET, SH10K, OFFER_SH = 80.240, 542.301, 242.681, 62.529408, 5.686813
CASH0 = round(CASH10K + INV10K + OFFER_NET, 3); SH0 = round(SH10K + OFFER_SH, 6)   # 865.222, 68.216221
DRY, RAISE, MIN0 = {}, {}, {}
for n in ("base", "bull", "bear"):
    d0 = dry(case(n, cash=CASH0, shares=SH0)); MIN0[n] = min(d0["cash"]); R = 0.0; d = d0
    if MIN0[n] < 0:
        R = math.ceil(-MIN0[n] / 50.0) * 50.0
        while True:
            d = dry(case(n, cash=round(CASH0 + R, 3), shares=round(SH0 + R / PRICE, 6)))
            if min(d["cash"]) >= 0: break
            R += 50.0
    DRY[n], RAISE[n] = d, R
    assert min(d["cash"]) >= 0
EVID = ("Year-0 cash = 10-K FY2025 cash and cash equivalents $80.240M + current investment securities $542.301M = $622.541M [A] "
        "+ June 2026 follow-on offering net proceeds $242.681M (5,686,813 shares at $45.50 incl. full option; 10-Q Q2 2026 cash flow) = $865.222M (David t129u 2026-11-02). "
        "Shares = 10-K cover 62.529408M + 5.686813M offering shares = 68.216221M. Employee option/ESPP proceeds ($6.985M) and ~1.15M plan shares excluded (only equity raises) [S]. ")
for n in ("base", "bull", "bear"):
    R = RAISE[n]; cash, sh = round(CASH0 + R, 3), round(SH0 + R / PRICE, 6)
    why = ("Minimum year-end cash with no extra raise = %.2f, so no extra raise is needed (extra raise $0)." % MIN0[n]) if R == 0 else \
          ("Minimum year-end cash with no extra raise = %.2f; extra year-0 raise $%.0fM [S] (smallest $50M multiple keeping cash >= 0 in every year, David t64u/t68u), issued at $25.30, no discount or fees, %.6fM shares." % (MIN0[n], R, R / PRICE))
    for path, val in (("baseline.cash", cash), ("market.shares", sh)):
        q = PI[((n,) if n == "bear" else (n,), path)]
        q.update(value=val, date="2026-11-02", quote="Year-0 should be 2025 cash+short term. And then adjust for any equity raises during the 2026 year. Then increase sharecount from 2025 to account for the equity raises.", note=EVID + why)
req["undecided_by_david"] = [u for u in req["undecided_by_david"] if "bear raise" not in u["item"]]
req["undecided_by_david"].append({"item": "v14 year-0 funding", "risk": "Employee-plan cash/shares and pre-funded warrants excluded; extra raises base %.0f, bull %.0f, bear %.0f [S]." % (RAISE["base"], RAISE["bull"], RAISE["bear"])})
req["note"] = ("v14 = v13 + David t129u (2026-11-02) year-0 cash = FY2025 cash + current investments + June 2026 offering net; shares + offering shares; extra raises base %.0f / bull %.0f / bear %.0f. Scratch dry check (not a valuation): min cash base %.2f, bull %.2f, bear %.2f.") % (RAISE["base"], RAISE["bull"], RAISE["bear"], min(DRY["base"]["cash"]), min(DRY["bull"]["cash"]), min(DRY["bear"]["cash"]))
minb0 = MIN0["bear"]; R = RAISE["bear"]; R11 = 5000.0
errs = check_request(req, fc); print("check_request:", errs); assert errs == [], errs
OUT = HERE / "valuation_request_v14.json"; OUT.write_text(json.dumps(req, indent=1, ensure_ascii=False) + "\n")
def canon(o): return json.dumps(o, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
h = {"rule": "sha256 of json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False, allow_nan=False); sidecar only",
     "blocks": {k: hashlib.sha256(canon(v)).hexdigest() for k, v in req["forecaster"].items()}, "prompt_inputs": hashlib.sha256(canon(req["prompt_inputs"])).hexdigest(),
     "whole_request": hashlib.sha256(canon(req)).hexdigest(), "file_bytes": hashlib.sha256(OUT.read_bytes()).hexdigest(), "forecast_json_bytes": hashlib.sha256((HERE / "forecast.json").read_bytes()).hexdigest()}
(HERE / "valuation_request_v14.sha256.json").write_text(json.dumps(h, indent=1) + "\n")
L = ["v14 scratch dry check (dry12.py on /workspace/forecaster-work/finagle; NOT a valuation)"]
for n in ("base", "bull", "bear"):
    for k in ("revenue", "ebitda", "capex", "cash"): L.append("%s %s %s" % (n, k, [round(x, 2) for x in DRY[n][k]]))
    L.append("%s min cash %.2f" % (n, min(DRY[n]["cash"])))
L += ["%s: min cash with no extra raise %.2f -> extra raise $%.0fM, cash %.3f, shares %.6f, final min cash %.2f" % (n, MIN0[n], RAISE[n], CASH0 + RAISE[n], SH0 + RAISE[n] / PRICE, min(DRY[n]["cash"])) for n in ("base", "bull", "bear")]
(HERE / "dry_v14_summary.txt").write_text("\n".join(L) + "\n"); json.dump(DRY, open(HERE / "dry_v14.json", "w"), indent=1); print("\n".join(L))
