# Driver patterns

Apply one pattern to a reported line, or add a line when the disclosure adds one. The pattern produces the unscaled build. Section 2c of the skill still scales that build to the total.

Pick the pattern management actually discusses. Then take the simplest one that fits the history. Do not import a pattern from a different industry because the product looks familiar. The examples below are illustrations of the pattern, not extra rules.

## Ramping

A line that is still being built: a recently launched product, a product that is approved but not yet launched, a coverage win that is not yet in a full year, a region that just opened.

Phase a product that has not launched from the stated launch date. Do not hold the first-year growth as a run rate. Use volume times price when you have both. Otherwise grow off the latest quarter and assume a slowdown, tagged `[S]`, because a new line rarely keeps its first-year growth. Watch a price change and a channel-inventory swing before you annualize a quarter. Inventory rebuild is not demand. If those dollars already sit in the line, in guidance, or in Consensus, they are an allocation inside that total, not a second amount. Section 2f of the skill places the product inside the explicit years when the launch falls there. The product does not lengthen the window.

## New or acquired

Management gave an amount or a floor (`more than $X`) and a start date. Phase it from the close or the launch. A floor is a floor, not a midpoint. Keep an acquired line out of the organic path when the deal is listed separately under `acquisitions`.

Record an acquired line in a standard block on the line in `forecast.json`, with synergies kept separate:

```json
"acquired": {
  "close_date": "2026-10-16",
  "stub_fraction": {"value": "<fraction, e.g. 0.21>", "tag": "C", "citation": {"text": "days from close to fiscal year end / days in the year", "url": "..."}},
  "target_source": {"text": "target's own guidance or consensus, as-of date", "url": "..."},
  "synergies": {"text": "separate from the target's revenue; none unless announced"}
}
```

Consensus scaling (skill 2c) does not apply to the acquired line, because consensus coverage of the deal is uncertain. Flag a target consensus that may be stale after the target delisted.

## Mature or declining

Flat at the latest-quarter run rate, or the recent trend, plus only the structural changes management names (a lost contract, a discontinued SKU, a price reset). Do not mean-revert a decline just because it looks tired.

## Milestone-dependent

A product still awaiting approval, a trial readout, or another stated event uses this pattern. Revenue equals the event amount times a probability. The probability is `[S]` unless a source states it. Do not put the full amount in the base because the event would be nice. If those dollars already sit in the line, in guidance, or in Consensus, they are an allocation inside that total, not a second amount. Section 2f of the skill places the product inside the explicit years when the launch falls there. The product does not lengthen the window.

## Acquisition-driven

Show organic revenue and the deal separately. Record the deal spend, the year, and what the organic path excludes. Do not hide the deal inside a growth rate and also list it under `acquisitions`. M&A-related costs are one-time unless the company says they continue. Integration costs stay in the short-term cost base only while the integration work is unfinished, and come out once it is done. Section 2d of the skill is the rule.

## Recurring

Starting base times retention, plus new bookings. Retention and the booking ramp are `[S]` or `[G]`, and they say whether the driver is customers kept or customers added.

## Contingent consideration

Royalties, license revenue, earn-outs, and similar payments stay inside the reported line that already includes them. The item is its own line only when management already reports it that way.

A running royalty or license uses `recurring`. An earn-out or milestone uses `milestone-dependent`. The probability is `[S]` unless a source states it. Do not put the full undiscounted contingent amount in the base. Build the operating piece and the contingent piece, then one line total.

If the dollars already sit in the reported line, in guidance, or in Consensus, they stay in that total. When the base is top-down, calibrated top-down, or Consensus, the contingent piece is an allocation inside the line. When the dollars cannot be split out, keep the single line, say the piece is not separable, and state how the build treats it: in the run rate, probability-weighted, or already inside the total.

A milestone the company pays another party, and similar contingent cash outside EBITDA, is not a revenue line. An equity offering is not a revenue line. Section 2g of the skill records those items. They are not built again here.
