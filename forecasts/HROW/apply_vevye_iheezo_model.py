"""Replace HROW VEVYE and IHEEZO with the 15 November 2026 workbook.

The workbook is ``Vevye and Iheezo model.xlsx`` in this folder, copied from
``C:\\Users\\david\\Documents\\Investing\\wd\\HROW\\Vevye and Iheezo model.xlsx``.

VEVYE TRx is in thousands. Revenue is price times TRx (thousands of dollars);
this script divides by 1,000 to store US$ millions. October and November use
that identity; the sheet's revenue row starts in December. Months after
December 2032 continue the same recurrences. FY2033 is only the next-period
growth year.

IHEEZO follows the IHEEZO sheet. Q4 2026 dollars use half, all, or none of the
2025 Q4 distributor/clinic seasonal effect for base, bull, and bear. Later
years are customer units times the sheet's 2027 ASP. The bear takes half of
each unit increment versus the normalized 2026 base. YOCHIL tracks the new
IHEEZO customer units. Do not run this twice.
"""

from __future__ import annotations

import csv
import json
import shutil
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
FORECAST = HERE / "forecast.json"
SNAPSHOT = HERE / "numbers_snapshot.json"
DRIVERS = HERE / "drivers.csv"
WORKBOOK_SRC = Path(r"C:\Users\david\Documents\Investing\wd\HROW\Vevye and Iheezo model.xlsx")

