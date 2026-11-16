from pathlib import Path

root = Path("forecasts/HROW")
report = (root / "report.md").read_text(encoding="utf-8")
section = (root / "_val_section.md").read_text(encoding="utf-8")
start = report.index("## 7. Valuation")
end = report.index("## 8. Risks")
report = report[:start] + section + "\n" + report[end:]
(root / "report.md").write_text(report, encoding="utf-8")
print("spliced", start, end, "new", len(report))
