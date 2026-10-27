"""Re-derive the HROW forecast under the forecaster method.

Actuals are the filing figures checked for this file. Consensus revenue is
the yfinance pull carried from 2026-10-22 (not re-pulled here). Everything
else is recomputed. Writes forecasts/HROW/forecast.json.
"""

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / "forecast.json"

U10K = "https://www.sec.gov/Archives/edgar/data/1360214/000149315226008562/form10-k.htm"
U25 = "https://www.sec.gov/Archives/edgar/data/1360214/000149315226008552/ex99-1.htm"
U25L = "https://www.sec.gov/Archives/edgar/data/1360214/000149315226008552/ex99-2.htm"
U10Q = "https://www.sec.gov/Archives/edgar/data/1360214/000162828026055271/hrow-20260630.htm"
UQ2 = "https://www.sec.gov/Archives/edgar/data/1360214/000149315226036865/ex99-1.htm"
UQ1 = "https://www.sec.gov/Archives/edgar/data/1360214/000149315226022227/ex99-1.htm"
UQ1L = "https://www.sec.gov/Archives/edgar/data/1360214/000149315226022227/ex99-2.htm"
U280 = "https://www.sec.gov/Archives/edgar/data/1360214/000164117225009247/ex99-2.htm"
U280B = "https://www.sec.gov/Archives/edgar/data/1360214/000164117225022971/ex99-1.htm"
U270 = "https://www.sec.gov/Archives/edgar/data/1360214/000149315225021555/ex99-2.htm"
UTYR = "https://www.sec.gov/Archives/edgar/data/1360214/000162828026064749/hrow-20261001xex991.htm"
UYAHOO = "https://finance.yahoo.com/quote/HROW/analysis/"

FY24 = {
    "IHEEZO": 49.303,
    "VEVYE": 28.061,
    "Other branded": 37.836 + 0.915,
    "ImprimisRx": 83.499,
}
FY25 = {
    "IHEEZO": 81.348,
    "VEVYE": 88.688,
    "Other branded": 25.326 + 0.394,
    "ImprimisRx": 76.547,
}
Q2 = {
    "IHEEZO": 15.619,
    "VEVYE": 29.387,
    "Other branded": 11.009 + 0.090,
    "ImprimisRx": 14.556,
}
H1 = {
    "IHEEZO": 17.535,
    "VEVYE": 50.335,
    "Other branded": 18.776 + 0.163,
    "ImprimisRx": 28.055,
}
FY25_EBITDA = 61.923
H1_EBITDA = -13.891
OPEX_Q = 61.370 - 3.788 - 0.460  # Q2 GAAP opex less SBC and depreciation (amortization sits in cost of sales)
AMORT_Q = 5.527  # Q2 amortization of intangibles, in cost of sales; added back to reach adjusted EBITDA
assert abs((50.363 + AMORT_Q - OPEX_Q) - (-1.232)) < 0.001  # reconciles to reported Q2 adjusted EBITDA
USA = "https://seekingalpha.com/article/4934770-harrow-inc-hrow-q2-2026-earnings-call-transcript"
LTM_GP = 204.369 - 79.819 + 77.408
LTM_REV = 272.303 - 111.573 + 114.864
LTM_GM = LTM_GP / LTM_REV
DECLINE = FY25["ImprimisRx"] / FY24["ImprimisRx"] - 1

# Unscaled H2 and FY27, before the revenue total is applied.
IH_Q = Q2["IHEEZO"] * 1.25
V3 = Q2["VEVYE"] * 1.075
V4 = V3 * 1.075
H2_U = {
    "IHEEZO": 2 * IH_Q,
    "VEVYE": V3 + V4,
    "Other branded": 13.0 + 14.5 + 4.0,
    "ImprimisRx": 2 * Q2["ImprimisRx"],
}
F27_U = {
    "IHEEZO": 4 * IH_Q * (1 + 0.34 / 2),
    "VEVYE": 4 * V4 * 1.10,
    "Other branded": 4 * 14.5 * 1.15 + 30.0,
    "ImprimisRx": 4 * Q2["ImprimisRx"] * (1 + DECLINE),
}
TYR_OPEX_26 = 5.0
TYR_OPEX_27 = 20.0
H1_REV = sum(H1.values())


