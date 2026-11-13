---
name: forecaster
description: Build an evidence-based revenue and EBITDA forecast for a public company, including the inputs a Finagle valuation reads. The explicit window is the longest of two years, the guidance horizon, and the Consensus horizon, unless the prompt states otherwise. On an update the window stays unless the prompt changes it. Use when forecasting a ticker, updating an existing forecast for a company update or a modelling refinement, or preparing a joint valuation.
---

# Forecaster

A way to build a revenue and EBITDA forecast, and the inputs a Finagle valuation reads. The same skill updates an existing case in `forecasts/<TICKER>/`, to take in a company update or a modelling refinement. On an update, start from that case's `forecast.md`, including its Status block, and follow the revision rules in section 4.

Finagle is the valuation model beside this repo. Every forecast writes the inputs it reads: the growth and margin leaves in section 2f, and the cash and share schedule in section 2g. A collaborative run sends them. Finagle runs only when the user asks for a joint valuation.

The explicit window is the longest of two years, the years management guidance covers, and the years Consensus estimates cover, unless the prompt states otherwise. On an update, keep the window already in the case unless the prompt changes it. Section 2f is that rule. Judgment is the work. The steps below are the default method, not a rulebook: a figure or an instruction in the prompt overrides them, and that override is tagged `[P]`.

Read the references when you reach that step. They hold the tables; this file holds the method.

- [Tagging](references/tagging.md)
- [Wording](references/wording-table.md)
- [Driver patterns](references/driver-patterns.md)

After the forecast, write the report with the [forecast-report skill](../forecast-report/SKILL.md).

Worked case: [forecasts/HROW](../../../forecasts/HROW/forecast.md). Layout: [AGENTS.md](../../../AGENTS.md).

## How to build a forecast

Read, in this order. Do not write outside this repo.

1. The prompt.
2. The company's filings for at least the last nine reported quarters. For a US issuer those are on EDGAR. For a Canadian issuer they are on SEDAR+. Also read the company's own IR pages.

Those documents are the financial reports, the earnings press releases, the earnings call transcripts, and any shareholder letter. From them, take revenue, and EBITDA or margin where the company reports it, for each of those quarters. EBITDA is the company's adjusted EBITDA when it reports one. Section 2e is the definition. That series is the baseline and the year-over-year growth.

Name the window (for example Q2 FY24 through Q2 FY26). The baseline year, year 0, is always the last fiscal year. Year-over-year growth is year 0 relative to year -1, the fiscal year before it. When a quarter has no call, say so. A missing call does not shorten the window. A shorter history (a new issuer, restated segments, or a quarter with none of those documents) is used as-is and flagged.

Consensus, when estimates exist, is a separate pull. It is not in the filings. Section 2 records it.

Reported results frame section 1: the baseline figures, the year-over-year growth, the historical trend, and the narrative. The same history is what the run rate and one-time items (2d), the cost base (2e), and `mc` and `gsnext` (2f) are checked against. Forward-looking statements and the company outlook, in the press releases, the transcripts, and management's discussion and analysis, set the explicit-year totals and the wording in section 2.

A number you cannot open stays out, or goes in with the citation text `link unverified`. Do not invent a URL or a figure.

## What you produce

For `forecasts/<TICKER>/`:

- `forecast.md`, the case a person can read
- `forecast.json`, the case the tests check
- `report.md` and `report.pdf`, the analyst-style update
- `revision_log.md`, one row per line for this year and next year, on every update

`forecast.json` has to pass `pytest`. Periods are named `FYyyA`/`FYyyE` for fiscal years and `H1A`, `H2E`, `9MA`, `Q4E` and the like for part years; `baseline_period` and `explicit_periods` set which years the checks run on. Growth keys are `YoY` or `YoY_*`. A lone reference quarter such as `Q4FY26A` (the latest quarter) is summed across lines but not to a year. Part years sum to the first explicit year unless `stub_of` maps them (e.g. `{"H1E": "FY27E", "H2E": "FY27E"}`). A line's `pattern`, when given, is one of the [driver patterns](references/driver-patterns.md) in lower case, optionally followed by a note in parentheses. Every number is a fact: a value, a tag, and a citation. See [tagging](references/tagging.md).

