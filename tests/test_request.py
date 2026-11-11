"""Offline checks for a collaborative valuation request."""

import importlib.util
import json
import math
from datetime import date
from pathlib import Path

from forecastcheck.collaborative import (
    apply_post_finagle,
    cash_share_adjustment,
    check_request,
    prepare_scenario,
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
    assert "Balance Sheet Adjustments" not in section
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


def test_write_notebooks_saves_each_scenario_script(tmp_path):
    script = ROOT / "templates" / "run_collaborative.py"
    spec = importlib.util.spec_from_file_location("run_collaborative", script)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = {
        "version": "v02",
        "scenarios": {
            "base": {"notebook_code": "import finagle as cmp\nco.value()\n"},
            "bear": {"ok": False},
            "bull": {"notebook_code": "co.display_fin()"},
        },
    }
    written = module.write_notebooks(tmp_path, result)
    names = sorted(path.name for path in written)
    assert names == ["notebook_base_v02.py", "notebook_bull_v02.py"]
    assert (tmp_path / "notebook_base_v02.py").read_text(encoding="utf-8") == (
        "import finagle as cmp\nco.value()\n"
    )
    assert (tmp_path / "notebook_bull_v02.py").read_text(encoding="utf-8") == (
        "co.display_fin()\n"
    )
    assert not (tmp_path / "notebook_bear_v02.py").exists()


def test_existing_forecasts_still_validate():
    for path in sorted((ROOT / "forecasts").glob("*/forecast.json")):
        report = validate_payload(_load(path))
        assert report["ok"], (path.name, report["errors"])


def _market_case():
    return {
        "baseline": {"cash": {"value": 10.0, "source": "yahoo", "evidence": "cash"}},
        "market": {
            "shares": {"value": 5.0, "source": "yahoo", "evidence": "shares"},
            "price": {"value": 20.0, "source": "yahoo", "evidence": "price", "as_of": "2026-11-09"},
        },
        "rates": {"re": {"value": 0.10, "source": "assumption", "evidence": "cost of equity"}},
    }


def _fact(value):
    return {"value": value}


def _cash(amount=-10.0, when="2028-11-09", probability=0.5, name="milestone"):
    return {
        "kind": "cash",
        "name": name,
        "when": _fact(when),
        "probability": _fact(probability),
        "amount": _fact(amount),
    }


def _offering(shares=2.0, when="2026-11-09", probability=1, price=None, proceeds=None):
    item = {
        "kind": "equity",
        "name": "follow-on",
        "when": _fact(when),
        "probability": _fact(probability),
    }
    if shares is not None:
        item["shares"] = _fact(shares)
    if proceeds is not None:
        item["proceeds"] = _fact(proceeds)
    if price is not None:
        item["price"] = _fact(price)
    return item


def _with_schedule(items, scenario="base"):
    request = _synthetic()
    request["cash_share_adjustments"] = {scenario: items}
    return request


def _years(when):
    return (date.fromisoformat(when) - date(2026, 11, 9)).days / 365.25


def _close(left, right):
    assert math.isclose(left, right, rel_tol=1e-12, abs_tol=1e-12)


def test_cash_is_discounted_at_the_cost_of_equity():
    when = "2028-11-09"
    request = _with_schedule([_cash(when=when)])
    adjustment = cash_share_adjustment(request, "base", _market_case())
    years = max(0.0, _years(when))
    present = -10.0 * 0.5 / (1.10 ** years)
    record = adjustment["record"]
    assert record["applied"] is True
    _close(record["items"][0]["years"], years)
    _close(record["items"][0]["present_value"], present)
    _close(record["cash"], 10.0 + present)
    _close(adjustment["leaves"]["baseline"]["cash"]["value"], 10.0 + present)
    assert "shares" not in adjustment["leaves"].get("market", {})


def test_a_past_cash_date_is_not_discounted_further():
    request = _with_schedule([_cash(amount=-4.0, when="2026-01-01", probability=1)])
    record = cash_share_adjustment(request, "base", _market_case())["record"]
    _close(record["items"][0]["years"], 0.0)
    _close(record["items"][0]["discount"], 1.0)
    _close(record["cash"], 6.0)


def test_equity_is_issued_at_todays_price_unless_a_price_is_stated():
    today = cash_share_adjustment(_with_schedule([_offering()]), "base", _market_case())
    record = today["record"]
    _close(record["items"][0]["amount"], 40.0)
    _close(record["items"][0]["present_value"], 40.0)
    _close(record["new_shares"], 2.0)
    _close(record["cash"], 50.0)
    _close(record["shares"], 7.0)
    _close(today["leaves"]["market"]["shares"]["value"], 7.0)
    assert record["items"][0]["price"] == 20.0

    stated = cash_share_adjustment(
        _with_schedule([_offering(price=8.0)]), "base", _market_case()
    )["record"]
    _close(stated["items"][0]["amount"], 16.0)
    _close(stated["present_value"], 16.0)
    assert stated["items"][0]["price"] == 8.0

    both = cash_share_adjustment(
        _with_schedule([_offering(shares=1.0, proceeds=15.0, price=10.0)]),
        "base",
        _market_case(),
    )["record"]
    _close(both["items"][0]["present_value"], 15.0)
    _close(both["new_shares"], 1.0)
    assert both["items"][0]["price"] == 10.0


def test_a_prompt_opening_balance_is_adjusted_unless_it_already_includes_the_items():
    request = _with_schedule([_cash(amount=-4.0, when="2026-11-09", probability=1)])
    request["prompt_inputs"] = [
        {
            "path": "baseline.cash",
            "value": 50.0,
            "applies_to": ["base"],
            "quote": "use the filing cash",
            "date": "2026-11-09",
        },
        {
            "path": "market.shares",
            "value": 10.0,
            "applies_to": ["base"],
            "quote": "use the filing share count",
            "date": "2026-11-09",
        },
    ]
    updates = scenario_updates(request, "base")
    record = prepare_scenario(request, "base", _market_case(), updates)
    _close(record["opening_cash"], 50.0)
    _close(record["cash"], 46.0)
    _close(updates["leaves"]["baseline"]["cash"]["value"], 46.0)
    assert updates["leaves"]["baseline"]["cash"]["source"] == "article"

    request["prompt_inputs"][0]["includes_adjustments"] = True
    updates = scenario_updates(request, "base")
    record = prepare_scenario(request, "base", _market_case(), updates)
    assert record["cash_includes_adjustments"] is True
    _close(record["present_value"], -4.0)
    _close(record["cash"], 50.0)
    assert updates["leaves"]["baseline"]["cash"]["source"] == "prompt"
    _close(updates["leaves"]["baseline"]["cash"]["value"], 50.0)


def test_a_stated_cost_of_equity_and_price_replace_the_fetched_ones():
    when = "2027-11-09"
    request = _with_schedule([_cash(amount=-10.0, when=when, probability=1)])
    request["prompt_inputs"] = [
        {
            "path": "rates.re",
            "value": 0.20,
            "applies_to": ["base"],
            "quote": "use a 20 percent cost of equity",
            "date": "2026-11-09",
        }
    ]
    years = max(0.0, _years(when))
    record = cash_share_adjustment(request, "base", _market_case())["record"]
    _close(record["items"][0]["present_value"], -10.0 / (1.20 ** years))

    request = _with_schedule([_offering(shares=1.0)])
    request["prompt_inputs"] = [
        {
            "path": "market.price",
            "value": 30.0,
            "applies_to": ["base"],
            "quote": "use a 30 dollar price",
            "date": "2026-11-09",
        }
    ]
    record = cash_share_adjustment(request, "base", _market_case())["record"]
    _close(record["items"][0]["amount"], 30.0)
    assert record["price_date"] == "2026-11-09"


def test_an_empty_schedule_does_not_change_cash_or_shares():
    request = _with_schedule([])
    adjustment = cash_share_adjustment(request, "base", _market_case())
    assert adjustment["leaves"] == {}
    assert adjustment["record"]["applied"] is False
    _close(adjustment["record"]["cash"], 10.0)
    _close(adjustment["record"]["shares"], 5.0)
    assert cash_share_adjustment(_synthetic(), "base", _market_case()) is None


def test_a_missing_scenario_uses_the_base_list():
    request = _with_schedule([_cash(amount=-4.0, when="2026-11-09", probability=1)])
    bull = cash_share_adjustment(request, "bull", _market_case())["record"]
    assert bull["list_from"] == "base"
    _close(bull["cash"], 6.0)

    request["cash_share_adjustments"]["bull"] = []
    bull = cash_share_adjustment(request, "bull", _market_case())
    assert bull["record"]["list_from"] == "bull"
    assert bull["record"]["items"] == []
    assert bull["leaves"] == {}


def test_cash_share_schedule_must_match_the_forecast():
    request = _synthetic()
    forecast = _forecast_for(request)
    schedule = {"base": []}
    request["cash_share_adjustments"] = schedule
    forecast["cash_share_adjustments"] = {"base": []}
    assert check_request(request, forecast) == []
    forecast["cash_share_adjustments"] = {"base": [{"kind": "cash"}]}
    errors = check_request(request, forecast)
    assert any("cash_share_adjustments" in error for error in errors)
    del request["cash_share_adjustments"]
    errors = check_request(request, forecast)
    assert any("cash_share_adjustments" in error for error in errors)


def test_balance_sheet_adjustments_prints_the_result_not_a_recompute():
    request = _synthetic()
    result = _load(SAMPLES / "synthetic_min" / "result.json")
    result["scenarios"]["base"]["cash_share_adjustments"] = {
        "opening_cash": 10.0,
        "opening_shares": 5.0,
        "cash": 17.5,
        "shares": 6.0,
        "present_value": 7.5,
        "new_shares": 1.0,
        "items": [
            {
                "name": "milestone",
                "amount": 9.0,
                "when": "2028-06-30",
                "probability": 0.5,
                "discount": 0.8,
                "present_value": 7.5,
                "shares": 1.0,
            }
        ],
        "errors": [],
    }
    section = render_valuation_section(result, request)
    assert "### Balance Sheet Adjustments" in section
    assert "7.5000" in section
    assert "Year-0 cash 17.5000 equals opening 10.0 plus present value 7.5000." in section

    result["scenarios"]["base"]["cash_share_adjustments"] = {
        "items": [],
        "errors": [],
    }
    section = render_valuation_section(result, request)
    assert "No cash or share adjustments." in section
