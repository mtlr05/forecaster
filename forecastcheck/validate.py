"""Validate a forecast file.

Every numeric forecast figure is a fact: ``{"value", "tag", "citation"}``.
``citation`` has a non-empty ``text`` and a ``url``. Line items in every
dollar period sum to ``totals.revenue``. Part-year periods on a line (H1A +
H2E, 9MA + Q4E, Q1A..Q4E) sum to their fiscal year, taken from ``stub_of``
or, when that is absent, the first explicit period. Organic revenue and
EBITDA compound from ``baseline_period`` through ``explicit_periods`` via
``finagle.sales_growth`` and ``finagle.ebitda_growth``, and ``me`` is the
final explicit year's organic EBITDA margin. The Finagle leaves are required
unless the case sets ``finagle_handoff: false``.

When the case has a ``sources`` list, every citation also carries an ``id``
(A1, G1, E1, S1, C1, P1, D1) and a ``page`` (or ``page_status:
"unverified"``). Each ID names one fact, resolves in ``sources``, and C
entries list ``inputs`` that are existing IDs. A/G/E entries carry their
quoted ``text``. Without a ``sources`` list the case passes with a warning.

When the case has a ``views`` block, each explicit year records bottom-up,
top-down, calibrated top-down, and Consensus for revenue and EBITDA, and the
ratios of those views. ``views.used`` names the base for each metric, or one
name shared by both, and that view matches ``totals``. A missing view or a
missing ratio is ``{"absent": "<reason>"}``. A Consensus fact with one analyst
or no ``as_of`` date passes with a warning. Without a ``views`` block the case
passes with a warning.

When the case has a ``cash_share_adjustments`` block, ``base`` is a list of
cash and equity items. Each item has a name, an ISO date, and a probability.
A cash item has a signed amount. An equity item has shares, proceeds, or both,
and an optional issue price. Without the block the case passes with a warning.
"""

from __future__ import annotations

import re
from datetime import datetime

TAGS = {"A", "G", "E", "P", "S", "C"}
FINAGLE_LEAVES = ("ebitda_growth", "sales_growth", "me", "mc", "gsnext")
SUM_TOLERANCE = 0.02  # millions
# Period keys are derived from their names, not a fixed list.
FISCAL_YEAR = re.compile(r"^FY\d{2}[AE]$")
PART_YEAR = re.compile(r"^(H[12]|Q[1-4]|9M)[AE]$")
# A lone reference quarter (e.g. the latest quarter, Q4FY26A). Summed across
# lines like any dollar period, but never required to make up a full year.
REFERENCE_QUARTER = re.compile(r"^Q[1-4]FY\d{2}[AE]$")
# Growth rates live beside the dollar periods and must not be added across lines.
NON_DOLLAR_KEYS = {"YoY"}
NON_DOLLAR_PREFIXES = ("YoY_",)  # e.g. YoY_FY26, YoY_Q4
# Part-year groups that make up one fiscal year.
STUB_GROUPS = (("H1", "H2"), ("9M", "Q4"), ("Q1", "Q2", "Q3", "Q4"))
PATTERNS = {
    "ramping",
    "new or acquired",
    "mature or declining",
    "milestone-dependent",
    "acquisition-driven",
    "recurring",
}
VIEW_NAMES = ("bottom_up", "top_down", "calibrated_top_down", "consensus")
POINT_VIEWS = ("bottom_up", "calibrated_top_down", "consensus")
RATIO_SPECS = (
    ("bottom_up_over_base", "bottom_up", "base"),
    ("top_down_over_base", "top_down", "base"),
    ("calibrated_top_down_over_base", "calibrated_top_down", "base"),
    ("consensus_over_base", "consensus", "base"),
    ("bottom_up_over_calibrated_top_down", "bottom_up", "calibrated_top_down"),
    ("bottom_up_over_consensus", "bottom_up", "consensus"),
)
RATIO_TOLERANCE = 0.0005


