"""Schema checks for forecasts/<TICKER>/forecast.json.

A forecast number is an object with value, tag, and citation. Bare numbers
are rejected. Line dollars sum to the stated totals. The Finagle leaves the
forecaster owns (EBITDA growth, sales growth, me, mc, gsnext) are present
and consistent with the organic dollars.
"""

import json
from pathlib import Path

import pytest

from forecastcheck.validate import validate_payload

ROOT = Path(__file__).resolve().parents[1]
HROW = ROOT / "forecasts" / "HROW" / "forecast.json"

TAGS = {"A", "G", "E", "P", "S", "C"}
DOLLAR_KEYS = ("FY24A", "FY25A", "H1A", "H2E", "FY26E", "FY27E")


def _load(path):
    return json.loads(path.read_text())


def _fact(value, tag="A"):
    return {
        "value": value,
        "tag": tag,
        "citation": {"text": "example", "url": "https://example.test/filing"},
    }


def _minimal(**overrides):
    payload = {
        "ticker": "EX",
        "baseline_period": "FY25A",
        "explicit_periods": ["FY26E", "FY27E"],
        "lines": [
            {
                "name": "Alpha",
                "periods": {"FY25A": _fact(40), "FY26E": _fact(50, "S"), "FY27E": _fact(60, "S")},
            },
            {
                "name": "Beta",
                "periods": {"FY25A": _fact(60), "FY26E": _fact(70, "S"), "FY27E": _fact(80, "S")},
            },
        ],
        "totals": {
            "revenue": {"FY25A": _fact(100), "FY26E": _fact(120, "E"), "FY27E": _fact(140, "E")},
            "ebitda": {"FY25A": _fact(20), "FY26E": _fact(24, "S"), "FY27E": _fact(30, "S")},
        },
        "organic": {
            "revenue": {"FY25A": _fact(100), "FY26E": _fact(110, "C"), "FY27E": _fact(121, "C")},
            "ebitda": {"FY25A": _fact(20), "FY26E": _fact(22, "C"), "FY27E": _fact(25, "C")},
        },
        "finagle": {
            "ebitda_growth": _fact([22 / 20 - 1, 25 / 22 - 1], "C"),
            "sales_growth": _fact([110 / 100 - 1, 121 / 110 - 1], "C"),
            "me": _fact(25 / 121, "C"),
            "mc": _fact(0.4, "S"),
            "gsnext": _fact(0.1, "S"),
        },
    }
    payload.update(overrides)
    return payload


def test_minimal_payload_passes():
    report = validate_payload(_minimal())
    assert report["ok"], report["errors"]


def test_untagged_number_fails():
    payload = _minimal()
    payload["lines"][0]["periods"]["FY25A"] = 40
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("tag" in error or "number" in error for error in report["errors"])


def test_missing_citation_fails():
    payload = _minimal()
    payload["totals"]["revenue"]["FY26E"] = {"value": 120, "tag": "E"}
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("citation" in error for error in report["errors"])


def test_lines_must_sum_to_revenue_totals():
    payload = _minimal()
    payload["totals"]["revenue"]["FY26E"] = _fact(999, "E")
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("sum" in error for error in report["errors"])


def test_finagle_leaves_are_required():
    payload = _minimal()
    del payload["finagle"]["gsnext"]
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("gsnext" in error for error in report["errors"])


def test_growth_must_match_organic_dollars():
    payload = _minimal()
    payload["finagle"]["sales_growth"] = _fact([0.5, 0.5], "C")
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("sales_growth" in error for error in report["errors"])


def test_h1_plus_h2_matches_fy26_when_both_are_present():
    payload = _minimal()
    payload["lines"][0]["periods"]["H1A"] = _fact(20)
    payload["lines"][0]["periods"]["H2E"] = _fact(20, "S")  # 40, but FY26E is 50
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("H1A" in error for error in report["errors"])