New cases also carry a `views` block: bottom-up, top-down, calibrated top-down, and Consensus, for revenue and for EBITDA, for each explicit year, plus which view is the base for each metric and the ratios between them. The shape is in section 2. A case without `views` passes with a warning.

New cases also carry a `cash_share_adjustments` block: milestone payments the company owes other parties, similar contingent cash outside EBITDA, and equity offerings. An empty base list means none were found. The shape is in section 2g. A case without the block passes with a warning.

## Status and open items

`forecast.md` can open with a short `## Status and open items` block. It replaces a separate status note.

- When a task names a ticker, read `forecasts/<TICKER>/forecast.md` first, starting with its Status block if it has one.
- The block holds only the open items, the current version and values, and how to resume (which scripts rebuild what, and their inputs). Assumptions and reasoning stay in the report and the rest of `forecast.md`; point to their sections, do not restate them.
- Update the block at each agreed change of a decision, a value or an open item. A value change also gets a `revision_log.md` row.
- Create the block when a ticker's work first has open items, or a resume procedure that `forecast.md` does not already give.

## 1. Frame the forecast

The reported history sets the baseline, the year-over-year growth, the trend, and the narrative. Reported periods stay put. Forecast only periods the company has not reported.

A business line is a unit the company already reports revenue for, and margin if it reports that too: a segment, a product, an operating business, a geography, a channel. Do not split finer than the disclosure. A single-segment filer's lines are the revenue breakdown it reports: geography, revenue type (e.g. service vs. vehicle sales), or both crossed if both are reported. Say which one you used.

A launch, a new product, or an acquisition stays inside the reported line management frames it as part of. It is its own line when management already reports it that way, or when the disclosure of the deal adds one. Size alone does not make a line. Section 2e gives the line its cost. Section 2f says whether the dollars sit inside a total that already includes them.

Royalties, license revenue, earn-outs, and similar contingent payments stay inside the reported line that already includes them. A contingent item is its own line only when management already reports it as its own line. Build the operating piece and the contingent piece, then one line total. See [driver patterns](references/driver-patterns.md). If those dollars already sit in the reported line, in guidance, or in Consensus, leave them there: they are an allocation inside the line when the base is top-down, calibrated top-down, or Consensus, and they are not added again on top of that total. When the dollars cannot be split out, keep the single line, say the piece is not separable, and state how the build treats it: in the run rate, probability-weighted, or already inside the total. A payment the company owes another party, and an equity offering, are not revenue. Section 2g records them.

The baseline year, year 0, is the last fiscal year. It shows year-over-year growth for the total and for each line, year 0 relative to year -1.

Lines add up to the total. If they do not, fix the lines before scaling anything.

Bear, base, and bull differ in two or three levers, named up front. They do not each invent a new story.

## 2. Set the totals, then the lines

The outlook and other forward-looking statements, in the press releases, the transcripts, and management's discussion and analysis, set the wording, and they set the total for a year that has a calibrated top-down. Consensus, when it exists, is a separate pull and sets the total when calibrated top-down is absent. A year with neither is bottom-up. The run rate, the cost base, and the inputs past the explicit years are checked against the reported history.

Four views are recorded for revenue and for EBITDA, for each explicit year, including the one chosen as the base. A view that does not exist is recorded as absent, with the reason.

- **Bottom-up.** Revenue is the sum of the unscaled lines. EBITDA is the cost build in 2e, unless the filing reports line profits that already sum to it.
- **Top-down.** Management's guidance range for that year: low and high. A single point (`more than $X`, `about $X`) is recorded as a point, and calibrated top-down is absent because there is no `C`.
- **Calibrated top-down.** `Low + C * (High - Low)` on the like-for-like range. Absent, with the reason, when there is no range, when `C` is not applied, or when this step says to leave guidance. `C` is not applied when `C < 0` and a Consensus exists, when guidance has been revised, or when there is no completed original range. When `C < 0` and no Consensus exists, apply `C` anyway: calibrated top-down is then the base, and it is flagged.
- **Consensus.** Analyst estimates, the latest pull, tagged `[E]`. Record `analysts` (the count on the pull) and `as_of` (the pull date) on the fact. If `analysts` is 1, or `as_of` is missing, flag it in the `[C]` block and on the assumptions list. The figure can still be the base. Absent when none exists.

