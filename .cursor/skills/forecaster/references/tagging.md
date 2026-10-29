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

## Currency

Forecast in the filer's reporting currency. Convert any input reported in another currency at a stated, cited rate, tagged `[C]` (or `[E]` for a market rate), with its as-of date. Flag the lines exposed to FX.

`[S]` and any other judgment go on the assumptions list so a person can change them without rereading the whole case.

Lines reconcile to totals. In `forecast.json` a fact is:

```json
{"value": 81.348, "tag": "A", "citation": {"text": "...", "url": "https://www.sec.gov/..."}}
```

No bare numbers. `pytest` walks the file and checks that, the line totals, and the growth and margin leaves.

## Numbered tags and the source list

Every tag carries an ID (A1, A2, G1, E1, S1, S2, C1, P1, D1) that points to a numbered source list at the end of `forecast.md` (and in the report's Appendix B).

- **D entries:** documents (publisher, title, date, URL; note "HTML; no page numbers" where relevant).
- **A/G/E entries:** the exact quote, the document ID, the page or slide (or `page unverified`), and the date. E entries also give the source and as-of date.
- **S entries:** the reasoning plus the quote it rests on, with page and link. Don't restate the number.
- **C entries:** the formula and the input IDs.
- **P entries:** what the prompt supplied.
- Reuse an ID when the same fact appears again. Anything without a verified link, page or date goes under "Not verified".

In `forecast.json` every citation carries `id` and `page` (or `page_status: "unverified"`), and the IDs resolve in a top-level `sources` list:

```json
{"value": 81.348, "tag": "A", "citation": {"id": "A1", "page": "p.8", "text": "...", "url": "https://www.sec.gov/..."}}
"sources": [{"id": "D1", "text": "..."}, {"id": "A1", "document": "D1", "page": "p.8", "text": "..."}, {"id": "C1", "inputs": ["A1", "A2"], "text": "A2 / A1 - 1"}]
```

`pytest` checks, when `sources` is present, that each ID names one fact, that every ID used in the lines and totals resolves in `sources`, that A/G/E entries carry the quoted `text`, and that C entries list existing input IDs. A case without `sources` passes with a warning; new cases should carry IDs.