def test_hrow_forecast_passes():
    assert HROW.is_file(), "forecasts/HROW/forecast.json is missing"
    report = validate_payload(_load(HROW))
    assert report["ok"], report["errors"]
    assert _load(HROW)["ticker"] == "HROW"


@pytest.mark.parametrize("tag", sorted(TAGS))
def test_known_tags_are_accepted(tag):
    payload = _minimal()
    payload["totals"]["revenue"]["FY27E"] = _fact(140, tag)
    report = validate_payload(payload)
    assert report["ok"], report["errors"]


def _july_fy():
    """A July-year case: FY26A baseline, FY27E/FY28E explicit."""
    payload = _minimal(baseline_period="FY26A", explicit_periods=["FY27E", "FY28E"])
    rename = {"FY25A": "FY26A", "FY26E": "FY27E", "FY27E": "FY28E"}
    for line in payload["lines"]:
        line["periods"] = {rename[k]: v for k, v in line["periods"].items()}
    for group in ("totals", "organic"):
        for key, series in payload[group].items():
            payload[group][key] = {rename[k]: v for k, v in series.items()}
    return payload


def test_july_fy_case_passes():
    report = validate_payload(_july_fy())
    assert report["ok"], report["errors"]


def test_july_fy_sum_outside_old_template_fails():
    payload = _july_fy()
    payload["totals"]["revenue"]["FY28E"] = _fact(999, "E")
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("FY28E lines sum" in error for error in report["errors"])


def test_july_fy_compounding_is_checked():
    payload = _july_fy()
    payload["finagle"]["sales_growth"] = _fact([0.1, 0.5], "C")
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("sales_growth does not compound to FY28E" in error for error in report["errors"])


def test_growth_list_length_mismatch_fails_loudly():
    payload = _july_fy()
    payload["finagle"]["sales_growth"] = _fact([0.1], "C")
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("1 rates" in error for error in report["errors"])


def test_unrecognized_period_fails():
    payload = _minimal()
    payload["lines"][0]["periods"]["FY2027"] = _fact(60, "S")
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("unrecognized period" in error for error in report["errors"])


def test_nine_month_plus_q4_stub_passes_and_fails():
    payload = _minimal()
    payload["lines"][0]["periods"]["9MA"] = _fact(35)
    payload["lines"][0]["periods"]["Q4E"] = _fact(15, "S")  # 50 == FY26E
    report = validate_payload(payload)
    assert report["ok"], report["errors"]
    payload["lines"][0]["periods"]["Q4E"] = _fact(10, "S")  # 45 != 50
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("9MA+Q4E" in error for error in report["errors"])


def test_stub_of_maps_halves_to_a_later_year():
    payload = _minimal(stub_of={"H1E": "FY27E", "H2E": "FY27E"})
    payload["lines"][0]["periods"]["H1E"] = _fact(30, "S")
    payload["lines"][0]["periods"]["H2E"] = _fact(20, "S")  # 50 != FY27E 60
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("FY27E" in error and "H1E+H2E" in error for error in report["errors"])


def test_finagle_leaves_optional_without_handoff():
    payload = _minimal(finagle_handoff=False)
    del payload["finagle"]
    report = validate_payload(payload)
    assert report["ok"], report["errors"]


def test_finagle_leaves_required_by_default():
    payload = _minimal()
    del payload["finagle"]
    report = validate_payload(payload)
    assert not report["ok"]


def test_line_pattern_is_validated():
    payload = _minimal()
    payload["lines"][0]["pattern"] = "ramping"
    assert validate_payload(payload)["ok"]
    payload["lines"][0]["pattern"] = "hockey stick"
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("pattern" in error for error in report["errors"])


