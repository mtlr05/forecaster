"""CLPT v11 replication. Not part of a default pytest run.

Needs the Finagle checkout beside this repo, network access to EDGAR and
Yahoo, and FINAGLE_SEC_USER_AGENT. Set RUN_COLLABORATIVE_REPLICATION=1.
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
SAMPLES = ROOT / "tests" / "samples" / "clpt_v11"

pytestmark = pytest.mark.skipif(
    os.environ.get("RUN_COLLABORATIVE_REPLICATION") != "1",
    reason="set RUN_COLLABORATIVE_REPLICATION=1 to replicate the CLPT v11 run",
)


def test_clpt_v11_matches_within_five_cents():
    assert os.environ.get("FINAGLE_SEC_USER_AGENT"), "FINAGLE_SEC_USER_AGENT is required"
    assert (FINAGLE / "finagle" / "agent" / "runner.py").is_file()
    request = json.loads((SAMPLES / "request.json").read_text())
    extra = json.loads((SAMPLES / "replication.json").read_text())
    expected = json.loads((SAMPLES / "expected.json").read_text())
    request["prompt_inputs"] = list(request["prompt_inputs"]) + list(extra["prompt_inputs"])
    with tempfile.TemporaryDirectory(prefix="clpt-v11-") as tmp:
        out = Path(tmp)
        request_path = out / "valuation_request.json"
        request_path.write_text(json.dumps(request))
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
        result_path = out / "valuation_result_v11.json"
        assert completed.returncode == 0, completed.stderr[-4000:]
        result = json.loads(result_path.read_text())
        assert result["finagle_commit"].startswith(expected["finagle_commit_prefix"])
        section = (out / "valuation_section.md").read_text()
        assert not (out / "report.md").exists()
        for name, row in expected["scenarios"].items():
            scenario = result["scenarios"][name]
            assert scenario["ok"] is True
            assert scenario["validation"]["errors"] == []
            assert scenario["validation"]["missing"] == []
            assert abs(scenario["value_per_share"] - row["value_per_share"]) < expected["tolerance"]
            sbc = scenario["case"]["forecast"]["sbc"]
            assert sbc["source"] == "prompt"
            assert scenario["defaults_filled"]
            raw = scenario["value_per_share"]
            assert f"{raw:.4f}" in section
            assert f"{raw * request['post_finagle']['factor']:.4f}" in section
        assert "[P]" in section
        assert "2026-10-26" in section
        for item in request["prompt_inputs"]:
            assert item["path"] in section
