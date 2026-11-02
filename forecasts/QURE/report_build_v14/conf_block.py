# ---- confirmatory study cost section (one profile in all scenarios; bands run through the same pipeline) ----
import re as _re
CY = ['FY27E','FY28E','FY29E','FY30E','FY31E']
PROF = {'lower': [15,25,16,7,0], 'central': [30,45,32,17,5], 'upper': [50,75,55,30,12]}
GROSS = {'lower': [25,35,26,17,9], 'central': [40,55,42,27,15], 'upper': [60,85,65,40,22]}
CONFY = dict(zip(CY, PROF['central']))
BANDR = {'central': R, 'lower': json.load(open('/workspace/out/QURE_run_v14_band_lower/valuation_result_v14.json')), 'upper': json.load(open('/workspace/out/QURE_run_v14_band_upper/valuation_result_v14.json'))}
BRA = {k: cv('bear', 'baseline', 'cash', X=v['scenarios']) - 865.222 for k, v in BANDR.items()}
def conf_prof():
    t = ['| US$M | ' + ' | '.join(CY) + ' | Total FY27E–FY31E |', '|---|' + '---|' * 6]
    for k in ('lower', 'central', 'upper'):
        g, p = GROSS[k], PROF[k]
        t.append(f"| {k.capitalize()}: gross study cost [I908] | " + ' | '.join(str(x) for x in g) + f" | {sum(g)} |")
        t.append(f"| {k.capitalize()}: less run-rate offset [S902] | " + ' | '.join(f"−{x-y}" for x, y in zip(g, p)) + f" | −{sum(g)-sum(p)} |")
        t.append(f"| **{k.capitalize()}: separate confirmatory line** [I908][S902] | " + ' | '.join(f"**{x}**" for x in p) + f" | **{sum(p)}** |")
    return '\n'.join(t)
def conf_eff():
    t = ['| US$M | ' + ' | '.join(CY) + ' |', '|---|' + '---|' * 5]
    t.append(f"| Confirmatory line, all scenarios {i('CONFR')} | " + ' | '.join(f"{CONFY[y]:,.0f}" for y in CY) + ' |')
    for sc in ('base','bull','bear'):
        t.append(f"| {sc.capitalize()} EBITDA excluding the study [C702] | " + ' | '.join(f"{D[sc]['e'][y]+CONFY[y]:,.1f}" for y in CY) + ' |')
        t.append(f"| {sc.capitalize()} EBITDA as forecast [D46] | " + ' | '.join(f"{D[sc]['e'][y]:,.1f}" for y in CY) + ' |')
    return '\n'.join(t)
def conf_val():
    t = ['| Cost profile (separate line, FY27E–FY31E total) | Base value per share | Bull value per share | Bear value per share | Bear year-0 raise [P109] | Bear minimum cash |', '|---|---|---|---|---|---|']
    for k, tag in (('lower', '[D47]'), ('central', '[D45]'), ('upper', '[D47]')):
        X = BANDR[k]['scenarios']
        t.append(f"| {k.capitalize()} (${sum(PROF[k])}M) | {ps(X['base']['value_per_share'])} {tag} | {ps(X['bull']['value_per_share'])} {tag} | {ps(X['bear']['value_per_share'])} {tag} | ${BRA[k]:,.0f}M {tag} | {n(X['bear']['checks']['min_cash'],2)} {tag} |")
    return '\n'.join(t)