def _with_ids():
    """The minimal case with numbered citations and a sources list."""
    payload = _minimal()
    counters = {}
    for _, fact in _iter_facts(payload):
        tag = fact["tag"]
        key = (tag, repr(fact["value"]))
        if key not in counters:
            counters[key] = "%s%d" % (tag, sum(1 for k in counters if k[0] == tag) + 1)
        fact["citation"]["id"] = counters[key]
        fact["citation"]["page"] = "p.1"
    sources = [{"id": "D1", "text": "Example filing: https://example.test/filing"}]
    for sid in sorted(set(counters.values())):
        entry = {"id": sid, "text": "example", "document": "D1"}
        if sid.startswith("C"):
            entry["inputs"] = ["D1"]
        sources.append(entry)
    payload["sources"] = sources
    return payload


def _iter_facts(obj):
    if isinstance(obj, dict) and "value" in obj and "tag" in obj:
        yield None, obj
    elif isinstance(obj, dict):
        for value in obj.values():
            yield from _iter_facts(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from _iter_facts(item)


def test_numbered_citations_pass():
    report = validate_payload(_with_ids())
    assert report["ok"], report["errors"]


def test_unresolved_id_fails():
    payload = _with_ids()
    payload["lines"][0]["periods"]["FY25A"]["citation"]["id"] = "A99"
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("A99 does not resolve" in error for error in report["errors"])


def test_duplicate_id_for_different_facts_fails():
    payload = _with_ids()
    reused = payload["lines"][0]["periods"]["FY25A"]["citation"]["id"]
    payload["lines"][1]["periods"]["FY25A"]["citation"]["id"] = reused
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("different fact" in error for error in report["errors"])


def test_duplicate_source_entry_fails():
    payload = _with_ids()
    payload["sources"].append({"id": "D1", "text": "again"})
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("listed twice" in error for error in report["errors"])


def test_calculation_inputs_must_exist():
    payload = _with_ids()
    calc = next(entry for entry in payload["sources"] if entry["id"].startswith("C"))
    calc["inputs"] = ["A42"]
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("input A42" in error for error in report["errors"])


def test_citation_needs_page_or_unverified():
    payload = _with_ids()
    del payload["lines"][0]["periods"]["FY25A"]["citation"]["page"]
    assert not validate_payload(payload)["ok"]
    payload["lines"][0]["periods"]["FY25A"]["citation"]["page_status"] = "unverified"
    assert validate_payload(payload)["ok"]

def test_yoy_prefixed_keys_are_growth_not_dollars():
    payload = _minimal()
    for line in payload["lines"]:
        line["periods"]["YoY_FY26"] = _fact(0.2, "C")
    payload["totals"]["revenue"]["YoY_FY26"] = _fact(0.2, "C")
    report = validate_payload(payload)
    assert report["ok"], report["errors"]


def test_reference_quarter_is_summed_but_not_a_stub():
    payload = _minimal()
    payload["lines"][0]["periods"]["Q4FY26A"] = _fact(12)
    payload["lines"][1]["periods"]["Q4FY26A"] = _fact(18)
    payload["totals"]["revenue"]["Q4FY26A"] = _fact(30)
    report = validate_payload(payload)
    assert report["ok"], report["errors"]
    payload["totals"]["revenue"]["Q4FY26A"] = _fact(31)
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("Q4FY26A lines sum" in error for error in report["errors"])


def test_pattern_may_carry_a_parenthetical_note():
    payload = _minimal()
    payload["lines"][0]["pattern"] = "ramping (share gain abroad)"
    assert validate_payload(payload)["ok"]
    payload["lines"][0]["pattern"] = "mature"
    assert not validate_payload(payload)["ok"]


def test_missing_sources_is_a_warning_not_an_error():
    report = validate_payload(_minimal())
    assert report["ok"], report["errors"]
    assert any("sources" in warning for warning in report["warnings"])
    assert not validate_payload(_with_ids())["warnings"]


def test_age_source_entries_need_quote_text():
    payload = _with_ids()
    entry = next(e for e in payload["sources"] if e["id"].startswith("A"))
    entry["text"] = "  "
    report = validate_payload(payload)
    assert not report["ok"]
    assert any("quoted source text" in error for error in report["errors"])
