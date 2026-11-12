# Forecaster

Revenue and EBITDA forecasts for a public company, and the inputs a Finagle valuation reads. The same skill updates an existing forecast for a company update or a modelling refinement. The explicit window is the longest of two years, the guidance horizon, and the Consensus horizon, unless the prompt states otherwise. On an update the window stays unless the prompt changes it. Every forecast writes those inputs. A collaborative run sends them. The method is the skill, not this file.

Read `.cursor/skills/forecaster/SKILL.md` before forecasting. Tables are in `.cursor/skills/forecaster/references/`. Every forecast also gets an analyst-style `report.md` and `report.pdf` beside it, written with `.cursor/skills/forecast-report/SKILL.md`.

## Layout

This repo is the one you write. Cases live in `forecasts/<TICKER>/`. Check a case with `pytest`.

## Collaborative run

Only when the user asks for a joint valuation. Follow `.cursor/skills/forecaster/references/collaborative-run.md`. Finagle is the valuation model already checked out beside this repo. It runs the case. This session does not clone it and does not pull. A collaborative run sends the inputs every forecast writes. Results come back here for the valuation section of the report. A forecast on its own does not use this section.