NINE_MONTH_VEVYE = 90.033
NINE_MONTH_IHEEZO = 42.833
NINE_MONTH_TRX = 864_142.0
SAME_STORE_BASE = 397.188
AMORT = {
    "FY27E": 24.0,
    "FY28E": 24.5,
    "FY29E": 25.0,
    "FY30E": 25.0,
    "FY31E": 25.0,
    "FY32E": 25.0,
}
PERIODS = ["Q4E", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E", "FY32E"]
YEARS = ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E", "FY32E"]
FORWARD = ["FY27E", "FY28E", "FY29E", "FY30E", "FY31E", "FY32E"]
GM = {
    "base": {"VEVYE": 0.80, "IHEEZO": 0.82, "YOCHIL": 0.72, "var": 0.04},
    "bull": {"VEVYE": 0.815, "IHEEZO": 0.835, "YOCHIL": 0.735, "var": 0.04},
    "bear": {"VEVYE": 0.77, "IHEEZO": 0.79, "YOCHIL": 0.69, "var": 0.08},
}
# Standing FY2033 steps for lines this workbook does not rebuild.
FY33_OTHER = {
    "base": {"TRIESENCE": 339.536, "Other branded products": 135.5, "Other revenues": 0.5,
             "ImprimisRx (compounding)": 79.0, "G-MELT (MELT-300)": 150.0},
    "bull": {"TRIESENCE": 339.536, "Other branded products": 151.76, "Other revenues": 0.56,
             "ImprimisRx (compounding)": 88.48, "G-MELT (MELT-300)": 280.0},
    "bear": {"TRIESENCE": 75.127, "Other branded products": 76.32, "Other revenues": 0.28,
             "ImprimisRx (compounding)": 44.4, "G-MELT (MELT-300)": 22.0},
}
GMELT = {
    "base": {"FY28E": 10.5, "FY29E": 45.0, "FY30E": 92.5, "FY31E": 142.5, "FY32E": 146.25},
    "bull": {"FY28E": 25.0, "FY29E": 90.0, "FY30E": 148.0, "FY31E": 209.0, "FY32E": 243.75},
    "bear": {"FY28E": 0.0, "FY29E": 0.0, "FY30E": 0.0, "FY31E": 8.0, "FY32E": 15.0},
}
YOCHIL_PEN = [60 / 750, 1 / 3, 2 / 3, 1.0, 1.0]
YOCHIL_BULL_PEN = [0.20, 0.50, 1.0, 1.0, 1.0]
YOCHIL_PRICE = [175, 180, 185, 190, 195]
YOCHIL_YEARS = [2028, 2029, 2030, 2031, 2032]


def r3(value: float) -> float:
    return round(value + 0.0, 3)


def ym(index: int) -> tuple[int, int]:
    month = 10 + index
    year = 2026 + (month - 1) // 12
    return year, (month - 1) % 12 + 1


def build_vevye(end_year: int, end_month: int, freeze_after: tuple[int, int] | None = None):
    """Monthly path. freeze_after holds share fixed after that calendar month."""
    n = (end_year - 2026) * 12 + (end_month - 10) + 1
    trx = [0.0] * n
    price = [0.0] * n
    share = [None] * n
    msize = [0.0] * n
    trx[0] = 118 * 1.05
    trx[1] = trx[0] * 1.05
    trx[2] = trx[1] * 1.05
    price[0] = 117.0
    for i in range(1, n):
        price[i] = price[i - 1] + (200.0 - price[i - 1]) * 0.03
    for i in range(3):
        msize[i] = 1200.0
    # January market-size factor is 1, so January equals December's 1,200 thousand TRx.
    msize[3] = 1200.0
    for i in range(4, n):
        msize[i] = msize[i - 1] * 1.01
    share[2] = trx[2] / msize[2]
    gain = 0.0057
    share[3] = share[2] + gain
    for i in range(4, n):
        gain *= 0.9
        share[i] = share[i - 1] + gain
    if freeze_after is not None:
        freeze_at = (freeze_after[0] - 2026) * 12 + (freeze_after[1] - 10)
        held = share[freeze_at]
        for i in range(freeze_at + 1, n):
            share[i] = held
    for i in range(3, n):
        trx[i] = share[i] * msize[i]
    by_year = defaultdict(lambda: {"rev_k": 0.0, "trx_k": 0.0, "end_share": None, "end_price": None})
    for i in range(n):
        year, _month = ym(i)
        bucket = by_year[year]
        bucket["rev_k"] += price[i] * trx[i]
        bucket["trx_k"] += trx[i]
        bucket["end_share"] = share[i]
        bucket["end_price"] = price[i]
    return by_year


def vevye_dollars(annual: dict, scale_from: dict | None = None) -> dict:
    q4 = r3(annual[2026]["rev_k"] / 1000.0)
    out = {"Q4E": q4, "FY26E": r3(NINE_MONTH_VEVYE + q4)}
    trx = {"FY26E": NINE_MONTH_TRX + annual[2026]["trx_k"] * 1000.0}
    for year, key in (
        (2027, "FY27E"), (2028, "FY28E"), (2029, "FY29E"),
        (2030, "FY30E"), (2031, "FY31E"), (2032, "FY32E"), (2033, "FY33E"),
    ):
        raw = r3(annual[year]["rev_k"] / 1000.0)
        if scale_from is not None and year >= 2027:
            raw = r3(scale_from[key] * 1.08)
        out[key] = raw
        trx[key] = annual[year]["trx_k"] * 1000.0
    out["trx"] = trx
    out["q4_trx"] = annual[2026]["trx_k"] * 1000.0
    out["end_share"] = {year: annual[year]["end_share"] for year in range(2026, 2034)}
    out["end_price"] = {year: annual[year]["end_price"] for year in range(2026, 2034)}
    out["avg_price"] = {}
    for key, rev in out.items():
        if key in trx and trx[key]:
            out["avg_price"][key] = rev * 1_000_000.0 / trx[key]
    out["avg_price"]["Q4E"] = q4 * 1_000_000.0 / out["q4_trx"]
    return out


def iheezo_units():
    order = ["Q4", "Q3", "Q2", "Q1"]
    reported = {"Q4": 62814.0, "Q3": 51545.0, "Q2": 48755.0, "Q1": 38931.0}
    rpu = {"Q4": 571.26, "Q3": 425.01, "Q2": 376.08, "Q1": 134.13}
    ex = {q: reported[q] * 0.75 for q in order}
    avg = sum(ex.values()) / 4.0
    season = {q: ex[q] / avg / 4.0 for q in order}
    increment = 62210.0 - ex["Q3"]
    norm = {q: ex[q] + increment / season["Q3"] * season[q] for q in order}
    units = {2026: sum(norm.values())}
    prev, prev_base = norm, ex
    for year in range(2027, 2034):
        nxt = {}
        for q in order:
            growth = (prev[q] / prev_base[q] - 1.0) / 2.0
            nxt[q] = prev[q] * (1.0 + growth)
        units[year] = sum(nxt.values())
        prev_base, prev = prev, nxt
    revenue_2025 = sum(reported[q] * rpu[q] for q in order)
    asp_2025 = revenue_2025 / sum(reported.values())
    asp = asp_2025 * 1.10
    ratio = rpu["Q4"] / asp_2025
    return {
        "units": units,
        "q4_units": norm["Q4"],
        "asp_2025": asp_2025,
        "asp": asp,
        "revenue_2025": revenue_2025,
        "reported_2025_units": sum(reported.values()),
        "q4_ratio": ratio,
        "half_mult": 1.0 + (ratio - 1.0) / 2.0,
        "norm_2026": units[2026],
        "growth_2026": units[2026] / sum(ex.values()) - 1.0,
    }


def iheezo_dollars(model: dict, q4_mult: float, unit_fn) -> dict:
    q4 = r3(model["q4_units"] * q4_mult * model["asp"] / 1_000_000.0)
    out = {"Q4E": q4, "FY26E": r3(NINE_MONTH_IHEEZO + q4)}
    units = {"Q4E": model["q4_units"], "FY26E": 248852.0}
    for year, key in (
        (2027, "FY27E"), (2028, "FY28E"), (2029, "FY29E"),
        (2030, "FY30E"), (2031, "FY31E"), (2032, "FY32E"), (2033, "FY33E"),
    ):
        level = unit_fn(year)
        units[key] = level
        out[key] = r3(level * model["asp"] / 1_000_000.0)
    out["units"] = units
    out["asp"] = model["asp"]
    return out


def yochil_dollars(units_by_year: dict, pens: list[float]) -> dict:
    out = {"Q4E": 0.0, "FY26E": 0.0, "FY27E": 0.0}
    stored_units = {"Q4E": 0.0, "FY26E": 0.0, "FY27E": 0.0}
    for year, pen, price, key in zip(YOCHIL_YEARS, pens, YOCHIL_PRICE, FORWARD[1:]):
        level = pen * units_by_year[year] / 3.0
        stored_units[key] = level
        out[key] = r3(level * price / 1_000_000.0)
    fy33_units = 1.0 * units_by_year[2033] / 3.0
    stored_units["FY33E"] = fy33_units
    out["FY33E"] = r3(fy33_units * 200.0 / 1_000_000.0)
    out["units"] = stored_units
    return out


def set_value(node: dict, value, text: str | None = None) -> None:
    node["value"] = value
    if text is not None and isinstance(node.get("citation"), dict):
        node["citation"]["text"] = text


def update_yoy(periods: dict, years: list[str], baseline: str) -> None:
    prev = periods[baseline]["value"]
    for year in years:
        key = "YoY_" + year
        node = periods.get(key)
        if isinstance(node, dict) and "value" in node and prev:
            set_value(node, round(periods[year]["value"] / prev - 1.0, 4))
        prev = periods[year]["value"]


def growth_rates(values: list[float]) -> list[float]:
    return [round(values[i] / values[i - 1] - 1.0, 9) for i in range(1, len(values))]


def compounds(start: float, rates: list[float], targets: list[float], label: str) -> None:
    level = start
    for rate, target in zip(rates, targets):
        level = level * (1.0 + rate)
        if abs(level - target) > 0.02:
            raise SystemExit("%s growth does not compound: %.6f vs %.6f" % (label, level, target))


RATE_KEY = {
    "VEVYE": "VEVYE",
    "IHEEZO": "IHEEZO",
    "YOCHIL (MELT-210)": "YOCHIL",
}


def apply_paths(block: dict, paths: dict, name: str) -> dict:
    rates = GM[name]
    old = {}
    new = {}
    for line_name, path in paths.items():
        line = next(item for item in block["lines"] if item["name"] == line_name)
        old[line_name] = {period: line["periods"][period]["value"] for period in PERIODS}
        new[line_name] = {period: path[period] for period in PERIODS}
        for period in PERIODS:
            set_value(line["periods"][period], path[period])
        update_yoy(line["periods"], YEARS, "FY25A")

    revenue = block["totals"]["revenue"]
    ebitda = block["totals"]["ebitda"]
    gross = block["totals"]["gross_margin"]
    old_rev = {period: revenue[period]["value"] for period in PERIODS}
    old_ebitda = {period: ebitda[period]["value"] for period in PERIODS}
    old_gm = {period: gross[period]["value"] for period in PERIODS}

    def delta(line_name, period):
        return new[line_name][period] - old[line_name][period]

    for period in PERIODS:
        moved = sum(delta(line_name, period) for line_name in paths)
        set_value(revenue[period], r3(old_rev[period] + moved))

    for period in ("Q4E", "FY26E"):
        # Fourth-quarter gross profit only. FY2026E cash opex stays the printed build.
        moved_gp = sum(rates[RATE_KEY[line_name]] * delta(line_name, "Q4E") for line_name in paths)
        if period == "Q4E":
            set_value(ebitda[period], r3(old_ebitda[period] + moved_gp))
        else:
            set_value(ebitda[period], r3(old_ebitda[period] + moved_gp))

    for year in FORWARD:
        moved_gp = 0.0
        variable = 0.0
        for line_name in paths:
            change = delta(line_name, year)
            moved_gp += rates[RATE_KEY[line_name]] * change
            if RATE_KEY[line_name] != "YOCHIL":
                variable += rates["var"] * change
        set_value(ebitda[year], r3(old_ebitda[year] + moved_gp - variable))

    q4_gp_old = old_gm["Q4E"] * old_rev["Q4E"]
    q4_gp = q4_gp_old + sum(rates[RATE_KEY[line_name]] * delta(line_name, "Q4E") for line_name in paths)
    set_value(gross["Q4E"], round(q4_gp / revenue["Q4E"]["value"], 6))
    nine_gp = old_gm["FY26E"] * old_rev["FY26E"] - q4_gp_old
    set_value(gross["FY26E"], round((nine_gp + q4_gp) / revenue["FY26E"]["value"], 6))
    for year in FORWARD:
        old_product_gp = old_gm[year] * old_rev[year] + AMORT[year]
        new_product_gp = old_product_gp + sum(rates[RATE_KEY[line_name]] * delta(line_name, year) for line_name in paths)
        set_value(gross[year], round((new_product_gp - AMORT[year]) / revenue[year]["value"], 6))

    update_yoy(revenue, YEARS, "FY25A")
    update_yoy(ebitda, YEARS, "FY25A")
    if "organic" in block:
        for year in YEARS:
            set_value(block["organic"]["revenue"][year], revenue[year]["value"])
            set_value(block["organic"]["ebitda"][year], ebitda[year]["value"])

    for period in PERIODS:
        total = revenue[period]["value"]
        summed = sum(line["periods"][period]["value"] for line in block["lines"])
        if abs(summed - total) > 0.02:
            raise SystemExit("%s %s lines %.4f != total %.4f" % (name, period, summed, total))
    nine = revenue["9MA"]["value"]
    if abs(nine + revenue["Q4E"]["value"] - revenue["FY26E"]["value"]) > 0.02:
        raise SystemExit("%s 9M+Q4 != FY26" % name)
    return {
        "revenue": {year: revenue[year]["value"] for year in ["FY25A", *YEARS]},
        "ebitda": {year: ebitda[year]["value"] for year in ["FY25A", *YEARS]},
        "q4_rev": revenue["Q4E"]["value"],
        "q4_ebitda": ebitda["Q4E"]["value"],
        "gm": {period: gross[period]["value"] for period in ("Q4E", *YEARS)},
        "gm32": gross["FY32E"]["value"],
    }


def set_finagle(finagle: dict, revenue: dict, ebitda: dict, gm32: float, gsnext: float, fy33: float, label: str) -> None:
    sales = growth_rates([revenue[year] for year in ["FY25A", *YEARS]])
    ebitda_g = growth_rates([ebitda[year] for year in ["FY25A", *YEARS]])
    compounds(revenue["FY25A"], sales, [revenue[year] for year in YEARS], label + " sales")
    compounds(ebitda["FY25A"], ebitda_g, [ebitda[year] for year in YEARS], label + " ebitda")
    me = round(ebitda["FY32E"] / revenue["FY32E"], 6)
    mc = round((me + gm32) / 2.0, 6)
    gs = round(gsnext, 6)
    set_value(
        finagle["sales_growth"], sales,
        "Revenue growth FY2026E–FY2032E off FY2025A (%s): %s." % (label, sales),
    )
    set_value(
        finagle["ebitda_growth"], ebitda_g,
        "Adjusted EBITDA growth FY2026E–FY2032E off FY2025A (%s): %s." % (label, ebitda_g),
    )
    set_value(finagle["me"], me, "FY2032E Adjusted EBITDA / revenue (%s) = %.6f." % (label, me))
    set_value(
        finagle["mc"], mc,
        "%s mc = (me %.6f + FY2032E GAAP gross margin %.6f) / 2 = %.6f. "
        "Halfway between the last explicit EBITDA margin and GAAP gross margin."
        % (label, me, gm32, mc),
    )
    set_value(
        finagle["gsnext"], gs,
        "%s gsnext is FY2033E revenue %.3f / FY2032E revenue %.3f − 1 = %.6f. "
        "FY2033E is one more year of the same build."
        % (label, fy33, revenue["FY32E"], gs),
    )


def replace_source(sources: list, sid: str, text: str) -> None:
    for entry in sources:
        if entry.get("id") == sid:
            entry["text"] = text
            return


def sync_citation_text(payload: dict, sid: str, text: str) -> None:
    replace_source(payload["sources"], sid, text)

    def walk(obj):
        if isinstance(obj, dict) and "value" in obj and isinstance(obj.get("citation"), dict):
            if obj["citation"].get("id") == sid:
                obj["citation"]["text"] = text
            return
        if isinstance(obj, dict):
            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for value in obj:
                walk(value)

    walk(payload)


def first_crossing(pairs: list[tuple[str, float]], threshold: float) -> tuple[str, float] | None:
    for year, amount in pairs:
        if amount + 1e-9 >= threshold:
            return year, amount
    return None


def combined(name: str, yochil: dict) -> dict:
    out = {}
    for year in FORWARD[1:]:
        out[year] = r3(GMELT[name][year] + yochil[year])
    return out


def main() -> None:
    payload = json.loads(FORECAST.read_text(encoding="utf-8"))
    if payload.get("as_of") == "2026-11-15":
        raise SystemExit("Vevye and Iheezo workbook is already applied. Do not run this twice.")

    base_annual = build_vevye(2033, 12)
    bear_annual = build_vevye(2033, 12, freeze_after=(2028, 12))
    base_v = vevye_dollars(base_annual)
    bull_v = vevye_dollars(base_annual, scale_from=base_v)
    bear_v = vevye_dollars(bear_annual)

    model = iheezo_units()
    base_units = model["units"]

    def bear_units(year: int) -> float:
        return base_units[2026] + 0.5 * (base_units[year] - base_units[2026])

    base_i = iheezo_dollars(model, model["half_mult"], lambda year: base_units[year])
    bull_i = iheezo_dollars(model, model["q4_ratio"], lambda year: base_units[year])
    bear_i = iheezo_dollars(model, 1.0, bear_units)
    base_y = yochil_dollars(base_units, YOCHIL_PEN)
    bull_y = yochil_dollars(base_units, YOCHIL_BULL_PEN)
    bear_y = {period: 0.0 for period in [*PERIODS, "FY33E"]}
    bear_y["units"] = {period: 0.0 for period in [*PERIODS, "FY33E"]}

    paths = {
        "base": {"VEVYE": base_v, "IHEEZO": base_i, "YOCHIL (MELT-210)": base_y},
        "bull": {"VEVYE": bull_v, "IHEEZO": bull_i, "YOCHIL (MELT-210)": bull_y},
        "bear": {"VEVYE": bear_v, "IHEEZO": bear_i, "YOCHIL (MELT-210)": bear_y},
    }
    blocks = {
        "base": payload,
        "bull": payload["scenarios"]["bull"],
        "bear": payload["scenarios"]["bear"],
    }
    applied = {}
    fy33 = {}
    for name, block in blocks.items():
        stats = apply_paths(block, paths[name], name)
        pieces = dict(FY33_OTHER[name])
        pieces["VEVYE"] = paths[name]["VEVYE"]["FY33E"]
        pieces["IHEEZO"] = paths[name]["IHEEZO"]["FY33E"]
        pieces["YOCHIL (MELT-210)"] = paths[name]["YOCHIL (MELT-210)"]["FY33E"]
        total33 = r3(sum(pieces.values()))
        fy33[name] = {"total": total33, "pieces": pieces}
        gsnext = total33 / stats["revenue"]["FY32E"] - 1.0
        stats["fy33"] = total33
        stats["gsnext"] = gsnext
        set_finagle(block["finagle"], stats["revenue"], stats["ebitda"], stats["gm32"], gsnext, total33, name)
        applied[name] = stats

    views = payload["views"]
    for year in YEARS:
        views["revenue"][year]["bottom_up"]["value"] = payload["totals"]["revenue"][year]["value"]
        views["ebitda"][year]["bottom_up"]["value"] = payload["totals"]["ebitda"][year]["value"]
    fy26_rev = payload["totals"]["revenue"]["FY26E"]["value"]
    fy26_ebitda = payload["totals"]["ebitda"]["FY26E"]["value"]
    views["ratios"]["FY26E"]["revenue"]["top_down_over_base"]["value"] = round(357.5 / fy26_rev, 6)
    views["ratios"]["FY26E"]["ebitda"]["top_down_over_base"]["value"] = round(40.0 / fy26_ebitda, 6)

    dec_share = base_annual[2026]["end_share"]
    dec28_share = base_annual[2028]["end_share"]
    approach = dec_share + 0.0057 / 0.1

    s1 = (
        "Q4 2026E VEVYE is the October–December 2026 path of Vevye and Iheezo model.xlsx (P10). "
        "September 2026 is 118 thousand TRx. October, November and December grow 5%% a month. "
        "Price starts at $117 per TRx and each month closes 3%% of the gap to $200. "
        "Those three months do not yet use the share formula, so this quarter matches the 14 November workbook. "
        "Revenue is price times TRx. TRx is in thousands on the sheet, so dollars are divided by 1,000. "
        "October and November use that identity; the sheet's revenue row starts in December. "
        "Q4 2026E is $%.3f million on %.0f TRx. Nine-month printed revenue of $90.033 million is unchanged, "
        "so FY2026E VEVYE is $%.3f million."
        % (base_v["Q4E"], base_v["q4_trx"], base_v["FY26E"])
    )
    s21 = (
        "FY2027E–FY2032E VEVYE follows Vevye and Iheezo model.xlsx (P10), extended with the same recurrences through December 2033 for the next-period year only. "
        "From January 2027, monthly TRx is market share times market size. "
        "October–December 2026 market size is 1,200 thousand TRx a month, so December 2026 share is %.2f%% (December TRx divided by 1,200). "
        "January 2027 market size stays 1,200 thousand; from February the market grows 1%% a month. "
        "Monthly share gains start at 0.57 points in January 2027 and are multiplied by 0.9 each month, so share approaches %.2f%%. "
        "Price continues to close 3%% of the gap to $200 each month. The sheet ends in December 2032. "
        "Dollars, US$ millions: %.3f / %.3f / %.3f / %.3f / %.3f / %.3f in FY2027E–FY2032E. "
        "Bull is 8%% above those published dollars from January 2027, the 14 November scenario rule (P8) applied to this sheet. "
        "Bear matches the sheet through December 2028 (share %.2f%%) and then holds that share while the market and the price path continue. "
        "Product gross margin stays 80%% in the base. TRx is a model unit."
        % (
            100.0 * dec_share, 100.0 * approach,
            base_v["FY27E"], base_v["FY28E"], base_v["FY29E"], base_v["FY30E"], base_v["FY31E"], base_v["FY32E"],
            100.0 * dec28_share,
        )
    )
    s2 = (
        "Q4 2026E IHEEZO customer units are %.0f, the IHEEZO sheet's normalized Q4, which equals 62,814 × (62,210 / 51,545). "
        "Dollars use the sheet's assumption that Q4 2026 recognizes half of the 2025 Q4 distributor/clinic seasonal effect. "
        "The 2025 Q4 revenue per customer unit was $571.26 against a reconstructed 2025 ASP of $%.2f (FY2025A IHEEZO revenue divided by 202,045 units), a ratio of %.3f. "
        "Half of that effect is a multiplier of %.3f. The price is the sheet's 2027 ASP, 10%% above the 2025 ASP, or $%.2f per customer unit. "
        "Q4 revenue is %.0f × %.3f × $%.2f = $%.3f million. "
        "The bull uses the full 2025 ratio (%.3f) and the bear uses no seasonal multiplier (S45). "
        "Realization is revenue per customer unit, not a separate list price."
        % (
            base_i["units"]["Q4E"], model["asp_2025"], model["q4_ratio"], model["half_mult"], model["asp"],
            base_i["units"]["Q4E"], model["half_mult"], model["asp"], base_i["Q4E"], model["q4_ratio"],
        )
    )
    s22 = (
        "IHEEZO FY2027E–FY2032E follows the IHEEZO sheet in Vevye and Iheezo model.xlsx (P10). "
        "The 2025 base is ex-ASC, 75%% of reported customer units. "
        "The 2026 normalized year allocates the Q3 2026 increment of 62,210 minus Q3 2025 ex-ASC across the 2025 seasonal weights, "
        "which keeps the cleaned four-quarter rate at %.0f units and does not carry Q2 2026 stocking forward. "
        "That normalized year is %.1f%% above the ex-ASC 2025 base. Each later year grows at half the prior year's growth rate, measured quarter by quarter on that sheet. "
        "Revenue is those customer units times the 2027 ASP of $%.2f, which is 10%% above the reconstructed 2025 ASP, with no further price step and no net full-year inventory build. "
        "Units %.0f / %.0f / %.0f / %.0f / %.0f / %.0f and dollars %.3f / %.3f / %.3f / %.3f / %.3f / %.3f in FY2027E–FY2032E. "
        "The bear takes half of each unit increment versus the normalized 2026 base, at the same ASP (S45). "
        "Bull units and dollars from FY2027E match the base; only Q4 2026 recognition differs."
        % (
            model["norm_2026"], 100.0 * model["growth_2026"], model["asp"],
            base_i["units"]["FY27E"], base_i["units"]["FY28E"], base_i["units"]["FY29E"],
            base_i["units"]["FY30E"], base_i["units"]["FY31E"], base_i["units"]["FY32E"],
            base_i["FY27E"], base_i["FY28E"], base_i["FY29E"], base_i["FY30E"], base_i["FY31E"], base_i["FY32E"],
        )
    )
    s32 = (
        "Base YOCHIL (MELT-210) revenue is an unweighted, conditional path on the company’s expected 2028 timing. "
        "End-of-Phase 2 was completed in the quarter ended 30 June 2026; Phase 3 is still ahead, so a 2028 launch is tighter than G-MELT’s. "
        "Units = penetration × (1/3) × that year’s IHEEZO customer units from the 15 November workbook (P10), "
        "with the same penetration fractions as the G-MELT ramp (60/750, 1/3, 2/3, 1, 1). "
        "IHEEZO units are %.0f / %.0f / %.0f / %.0f / %.0f in FY2028E–FY2032E. "
        "Assumed net price follows the G-MELT $175–$195 path. "
        "Revenue is $%.3f / $%.3f / $%.3f / $%.3f / $%.3f. "
        "The bull uses penetration 0.20 / 0.50 / 1 / 1 / 1 on the same units (S45). The bear has no YOCHIL revenue in the window. "
        "YOCHIL is not placed on the cataract 15%% target. Compounded MKO remains in ImprimisRx."
        % (
            base_i["units"]["FY28E"], base_i["units"]["FY29E"], base_i["units"]["FY30E"],
            base_i["units"]["FY31E"], base_i["units"]["FY32E"],
            base_y["FY28E"], base_y["FY29E"], base_y["FY30E"], base_y["FY31E"], base_y["FY32E"],
        )
    )
    c16 = (
        "YOCHIL revenue = penetration × (IHEEZO customer units / 3) × assumed net price / 1,000,000. "
        "IHEEZO units %.0f / %.0f / %.0f / %.0f / %.0f in FY2028E–FY2032E (P10). "
        "Penetration 60/750, 1/3, 2/3, 1, 1. Prices $175 / $180 / $185 / $190 / $195. "
        "Result: $%.3f / $%.3f / $%.3f / $%.3f / $%.3f."
        % (
            base_i["units"]["FY28E"], base_i["units"]["FY29E"], base_i["units"]["FY30E"],
            base_i["units"]["FY31E"], base_i["units"]["FY32E"],
            base_y["FY28E"], base_y["FY29E"], base_y["FY30E"], base_y["FY31E"], base_y["FY32E"],
        )
    )
    s45 = (
        "Scenario rules on the 15 November 2026 IHEEZO sheet, continuing the existing levers rather than a new story. "
        "Base Q4 uses half of the 2025 Q4 distributor/clinic ratio, which is the assumption written on the sheet. "
        "Bull Q4 uses the full 2025 ratio. Bear Q4 uses customer units times the 2027 ASP and no seasonal multiplier. "
        "From FY2027E the bull matches the base unit path. "
        "The bear adds half of each base-unit increment versus the normalized 2026 base of %.0f, at the same 2027 ASP. "
        "The 10%% ASP step is in all three cases because it is the sheet's price, not a scenario lever. "
        "Product gross margins stay 1.5 points above the base in the bull and 3 points below in the bear. "
        "Bull YOCHIL penetration is 0.20 / 0.50 / 1 / 1 / 1 of the same IHEEZO one-third. Bear YOCHIL revenue is zero."
        % model["norm_2026"]
    )
    p10 = (
        "Prompt [P], David, 15 November 2026: update the HROW forecast and run Finagle collaboratively "
        "using C:\\Users\\david\\Documents\\Investing\\wd\\HROW\\Vevye and Iheezo model.xlsx for the Vevye and Iheezo model. "
        "The Vevye sheet replaces the 14 November Vevye workbook. December 2026 market size is 1,200 thousand TRx. "
        "Monthly share gains start at 0.57 points in January 2027 and shrink by 0.9. "
        "The market grows 1% a month after January 2027. Price still starts at $117 and closes 3% of the gap to $200. "
        "The IHEEZO sheet replaces the constant 41,804 unit add. "
        "2025 units are taken at 75% (ex-ASC). The 2026 normalized year is built from Q3 2026 units of 62,210. "
        "Later-year unit growth is half the prior year's growth. "
        "The ASP increase cell is 10%, applied to 2027 and to Q4 2026. "
        "The sheet's Q4 assumption is half of the 2025 Q4 distributor/clinic seasonal effect. "
        "The 14 November bull and bear rules are not restated and are kept: VEVYE bull is 8% above the published dollars from January 2027, "
        "and VEVYE bear holds December 2028 share."
    )
    c1 = (
        "FY2026E revenue = nine-month 2026 printed actual (A2) + Q4 2026E. "
        "VEVYE %.3f; IHEEZO %.3f; TRIESENCE 33.538; Other branded 31.944; Other revenues 0.527; "
        "Compounding 60.890; G-MELT 0; YOCHIL 0; total %.3f."
        % (base_v["FY26E"], base_i["FY26E"], fy26_rev)
    )
    c15 = (
        "The FY2026E bottom-up total of %.3f is %.3f below the exact $350 low end of the reaffirmed $350–365 range. "
        "Implied Q4 to hit $350 is 135.839 versus base Q4 %.3f. The shortfall is not closed by a plug."
        % (fy26_rev, 350.0 - fy26_rev, applied["base"]["q4_rev"])
    )
    base_comb = combined("base", base_y)
    bull_comb = combined("bull", bull_y)
    base_hit = first_crossing(list(base_comb.items()), 100.0)
    bull_100 = first_crossing(list(bull_comb.items()), 100.0)
    bull_250 = first_crossing(list(bull_comb.items()), 250.0)
    if base_hit is None or base_hit[0] != "FY30E":
        raise SystemExit("base Melt $100 year moved: %s" % (base_hit,))
    if bull_100 is None or bull_100[0] != "FY29E":
        raise SystemExit("bull Melt $100 year moved: %s" % (bull_100,))
    if bull_250 is None or bull_250[0] != "FY32E":
        raise SystemExit("bull Melt $250 year moved: %s" % (bull_250,))
    s34 = (
        "Combined base G-MELT + YOCHIL sales first exceed $100 of Annual Net Sales in FY2030E ($%.3f). "
        "The item is dated 31 December 2030, the year-end of the year the threshold is hit. "
        "Payment is due within 75 days after that year-end."
        % base_hit[1]
    )
    s36 = (
        "Combined bull G-MELT + YOCHIL sales first exceed $100 of Annual Net Sales in FY2029E ($%.3f). "
        "The item is dated 31 December 2029. Payment is due within 75 days after that year-end."
        % bull_100[1]
    )
    s38 = (
        "Combined bull G-MELT + YOCHIL sales first exceed $250 of Annual Net Sales in FY2032E ($%.3f). "
        "The item is dated 31 December 2032. Payment is due within 75 days after that year-end."
        % bull_250[1]
    )
    for sid, text in (
        ("S1", s1), ("S21", s21), ("S2", s2), ("S22", s22), ("S32", s32),
        ("C16", c16), ("S34", s34), ("S36", s36), ("S38", s38), ("C15", c15),
    ):
        sync_citation_text(payload, sid, text)
        for entry in payload["sources"]:
            eid = entry.get("id") or ""
            if eid.startswith(sid + "_"):
                entry["text"] = text + " [Instance %s.]" % eid
    sync_citation_text(payload, "C1", (
        "FY2026E VEVYE = nine-month 2026 printed $90.033 million (A2) + Q4 workbook $%.3f million (S1, P10) = $%.3f million."
        % (base_v["Q4E"], base_v["FY26E"])
    ))
    # The company FY2026E identity lives on C1_23.
    sync_citation_text(payload, "C1_23", c1)

    payload["sources"].append({
        "id": "P10",
        "document": "prompt",
        "page": "n/a",
        "text": p10,
    })
    payload["sources"].append({
        "id": "S45",
        "document": "prompt",
        "page": "n/a",
        "text": s45,
    })
    # Point the changed forward-year citations at the refreshed paragraphs while keeping one id per value.
    for name, block in blocks.items():
        vevye = next(item for item in block["lines"] if item["name"] == "VEVYE")
        iheezo = next(item for item in block["lines"] if item["name"] == "IHEEZO")
        yochil = next(item for item in block["lines"] if item["name"] == "YOCHIL (MELT-210)")
        if isinstance(vevye["periods"]["Q4E"].get("citation"), dict):
            vevye["periods"]["Q4E"]["citation"]["text"] = s1
        for key in FORWARD:
            if isinstance(vevye["periods"][key].get("citation"), dict):
                vevye["periods"][key]["citation"]["text"] = s21
            if isinstance(iheezo["periods"][key].get("citation"), dict):
                iheezo["periods"][key]["citation"]["text"] = s22
        if isinstance(iheezo["periods"]["Q4E"].get("citation"), dict):
            iheezo["periods"]["Q4E"]["citation"]["text"] = s2
        for key in FORWARD[1:]:
            if isinstance(yochil["periods"][key].get("citation"), dict):
                yochil["periods"][key]["citation"]["text"] = s32

    payload["as_of"] = "2026-11-15"
    payload["horizon_note"] = (
        "Seven explicit years FY2026E–FY2032E are a prompt override (P1) and are kept. "
        "On 15 November 2026 VEVYE and IHEEZO were replaced with Vevye and Iheezo model.xlsx (P10). "
        "VEVYE bull stays 8% above the workbook from January 2027 and VEVYE bear holds December 2028 share (P8). "
        "YOCHIL uses the new IHEEZO customer units. No year-0 equity raise (P9). "
        "No Harrow filing after the 9 November 2026 8-K and 10-Q was found. "
        "A collaborative Finagle valuation is run on this case."
    )
    payload["scenarios"]["bear"]["description"] = (
        "FY2026E misses the $350 low end. IHEEZO Q4 drops the distributor seasonal effect and later years take half the workbook unit increments (S45). "
        "VEVYE matches the 15 November workbook through December 2028 and then holds that month's share (P8, P10). "
        "Novaliq consent haircuts TYRVAYA. Biosimilars are slower. G-MELT is delayed past 2030 and YOCHIL has no revenue in the window. "
        "TRIESENCE fades after the 2029 patents. Product gross margins are 3 points below the base. "
        "Bear FY2026E Adjusted EBITDA may miss the more-than-$40 floor. "
        "Operating leverage: core cash opex inflates at 5% and same-store variable opex is 8% (S42)."
    )
    payload["scenarios"]["bull"]["description"] = (
        "Q4/FY2026E is not plugged to the $365 high end. VEVYE matches the 15 November workbook through December 2026 and is 8% above it from January 2027 (P8, P10). "
        "IHEEZO Q4 uses the full 2025 distributor/clinic ratio; from FY2027E the bull matches the workbook unit path (S45). "
        "TYRVAYA clears the Novaliq issue. BYOOVIZ/OPUVIZ ramp faster. "
        "G-MELT ramps faster than the 15% base. YOCHIL penetration of the same IHEEZO one-third is 0.20 / 0.50 / 1 from FY2028E. "
        "Product margins are about 1.5 points above the base. "
        "Cost build as the base: 4% core inflation and 4% variable opex on same-store growth above the Q3 2026 annualized base."
    )

    # Refresh finagle citation texts into the source list, including the new numbers.
    for name, block in blocks.items():
        for leaf in ("sales_growth", "ebitda_growth", "me", "mc", "gsnext"):
            cite = block["finagle"][leaf]["citation"]
            replace_source(payload["sources"], cite["id"], cite["text"])

    FORECAST.write_text(json.dumps(payload, indent=1, ensure_ascii=True) + "\n", encoding="utf-8")
    if WORKBOOK_SRC.exists():
        shutil.copyfile(WORKBOOK_SRC, HERE / "Vevye and Iheezo model.xlsx")

    detail = {
        "as_of": "2026-11-15",
        "vevye": {
            "dec_2026_share": dec_share,
            "dec_2028_share": dec28_share,
            "approach_share": approach,
            "base": {key: base_v[key] for key in ["Q4E", *YEARS, "FY33E"]},
            "bull": {key: bull_v[key] for key in ["Q4E", *YEARS, "FY33E"]},
            "bear": {key: bear_v[key] for key in ["Q4E", *YEARS, "FY33E"]},
            "trx": base_v["trx"],
            "avg_price": base_v["avg_price"],
        },
        "iheezo": {
            "asp_2025": model["asp_2025"],
            "asp_2027": model["asp"],
            "q4_ratio": model["q4_ratio"],
            "half_mult": model["half_mult"],
            "norm_2026": model["norm_2026"],
            "growth_vs_ex_asc": model["growth_2026"],
            "base": {key: base_i[key] for key in ["Q4E", *YEARS, "FY33E"]},
            "bull": {key: bull_i[key] for key in ["Q4E", *YEARS, "FY33E"]},
            "bear": {key: bear_i[key] for key in ["Q4E", *YEARS, "FY33E"]},
            "base_units": base_i["units"],
            "bear_units": bear_i["units"],
        },
        "yochil": {
            "base": {key: base_y[key] for key in ["Q4E", *YEARS, "FY33E"]},
            "bull": {key: bull_y[key] for key in ["Q4E", *YEARS, "FY33E"]},
            "base_units": base_y["units"],
            "bull_units": bull_y["units"],
        },
        "combined_melt": {"base": base_comb, "bull": bull_comb},
        "company": applied,
        "fy33": fy33,
    }
    (HERE / "vevye_iheezo_path.json").write_text(json.dumps(detail, indent=1), encoding="utf-8")
    write_drivers(detail)
    write_snapshot(detail)
    print(json.dumps({
        "company": {name: {k: applied[name][k] for k in ("revenue", "ebitda", "q4_rev", "q4_ebitda", "fy33", "gsnext")} for name in applied},
        "vevye_base": {k: base_v[k] for k in ["Q4E", *YEARS]},
        "iheezo_base": {k: base_i[k] for k in ["Q4E", *YEARS]},
        "yochil_base": {k: base_y[k] for k in FORWARD[1:]},
        "dec_share": round(dec_share, 4),
        "dec28_share": round(dec28_share, 4),
        "asp": round(model["asp"], 2),
    }, indent=1))


def write_drivers(detail) -> None:
    with DRIVERS.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    base_v = detail["vevye"]["base"]
    trx = detail["vevye"]["trx"]
    price = detail["vevye"]["avg_price"]
    base_i = detail["iheezo"]["base"]
    units = detail["iheezo"]["base_units"]
    asp = detail["iheezo"]["asp_2027"]
    base_y = detail["yochil"]["base"]
    yunits = detail["yochil"]["base_units"]
    company = detail["company"]["base"]
    vol = []
    prev = trx["FY26E"]
    for year in FORWARD:
        vol.append(trx[year] / prev - 1.0)
        prev = trx[year]

    def cells(line, metric):
        for row in rows:
            if row and row[0] == line and row[1] == metric:
                return row
        raise SystemExit("missing drivers row %s %s" % (line, metric))

    old_v = [float(item) for item in cells("VEVYE", "revenue_usd_m")[3:9]]
    old_i = [float(item) for item in cells("IHEEZO", "revenue_usd_m")[3:9]]
    new_v = [base_v[year] for year in FORWARD]
    new_i = [base_i[year] for year in FORWARD]
    ss_row = cells("Cash opex bridge", "same_store_revenue_usd_m")
    var_row = cells("Cash opex bridge", "same_store_variable_4pct_usd_m")
    ox_row = cells("Cash opex bridge", "total_cash_opex_usd_m")
    gp_row = cells("Gross margin build", "product_GP_before_amort_usd_m")
    new_ss, new_var, new_ox, new_gp = [], [], [], []
    for index, year in enumerate(FORWARD):
        ss = float(ss_row[3 + index]) + (new_v[index] - old_v[index]) + (new_i[index] - old_i[index])
        var = round(0.04 * (ss - SAME_STORE_BASE), 3)
        ox = round(float(ox_row[3 + index]) + var - float(var_row[3 + index]), 3)
        gp = round(float(gp_row[3 + index]) + 0.80 * (new_v[index] - old_v[index]) + 0.82 * (new_i[index] - old_i[index]) + 0.72 * (base_y[year] - float(cells("YOCHIL (MELT-210)", "revenue_usd_m")[3 + index])), 3)
        new_ss.append(ss)
        new_var.append(var)
        new_ox.append(ox)
        new_gp.append(gp)
    bear_var_row = cells("Bear cost lever", "bear_variable_8pct_usd_m")
    bear_v = detail["vevye"]["bear"]
    bear_i = detail["iheezo"]["bear"]
    # Bear same-store moves with bear VEVYE and IHEEZO versus the rows still on the sheet.
    old_bear_v = [285.252, 415.967, 520.667, 619.527, 723.762, 835.619]
    old_bear_i = [107.658, 116.158, 124.657, 133.157, 141.656, 150.156]
    new_bear_var = []
    for index, year in enumerate(FORWARD):
        # Reconstruct bear same-store from the stored variable, then move it.
        old_ss_bear = SAME_STORE_BASE + float(bear_var_row[3 + index]) / 0.08
        ss_bear = old_ss_bear + (bear_v[year] - old_bear_v[index]) + (bear_i[year] - old_bear_i[index])
        new_bear_var.append(round(0.08 * (ss_bear - SAME_STORE_BASE), 3))

    def put(line, metric, values, note):
        for row in rows:
            if row and row[0] == line and row[1] == metric:
                row[2:9] = values
                if len(row) < 10:
                    row.append(note)
                else:
                    row[9] = note
                return
        raise SystemExit("missing drivers row %s %s" % (line, metric))

    put(
        "VEVYE", "revenue_usd_m",
        ["%s" % base_v[year] for year in YEARS],
        "Workbook (P10). Q4 2026E TRx %.0f at an average $%.2f per TRx. "
        "FY26 blends printed nine-month revenue with that quarter. "
        "From January 2027, TRx is share times a market of 1,200 thousand TRx in December 2026, growing 1%% a month from February 2027. "
        "December 2026 share is %.2f%%. Monthly gains start at 0.57 points and shrink by 0.9, so share approaches %.2f%%. "
        "Price closes 3%% of the gap to $200 each month. FY27–FY32 TRx %.0f / %.0f / %.0f / %.0f / %.0f / %.0f."
        % (
            trx["FY26E"] - NINE_MONTH_TRX,
            price["Q4E"],
            100.0 * detail["vevye"]["dec_2026_share"],
            100.0 * detail["vevye"]["approach_share"],
            trx["FY27E"], trx["FY28E"], trx["FY29E"], trx["FY30E"], trx["FY31E"], trx["FY32E"],
        ),
    )
    put(
        "VEVYE", "volume_growth_vs_prior",
        ["n/a"] + ["%.4f" % item for item in vol],
        "Output of the workbook share and market path, not an input rate. FY26 TRx is nine-month reconstructed 864,142 plus Q4.",
    )
    put(
        "VEVYE", "npp_usd_per_trx",
        ["%.2f" % price[year] for year in YEARS],
        "Average net dollars per model TRx. FY26 blends the printed nine months with the Q4 workbook. "
        "Later years are the workbook price path. Bull is 8% above workbook revenue from January 2027. "
        "Bear uses the same price path and freezes share after December 2028.",
    )
    put(
        "IHEEZO", "revenue_usd_m",
        ["%s" % base_i[year] for year in YEARS],
        "Q4 2026E customer units %.0f. Q4 dollars use half the 2025 Q4 distributor/clinic ratio (%.3f) times the 2027 ASP of $%.2f. "
        "FY27–FY32 revenue is annual customer units times that ASP, with no net full-year inventory. "
        "Unit growth halves each year off a normalized 2026 rate of %.0f. The 10%% ASP step is the workbook input."
        % (units["Q4E"], detail["iheezo"]["half_mult"], asp, detail["iheezo"]["norm_2026"]),
    )
    put(
        "IHEEZO", "units",
        ["%.0f" % units[year] for year in YEARS],
        "FY26 reported units keep Q1–Q3 actuals plus Q4 demand of %.0f. "
        "FY27–FY32 are the workbook customer-unit path: %.0f / %.0f / %.0f / %.0f / %.0f / %.0f. "
        "Realization is revenue per customer unit."
        % (units["Q4E"], units["FY27E"], units["FY28E"], units["FY29E"], units["FY30E"], units["FY31E"], units["FY32E"]),
    )
    realizations = [base_i["FY26E"] * 1_000_000.0 / units["FY26E"]] + [asp] * 6
    put(
        "IHEEZO", "realization_usd_per_unit",
        ["%.2f" % item for item in realizations],
        "FY26 blends three printed quarters with Q4 at half the 2025 seasonal effect and the 2027 ASP. FY27–FY32 use the 2027 ASP of $%.2f."
        % asp,
    )
    put(
        "YOCHIL (MELT-210)", "units",
        ["%.0f" % yunits[year] for year in YEARS],
        "Units = penetration × (1/3) × workbook IHEEZO customer units. Penetration 60/750, 1/3, 2/3, 1, 1. "
        "FY28–FY32 units %.0f / %.0f / %.0f / %.0f / %.0f."
        % (yunits["FY28E"], yunits["FY29E"], yunits["FY30E"], yunits["FY31E"], yunits["FY32E"]),
    )
    put(
        "YOCHIL (MELT-210)", "revenue_usd_m",
        ["%s" % base_y[year] for year in YEARS],
        "units × net / 1,000,000 on the workbook IHEEZO units. Product GM 72%.",
    )
    put(
        "Total revenue", "revenue_usd_m",
        ["%s" % company["revenue"][year] for year in YEARS],
        "Sum of official lines plus the G-MELT and YOCHIL memo lines. FY2026E is nine-month actual plus Q4.",
    )
    put(
        "Adjusted EBITDA", "ebitda_usd_m",
        ["%s" % company["ebitda"][year] for year in YEARS],
        "Product GP − cash opex from FY27. FY26 is the 9M+Q4 cost build and is not forced to the more-than-$40m floor.",
    )
    margins = [100.0 * company["ebitda"][year] / company["revenue"][year] for year in YEARS]
    put(
        "Adjusted EBITDA", "ebitda_margin_pct",
        ["%.1f" % item for item in margins],
        "FY32 margin is the fully costed central result. It sits beyond the FY24A 20.2% / FY25A 22.7% history and is flagged, not capped.",
    )
    put(
        "Gross margin build", "GAAP_gross_margin_pct",
        ["%.1f" % (100.0 * company["gm"][year]) for year in YEARS],
        "(product GP − amort) / revenue from FY27. FY26 is the 9M+Q4 blend.",
    )
    put(
        "Gross margin build", "product_GP_before_amort_usd_m",
        ["n/a (9M+Q4 path)"] + ["%s" % item for item in new_gp],
        "FY26 GP is built from the 9M+Q4 path. VEVYE 80%, IHEEZO 82%, YOCHIL 72%.",
    )
    put(
        "Cash opex bridge", "same_store_revenue_usd_m",
        ["n/a"] + ["%s" % round(item, 3) for item in new_ss],
        "Same-store revenue; Q3 2026 annualized base 397.188. VEVYE and IHEEZO move with the 15 November workbook. YOCHIL is outside this base.",
    )
    put(
        "Cash opex bridge", "same_store_variable_4pct_usd_m",
        ["n/a"] + ["%s" % item for item in new_var],
        "4% of same-store revenue above 397.188. Does not take 4% of TYRVAYA, BYOOVIZ, OPUVIZ, BYQLOVI, G-MELT or YOCHIL.",
    )
    put(
        "Cash opex bridge", "total_cash_opex_usd_m",
        ["%s" % ox_row[2]] + ["%s" % item for item in new_ox],
        "FY26 cash opex is the 9M+Q4 build. Later years move only with the 4% variable piece on VEVYE and IHEEZO.",
    )
    bear = detail["company"]["bear"]
    put(
        "Bear cost lever", "bear_variable_8pct_usd_m",
        ["n/a"] + ["%s" % item for item in new_bear_var],
        "Bear variable 8% of same-store revenue above the Q3 annualized base. VEVYE and IHEEZO are inside same-store.",
    )
    put(
        "Bear cost lever", "bear_ebitda_usd_m",
        ["%s" % bear["ebitda"][year] for year in YEARS],
        "Bear Adjusted EBITDA with the operating-leverage lever, the workbook VEVYE path (share frozen after December 2028), and half the IHEEZO unit increments.",
    )
    with DRIVERS.open("w", encoding="utf-8", newline="") as handle:
        csv.writer(handle, lineterminator="\n").writerows(rows)


def write_snapshot(detail) -> None:
    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    company = detail["company"]["base"]
    for period in PERIODS:
        snap["LINES"]["VEVYE"][period] = detail["vevye"]["base"][period]
        snap["LINES"]["IHEEZO"][period] = detail["iheezo"]["base"][period]
        snap["LINES"]["YOCHIL (MELT-210)"][period] = detail["yochil"]["base"][period]
        key = "Q4E" if period == "Q4E" else period
        snap["REV"][period] = company["q4_rev"] if period == "Q4E" else company["revenue"][key]
        snap["EBITDA"][period] = company["q4_ebitda"] if period == "Q4E" else company["ebitda"][key]
        snap["GM"][period] = company["gm"][period] if period in company["gm"] else snap["GM"][period]
    for label, prefix in (("bull", "BULL"), ("bear", "BEAR")):
        block = detail["company"][label]
        for period in ("Q4E", *YEARS):
            snap[prefix + "_V"][period] = detail["vevye"][label][period]
            snap[prefix + "_I"][period] = detail["iheezo"][label][period]
            if period == "Q4E":
                snap[prefix + "_REV"][period] = block["q4_rev"]
                snap[prefix + "_EBITDA"][period] = block["q4_ebitda"]
                snap[prefix + "_GM"][period] = block["gm"].get(period, snap[prefix + "_GM"][period])
            else:
                snap[prefix + "_REV"][period] = block["revenue"][period]
                snap[prefix + "_EBITDA"][period] = block["ebitda"][period]
                snap[prefix + "_GM"][period] = block["gm"][period]
    snap["YOCHIL_U"] = {year: detail["yochil"]["base_units"][year] for year in FORWARD[1:]}
    snap["BASE_COMB"] = {"FY26E": 0.0, "FY27E": 0.0, **detail["combined_melt"]["base"]}
    snap["P_IH"] = detail["iheezo"]["asp_2027"]
    snap["MODEL_NOTE"] = "15 November 2026 Vevye and Iheezo workbook. See vevye_iheezo_path.json."
    SNAPSHOT.write_text(json.dumps(snap, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