def fact(value, tag, text, url):
    if isinstance(value, float):
        value = round(value, 6)
    elif isinstance(value, list):
        value = [round(item, 6) if isinstance(item, float) else item for item in value]
    return {"value": value, "tag": tag, "citation": {"text": text, "url": url}}


def scenario(revenue_26, revenue_27, gross_margin, opex_inflation):
    h2_target = revenue_26 - H1_REV
    scale_26 = h2_target / sum(H2_U.values())
    scale_27 = revenue_27 / sum(F27_U.values())
    fy26 = {name: H1[name] + H2_U[name] * scale_26 for name in H2_U}
    fy27 = {name: F27_U[name] * scale_27 for name in F27_U}
    h2 = {name: fy26[name] - H1[name] for name in fy26}
    tyr26 = 4.0 * scale_26
    tyr27 = 30.0 * scale_27
    opex_h2 = 2 * OPEX_Q + TYR_OPEX_26
    ebitda_26 = H1_EBITDA + h2_target * gross_margin + 2 * AMORT_Q - opex_h2
    opex_27 = 4 * OPEX_Q * (1 + opex_inflation) + TYR_OPEX_27
    ebitda_27 = revenue_27 * gross_margin + 4 * AMORT_Q - opex_27
    tyr_ebitda_26 = tyr26 * gross_margin - TYR_OPEX_26
    tyr_ebitda_27 = tyr27 * gross_margin - TYR_OPEX_27
    organic_revenue_26 = revenue_26 - tyr26
    organic_revenue_27 = revenue_27 - tyr27
    organic_ebitda_26 = ebitda_26 - tyr_ebitda_26
    organic_ebitda_27 = ebitda_27 - tyr_ebitda_27
    return {
        "scale_26": scale_26,
        "scale_27": scale_27,
        "fy26": fy26,
        "fy27": fy27,
        "h2": h2,
        "revenue_26": revenue_26,
        "revenue_27": revenue_27,
        "ebitda_26": ebitda_26,
        "ebitda_27": ebitda_27,
        "opex_h2": opex_h2,
        "opex_27": opex_27,
        "tyr26": tyr26,
        "tyr27": tyr27,
        "tyr_ebitda_26": tyr_ebitda_26,
        "tyr_ebitda_27": tyr_ebitda_27,
        "organic_revenue_26": organic_revenue_26,
        "organic_revenue_27": organic_revenue_27,
        "organic_ebitda_26": organic_ebitda_26,
        "organic_ebitda_27": organic_ebitda_27,
        "gross_margin": gross_margin,
        "gf": [
            organic_ebitda_26 / FY25_EBITDA - 1,
            organic_ebitda_27 / organic_ebitda_26 - 1,
        ],
        "sg": [
            organic_revenue_26 / sum(FY25.values()) - 1,
            organic_revenue_27 / organic_revenue_26 - 1,
        ],
    }


