# Forecaster

Evidence-based revenue and EBITDA forecasts for a public company, and the inputs a Finagle valuation reads. The same skill updates an existing forecast for a company update or a modelling refinement. The explicit window is the longest of two years, the guidance horizon, and the Consensus horizon, unless the prompt states otherwise. On an update the window stays unless the prompt changes it.

The method is a skill, not a closed rulebook. A figure in the prompt overrides a default.

- Skill: [`.cursor/skills/forecaster/SKILL.md`](.cursor/skills/forecaster/SKILL.md)
- Worked case: [`forecasts/HROW/forecast.md`](forecasts/HROW/forecast.md) (Harrow, Inc.)

## Layout

Cases live in `forecasts/<TICKER>/`. Read the filings for at least the last nine reported quarters: the financial reports, the earnings press releases, the earnings call transcripts, and any shareholder letter. US issuers are on EDGAR, Canadian issuers on SEDAR+, and the company's own IR pages. See [AGENTS.md](AGENTS.md).

## Collaborative run

Only when the user asks for a joint valuation. See [`.cursor/skills/forecaster/references/collaborative-run.md`](.cursor/skills/forecaster/references/collaborative-run.md). Values the user may state, and that the forecast does not set, are listed in [`templates/case_template.json`](templates/case_template.json).

## Check

```bash
pip install -r requirements-dev.txt
pytest
```

`pytest` checks `forecasts/<TICKER>/forecast.json`: every number has a tag and a citation, the lines add up, part-year periods add up to their fiscal year, and, unless a case sets `finagle_handoff: false`, the growth and margin leaves (`ebitda_growth`, `sales_growth`, `me`, `mc`, `gsnext`) are present and consistent with the organic dollars.

## Sources and credit

Four practices were adapted from [anthropics/financial-services](https://github.com/anthropics/financial-services) (Apache-2.0) and restated in this repo's own words: the revision table (model-update), consensus dated before the release (earnings-analysis), one-time versus sustainable beat/miss classification (earnings-analysis step 5), and a driver that explains why rather than what (fund-admin variance-commentary). See [NOTICE](NOTICE).
