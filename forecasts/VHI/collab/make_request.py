import json, sys
sys.path.insert(0, "/workspace/forecaster-work/forecaster-main-20261110")
from forecastcheck.collaborative import check_request
H="/workspace/forecaster-work/output/VHI/2026-11-17/"
fj = json.load(open(H+"forecast.json"))
MAP = {"sales_growth": "forecast.sales_growth", "ebitda_growth": "forecast.ebitda_growth", "me": "forecast.margin_path.me",
       "mc": "forecast.margin_path.mc", "gsnext": "forecast.margin_path.gsnext", "ebitda_basis": "forecast.ebitda_basis"}
def block(fb, base):
    out = {}
    for k, path in MAP.items():
        f = fb.get(k) or base[k]
        out[path] = {"value": f["value"], "tag": f["tag"], "cite_id": f["citation"]["id"], "evidence": f["citation"]["text"]}
    st = base["acquisition_disclosure"]["status"]
    out["forecast.acquisition_disclosure.status"] = {"value": st["value"], "tag": st["tag"], "cite_id": st["citation"]["id"], "evidence": st["citation"]["text"]}
    return out
F=fj["finagle"]
req = {
    "mode": "collaborative", "ticker": "VHI.TO", "version": "v01", "parent_version": None,
    "forecast_commit": "uncommitted (live case %sforecast.json, v3 of 18 Nov 2026; forecaster method 3a46f0a61f6b26de1a588acbc941120420d2ec41)" % H,
    "scenarios": ["base", "bull", "bear"],
    "forecaster": {"base": block(F, F), "bull": block(fj["scenarios"]["bull"]["finagle"], F), "bear": block(fj["scenarios"]["bear"]["finagle"], F)},
    "prompt_inputs": [],
    "cash_share_adjustments": fj["cash_share_adjustments"],
    "post_finagle": None,
}
errs = check_request(req, fj)
print("check_request errors:", errs)
json.dump(req, open(H+"finagle-run/valuation_request_v01.json", "w"), indent=1, ensure_ascii=False)