def line_block(result, revenue_why, scale_note):
    lines = []
    notes = {
        "IHEEZO": (
            "Price: July 1, 2026 net price per unit +25%, so H2 quarters are Q2 revenue times 1.25 with units held at the Q2 run rate (65,477, already +34% year over year). FY27 units grow 17%, half that Q2 unit growth, because a recent launch rarely keeps a 34% unit step. "
            + scale_note
        ),
        "VEVYE": (
            "Volume and mix after the August 1 coverage win: H2 steps +7.5% a quarter off Q2, faster than the 'momentum continues' default of holding the prior growth rate, and FY27 is the Q4 run rate times 4 times 1.10. The 'over $100 million' 2026 floor is met. The Q1 gross-to-net cut of about $8 million is one-time and is not in this run rate. "
            + scale_note
        ),
        "Other branded": (
            "BYOOVIZ and the rest of the branded book are a new-line ramp (Q3 13 and Q4 14.5 are judgments; the filing only says revenue builds over the balance of 2026). TYRVAYA adds a $4 million Q4 stub, inside the 1-3% 'modest' band, and a $30 million 2027 floor ('more than $30 million'). "
            + scale_note
        ),
        "ImprimisRx": (
            "Mature compounding book: H2 is flat at the Q2 run rate, and FY27 applies the FY25 volume decline (ImprimisRx fell year over year). No structural change was guided. "
            + scale_note
        ),
    }
    actual_url = {
        "IHEEZO": U10K,
        "VEVYE": U10K,
        "Other branded": U10K,
        "ImprimisRx": U10K,
    }
    actual_text = {
        "IHEEZO": "FY2025 10-K product revenue, IHEEZO. FY2024 is the prior-year column of the same table.",
        "VEVYE": "FY2025 10-K product revenue, VEVYE. FY2024 is the prior-year column of the same table.",
        "Other branded": "FY2025 10-K 'other branded products' plus 'other revenues'. Same split for FY2024. Not a finer cut than the filing.",
        "ImprimisRx": "FY2025 10-K ImprimisRx (compounding) revenue. FY2024 is the prior-year column.",
    }
    h1_text = {
        "IHEEZO": "Q2 2026 10-Q six-month IHEEZO revenue. H1 is reported; it is not forecast.",
        "VEVYE": "Q2 2026 10-Q six-month VEVYE revenue.",
        "Other branded": "Q2 2026 10-Q six-month other branded products plus other revenues.",
        "ImprimisRx": "Q2 2026 10-Q six-month compounding revenue.",
    }
    for name in ("IHEEZO", "VEVYE", "Other branded", "ImprimisRx"):
        yoy = FY25[name] / FY24[name] - 1
        lines.append(
            {
                "name": name,
                "periods": {
                    "FY24A": fact(FY24[name], "A", actual_text[name], actual_url[name]),
                    "FY25A": fact(FY25[name], "A", actual_text[name], actual_url[name]),
                    "YoY": fact(
                        yoy,
                        "C",
                        "Year-over-year growth of the reported line, FY25 divided by FY24 minus 1.",
                        actual_url[name],
                    ),
                    "H1A": fact(H1[name], "A", h1_text[name], U10Q),
                    "H2E": fact(
                        result["h2"][name],
                        "S",
                        notes[name] + " H2 is the unreported half only.",
                        UQ2,
                    ),
                    "FY26E": fact(result["fy26"][name], "S", notes[name], UQ2),
                    "FY27E": fact(
                        result["fy27"][name],
                        "S",
                        notes[name] + " FY27 is still inside the explicit window; no FY28 dollars are set.",
                        UQ2,
                    ),
                },
            }
        )
    return lines


def organic_block(result):
    return {
        "revenue": {
            "FY25A": fact(
                sum(FY25.values()),
                "A",
                "Year-0 revenue. TYRVAYA had not closed, so year-0 is already organic.",
                U10K,
            ),
            "FY26E": fact(
                result["organic_revenue_26"],
                "C",
                "Consensus revenue minus TYRVAYA, which closed after year 0 and is booked as an acquisition rather than in the organic path.",
                UTYR,
            ),
            "FY27E": fact(
                result["organic_revenue_27"],
                "C",
                "FY27 consensus revenue minus TYRVAYA's scaled 2027 floor, kept out of organic sales growth.",
                UTYR,
            ),
        },
        "ebitda": {
            "FY25A": fact(
                FY25_EBITDA,
                "A",
                "FY2025 adjusted EBITDA from the March 2, 2026 earnings release reconciliation.",
                U25,
            ),
            "FY26E": fact(
                result["organic_ebitda_26"],
                "C",
                "Cost-build EBITDA minus TYRVAYA's contribution (its revenue times the gross-margin assumption, less the assumed incremental cost).",
                UQ2,
            ),
            "FY27E": fact(
                result["organic_ebitda_27"],
                "C",
                "FY27 cost-build EBITDA minus TYRVAYA, so forecast_ebitda does not also get EBITDA that acquisitions will add.",
                UTYR,
            ),
        },
    }


