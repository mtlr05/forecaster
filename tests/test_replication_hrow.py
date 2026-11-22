"""HROW v03 replication. Not part of a default pytest run.

Needs the Finagle checkout beside this repo, network access to EDGAR,
Yahoo, and FRED, and FINAGLE_SEC_USER_AGENT. Set RUN_COLLABORATIVE_REPLICATION=1.
The run writes into a temporary directory and deletes it.
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
FINAGLE = ROOT.parent / "finagle"
SAMPLES = ROOT / "tests" / "samples" / "hrow_v03"

pytestmark = pytest.mark.skipif(
    os.environ.get("RUN_COLLABORATIVE_REPLICATION") != "1",
    reason="set RUN_COLLABORATIVE_REPLICATION=1 to replicate the HROW v03 run",
)


def test_hrow_v03_matches_with_lam_zero():
    expected = json.loads((SAMPLES / "expected.json").read_text())
    result = _run(_pins())
    for name, row in expected["scenarios"].items():
        scenario = result["scenarios"][name]
        assert scenario["ok"] is True
        assert scenario["validation"]["errors"] == []
        assert scenario["validation"]["missing"] == []
        assert abs(scenario["value_per_share"] - row["value_per_share"]) < expected["tolerance"]


def test_hrow_with_the_default_pass_through_differs_from_v03():
    expected = json.loads((SAMPLES / "expected.json").read_text())
    pins = [item for item in _pins() if item["path"] != "rates.lam"]
    result = _run(pins)
    for name, row in expected["scenarios"].items():
        scenario = result["scenarios"][name]
        assert scenario["ok"] is True
        assert "rates.lam" in scenario["defaults_filled"]
        inflation = scenario["case"]["rates"]["inflation"]
        assert inflation.get("value") is not None
        assert abs(scenario["value_per_share"] - row["value_per_share"]) >= expected["tolerance"]


def _pins():
    extra = json.loads((SAMPLES / "replication.json").read_text())
    return list(extra["prompt_inputs"])


def _run(pins):
    assert os.environ.get("FINAGLE_SEC_USER_AGENT"), "FINAGLE_SEC_USER_AGENT is required"
    assert (FINAGLE / "finagle" / "agent" / "runner.py").is_file()
    request = json.loads((SAMPLES / "request.json").read_text(encoding="utf-8"))
    request["prompt_inputs"] = pins
    with tempfile.TemporaryDirectory(prefix="hrow-v03-") as tmp:
        out = Path(tmp)
        request_path = out / "valuation_request.json"
        request_path.write_text(json.dumps(request), encoding="utf-8")
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "templates" / "run_collaborative.py"),
                "--request",
                str(request_path),
                "--finagle",
                str(FINAGLE),
                "--out",
                str(out),
            ],
            cwd=str(ROOT),
            text=True,
            capture_output=True,
        )
        result_path = out / "valuation_result_v03.json"
        assert completed.returncode == 0, completed.stderr[-4000:]
        return json.loads(result_path.read_text(encoding="utf-8"))
