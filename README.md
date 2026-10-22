# Forecaster

Evidence-based near-term forecasts for a public company: explicit years, usually two, then a handoff to [Finagle](https://github.com/mtlr05/finagle) for the DCF. Terminal growth stays in Finagle.

The method is a skill, not a closed rulebook. A figure in the prompt overrides a default.

- Skill: [`.cursor/skills/forecaster/SKILL.md`](.cursor/skills/forecaster/SKILL.md)
- Worked case: [`forecasts/HROW/forecast.md`](forecasts/HROW/forecast.md) (Harrow, Inc.)
- Template leaves the forecast does not set: [`templates/case_template.json`](templates/case_template.json)

## Layout

```
forecaster/    this repo
finagle/       github.com/mtlr05/finagle    read-only
ceochat/       github.com/mtlr05/ceochat    read-only
```

History comes from a CEO repo when one exists, from EDGAR or SEDAR+, and from the company's IR. See [AGENTS.md](AGENTS.md).

## Check

```bash
pip install pytest
pytest
```

`pytest` checks `forecasts/<TICKER>/forecast.json`: every number has a tag and a citation, the lines add up, and the Finagle leaves (`ebitda_growth`, `sales_growth`, `me`, `mc`, `gsnext`) are present and consistent with the organic dollars.

## Sources and credit

Four practices were adapted from [anthropics/financial-services](https://github.com/anthropics/financial-services) (Apache-2.0) and restated in this repo's own words: the revision table (model-update), consensus dated before the release (earnings-analysis), one-time versus sustainable beat/miss classification (earnings-analysis step 5), and a driver that explains why rather than what (fund-admin variance-commentary). See [NOTICE](NOTICE).
