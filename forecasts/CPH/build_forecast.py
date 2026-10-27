"""Cipher Pharmaceuticals (TSX: CPH) near-term forecast. USD millions (Cipher reports in USD).
Every fact carries the skill tag plus a numbered source id (A1, G1, E1, S1, C1...) that points
to the numbered source list in forecast.md. Run: python3 build_forecast.py"""
import json
from pathlib import Path

OUT = Path(__file__).with_name("forecast.json")
Q2R = "https://www.cipherpharma.com/wp-content/uploads/2026/08/Cipher-Quarterly-Report-Q2-2026.pdf"
AR = "https://www.cipherpharma.com/wp-content/uploads/2026/03/Cipher-Annual-Report-2025.pdf"
TR = "https://stockanalysis.com/quote/tsx/CPH/transcripts/663762-q2-2026/"
YH = "https://finance.yahoo.com/quote/CPH.TO/analysis/"

# ---- actuals, thousands -> millions [A]
FY24 = {"Natroba (U.S. product)": 11.950, "Canadian product portfolio": 14.790, "Licensing (U.S.)": 6.623}
FY25 = {"Natroba (U.S. product)": 29.990, "Canadian product portfolio": 16.907, "Licensing (U.S.)": 3.554}
H1_25 = {"Natroba (U.S. product)": 14.444, "Canadian product portfolio": 8.743, "Licensing (U.S.)": 2.213}
H1 = {"Natroba (U.S. product)": 13.187, "Canadian product portfolio": 9.121, "Licensing (U.S.)": 2.264}
NAMES = list(FY25)
FY24_EBITDA, FY25_EBITDA, H1_EBITDA = 15.684, 28.057, 14.552
FY24_GP = 33.363 - 9.260
FY25_GP = 50.451 - 10.029
H1_GP = 19.996
Q2_SGA, Q2_SBC, Q2_ACQ, Q2_GP = 3.439, 0.323, 0.259, 9.699
OPEX_Q = Q2_SGA - Q2_SBC - Q2_ACQ  # cash opex; R&D nil
assert abs(Q2_GP - OPEX_Q - 6.842) < 0.001
H2_25 = {n: FY25[n] - H1_25[n] for n in NAMES}

# line gross margins [A] H1 2026 (Natroba 86%, Canada 71%); licensing is the residual [C]
GM_H1 = {"Natroba (U.S. product)": 0.86, "Canadian product portfolio": 0.71}
GM_H1["Licensing (U.S.)"] = (H1_GP - sum(H1[n] * GM_H1[n] for n in GM_H1)) / H1["Licensing (U.S.)"]
GM_Q2 = {"Natroba (U.S. product)": 0.84, "Canadian product portfolio": 0.70, "Licensing (U.S.)": GM_H1["Licensing (U.S.)"]}

# ---- unscaled line drivers [S]
NAT_H2_G = H1["Natroba (U.S. product)"] / H1_25["Natroba (U.S. product)"] - 1   # H1 YoY, -8.7%
CAN_H2_G = 4.628 / 4.138 - 1                                                    # Q2 YoY, +11.8%
H2_U = {
    "Natroba (U.S. product)": H2_25["Natroba (U.S. product)"] * (1 + NAT_H2_G),
    "Canadian product portfolio": H2_25["Canadian product portfolio"] * (1 + CAN_H2_G),
    "Licensing (U.S.)": H2_25["Licensing (U.S.)"],
}
G27 = {"Natroba (U.S. product)": 0.03, "Canadian product portfolio": 0.10, "Licensing (U.S.)": -0.10}
F27_U = {n: (H1[n] + H2_U[n]) * (1 + G27[n]) for n in NAMES}

# ---- consensus [E], Yahoo shows CAD; converted at Yahoo's own implied rate
FX = 68.72536 / 50.451  # Yahoo FY25 'year ago revenue' CAD / reported FY25 USD
CONS = {"base": (70.84948, 81.35280), "bear": (70.297, 74.94468), "bull": (71.26395, 92.37638)}
H1_REV = sum(H1.values())

