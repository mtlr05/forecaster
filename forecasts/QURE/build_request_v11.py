"""Build valuation_request_v11.json: v10 request + forecast rev4/v11 (AMT-130 pool model m = 0.62, CLPT ramp; David t97u/t98u 2026-10-30).
Forecaster block rebuilt from /workspace/out/QURE_run_v11/forecast.json (same leaf()/block() as build_request_v7.py). Prompt inputs carried from v10;
only items that mechanically follow the volume path are recomputed with v10's own rules: SBC lists (David's rule, 5% [S]), debt.start_year (first EBITDA-positive year),
bear capex = base dollars (base Finagle method-1 capex, scratch dry run). Raise sizes kept from v10 unless cash goes negative (David t64u/t68u rule) -> checked by dry11.py.
Does not call the Finagle bot and does not write to /workspace/finagle or the forecaster repo."""
import hashlib, json, pathlib, sys, copy
REPO = pathlib.Path("/workspace/forecaster-work/forecaster-main"); sys.path.insert(0, str(REPO))
from forecastcheck.collaborative import check_request
from forecastcheck.validate import validate_payload
HERE = pathlib.Path(__file__).parent; V10 = pathlib.Path("/workspace/out/QURE_run")
sys.path.insert(0, str(HERE)); from dry11 import run as dry
FC = HERE / "forecast.json"; OUT = HERE / "valuation_request_v11.json"
fc = json.loads(FC.read_text()); assert validate_payload(fc)["ok"]
def leaf(f):
    c = f["citation"]; return {"value": f["value"], "tag": f["tag"], "cite_id": c["id"], "evidence": c["text"] + " (" + c["url"] + ")"}
def block(fin):
    return {"forecast.sales_growth": leaf(fin["sales_growth"]), "forecast.ebitda_growth": leaf(fin["ebitda_growth"]),
            "forecast.margin_path.me": leaf(fin["me"]), "forecast.margin_path.mc": leaf(fin["mc"]),
            "forecast.margin_path.gsnext": leaf(fin["gsnext"]), "forecast.ebitda_basis": leaf(fin["ebitda_basis"]),
            "forecast.acquisition_disclosure.status": leaf(fin["acquisition_disclosure"]["status"])}
SCN = {"base": fc, "bull": fc["scenarios"]["bull"], "bear": fc["scenarios"]["bear"]}
req = json.loads((V10 / "valuation_request_v10.json").read_text())
req["version"], req["parent_version"] = "v11", "v10"
req["forecast_commit"] = "uncommitted (v11 forecast at /workspace/out/QURE_run_v11/forecast.json, built from forecasts/QURE on top of 52d4ce35301fdfde755ca8572d8ac62dc34017cc)"
req["forecaster"] = {n: block(SCN[n]["finagle"]) for n in ("base", "bull", "bear")}
D = "2026-10-30"; Q97 = "Write is up with m=0.62 its the most internally consistent"; Q98 = "Redo the finagle too"
# --- dry-case builder: v10 compiled cases with the v11 forecaster values swapped in ---
def case(n, sbc=None, capex=None, cash=None, shares=None, start=None):
    c = json.loads((V10 / ("case_%s_v10.json" % n)).read_text()); fb = req["forecaster"][n]
    for k, v in fb.items():
        node = c
        for p in k.split(".")[:-1]: node = node[p]
        node[k.split(".")[-1]]["value"] = v["value"]
    if sbc is not None: c["forecast"]["sbc"]["value"] = sbc
    if capex is not None: c["forecast"]["capex"]["value"] = capex
    if cash is not None: c["baseline"]["cash"]["value"] = cash
    if shares is not None: c["market"]["shares"]["value"] = shares
    if start is not None: c["debt"]["start_year"]["value"] = start
    return c