def _is_dollar_period(key):
    return bool(FISCAL_YEAR.match(key) or PART_YEAR.match(key) or REFERENCE_QUARTER.match(key))


def _is_non_dollar_key(key):
    return key in NON_DOLLAR_KEYS or key.startswith(NON_DOLLAR_PREFIXES)


def validate_payload(payload):
    errors = []
    warnings = []
    if not isinstance(payload, dict):
        return {"ok": False, "errors": ["forecast must be an object"], "warnings": []}
    if not payload.get("ticker"):
        errors.append("ticker is required")
    explicit = payload.get("explicit_periods")
    if not isinstance(explicit, list) or not explicit:
        errors.append("explicit_periods must be a non-empty list")
        explicit = []
    for period in explicit:
        if not isinstance(period, str) or not FISCAL_YEAR.match(period):
            errors.append("explicit period %r is not a fiscal year (FYyyE)" % (period,))
    baseline = payload.get("baseline_period")
    if not isinstance(baseline, str) or not FISCAL_YEAR.match(baseline):
        errors.append("baseline_period must be a fiscal year (FYyyA), got %r" % (baseline,))
        baseline = None
    stub_of = payload.get("stub_of") or {}
    if not isinstance(stub_of, dict):
        errors.append("stub_of must map part-year periods to a fiscal year")
        stub_of = {}
    handoff = payload.get("finagle_handoff", True) is not False
    ctx = {"explicit": explicit, "baseline": baseline, "stub_of": stub_of, "handoff": handoff}
    _walk_numbers({k: v for k, v in payload.items() if k != "sources"}, errors)
    if "sources" in payload:
        _check_ids(payload, errors)
    else:
        warnings.append("no sources block: numbered citation IDs and a sources list are expected for new cases")
    if "views" in payload:
        _check_views(payload, explicit, errors, warnings)
    else:
        warnings.append(
            "no views block: bottom-up, top-down, calibrated top-down, and Consensus are expected for new cases"
        )
    if "cash_share_adjustments" in payload:
        _check_cash_share_adjustments(payload.get("cash_share_adjustments"), errors)
    else:
        warnings.append(
            "no cash_share_adjustments block: milestone payments, contingent cash, and equity offerings are expected for new cases"
        )
    _check_block(payload, ctx, errors, prefix="")
    for name, scenario in (payload.get("scenarios") or {}).items():
        if isinstance(scenario, dict):
            _check_block(scenario, ctx, errors, prefix="scenarios.%s." % name)
    return {"ok": not errors, "errors": errors, "warnings": warnings}


def _check_block(block, ctx, errors, prefix):
    explicit = ctx["explicit"]
    lines = block.get("lines")
    totals = block.get("totals") or {}
    revenue = totals.get("revenue") or {}
    if not isinstance(lines, list) or not lines:
        if prefix == "":
            errors.append("lines must be a non-empty list")
        return
    _check_period_keys(lines, totals, errors, prefix)
    # Sum every dollar period the totals publish.
    for period in revenue:
        if not _is_dollar_period(period):
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
        _check_stubs(line, ctx, errors, prefix)
        pattern = line.get("pattern")
        # A trailing parenthetical note is allowed: "ramping (share gain abroad)".
        if pattern is not None and re.sub(r"\s*\(.*\)\s*$", "", str(pattern)).strip().lower() not in PATTERNS:
            errors.append(
                "%sline %s pattern %r is not one of: %s"
                % (prefix, line.get("name"), pattern, ", ".join(sorted(PATTERNS)))
            )
    organic = block.get("organic") or {}
    finagle = block.get("finagle") or {}
    if (prefix == "" and ctx["handoff"]) or finagle:
        _check_finagle(organic, finagle, ctx, errors, prefix)


