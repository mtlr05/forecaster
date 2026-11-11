"""Checks and report text for a collaborative valuation.

The Finagle calls live in ``templates/run_collaborative.py``. This module
does not use the network.
"""

from __future__ import annotations

import math
from datetime import date, datetime

# Inputs Finagle determines, unless the user stated one and quoted it.
FINAGLE_DETERMINED = (
    "market.price",
    "market.shares",
    "rates.risk_free",
    "rates.re",
    "rates.gt",
)

# forecast.json ``finagle`` keys, and the request paths they match.
_FROM_FORECAST = {
    "sales_growth": "forecast.sales_growth",
    "ebitda_growth": "forecast.ebitda_growth",
    "me": "forecast.margin_path.me",
    "mc": "forecast.margin_path.mc",
    "gsnext": "forecast.margin_path.gsnext",
    "ebitda_basis": "forecast.ebitda_basis",
}

# Plain case fields. Finagle does not store these as leaves.
_PLAIN = {"year", "path", "ticker"}


def check_request(request, forecast=None):
    """Return a list of errors. An empty list means the request can run."""
    errors = []
    if not isinstance(request, dict):
        return ["request must be an object"]
    if request.get("mode") != "collaborative":
        errors.append("mode must be collaborative")
    scenarios = request.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        errors.append("scenarios must be a non-empty list")
        scenarios = []
    forecaster = request.get("forecaster")
    if not isinstance(forecaster, dict):
        errors.append("forecaster block is required")
        forecaster = {}
    for name in scenarios:
        block = forecaster.get(name)
        if not isinstance(block, dict):
            errors.append("forecaster.%s is missing" % name)
            continue
        for path, fact in block.items():
            if path in FINAGLE_DETERMINED:
                errors.append("%s belongs in prompt_inputs, with a quote" % path)
            if not _is_fact(fact):
                errors.append(
                    "forecaster.%s.%s needs value, tag, and evidence" % (name, path)
                )
    prompt = request.get("prompt_inputs", [])
    if not isinstance(prompt, list):
        errors.append("prompt_inputs must be a list")
        prompt = []
    for index, item in enumerate(prompt):
        if not isinstance(item, dict):
            errors.append("prompt_inputs[%d] must be an object" % index)
            continue
        if not item.get("path"):
            errors.append("prompt_inputs[%d] needs a path" % index)
        if "value" not in item:
            errors.append("prompt_inputs[%d] needs a value" % index)
        if not item.get("quote"):
            label = item.get("path") or ("prompt_inputs[%d]" % index)
            errors.append("%s needs a quote" % label)
        if not item.get("date"):
            label = item.get("path") or ("prompt_inputs[%d]" % index)
            errors.append("%s needs a date" % label)
    if forecast is not None:
        errors.extend(forecast_mismatches(request, forecast))
    return errors


def forecast_mismatches(request, forecast):
    """Value differences between the request and a forecast.json payload."""
    errors = []
    if not isinstance(forecast, dict):
        return ["forecast must be an object"]
    forecaster = request.get("forecaster") or {}
    if not isinstance(forecaster, dict):
        return errors
    for name, block in forecaster.items():
        if not isinstance(block, dict):
            continue
        expected = _forecast_leaves(forecast, name)
        if expected is None:
            errors.append("forecast has no finagle block for %s" % name)
            continue
        for path, fact in block.items():
            if not _is_fact(fact):
                continue
            if path not in expected:
                errors.append("forecaster.%s.%s is not in forecast.json" % (name, path))
                continue
            if not _same(fact["value"], expected[path]):
                errors.append("forecaster.%s.%s differs from forecast.json" % (name, path))
        for path in expected:
            if path not in block:
                errors.append("forecaster.%s is missing %s" % (name, path))
    errors.extend(_adjustment_mismatches(request, forecast))
    return errors