def finagle_block(result):
    me = result["organic_ebitda_27"] / result["organic_revenue_27"]
    mc = (me + result["gross_margin"]) / 2
    multiple = 30.0 / result["tyr_ebitda_27"]
    return {
        "ebitda_basis": fact(
            "organic",
            "C",
            "TYRVAYA closes in October 2026, after FY2025, so the EBITDA path stays organic and the purchase is an acquisition.",
            UTYR,
        ),
        "ebitda_growth": fact(
            result["gf"],
            "C",
            "Organic adjusted-EBITDA growth for FY26 and FY27 off FY25. The FY27 step is large because consensus revenue is scaled up and cash opex stays on the Q2 run rate; that is a flagged consequence, not a margin target management stated.",
            U25,
        ),
        "sales_growth": fact(
            result["sg"],
            "C",
            "Organic sales growth for the same two years. Finagle recomputes the margin it passes to forecast_ebitda as ending organic EBITDA over ending organic revenue, so these rates are the ones that reproduce those dollars.",
            U10K,
        ),
        "me": fact(
            me,
            "C",
            "Final explicit year organic EBITDA divided by organic revenue. This is the margin forecast_ebitda uses once sales growth reaches that year, not the year-0 margin.",
            U25,
        ),
        "mc": fact(
            mc,
            "S",
            "Contribution margin set halfway between that ending EBITDA margin and the trailing gross margin, which is the band a dollar of extra sales should fall in. Finagle's own filler would average the year-0 margin instead; this is set on purpose so the fade is not that default.",
            U10Q,
        ),
        "gsnext": fact(
            0.20,
            "S",
            "First sales growth after the explicit window. FY25 revenue grew 36%, and management still expects a launch a year through 2029 inside the existing cost structure, but there is no FY28 dollar evidence, so 20% fades the explicit step-up instead of repeating it. Terminal growth after that is Finagle's.",
            UQ2,
        ),
        "deal_spend": fact(
            [0, 30],
            "G",
            "Cash paid at the October 5, 2026 close. Index 0 is FY2025, which had no deal. Contingent milestones of up to $70 million are not included.",
            UTYR,
        ),
        "acquisition": {
            "year": fact(1, "G", "Close is October 5, 2026, the first forecast year if year 0 is FY2025.", UTYR),
            "deal_value": fact(30, "G", "Harrow paid $30 million in cash at closing.", UTYR),
            "multiple": fact(
                multiple,
                "S",
                "Cash paid divided by FY27 TYRVAYA EBITDA. That EBITDA is the scaled revenue floor times gross margin, less an assumed $20 million of incremental cost, because the filing says revenue exceeds incremental cost and does not give the cost.",
                UTYR,
            ),
            "leverage": fact(0, "G", "Funded with cash at closing, so the deal adds no debt.", UTYR),
            "next_growth": fact(
                0.15,
                "S",
                "No growth rate after the 2027 floor was stated. 15% is a placeholder below the organic gsnext fade and should be replaced if a later source appears.",
                UTYR,
            ),
            "capex_frac": fact(
                0.02,
                "S",
                "No capex figure was given for the brand. 2% of acquired EBITDA is a thin asset-light placeholder.",
                UTYR,
            ),
            "pay_from_cash": fact(
                False,
                "C",
                "The cash left the company at a year-1 close. Finagle's pay_from_cash flag only reduces year-0 cash, so it is false here.",
                UTYR,
            ),
        },
    }


