# Tagging

Every number in `forecast.md` and in `forecast.json` carries one tag and a citation. The citation has the words you are relying on and a link. A filing link is the EDGAR or SEDAR+ document URL. A press release or transcript link is fine when that is the source. If you could not open the link, the citation text says `link unverified` and you do not pretend you did.

| Tag | Use it when |
|---|---|
| `[A]` | A reported actual. |
| `[G]` | Guidance or another management statement. Direct quote and the date. |
| `[E]` | An analyst estimate. Name the source and the as-of date. Consensus used to judge a reported period is the consensus from before that release. |
| `[P]` | The prompt supplied the figure or told you to override the method. The prompt wins. |
| `[S]` | An assumption. The citation says why: volume, price, a coverage win, destocking, a launch ramp. It does not restate the number. |
| `[C]` | Arithmetic from the method: a coefficient, a scale factor, a growth rate, a sum. Cite the inputs. |

`[S]` and any other judgment go on the assumptions list so a person can change them without rereading the whole case.

Lines reconcile to totals. In `forecast.json` a fact is:

```json
{"value": 81.348, "tag": "A", "citation": {"text": "...", "url": "https://www.sec.gov/..."}}
```

No bare numbers. `pytest` walks the file and checks that, the line totals, and the Finagle leaves.
