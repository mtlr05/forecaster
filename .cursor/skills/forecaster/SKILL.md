---
name: forecaster
description: Build an evidence-based near-term (explicit-year, usually two-year) revenue and EBITDA forecast for a public company. Use when forecasting a ticker or updating forecasts/<TICKER>/.
---

# Forecaster

A way to build a near-term operating forecast. Judgment is the work. The steps below are the default method, not a rulebook: a figure or an instruction in the prompt overrides them, and that override is tagged `[P]`.

Read the references when you reach that step. They hold the tables; this file holds the method.

- [Tagging](references/tagging.md)
- [Wording](references/wording-table.md)
- [Driver patterns](references/driver-patterns.md)

After the forecast, write the report with the [forecast-report skill](../forecast-report/SKILL.md).

Worked case: [forecasts/HROW](../../../forecasts/HROW/forecast.md). Layout: [AGENTS.md](../../../AGENTS.md).

## Where the history comes from

Read, in this order. Do not write outside this repo.

1. The prompt.
2. The filing (EDGAR for a US issuer, SEDAR+ for a Canadian one) and the company's own IR release or transcript.

A number you cannot open stays out, or goes in with the citation text `link unverified`. Do not invent a URL or a figure.

## What you produce

For `forecasts/<TICKER>/`:

- `forecast.md`, the case a person can read
- `forecast.json`, the case the tests check
- `report.md` and `report.pdf`, the analyst-style update
- `revision_log.md`, one row per line for this year and next year, on every update

`forecast.json` has to pass `pytest`. Periods are named `FYyyA`/`FYyyE` for fiscal years and `H1A`, `H2E`, `9MA`, `Q4E` and the like for part years; `baseline_period` and `explicit_periods` set which years the checks run on. Growth keys are `YoY` or `YoY_*`. A lone reference quarter such as `Q4FY26A` (the latest quarter) is summed across lines but not to a year. Part years sum to the first explicit year unless `stub_of` maps them (e.g. `{"H1E": "FY27E", "H2E": "FY27E"}`). A line's `pattern`, when given, is one of the [driver patterns](references/driver-patterns.md) in lower case, optionally followed by a note in parentheses. Every number is a fact: a value, a tag, and a citation. See [tagging](references/tagging.md).

## Status and open items

`forecast.md` can open with a short `## Status and open items` block. It replaces a separate status note.

- When a task names a ticker, read `forecasts/<TICKER>/forecast.md` first, starting with its Status block if it has one.
- The block holds only the open items, the current version and values, and how to resume (which scripts rebuild what, and their inputs). Assumptions and reasoning stay in the report and the rest of `forecast.md`; point to their sections, do not restate them.
- Update the block at each agreed change of a decision, a value or an open item. A value change also gets a `revision_log.md` row.
- Create the block when a ticker's work first has open items, or a resume procedure that `forecast.md` does not already give.

## 1. Frame the forecast

Reported periods stay put. Forecast only periods the company has not reported.

A business line is a unit the company already reports revenue for, and margin if it reports that too: a segment, a product, an operating business, a geography, a channel. Do not split finer than the disclosure. A single-segment filer's lines are the revenue breakdown it reports: geography, revenue type (e.g. service vs. vehicle sales), or both crossed if both are reported. Say which one you used.

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

No guidance at all: use estimates if they exist, otherwise the bottom-up total, and flag it. There is no `C` to calculate. Say so in the `[C]` block, name the branch taken (consensus, or the line build when there is no consensus), and flag it in the assumptions list.

Show `C`, the low, the high, the actual, and which branch you took. Tag that block `[C]`.

### 2b. Turn words into numbers

Use [wording-table.md](references/wording-table.md). Absolute phrases map to a band. Relative phrases (`accelerating`, `momentum continues`) are read against that line's own prior-year growth.

The step size is a judgment from the adjective and the context. Tag it `[S]`, quote the sentence, and put it on the assumptions list. The step table in the reference is a set of starting defaults, not a conversion the quote has to survive.

Where a line splits price and volume, tag the phrase as a price effect (price, mix, rebates) or a volume effect (units, patients, procedures, customers). Forecast the two and multiply.

### 2c. Scale the lines to the total

Build the lines, then scale the unreported periods so they hit the 2a total. Actuals do not scale.

When consensus or guidance sets the total, say that the lines are scaled to it. The unscaled build is a diagnostic only, never an alternative forecast.

