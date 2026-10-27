"""Copart (NASDAQ: CPRT) forecast, FY27E and FY28E (fiscal year ends July 31). USD millions.
Every fact carries the skill tag plus a numbered source id (A1, G1, E1, S1, C1...) that points to the
numbered source list in forecast.md. ACV Auctions (closed 2026-10-16) is a separate acquired line.
Run: python3 build_forecast.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from forecastcheck.validate import validate_payload

OUT = Path(__file__).with_name("forecast.json")
K10 = "https://www.sec.gov/Archives/edgar/data/900075/000119312526405731/cprt-20260731.htm"
Q4 = "https://www.sec.gov/Archives/edgar/data/900075/000119312526387902/cprt-ex99_1.htm"
DEAL = "https://www.sec.gov/Archives/edgar/data/900075/000119312526388064/d138322dex991.htm"
CLOSE = "https://www.sec.gov/Archives/edgar/data/900075/000119312526423478/d129535dex991.htm"
ACVQ2 = "https://www.sec.gov/Archives/edgar/data/1637873/000163787326000031/q2-26earningspressrelease.htm"
YH = "https://finance.yahoo.com/quote/CPRT/analysis/"
YHA = "https://finance.yahoo.com/quote/ACVA/analysis/"
PU = "page unverified (HTML filing, no page numbers)"

NAMES = ["U.S. service revenues", "U.S. vehicle sales", "International service revenues", "International vehicle sales"]
ACV = "ACV Auctions (acquired 2026-10-16)"
# ---- actuals [A1] 10-K segment note, $000 -> $M
FY24 = dict(zip(NAMES, (3126.102, 338.633, 434.900, 337.188)))
FY25 = dict(zip(NAMES, (3451.558, 403.546, 517.104, 274.750)))
FY26 = dict(zip(NAMES, (3388.287, 419.143, 581.233, 277.546)))
Q4_26 = dict(zip(NAMES, (817.822, 112.512, 151.722, 70.383)))   # [A4]
Q4_25 = dict(zip(NAMES, (824.813, 101.450, 131.396, 67.438)))   # [A4]
REV = {"FY24A": 4236.823, "FY25A": 4646.958, "FY26A": 4666.209}
GP = {"FY25A": 2099.643, "FY26A": 2083.858}                      # [A3] reported gross profit
OI = {"FY25A": 1696.714, "FY26A": 1652.590}                      # [A2]
DA = {"FY25A": 215.849, "FY26A": 229.373}                        # [A1] excl. debt costs
SBC = {"FY25A": 38.004, "FY26A": 38.818}                         # [A3] cash-flow statement
EB = {k: OI[k] + DA[k] + SBC[k] for k in OI}                     # [C2]
FAC_DA = {"FY25A": 191.775, "FY26A": 201.669}; FAC_SBC = {"FY25A": 8.107, "FY26A": 8.472}
CGM = {k: (GP[k] + FAC_DA[k] + FAC_SBC[k]) / REV[k] for k in GP}  # [C3] cash gross margin
Q4_REV, Q4_GP, Q4_FDA, Q4_FSBC, Q4_GA = 1152.439, 481.449, 53.759, 2.275, 97.813
CGM_Q4 = (Q4_GP + Q4_FDA + Q4_FSBC) / Q4_REV
GA_RUN = 4 * Q4_GA                                               # [C4]
GM_REP_FY26, GM_REP_Q4 = GP["FY26A"] / REV["FY26A"], Q4_GP / Q4_REV
for d in (FY24, FY25, FY26):
    pass
assert abs(sum(FY26.values()) - REV["FY26A"]) < 0.01 and abs(sum(FY25.values()) - REV["FY25A"]) < 0.01
assert abs(sum(FY24.values()) - REV["FY24A"]) < 0.01
assert abs(DA["FY26A"] - (201.669 + 27.704)) < 0.001

# ---- organic drivers [S1-S4]: FY27 growth, FY28 growth
G = {"U.S. service revenues": (0.02, 0.03), "U.S. vehicle sales": (0.03, 0.03),
     "International service revenues": (0.09, 0.09), "International vehicle sales": (0.01, 0.01)}
U27 = {n: FY26[n] * (1 + G[n][0]) for n in NAMES}
U28 = {n: U27[n] * (1 + G[n][1]) for n in NAMES}

# ---- ACV [A11, G1, G2, E2] calendar-year company, mapped to Copart fiscal years
ACV_H1, ACV_H1_E = 418.133, 37.868
ACV_CY26, ACV_CY26_E = 850.0, 75.0        # guidance midpoints [G1]
ACV_Q3, ACV_Q3_E = 222.0, 22.5            # guidance midpoints [G2]
ACV_Q4 = ACV_CY26 - ACV_H1 - ACV_Q3       # [C6]
ACV_Q4_E = ACV_CY26_E - ACV_H1_E - ACV_Q3_E
STUB = 77 / 92                            # Oct 16 - Dec 31 of Q4 CY26 (77 of 92 days) [S5]
ACV_CY27 = 937.50996                      # [E2]
ACV_G28 = 0.10                            # CY28 growth [S6]
A27 = ACV_Q4 * STUB + ACV_CY27 * 7 / 12
A28 = ACV_CY27 * 5 / 12 + ACV_CY27 * (1 + ACV_G28) * 7 / 12
ACV_GM = 1 - (165.324 + 40.702) / ACV_H1  # [C9] ACV cost of revenue excl. D&A, H1 CY26

CONS = {"base": (5487.76133, 6216.544), "bear": (5403.779, 6056.778), "bull": (5571.000, 6319.854)}  # [E1]
CASES = {  # cash GM, G&A FY27 vs run rate, G&A FY28 growth, ACV margin FY27/FY28 part, organic reported GM
    "base": dict(cgm=CGM["FY26A"], ga27=0.00, ga28=0.05, am=(0.10, 0.11), rgm=GM_REP_FY26),
    "bear": dict(cgm=CGM_Q4, ga27=0.03, ga28=0.07, am=(0.08, 0.09), rgm=GM_REP_Q4),
    "bull": dict(cgm=CGM["FY25A"], ga27=0.00, ga28=0.03, am=(0.11, 0.13), rgm=GP["FY25A"] / REV["FY25A"]),
}

def fact(v, tag, sid, text, url, page=PU):
    if isinstance(v, float): v = round(v, 6)
    if isinstance(v, list): v = [round(x, 6) for x in v]
    c = {"id": sid, "text": text, "url": url, "page": page}
    return {"value": v, "tag": tag, "citation": c}

def scenario(key):
    p = CASES[key]; r27, r28 = CONS[key]
    k27 = r27 / (sum(U27.values()) + A27); k28 = r28 / (sum(U28.values()) + A28)
    f27 = {n: U27[n] * k27 for n in NAMES}; f28 = {n: U28[n] * k28 for n in NAMES}
    a27, a28 = A27 * k27, A28 * k28
    o27, o28 = sum(f27.values()), sum(f28.values())
    ga27 = GA_RUN * (1 + p["ga27"]); ga28 = ga27 * (1 + p["ga28"])
    eo27, eo28 = p["cgm"] * o27 - ga27, p["cgm"] * o28 - ga28
    # ACV FY27: stub at Q4 CY26 guided margin, Jan-Jul 27 at case margin; FY28 blends CY27 and CY28 margins
    acv_stub = ACV_Q4 * STUB * k27
    ea27 = acv_stub * (ACV_Q4_E / ACV_Q4) + (a27 - acv_stub) * p["am"][0]
    ea28 = a28 * (5 / 12 * ACV_CY27) / A28 * p["am"][0] + a28 * (1 - (5 / 12 * ACV_CY27) / A28) * p["am"][1]
    gp27 = p["rgm"] * o27 + ACV_GM * a27; gp28 = p["rgm"] * o28 + ACV_GM * a28
    return dict(key=key, p=p, r27=r27, r28=r28, k27=k27, k28=k28, f27=f27, f28=f28, a27=a27, a28=a28,
                o27=o27, o28=o28, ga27=ga27, ga28=ga28, eo27=eo27, eo28=eo28, ea27=ea27, ea28=ea28,
                e27=eo27 + ea27, e28=eo28 + ea28, gp27=gp27, gp28=gp28)

LINE_SRC = {"U.S. service revenues": ("S1", "U.S. service FY27 +2%, FY28 +3% before scale"),
            "U.S. vehicle sales": ("S2", "U.S. vehicle sales +3% a year before scale"),
            "International service revenues": ("S3", "International service +9% a year before scale"),
            "International vehicle sales": ("S4", "International vehicle sales +1% a year before scale")}

def lines(s):
    out = []
    for n in NAMES:
        sid, txt = LINE_SRC[n]
        out.append({"name": n, "pattern": "mature" if "International service" not in n else "ramping (share gain abroad)", "periods": {
            "FY24A": fact(FY24[n], "A", "A1", "FY2024 column, segment table, FY2026 10-K notes.", K10),
            "FY25A": fact(FY25[n], "A", "A1", "FY2025 column, segment table, FY2026 10-K notes.", K10),
            "FY26A": fact(FY26[n], "A", "A1", "FY2026 column, segment table, FY2026 10-K notes.", K10),
            "YoY_FY26": fact(FY26[n] / FY25[n] - 1, "C", "C1", "FY26A / FY25A - 1 (A1).", K10),
            "Q4FY26A": fact(Q4_26[n], "A", "A4", "Three months ended July 31, 2026 segment table, Q4 release.", Q4),
            "YoY_Q4": fact(Q4_26[n] / Q4_25[n] - 1, "C", "C1", "Q4 FY26 / Q4 FY25 - 1 (A4).", Q4),
            "FY27E": fact(s["f27"][n], "S", sid, txt + " x scale C5.", K10),
            "FY28E": fact(s["f28"][n], "S", sid, txt + " x scale C5.", K10)}})
    out.append({"name": ACV, "pattern": "acquisition-driven", "periods": {
        "FY24A": fact(0.0, "A", "A13", "Not owned; closed 2026-10-16.", CLOSE),
        "FY25A": fact(0.0, "A", "A13", "Not owned; closed 2026-10-16.", CLOSE),
        "FY26A": fact(0.0, "A", "A13", "Not owned; closed 2026-10-16.", CLOSE),
        "FY27E": fact(s["a27"], "S", "S5", "ACV Oct 16-Dec 31 2026 (C6 x 77/92) + 7/12 of CY27 consensus E2, x scale C5.", ACVQ2),
        "FY28E": fact(s["a28"], "S", "S6", "5/12 of CY27 E2 + 7/12 of CY27 x (1 + 10%), x scale C5.", YHA)}})
    return out

def totals(s, label):
    return {
        "revenue": {
            "FY24A": fact(REV["FY24A"], "A", "A2", "Total service revenues and vehicle sales, FY2026 10-K income statement.", K10),
            "FY25A": fact(REV["FY25A"], "A", "A2", "Total service revenues and vehicle sales, FY2026 10-K.", K10),
            "FY26A": fact(REV["FY26A"], "A", "A2", "Total service revenues and vehicle sales, FY2026 10-K.", K10),
            "FY27E": fact(s["r27"], "E", "E1", label + " FY27 (Jul-27) revenue consensus, Yahoo/yfinance 2026-10-22 ('0y').", YH),
            "FY28E": fact(s["r28"], "E", "E1", label + " FY28 (Jul-28) revenue consensus, Yahoo/yfinance 2026-10-22 ('+1y').", YH)},
        "gross_margin": {
            "FY25A": fact(GP["FY25A"] / REV["FY25A"], "C", "C7", "Reported gross profit / revenue (A3).", Q4),
            "FY26A": fact(GM_REP_FY26, "C", "C7", "Reported gross profit 2,083.9 / revenue 4,666.2 (A3).", Q4),
            "FY27E": fact(s["gp27"] / s["r27"], "C", "C7", "Organic revenue x case reported GM + ACV x C9, / revenue.", Q4),
            "FY28E": fact(s["gp28"] / s["r28"], "C", "C7", "Organic revenue x case reported GM + ACV x C9, / revenue.", Q4)},
        "ebitda": {
            "FY25A": fact(EB["FY25A"], "C", "C2", "Operating income + D&A + SBC (A1, A2, A3). Copart does not report adjusted EBITDA.", K10),
            "FY26A": fact(EB["FY26A"], "C", "C2", "Operating income 1,652.6 + D&A 229.4 + SBC 38.8 (A1, A2, A3).", K10),
            "FY27E": fact(s["e27"], "S", "S7", "Organic: cash GM C3 x organic revenue - G&A C4; plus ACV at S8 margin.", Q4),
            "FY28E": fact(s["e28"], "S", "S7", "Organic: cash GM C3 x organic revenue - G&A C4 x growth; plus ACV at S8.", Q4)},
        "ebitda_margin": {
            "FY25A": fact(EB["FY25A"] / REV["FY25A"], "C", "C8", "C2 / A2.", K10),
            "FY26A": fact(EB["FY26A"] / REV["FY26A"], "C", "C8", "C2 / A2.", K10),
            "FY27E": fact(s["e27"] / s["r27"], "C", "C8", "S7 / E1.", K10),
            "FY28E": fact(s["e28"] / s["r28"], "C", "C8", "S7 / E1.", K10)}}

def leaves(s):
    me = s["eo28"] / s["o28"]; mc = (me + s["p"]["rgm"]) / 2
    org = {"note": "Organic = Copart excluding ACV.",
           "revenue": {"FY26A": fact(REV["FY26A"], "A", "A2", "FY26 total = organic.", K10),
                       "FY27E": fact(s["o27"], "C", "C10", "Sum of four Copart lines, scaled.", YH),
                       "FY28E": fact(s["o28"], "C", "C10", "Sum of four Copart lines, scaled.", YH)},
           "ebitda": {"FY26A": fact(EB["FY26A"], "C", "C2", "FY26 adjusted EBITDA (analyst-defined).", K10),
                      "FY27E": fact(s["eo27"], "S", "S7", "Organic EBITDA, cash GM x organic revenue - G&A.", Q4),
                      "FY28E": fact(s["eo28"], "S", "S7", "Organic EBITDA, cash GM x organic revenue - G&A.", Q4)},
           "acquired": {"revenue": {"FY27E": fact(s["a27"], "S", "S5", "ACV line.", ACVQ2), "FY28E": fact(s["a28"], "S", "S6", "ACV line.", YHA)},
                        "ebitda": {"FY27E": fact(s["ea27"], "S", "S8", "ACV adjusted EBITDA contribution.", ACVQ2), "FY28E": fact(s["ea28"], "S", "S8", "ACV adjusted EBITDA contribution.", ACVQ2)}}}
    fin = {"note": "Operating-path leaves required by the skill. NOT handed to Finagle; no valuation run.",
           "ebitda_growth": fact([s["eo27"] / EB["FY26A"] - 1, s["eo28"] / s["eo27"] - 1], "C", "C11", "Organic EBITDA growth FY27, FY28.", K10),
           "sales_growth": fact([s["o27"] / REV["FY26A"] - 1, s["o28"] / s["o27"] - 1], "C", "C11", "Organic revenue growth FY27, FY28.", K10),
           "me": fact(me, "C", "C12", "FY28 organic EBITDA / organic revenue.", K10),
           "mc": fact(mc, "S", "S10", "Average of me and organic reported gross margin.", Q4),
           "gsnext": fact(0.05, "S", "S9", "Organic growth after FY28; see S9.", K10)}
    return org, fin

def selfcheck(s):
    for per, key in (("FY27E", "f27"), ("FY28E", "f28")):
        tot = sum(s[key].values()) + s["a" + per[2:4]]
        assert abs(tot - s["r" + per[2:4]]) < 0.01, (per, tot)
    o, f = leaves(s)
    lv = REV["FY26A"]
    for r, nm in zip(f["sales_growth"]["value"], ("FY27E", "FY28E")):
        lv *= 1 + r; assert abs(lv - o["revenue"][nm]["value"]) < 0.02
    lv = EB["FY26A"]
    for r, nm in zip(f["ebitda_growth"]["value"], ("FY27E", "FY28E")):
        lv *= 1 + r; assert abs(lv - o["ebitda"][nm]["value"]) < 0.02

def main():
    S = {k: scenario(k) for k in CASES}
    for s in S.values(): selfcheck(s)
    def block(s, label):
        org, fin = leaves(s)
        return {"lines": lines(s), "totals": totals(s, label), "organic": org, "finagle": fin}
    b = S["base"]
    payload = {"ticker": "CPRT", "company": "Copart, Inc. (NASDAQ: CPRT)", "units": "USD millions",
               "fiscal_year_end": "July 31", "baseline_period": "FY26A", "explicit_periods": ["FY27E", "FY28E"],
               "period_note": "True fiscal labels kept. validate.py DOLLAR_PERIODS only sums FY24A/FY25A/FY27E and _compounds needs FY25A; build_forecast.py self-checks FY26A/FY28E sums and compounding.",
               "as_of": "2026-10-22", **block(b, "Mean"),
               "bridge": {
                   "cash_gross_margin_fy26": fact(CGM["FY26A"], "C", "C3", "(Gross profit 2,083.9 + facility D&A 201.7 + facility SBC 8.5) / revenue 4,666.2 (A3).", Q4),
                   "cash_gross_margin_q4": fact(CGM_Q4, "C", "C3", "(Q4 gross profit 481.4 + facility D&A 53.8 + SBC 2.3) / Q4 revenue 1,152.4 (A3).", Q4),
                   "cash_gross_margin_fy25": fact(CGM["FY25A"], "C", "C3", "FY25 equivalent (A3).", Q4),
                   "ga_run_rate": fact(GA_RUN, "C", "C4", "4 x Q4 G&A ex D&A and SBC 97.813 (A3).", Q4),
                   "scale_fy27": fact(b["k27"], "C", "C5", "E1 FY27 / (unscaled Copart lines + ACV S5).", YH),
                   "scale_fy28": fact(b["k28"], "C", "C5", "E1 FY28 / (unscaled Copart lines + ACV S6).", YH),
                   "acv_q4cy26_rev": fact(ACV_Q4, "C", "C6", "G1 midpoint 850 - A11 H1 418.1 - G2 midpoint 222.", ACVQ2),
                   "acv_q4cy26_ebitda": fact(ACV_Q4_E, "C", "C6", "G1 midpoint 75 - A11 H1 37.9 - G2 midpoint 22.5.", ACVQ2),
                   "acv_gross_margin": fact(ACV_GM, "C", "C9", "1 - (165.3 + 40.7) / 418.1, ACV H1 CY26 (A11).", ACVQ2),
                   "unscaled_fy27": fact(sum(U27.values()) + A27, "S", "S1", "Diagnostic only.", K10),
                   "unscaled_fy28": fact(sum(U28.values()) + A28, "S", "S1", "Diagnostic only.", K10)},
               "scenarios": {"bear": block(S["bear"], "Low"), "bull": block(S["bull"], "High")}}
    res = validate_payload(payload); assert res["ok"], res["errors"]
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    for k, s in S.items():
        print(k, "k", round(s["k27"], 4), round(s["k28"], 4), "rev", round(s["r27"], 1), round(s["r28"], 1),
              "org", round(s["o27"], 1), round(s["o28"], 1), "acv", round(s["a27"], 1), round(s["a28"], 1),
              "EB", round(s["e27"], 1), round(s["e28"], 1), "m", round(s["e27"] / s["r27"], 4), round(s["e28"] / s["r28"], 4),
              "eo", round(s["eo27"], 1), round(s["eo28"], 1), "ea", round(s["ea27"], 1), round(s["ea28"], 1),
              "GM", round(s["gp27"] / s["r27"], 4), round(s["gp28"] / s["r28"], 4))
        print("   lines27", {n[:12]: round(v, 1) for n, v in s["f27"].items()}, "lines28", {n[:12]: round(v, 1) for n, v in s["f28"].items()})
    print("EB", EB, "CGM", CGM, "CGMQ4", CGM_Q4, "GA", GA_RUN, "ACVQ4", ACV_Q4, ACV_Q4_E, "A27", A27, "A28", A28, "ACVGM", ACV_GM, "U27", sum(U27.values()), "U28", sum(U28.values()))
    print("me", leaves(b)[1]["me"]["value"], "mc", leaves(b)[1]["mc"]["value"], "sg", leaves(b)[1]["sales_growth"]["value"], "eg", leaves(b)[1]["ebitda_growth"]["value"])

if __name__ == "__main__":
    main()
