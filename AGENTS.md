# Forecaster

Near-term revenue and EBITDA forecasts for a public company. The method is the skill, not this file.

Read `.cursor/skills/forecaster/SKILL.md` before forecasting. Tables are in `.cursor/skills/forecaster/references/`. Every forecast also gets an analyst-style `report.md` and `report.pdf` beside it, written with `.cursor/skills/forecast-report/SKILL.md`.

## Layout

This repo is the one you write. Cases live in `forecasts/<TICKER>/`. Check a case with `pytest`.

## Collaborative run

Only when the user asks for a joint valuation. Follow `.cursor/skills/forecaster/references/collaborative-run.md`. The Finagle checkout already beside this repo runs the case. This session does not clone it and does not pull. Results come back here for the valuation section of the report. A forecast on its own does not use this section.