def totals(result, revenue_text, revenue_tag):
    return {
        "revenue": {
            "FY24A": fact(sum(FY24.values()), "A", "FY2024 revenue, prior-year column of the FY2025 10-K.", U10K),
            "FY25A": fact(sum(FY25.values()), "A", "FY2025 revenue, 10-K and the March 2, 2026 release.", U10K),
            "YoY": fact(
                sum(FY25.values()) / sum(FY24.values()) - 1,
                "C",
                "Reported FY25 revenue over FY24 revenue, minus 1.",
                U10K,
            ),
            "H1A": fact(H1_REV, "A", "Six months ended June 30, 2026 revenue, Q2 10-Q.", U10Q),
            "H2E": fact(
                result["revenue_26"] - H1_REV,
                revenue_tag,
                revenue_text + " H2 is the consensus (or scenario) year minus reported H1.",
                UYAHOO,
            ),
            "FY26E": fact(result["revenue_26"], revenue_tag, revenue_text, UYAHOO),
            "FY27E": fact(
                result["revenue_27"],
                revenue_tag,
                "FY27 has no formal range. The same branch, estimates because the latest completed range was missed, uses the carried FY27 consensus.",
                UYAHOO,
            ),
        },
        "ebitda": {
            "FY24A": fact(40.327, "A", "FY2024 adjusted EBITDA, March 2, 2026 release reconciliation.", U25),
            "FY25A": fact(FY25_EBITDA, "A", "FY2025 adjusted EBITDA, March 2, 2026 release reconciliation.", U25),
            "YoY": fact(
                FY25_EBITDA / 40.327 - 1,
                "C",
                "FY25 adjusted EBITDA over FY24 adjusted EBITDA, minus 1.",
                U25,
            ),
            "H1A": fact(H1_EBITDA, "A", "First-half 2026 adjusted EBITDA, August 10, 2026 release reconciliation.", UQ2),
            "H2E": fact(
                result["ebitda_26"] - H1_EBITDA,
                "C",
                "H2 revenue times the scenario GAAP gross margin ('increasing gross margins into the high 70s'), plus two quarters of Q2 amortization in cost of sales (5.527 each, added back to adjusted EBITDA), minus base adjusted opex held flat at Q2 (57.122 a quarter; 'base SG&A dollars to remain approximately flat with second quarter levels for the balance of the year') and an assumed $5 million Q4 TYRVAYA cost. Q2 2026 call, August 2026.",
                UQ2,
            ),
            "FY26E": fact(
                result["ebitda_26"],
                "C",
                "H1 adjusted EBITDA plus the H2 bridge management described: 'substantially higher revenue, increasing gross margins into the high 70s, and a base operating expense structure that remains approximately flat.' Revenue is consensus, so the result sits below the $80-100 million guide. No EBITDA coefficient or estimate exists.",
                UQ2,
            ),
            "FY27E": fact(
                result["ebitda_27"],
                "S",
                "FY27 revenue times the scenario GAAP gross margin held at the H2 level, plus four quarters of Q2 amortization, minus four quarters of Q2 base adjusted opex grown by the scenario inflation, minus about $20 million of TYRVAYA SG&A ('increasing SG&A expenses by approximately $20 million on an annualized basis once fully integrated', Q2 call).",
                UQ2,
            ),
        },
    }