def fact(v, tag, sid, text, url, page=None):
    if isinstance(v, float): v = round(v, 6)
    if isinstance(v, list): v = [round(x, 6) for x in v]
    c = {"id": sid, "text": text, "url": url}
    if page is not None: c["page"] = page
    return {"value": v, "tag": tag, "citation": c}

def scenario(key, gm, infl):
    r26, r27 = (x / FX for x in CONS[key])
    h2t = r26 - H1_REV
    k26, k27 = h2t / sum(H2_U.values()), r27 / sum(F27_U.values())
    h2 = {n: H2_U[n] * k26 for n in NAMES}
    fy26 = {n: H1[n] + h2[n] for n in NAMES}
    fy27 = {n: F27_U[n] * k27 for n in NAMES}
    gp_h2 = sum(h2[n] * gm[n] for n in NAMES)
    gp27 = sum(fy27[n] * gm[n] for n in NAMES)
    opex_h2, opex27 = 2 * OPEX_Q, 4 * OPEX_Q * (1 + infl)
    e26 = H1_EBITDA + gp_h2 - opex_h2
    e27 = gp27 - opex27
    return dict(r26=r26, r27=r27, k26=k26, k27=k27, h2=h2, fy26=fy26, fy27=fy27, gp26=H1_GP + gp_h2, gp27=gp27,
                e26=e26, e27=e27, opex_h2=opex_h2, opex27=opex27, gm=gm, infl=infl,
                gf=[e26 / FY25_EBITDA - 1, e27 / e26 - 1], sg=[r26 / sum(FY25.values()) - 1, r27 / r26 - 1])

SID_LINE = {  # (FY24/FY25 source id, H1 source id, H2 driver id, FY27 driver id)
    "Natroba (U.S. product)": ("A2", "A6", "S1", "S2"),
    "Canadian product portfolio": ("A2", "A6", "S3", "S4"),
    "Licensing (U.S.)": ("A2", "A6", "S5", "S6"),
}

def lines(s):
    out = []
    for n in NAMES:
        a, h, sh2, s27 = SID_LINE[n]
        out.append({"name": n, "periods": {
            "FY24A": fact(FY24[n], "A", "A2", "FY2024 column, segment note (Note 19), 2025 annual report.", AR, 83),
            "FY25A": fact(FY25[n], "A", "A2", "FY2025 column, segment note (Note 19), 2025 annual report.", AR, 83),
            "YoY": fact(FY25[n] / FY24[n] - 1, "C", "C1", "FY25A / FY24A - 1 (A2).", AR, 83),
            "H1A": fact(H1[n], "A", "A6", "Six months ended June 30, 2026, segment note (Note 15), Q2 2026 report.", Q2R, 39),
            "H2E": fact(s["h2"][n], "S", sh2, "Unscaled H2 driver x scale C5. See source list.", Q2R, 8),
            "FY26E": fact(s["fy26"][n], "C", "C6", "H1A (A6) + H2E.", Q2R, 39),
            "FY27E": fact(s["fy27"][n], "S", s27, "Unscaled FY27 driver x scale C7. See source list.", Q2R, 8),
        }, "gross_margin": fact(s["gm"][n], "A" if n != "Licensing (U.S.)" else "C",
                                 {"Natroba (U.S. product)": "A9", "Canadian product portfolio": "A9", "Licensing (U.S.)": "C8"}[n],
                                 "Line gross margin used for H2 and FY27.", Q2R, 9)})
    return out

