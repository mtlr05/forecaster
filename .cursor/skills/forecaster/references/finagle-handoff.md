# Finagle handoff

Checked against [finagle](https://github.com/mtlr05/finagle) commit `bb39642` (2026-10-14). Finagle is read-only. If that repo has moved, re-read the functions below before you change this contract. Do not edit Finagle to make a case run.

A value per share comes only from `run_case`. Do not compute one beside it.

## Order

1. `describe_inputs()` in `finagle/agent/catalog.py`. It is the field list.
2. `build_baseline(...)` in `finagle/agent/sources.py`.
3. Leaves the forecaster fills (below).
4. Leaves the user fills from [templates/case_template.json](../../../templates/case_template.json).
5. `validate_case`. `missing` has to be empty. Errors are empty too. Warnings can remain if you report them.
6. `run_case`.

An update is `update_case(case, updates)` with only the leaves that changed. Do not call `build_baseline` again.

`build_baseline` takes the first source that has each year-0 field (`schema.py` `BASELINE_PRIORITY`): prompt, article, attachments, SEC 10-K, yfinance. It also fills price, shares, the risk-free rate, and, when nobody set them, `re` (risk-free + 0.055), `gt` (the risk-free rate), and `roict` (0.15). See `defaults.py` `_yield_and_rates`. You still do not set `gt` yourself. If the prompt sets it, that is the user's leaf, not a forecast output.

## What the forecaster must supply

Refuse to hand off if any of these is missing. On a prior HROW case, dropping `margin_path` entirely changed `run_case` from $56.69 to $171.62. This repo did not re-run that case. The mechanism is in the code: `compile.py` adds `me`, `mc`, and `gsnext` to `forecast_ebitda` only when `margin_path` is present (`_compile_ebitda`). `company.py` `forecast_ebitda` then either follows the margin path or, in the other branch, writes revenue as 0 and grows EBITDA with `gf` faded toward `gt` for the whole horizon. `me` and `mc` of 0 are treated as unset (`if mc and me`).

| Leaf | What it is |
|---|---|
| `forecast.ebitda_growth` | Organic EBITDA growth for each explicit year. This is `gf`. Do not also set `forecast.ebitda`. |
| `forecast.sales_growth` | Organic sales growth for the same years. |
| `forecast.margin_path.me` | The margin the explicit window ends on. |
| `forecast.margin_path.mc` | Contribution margin. Non-zero. Justify it against history. |
| `forecast.margin_path.gsnext` | Sales growth in the first year after the explicit EBITDA growth. |
| `forecast.ebitda_basis` | `organic` when any deal closes after year 0. `total` only if there is no future deal. |
| `forecast.acquisition_disclosure.status` | `future_deals` or `none`. |
| `forecast.acquisition_disclosure.deal_spend` | Enterprise value by year. Index 0 is the baseline year. A year-1 deal is `[0, deal]`, not `[deal]`. |
| `acquisitions[]` | One object per deal, all seven fields below. |

`sales_growth` and `ebitda_growth` have to describe the same organic dollars. `compile.py` `_handoff_margin` replaces `me` with ending EBITDA divided by ending revenue when the sales path reaches the last explicit year (`_revenue_prefix` compounds `sales_growth` onto year-0 revenue). Set `me` to that ratio so the leaf and the argument `forecast_ebitda` receives are the same number. Year-0 EBITDA/revenue is the wrong `me` once you have an explicit path.

`gsnext` has to be set even though Finagle will guess. `defaults.py` `_next_sales_growth` copies the last sales growth, or `gt` if it cannot. Leaving it blank does not fade anything.

`mc` has to be set for the same reason. The filler in `_margins` averages the **year-0** EBITDA margin with gross margin. That is not the ending margin you want the fade to use.

## The seven acquisition fields

`year`, `deal_value`, `multiple`, `leverage`, `next_growth`, `capex_frac`, `pay_from_cash`.

`compile.py` `_acquisition_steps` requires those (plus a way to size EBITDA: `deal_value` and `multiple`, or acquired EBITDA). `pay_from_cash` only reduces year-0 cash. A deal that closes in year 1 is `false` even when the company paid cash at closing. `catalog.py` `_fields()` describes the same leaves.

Organic EBITDA in `ebitda_growth` excludes these deals. Booking the EBITDA in the path and again in `acquisitions` double-counts it (`catalog.py` `do_not`).

## What the user fills

Not forecast outputs. Placeholders live in `templates/case_template.json` with no values attached.

- `year`
- `rates.rd`
- `rates.t`
- `baseline.nol`
- `baseline.noa`
- `forecast.dwc.mode`
- `distribution.mode`
- `debt.mode`
- `rates.gt`

`debt.mode` is a real choice. If it is omitted, `defaults.py` `_leverage` sets `target` at the year-0 debt/EBITDA from year 1, which re-borrows as EBITDA grows. On the prior HROW run that default was worth about $12 a share versus holding debt flat ($56.52 against $44.05). Not re-run here. Pick hold, path, or target on purpose.

`rates.gt` stays with Finagle or with the user. The forecaster does not set it.