def _check_period_keys(lines, totals, errors, prefix):
    maps = [("line %s" % line.get("name"), line.get("periods") or {}) for line in lines]
    maps += [("totals.%s" % key, value) for key, value in totals.items() if isinstance(value, dict)]
    for label, periods_map in maps:
        for key in periods_map:
            if _is_non_dollar_key(key) or _is_dollar_period(key):
                continue
            errors.append("%s%s has unrecognized period %r" % (prefix, label, key))


def _check_stubs(line, ctx, errors, prefix):
    periods_map = line.get("periods") or {}
    parts = [key for key in periods_map if PART_YEAR.match(key)]
    if not parts:
        return
    default = ctx["explicit"][0] if ctx["explicit"] else None
    by_year = {}
    for key in parts:
        year = ctx["stub_of"].get(key, default)
        if not year:
            errors.append("%sline %s %s has no fiscal year in stub_of" % (prefix, line.get("name"), key))
            continue
        by_year.setdefault(year, []).append(key)
    for year, keys in by_year.items():
        stems = {key[:-1] for key in keys}
        group = next((g for g in STUB_GROUPS if stems == set(g)), None)
        if group is None:
            errors.append(
                "%sline %s part-year periods %s do not form a full %s"
                % (prefix, line.get("name"), "+".join(sorted(keys)), year)
            )
            continue
        target = (periods_map.get(year) or {}).get("value") if isinstance(periods_map.get(year), dict) else None
        values = [(periods_map.get(key) or {}).get("value") for key in keys]
        if not isinstance(target, (int, float)):
            errors.append("%sline %s has %s but no numeric %s" % (prefix, line.get("name"), "+".join(keys), year))
            continue
        if not all(isinstance(x, (int, float)) for x in values):
            continue
        ordered = sorted(keys, key=lambda k: group.index(k[:-1]))
        if abs(sum(values) - target) > SUM_TOLERANCE:
            errors.append(
                "%sline %s %s %.4f != %s %.4f"
                % (prefix, line.get("name"), "+".join(ordered), sum(values), year, target)
            )


def _check_finagle(organic, finagle, ctx, errors, prefix):
    explicit = ctx["explicit"]
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
        _compounds(organic, "ebitda", growth, "ebitda_growth", ctx, errors, prefix)
        _compounds(organic, "revenue", sales, "sales_growth", ctx, errors, prefix)
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


def _compounds(organic, key, rates, label, ctx, errors, prefix):
    series = organic.get(key) or {}
    if ctx["baseline"] is None:
        return  # already reported as an error
    ordered = [ctx["baseline"], *ctx["explicit"]]
    values = []
    for name in ordered:
        value = (series.get(name) or {}).get("value")
        if not isinstance(value, (int, float)):
            errors.append("%sorganic.%s missing numeric %s for compounding" % (prefix, key, name))
            return
        values.append(value)
    if len(values) != len(rates) + 1:
        errors.append(
            "%sfinagle.%s has %d rates but organic.%s has %d periods after %s"
            % (prefix, label, len(rates), key, len(values) - 1, ctx["baseline"])
        )
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


def _is_absent(obj):
    return isinstance(obj, dict) and set(obj.keys()) == {"absent"}


def _absent_reason(obj):
    return str(obj.get("absent") or "").strip()


def _fact_value(obj):
    if not isinstance(obj, dict) or "tag" not in obj:
        return None
    value = obj.get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return value


def _read_point(obj, path, errors):
    if _is_absent(obj):
        if not _absent_reason(obj):
            errors.append("%s absent needs a reason" % path)
        return None
    if isinstance(obj, dict) and "absent" in obj:
        errors.append("%s cannot be both a fact and absent" % path)
        return None
    value = _fact_value(obj)
    if value is None:
        errors.append('%s must be a fact or {"absent": "..."}' % path)
        return None
    return value