def totals(s, label):
    return {
        "revenue": {
            "FY24A": fact(33.363, "A", "A1", "Net revenue 2024, 2025 annual report.", AR, 8),
            "FY25A": fact(50.451, "A", "A1", "Net revenue 2025, 2025 annual report.", AR, 8),
            "YoY": fact(50.451 / 33.363 - 1, "C", "C1", "A1 FY25 / FY24 - 1.", AR, 8),
            "H1A": fact(H1_REV, "A", "A5", "Net revenue YTD Q2 2026.", Q2R, 5),
            "H2E": fact(s["r26"] - H1_REV, "C", "C4", "E1 FY26 consensus (USD) - A5.", YH),
            "FY26E": fact(s["r26"], "E", "E1", label + " FY26 revenue consensus, Yahoo/yfinance 2026-10-22, CAD converted at C3.", YH),
            "FY27E": fact(s["r27"], "E", "E1", label + " FY27 revenue consensus, Yahoo/yfinance 2026-10-22, CAD converted at C3.", YH),
        },
        "gross_margin": {
            "FY25A": fact(FY25_GP / 50.451, "C", "C9", "(A1 revenue - A3 cost of products sold) / revenue.", AR, 9),
            "H1A": fact(H1_GP / H1_REV, "A", "A5", "Gross profit 19,996 / net revenue 24,572, YTD Q2 2026.", Q2R, 5),
            "FY26E": fact(s["gp26"] / s["r26"], "C", "C10", "(A5 H1 gross profit + sum of H2 line revenue x line margin) / FY26 revenue.", Q2R, 9),
            "FY27E": fact(s["gp27"] / s["r27"], "C", "C10", "Sum of FY27 line revenue x line margin / FY27 revenue.", Q2R, 9),
        },
        "ebitda": {
            "FY24A": fact(FY24_EBITDA, "A", "A4", "Adjusted EBITDA 2024 reconciliation.", AR, 14),
            "FY25A": fact(FY25_EBITDA, "A", "A4", "Adjusted EBITDA 2025 reconciliation.", AR, 14),
            "YoY": fact(FY25_EBITDA / FY24_EBITDA - 1, "C", "C1", "A4 FY25/FY24 - 1.", AR, 14),
            "H1A": fact(H1_EBITDA, "A", "A7", "Adjusted EBITDA six months ended June 30, 2026.", Q2R, 13),
            "H2E": fact(s["e26"] - H1_EBITDA, "C", "C11", "H2 gross profit (C10 inputs) - 2 x Q2 cash opex C2.", Q2R, 10),
            "FY26E": fact(s["e26"], "C", "C11", "A7 + H2E. No EBITDA guidance or EBITDA consensus.", Q2R, 13),
            "FY27E": fact(s["e27"], "S", "S7", "FY27 gross profit - 4 x C2 x (1 + inflation S7).", Q2R, 10),
        },
        "ebitda_margin": {
            "FY25A": fact(FY25_EBITDA / 50.451, "C", "C12", "A4 / A1.", AR, 14),
            "H1A": fact(H1_EBITDA / H1_REV, "C", "C12", "A7 / A5.", Q2R, 13),
            "FY26E": fact(s["e26"] / s["r26"], "C", "C12", "C11 / E1.", Q2R, 13),
            "FY27E": fact(s["e27"] / s["r27"], "C", "C12", "S7 / E1.", Q2R, 13),
        },
    }

def leaves(s):
    me = s["e27"] / s["r27"]
    mc = (me + s["gp27"] / s["r27"]) / 2
    return ({"revenue": {"FY25A": fact(50.451, "A", "A1", "Organic = total; no deal in the window.", AR, 8),
                         "FY26E": fact(s["r26"], "E", "E1", "Organic = total.", YH),
                         "FY27E": fact(s["r27"], "E", "E1", "Organic = total.", YH)},
             "ebitda": {"FY25A": fact(FY25_EBITDA, "A", "A4", "Organic = total.", AR, 14),
                        "FY26E": fact(s["e26"], "C", "C11", "Organic = total.", Q2R, 13),
                        "FY27E": fact(s["e27"], "S", "S7", "Organic = total.", Q2R, 10)}},
            {"note": "Operating-path leaves the skill requires in the file. NOT handed to Finagle; no valuation run.",
             "ebitda_growth": fact(s["gf"], "C", "C13", "Organic adjusted EBITDA growth FY26, FY27 (A4, C11, S7).", Q2R, 13),
             "sales_growth": fact(s["sg"], "C", "C13", "Organic revenue growth FY26, FY27 (A1, E1).", YH),
             "me": fact(me, "C", "C14", "FY27 EBITDA / FY27 revenue.", Q2R, 13),
             "mc": fact(mc, "S", "S8", "Average of me and FY27 gross margin.", Q2R, 9),
             "gsnext": fact(0.05, "S", "S9", "First growth after FY27; see S9.", TR)})