def scenario_updates(request, scenario):
    """Leaves to lay on a case, Forecaster first, then prompt inputs.

    ``plain`` holds fields Finagle stores as bare values, such as ``year``.
    ``leaves`` is a partial case of provenance leaves for ``update_case``.
    """
    leaves = {}
    plain = {}
    block = (request.get("forecaster") or {}).get(scenario) or {}
    if isinstance(block, dict):
        for path, fact in block.items():
            if _is_fact(fact):
                _place(leaves, plain, path, _leaf_from_fact(fact))
    for item in request.get("prompt_inputs") or []:
        if not isinstance(item, dict):
            continue
        applies = item.get("applies_to") or []
        if scenario not in applies or not item.get("path") or "value" not in item:
            continue
        quote = item.get("quote") or ""
        date = item.get("date") or ""
        evidence = quote if not date else "%s (%s)" % (quote, date)
        _place(
            leaves,
            plain,
            item["path"],
            {"value": item["value"], "source": "prompt", "evidence": evidence},
        )
    return {"leaves": leaves, "plain": plain}


def cash_share_adjustment(request, scenario, case):
    """Discount the schedule and build the year-0 cash and share leaves.

    Returns None when the request has no schedule. Otherwise ``leaves`` is the
    partial case to lay, empty when nothing changes, and ``record`` is the
    worked figures stored on the result.
    """
    if not isinstance(request, dict) or "cash_share_adjustments" not in request:
        return None
    openings = _openings(request, scenario, case)
    record = {
        "opening_cash": openings["opening_cash"],
        "opening_shares": openings["opening_shares"],
        "cost_of_equity": openings["cost_of_equity"],
        "price": openings["price"],
        "price_date": openings["price_date"],
        "cash_includes_adjustments": openings["cash_includes_adjustments"],
        "shares_includes_adjustments": openings["shares_includes_adjustments"],
        "present_value": 0.0,
        "new_shares": 0.0,
        "cash": openings["opening_cash"],
        "shares": openings["opening_shares"],
        "items": [],
        "applied": False,
        "errors": [],
        "list_from": None,
    }
    block = request.get("cash_share_adjustments")
    if not isinstance(block, dict):
        record["errors"].append("cash_share_adjustments must be an object")
        return {"leaves": {}, "record": record}
    items, list_from = _scenario_schedule(block, scenario)
    record["list_from"] = list_from
    if not isinstance(items, list):
        record["errors"].append("cash_share_adjustments has no list for %s" % scenario)
        return {"leaves": {}, "record": record}
    if not items:
        return {"leaves": {}, "record": record}

    errors = []
    if not _is_num(openings["cost_of_equity"]) or (1 + openings["cost_of_equity"]) <= 0:
        errors.append("cost of equity is missing")
    if _parse_date(openings["price_date"]) is None:
        errors.append("price date is missing")
    if not _is_num(openings["opening_cash"]):
        errors.append("year-0 cash is missing")
    if not _is_num(openings["opening_shares"]):
        errors.append("share count is missing")

    worked = []
    has_equity = False
    for index, item in enumerate(items):
        built, item_errors = _discount_item(item, openings, index)
        errors.extend(item_errors)
        if built:
            worked.append(built)
            if built["kind"] == "equity":
                has_equity = True
    record["items"] = worked
    if errors:
        record["errors"] = errors
        return {"leaves": {}, "record": record}

    present_value = sum(item["present_value"] for item in worked)
    new_shares = sum(item["shares"] for item in worked)
    cash = openings["opening_cash"]
    shares = openings["opening_shares"]
    if not openings["cash_includes_adjustments"]:
        cash = cash + present_value
    if not openings["shares_includes_adjustments"]:
        shares = shares + new_shares
    record["present_value"] = present_value
    record["new_shares"] = new_shares
    record["cash"] = cash
    record["shares"] = shares
    record["applied"] = True

    leaves = {}
    if not openings["cash_includes_adjustments"]:
        _place(leaves, {}, "baseline.cash", _cash_leaf(openings, present_value, cash))
    if has_equity and not openings["shares_includes_adjustments"]:
        _place(leaves, {}, "market.shares", _shares_leaf(openings, new_shares, shares))
    return {"leaves": leaves, "record": record}


