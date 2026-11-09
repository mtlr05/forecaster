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

Read at least nine reported quarters of revenue, and of EBITDA or margin where the company reports them, plus the earnings transcript for each of those quarters, where the documents exist. When a quarter has no call, the earnings press release for that quarter is the call material. Use its words for one-time items (2d) and for `mc`, `gsnext`, and the other inputs past the explicit years (2f). Name the substitute and flag that there was no call. A missing call alone does not make the window short. Name the window (for example Q2 FY24 through Q2 FY26). A shorter history (a new issuer, restated segments, a quarter with neither a transcript nor a release) is used as-is and flagged.

A number you cannot open stays out, or goes in with the citation text `link unverified`. Do not invent a URL or a figure.

## What you produce

For `forecasts/<TICKER>/`:

- `forecast.md`, the case a person can read
- `forecast.json`, the case the tests check
- `report.md` and `report.pdf`, the analyst-style update
- `revision_log.md`, one row per line for this year and next year, on every update

`forecast.json` has to pass `pytest`. Periods are named `FYyyA`/`FYyyE` for fiscal years and `H1A`, `H2E`, `9MA`, `Q4E` and the like for part years; `baseline_period` and `explicit_periods` set which years the checks run on. Growth keys are `YoY` or `YoY_*`. A lone reference quarter such as `Q4FY26A` (the latest quarter) is summed across lines but not to a year. Part years sum to the first explicit year unless `stub_of` maps them (e.g. `{"H1E": "FY27E", "H2E": "FY27E"}`). A line's `pattern`, when given, is one of the [driver patterns](references/driver-patterns.md) in lower case, optionally followed by a note in parentheses. Every number is a fact: a value, a tag, and a citation. See [tagging](references/tagging.md).

New cases also carry a `views` block: bottom-up, top-down, calibrated top-down, and Consensus, for revenue and for EBITDA, for each explicit year, plus which view is the base for each metric and the ratios between them. The shape is in section 2. A case without `views` passes with a warning.

## Status and open items

`forecast.md` can open with a short `## Status and open items` block. It replaces a separate status note.

- When a task names a ticker, read `forecasts/<TICKER>/forecast.md` first, starting with its Status block if it has one.
- The block holds only the open items, the current version and values, and how to resume (which scripts rebuild what, and their inputs). Assumptions and reasoning stay in the report and the rest of `forecast.md`; point to their sections, do not restate them.
- Update the block at each agreed change of a decision, a value or an open item. A value change also gets a `revision_log.md` row.
- Create the block when a ticker's work first has open items, or a resume procedure that `forecast.md` does not already give.

## 1. Frame the forecast

Reported periods stay put. Forecast only periods the company has not reported.

A business line is a unit the company already reports revenue for, and margin if it reports that too: a segment, a product, an operating business, a geography, a channel. Do not split finer than the disclosure. A single-segment filer's lines are the revenue breakdown it reports: geography, revenue type (e.g. service vs. vehicle sales), or both crossed if both are reported. Say which one you used.

Royalties, license revenue, earn-outs, and similar contingent payments stay inside the reported line that already includes them. A contingent item is its own line only when management already reports it as its own line. Build the operating piece and the contingent piece, then one line total. See [driver patterns](references/driver-patterns.md). If those dollars already sit in the reported line, in guidance, or in Consensus, leave them there: they are an allocation inside the line when the base is top-down, calibrated top-down, or Consensus, and they are not added again on top of that total. When the dollars cannot be split out, keep the single line, say the piece is not separable, and state how the build treats it: in the run rate, probability-weighted, or already inside the total.

The baseline year shows year-over-year growth for the total and for each line.

Lines add up to the total. If they do not, fix the lines before scaling anything.

Bear, base, and bull differ in two or three levers, named up front. They do not each invent a new story.

## 2. Set the totals, then the lines

Four views are recorded for revenue and for EBITDA, for each explicit year, including the one chosen as the base. A view that does not exist is recorded as absent, with the reason.

- **Bottom-up.** Revenue is the sum of the unscaled lines. EBITDA is the cost build in 2e, unless the filing reports line profits that already sum to it.
- **Top-down.** Management's guidance range for that year: low and high. A single point (`more than $X`, `about $X`) is recorded as a point, and calibrated top-down is absent because there is no `C`.
- **Calibrated top-down.** `Low + C * (High - Low)` on the like-for-like range. Absent, with the reason, when there is no range, when `C` is not applied, or when this step says to leave guidance. `C` is not applied when `C < 0` and a Consensus exists, when guidance has been revised, or when there is no completed original range. When `C < 0` and no Consensus exists, apply `C` anyway: calibrated top-down is then the base, and it is flagged.
- **Consensus.** Analyst estimates, the latest pull, tagged `[E]`. Record `analysts` (the count on the pull) and `as_of` (the pull date) on the fact. If `analysts` is 1, or `as_of` is missing, flag it in the `[C]` block and on the assumptions list. The figure can still be the base. Absent when none exists.