The base is chosen separately for revenue and for EBITDA, and separately for each explicit year. Calibrated top-down when that view exists. Consensus when it does not and an estimate exists. Bottom-up when neither exists. Bottom-up stays a recorded view beside that base. The dollars on `lines` are the scaled base-case dollars.

Do this separately for revenue and for EBITDA. A year with no guidance range has top-down and calibrated top-down absent. Its base is then Consensus if that year has an estimate, otherwise bottom-up.

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

Single-point guidance (`more than $X`, `about $X`) does not have a `C`. Top-down is that point. Calibrated top-down is absent. The base is Consensus if one exists, otherwise bottom-up. The words are enforced on that base: `more than $X` means the total stays at or above `X`; `about $X` means it stays inside a stated band. If the base violates the words, flag it and adjust.

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

EBITDA is the company's adjusted EBITDA when it reports one. Reconcile the cash cost to that figure. Show a gap, including the effect of including or excluding stock comp. When the company does not report adjusted EBITDA, state the definition as a calculation with the same items the cash cost removes: operating income + D&A + stock comp + one-time items, tagged `[C]`. Keep it consistent with any acquired company's own definition.

Adjusted EBITDA equals revenue minus cash cost. State which basis is used, and use it for the history, for management's margin language, and for the forecast. Stock comp is SBC.

1. GAAP COGS + GAAP opex − D&A − stock comp − one-time items. D&A and stock comp come out wherever the company records them, in COGS or in opex.
2. When the disclosure is sufficient, cash COGS + cash opex. D&A, stock comp, and one-time items are already out of the cash lines. Reported D&A, stock comp, and one-time items equal the amounts removed to get from the GAAP lines to cash COGS and cash opex.

One-time items are items the company flags and M&A costs treated as one-time under 2d. Integration costs stay in cash cost while the integration work is unfinished, and come out once that work is done.

*Example.* Revenue 100, GAAP COGS 40, of which D&A is 5, GAAP opex 30, of which stock comp is 3 and a company-flagged one-time item is 2. Cash cost on basis 1 is 40 + 30 − 5 − 3 − 2 = 60. Adjusted EBITDA is 100 − 60 = 40.

The description that governs the bottom-up cost build is the one that belongs to the current guide. Language that described a withdrawn guide is not applied unless management restates it for the current guide. The base for the year is still calibrated top-down, then Consensus, then bottom-up.

When management describes how it gets to its EBITDA guide (for example higher revenue, a higher gross margin, and an operating-expense base that stays about flat), the bottom-up cost step follows that description first.

When there is no such description, split the cash operating-expense piece into a core piece and a variable piece. The core piece is the latest-quarter cash run rate, annualized, plus step changes the company has actually announced, grown for inflation. The inflation rate is a rate the company states, or else a named rate tagged `[S]` with its source. The variable piece is a rate times the revenue base's increment over the annualized revenue of that same quarter. The core run rate already pays for that quarter's revenue pace. Year 0 stays the baseline for year-over-year growth. Exclude lines whose incremental cost is already in the core piece or in cash COGS: a disclosed incremental opex add-on, an explicit launch program, or a profit-share or royalty. The rate comes from the history window where incremental cash opex, after those same exclusions, can be measured. When it cannot, state a central rate and a band, tagged `[S]`, and use the central rate in the base. Do not apply the variable rate to a line that already has a dedicated program or a cash-COGS take.

A launch, a new product, or a newly acquired line inside the explicit window is not given a cost of zero because the company did not quantify it. Add an explicit program, tagged `[S]`, with a basis (a company comment on the existing team or footprint, a comparator, or a stated add-on) and a band. The central figure is the one in the base. Do not invent a second sales force when management says the existing team will carry the product. Do not double-count costs already in the run rate. An acquired line's program cost stays with that line and is not scaled to Consensus, as section 2c already says for its revenue.

Gross margin stays at the trailing level unless a source moves it, on the stated basis. Mix, a disclosed product or segment margin, and a stated cost take are sources that can move it. When one of those exists, consolidated gross margin is the weighted build on the stated basis. When a royalty, a profit-share, or a similar take is known to exist but the rate is not disclosed, state a central rate and a band, tagged `[S]`, and name any comparator. The base uses the central rate. A target phrase sets the margin only when it still describes the current guide.

