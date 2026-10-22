"""Validate a forecast file.

Every numeric forecast figure is a fact: ``{"value", "tag", "citation"}``.
``citation`` has a non-empty ``text`` and a ``url``. Line items in dollar
periods sum to ``totals.revenue``. When a line has both ``H1A`` and ``H2E``,
they sum to ``FY26E``. Organic revenue and EBITDA compound through
``finagle.sales_growth`` and ``finagle.ebitda_growth``, and ``me`` is the
final explicit year's organic EBITDA margin.
"""

from __future__ import annotations

TAGS = {"A", "G", "E", "P", "S", "C"}
FINAGLE_LEAVES = ("ebitda_growth", "sales_growth", "me", "mc", "gsnext")
SUM_TOLERANCE = 0.02  # millions
# Growth rates live beside the dollar periods and must not be added across lines.
DOLLAR_PERIODS = {"FY24A", "FY25A", "H1A", "H2E", "FY26E", "FY27E"}


def validate_payload(payload):
    errors = []
    if not isinstance(payload, dict):
        return {"ok": False, "errors": ["forecast must be an object"]}
    if not payload.get("ticker"):
        errors.append("ticker is required")
    explicit = payload.get("explicit_periods")
    if not isinstance(explicit, list) or not explicit:
        errors.append("explicit_periods must be a non-empty list")
        explicit = []
    _walk_numbers(payload, errors)
    _check_block(payload, explicit, errors, prefix="")
    for name, scenario in (payload.get("scenarios") or {}).items():
        if isinstance(scenario, dict):
            _check_block(scenario, explicit, errors, prefix="scenarios.%s." % name)
    return {"ok": not errors, "errors": errors}


def _check_block(block, explicit, errors, prefix):
    lines = block.get("lines")
    totals = block.get("totals") or {}
    revenue = totals.get("revenue") or {}
    if not isinstance(lines, list) or not lines:
        if prefix == "":
            errors.append("lines must be a non-empty list")
        return
    periods = ["FY25A", *explicit] if "FY25A" in (lines[0].get("periods") or {}) else list(explicit)
    # Sum whichever dollar periods the totals actually publish.
    for period in revenue:
        if period not in DOLLAR_PERIODS:
            continue
        if not isinstance(revenue.get(period), dict):
            continue
        values = []
        for line in lines:
            fact = (line.get("periods") or {}).get(period)
            if not isinstance(fact, dict) or not isinstance(fact.get("value"), (int, float)):
                errors.append("%sline %s missing numeric %s" % (prefix, line.get("name"), period))
                continue
            values.append(fact["value"])
        total = revenue[period].get("value")
        if isinstance(total, (int, float)) and values:
            if abs(sum(values) - total) > SUM_TOLERANCE:
                errors.append(
                    "%s%s lines sum to %.4f, total is %.4f"
                    % (prefix, period, sum(values), total)
                )
    for line in lines:
        periods_map = line.get("periods") or {}
        h1 = periods_map.get("H1A")
        h2 = periods_map.get("H2E")
        fy26 = periods_map.get("FY26E")
        if isinstance(h1, dict) and isinstance(h2, dict) and isinstance(fy26, dict):
            a, b, c = h1.get("value"), h2.get("value"), fy26.get("value")
            if all(isinstance(x, (int, float)) for x in (a, b, c)):
                if abs(a + b - c) > SUM_TOLERANCE:
                    errors.append(
                        "%sline %s H1A+H2E %.4f != FY26E %.4f"
                        % (prefix, line.get("name"), a + b, c)
                    )
    organic = block.get("organic") or {}
    finagle = block.get("finagle") or {}
    if prefix == "" or finagle:
        _check_finagle(organic, finagle, explicit, errors, prefix)


