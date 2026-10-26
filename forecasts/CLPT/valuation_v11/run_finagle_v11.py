"""CLPT v11 (v10 with cost of equity = Finagle default 10yr + 5.5% ERP, re left unset, re 12%; dilution x0.90 applied post hoc outside Finagle) (David 2026-10-26): explicit EBITDA growth ends FY2031 (year 6); gsnext = 0.20 fades to Finagle's default gt by FY2040 (year = 15).
Otherwise v4 settings. Also runs a v4-equivalent bear (year 20, FY32 explicit end) for comparison. Builds cases from origin/main run_finagle.py."""
import json, copy
from pathlib import Path
CLPT = Path("/workspace/forecaster-work/fc-clpt-val/forecasts/CLPT")
OUT = Path("/workspace/out/clpt_val_v11")
ns = {"__file__": str(CLPT / "run_finagle.py")}
exec((CLPT / "run_finagle.py").read_text().split("out = {}")[0], ns)
leaf, case_for, fc = ns["leaf"], ns["case_for"], ns["fc"]
validate_case, run_case = ns["validate_case"], ns["run_case"]
P = "prompt"
BLOCKS = {"base": fc, "bull": fc["scenarios"]["bull"], "bear": fc["scenarios"]["bear"]}

def first_pos(ebitda):
    return next(i for i, e in enumerate(ebitda) if i > 0 and e > 0)

def build(label, v6, sbc_list=None, start=3):
    b = BLOCKS[label]
    c = case_for(b, label)
    fo = c["forecast"]
    if v6:
        c["year"] = 15
        f = b["finagle"]; t = b["totals"]
        fo["ebitda_growth"] = leaf(f["ebitda_growth"]["value"][:6], "assumption", "forecaster %s FY26-FY31 (C11); explicit path ends FY2031 per David 2026-10-26" % label)
        fo["sales_growth"] = leaf(f["sales_growth"]["value"][:6], "assumption", "forecaster %s FY26-FY31 (C11)" % label)
        me31 = t["ebitda"]["FY31E"]["value"] / t["revenue"]["FY31E"]["value"]
        fo["margin_path"]["me"] = leaf(me31, "assumption", "forecaster %s FY31E EBITDA / FY31E revenue (end of explicit window)" % label)
        fo["margin_path"]["gsnext"] = leaf(0.15, P, "David 2026-10-26: sales growth 15% (about half FY2031 sales growth) in the first year after the explicit window (FY2032), fading to terminal growth by FY2040")
    c["debt"] = {"mode": leaf("target", P, "David 2026-10-26: +$50M draw in 2026; 2x Debt/EBITDA from first positive-EBITDA year"),
                 "values": leaf([49.077] + [99.077] * c["year"], P, "Baseline $49.077M (2025 10-K LongTermDebt) + $50M Oberland/TPC draw in 2026 (David 2026-10-26)"),
                 "leverage": leaf(2.0, P, "David 2026-10-26: 2x leverage"),
                 "start_year": leaf(start, P, "First forecast year with positive EBITDA in this case's run")}
    if RD: c["rates"]["rd"] = leaf(0.092, P, "David 2026-10-26 (assumption, avoids double counting): Oberland/TPC notes 8.25% minimum coupon (Q2 2026 10-Q) + ~0.7%/yr discount and issuance costs ($0.6M + $0.7M on the $30M first note over 6 years) + ~0.25%/yr revenue participation (0.525% of up to $50M net revenue on $105M) = ~9.2%")
    if RE: c["rates"]["re"] = leaf(0.12, P, "David 2026-10-26: cost of equity 12% (assumption)")
    c["rates"]["roict"] = leaf(0.25, P, "David 2026-10-26 (assumption): terminal-year ROIC 25%; more scale argues for lower capex/revenue")
    if sbc_list is not None:
        fo["sbc"] = leaf(sbc_list, P, "Assumption stated by David 2026-10-26: SBC $8M/yr through first positive-EBITDA year, then linear in dollars to 5% of terminal-year EBITDA; index 0 = FY2025A $8.18M (2025 10-K)")
    return c

def sbc_path(eb, start, Y, eT):
    sT = 0.05 * eT
    return [8.18] + [8.0] * start + [8.0 + (sT - 8.0) * (i - start) / (Y - start) for i in range(start + 1, Y + 1)]

def years_ebitda(r):
    return [y["ebitda"] for y in r["years"]] if isinstance(r["years"], list) and isinstance(r["years"][0], dict) else None

out = {}
RD, RE = True, False  # v11: re not overridden -> baseline default 0.055 + 10yr (David 2026-10-26: 10yr + ERP)
for tag, labels, v6 in (("v11", ("base", "bull", "bear"), True),):
    for label in labels:
        c0 = build(label, v6)                      # pass 1: EBITDA is independent of SBC and debt
        r0 = run_case(c0)
        eb = r0["_ebitda"] if "_ebitda" in r0 else None
        import pandas as pd
        nsb = {}; exec(r0["notebook_code"].replace("co.display_fin()", ""), nsb)
        eb = list(nsb["co"].fin["ebitda"])
        start = first_pos(eb); Y = c0["year"]
        c = build(label, v6, sbc_path(eb, start, Y, eb[Y]), start)
        v = validate_case(c)
        r = run_case(c)
        out[f"{label}_{tag}"] = {"validate": v, "result": r, "case": c, "start_year": start, "pass1_ebitda": eb}
        print(label, tag, "start", start, "errors", v.get("errors"), "missing", v.get("missing"), "warnings", v.get("warnings"), "flags", r.get("sanity_flags"), "vps", r["value_per_share"], r["value_per_share_DDM"])
json.dump(out, open(OUT / "finagle_run_v11.json", "w"), indent=1, default=str)

