"""Offline checks for a collaborative valuation request."""

import json
from pathlib import Path

from forecastcheck.collaborative import (
    apply_post_finagle,
    check_request,
    render_valuation_section,
    scenario_updates,
    update_paths,
)
from forecastcheck.validate import validate_payload

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "tests" / "samples"


def _load(path):
    return json.loads(path.read_text())


def _synthetic():
    return _load(SAMPLES / "synthetic_min" / "request.json")


def _clpt():
    return _load(SAMPLES / "clpt_v11" / "request.json")


def _forecast_for(request, scenario="base"):
    """A forecast.json-shaped payload whose finagle block matches the request."""
    block = request["forecaster"][scenario]
    finagle = {
        "sales_growth": block["forecast.sales_growth"],
        "ebitda_growth": block["forecast.ebitda_growth"],
        "me": block["forecast.margin_path.me"],
        "mc": block["forecast.margin_path.mc"],
        "gsnext": block["forecast.margin_path.gsnext"],
        "ebitda_basis": block["forecast.ebitda_basis"]["value"],
    }
    if "forecast.acquisition_disclosure.status" in block:
        finagle["acquisition_disclosure"] = {
            "status": block["forecast.acquisition_disclosure.status"]["value"]
        }
    payload = {"ticker": request["ticker"], "finagle": finagle}
    if scenario != "base":
        payload = {"ticker": request["ticker"], "scenarios": {scenario: {"finagle": finagle}}}
    return payload


def test_synthetic_request_has_no_errors():
    assert check_request(_synthetic()) == []


def test_clpt_request_has_no_errors():
    assert check_request(_clpt()) == []


def test_prompt_item_needs_a_quote_and_a_date():
    request = _synthetic()
    request["prompt_inputs"] = [
        {"path": "market.shares", "value": 100.0, "applies_to": ["base"]}
    ]
    errors = check_request(request)
    assert any("quote" in error for error in errors)
    assert any("date" in error for error in errors)


def test_price_shares_and_rates_need_a_quote():
    request = _synthetic()
    request["prompt_inputs"] = [
        {"path": path, "value": 1.0, "applies_to": ["base"], "date": "2026-10-26"}
        for path in (
            "market.price",
            "market.shares",
            "rates.risk_free",
            "rates.re",
            "rates.gt",
        )
    ]
    errors = check_request(request)
    for path in ("market.price", "market.shares", "rates.risk_free", "rates.re", "rates.gt"):
        assert any(path in error and "quote" in error for error in errors)


def test_a_quoted_share_count_is_a_prompt_input():
    request = _synthetic()
    request["prompt_inputs"] = [
        {
            "path": "market.shares",
            "value": 30.5,
            "applies_to": ["base"],
            "quote": "use the share count from the filing",
            "date": "2026-10-26",
        }
    ]
    assert check_request(request) == []


def test_forecaster_block_must_match_the_forecast_file():
    request = _synthetic()
    forecast = _forecast_for(request)
    assert check_request(request, forecast) == []
    forecast["finagle"]["me"] = {"value": 0.99, "tag": "C", "citation": {"text": "changed"}}
    errors = check_request(request, forecast)
    assert any("differs from forecast.json" in error for error in errors)


def test_empty_prompt_inputs_add_no_leaves():
    request = _synthetic()
    updates = scenario_updates(request, "base")
    paths = update_paths(updates)
    assert request["prompt_inputs"] == []
    assert "forecast.sbc" not in paths
    assert "debt.mode" not in paths
    assert "rates.rd" not in paths
    assert "year" not in paths
    assert "forecast.sales_growth" in paths
    assert "forecast.margin_path.gsnext" in paths


def test_prompt_input_replaces_the_forecaster_leaf():
    request = _clpt()
    updates = scenario_updates(request, "base")
    gsnext = updates["leaves"]["forecast"]["margin_path"]["gsnext"]
    assert gsnext["value"] == 0.15
    assert gsnext["source"] == "prompt"
    assert updates["plain"]["year"] == 15
    sbc = updates["leaves"]["forecast"]["sbc"]
    assert sbc["source"] == "prompt"
    assert len(sbc["value"]) == 16


def test_synthetic_report_has_no_adjusted_value():
    request = _synthetic()
    result = _load(SAMPLES / "synthetic_min" / "result.json")
    applied = apply_post_finagle(10.0, request)
    assert applied["raw"] == 10.0
    assert applied["adjusted"] is None
    section = render_valuation_section(result, request)
    assert "10.0" in section
    assert "Adjusted" not in section
    assert "[P]" not in section


def test_post_finagle_factor_is_applied_only_from_the_request():
    request = _clpt()
    expected = _load(SAMPLES / "clpt_v11" / "expected.json")
    section_parts = []
    for name, row in expected["scenarios"].items():
        applied = apply_post_finagle(row["value_per_share"], request)
        assert abs(applied["adjusted"] - row["adjusted"]) < 0.0001
        section_parts.append(applied)
    bare = dict(request)
    bare["post_finagle"] = None
    assert apply_post_finagle(65.2013, bare)["adjusted"] is None
    result = {
        "finagle_commit": "bb39642",
        "scenarios": {
            name: {"value_per_share": row["value_per_share"], "defaults_filled": ["rates.re"]}
            for name, row in expected["scenarios"].items()
        },
    }
    section = render_valuation_section(result, request)
    assert "58.6812" in section
    assert "79.5195" in section
    assert "13.1019" in section
    assert "[P] 2026-10-26" in section
    assert "rates.re" in section


def test_existing_forecasts_still_validate():
    for path in sorted((ROOT / "forecasts").glob("*/forecast.json")):
        report = validate_payload(_load(path))
        assert report["ok"], (path.name, report["errors"])