The base is chosen separately for revenue and for EBITDA. For each metric: calibrated top-down while still on guidance. Consensus when leaving guidance and an estimate exists. Bottom-up when neither exists, or when a single-point guide is enforced on the line build. Top-down is the base only when the base is an explicit point inside the range, named in the citation. Bottom-up stays a recorded view beside that base. The dollars on `lines` are the scaled base-case dollars.

Do this separately for revenue and for EBITDA. A later explicit year with no guidance range has top-down and calibrated top-down absent.

`forecast.md` shows the four views, which one is the base for each metric, and the ratios beside the `[C]` block. `forecast.json` records them under `views`:

- `views.used` is `{"revenue": "...", "ebitda": "..."}`. Each value is `bottom_up`, `top_down`, `calibrated_top_down`, or `consensus`.
- `views.revenue.<FYyyE>` and `views.ebitda.<FYyyE>` each hold `bottom_up`, `top_down`, `calibrated_top_down`, and `consensus`. A point view is a fact. Top-down is `low` and `high`, or `point` when guidance is a single point. When top-down is the base, `point` is that base and the citation names it. A missing view is `{"absent": "<reason>"}`.
- `views.ratios.<FYyyE>.revenue` and `.ebitda` hold `bottom_up_over_base`, `top_down_over_base`, `calibrated_top_down_over_base`, `consensus_over_base`, `bottom_up_over_calibrated_top_down`, and `bottom_up_over_consensus`. Each is a fact or an absent reason. A ratio divides by that metric's base. The top-down ratio uses the midpoint of low and high, tagged `[C]`. A missing numerator or denominator is absent.

Every dollar and every ratio is a fact. A case without `views` passes with a warning; new cases carry the block.

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

Leave guidance when `C < 0` (the low end was missed) or when this year's guidance has been revised. The base is then Consensus if one exists. Consensus used to score a print is the Consensus dated **before** that release. Consensus used as the forward total is the latest pull, with its as-of date, tagged `[E]`.

If `C < 0` and no Consensus exists, the base is calibrated top-down anyway, and flag it.

Single-point guidance (`more than $X`, `about $X`) does not have a `C`. Top-down is that point. Calibrated top-down is absent. The base is bottom-up, and the words are enforced: `more than $X` means the total stays at or above `X`; `about $X` means it stays inside a stated band. If the build violates the words, flag it and adjust.

No guidance at all: top-down and calibrated top-down are absent. There is no `C`. The base is Consensus if one exists, otherwise bottom-up. Say so in the `[C]` block, name the view used, and flag it in the assumptions list.

Show `C`, the low, the high, the actual, and which view is the base for revenue and for EBITDA. Tag that block `[C]`. The same block records the four views and the ratios.

### 2b. Turn words into numbers

Use [wording-table.md](references/wording-table.md). Absolute phrases map to a band. Relative phrases (`accelerating`, `momentum continues`) are read against that line's own prior-year growth.

The step size is a judgment from the adjective and the context. Tag it `[S]`, quote the sentence, and put it on the assumptions list. The step table in the reference is a set of starting defaults, not a conversion the quote has to survive.

Where a line splits price and volume, tag the phrase as a price effect (price, mix, rebates) or a volume effect (units, patients, procedures, customers). Forecast the two and multiply.

When management gives a size by rank, share, or another comparison, and a disclosed customer or line turns that comparison into dollars, the band is the magnitude. Put it on the explicit year the words point to. Score the base and the bull against it. A miss moves that product's allocation up to the band. The company total stays on Consensus, top-down, or calibrated top-down. A build below the band survives only when the volume evidence shows the dollars cannot be shipped in that year, and the write-up shows that cap. The bear may miss the band. A rank is not a note written after the build.

### 2c. Scale the lines to the total

Build the lines, then scale the unreported periods so they hit the base-case total from 2a. Actuals do not scale.

When Consensus, top-down, or calibrated top-down sets the total, say that the lines are scaled to it. Bottom-up is recorded under `views`. It stays beside the base case.

If the factor is more than 10% away from 1, the line commentary and the base-case total disagree. Flag it. The lines are then allocating a total they did not earn on their own.

Above about 1.25×, scaling revenue with costs held fixed inflates margins mechanically. Scale the variable costs too, or show the unscaled case beside the scaled one as a sensitivity.

An acquired line is not scaled to Consensus, because Consensus coverage of the deal is uncertain. See [driver-patterns.md](references/driver-patterns.md).

### 2d. Run rate

Start from the latest reported quarter. Search the whole history window, not only the latest print, for items the company flags as one-time. Remove a one-time item only when the company flags it. Say which quarters were adjusted. Before a beat or a miss touches the run rate, classify the driver as one-time or recurring, and say why.

M&A-related costs are the exception. Treat them as one-time unless the company says they continue. Integration costs tied to the deal may stay in the short-term run rate while the integration work is unfinished, and come out once that work is done. Say which quarters hold the integration costs and when they come out. Tag the end date `[S]` when the company does not give one.

*Example (insurance-auction businesses):* catastrophe or hurricane volume, such as CPRT's FY25 Helene/Milton volume, is one-time.

