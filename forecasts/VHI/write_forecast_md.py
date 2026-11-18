"""Write forecast.md (v3) from forecast.json and work/numbers.json."""
import json
from pathlib import Path
H = Path(__file__).parent
d = json.load(open(H / 'forecast.json')); n = json.load(open(H / 'work' / 'numbers.json'))
src = d['sources']; L = n['L']; Y = ['Q4E', 'FY26E', 'FY27E', 'FY28E', 'FY29E']
f = lambda x: '%.3f' % x
lines = [('Term licences, maintenance and support', 'term', '85.443', '57.070'), ('Virtual care (Attend Anywhere)', 'vc', '5.185', '0.000'), ('Perpetual licences', 'perp', '2.089', '0.498'), ('Services, hardware and other', 'svc', '16.250', '11.026')]
nine = {'term': '74.253', 'vc': '7.019', 'perp': '1.944', 'svc': '12.341'}
rows = '\n'.join(f"| {nm} | {a24} | {a25} | {nine[k]} | {f(L[k]['Q4E'])} | {f(L[k]['FY26E'])} | {f(L[k]['FY27E'])} | {f(L[k]['FY28E'])} | {f(L[k]['FY29E'])} |" for nm, k, a25, a24 in lines)
R = n['rev_base']; E = n['ebitda_base']
def sc(c, key): return ' / '.join('%.2f' % n['SC'][c][key][y] for y in Y[1:])
groups = [('Documents', 'D'), ('Actuals', 'A'), ('Guidance and management statements', 'G'), ('Estimates', 'E'), ('Assumptions', 'S'), ('Calculations', 'C'), ('Prompt', 'P')]
def srcs():
    out = []
    for title, ch in groups:
        out.append(f'\n### {title}\n')
        for s in src:
            if s['id'][0] == ch:
                ex = []
                if s.get('document'): ex.append(s['document'])
                if s.get('page') and ch not in 'DCSP': ex.append(s['page'])
                if s.get('url') and ch == 'D': ex.append(s['url'])
                if s.get('inputs'): ex.append('inputs: ' + ', '.join(s['inputs']))
                out.append(f"- **{s['id']}** {s['text']}" + (f" ({'; '.join(ex)})" if ex else ''))
    return '\n'.join(out)