def _read_top_down(obj, path, errors):
    """Return the ratio numerator (midpoint, else point) and the base point."""
    if _is_absent(obj):
        if not _absent_reason(obj):
            errors.append("%s absent needs a reason" % path)
        return None, None
    if not isinstance(obj, dict) or "absent" in obj:
        errors.append("%s must be a range, a point, or absent" % path)
        return None, None
    extra = set(obj) - {"low", "high", "point"}
    if extra:
        errors.append("%s has unexpected keys %s" % (path, ", ".join(sorted(extra))))
    has_low = "low" in obj
    has_high = "high" in obj
    has_point = "point" in obj
    low = _fact_value(obj.get("low")) if has_low else None
    high = _fact_value(obj.get("high")) if has_high else None
    point = _fact_value(obj.get("point")) if has_point else None
    if has_low or has_high:
        if not has_low or not has_high or low is None or high is None:
            errors.append("%s range needs numeric low and high" % path)
            midpoint = None
        else:
            midpoint = (low + high) / 2.0
    else:
        midpoint = None
    if has_point and point is None:
        errors.append("%s point must be a fact" % path)
    if midpoint is None and point is None:
        if not (has_low or has_high or has_point):
            errors.append("%s must be a range, a point, or absent" % path)
        return None, None
    return (midpoint if midpoint is not None else point), point


def _expect_ratio(obj, numerator, denominator, path, errors):
    can_divide = (
        isinstance(numerator, (int, float))
        and not isinstance(numerator, bool)
        and isinstance(denominator, (int, float))
        and not isinstance(denominator, bool)
        and denominator != 0
    )
    if _is_absent(obj):
        if not _absent_reason(obj):
            errors.append("%s absent needs a reason" % path)
        if can_divide:
            errors.append("%s is absent but both inputs exist" % path)
        return
    value = _fact_value(obj)
    if value is None:
        errors.append('%s must be a fact or {"absent": "..."}' % path)
        return
    if not can_divide:
        errors.append("%s is a fact but a numerator or denominator is missing" % path)
        return
    expected = numerator / float(denominator)
    if abs(value - expected) > RATIO_TOLERANCE:
        errors.append("%s %.4f != %.4f" % (path, value, expected))


def _resolve_used(used, errors):
    """Map each metric to its base view. A string applies to both."""
    if isinstance(used, str):
        if used not in VIEW_NAMES:
            errors.append("views.used must be one of %s" % ", ".join(VIEW_NAMES))
            return {"revenue": None, "ebitda": None}
        return {"revenue": used, "ebitda": used}
    if isinstance(used, dict):
        extra = set(used) - {"revenue", "ebitda"}
        if extra:
            errors.append("views.used has unexpected keys %s" % ", ".join(sorted(extra)))
        resolved = {}
        for metric in ("revenue", "ebitda"):
            name = used.get(metric)
            if name not in VIEW_NAMES:
                errors.append(
                    "views.used.%s must be one of %s" % (metric, ", ".join(VIEW_NAMES))
                )
                resolved[metric] = None
            else:
                resolved[metric] = name
        return resolved
    errors.append('views.used must be a view name or {"revenue", "ebitda"}')
    return {"revenue": None, "ebitda": None}


def _flag_consensus(fact, path, warnings):
    if not isinstance(fact, dict) or _is_absent(fact) or "value" not in fact:
        return
    analysts = fact.get("analysts")
    if isinstance(analysts, bool) or not isinstance(analysts, int):
        warnings.append("%s consensus analyst count is not recorded" % path)
    elif analysts == 1:
        warnings.append("%s consensus is a single analyst" % path)
    as_of = fact.get("as_of")
    if not isinstance(as_of, str) or not as_of.strip():
        warnings.append("%s consensus is undated" % path)


