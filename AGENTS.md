# Forecaster

Near-term revenue and EBITDA forecasts for a public company, handed to Finagle. The method is the skill, not this file.

Read `.cursor/skills/forecaster/SKILL.md` before forecasting. Tables and the Finagle contract are in `.cursor/skills/forecaster/references/`. Every forecast also gets an analyst-style `report.md` and `report.pdf` beside it, written with `.cursor/skills/forecast-report/SKILL.md`.

## Layout

Clone the three repos side by side. Only this one is writable.

```
forecaster/    this repo
finagle/       https://github.com/mtlr05/finagle   read-only
ceochat/       https://github.com/mtlr05/ceochat   read-only
```

Finagle runs the case (`describe_inputs`, `build_baseline`, `validate_case`, `run_case`). Ceochat CEO repos are background on how management talks. Neither gets edits from a forecast.

Cases live in `forecasts/<TICKER>/`. The empty slots a person still has to fill are `templates/case_template.json`. Check a case with `pytest`.