def prepare_scenario(request, scenario, case, updates):
    """Lay adjustment leaves onto ``updates`` after the prompt leaves.

    Returns the worked record, or None when the request has no schedule.
    A stated year-0 cash or share count is the opening figure. The present
    value and the new shares are added unless that prompt says the stated
    figure already includes the adjustments.
    """
    adjustment = cash_share_adjustment(request, scenario, case)
    if adjustment and adjustment.get("leaves"):
        merge_leaves(updates.setdefault("leaves", {}), adjustment["leaves"])
    if adjustment is None:
        return None
    return adjustment["record"]


def merge_leaves(base, extra):
    """Overlay ``extra`` leaves onto a partial case. Later leaves win."""
    if not isinstance(extra, dict):
        return base
    for path in list(_walk(extra)):
        _place(base, {}, path, _lookup(extra, path))
    return base


def update_paths(updates):
    """Dotted paths that ``scenario_updates`` would lay on the case."""
    paths = list(updates.get("plain") or [])
    paths.extend(_walk(updates.get("leaves") or {}))
    return paths


def apply_post_finagle(value, request):
    """Raw value, and the adjusted value only when the request has a factor."""
    post = request.get("post_finagle") if isinstance(request, dict) else None
    if not post:
        return {"raw": value, "adjusted": None}
    factor = post.get("factor")
    adjusted = None
    if factor is not None and isinstance(value, (int, float)) and not isinstance(value, bool):
        adjusted = value * factor
    return {
        "raw": value,
        "adjusted": adjusted,
        "factor": factor,
        "label": post.get("label"),
        "quote": post.get("quote"),
        "date": post.get("date"),
    }


def render_valuation_section(result, request):
    """Markdown for the report. Numbers come from ``result`` and the request."""
    lines = ["## Valuation", ""]
    commit = (result or {}).get("finagle_commit")
    if commit:
        lines.append("Finagle commit `%s`." % commit)
        lines.append("")
    fetched = (result or {}).get("fetched") or {}
    if fetched:
        lines.append(
            "Fetched price %s on %s, risk-free rate %s on %s, shares %s (%s)."
            % (
                _fmt(fetched.get("price")),
                fetched.get("price_date"),
                _fmt(fetched.get("rf")),
                fetched.get("rf_date"),
                _fmt(fetched.get("shares")),
                fetched.get("shares_source"),
            )
        )
        lines.append("")
    scenarios = (result or {}).get("scenarios") or {}
    order = list((request or {}).get("scenarios") or scenarios.keys())
    for name in order:
        scenario = scenarios.get(name) or {}
        applied = apply_post_finagle(scenario.get("value_per_share"), request or {})
        lines.append("### %s" % name)
        lines.append("")
        lines.append("Value per share %s." % _fmt(applied["raw"]))
        if applied["adjusted"] is not None:
            post = (request or {}).get("post_finagle") or {}
            lines.append(
                "Adjusted value per share %s (%s %s) [P] %s."
                % (
                    _fmt(applied["adjusted"]),
                    post.get("label") or "factor",
                    _fmt(post.get("factor")),
                    post.get("date") or "",
                )
            )
            if post.get("quote"):
                lines.append(post["quote"])
        for flag in scenario.get("sanity_flags") or []:
            lines.append("Flag: %s" % flag)
        validation = scenario.get("validation") or {}
        for warning in validation.get("warnings") or []:
            lines.append("Warning: %s" % warning)
        filled = scenario.get("defaults_filled") or []
        if filled:
            lines.append("Defaults filled: %s." % ", ".join(filled))
        lines.append("")
    lines.extend(_render_balance_sheet(result, order))
    lines.append("### Prompt inputs")
    lines.append("")
    items = (request or {}).get("prompt_inputs") or []
    if not items:
        lines.append("None.")
    for item in items:
        lines.append(
            "- `%s` = %s [P] %s. %s"
            % (item.get("path"), _fmt(item.get("value")), item.get("date"), item.get("quote"))
        )
    return "\n".join(lines).rstrip() + "\n"