bv = {k: BANDR[k]['scenarios']['base']['value_per_share'] for k in BANDR}
MODEL_EFFECT = f"""### How the cost enters the forecast and the valuation

The central separate-line profile is carried unchanged in all three scenarios. In base and bull it is added to an opex build that starts from the Q2 2026 run rate; in bear it is added on top of the restructured opex (Figure A3). Bear still assumes AMT-130 is not approved, but the study starts screening before the FDA's decision and is assumed to be committed, so bear pays for it as well. Each scenario's EBITDA is therefore lower by exactly the amount on the line in each year from FY2027E to FY2031E, and is unaffected before and after (Figure 16).

**Figure 16 – Separate confirmatory-study line and EBITDA with and without it (US$M)**

{conf_eff()}

*Source: forecast file [D46]; "excluding" adds the line back [C702].*

The cost bands were run through the same forecast and valuation pipeline, changing nothing but the confirmatory line, and resizing the bear year-0 equity raise in each run so that bear cash never goes negative [P109]. Figure 17 shows the result. Because approval is assumed in base and bull, a cost of this size barely moves their values: between the lower and upper bands, base value per share moves by about ${bv['lower']-bv['upper']:.2f} (from {ps(bv['lower'])} to {ps(bv['upper'])}), well under 1% of the central value. In bear, where there is no revenue to absorb it, the cost goes straight into the cash the company must raise: the raise is ${BRA['lower']:,.0f}M on the lower band, ${BRA['central']:,.0f}M at the centre and ${BRA['upper']:,.0f}M on the upper band. Bear value per share is close to zero in every band ({ps(BANDR['lower']['scenarios']['bear']['value_per_share'])}, {ps(BANDR['central']['scenarios']['bear']['value_per_share'])} and {ps(BANDR['upper']['scenarios']['bear']['value_per_share'])}). The ordering is not monotonic because the raise is sized in $50M steps, so the cash left over at the end differs between runs; in bear a higher study cost shows up mainly as a larger raise and more dilution rather than as a lower value per share.

**Figure 17 – Value per share and bear raise by confirmatory-cost band**

{conf_val()}

*Source: central run [D45]; lower and upper band runs [D47]. Each run uses the same market data, capex, demand model and 2% terminal growth; only the confirmatory line and the bear raise differ.*
"""
body = open(f'{H}/report_build_v14/conf_section_body.md').read()
body = body.replace('| US$ million | FY27E | FY28E | FY29E | FY30E | FY31E | Total |', 'SEPLINE_TABLE_START| US$ million | FY27E | FY28E | FY29E | FY30E | FY31E | Total |', 1)
body = _re.sub(r'SEPLINE_TABLE_START.*?\n\n', lambda m: '**Figure 15 – Gross study cost, run-rate offset and separate confirmatory line (US$M)**\n\n' + conf_prof() + '\n\n*Source: gross cost from the cost bands above [I908]; offset is our assumption [S902].*\n\n', body, count=1, flags=_re.S)
body = body.replace('| US$ million | FY26 | FY27 |', '**Figure 14 – Gross confirmatory-study cost by band and year (US$M)**\n\n| US$ million | FY26 | FY27 |', 1)
body = body.replace('| Lower | 3 |', '| Lower [I908] | 3 |').replace('| **Central** | 4 |', '| **Central** [I908] | 4 |').replace('| Upper | 6 |', '| Upper [I908] | 6 |')
body = body.replace('| 3.9 | 5.9 | 4.1 |', '| 3.9 [D901] | 5.9 [D901] | 4.1 [D901] |').replace('| 6.9 | 10.5 | 19.8 | 13.0 | 18.0 | 42.5 | 14.3 |', '| 6.9 [D901] | 10.5 [D901] | 19.8 [D903] | 13.0 [D902] | 18.0 [D902] | 42.5 [D902] | 14.3 [D904] |')
body = _re.sub(r'(?m)^(?!\s*- )(.+)\n(- )', r'\1\n\n\2', body)
body = _re.sub(r'(?m)^  - ', '    - ', body)
CONF_SECTION = body.replace('MODEL_EFFECT', MODEL_EFFECT)
# sources for this section
_src = open(f'{H}/report_build_v14/conf_section_src.md').read()
CONF_SRC = {m.group(1): m.group(2) for m in _re.finditer(r'^- \*\*([DBK]\d+)\*\* (.*)$', _src, flags=_re.M)}
CONF_SRC['D905'] = CONF_SRC['D905'].replace('Use of Proceeds (p.85): ', 'Use of Proceeds (p.85): "net proceeds to us from this offering will be approximately $125.8 million (or approximately $145.4 million if the underwriters exercise their option to purchase additional shares in full)"; ')
CONF_SRC['D903'] += ' The FY2022 AMT-130 direct R&D of $19.8M is read from the same 10-K MD&A R&D table; the exact cell quote was not captured (partly unverified).'
for k in ('D906', 'D907'): CONF_SRC[k] = CONF_SRC[k].replace('Same document', 'Aspen Neuroscience 424B4 (same link as D905)')
for k in ('D908', 'D909', 'D910', 'D911', 'B902', 'B903', 'B904', 'B905'): CONF_SRC[k] += ' (web page; no page numbers)'
CONF_SRC['K901'] = 'Matt Kapusta bot: a CEO-simulation bot that reasons from public filings in the manner of uniQure\'s chief executive; a simulation, not a company statement. Output: gross study cost $190M / $250M / $320M (low / base / high); base phasing FY27–FY31 $50M / $75M / $62M / $38M / $25M; $1.2–1.8M per treated patient, $0.3–0.5M per control, $15–30M start-up. No page or link (simulation output).'
CONF_SRC.update({
 'I901': 'AMT-130 direct R&D 2017–H1 2026: 3.9 + 5.9 + 4.1 + 6.9 + 10.5 + 19.8 + 13.0 + 18.0 + 42.5 + 14.3 = $138.9M, from D901–D904',
 'I902': 'Phase I/II cost per treated patient: $138.9M less $19.4M BLA preparation and ~$10M pre-IND work = ~$110M; $110M / 57 patients = ~$1.9M, from D902–D904',
 'I903': 'Per dosing event excluding vector: ($110M − ~$30M fixed overhead − 205 patient-years × $0.15M = ~$31M) / 57 = ~$0.85M',
 'I904': 'Cash walk mid-2026 to end-2029: $811.9M cash + $100M Hercules tranche − 14 quarters × ($34.0M R&D + $17.4M SG&A) − launch allowance, no AMT-130 sales; leaves ~0 with a ~$150M study and ~−$70M with a ~$250M study',
 'I905': 'Aspen total Phase 3 cost: $110M / (0.50 to 0.67) = ~$165–220M; / ~100 patients = $1.6–2.2M per randomised patient',
 'I906': 'Aspen scaled to AMT-130: 133 treated × $1.0–1.35M + 67 controls × $0.25–0.40M + $30–40M fixed = ~$180–260M',
 'I907': 'Vector cost per AMT-130 patient $0.05–0.30M: a local brain dose scaled down from $0.5–1.0M generic AAV [B904] and $1–2M Hemgenix [B905]; dose ratio unverified',
 'I908': 'Bottom-up build: treated patients × (surgery and site $0.2–0.85M + vector $0.05–0.30M + follow-up) + controls × follow-up + $30–40M fixed = $84–275M, middle $150M; combined with I906 and K901 into gross bands $120M / $190M / $290M (FY26–FY32), phased by trial activity',
 'S901': 'Aspen Phase 3 size assumed at about 100 patients, in line with the AskBio and BlueRock trials (D908, D909); the 424B4 does not state the number of patients [S]',
 'S902': 'About $10M a year of the Q2 2026 AMT-130 external run rate (~$25M a year, D904) is redeployed to the confirmatory study, so the separate line = gross cost − $10M a year, floored at zero [S]',
 'D47': 'Band runs of the same pipeline: /workspace/out/QURE_run_v14_band_lower/valuation_result_v14.json and /workspace/out/QURE_run_v14_band_upper/valuation_result_v14.json (Finagle commit ' + R['finagle_commit'][:8] + ')',
 'P110': 'Analyst instruction, dated 2026-11-02: "Check the Aspen s-1 for more data. They will run a trial similar in size to AskBio and BlueRock. So this gives another data point. Bull, Base and Bear can use the same cost but include a detailed section in the report explaining analysis and upper and lower cost bands. Make it self contained and use prose to explain."',
})

