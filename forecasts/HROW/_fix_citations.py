from pathlib import Path

path = Path("forecasts/HROW/forecast.json")
text = path.read_text(encoding="utf-8")
vevye = (
    "FY2026E VEVYE = nine-month 2026 printed $90.033 million (A2) "
    "+ Q4 workbook $46.694 million (S1, P8) = $136.727 million."
)
c5 = (
    "Q4 2026E cash opex $68.258 = $59.258 + $5.0 (TYRVAYA partial) + $4.0 "
    "(G-MELT filing allowance). Q4 GAAP gross profit is the prior $98.648 plus "
    "80% of the VEVYE revenue change (46.694-50.080), equal to $95.939. "
    "Q4 Adjusted EBITDA 33.253 = 95.939 + amortization add-back $5.572 - "
    "cash opex $68.258. FY2026E Adjusted EBITDA 40.580 = 9M $7.327 + Q4 33.253. "
    "FY2026E GAAP gross profit = 9M $152.311 + Q4 $95.939 = $248.250; "
    "FY2026E GAAP gross margin 72.0% = 248.250 / 344.746."
)
c15 = (
    "The FY2026E bottom-up total of 344.746 is 5.254 below the exact $350 low end "
    "of the reaffirmed $350-365 range (C2 implied Q4 of 135.839-150.839 versus "
    "base Q4 130.585). The shortfall is not closed by a plug."
)
old_v = "FY2026E VEVYE = nine-month 2026 printed .033 million (A2) + Q4 workbook .694 million (S1, P8) = .727 million."
old_c5 = (
    "Q4 2026E cash opex .258 = .258 + .0 (TYRVAYA partial) + .0 (G-MELT filing allowance). "
    "Q4 GAAP gross profit is the prior .648 plus 80% of the VEVYE revenue change (46.694-50.080), "
    "equal to .939. Q4 Adjusted EBITDA 33.253 = 95.939 + amortization add-back .572 - cash opex .258. "
    "FY2026E Adjusted EBITDA 40.580 = 9M .327 + Q4 33.253. "
    "FY2026E GAAP gross profit = 9M .311 + Q4 .939 = .250; FY2026E GAAP gross margin 72.0% = 248.250 / 344.746."
)
old_c15 = (
    "The FY2026E bottom-up total of 344.746 is 5.254 below the exact  low end "
    "of the reaffirmed -365 range (C2 implied Q4 of 135.839-150.839 versus "
    "base Q4 130.585). The shortfall is not closed by a plug."
)
for old, new, name in ((old_v, vevye, "vevye"), (old_c5, c5, "c5"), (old_c15, c15, "c15")):
    count = text.count(old)
    print(name, count)
    if count == 0:
        raise SystemExit("missing " + name)
    text = text.replace(old, new)
path.write_text(text, encoding="utf-8")
print("ok")