def _adjustment_mismatches(request, forecast):
    if not isinstance(forecast, dict):
        return []
    left_missing = "cash_share_adjustments" not in request
    right_missing = "cash_share_adjustments" not in forecast
    if left_missing and right_missing:
        return []
    left = request.get("cash_share_adjustments")
    right = forecast.get("cash_share_adjustments")
    if left_missing or right_missing or not _equal(left, right):
        return ["cash_share_adjustments differs from forecast.json"]
    return []


def _scenario_schedule(block, scenario):
    if scenario in block:
        return block[scenario], scenario
    if "base" in block:
        return block["base"], "base"
    return None, None


def _openings(request, scenario, case):
    cash_leaf = _case_leaf(case, ("baseline", "cash"))
    shares_leaf = _case_leaf(case, ("market", "shares"))
    price_leaf = _case_leaf(case, ("market", "price"))
    re_leaf = _case_leaf(case, ("rates", "re"))
    openings = {
        "opening_cash": cash_leaf.get("value") if isinstance(cash_leaf, dict) else None,
        "opening_shares": shares_leaf.get("value") if isinstance(shares_leaf, dict) else None,
        "price": price_leaf.get("value") if isinstance(price_leaf, dict) else None,
        "price_date": price_leaf.get("as_of") if isinstance(price_leaf, dict) else None,
        "cost_of_equity": re_leaf.get("value") if isinstance(re_leaf, dict) else None,
        "cash_includes_adjustments": False,
        "shares_includes_adjustments": False,
    }
    for item in (request or {}).get("prompt_inputs") or []:
        if not isinstance(item, dict):
            continue
        if scenario not in (item.get("applies_to") or []):
            continue
        if "value" not in item:
            continue
        path = item.get("path")
        if path == "baseline.cash":
            openings["opening_cash"] = item["value"]
            openings["cash_includes_adjustments"] = bool(item.get("includes_adjustments"))
        elif path == "market.shares":
            openings["opening_shares"] = item["value"]
            openings["shares_includes_adjustments"] = bool(item.get("includes_adjustments"))
        elif path == "market.price":
            openings["price"] = item["value"]
            openings["price_date"] = item.get("date") or openings["price_date"]
        elif path == "rates.re":
            openings["cost_of_equity"] = item["value"]
    return openings


def _discount_item(item, openings, index):
    label = "adjustment %d" % (index + 1)
    if not isinstance(item, dict):
        return None, ["%s must be an object" % label]
    name = item.get("name")
    if isinstance(name, str) and name.strip():
        label = name.strip()
    kind = item.get("kind")
    if kind not in ("cash", "equity"):
        return None, ["%s kind must be cash or equity" % label]
    when = _fact_value(item.get("when"))
    years = _years_between(openings.get("price_date"), when)
    probability = _fact_value(item.get("probability"))
    errors = []
    if years is None:
        errors.append("%s needs an ISO date" % label)
    if not _is_num(probability) or not 0 <= probability <= 1:
        errors.append("%s probability must be from 0 to 1" % label)
    re = openings.get("cost_of_equity")
    discount = None
    if years is not None and _is_num(re) and (1 + re) > 0:
        discount = 1.0 / (1.0 + re) ** years
    elif years is not None:
        errors.append("%s could not be discounted" % label)
    if kind == "cash":
        amount = _fact_value(item.get("amount"))
        if not _is_num(amount):
            errors.append("%s amount must be a number" % label)
        if errors or discount is None:
            return None, errors
        return {
            "name": label,
            "kind": "cash",
            "amount": amount,
            "when": when,
            "probability": probability,
            "years": years,
            "discount": discount,
            "present_value": amount * probability * discount,
            "shares": 0.0,
            "price": None,
        }, []
    shares, proceeds, price, price_errors = _equity_terms(item, openings, label)
    errors.extend(price_errors)
    if errors or discount is None or shares is None or proceeds is None:
        return None, errors
    return {
        "name": label,
        "kind": "equity",
        "amount": proceeds,
        "when": when,
        "probability": probability,
        "years": years,
        "discount": discount,
        "present_value": proceeds * probability * discount,
        "shares": shares * probability,
        "price": price,
    }, []