SBC0, PCT = 17.679, 0.05
def sbc_rule(rev, eb):
    out, pos = [], False
    for i, (r, e) in enumerate(zip(rev, eb)):
        pos = pos or (i > 0 and e > 0); out.append(round(SBC0 if not pos else PCT * r, 6))
    return out
PI = {(tuple(p["applies_to"]), p["path"]): p for p in req["prompt_inputs"]}
NEW, DRY = {}, {}
for n in ("base", "bull"):
    f0 = dry(case(n))
    fp = next(i for i in range(1, 11) if f0["ebitda"][i] > 0)
    s = sbc_rule(f0["revenue"], f0["ebitda"])
    f1 = dry(case(n, sbc=s, start=fp)); NEW[n] = dict(sbc=s, start=fp, rev=f0["revenue"], eb=f0["ebitda"]); DRY[n] = f1
BASECAPEX = [round(x, 6) for x in DRY["base"]["capex"]]
bc = PI[(("bear",), "baseline.cash")]["value"]; bs = PI[(("bear",), "market.shares")]["value"]
DRY["bear"] = dry(case("bear", capex=BASECAPEX))
PRICE, SH0, CASH0, R10 = 25.3, 62.529408, 80.24, 3250.0
R = R10; minb = min(DRY["bear"]["cash"])
if minb < 0:   # David t64u/t68u: cash must not go negative -> raise by the shortfall, rounded up to next $50M
    import math; R = R10 + math.ceil(-minb / 50.0) * 50.0
    DRY["bear"] = dry(case("bear", capex=BASECAPEX, cash=round(CASH0 + R, 2), shares=round(SH0 + R / PRICE, 6)))
for n in ("base", "bull"):
    p = PI[((n,), "forecast.sbc")]
    p.update(value=NEW[n]["sbc"], note=("v11: list recomputed on the v11 (pool model m = 0.62, CLPT ramp) revenue path with v10's rule unchanged: SBC $17.679M until the first EBITDA-positive Finagle year, then 5.0%% [S] x revenue. "
      "First positive year is now index %d (FY20%02dE). Revenue in Finagle years from a scratch dry compile of the read-only Finagle copy (gt 2%%, not a valuation): %s. Previous v10 note: " % (NEW[n]["start"], 25 + NEW[n]["start"], [round(x, 1) for x in NEW[n]["rev"]])) + p["note"])
for k in (("base", "bull"),):
    p = PI[(k, "debt.start_year")]; assert NEW["base"]["start"] == NEW["bull"]["start"]
    old = p["value"]; p.update(value=NEW["base"]["start"], note=("v11 mapping (follows the forecast, not a new instruction): first year v11 EBITDA is positive = index %d (FY20%02dE: base %.1f, bull %.1f). v10 used %d. Previous note: " % (NEW["base"]["start"], 25 + NEW["base"]["start"], NEW["base"]["eb"][NEW["base"]["start"]], NEW["bull"]["eb"][NEW["bull"]["start"]], old)) + p["note"])
    PI[(k, "debt.mode")]["note"] = p["note"]
p = PI[(("bear",), "forecast.capex")]
p.update(value=BASECAPEX, note=("v11: bear capex = base's dollar capex per year (v10 rule), re-derived from the v11 base path by Finagle method 1 in a scratch dry compile (not a valuation). Previous note: ") + p["note"])
if R != R10:
    for path, val in (("baseline.cash", round(CASH0 + R, 2)), ("market.shares", round(SH0 + R / PRICE, 6))):
        q = PI[(("bear",), path)]; q.update(value=val, note=("v11 SUPERSEDES v10 (bear raise $%.0fM): with bear capex = v11 base dollars, v10 bear cash would reach %.2f; raise increased by the shortfall rounded up to the next $50M = $%.0fM [S], per David t64u/t68u (cash never negative). Previous note: " % (R10, minb, R)) + q["note"])