If the factor is more than 10% away from 1, the line commentary and the top-level target disagree. Flag it. The lines are then allocating a total they did not earn on their own.

Above about 1.25×, scaling revenue with costs held fixed inflates margins mechanically. Scale the variable costs too, or show the unscaled case beside the scaled one as a sensitivity.

An acquired line is not scaled to consensus, because consensus coverage of the deal is uncertain. See [driver-patterns.md](references/driver-patterns.md).

### 2d. Run rate

Start from the latest reported quarter. Remove a one-time item only when the company flags it. Before a beat or a miss touches the run rate, classify the driver as one-time or recurring, and say why.

*Example (insurance-auction businesses):* catastrophe or hurricane volume, such as CPRT's FY25 Helene/Milton volume, is one-time.

### 2e. Costs

Gross margin stays at the trailing level unless a source moves it. State the gross margin basis (GAAP or cash), and keep management's margin language on the same basis.

Define the cost base first. Cash opex = GAAP operating expenses − stock comp − depreciation (− company-flagged one-time items). Reconcile it to reported adjusted EBITDA: gross profit + amortization in COGS − cash opex = adjusted EBITDA (HROW Q2'26: 50.363 + 5.527 − 57.122 = −1.232). State where amortization and stock comp sit. Gross profit minus adjusted EBITDA is not the cost base: it nets amortization into opex and understates EBITDA.

When management describes how it gets to its EBITDA guide (HROW: "substantially higher revenue, increasing gross margins into the high 70s, and a base operating expense structure that remains approximately flat"), the cost step follows that description first. Only when there isn't one, cash operating cost is the latest-quarter run rate plus step changes the company has actually announced, grown for inflation.

When the company doesn't report adjusted EBITDA, state the definition as a calculation, e.g. operating income + D&A + stock comp, tagged `[C]`. Keep it consistent with any acquired company's own definition, and show the effect of including or excluding stock comp.

When a revenue consensus exists but no EBITDA estimate does, build EBITDA from costs as above, and flag it.

If you have a 2a EBITDA total, and the operating cost it implies differs from this cost build by more than 10%, keep the guidance-based EBITDA, flag the gap, and show the cost-based EBITDA beside it.

### 2f. Where the explicit years stop

Stop when the specific evidence stops. That is usually two years.

Write the growth of those dollars on `forecast.json` under `finagle`. That is the block the tests check. `sales_growth` and `ebitda_growth` are one rate per explicit year, and they compound back to the revenue and EBITDA you just wrote. `me` is the last explicit year's EBITDA divided by revenue. `mc` is the contribution margin, set against the history. `gsnext` is sales growth in the year after the explicit window. Tag them. `me` and `mc` are not zero.

## 3. Pick a driver pattern

Use [driver-patterns.md](references/driver-patterns.md). One pattern per line, or a new line when the disclosure adds one. The pattern builds the unscaled line; 2c still scales it to the total.

Choose from what management discusses, then the simplest pattern that fits the history.

## 4. Write down what a person should change

End every case with an assumptions list:

- the three to five moves that actually change the answer
- every `[S]` and every other judgment tag

Each entry says what to revise. A driver explains why (volume, price, a coverage win, destocking), not the number over again.

On an update, first check EDGAR or SEDAR+ for filings since the last revision, and record the consensus pull date and source in the file. Then add a revision-log row per line for this year and next year: old, new, change, one line of why, including the growth rate old to new. Store it in `forecasts/<TICKER>/revision_log.md`.

## 5. Check

`pytest` from the repo root. The HROW forecast is the case that has to pass.

## Collaborative run

Only when the user asks for a joint valuation. Follow [collaborative-run.md](references/collaborative-run.md). Copy the user's `prompt_inputs` into the request unchanged. Add nothing the user did not state. The published value is the one in the result file. Write the valuation section of the report from that file. Apply a post-run factor only when the request has one, and show the raw and adjusted values side by side, tagged `[P]` with the user's date.

## Sources and credit

Four practices were adapted from [anthropics/financial-services](https://github.com/anthropics/financial-services) (Apache-2.0), and restated here rather than copied:

- a revision table, from the model-update skill
- consensus dated before the release, from the earnings-analysis workflow
- classifying a beat or miss as one-time or sustainable before it changes the forecast, from earnings-analysis step 5
- a driver explains why, not what, from the fund-admin variance-commentary skill

See `NOTICE`.
