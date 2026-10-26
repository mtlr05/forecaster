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
"""

from __future__ import annotations

import re

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
