"""Format Finagle v12 output rows for report Figures 9, 10a, 10b (same layout as v11)."""
import json
T = json.load(open("finagle_template_table_v12.json"))
def f(x):
    if abs(x) >= 100: return f"{x:,.0f}".replace("-", "−")
    s = f"{x:.1f}"; return ("−" + s[1:]) if s.startswith("-") and s != "-0.0" else s.replace("-0.0", "0.0")
LAB = [("revenue","Revenue"),("g","Revenue growth (derived)"),("ebitda","EBITDA"),("sbc","Stock-based compensation"),("interest","Interest"),
       ("income_pretax","Pre-tax Income"),("nol","Net Operating Loss (NOL)"),("tax_cash","Cash Taxes"),("capex","Capex"),("MnA","MnA"),("dwc","dWC"),
       ("dDebt","dDebt"),("fcf","FCF, 'Owners Earnings'"),("fcfe","FCFE"),("fcff","FCFF"),("firm","Firm, Intrinsic Value"),("debt","Debt, Market Value"),
       ("EV","Enterprise Value"),("equity","Equity, Intrinsic Value"),("cash","Cash"),("wacc","Cost of Capital, WACC"),("value_per_share","Intrinsic Value per Share (US$)")]
KEY = ["revenue","g","ebitda","sbc","interest","tax_cash","capex","debt","fcfe","equity","cash","value_per_share"]
def rows(case, a, b, keys):
    R = T[case]["rows"]; out = []
    for k, lab in LAB:
        if k not in keys: continue
        cells = []
        for i in range(a, b):
            if k == "g": cells.append("–" if i == 0 else f"{(R['revenue'][i]/R['revenue'][i-1]-1)*100:.1f}%")
            elif k == "wacc": cells.append(f"{R[k][i]*100:.1f}%")
            elif k == "value_per_share": cells.append(f"{R[k][i]:.2f}")
            else: cells.append(f(R[k][i]))
        out.append(f"| {lab} | " + " | ".join(cells) + " |")
    return "\n".join(out)
allk = [k for k, _ in LAB]
res = {"base_a": rows("base_v12",0,7,allk), "base_b": rows("base_v12",7,16,allk),
       "bull_a": rows("bull_v12",0,7,KEY), "bull_b": rows("bull_v12",7,16,KEY),
       "bear_a": rows("bear_v12",0,7,KEY), "bear_b": rows("bear_v12",7,16,KEY)}
json.dump(res, open("tables_v12.json","w"), indent=1)
if __name__ == "__main__":
    for k, v in res.items(): print("##", k); print(v)