When the explicit window is longer than two years, keep applying the same cost build each year. A rising or falling margin is the result of that build. If a later year's bottom-up EBITDA margin moves well beyond the history window and beyond any margin management has described, flag it, show the bridge, and put the downside in the bear as one of the named levers. Do not haircut the bottom-up build just to keep its margin inside the historical range. A calibrated top-down or Consensus EBITDA total remains the base under the 10% rule.

When a revenue Consensus exists but no EBITDA Consensus does, EBITDA equals that revenue base minus the cash cost of the same revenue. The variable piece and the core piece above are applied to this revenue base. They are not scaled a second time. The margin is that EBITDA divided by the revenue base. The unscaled cost build remains the bottom-up view. Flag it. Consensus EBITDA is absent. An unscaled cash cost, or unscaled EBITDA dollars, set against a different revenue is not that margin. Section 2c states the same rule when revenue is scaled and costs are held fixed.

If you have a calibrated top-down or Consensus EBITDA total, and the cash cost it implies differs from the bottom-up cash cost of that same revenue by more than 10%, keep that total as the base, flag the gap, and record the cost-based figure as bottom-up. The comparison uses one revenue figure.

### 2f. Where the explicit years stop

The explicit window is the longest of three horizons, unless the prompt states a different one, tagged `[P]`. The three are two years, the years management guidance covers, and the years Consensus estimates cover. Count a year when either revenue or EBITDA has that guidance or that estimate. On an update, keep the explicit window already in the case unless the prompt changes it. A new guide, a longer or shorter Consensus, or a product launch date does not move it.

A product does not lengthen the window. From the history window and the latest pipeline disclosure, list each one management names: what it is, the stated timing, and whether a dollar figure or a peak-sales figure was given. If none is named, say so in one line.

Leave the product inside the line when the base already covers the launch. Do not add pipeline revenue on top of calibrated top-down or Consensus. Add explicit-year dollars only when the base is bottom-up, or when management says the guide or the estimates exclude the product and a launch date falls inside the window. When those dollars are added because the published total excludes them, the base for that year is bottom-up, and the published view stays recorded beside it. Those dollars sit inside the reported line that will hold them. Section 1 says whether the product or the deal is its own line. An unapproved product uses a probability, tagged `[S]` unless a source states it. An approved product that has not launched is phased from the stated launch date. Do not put peak sales or the full undiscounted amount in the base.

When the prompt sets a longer window, each added year records the four views and uses the same base order. `gsnext` starts the year after the window.

`gsnext` and `mc` take the pipeline in, together with the history window. `mc` moves when the new product's margin differs from the current mix. Tag `[S]`, name the product, cite the stated timing, and do not invent a dollar figure or a trend the company did not give. A product with no amount and no timing leaves `gsnext` and `mc` unchanged and is recorded as considered. `gsnext` is one more year of the same build as an explicit year. A phrase that reaches that next year is read against that line's own prior growth, the same way section 2b reads an explicit year. A phrase that stops at the last explicit year does not set the next year, and it does not set the line to zero. The line keeps the growth its history and the last explicit year already support. The write-up names where the phrase stopped. A rank or other comparison scored under 2b continues one more year on its own dollars and is included. It does not replace the other lines. Company `gsnext` is that next-year total divided by last explicit revenue, minus 1. It does not step down to a round rate nobody stated. Finagle fades `gsnext` toward terminal growth after that next year, and that fade is the later decline. A launch curve is not built product by product past `gsnext`. The prompt is what lengthens the window. A separate risk, such as a contract renewal, may set the bear. It does not replace the implied growth in the base.

Write the growth of those dollars on `forecast.json` under `finagle`. That is the block the tests check. `sales_growth` and `ebitda_growth` are one rate per explicit year, and they compound back to the revenue and EBITDA you just wrote. `me` is the last explicit year's EBITDA divided by revenue. `mc` is the contribution margin. `gsnext` is sales growth in the year after the explicit window. Set `mc`, `gsnext`, and any other input past the explicit years against the history window, the transcript language, and any unlaunched product recorded above. Tag them `[S]`, cite the quarters, and do not invent a trend the series does not show. `me` and `mc` are not zero.

