"""Replace HROW VEVYE with the monthly workbook and drop equity raises.

The workbook is forecasts/HROW/Vevye model.xlsx. TRx on that sheet is in
thousands. Revenue is price times TRx (thousands of dollars); this script
divides by 1,000 to store US$ millions. October and November use price times
TRx; the sheet's revenue row starts in December. Months after October 2032
continue the same recurrences. FY2033 is only the next-period growth year.
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FORECAST = HERE / "forecast.json"
SNAPSHOT = HERE / "numbers_snapshot.json"
DRIVERS = HERE / "drivers.csv"

NINE_MONTH_TRX = 864_142.0  # reconstructed Q1–Q3 2026, unchanged
NINE_MONTH_REV = 90.033
NINE_MONTH_GP = 152.311
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
# Old FY2033 company revenue and the VEVYE piece inside it (S44).
OLD_FY33 = {"base": (1838.379, 879.926), "bull": (2064.574, 950.321), "bear": (641.437, 264.655)}


def r3(value: float) -> float:
    return round(value + 0.0, 3)


def months_between(y1, m1, y2, m2) -> int:
    return (y2 - y1) * 12 + (m2 - m1) + 1


def ym(index: int) -> tuple[int, int]:
    month = 10 + index
    year = 2026 + (month - 1) // 12
    return year, (month - 1) % 12 + 1


def build_path(end_year: int, end_month: int, freeze_after: tuple[int, int] | None = None):
    """Monthly path. freeze_after holds share fixed after that calendar month."""
    n = months_between(2026, 10, end_year, end_month)
    trx = [0.0] * n
    price = [0.0] * n
    share = [None] * n
    gain = [None] * n
    msize = [None] * n
    trx[0] = 118 * 1.05
    trx[1] = trx[0] * 1.05
    trx[2] = trx[1] * 1.05
    price[0] = 117.0
    for i in range(1, n):
        price[i] = price[i - 1] + (200.0 - price[i - 1]) * 0.03
    share[2] = 0.155
    gain[3] = 0.0065
    for i in range(4, n):
        gain[i] = gain[i - 1] * 0.9
    share[3] = share[2] + gain[3]
    for i in range(4, n):
        share[i] = share[i - 1] + gain[i]
    if freeze_after is not None:
        freeze_at = months_between(2026, 10, freeze_after[0], freeze_after[1]) - 1
        held = share[freeze_at]
        for i in range(freeze_at + 1, n):
            share[i] = held
    msize[2] = trx[2] / share[2]
    for i in range(3, n):
        msize[i] = msize[i - 1] * 1.01
    for i in range(3, n):
        trx[i] = share[i] * msize[i]
    rev_k = [price[i] * trx[i] for i in range(n)]
    return {"trx_k": trx, "price": price, "share": share, "rev_k": rev_k}


def annualize(path: dict) -> dict:
    by_year = {}
    for i, rev_k in enumerate(path["rev_k"]):
        year, _month = ym(i)
        bucket = by_year.setdefault(year, {"rev_k": 0.0, "trx_k": 0.0, "n": 0, "end_share": None, "end_price": None})
        bucket["rev_k"] += rev_k
        bucket["trx_k"] += path["trx_k"][i]
        bucket["n"] += 1
        bucket["end_share"] = path["share"][i]
        bucket["end_price"] = path["price"][i]
    return by_year


def vevye_dollars(annual: dict, scale: float, from_year: int) -> dict:
    """US$ millions, rounded to 3 decimals. scale applies from from_year on."""
    q4 = r3(annual[2026]["rev_k"] / 1000.0)
    out = {"Q4E": q4, "FY26E": r3(NINE_MONTH_REV + q4)}
    for year, key in (
        (2027, "FY27E"),
        (2028, "FY28E"),
        (2029, "FY29E"),
        (2030, "FY30E"),
        (2031, "FY31E"),
        (2032, "FY32E"),
    ):
        raw = annual[year]["rev_k"] / 1000.0
        out[key] = r3(raw * scale) if year >= from_year else r3(raw)
    out["FY33E"] = r3((annual[2033]["rev_k"] / 1000.0) * (scale if 2033 >= from_year else 1.0))
    out["q4_trx"] = annual[2026]["trx_k"] * 1000.0
    out["trx"] = {}
    out["trx"]["FY26E"] = NINE_MONTH_TRX + out["q4_trx"]
    for year, key in (
        (2027, "FY27E"),
        (2028, "FY28E"),
        (2029, "FY29E"),
        (2030, "FY30E"),
        (2031, "FY31E"),
        (2032, "FY32E"),
        (2033, "FY33E"),
    ):
        out["trx"][key] = annual[year]["trx_k"] * 1000.0
    out["end_share"] = {year: annual[year]["end_share"] for year in range(2026, 2034)}
    out["end_price"] = {year: annual[year]["end_price"] for year in range(2026, 2034)}
    out["avg_price"] = {}
    for key, rev in out.items():
        if key in out["trx"] and out["trx"][key]:
            out["avg_price"][key] = rev * 1_000_000.0 / out["trx"][key]
    out["avg_price"]["Q4E"] = q4 * 1_000_000.0 / out["q4_trx"]
    return out


def set_value(node: dict, value) -> None:
    node["value"] = value


def update_yoy(periods: dict, years: list[str], baseline: str) -> None:
    prev = periods[baseline]["value"]
    for year in years:
        key = "YoY_" + year
        if key in periods and isinstance(periods[key], dict) and "value" in periods[key]:
            set_value(periods[key], round(periods[year]["value"] / prev - 1.0, 4))
        prev = periods[year]["value"]


def apply_block(block: dict, new_v: dict, gm_rate: float, var_rate: float) -> dict:
    line = next(item for item in block["lines"] if item["name"] == "VEVYE")
    old_v = {period: line["periods"][period]["value"] for period in PERIODS}
    for period in PERIODS:
        set_value(line["periods"][period], new_v[period])
    update_yoy(line["periods"], YEARS, "FY25A")

    revenue = block["totals"]["revenue"]
    ebitda = block["totals"]["ebitda"]
    gross = block["totals"]["gross_margin"]
    old_rev = {period: revenue[period]["value"] for period in PERIODS}
    old_ebitda = {period: ebitda[period]["value"] for period in list(ebitda) if period in PERIODS or period == "Q4E"}
    old_gm = {period: gross[period]["value"] for period in PERIODS if period in gross}

    delta = {period: new_v[period] - old_v[period] for period in PERIODS}
    for period in PERIODS:
        set_value(revenue[period], r3(old_rev[period] + delta[period]))

    set_value(ebitda["Q4E"], r3(old_ebitda["Q4E"] + gm_rate * delta["Q4E"]))
    set_value(ebitda["FY26E"], r3(old_ebitda["FY26E"] + gm_rate * delta["Q4E"]))
    for year in YEARS[1:]:
        set_value(ebitda[year], r3(old_ebitda[year] + (gm_rate - var_rate) * delta[year]))

    old_q4_gp = old_gm["Q4E"] * old_rev["Q4E"]
    new_q4_gp = old_q4_gp + gm_rate * delta["Q4E"]
    set_value(gross["Q4E"], round(new_q4_gp / revenue["Q4E"]["value"], 6))
    new_fy26_gp = NINE_MONTH_GP + new_q4_gp
    set_value(gross["FY26E"], round(new_fy26_gp / revenue["FY26E"]["value"], 6))
    for year in YEARS[1:]:
        old_gp = old_gm[year] * old_rev[year] + AMORT[year]
        new_gp = old_gp + gm_rate * delta[year]
        set_value(gross[year], round((new_gp - AMORT[year]) / revenue[year]["value"], 6))

    update_yoy(revenue, YEARS, "FY25A")
    update_yoy(ebitda, YEARS, "FY25A")

    if "organic" in block:
        for year in YEARS:
            set_value(block["organic"]["revenue"][year], revenue[year]["value"])
            set_value(block["organic"]["ebitda"][year], ebitda[year]["value"])
    return {
        "old_v": old_v,
        "delta": delta,
        "revenue": {year: revenue[year]["value"] for year in ["FY25A", *YEARS]},
        "ebitda": {year: ebitda[year]["value"] for year in ["FY25A", *YEARS]},
        "q4_rev": revenue["Q4E"]["value"],
        "q4_ebitda": ebitda["Q4E"]["value"],
        "gm32": gross["FY32E"]["value"],
    }


def growth_rates(values: list[float]) -> list[float]:
    return [round(values[i] / values[i - 1] - 1.0, 9) for i in range(1, len(values))]


def compounds(start: float, rates: list[float], targets: list[float]) -> None:
    level = start
    for rate, target in zip(rates, targets):
        level = level * (1.0 + rate)
        if abs(level - target) > 0.02:
            raise SystemExit("growth does not compound: %.6f vs %.6f" % (level, target))


def set_finagle(finagle: dict, revenue: dict, ebitda: dict, gm32: float, gsnext: float) -> None:
    sales = growth_rates([revenue[year] for year in ["FY25A", *YEARS]])
    ebitda_g = growth_rates([ebitda[year] for year in ["FY25A", *YEARS]])
    compounds(revenue["FY25A"], sales, [revenue[year] for year in YEARS])
    compounds(ebitda["FY25A"], ebitda_g, [ebitda[year] for year in YEARS])
    me = round(ebitda["FY32E"] / revenue["FY32E"], 6)
    if abs(me - ebitda["FY32E"] / revenue["FY32E"]) > 0.002:
        raise SystemExit("me rounding too coarse")
    mc = round((me + gm32) / 2.0, 6)
    set_value(finagle["sales_growth"], sales)
    set_value(finagle["ebitda_growth"], ebitda_g)
    set_value(finagle["me"], me)
    set_value(finagle["mc"], mc)
    set_value(finagle["gsnext"], round(gsnext, 6))


def drop_equity(schedule: dict) -> None:
    for name, items in schedule.items():
        schedule[name] = [item for item in items if item.get("kind") != "equity"]


def replace_source(sources: list, sid: str, text: str) -> None:
    for entry in sources:
        if entry.get("id") == sid:
            entry["text"] = text
            return
    raise SystemExit("missing source " + sid)


def main() -> None:
    base_annual = annualize(build_path(2033, 12))
    bear_annual = annualize(build_path(2033, 12, freeze_after=(2028, 12)))
    base_v = vevye_dollars(base_annual, 1.0, 2099)
    # Bull matches the workbook through December 2026 and is 8% above the published dollars after that.
    bull_v = dict(base_v)
    for key in ("FY27E", "FY28E", "FY29E", "FY30E", "FY31E", "FY32E", "FY33E"):
        bull_v[key] = r3(base_v[key] * 1.08)
    bear_v = vevye_dollars(bear_annual, 1.0, 2099)

    payload = json.loads(FORECAST.read_text(encoding="utf-8"))
    if payload.get("as_of") == "2026-11-14":
        raise SystemExit("VEVYE workbook is already applied (as_of 2026-11-14). Do not run this twice.")
    applied = {
        "base": apply_block(payload, base_v, 0.80, 0.04),
        "bear": apply_block(payload["scenarios"]["bear"], bear_v, 0.77, 0.08),
        "bull": apply_block(payload["scenarios"]["bull"], bull_v, 0.815, 0.04),
    }
    for name, block in (
        ("base", payload),
        ("bear", payload["scenarios"]["bear"]),
        ("bull", payload["scenarios"]["bull"]),
    ):
        stats = applied[name]
        vevye = base_v if name == "base" else bear_v if name == "bear" else bull_v
        old_fy33, old_piece = OLD_FY33[name]
        fy33 = r3(old_fy33 - old_piece + vevye["FY33E"])
        gsnext = fy33 / stats["revenue"]["FY32E"] - 1.0
        stats["fy33"] = fy33
        stats["gsnext"] = gsnext
        stats["me"] = round(stats["ebitda"]["FY32E"] / stats["revenue"]["FY32E"], 6)
        stats["mc"] = round((stats["me"] + stats["gm32"]) / 2.0, 6)
        set_finagle(block["finagle"], stats["revenue"], stats["ebitda"], stats["gm32"], gsnext)
        # Lines must sum.
        for period in PERIODS:
            total = block["totals"]["revenue"][period]["value"]
            summed = sum(line["periods"][period]["value"] for line in block["lines"])
            if abs(summed - total) > 0.02:
                raise SystemExit("%s %s lines %.4f != total %.4f" % (name, period, summed, total))
            nine = block["totals"]["revenue"]["9MA"]["value"]
            q4 = block["totals"]["revenue"]["Q4E"]["value"]
            fy26 = block["totals"]["revenue"]["FY26E"]["value"]
            if abs(nine + q4 - fy26) > 0.02:
                raise SystemExit("%s 9M+Q4 != FY26" % name)

    views = payload["views"]
    for year in YEARS:
        views["revenue"][year]["bottom_up"]["value"] = payload["totals"]["revenue"][year]["value"]
        views["ebitda"][year]["bottom_up"]["value"] = payload["totals"]["ebitda"][year]["value"]
    fy26_rev = payload["totals"]["revenue"]["FY26E"]["value"]
    fy26_ebitda = payload["totals"]["ebitda"]["FY26E"]["value"]
    views["ratios"]["FY26E"]["revenue"]["top_down_over_base"]["value"] = round(357.5 / fy26_rev, 6)
    views["ratios"]["FY26E"]["ebitda"]["top_down_over_base"]["value"] = round(40.0 / fy26_ebitda, 6)

    drop_equity(payload["cash_share_adjustments"])
    payload["as_of"] = "2026-11-14"
    payload["horizon_note"] = (
        "Seven explicit years FY2026E–FY2032E are a prompt override of the method's usual two-year explicit window (P1) and are kept on this update. "
        "On 14 November 2026 the VEVYE path was replaced with the monthly workbook (P8). "
        "Bull VEVYE is 8% above that workbook from January 2027. Bear VEVYE matches it through December 2028 and then holds December 2028 share. "
        "All year-0 equity raises were removed (P9), overriding P6. A collaborative Finagle valuation is run on this case."
    )
    payload["scenarios"]["bear"]["description"] = (
        "FY2026E misses the $350 low end on a weaker Q4 mix, no IHEEZO year-end recognition, and half the recent TRIESENCE net add; "
        "Novaliq consent requires a TYRVAYA haircut or modified terms; slower biosimilars and delayed OPUVIZ; "
        "G-MELT approval delayed past 2030 (no 2028 launch) and YOCHIL has no revenue in the window (Phase 3 still ahead); "
        "VEVYE matches the workbook through December 2028 and then holds December 2028 market share while the market keeps growing 1% a month and the price path continues (P8); "
        "TRIESENCE fades after 2029 patents; product gross margins 3 points below the base (higher Samsung take, tighter royalties). "
        "Bear FY2026E Adjusted EBITDA may miss the more-than-$40 floor; the base is not forced to that floor. "
        "Combined Melt Annual Net Sales do not reach $100 in the explicit window. "
        "Operating leverage is a named bear lever: core cash opex inflates at 5% instead of 4% and same-store variable opex is 8% instead of 4% of same-store growth above the Q3 2026 annualized base (S42)."
    )
    payload["scenarios"]["bull"]["description"] = (
        "Q4/FY2026E is not plugged to the $365 high end; VEVYE matches the workbook through December 2026 and is 8% above it from January 2027 (P8); "
        "IHEEZO Q4 uses the 2025 recognition uplift; TYRVAYA clears the Novaliq issue; BYOOVIZ/OPUVIZ ramp faster; "
        "G-MELT is approved on the standard-review clock, launches in 2028, and ramps faster than the 15% base (to about 25% of the 5 million cataract target by FY2032E); "
        "YOCHIL uses a faster penetration of the same IHEEZO one-third (0.20 / 0.50 / 1 from FY2028E). "
        "Combined Melt Annual Net Sales reach $100 in FY2029E and $250 in FY2032E, triggering commercial cash that is still not an EBITDA item. "
        "Product margins are about 1.5 points above the base; launch spend is 8% above the base G-MELT and YOCHIL programs. "
        "Cost build as the base (4% core inflation and 4% variable on same-store growth above the Q3 2026 annualized base)."
    )

    s1 = (
        "Q4 2026E VEVYE is the October–December 2026 path of the Vevye workbook (P8). "
        "September 2026 is 118 thousand TRx. October, November and December grow 5%% a month. "
        "Price starts at $117 per TRx and each month closes 3%% of the gap to $200. "
        "Revenue is price times TRx. TRx is in thousands on the sheet, so dollars are divided by 1,000 to reach US$ millions. "
        "October and November use that identity; the sheet's revenue row starts in December. "
        "Q4 2026E is $%.3f million on %.0f TRx. Nine-month printed revenue of $90.033 million is unchanged, so FY2026E VEVYE is $%.3f million."
        % (base_v["Q4E"], base_v["q4_trx"], base_v["FY26E"])
    )
    s21 = (
        "FY2027E–FY2032E VEVYE follows the Vevye workbook (P8), extended with the same recurrences through December 2032. "
        "From January 2027, monthly TRx is market share times market size. December 2026 share is 15.5%%. "
        "Monthly share gains start at 0.65 points in January 2027 and are multiplied by 0.9 each month, so share approaches 22%%. "
        "December 2026 market size is that month's TRx divided by 15.5%%, then the market grows 1%% a month. "
        "Price continues to close 3%% of the gap to $200 each month. "
        "The sheet ends in October 2032; November and December 2032 continue the same formulas. "
        "Dollars, US$ millions: %.3f / %.3f / %.3f / %.3f / %.3f / %.3f in FY2027E–FY2032E. "
        "Bull is 8%% above the workbook from January 2027. "
        "Bear matches the workbook through December 2028 (share %.2f%%) and then holds that share while the market and the price path continue. "
        "Product gross margin stays 80%% in the base. TRx is a model unit, not a reported prescription count."
        % (
            base_v["FY27E"],
            base_v["FY28E"],
            base_v["FY29E"],
            base_v["FY30E"],
            base_v["FY31E"],
            base_v["FY32E"],
            100.0 * base_annual[2028]["end_share"],
        )
    )
    replace_source(payload["sources"], "S1", s1)
    replace_source(payload["sources"], "S21", s21)
    payload["sources"].append(
        {
            "id": "P8",
            "document": "prompt",
            "page": "n/a",
            "text": (
                "Prompt [P], David, 14 November 2026: use the Vevye workbook Vevye model.xlsx in this folder "
                "(copied from C:\\Users\\david\\Documents\\Investing\\wd\\HROW\\Vevye model.xlsx) as the VEVYE path. "
                "September 2026 is 118 thousand TRx. October–December 2026 grow 5% a month. "
                "From January 2027, TRx is share times market size. December 2026 share is 15.5%. "
                "Monthly share gains start at 0.65 points and shrink by a factor of 0.9 each month. "
                "Market size grows 1% a month from December TRx divided by 15.5%. "
                "Price starts at $117 and closes 3% of the gap to $200 each month. "
                "Revenue is price times TRx, converted from thousands of dollars to US$ millions. "
                "October and November use that identity. The sheet ends October 2032; later months continue the same recurrences. "
                "Bull is 8% above the workbook from January 2027. "
                "Bear matches the workbook through December 2028 and then freezes share."
            ),
        }
    )
    payload["sources"].append(
        {
            "id": "P9",
            "document": "prompt",
            "page": "n/a",
            "text": (
                "Prompt [P], David, 14 November 2026: remove all year-0 equity raise adjustments from the base, bull, and bear schedules. "
                "Do not add a raise back if year-0 cash is negative. This overrides P6 for this case."
            ),
        }
    )

    # Point the VEVYE forecast citations at the workbook prompt while keeping one id per distinct value.
    line = next(item for item in payload["lines"] if item["name"] == "VEVYE")
    line["periods"]["Q4E"]["citation"]["text"] = s1
    for key in ("FY27E", "FY28E", "FY29E", "FY30E", "FY31E", "FY32E"):
        line["periods"][key]["citation"]["text"] = s21

    FORECAST.write_text(json.dumps(payload, indent=1, ensure_ascii=True) + "\n", encoding="utf-8")

    detail = {
        "base": {key: base_v[key] for key in ["Q4E", *YEARS, "FY33E", "q4_trx", "trx", "avg_price", "end_share", "end_price"]},
        "bull": {key: bull_v[key] for key in ["Q4E", *YEARS, "FY33E"]},
        "bear": {key: bear_v[key] for key in ["Q4E", *YEARS, "FY33E", "end_share"]},
        "company": applied,
        "dec_2028_share": base_annual[2028]["end_share"],
    }
    (HERE / "vevye_path.json").write_text(json.dumps(detail, indent=1), encoding="utf-8")

    snap = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    for label, vevye, stats in (
        ("", base_v, applied["base"]),
        ("BEAR_", bear_v, applied["bear"]),
        ("BULL_", bull_v, applied["bull"]),
    ):
        if label == "":
            for period in PERIODS:
                snap["LINES"]["VEVYE"][period] = vevye[period]
                snap["REV"][period] = stats["q4_rev"] if period == "Q4E" else stats["revenue"][period]
                snap["EBITDA"][period] = stats["q4_ebitda"] if period == "Q4E" else stats["ebitda"][period]
            snap["GM"]["Q4E"] = payload["totals"]["gross_margin"]["Q4E"]["value"]
            for year in YEARS:
                snap["GM"][year] = payload["totals"]["gross_margin"][year]["value"]
        else:
            key_v = label + "V"
            key_r = label + "REV"
            key_e = label + "EBITDA"
            for period in ("Q4E", *YEARS):
                snap[key_v][period] = vevye[period]
                if period == "Q4E":
                    snap[key_r][period] = stats["q4_rev"]
                    snap[key_e][period] = stats["q4_ebitda"]
                else:
                    snap[key_r][period] = stats["revenue"][period]
                    snap[key_e][period] = stats["ebitda"][period]
    snap["VEVYE"] = {
        "Q4E": base_v["Q4E"],
        "Q4E_trx": base_v["q4_trx"],
        "note": "Workbook path. See vevye_path.json.",
    }
    for year in YEARS[1:]:
        # Same-store moves one-for-one with VEVYE versus the pre-workbook base.
        pass
    SNAPSHOT.write_text(json.dumps(snap, indent=1) + "\n", encoding="utf-8")

    # drivers.csv: rewrite the VEVYE rows and the totals that move with VEVYE.
    rows = DRIVERS.read_text(encoding="utf-8").splitlines()
    def trx_m(key):
        return "%.0f" % base_v["trx"][key]

    vol = []
    prev_trx = base_v["trx"]["FY26E"]
    for year in YEARS[1:]:
        vol.append(base_v["trx"][year] / prev_trx - 1.0)
        prev_trx = base_v["trx"][year]
    rows[1] = (
        "VEVYE,revenue_usd_m,%s,%s,%s,%s,%s,%s,%s,"
        "\"Workbook (P8). Q4 2026E TRx %.0f at an average $%.2f per TRx. "
        "FY26 blends printed nine-month revenue with that quarter. "
        "From January 2027, TRx is share times a market that grows 1%% a month; "
        "share starts at 15.5%% in December 2026 and approaches 22%%. "
        "Price closes 3%% of the gap to $200 each month. "
        "FY27–FY32 TRx %.0f / %.0f / %.0f / %.0f / %.0f / %.0f.\""
        % (
            base_v["FY26E"],
            base_v["FY27E"],
            base_v["FY28E"],
            base_v["FY29E"],
            base_v["FY30E"],
            base_v["FY31E"],
            base_v["FY32E"],
            base_v["q4_trx"],
            base_v["avg_price"]["Q4E"],
            base_v["trx"]["FY27E"],
            base_v["trx"]["FY28E"],
            base_v["trx"]["FY29E"],
            base_v["trx"]["FY30E"],
            base_v["trx"]["FY31E"],
            base_v["trx"]["FY32E"],
        )
    )
    rows[2] = (
        "VEVYE,volume_growth_vs_prior,n/a,%.4f,%.4f,%.4f,%.4f,%.4f,%.4f,"
        "\"Output of the workbook share and market path, not an input rate. FY26 TRx is nine-month reconstructed 864,142 plus Q4.\""
        % tuple(vol)
    )
    prices = [base_v["avg_price"][year] for year in YEARS]
    rows[3] = (
        "VEVYE,npp_usd_per_trx,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,"
        "\"Average net dollars per model TRx. FY26 blends the printed nine months with the Q4 workbook. "
        "Later years are the workbook price path, which closes 3%% of the gap to $200 a month. "
        "Bull is 8%% above workbook revenue from January 2027, which is 8%% on this price at the workbook TRx. "
        "Bear uses the same price path and freezes share after December 2028.\""
        % tuple(prices)
    )
    # Total revenue, same-store, variable, ebitda: columns FY26..FY32 are fields 2..8
    base_rev = applied["base"]["revenue"]
    base_ebitda = applied["base"]["ebitda"]
    rows[24] = (
        "Total revenue,revenue_usd_m,%s,%s,%s,%s,%s,%s,%s,"
        "Sum of official lines plus the G-MELT and YOCHIL memo lines. FY2026E is nine-month actual plus Q4."
        % tuple(base_rev[year] for year in YEARS)
    )
    old_v = {
        "FY27E": 264.435, "FY28E": 367.017, "FY29E": 469.599,
        "FY30E": 572.18, "FY31E": 674.762, "FY32E": 777.344,
    }
    old_ss = {
        "FY27E": 556.684, "FY28E": 720.422, "FY29E": 883.161,
        "FY30E": 1047.398, "FY31E": 1212.136, "FY32E": 1377.875,
    }
    old_var = {
        "FY27E": 6.38, "FY28E": 12.929, "FY29E": 19.439,
        "FY30E": 26.008, "FY31E": 32.598, "FY32E": 39.227,
    }
    old_gp = {
        "FY27E": 468.07, "FY28E": 617.171, "FY29E": 784.319,
        "FY30E": 962.319, "FY31E": 1142.873, "FY32E": 1283.224,
    }
    old_ox = {
        "FY26E": 229.47, "FY27E": 290.893, "FY28E": 319.303, "FY29E": 330.067,
        "FY30E": 348.802, "FY31E": 367.983, "FY32E": 387.648,
    }
    ss, var, gp, ox = {}, {}, {}, {"FY26E": old_ox["FY26E"]}
    for year in YEARS[1:]:
        dv = base_v[year] - old_v[year]
        ss[year] = r3(old_ss[year] + dv)
        var[year] = r3(old_var[year] + 0.04 * dv)
        gp[year] = r3(old_gp[year] + 0.80 * dv)
        ox[year] = r3(old_ox[year] + (var[year] - old_var[year]))
    def money(seq):
        return ",".join("%s" % seq[year] for year in YEARS)

    rows[32] = (
        "Gross margin build,product_GP_before_amort_usd_m,n/a (9M+Q4 path),%s,%s,%s,%s,%s,%s,"
        "\"FY26 GP is built from the 9M+Q4 actual/estimate path, not from these forward rates. VEVYE is at 80%%.\""
        % tuple(gp[year] for year in YEARS[1:])
    )
    gm = payload["totals"]["gross_margin"]
    rows[34] = (
        "Gross margin build,GAAP_gross_margin_pct,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,"
        "(product GP − amort) / revenue from FY27. FY26 is the 9M+Q4 blend after a $2.5m Q4 inventory step-up that is not added back."
        % tuple(100.0 * gm[year]["value"] for year in YEARS)
    )
    rows[39] = (
        "Cash opex bridge,same_store_revenue_usd_m,n/a,%s,%s,%s,%s,%s,%s,"
        "\"Same-store revenue; Q3 2026 annualized base 397.188 = 4 × 99.297 (C17). VEVYE is inside this base and moves with the workbook.\""
        % tuple(ss[year] for year in YEARS[1:])
    )
    rows[40] = (
        "Cash opex bridge,same_store_variable_4pct_usd_m,n/a,%s,%s,%s,%s,%s,%s,"
        "\"4%% (S41) of same-store revenue above 397.188. Does not also take 4%% of TYRVAYA, BYOOVIZ, OPUVIZ, BYQLOVI, G-MELT or YOCHIL.\""
        % tuple(var[year] for year in YEARS[1:])
    )
    rows[41] = (
        "Cash opex bridge,total_cash_opex_usd_m,%s,"
        "\"FY26 cash opex is the 9M+Q4 build ($229.470m), not re-derived from this bridge. Later years move only with the 4%% variable piece on VEVYE.\""
        % money(ox)
    )
    # The line above inserted the note in the wrong column. Rebuild it properly.
    rows[41] = (
        "Cash opex bridge,total_cash_opex_usd_m,%s,%s,%s,%s,%s,%s,%s,"
        "\"FY26 cash opex is the 9M+Q4 build, not re-derived from this bridge. Later years move only with the 4%% variable piece on VEVYE.\""
        % tuple(ox[year] for year in YEARS)
    )
    margins = [100.0 * base_ebitda[year] / base_rev[year] for year in YEARS]
    rows[42] = (
        "Adjusted EBITDA,ebitda_usd_m,%s,%s,%s,%s,%s,%s,%s,"
        "Product GP − cash opex from FY27. FY26 is the 9M+Q4 cost build and is not forced to the more-than-$40m floor."
        % tuple(base_ebitda[year] for year in YEARS)
    )
    rows[43] = (
        "Adjusted EBITDA,ebitda_margin_pct,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,"
        "\"FY32 margin is the fully costed central result. It sits beyond the FY24A 20.2%% / FY25A 22.7%% history and is flagged, not capped.\""
        % tuple(margins)
    )
    bear_ebitda = applied["bear"]["ebitda"]
    old_bear_var = {
        "FY27E": 6.116, "FY28E": 11.063, "FY29E": 13.855,
        "FY30E": 13.726, "FY31E": 13.656, "FY32E": 13.703,
    }
    old_bear_v = {
        "FY27E": 221.815, "FY28E": 255.475, "FY29E": 264.655,
        "FY30E": 264.655, "FY31E": 264.655, "FY32E": 264.655,
    }
    bear_var = {year: r3(old_bear_var[year] + 0.08 * (bear_v[year] - old_bear_v[year])) for year in YEARS[1:]}
    rows[45] = (
        "Bear cost lever,bear_variable_8pct_usd_m,n/a,%s,%s,%s,%s,%s,%s,"
        "Bear variable 8%% of same-store revenue above the Q3 annualized base (S42). VEVYE is inside same-store, so this row moves with the bear VEVYE path."
        % tuple(bear_var[year] for year in YEARS[1:])
    )
    rows[46] = (
        "Bear cost lever,bear_ebitda_usd_m,%s,%s,%s,%s,%s,%s,%s,"
        "Bear Adjusted EBITDA with the operating-leverage lever and the workbook VEVYE path (share frozen after December 2028)."
        % tuple(bear_ebitda[year] for year in YEARS)
    )
    DRIVERS.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(json.dumps({name: {k: applied[name][k] for k in ("revenue", "ebitda", "q4_rev", "q4_ebitda", "fy33", "gsnext", "me", "mc")} for name in applied}, indent=1))
    print("VEVYE base", {k: base_v[k] for k in ["Q4E", *YEARS, "FY33E"]})
    print("VEVYE bull", {k: bull_v[k] for k in ["Q4E", *YEARS, "FY33E"]})
    print("VEVYE bear", {k: bear_v[k] for k in ["Q4E", *YEARS, "FY33E"]})
    print("Dec 2028 share", round(base_annual[2028]["end_share"], 4))


if __name__ == "__main__":
    main()