def _equity_terms(item, openings, label):
    """Stated shares and proceeds, or the missing one at the issue price."""
    errors = []
    stated_shares = "shares" in item
    stated_proceeds = "proceeds" in item
    shares = _fact_value(item.get("shares")) if stated_shares else None
    proceeds = _fact_value(item.get("proceeds")) if stated_proceeds else None
    stated_price = _fact_value(item.get("price")) if "price" in item else None
    if not stated_shares and not stated_proceeds:
        return None, None, None, ["%s needs shares or proceeds" % label]
    if stated_shares and (not _is_num(shares) or shares <= 0):
        errors.append("%s shares must be a positive number" % label)
    if stated_proceeds and (not _is_num(proceeds) or proceeds <= 0):
        errors.append("%s proceeds must be a positive number" % label)
    if "price" in item and (not _is_num(stated_price) or stated_price <= 0):
        errors.append("%s price must be a positive number" % label)
    if errors:
        return None, None, None, errors
    if stated_price is not None:
        price = stated_price
    elif stated_shares and stated_proceeds:
        price = proceeds / shares
    else:
        price = openings.get("price")
    if not _is_num(price) or price <= 0:
        return None, None, None, ["%s needs today's price" % label]
    if not stated_shares:
        shares = proceeds / price
    if not stated_proceeds:
        proceeds = shares * price
    return shares, proceeds, price, []


def _cash_leaf(openings, present_value, cash):
    return {
        "value": cash,
        "source": "article",
        "evidence": (
            "year-0 cash %.6g plus present value %.6g of cash and share adjustments, "
            "discounted at the cost of equity %.6g"
            % (openings["opening_cash"], present_value, openings["cost_of_equity"])
        ),
    }


def _shares_leaf(openings, new_shares, shares):
    price = openings.get("price")
    price_text = "unstated" if not _is_num(price) else "%.6g" % price
    return {
        "value": shares,
        "source": "article",
        "evidence": (
            "share count %.6g plus %.6g shares from equity offerings; "
            "issued at today's price %s unless a price was stated"
            % (openings["opening_shares"], new_shares, price_text)
        ),
    }


def _render_balance_sheet(result, order):
    scenarios = (result or {}).get("scenarios") or {}
    names = list(order or [])
    for name in scenarios:
        if name not in names:
            names.append(name)
    found = []
    for name in names:
        scenario = scenarios.get(name)
        if not isinstance(scenario, dict):
            continue
        record = scenario.get("cash_share_adjustments")
        if isinstance(record, dict):
            found.append((name, record))
    if not found:
        return []
    lines = ["### Balance Sheet Adjustments", ""]
    for name, record in found:
        lines.extend(_balance_lines(name, record))
        lines.append("")
    return lines