def main():
    base = scenario(350.144, 536.328, 0.78, 0.03)
    bear = scenario(341.0, 479.0, 0.77, 0.08)
    bull = scenario(355.0, 587.0, 0.79, 0.00)
    scale_note = (
        "The line is then scaled so unreported revenue hits the scenario total. "
        "The factor is well above 1.1, so the filing commentary does not by itself support the total; the lines allocate it."
    )
    revenue_text = (
        "H1 revenue was $114.864 million against an original H1 range of $133-153 million, so the position coefficient is negative. "
        "Analyst revenue estimates exist, so FY26 uses the Yahoo consensus carried from yfinance on 2026-10-22 ($350.144 million; range $341-355 million), not the $350-365 million guide. "
        "Re-pulled from yfinance on 2026-10-22 and unchanged. The lines are scaled to this total; the unscaled build is a diagnostic only."
    )
    c_h1 = (114.864 - 133) / (153 - 133)
    c_q2 = (70.661 - 71) / (81 - 71)
    payload = {
        "ticker": "HROW",
        "company": "Harrow, Inc.",
        "units": "USD millions",
        "baseline_period": "FY25A",
        "explicit_periods": ["FY26E", "FY27E"],
        "as_of": "2026-10-22",
        "method_note": (
            "Re-derived under the guidance-position method. FY25 guidance was a single point, so no coefficient. "
            "FY26 revenue leaves the range because H1 missed the low end and a revenue consensus exists."
        ),
        "lines": line_block(base, revenue_text, scale_note),
        "totals": totals(base, revenue_text, "E"),
        "organic": organic_block(base),
        "finagle": finagle_block(base),
        "bridge": {
            "h1_coefficient": fact(
                c_h1,
                "C",
                "H1 actual minus the original low, divided by the original high minus low. Negative means the low end was missed, so the revenue total switches to estimates.",
                U25,
            ),
            "q2_coefficient": fact(
                c_q2,
                "C",
                "Q2 actual versus the May 11 range of $71-81 million. Also below the low end. Shown as a second completed window; the H1 window is the one that sets the branch.",
                UQ1,
            ),
            "scale_fy26_h2": fact(
                base["scale_26"],
                "C",
                "Consensus H2 revenue divided by the unscaled line build. More than 10% from 1, so line commentary and the top-level total disagree.",
                UYAHOO,
            ),
            "scale_fy27": fact(
                base["scale_27"],
                "C",
                "FY27 consensus divided by the unscaled line build. More than 10% from 1.",
                UYAHOO,
            ),
            "q2_amortization_in_cogs": fact(AMORT_Q, "A", "Q2 2026 amortization of intangible assets, from the adjusted EBITDA reconciliation. The Q2 letter attributes the gross-margin decline partly to 'amortization of acquired NDAs', so it is in cost of sales.", UQ2),
            "gross_margin_basis": fact(0.78, "S", "Base H2 and FY27 GAAP gross margin, the midpoint of a 77-79% reading of 'high 70s'. GAAP basis because management's 71% Q2 figure and 'trend back towards the high 70s' are both GAAP gross margin. Amortization is then added back to reach adjusted EBITDA. Q2 cash gross margin was (50.363 + 5.527) / 70.661 = 79.1%.", USA),
            "ltm_gross_margin": fact(
                LTM_GM,
                "C",
                "Trailing gross profit over trailing revenue: FY25 gross profit, minus H1 2025 gross profit, plus H1 2026 gross profit. Held for the unreported periods because no newer margin guide was given.",
                U10Q,
            ),
            "q2_cash_opex": fact(
                OPEX_Q,
                "C",
                "Q2 total operating expenses 61.370 minus stock-based compensation 3.788 and depreciation 0.460. Amortization of intangibles (5.527) sits in cost of sales, so it is not in opex. Check: gross profit 50.363 + amortization 5.527 - 57.122 = -1.232, the reported Q2 adjusted EBITDA.",
                UQ2,
            ),
            "unscaled_h2_revenue": fact(
                sum(H2_U.values()),
                "S",
                "Sum of the line drivers before scaling: IHEEZO price step, VEVYE sequential step, other-branded ramp plus the TYRVAYA stub, ImprimisRx flat at Q2.",
                UQ2,
            ),
            "unscaled_fy27_revenue": fact(
                sum(F27_U.values()),
                "S",
                "Sum of the FY27 line drivers before scaling, including the $30 million TYRVAYA floor.",
                UQ2,
            ),
        },
        "scenarios": {
            "bear": {
                "levers": "Consensus low, GAAP gross margin 77% (low edge of 'high 70s') H2 and FY27, FY27 base opex +8%.",
                "lines": line_block(bear, "Bear revenue is the low end of the carried consensus range.", scale_note),
                "totals": totals(
                    bear,
                    "Bear uses the low end of the carried Yahoo range, $341 million for FY26 and $479 million for FY27. Not re-pulled.",
                    "E",
                ),
                "organic": organic_block(bear),
                "finagle": finagle_block(bear),
            },
            "bull": {
                "levers": "Consensus high, GAAP gross margin 79% (high edge of 'high 70s') H2 and FY27, no FY27 base opex inflation.",
                "lines": line_block(bull, "Bull revenue is the high end of the carried consensus range.", scale_note),
                "totals": totals(
                    bull,
                    "Bull uses the high end of the carried Yahoo range, $355 million for FY26 and $587 million for FY27. Not re-pulled.",
                    "E",
                ),
                "organic": organic_block(bull),
                "finagle": finagle_block(bull),
            },
        },
    }
    # The three scenarios differ only by those levers. Base is the top-level case.
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print("wrote", OUT)
    for label, result in ("base", base), ("bear", bear), ("bull", bull):
        print(
            label,
            "k",
            round(result["scale_26"], 4),
            round(result["scale_27"], 4),
            "rev",
            round(result["revenue_26"], 3),
            round(result["revenue_27"], 3),
            "ebitda",
            round(result["ebitda_26"], 3),
            round(result["ebitda_27"], 3),
            "me",
            round(result["organic_ebitda_27"] / result["organic_revenue_27"], 4),
            "gf",
            [round(x, 4) for x in result["gf"]],
            "sg",
            [round(x, 4) for x in result["sg"]],
            "mult",
            round(30 / result["tyr_ebitda_27"], 2),
        )


if __name__ == "__main__":
    main()
