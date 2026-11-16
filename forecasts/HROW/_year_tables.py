import json
from pathlib import Path

r = json.loads(Path("forecasts/HROW/collab/valuation_result_v02.json").read_text(encoding="utf-8"))


def cell(x, kind="m"):
    if kind == "ps":
        return f"{x:.2f}"
    ax = abs(x)
    if ax >= 100:
        return f"{round(x):,}"
    return f"{x:.1f}"


keys = [
    ("revenue", "m"),
    ("ebitda", "m"),
    ("capex", "m"),
    ("MnA", "m"),
    ("dDebt", "m"),
    ("fcf", "m"),
    ("fcfe", "m"),
    ("fcff", "m"),
    ("debt", "m"),
    ("cash", "m"),
    ("cashBS", "m"),
    ("shares", "m"),
    ("dividend", "ps"),
    ("equity", "m"),
    ("firm", "m"),
]
labels = {
    "revenue": "Revenue",
    "ebitda": "EBITDA",
    "capex": "Capex",
    "MnA": "M&A",
    "dDebt": "Debt change",
    "fcf": "FCF",
    "fcfe": "FCFE",
    "fcff": "FCFF",
    "debt": "Debt",
    "cash": "Cash (cumulative retained FCFE)",
    "cashBS": "Balance-sheet cash",
    "shares": "Shares (millions)",
    "dividend": "Dividend per share (US$)",
    "equity": "Equity value",
    "firm": "Firm value",
}
lines = []
for name in ["base", "bull", "bear"]:
    years = r["scenarios"][name]["years"]
    lines.append("## " + name)
    for a, b in [(0, 6), (6, 11)]:
        cols = years[a:b]
        heads = []
        for y in cols:
            heads.append("FY2025A" if y["year"] == 0 else "FY%dE" % (2025 + y["year"]))
        lines.append("| | " + " | ".join(heads) + " |")
        for k, kind in keys:
            if name != "base" and k in ("MnA", "fcf", "fcff", "cash", "cashBS", "shares", "firm"):
                continue
            row = " | ".join(cell(y[k], kind) for y in cols)
            lines.append("| " + labels[k] + " | " + row + " |")
        lines.append("")
Path("forecasts/HROW/_year_tables.md").write_text("\n".join(lines), encoding="utf-8")
print("wrote", len(lines))
