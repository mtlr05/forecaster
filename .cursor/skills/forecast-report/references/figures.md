# Figures

This file describes the displays by name. The forecast-report skill decides which ones a report uses, where they sit, and which are captioned figures. Numbering is that skill's rule. Changing a condition there does not change this file.

Use the number format in [the forecast-report skill](../SKILL.md).

## Shared format

A captioned figure has a caption `**Figure N – Title, period (units)**`. The caption carries the period span and the units. `N` is the number the skill assigns. A split of one display is labeled `(continued)` under the same number.

One sentence before the figure says what to take from it. The figure holds no second sentence.

An italic `*Source: ...*` line carries the tags and a short pointer. The method stays in the prose, the forecast file, and Appendix B.

## Estimate comparison

One figure, in two blocks: revenue, then EBITDA. Both blocks use the same columns, in this order: the previous-year baseline (the last actual fiscal year), the year-to-date actual, the estimated remainder, and the explicit years the skill selects. Period names come from the case.

Rows in each block, in this order: bottom-up, top-down low and high (or the single point), calibrated top-down, Consensus, and the base. Then each other view divided by that metric's base, bottom-up divided by calibrated top-down, and bottom-up divided by Consensus. A ratio is a 1-decimal percentage or a factor, and only when that ratio is already stored as `[C]`. Any other ratio cell is "n/a".

On the previous-year baseline and the year-to-date actual, the base row is the reported number. The view rows are "n/a" plus "reported actual", unless that view was recorded for the period. On the estimated remainder, the base row is the remainder. A view row is filled only when that view exists for the remainder. A missing view elsewhere is "n/a" plus the short reason (no range, no estimate, guidance left). View dollars come from `views` in the forecast file. The reported baseline, the year-to-date, and the remainder come from the reported and explicit figures in that file.

## Financial summary

The base case: revenue, growth, gross margin, EBITDA, EBITDA growth and margin. Columns are two actual years, the first two explicit years, and the last explicit year. When the last explicit year is already one of the first two, it appears once.

## Revenue by line

Revenue by line for the last full year, with each line's share of the total.

## Recent events

Dated events: deals, launches, approvals, guidance, financing, buybacks, legal.

## Evidence → judgements → forecast impact

One row per judgment that moves a base-case number. The row names the development, driver, or risk, the judgment it sets, and the effect on the base-case numbers.

## Reporting-line table

The title is the line name. A product that sits inside the line is a row. A volume path or a pool path is a row when that is how the line was built. Columns and year-range splits match Base case by line, including a continued block. For a new product launch, the first column is the launch year, and the later columns match Base case by line from that year forward. Years before the launch are omitted. Do not add a column of zeros. Rows are revenue and growth, then those inputs. Add cost and margin rows only when that line was modelled explicitly.

## Base case by line

Revenue by line, the total, growth, EBITDA and margin, for the actual years (including the latest partial period when it is used) and each forecast year.

## Cash opex and margin bridge

The same year path as Base case by line. Rows follow the build used: gross profit, each cash-opex component (core run rate, announced step-ups, launch or program costs, variable load), total cash opex, EBITDA, and margin. When an early year is built a different way, the bridge starts at the first year it covers.

## Cash opex and margin bridge, other case

For a bull or a bear whose cost build differs from the base. Rows follow the build used for that case. A component the case uses is a row. A row the case adds, such as the effect of a lever, is included. A base-bridge row the case does not use is omitted. A year of zeros before that case's build starts is omitted.

## Stub bridge

By line: the reported portion of the open year, the estimated remainder, the implied guidance window, and the gap. Company-level views stay on Estimate comparison.

## Quarterly grid

Printed quarters through the stub, and the stub total.

## Balance Sheet Adjustments

One row per item: the name, the amount, the timing, the probability, the discount, the present value, and any shares issued. An empty schedule has no table.

## Valuation inputs

Columns are Bull, Base, Bear, and Basis. Basis is valuation default, forecast-file input, stated assumption (tagged `[P]`), or judgment, and the row gets tags. Rows, in this order: cost of equity, cost of debt, tax rate, terminal growth, shares, price, debt and cash, starting margin, incremental margin (mc), next-period growth (gsnext), and the terminal WACC. A further input the result file carries, such as terminal return on invested capital or the debt policy, is a row in those same columns. The cash row and the shares row are the adjusted figures from Balance Sheet Adjustments.

## Medium-term organic growth, base case

One row per line, then the continued path, then the total. Columns are the last explicit year, the next year, and the change. The changes sum to the dollar increase, and that increase divided by last-explicit revenue is the growth rate, marked derived with a C tag. It stays on one page. "May not sum due to rounding."

## Medium-term organic growth, bull and bear

The same row layout as Medium-term organic growth, base case. One column group for each of the bull and the bear whose next-year line build is set out and differs from the base.

## Value bridge

For the bull, the base, and the bear: the present value of explicit-period cash flows, the terminal value and its share of the total, firm value, less debt, plus cash, equity value, and value per share vs. the current price (% upside or downside).

## Base-case year statement

The base-case statement from the valuation, from the last actual year through the end of the valuation horizon. A header block (ticker, price, shares, rates, terminal growth), then one column per year. The rows are the ones the result file contains. Print the valuation's values as output. A sign flip is a note. Split into continued blocks when one table would not fit on a page. A year-by-year table that does not fit in portrait uses a landscape page.

## Sensitivity

Value per share when one input moves at a time (cost of equity ±1 pt, mc ±10 pts, gsnext ±5 pts). The numbers come from that run's result file.

## Headline scenarios

From the forecast file only: revenue, EBITDA, and margin for the bull, the base, and the bear.

## Bull and bear line builds

Revenue by line for the lines that differ from the base, for the bull and for the bear, plus the total, EBITDA, and margin.