def _check_views(payload, explicit, errors, warnings):
    views = payload.get("views")
    if not isinstance(views, dict):
        errors.append("views must be an object")
        return
    used_by = _resolve_used(views.get("used"), errors)
    ratios_root = views.get("ratios")
    if not isinstance(ratios_root, dict):
        errors.append("views.ratios must be an object")
        ratios_root = {}
    years = [period for period in explicit if isinstance(period, str) and FISCAL_YEAR.match(period)]
    totals = payload.get("totals") or {}
    announced_ratio_years = set()
    for metric in ("revenue", "ebitda"):
        used = used_by[metric]
        series = views.get(metric)
        if not isinstance(series, dict):
            errors.append("views.%s must be an object of explicit years" % metric)
            series = {}
        for year in years:
            path = "views.%s.%s" % (metric, year)
            slot = series.get(year)
            if not isinstance(slot, dict):
                errors.append("%s must hold the four views" % path)
                continue
            points = {}
            for name in POINT_VIEWS:
                if name not in slot:
                    errors.append("%s.%s is required" % (path, name))
                    continue
                points[name] = _read_point(slot[name], "%s.%s" % (path, name), errors)
                if name == "consensus":
                    _flag_consensus(slot[name], "%s.consensus" % path, warnings)
            if "top_down" not in slot:
                errors.append("%s.top_down is required" % path)
                top_numerator, top_point = None, None
            else:
                top_numerator, top_point = _read_top_down(slot["top_down"], "%s.top_down" % path, errors)
            points["top_down"] = top_numerator
            total = ((totals.get(metric) or {}).get(year) or {})
            total_value = total.get("value") if isinstance(total, dict) else None
            if isinstance(total_value, bool):
                total_value = None
            used_value = None
            if used == "top_down":
                used_value = top_point
                if used_value is None and _is_absent(slot.get("top_down")):
                    errors.append("%s top_down is the base but is absent" % path)
                elif used_value is None and "top_down" in slot and not _is_absent(slot.get("top_down")):
                    errors.append("%s top_down is the base but no point is recorded" % path)
            elif used in points or (used in POINT_VIEWS and used in slot):
                used_value = points.get(used)
                if used_value is None and _is_absent(slot.get(used)):
                    errors.append("%s %s is the base but is absent" % (path, used))
            if isinstance(used_value, (int, float)) and isinstance(total_value, (int, float)):
                if abs(used_value - total_value) > SUM_TOLERANCE:
                    errors.append(
                        "%s %s %.4f does not match totals.%s %.4f"
                        % (path, used, used_value, metric, total_value)
                    )
            elif isinstance(used_value, (int, float)):
                errors.append("%s %s has no totals.%s to match" % (path, used, metric))
            year_ratios = ratios_root.get(year)
            ratio_path = "views.ratios.%s.%s" % (year, metric)
            if not isinstance(year_ratios, dict):
                if year not in announced_ratio_years:
                    errors.append("views.ratios.%s must hold revenue and ebitda" % year)
                    announced_ratio_years.add(year)
                continue
            block = year_ratios.get(metric)
            if not isinstance(block, dict):
                errors.append("%s must hold the six ratios" % ratio_path)
                continue
            for key, numerator_name, denominator_name in RATIO_SPECS:
                if key not in block:
                    errors.append("%s.%s is required" % (ratio_path, key))
                    continue
                numerator = points.get(numerator_name)
                denominator = total_value if denominator_name == "base" else points.get(denominator_name)
                _expect_ratio(block[key], numerator, denominator, "%s.%s" % (ratio_path, key), errors)


def _check_cash_share_adjustments(block, errors):
    if not isinstance(block, dict):
        errors.append("cash_share_adjustments must be an object of scenarios")
        return
    if "base" not in block:
        errors.append("cash_share_adjustments.base is required")
    for name, items in block.items():
        path = "cash_share_adjustments.%s" % name
        if not isinstance(items, list):
            errors.append("%s must be a list" % path)
            continue
        for index, item in enumerate(items):
            _check_adjustment(item, "%s[%d]" % (path, index), errors)


