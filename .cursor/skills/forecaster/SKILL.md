---
name: forecaster
description: Build an evidence-based near-term (explicit-year, usually two-year) revenue and EBITDA forecast for a public company and hand the operating path to Finagle. Use when forecasting a ticker, updating forecasts/<TICKER>/, or filling Finagle leaves (ebitda_growth, sales_growth, me, mc, gsnext). Does not set terminal growth and does not compute a value per share.
---

# Forecaster

A way to build a near-term operating forecast and hand it to [Finagle](https://github.com/mtlr05/finagle). Judgment is the work. The steps below are the default method, not a rulebook: a figure or an instruction in the prompt overrides them, and that override is tagged `[P]`.

Terminal growth, and the fade after the explicit window, belong to Finagle. This skill never sets `rates.gt`.

Read the references when you reach that step. They hold the tables; this file holds the method.

- [Tagging](references/tagging.md)
- [Wording](references/wording-table.md)
- [Driver patterns](references/driver-patterns.md)
- [Finagle handoff](references/finagle-handoff.md)

After the forecast, write the report with the [forecast-report skill](../forecast-report/SKILL.md).

Worked case: [forecasts/HROW](../../../forecasts/HROW/forecast.md). Layout: [AGENTS.md](../../../AGENTS.md).

## Where the history comes from

Read, in this order, and do not write to the last two:

1. The prompt.
2. The company's CEO repo from [ceochat](https://github.com/mtlr05/ceochat), if one is cloned beside this repo. It is how management talks about the lines. It is not a source of unpublished numbers.
3. The filing (EDGAR for a US issuer, SEDAR+ for a Canadian one) and the company's own IR release or transcript.

A number you cannot open stays out, or goes in with the citation text `link unverified`. Do not invent a URL or a figure.

## What you produce

For `forecasts/<TICKER>/`:

- `forecast.md`, the case a person can read
- `forecast.json`, the case the tests check
- `revision_log.md`, one row per line for this year and next year, on every update

`forecast.json` has to pass `pytest`. Periods are named `FYyyA`/`FYyyE` for fiscal years and `H1A`, `H2E`, `9MA`, `Q4E` and the like for part years; `baseline_period` and `explicit_periods` set which years the checks run on. Growth keys are `YoY` or `YoY_*`. A lone reference quarter such as `Q4FY26A` (the latest quarter) is summed across lines but not to a year. Part years sum to the first explicit year unless `stub_of` maps them (e.g. `{"H1E": "FY27E", "H2E": "FY27E"}`). A line's `pattern`, when given, is one of the [driver patterns](references/driver-patterns.md) in lower case, optionally followed by a note in parentheses. Every number is a fact: a value, a tag, and a citation. See [tagging](references/tagging.md).

## 1. Frame the forecast

Reported periods stay put. Forecast only periods the company has not reported.

A business line is a unit the company already reports revenue for, and margin if it reports that too: a segment, a product, an operating business, a geography, a channel. Do not split finer than the disclosure.

The baseline year shows year-over-year growth for the total and for each line.

Lines add up to the total. If they do not, fix the lines before scaling anything.

Bear, base, and bull differ in two or three levers, named up front. They do not each invent a new story.

## 2. Set the totals, then the lines

### 2a. Guidance-position coefficient

Do this separately for revenue and for EBITDA or margin.

For the last completed year, using that year's **original** range, before any revision:

```
C = (Actual - Low) / (High - Low)
```

The next year's forecast, if you are still on guidance, is:

```
Forecast = Low + C * (High - Low)
```

of next year's range.

Like for like. An original-range `C` is applied to an original range. A `C` from a revised range is applied only to a range that was revised at a similar point in the year.

Leave guidance when `C < 0` (the low end was missed) or when this year's guidance has been revised. Use the analyst consensus if one exists. Consensus used to score a print is the consensus dated **before** that release. Consensus used as the forward total is the latest pull, with its as-of date, tagged `[E]`.

If `C < 0` and no estimate exists, apply `C` anyway and flag it.

Single-point guidance (`more than $X`, `about $X`) does not have a `C`. Build the total from the lines (2b–2d) and enforce the words: `more than $X` means the total stays at or above `X`; `about $X` means it stays inside a stated band. If the build violates the words, flag it and adjust.

No guidance at all: use estimates if they exist, otherwise the bottom-up total, and flag it.

Show `C`, the low, the high, the actual, and which branch you took. Tag that block `[C]`.

### 2b. Turn words into numbers

Use [wording-table.md](references/wording-table.md). Absolute phrases map to a band. Relative phrases (`accelerating`, `momentum continues`) are read against that line's own prior-year growth.

The step size is a judgment from the adjective and the context. Tag it `[S]`, quote the sentence, and put it on the assumptions list. The step table in the reference is a set of starting defaults, not a conversion the quote has to survive.

Where a line splits price and volume, tag the phrase as a price effect (price, mix, rebates) or a volume effect (units, patients, procedures, customers). Forecast the two and multiply.

### 2c. Scale the lines to the total

Build the lines, then scale the unreported periods so they hit the 2a total. Actuals do not scale.

If the factor is more than 10% away from 1, the line commentary and the top-level target disagree. Flag it. The lines are then allocating a total they did not earn on their own.

### 2d. Run rate

Start from the latest reported quarter. Remove a one-time item only when the company flags it. Before a beat or a miss touches the run rate, classify the driver as one-time or recurring, and say why.

### 2e. Costs

Gross margin stays at the trailing level unless a source moves it.

Cash operating cost is the latest-quarter run rate plus step changes the company has actually announced. The run rate used here is gross profit minus adjusted EBITDA when that is the EBITDA the company guides. Say so. It is not a GAAP operating-expense line.

If you have a 2a EBITDA total, and the operating cost it implies differs from this run-rate build by more than 10%, keep the guidance-based EBITDA, flag the gap, and show the cost-based EBITDA beside it.

### 2f. Where the explicit years stop

Stop when the specific evidence stops. That is usually two years. Do not fill a third year to make a DCF look complete.

When the case hands off to Finagle, `me`, `mc`, and `gsnext` are required and are judgments about the path you just built, set against the history. Tag them. What happens after `gsnext` is Finagle fading toward `gt`. You do not choose `gt`.

## 3. Pick a driver pattern

Use [driver-patterns.md](references/driver-patterns.md). One pattern per line, or a new line when the disclosure adds one. The pattern builds the unscaled line; 2c still scales it to the total.

Choose from what management discusses, then the simplest pattern that fits the history.

## 4. Write down what a person should change

End every case with an assumptions list:

- the three to five moves that actually change the answer
- every `[S]` and every other judgment tag

Each entry says what to revise. A driver explains why (volume, price, a coverage win, destocking), not the number over again.

On an update, add a revision-log row per line for this year and next year: old, new, change, one line of why, including the growth rate old to new. Store it in `forecasts/<TICKER>/revision_log.md`.

## 5. Hand off to Finagle, or refuse

The handoff is optional. A case built without one sets `finagle_handoff: false` in `forecast.json` and skips this step; the Finagle leaves are then not required. A case that omits the field is treated as a handoff.

Follow [finagle-handoff.md](references/finagle-handoff.md). The order is `describe_inputs`, `build_baseline`, the leaves this skill fills, the leaves the template fills, `validate_case`, `run_case`.

Refuse the handoff if `forecast.ebitda_growth`, `forecast.sales_growth`, `me`, `mc`, or `gsnext` is missing. Omitting the margin path on a prior HROW case changed the value from $56.69 to $171.62. Do not compute a value anywhere except `run_case`. An update goes through `update_case`.

## 6. Check

`pytest` from the repo root. The HROW file is the fixture that has to pass.

## Sources and credit

Four practices were adapted from [anthropics/financial-services](https://github.com/anthropics/financial-services) (Apache-2.0), and restated here rather than copied:

- a revision table, from the model-update skill
- consensus dated before the release, from the earnings-analysis workflow
- classifying a beat or miss as one-time or sustainable before it changes the forecast, from earnings-analysis step 5
- a driver explains why, not what, from the fund-admin variance-commentary skill

See `NOTICE`.