### 2g. Cash and share adjustments

Record milestone payments the company owes other parties, similar contingent cash that sits outside EBITDA, and equity offerings. Royalties, license revenue, and earn-outs that stay inside a reported line are not listed again. Cash already inside the year-0 balance is not listed. These items do not enter revenue, EBITDA, a later cash-flow year, or a later share path.

`forecast.md` lists each item. `forecast.json` holds them under `cash_share_adjustments`. The block is an object of scenarios. `base` is a list. An empty list means none were found. Bull and bear have their own list when the probability or the amount differs. A missing scenario uses the base list.

Each item is tagged facts, in millions of the reporting currency and millions of shares. `kind` is `cash` or `equity`. `name` says what it is. `when` is an ISO date. A source that gives only a year uses that fiscal year-end, tagged `[S]`. `probability` is `[S]` unless a source states it. A contracted item with no contingency is 1. Do not haircut the cash a second time. A cash item has a signed `amount`. A payment to another party is negative. An equity item has `shares`, or `proceeds`, or both. Omit `price` when the shares are issued at today's price. A filing price or a price the user states is a fact on the item.

```json
"cash_share_adjustments": {
  "base": [
    {
      "kind": "cash",
      "name": "milestone payable to Partner",
      "when": {"value": "2028-06-30", "tag": "G", "citation": {"text": "...", "url": "..."}},
      "probability": {"value": 0.5, "tag": "S", "citation": {"text": "...", "url": "..."}},
      "amount": {"value": -25.0, "tag": "G", "citation": {"text": "...", "url": "..."}}
    }
  ]
}
```

On a joint valuation the runner discounts each item at Finagle's cost of equity, the required return on equity, and adds the present value to year-0 cash. New shares, multiplied by the probability, are added to the current share count. The issue price is today's price unless the item states one. Proceeds equal shares times that price, or shares equal proceeds divided by that price. The forecast file stores the undiscounted schedule. The worked figures live in the valuation result.

Put the probability, a year-end date the source did not give, and an issue price that is not today's price on the assumptions list.

## 3. Pick a driver pattern

Use [driver-patterns.md](references/driver-patterns.md). One pattern per line, or a new line when the disclosure adds one. The pattern builds the bottom-up line; 2c still scales it to the base-case total. A royalty, license, or earn-out uses the pattern inside the reported line that already holds it. A product still in development uses ramping or milestone-dependent the same way, inside the line that will hold it. Section 2f places the product inside the explicit window when the launch falls there. The product does not lengthen the window.

Choose from what management discusses, then the simplest pattern that fits the history.

## 4. Write down what a person should change

End every case with an assumptions list:

- the three to five moves that actually change the answer
- every `[S]` and every other judgment tag
- the probability, the date, and the issue price on each cash or share adjustment

Each entry says what to revise. A driver explains why (volume, price, a coverage win, destocking), not the number over again.

On an update, keep the explicit window already in the case unless the prompt changes it. First check EDGAR or SEDAR+ for filings since the last revision, and record the consensus pull date and source in the file. Then add a revision-log row per line for this year and next year: old, new, change, one line of why, including the growth rate old to new. Store it in `forecasts/<TICKER>/revision_log.md`.

## 5. Check

`pytest` from the repo root. The HROW forecast is the case that has to pass.

## Collaborative run

Only when the user asks for a joint valuation. Follow [collaborative-run.md](references/collaborative-run.md). Copy the user's `prompt_inputs` into the request unchanged. Copy `cash_share_adjustments` from the forecast. Add nothing the user did not state. The published value is the one in the result file. Write the valuation section of the report from that file. Apply a post-run factor only when the request has one, and show the raw and adjusted values side by side, tagged `[P]` with the user's date.

## Sources and credit

Four practices were adapted from [anthropics/financial-services](https://github.com/anthropics/financial-services) (Apache-2.0), and restated here rather than copied:

- a revision table, from the model-update skill
- consensus dated before the release, from the earnings-analysis workflow
- classifying a beat or miss as one-time or sustainable before it changes the forecast, from earnings-analysis step 5
- a driver explains why, not what, from the fund-admin variance-commentary skill

See `NOTICE`.