UNDEC = req["undecided_by_david"]
MC = PRICE * SH0
UNDEC.append({"item": "v11 volume-path consistency flags", "risk": ("Base/bull year-0 raises ($400M/$350M) were sized for the old path; with EBITDA positive from FY2027E minimum year-end cash is now base %.1f / bull %.1f (dry), so the raises are larger than needed but kept (David's v10 values). "
  "Bear raise $%.0fM (~%.1fx market cap) driven by bear capex = base dollars (base capex now larger). Centers implied by CLPT capacity at 2/week: ~29 base, ~34-43 bull (opex $1.5M/center). Bull starts from the same 6,000 pool with unfiltered entrants (steady pool ~8,200), base entrants filtered x1.0045 to hold 6,000. "
  "m = 0.62 (stay ~1.6y) is shorter than the duration evidence (crossover 2 of 6 lost eligibility in ~1 year implies ~0.41/yr).") % (min(DRY["base"]["cash"]), min(DRY["bull"]["cash"]), R, R / MC)})
req["note"] = ("v11 = v10 + forecast rev4 (David t97u 2026-10-30 \"" + Q97 + "\", t98u \"" + Q98 + "\"): AMT-130 US treated from the pool model at m = 0.62 (start pool 6,000, P 0.729, g 0.5%%, quarterly, launch 2027-07-01) "
  "with capacity = CLPT ramp 330/2,500/3,000 cap (bull 880/4,500/3,500, bull inputs incidence 1.59, share 0.95, P 0.857); bear not approved. Forecaster block rebuilt. Mechanically re-derived with v10 rules: SBC lists, debt.start_year %d, bear capex = base dollars%s. "
  "Everything else carried from v10 (price, COGS/opex rules, capex method 1, NOL, da, gt 2%%, Dutch tax, rd 10%%, base/bull raises). Scratch dry check (not a valuation): min year-end cash base %.2f, bull %.2f, bear %.2f.") % (
  NEW["base"]["start"], (", bear raise $%.0fM" % R) if R != R10 else "", min(DRY["base"]["cash"]), min(DRY["bull"]["cash"]), min(DRY["bear"]["cash"]))
errs = check_request(req, fc); print("check_request:", errs); assert errs == [], errs
OUT.write_text(json.dumps(req, indent=1, ensure_ascii=False) + "\n")
def canon(o): return json.dumps(o, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
h = {"rule": "sha256 of json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False, allow_nan=False); sidecar only (repo defines no in-file hash)",
     "blocks": {k: hashlib.sha256(canon(v)).hexdigest() for k, v in req["forecaster"].items()},
     "prompt_inputs": hashlib.sha256(canon(req["prompt_inputs"])).hexdigest(),
     "whole_request": hashlib.sha256(canon(req)).hexdigest(),
     "file_bytes": hashlib.sha256(OUT.read_bytes()).hexdigest(),
     "forecast_json_bytes": hashlib.sha256(FC.read_bytes()).hexdigest()}
(HERE / "valuation_request_v11.sha256.json").write_text(json.dumps(h, indent=1) + "\n")
assert hashlib.sha256(canon(json.loads(OUT.read_text()))).hexdigest() == h["whole_request"]
# dry summary
L = ["v11 scratch dry check (read-only Finagle copy /workspace/out/finagle_scratch, dry11.py; NOT a valuation, Finagle bot not called)"]
for n in ("base", "bull", "bear"):
    for k in ("revenue", "ebitda", "capex", "da", "cash", "debt"): L.append("%s %s %s" % (n, k, [round(x, 2) for x in DRY[n][k]]))
    L.append("%s min cash %.2f, min D&A %.2f" % (n, min(DRY[n]["cash"]), min(DRY[n]["da"])))
L.append("bear raise $%.0fM (v10 $%.0fM)" % (R, R10))
(HERE / "dry_v11_summary.txt").write_text("\n".join(L) + "\n")
json.dump({n: DRY[n] for n in DRY}, open(HERE / "dry_v11.json", "w"), indent=1)
print("\n".join(L)); print(json.dumps(h, indent=1))
