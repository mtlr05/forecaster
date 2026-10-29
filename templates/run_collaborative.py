#!/usr/bin/env python3
"""Run a collaborative valuation on the Finagle checkout beside this repo.

Uses that checkout as it is. Does not fetch, merge, clone, or check out
another commit. Does not apply a post-run factor and does not write a
company report. The valuation section markdown is numbers from the result.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from forecastcheck.collaborative import (  # noqa: E402
    check_request,
    render_valuation_section,
    scenario_updates,
)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", required=True, help="Path to valuation_request JSON")
    parser.add_argument("--finagle", required=True, help="Path to the existing Finagle checkout")
    parser.add_argument("--out", required=True, help="Directory for the result files")
    args = parser.parse_args(argv)

    request_path = Path(args.request)
    request = json.loads(request_path.read_text())
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    errors = check_request(request)
    if errors:
        _write_result(out, request, {"ok": False, "errors": errors})
        print("\n".join(errors), file=sys.stderr)
        return 1

    finagle = Path(args.finagle).resolve()
    if str(finagle) not in sys.path:
        sys.path.insert(0, str(finagle))
    from finagle.agent.catalog import describe_inputs
    from finagle.agent.schema import iter_leaves
    from finagle.agent.sources import build_baseline
    from finagle.agent.update import update_case

    describe_inputs()
    commit = subprocess.check_output(
        ["git", "-C", str(finagle), "rev-parse", "HEAD"], text=True
    ).strip()
    baseline = build_baseline(
        request["ticker"], user_agent=os.environ.get("FINAGLE_SEC_USER_AGENT")
    )
    result = {
        "ticker": request.get("ticker"),
        "version": request.get("version"),
        "finagle_commit": commit,
        "run_at": datetime.now(timezone.utc).isoformat(),
        "scenarios": {},
    }
    if not baseline.get("ok"):
        result["ok"] = False
        result["error"] = baseline.get("error")
        result["unread_charts"] = baseline.get("unread_charts")
        _write_result(out, request, result)
        print(result["error"], file=sys.stderr)
        return 1

    case0 = baseline["case"]
    result["fetched"] = _fetched(case0)
    for name in request["scenarios"]:
        updates = scenario_updates(request, name)
        case = copy.deepcopy(case0)
        for key, value in updates["plain"].items():
            case[key] = value
        leaves = _stamp_baseline(updates["leaves"], case)
        run = update_case(case, leaves, run=True)
        ran = run.get("case") or case
        run["defaults_filled"] = [
            path for path, node in iter_leaves(ran) if node.get("source") == "assumption"
        ]
        result["scenarios"][name] = run
        case_name = "case_%s_%s.json" % (name, request.get("version") or "v")
        (out / case_name).write_text(json.dumps(ran, indent=2, default=str))

    _write_result(out, request, result)
    failed = any(not (item or {}).get("ok") for item in result["scenarios"].values())
    return 1 if failed else 0


def _stamp_baseline(leaves, case):
    """Year-0 figures the user stated need the baseline fiscal year."""
    baseline = case.get("baseline") if isinstance(case.get("baseline"), dict) else {}
    date = baseline.get("date") if isinstance(baseline.get("date"), dict) else {}
    period = date.get("value")
    currency = None
    for node in baseline.values():
        if isinstance(node, dict) and node.get("currency"):
            currency = node["currency"]
            break
    stated = leaves.get("baseline")
    if isinstance(stated, dict) and period:
        for node in stated.values():
            if isinstance(node, dict) and "value" in node and "source" in node:
                node.setdefault("basis", "fiscal_year")
                node.setdefault("period_end", period)
                if currency:
                    node.setdefault("currency", currency)
    return leaves


def _fetched(case):
    market = case.get("market") or {}
    rates = case.get("rates") or {}
    price = market.get("price") if isinstance(market.get("price"), dict) else {}
    shares = market.get("shares") if isinstance(market.get("shares"), dict) else {}
    risk_free = rates.get("risk_free") if isinstance(rates.get("risk_free"), dict) else {}
    return {
        "price": price.get("value"),
        "price_date": price.get("as_of"),
        "rf": risk_free.get("value"),
        "rf_date": risk_free.get("as_of"),
        "shares": shares.get("value"),
        "shares_source": shares.get("source"),
    }


def _write_result(out, request, result):
    version = request.get("version") or "v"
    (out / ("valuation_result_%s.json" % version)).write_text(
        json.dumps(result, indent=2, default=str)
    )
    if result.get("scenarios") is not None:
        (out / "valuation_section.md").write_text(render_valuation_section(result, request))


if __name__ == "__main__":
    sys.exit(main())
