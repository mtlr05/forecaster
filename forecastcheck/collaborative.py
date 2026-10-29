"""Checks and report text for a collaborative valuation.

The Finagle calls live in ``templates/run_collaborative.py``. This module
does not use the network.
"""

from __future__ import annotations

import math

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