CONF_SRC.update({
 'D48': 'uniQure 10-K FY2025, consolidated balance sheets (page number not captured): "Cash and cash equivalents $ 80,240 … Current investment securities 542,301" (US$ thousands, 31 December 2025). https://www.sec.gov/Archives/edgar/data/1590560/000110465926021898/qure-20251231x10k.htm',
 'D49': 'uniQure 8-K dated 24 June 2026, Item 1.01: "On June 24, 2026, the Underwriters exercised the Option in full. The Company estimates that the net proceeds from the Offering will be approximately $242.7 million after deducting underwriting discounts and commissions and estimated offering expenses." https://www.sec.gov/Archives/edgar/data/1590560/000110465926077339/tm2618105d1_8k.htm',
 'D50': 'uniQure 10-Q Q2 2026, condensed consolidated statements of shareholders\' equity (page number not captured): "Follow-on public offering 5,686,813 … 242,681" (shares; US$ thousands). Employee option exercises and ESPP added $6.985M in H1 2026. https://www.sec.gov/Archives/edgar/data/1590560/000110465926087815/qure-20260630x10q.htm',
 'P111': 'Analyst instruction, dated 2026-11-02: "Year-0 should be 2025 cash+short term. And then adjust for any equity raises during the 2026 year. Then increase sharecount from 2025 to account for the equity raises."',
})