md = f"""# Vitalhub Corp. (TSX: VHI)

## Status and open items

Version: **v3, 18 November 2026, 12:55 ET** (America/Toronto). v3 forecasts organic ARR additions in dollars after a review of the ARR bridge trend, prompted by the CEO bot's term-licence product sheet [D24] at David May's request [P8]. v2 (17 Nov, 10:05 ET) added the 2027 SHREWD roll-off after the FDP extension to March 2029 [D23][G26][P7]. v1 and v2 are archived in `v1/` and `v2/`; the change log is `revision_log.md`. Forecaster method commit 3a46f0a61f6b26de1a588acbc941120420d2ec41 (fetched again for v3: already up to date). Source mirror: read-only clone of mtlr05/ceochat at 25246c9 (pulled 18 Nov), companies/vhi/ only; every filing number re-checked against the original SEDAR PDF (via OTC Markets). Valuation: the Finagle bot ran the collaborative valuation on 18 Nov 2026 (finagle-run/valuation_result_v05.json, Finagle 377f177b) with David's stated inputs (P10-P15, including year-0 Adjusted EBITDA 26.554); value per share base C$9.226, bull 11.216, bear 6.827 vs C$6.73 (Yahoo, 18 Nov 2026) [C41]. v01-v03 stopped; v04 superseded (Yahoo year-0 EBITDA). The Forecaster wrote the request and the report section only.

Explicit window FY2026E–FY2029E [P1]; year 0 is FY2025A. **Currency: C$ millions** [P4]. Base FY2026E revenue 129 and Adjusted EBITDA 34.0; FY2029E revenue {R['FY29E']:.1f} and Adjusted EBITDA {E['FY29E']:.1f} ({100*E['FY29E']/R['FY29E']:.1f}% margin).

Open items:
- SHREWD (NHS England, 7–8% of ARR, about 7.5–8.6) [G2][C31]. Base: 4.0 rolls off straight-line in 2027, none after [S26]. Bull 1.5, bear 8.0 [S22].
- Consensus (FactSet via Markets Insider, pulled 17 Nov 2026) is taken to predate the 16 Nov announcement. The base is Consensus plus the SHREWD roll-off effect alone, measured on the v3 build with and without the loss (C36); the raw FactSet figure is kept under `unadjusted` in each total. Whole numbers, no analyst count (8 validator warnings).
- FY2029 base margin {100*E['FY29E']/R['FY29E']:.1f}% is above every reported year (FY2024 26.0%, FY2025 24.4%, best quarter 27.6% in Q3 2024); flagged and banded by the bear (24.9%) [P2]. Bottom-up FY2029 EBITDA is 10.3% below the base (0.897), flagged.
- FDP re-procurement (from H2 2027, about 18 months) is upside outside the window and in no case [S28][G27].
- Questions for Dan Matlow (not sent; David relays): how much SHREWD ARR is already removed from the 107.2; which SHREWD modules overlap FDP; whether Vitalhub will bid in the new FDP procurement or the maternity work; net revenue retention; currency mix of ARR; organic growth of acquired books since close vs the legacy book; why term revenue / average ARR fell from about 1.05 to 0.985 after 2024.

Tests: `forecast.json` passes `forecastcheck.validate_payload` (0 errors, 8 warnings: consensus analyst count not recorded). Rebuild with `python3 build_forecast.py`. Every number carries a tag under **Numbered sources**; page numbers are PDF pages.

## Lines

Single operating segment; four reported revenue types that add to total revenue [A3_1][A4_1][A5_1][A1_1]. Buddy (closed 10 Jul 2026) sits inside the term line at its acquired 4.48 of ARR, unscaled [S17][A28_4]. SHREWD sits inside the term line (and the services that ride on it).

## Base forecast

| Line | FY24A | FY25A | 9M26A | Q4 26E | FY26E | FY27E | FY28E | FY29E |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
{rows}
| **Revenue** | **68.594** [A1] | **108.967** [A1_1] | **95.557** [A1_2] | **33.443** [C5] | **129** [E1] | **{R['FY27E']:.3f}** [C36] | **{R['FY28E']:.3f}** [C36] | **{R['FY29E']:.3f}** [C36] |
| **Adj. EBITDA** | **17.840** [A2] | **26.554** [A2_1] | **24.773** [A2_2] | **9.227** | **34** [E2] | **{E['FY27E']:.3f}** [C36] | **{E['FY28E']:.3f}** [C36] | **{E['FY29E']:.3f}** [C36] |
| Margin | 26.0% | 24.4% | 25.9% | 27.6% | 26.4% | {100*E['FY27E']/R['FY27E']:.1f}% | {100*E['FY28E']/R['FY28E']:.1f}% | {100*E['FY29E']/R['FY29E']:.1f}% |

Growth: revenue +18.4% / +6.0% / +4.2% / +13.3%; Adjusted EBITDA +28.0% / +9.3% / +11.2% / +16.9% [C22][C23]. The FY2028 dip and FY2029 jump come from the FactSet path (+7.8% / +5.8% / +12.9%) [C34].

## Totals (four views)

- **No guidance.** The Q2 2026 10%–11% organic comfort [G13] was not restated on the Q3 call and is treated as withdrawn. Top-down and calibrated top-down are absent; the base is Consensus [E1][E2].
- **Post-pull event.** The skill has no explicit rule for news after the Consensus pull; its preamble lets a prompt instruction override the default method, tagged [P]. David's instruction [P7] plus the FDP extension [D23] is applied as an additive adjustment: base = FactSet + (v3 bottom-up with the 4.0 SHREWD loss − the same build with no loss) for FY2027–29, revenue −2.295 / −4.590 / −4.590 and Adjusted EBITDA −1.836 / −3.672 / −3.672 [C36]. v3 confines the adjustment to the post-pull event; v2 also carried our organic-rate change, which rests on information analysts already had and so belongs in the bottom-up view, not the base. FY2026 is unchanged. Reason the pull is treated as pre-event: it was taken about a day after a statement made to MPs, and the v1 build (SHREWD unresolved, no roll-off) already matched FactSet within 1.2% in FY2026–27, so FactSet does not embed a 2027 roll-off.
- **Bottom-up v3**: revenue 129.58 / 138.45 / 146.48 / 157.90; EBITDA 34.16 / 37.17 / 39.09 / 43.37 (v2 138.94 / 148.38 / 161.75 and 37.41 / 40.04 / 45.30). Bottom-up / base revenue 1.005 / 1.013 / 1.029 / 0.978; EBITDA 1.005 / 1.000 / 0.946 / 0.897. Scale factors on organic lines: Q4 0.9825, FY27 0.987, FY28 0.971, FY29 1.023 (all within 10% of 1).
- **Cash cost check** on base revenue: Q4 −0.5%, FY27 −0.9%, FY28 −4.1%, FY29 −2.8% [C15].

## ARR bridge trend and organic additions (v3)

Printed ARR bridge [A75]–[A78][C38]: organic additions net of churn 6.39 (2023), 6.48 (2024), 7.23 (2025), 8.12 (12 months to Q2 2026), 7.23 (12 months to Q3 2026, with the SHREWD drag). Opening ARR 36.2 / 44.6 / 71.1 / 79.6 / 93.7, so the organic rate fell 17.7% / 14.5% / 10.2% / 10.2% / 7.7%. Acquired ARR 1.10 / 17.9 / 15.9 (and 4.48 Buddy in Q3 2026). Dollar additions rose about 10% a year while 38 of acquired ARR joined the base with little net organic growth in aggregate. Seasonality, 2022–25 average: Q1 1.57, Q2 1.35, Q3 1.28, Q4 1.84; Q3 2026 0.816 was the weakest Q3 since 2022. FX +2.09 (2024), +1.99 (2025), +1.22 (9M 2026), held at zero [S15]. Term revenue / average ARR 0.994 / 0.980 / 0.979 / 0.988 for Q4 2025–Q3 2026, average 0.985, confirming S1; earlier quarters ran 1.01–1.14, highest in acquisition quarters; ARR excludes virtual care [A79][C39]. Term share of revenue 83% FY2024 [A80], 78% FY2025, 81% Q3 2026.

Driver [S29]: organic additions in dollars, base +10% a year from 8.12 = 8.94 / 9.83 / 10.8 (8.2% / 8.7% / 8.8% of opening ARR) [S3]–[S5]; bull +15% a year, bear flat 7.23 [S22]. Q4 2026 add 1.5 [S2]. v2's 9% / 10% of opening ARR implied 9.8–12.6 a year, above any year printed.

## SHREWD roll-off (v2, unchanged in v3)

Base 4.0 of ARR lost straight-line during 2027, about half of 7.5–8.6, none in 2028–29 [S26]. For a loss in 2027: the FDP that displaces SHREWD now runs to March 2029 [G26], and some suspended accounts are still in ARR [G3]. Against a larger loss: SHREWD is "in all different pockets" [G1], and a new FDP is procured from H2 2027, open to UK SMEs and new capability providers, starting with maternity [G27][G28]. Organic additions are measured before the SHREWD loss, so the Q3 drag is not counted twice [S29]. Lost revenue saves only cash cost of sales [S27][G14]. Closing ARR: 108.7 / 113.6 / 123.5 / 134.3 [C28].

## Costs

Cash gross margin 80% [S10]. Core cash opex 17.197 a quarter, +2% a year [S11][S12]. Variable opex 30% of revenue before the SHREWD loss above 127.65 [S13][S27]. Buddy saving 0.5 a year from FY2027 [S14]. FX at zero [S15].

## Scenarios

Levers [S18]: (1) SHREWD roll-off and organic dollar additions, (2) cost build, (3) Attend Anywhere. Scenario = base + (scenario bottom-up − base bottom-up).

- **Bull**: 1.5 SHREWD lost in 2027; Q4 add 2.5; organic additions +15% a year (9.34 / 10.7 / 12.4); VC flat; variable opex 20%; Buddy saving 1.0; no FDP procurement revenue [S22][S28]. Revenue {sc('bull','rev')}; EBITDA {sc('bull','ebitda')}.
- **Bear**: all 8.0 SHREWD lost during 2027; Q4 add 0.5; organic additions flat at 7.23; VC −15%; variable opex 40%; no saving [S22]. Revenue {sc('bear','rev')}; EBITDA {sc('bear','ebitda')}.
- v2→v3 changes are in C40 (v1→v2 in C37); unscaled bottom-up scenario totals in C33. The v3 bear headline rises vs v2 in FY2028–29 (+0.93 / +3.27 revenue) because the base bottom-up fell while base totals stay on Consensus.

## Operating-path leaves (written to the file; Finagle not run)

sales_growth and ebitda_growth on totals compound the base to FY2029E; me = {100*E['FY29E']/R['FY29E']:.1f}% [C24]; mc 0.50 (bull 0.60, bear 0.40) [S16]; gsnext {100*n['gsnext']:.2f}% (bull {100*n['gsnext_s']['bull']:.2f}%, bear {100*n['gsnext_s']['bear']:.2f}%) [S6]. No acquisition after Buddy [C21].

## Year 0, cash and shares

Unchanged from v1. Year-0 cash 57.630 + 61.551 + 0 = **119.181** [C16]; shares **63.232054** million [C17]. Dated items: Buddy cash −12.368 and 75,000 shares (10 Jul 2026); earn-outs paid −0.781; Novari earn-out up to 4.5 at 0.844 (4 Jul 2027); Buddy earn-out up to 7.249 at 0.442 (10 Jan 2029) [S20][S21]. No case goes cash-negative; no raise [C18].

## Assumptions to revise

1. SHREWD roll-off 4.0 in 2027 (band 1.5–8.0) and its timing [S26][S22].
2. Organic ARR additions growing 10% a year in dollars (band 0%–15%; 7.23 flat to 12.4 by FY2029) [S29][S3]–[S5].
3. Variable opex 30% (band 20%–40%) [S13]; fall-through of lost SHREWD revenue 80% [S27].
4. Attend Anywhere −5% a year (band 0% to −15%) [S7].
5. Term revenue / average ARR 0.985 (0.975–0.995) [S1]; services 16.5% of term (15%–19%) [S9].

## Numbered sources
{srcs()}

## Not verified

- D12/D13 (Seeking Alpha transcripts) read from the ceochat mirror; links not opened.
- D23 (The Register) is press reporting of a ministerial statement to MPs; Hansard was not checked.
- D22 / S19 (Dan Matlow CEO bot) is a simulated view, not company disclosure. D24 (CEO bot product sheet) was used only as an index; each figure was checked in the filing it names.
- The FY2023 MD&A could not be downloaded (OTC Markets "Temporarily Unavailable"); 2023 quarters come from the FY2024 MD&A comparatives [A75].
- Consensus (D17) shows whole numbers and no analyst count; whether any analyst revised after 16 Nov is unknown.
"""
(H / 'forecast.md').write_text(md, encoding='utf-8')
print(len(md))