def _check_finagle(organic, finagle, explicit, errors, prefix):
    if not isinstance(finagle, dict):
        errors.append("%sfinagle leaves are required" % prefix)
        return
    for name in FINAGLE_LEAVES:
        if name not in finagle:
            errors.append("%sfinagle.%s is required" % (prefix, name))
    growth = (finagle.get("ebitda_growth") or {}).get("value")
    sales = (finagle.get("sales_growth") or {}).get("value")
    if isinstance(growth, list) and isinstance(sales, list):
        if len(growth) != len(explicit) or len(sales) != len(explicit):
            errors.append(
                "%sfinagle growth lists must cover the explicit years (%d)"
                % (prefix, len(explicit))
            )
        _compounds(organic, "ebitda", growth, "ebitda_growth", errors, prefix)
        _compounds(organic, "revenue", sales, "sales_growth", errors, prefix)
        ebitda = organic.get("ebitda") or {}
        revenue = organic.get("revenue") or {}
        if explicit:
            last = explicit[-1]
            e_last = (ebitda.get(last) or {}).get("value")
            r_last = (revenue.get(last) or {}).get("value")
            me = (finagle.get("me") or {}).get("value")
            if all(isinstance(x, (int, float)) for x in (e_last, r_last, me)) and r_last:
                if abs(me - e_last / r_last) > 0.002:
                    errors.append(
                        "%sfinagle.me %.4f != final organic EBITDA/revenue %.4f"
                        % (prefix, me, e_last / r_last)
                    )
    me = (finagle.get("me") or {}).get("value")
    mc = (finagle.get("mc") or {}).get("value")
    if isinstance(me, (int, float)) and me == 0:
        errors.append("%sfinagle.me must be non-zero" % prefix)
    if isinstance(mc, (int, float)) and mc == 0:
        errors.append("%sfinagle.mc must be non-zero" % prefix)


def _compounds(organic, key, rates, label, errors, prefix):
    series = organic.get(key) or {}
    # Baseline is the period that is not an explicit forecast key.
    ordered = [name for name in ("FY25A", "FY26E", "FY27E", "FY28E") if name in series]
    values = []
    for name in ordered:
        value = (series.get(name) or {}).get("value")
        if isinstance(value, (int, float)):
            values.append(value)
    if len(values) != len(rates) + 1:
        return
    level = values[0]
    for index, rate in enumerate(rates):
        if not isinstance(rate, (int, float)):
            errors.append("%sfinagle.%s rate is not numeric" % (prefix, label))
            return
        level = level * (1.0 + rate)
        if abs(level - values[index + 1]) > SUM_TOLERANCE:
            errors.append(
                "%sfinagle.%s does not compound to %s (%.4f vs %.4f)"
                % (prefix, label, ordered[index + 1], level, values[index + 1])
            )


def _walk_numbers(obj, errors, in_fact=False, path="$"):
    if isinstance(obj, bool):
        return
    if isinstance(obj, dict) and _is_fact(obj):
        _check_fact(obj, errors, path)
        _walk_numbers(obj.get("value"), errors, in_fact=True, path=path + ".value")
        return
    if isinstance(obj, dict):
        for key, value in obj.items():
            _walk_numbers(value, errors, in_fact=False, path="%s.%s" % (path, key))
        return
    if isinstance(obj, list):
        if in_fact:
            for index, item in enumerate(obj):
                if isinstance(item, bool) or not isinstance(item, (int, float)):
                    errors.append("%s list values must be numbers" % path)
                _walk_numbers(item, errors, in_fact=True, path="%s[%d]" % (path, index))
            return
        for index, item in enumerate(obj):
            _walk_numbers(item, errors, in_fact=False, path="%s[%d]" % (path, index))
        return
    if isinstance(obj, (int, float)) and not in_fact:
        errors.append("%s is a number with no tag" % path)


def _is_fact(obj):
    return isinstance(obj, dict) and "value" in obj and ("tag" in obj or "citation" in obj)


def _check_fact(obj, errors, path):
    if obj.get("tag") not in TAGS:
        errors.append("%s tag must be one of %s" % (path, ", ".join(sorted(TAGS))))
    citation = obj.get("citation")
    if not isinstance(citation, dict):
        errors.append("%s is missing a citation" % path)
        return
    if not str(citation.get("text") or "").strip():
        errors.append("%s citation needs text that states the driver or the source" % path)
    url = str(citation.get("url") or "").strip()
    status = citation.get("url_status")
    if status == "unverified":
        if "unverified" not in str(citation.get("text")).lower():
            errors.append("%s unverified link must say 'link unverified' in the citation text" % path)
        return
    if not url:
        errors.append("%s citation needs a url" % path)