def main():
    base = scenario("base", GM_H1, 0.03)
    bear = scenario("bear", GM_Q2, 0.08)
    bull = scenario("bull", GM_H1, 0.00)
    def block(s, label):
        org, fin = leaves(s)
        return {"lines": lines(s), "totals": totals(s, label), "organic": org, "finagle": fin}
    top = block(base, "Mean")
    payload = {"ticker": "CPH", "company": "Cipher Pharmaceuticals Inc. (TSX: CPH)", "units": "USD millions",
               "currency_note": "Cipher reports in USD. Yahoo consensus is shown in CAD and converted at C3.",
               "baseline_period": "FY25A", "explicit_periods": ["FY26E", "FY27E"], "as_of": "2026-10-22", **top,
               "bridge": {
                   "fx_cad_per_usd": fact(FX, "C", "C3", "Yahoo FY25 'year ago revenue' CAD 68.725 / reported FY25 USD 50.451 (A1).", YH),
                   "q2_cash_opex": fact(OPEX_Q, "C", "C2", "Q2 SG&A 3.439 - SBC 0.323 - acquisition/restructuring 0.259 (A8); R&D nil. Check: Q2 GP 9.699 - 2.857 = 6.842 = reported Q2 adjusted EBITDA.", Q2R, 10),
                   "scale_h2": fact(base["k26"], "C", "C5", "Consensus H2 / unscaled H2 line build.", YH),
                   "scale_fy27": fact(base["k27"], "C", "C7", "FY27 consensus / unscaled FY27 line build.", YH),
                   "licensing_gm": fact(GM_H1["Licensing (U.S.)"], "C", "C8", "(H1 gross profit A5 - Natroba and Canada line GP at A9 margins) / H1 licensing revenue A6.", Q2R, 9),
                   "unscaled_h2": fact(sum(H2_U.values()), "S", "S1", "Sum of S1, S3, S5 drivers (diagnostic only).", Q2R, 8),
                   "unscaled_fy27": fact(sum(F27_U.values()), "S", "S2", "Sum of S2, S4, S6 drivers (diagnostic only).", Q2R, 8)},
               "scenarios": {"bear": block(bear, "Low"), "bull": block(bull, "High")}}
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    for lab, s in (("bear", bear), ("base", base), ("bull", bull)):
        print(lab, {k: (round(v, 4) if isinstance(v, float) else {n: round(x, 3) for n, x in v.items()} if isinstance(v, dict) else [round(x, 4) for x in v] if isinstance(v, list) else v)
                    for k, v in s.items() if k not in ("gm",)})
        print("  gm26", round(s["gp26"] / s["r26"], 4), "gm27", round(s["gp27"] / s["r27"], 4), "em", round(s["e26"] / s["r26"], 4), round(s["e27"] / s["r27"], 4))
    print("FX", FX, "opex", OPEX_Q, "licGM", GM_H1["Licensing (U.S.)"], "H2U", H2_U, sum(H2_U.values()), "F27U", F27_U, sum(F27_U.values()))
    print("mc", leaves(base)[1]["mc"]["value"], "me", leaves(base)[1]["me"]["value"])

if __name__ == "__main__":
    main()
