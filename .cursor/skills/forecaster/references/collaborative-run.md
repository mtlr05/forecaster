# Collaborative run

This file applies only when the user asks for a joint valuation. The request then carries `"mode": "collaborative"`. A forecast on its own does not use this file.

The Forecaster writes the operating path. The user may state any values for this valuation. Those values are `prompt_inputs`: the same explicit numbers go to Finagle and into the report, tagged `[P]`, with the user's words and date. Precedence is the user's values, then the Forecaster, then Finagle's defaults. A joint run adds no rules of its own. One-off numbers from an earlier company are not defaults.

## What each side provides

The Forecaster provides, for each scenario:

- `forecast.sales_growth` and `forecast.ebitda_growth`, one rate per explicit year
- `forecast.ebitda_basis` (`organic` or `total`)
- `forecast.acquisition_disclosure` and `acquisitions`, only for deals the forecast includes
- `forecast.margin_path.me`, `.mc`, and `.gsnext`

`me` is the last explicit year's EBITDA divided by revenue. A value the user states for `me`, `mc`, or `gsnext` replaces the Forecaster's when the case runs. Record the user's value as `[P]` with their words and date. Keep the Forecaster's own value in the request.

`prompt_inputs` holds only what the user stated for this valuation. It may be empty. Each item has a path, a value (a list written out year by year), `applies_to`, a quote, and a date. Nothing is inferred from an earlier valuation.

Finagle supplies price, shares, the risk-free rate, the cost of equity, terminal growth, and the year-0 figures, unless the user stated one. A stated one is a `prompt_inputs` item. The request does not carry price, shares, the risk-free rate, the cost of equity, or terminal growth unless that quote is present.

Do not set a capex path or a stock-comp path unless the user stated one. Stock comp inside the cost build defines EBITDA. It is not a stock-comp forecast.

Values the user may state, and that the forecast does not choose, are listed in [templates/case_template.json](../../../templates/case_template.json).

## Request

The Forecaster writes `valuation_request_vNN.json` in the run folder. Commit it only if the user asks.

```json
{
  "mode": "collaborative",
  "ticker": "<TICKER>",
  "version": "vNN",
  "parent_version": null,
  "forecast_commit": "<sha or uncommitted>",
  "scenarios": ["base"],
  "forecaster": {
    "base": {
      "forecast.sales_growth": {"value": [], "tag": "C", "cite_id": "C1", "evidence": "..."}
    }
  },
  "prompt_inputs": [],
  "post_finagle": null
}
```

`forecaster` is copied from `forecast.json`. Each leaf is a tagged fact. `prompt_inputs` is copied unchanged from what the user stated. `post_finagle` stays null unless the user stated an adjustment for this company, for example `{"factor": 0.90, "label": "dilution", "quote": "...", "date": "YYYY-MM-DD"}`. Every change is a new version.

## Order

1. Build or refresh `forecast.json` as usual. `pytest` passes.
2. Write the request. Copy `prompt_inputs` unchanged.
3. Check the request: every prompt item has a quote and a date, the Forecaster block matches `forecast.json`, and price, shares, the risk-free rate, the cost of equity, and terminal growth appear only with a user quote.
4. On the Finagle checkout already beside this repo, call `describe_inputs`, then `build_baseline(ticker)`. Lay the Forecaster leaves, then `prompt_inputs`, onto the case with `update_case` after `build_baseline`. `build_baseline` drops a prompt leaf that has no fiscal-year basis, so year-0 figures the user stated are stamped to the baseline year there. `validate_case` errors or missing fields stop the scenario. `run_case` runs once per scenario. The result records the Finagle commit and every leaf Finagle filled by default.
5. Write the report's valuation section from `valuation_result_vNN.json` only. The result file's value is the raw value. Apply `post_finagle` in the report when the request has one, and show raw and adjusted side by side, tagged `[P]` with the user's date.

Cursor uses the Finagle checkout it already has. It does not clone Finagle and does not pull. The Grok Bot's Finagle side fast-forwards its own clone to `origin/main` before the run (`git fetch`, then `git merge --ff-only`) and records the commit. If that fast-forward fails, it stops. It does not reset.

A prompt list, including a stock-comp list, uses Finagle source `prompt`. A full list whose source is `assumption` is cut back to year 0.

`forecast.acquisition_disclosure` is an object. The leaf is `.status`.

## Result

`valuation_result_vNN.json` carries `ticker`, `version`, `finagle_commit`, `run_at`, and `fetched` (price, price date, risk-free rate, rate date, shares, shares source). Each scenario keeps `run_case`'s own keys and adds `defaults_filled`, the leaves whose source is `assumption`.

The valuation section of the report lists:

- the raw value per share, and the adjusted value when `post_finagle` is set
- every prompt input, tagged `[P]` with its date
- `defaults_filled`, sanity flags, and validation warnings, in the result's own words
- the fetched market inputs and the Finagle commit
