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