def _check_adjustment(item, path, errors):
    if not isinstance(item, dict):
        errors.append("%s must be an object" % path)
        return
    kind = item.get("kind")
    if kind not in ("cash", "equity"):
        errors.append("%s kind must be cash or equity" % path)
    name = item.get("name")
    if not isinstance(name, str) or not name.strip():
        errors.append("%s needs a name" % path)
    when = item.get("when")
    when_value = when.get("value") if isinstance(when, dict) else None
    if not _is_fact(when) or not _is_iso_date(when_value):
        errors.append("%s when must be a fact with an ISO date" % path)
    probability = _number_fact(item.get("probability"))
    if probability is None or not 0 <= probability <= 1:
        errors.append("%s probability must be a fact from 0 to 1" % path)
    if kind == "cash":
        extra = sorted(set(item) - {"kind", "name", "when", "probability", "amount"})
        if extra:
            errors.append("%s cash item has unexpected %s" % (path, ", ".join(extra)))
        if _number_fact(item.get("amount")) is None:
            errors.append("%s amount must be a signed fact in millions" % path)
    elif kind == "equity":
        extra = sorted(set(item) - {"kind", "name", "when", "probability", "shares", "proceeds", "price"})
        if extra:
            errors.append("%s equity item has unexpected %s" % (path, ", ".join(extra)))
        shares = _number_fact(item.get("shares")) if "shares" in item else None
        proceeds = _number_fact(item.get("proceeds")) if "proceeds" in item else None
        if "shares" not in item and "proceeds" not in item:
            errors.append("%s needs shares or proceeds" % path)
        if "shares" in item and (shares is None or shares <= 0):
            errors.append("%s shares must be a positive fact in millions" % path)
        if "proceeds" in item and (proceeds is None or proceeds <= 0):
            errors.append("%s proceeds must be a positive fact in millions" % path)
        if "price" in item:
            price = _number_fact(item.get("price"))
            if price is None or price <= 0:
                errors.append("%s price must be a positive fact" % path)


def _is_iso_date(value):
    if not isinstance(value, str):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def _number_fact(obj):
    if not _is_fact(obj):
        return None
    value = obj.get("value")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return value


def _check_ids(payload, errors):
    sources = payload.get("sources")
    if not isinstance(sources, list):
        errors.append("sources must be a list of entries with an id")
        return
    known = {}
    for index, entry in enumerate(sources):
        sid = entry.get("id") if isinstance(entry, dict) else None
        if not isinstance(sid, str) or not sid:
            errors.append("sources[%d] needs an id" % index)
            continue
        if sid in known:
            errors.append("sources id %s is listed twice" % sid)
        known[sid] = entry
        if sid[:1] in ("A", "G", "E") and not str(entry.get("text") or "").strip():
            errors.append("sources %s needs the quoted source text" % sid)
    for sid, entry in known.items():
        if sid.startswith("C"):
            inputs = entry.get("inputs")
            if not isinstance(inputs, list) or not inputs:
                errors.append("sources %s (calculation) must list its input ids" % sid)
                continue
            for ref in inputs:
                if ref not in known:
                    errors.append("sources %s input %s does not resolve" % (sid, ref))
    seen = {}
    for path, fact in _facts({k: v for k, v in payload.items() if k != "sources"}, "$"):
        citation = fact.get("citation")
        if not isinstance(citation, dict):
            continue
        cid = citation.get("id")
        if not isinstance(cid, str) or not cid:
            errors.append("%s citation needs an id" % path)
            continue
        if not citation.get("page") and citation.get("page_status") != "unverified":
            errors.append("%s citation needs a page or page_status 'unverified'" % path)
        if cid not in known:
            errors.append("%s citation id %s does not resolve in sources" % (path, cid))
        key = (fact.get("tag"), repr(fact.get("value")))
        if cid in seen and seen[cid][0] != key:
            errors.append("%s citation id %s is already used for a different fact at %s" % (path, cid, seen[cid][1]))
        seen.setdefault(cid, (key, path))


def _facts(obj, path):
    if isinstance(obj, dict) and _is_fact(obj):
        yield path, obj
        return
    if isinstance(obj, dict):
        for key, value in obj.items():
            yield from _facts(value, "%s.%s" % (path, key))
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            yield from _facts(item, "%s[%d]" % (path, index))