def _balance_lines(name, record):
    title = name[:1].upper() + name[1:]
    errors = record.get("errors") or []
    if errors:
        return ["%s. Adjustments were not applied. %s" % (title, "; ".join(errors))]
    items = record.get("items") or []
    if not items:
        return ["%s. No cash or share adjustments." % title]
    lines = [_balance_sentence(record), ""]
    lines.append("| Item | Amount | When | Probability | Discount | Present value | Shares |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for item in items:
        lines.append(
            "| %s | %s | %s | %s | %s | %s | %s |"
            % (
                item.get("name"),
                _fmt(item.get("amount")),
                item.get("when"),
                _fmt(item.get("probability")),
                _fmt(item.get("discount")),
                _fmt(item.get("present_value")),
                _fmt(item.get("shares")),
            )
        )
    return lines


def _balance_sentence(record):
    if record.get("cash_includes_adjustments"):
        cash = "Year-0 cash %s is the stated balance and already includes these items." % _fmt(
            record.get("cash")
        )
    else:
        cash = (
            "Year-0 cash %s equals opening %s plus present value %s."
            % (_fmt(record.get("cash")), _fmt(record.get("opening_cash")), _fmt(record.get("present_value")))
        )
    if record.get("shares_includes_adjustments"):
        shares = " Share count %s is the stated count and already includes these items." % _fmt(
            record.get("shares")
        )
    else:
        shares = " Share count %s equals opening %s plus %s shares." % (
            _fmt(record.get("shares")),
            _fmt(record.get("opening_shares")),
            _fmt(record.get("new_shares")),
        )
    return cash + shares


def _case_leaf(case, parts):
    cursor = case if isinstance(case, dict) else {}
    for part in parts:
        if not isinstance(cursor, dict):
            return {}
        cursor = cursor.get(part)
    return cursor if isinstance(cursor, dict) else {}


def _fact_value(fact):
    if isinstance(fact, dict) and "value" in fact:
        return fact.get("value")
    return None


def _years_between(price_date, when):
    start = _parse_date(price_date)
    end = _parse_date(when)
    if start is None or end is None:
        return None
    return max(0.0, (end - start).days / 365.25)


def _parse_date(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    text = str(value or "").strip()
    if len(text) >= 10:
        text = text[:10]
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        return None


def _is_num(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _lookup(node, path):
    cursor = node
    for part in path.split("."):
        cursor = cursor[part]
    return cursor


def _equal(left, right):
    if isinstance(left, dict) and isinstance(right, dict):
        return set(left) == set(right) and all(_equal(left[key], right[key]) for key in left)
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(_equal(a, b) for a, b in zip(left, right))
    return _same(left, right)


def _is_fact(fact):
    return (
        isinstance(fact, dict)
        and "value" in fact
        and fact.get("tag")
        and fact.get("evidence")
    )


def _leaf_from_fact(fact):
    evidence = fact.get("evidence") or ""
    cite = fact.get("cite_id")
    if cite:
        evidence = "%s [%s]" % (evidence, cite)
    source = "prompt" if fact.get("tag") == "P" else "article"
    return {"value": fact["value"], "source": source, "evidence": evidence}


def _place(leaves, plain, path, node):
    if path in _PLAIN:
        plain[path] = node["value"]
        return
    cursor = leaves
    parts = path.split(".")
    for part in parts[:-1]:
        current = cursor.get(part)
        if not isinstance(current, dict) or _is_leaf(current):
            current = {}
            cursor[part] = current
        cursor = current
    cursor[parts[-1]] = node


def _is_leaf(node):
    return isinstance(node, dict) and "value" in node and "source" in node and "evidence" in node


def _walk(node, prefix=""):
    if _is_leaf(node):
        if prefix:
            yield prefix
        return
    if isinstance(node, dict):
        for key, child in node.items():
            path = "%s.%s" % (prefix, key) if prefix else key
            yield from _walk(child, path)


def _forecast_leaves(forecast, scenario):
    block = _finagle_block(forecast, scenario)
    if block is None:
        return None
    found = {}
    for key, dotted in _FROM_FORECAST.items():
        if key in block:
            found[dotted] = _unwrap(block[key])
    disclosure = block.get("acquisition_disclosure")
    if isinstance(disclosure, dict) and "status" in disclosure:
        found["forecast.acquisition_disclosure.status"] = _unwrap(disclosure["status"])
    return found


def _finagle_block(forecast, scenario):
    if scenario == "base" and isinstance(forecast.get("finagle"), dict):
        return forecast["finagle"]
    node = (forecast.get("scenarios") or {}).get(scenario)
    if isinstance(node, dict) and isinstance(node.get("finagle"), dict):
        return node["finagle"]
    return None


def _unwrap(node):
    if isinstance(node, dict) and "value" in node:
        return node["value"]
    return node


def _same(left, right):
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(_same(a, b) for a, b in zip(left, right))
    if (
        isinstance(left, (int, float))
        and isinstance(right, (int, float))
        and not isinstance(left, bool)
        and not isinstance(right, bool)
    ):
        return math.isclose(float(left), float(right), rel_tol=1e-9, abs_tol=1e-9)
    return left == right


def _fmt(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, float) and not math.isfinite(value):
        return str(value)
    if float(value) == int(value) and abs(value) < 1e12:
        return "%.1f" % value
    return "%.4f" % float(value)