### 2e. Costs

Gross margin stays at the trailing level unless a source moves it. State the gross margin basis (GAAP or cash), and keep management's margin language on the same basis.

Define the cost base first. Cash opex = GAAP operating expenses − stock comp − depreciation (− company-flagged one-time items − M&A costs treated as one-time under 2d). Integration costs stay in that base only while the integration work is unfinished. Reconcile it to reported adjusted EBITDA: gross profit + amortization in COGS − cash opex = adjusted EBITDA (HROW Q2'26: 50.363 + 5.527 − 57.122 = −1.232). State where amortization and stock comp sit. Gross profit minus adjusted EBITDA is not the cost base: it nets amortization into opex and understates EBITDA.

When management describes how it gets to its EBITDA guide (HROW: "substantially higher revenue, increasing gross margins into the high 70s, and a base operating expense structure that remains approximately flat"), the cost step follows that description first. Only when there isn't one, cash operating cost is the latest-quarter run rate plus step changes the company has actually announced, grown for inflation.

When the company doesn't report adjusted EBITDA, state the definition as a calculation, e.g. operating income + D&A + stock comp, tagged `[C]`. Keep it consistent with any acquired company's own definition, and show the effect of including or excluding stock comp.

When a revenue Consensus exists but no EBITDA Consensus does, bottom-up EBITDA is the cost build above, and that build is the base. Flag it. Consensus EBITDA is absent.

If you have a calibrated top-down or Consensus EBITDA total, and the operating cost it implies differs from the bottom-up cost build by more than 10%, keep that total as the base, flag the gap, and record the cost-based figure as bottom-up.

### 2f. Where the explicit years stop

Stop when the specific evidence stops. That is usually two years.

Products still in development can move that stop. From the history window and the latest pipeline disclosure, list each one management names: what it is, the stated timing, and whether a dollar figure or a peak-sales figure was given. If none is named, say so in one line.

Leave the explicit years as they are when the base already covers the launch. Do not add pipeline revenue on top of top-down, calibrated top-down, or Consensus. Add explicit-year dollars only when the base is bottom-up, or when management says the guide or the estimates exclude the product, and a launch date falls inside the window. Those dollars sit inside the reported line that will hold them. A new line is used only when management already reports the product on its own. An unapproved product uses a probability, tagged `[S]` unless a source states it. An approved product that has not launched is phased from the stated launch date. Do not put peak sales or the full undiscounted amount in the base.

Extend the explicit window when the product's impact is well enough understood to write year by year: a timing, a basis for the dollars (a company figure, a stated ramp, or a probability times a stated amount), and the line that holds them. Say why the window moved. The same rule applies to the added years: do not add the product on top of a total that already includes it. Each added year still records the four views. Top-down and Consensus are absent when nobody published them, and the base for that year is bottom-up. `gsnext` then starts the year after the longer window.

When the impact is not that clear, leave the window at the usual stop. `gsnext` and `mc` take the pipeline in, together with the history window. `mc` moves when the new product's margin differs from the current mix. Tag `[S]`, name the product, cite the stated timing, and do not invent a dollar figure or a trend the company did not give. A product with no amount and no timing leaves `gsnext` and `mc` unchanged and is recorded as considered. `gsnext` is one more year of the same build as an explicit year. A phrase that reaches that next year is read against that line's own prior growth, the same way section 2b reads an explicit year. A phrase that stops at the last explicit year does not set the next year, and it does not set the line to zero. The line keeps the growth its history and the last explicit year already support. The write-up names where the phrase stopped. A rank or other comparison scored under 2b continues one more year on its own dollars and is included. It does not replace the other lines. Company `gsnext` is that next-year total divided by last explicit revenue, minus 1. It does not step down to a round rate nobody stated. Finagle fades `gsnext` toward terminal growth after that next year, and that fade is the later decline. A launch curve is not built product by product past `gsnext` unless the explicit window was extended. A separate risk, such as a contract renewal, may set the bear. It does not replace the implied growth in the base.

Write the growth of those dollars on `forecast.json` under `finagle`. That is the block the tests check. `sales_growth` and `ebitda_growth` are one rate per explicit year, and they compound back to the revenue and EBITDA you just wrote. `me` is the last explicit year's EBITDA divided by revenue. `mc` is the contribution margin. `gsnext` is sales growth in the year after the explicit window. Set `mc`, `gsnext`, and any other input past the explicit years against the history window, the transcript language, and any unlaunched product recorded above. Tag them `[S]`, cite the quarters, and do not invent a trend the series does not show. `me` and `mc` are not zero.

## 3. Pick a driver pattern

Use [driver-patterns.md](references/driver-patterns.md). One pattern per line, or a new line when the disclosure adds one. The pattern builds the bottom-up line; 2c still scales it to the base-case total. A royalty, license, or earn-out uses the pattern inside the reported line that already holds it. A product still in development uses ramping or milestone-dependent the same way, inside the line that will hold it. Section 2f says whether that product extends the explicit years.

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
