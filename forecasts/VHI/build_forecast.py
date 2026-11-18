"""Build forecast.json, drivers.csv and numbers.json for VHI (C$ millions).
Inputs: model.py (bottom-up build), work/otc_*.txt (SEDAR filings via OTC Markets, for page numbers).
Run from this folder: python3 build_forecast.py
"""
import json, sys, csv
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'work')); sys.path.insert(0, str(Path(__file__).parent))
import model as M
from pf import find

H = Path(__file__).parent
OTC = 'https://www.otcmarkets.com/filing/%s/content'
CEO_URL = 'https://github.com/mtlr05/ceochat/tree/main/companies/vhi'
CEO_TXT = 'simulated CEO view (Dan Matlow CEO bot), 17 Nov 2026; not company disclosure; link unverified'

DOCS = [
 ('D1', '607877', 'Vitalhub Corp., Interim MD&A for the three and nine months ended September 30, 2026, filed 2026-11-12 (SEDAR, PDF via OTC Markets; PDF page numbers)', '2026-11-12'),
 ('D2', '607876', 'Vitalhub Corp., Interim condensed consolidated financial statements, three and nine months ended September 30, 2026, filed 2026-11-12 (PDF page numbers)', '2026-11-12'),
 ('D3', '538307', 'Vitalhub Corp., Annual MD&A for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers)', '2026-03-18'),
 ('D4', '538304', 'Vitalhub Corp., Audited consolidated financial statements for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers)', '2026-03-18'),
 ('D5', '449868', 'Vitalhub Corp., Annual MD&A for the year ended December 31, 2024, filed 2025-03-27 (PDF page numbers)', '2025-03-27'),
 ('D6', '505549', 'Vitalhub Corp., Interim MD&A, three and nine months ended September 30, 2025, filed 2025-11-06 (PDF page numbers)', '2025-11-06'),
 ('D7', '583610', 'Vitalhub Corp., Interim MD&A, three and six months ended June 30, 2026, filed 2026-08-06 (PDF page numbers)', '2026-08-06'),
 ('D8', '560702', 'Vitalhub Corp., Interim MD&A, three months ended March 31, 2026, filed 2026-05-07 (PDF page numbers)', '2026-05-07'),
 ('D9', '485101', 'Vitalhub Corp., Interim MD&A, three and six months ended June 30, 2025, filed 2025-08-07 (PDF page numbers)', '2025-08-07'),
 ('D10', '462830', 'Vitalhub Corp., Interim MD&A, three months ended March 31, 2025, filed 2025-05-08 (PDF page numbers)', '2025-05-08'),
 ('D11', '424935', 'Vitalhub Corp., Interim MD&A, three and nine months ended September 30, 2024, filed 2024-11-13 (PDF page numbers)', '2024-11-13'),
 ('D14', '578190', 'Vitalhub Corp., news release "VitalHub Announces Acquisition of Buddy Healthcare", 2026-07-13 (PDF)', '2026-07-13'),
 ('D15', '607875', 'Vitalhub Corp., news release "VitalHub Reports Third Quarter 2026 Results", 2026-11-12 (PDF)', '2026-11-12'),
 ('D16', '538308', 'Vitalhub Corp., Annual Information Form for the year ended December 31, 2025, filed 2026-03-18 (PDF page numbers)', '2026-03-18'),
 ('D19', '593890', 'Vitalhub Corp., news release "VitalHub Announces Expansion of AI Capabilities with Launch of AI Scribe", 2026-09-15 (PDF)', '2026-09-15'),
]
OTHER_DOCS = [
 ('D12', 'https://seekingalpha.com/article/4967874-vitalhub-corp-vhi-ca-q3-2026-earnings-call-transcript', 'Seeking Alpha, "Vitalhub Corp. (VHI:CA) Q3 2026 Earnings Call Transcript", call held 2026-11-13 (HTML; no page numbers; text read from the ceochat mirror companies/vhi/sources/calls/seeking-alpha/2026-Q3.md at commit 8f8b44f; Seeking Alpha link unverified)', '2026-11-13'),
 ('D13', 'https://seekingalpha.com/article/4933144-vitalhub-corp-vhi-ca-q2-2026-earnings-call-transcript', 'Seeking Alpha, "Vitalhub Corp. (VHI:CA) Q2 2026 Earnings Call Transcript", call held 2026-08-07 (HTML; no page numbers; text read from the ceochat mirror 2026-Q2.md; link unverified)', '2026-08-07'),
 ('D17', 'https://markets.businessinsider.com/stocks/vhibf-stock', 'Markets Insider, "Vitalhub Estimates in CAD" (source: FactSet), pulled 2026-11-17; the Q3 2026 column shows as reported, so the pull is post-release (HTML; no page numbers)', '2026-11-17'),
 ('D18', 'https://stockanalysis.com/quote/tsx/VHI/forecast/', 'StockAnalysis, "Vitalhub (TSX:VHI) Stock Forecast" (S&P Global Market Intelligence), last updated 2026-11-17 (HTML)', '2026-11-17'),
 ('D21', 'https://finance.yahoo.com/healthcare/articles/vitalhub-vhi-said-q3-earnings-221424315.html', 'MarketBeat via Yahoo Finance, "What Vitalhub (VHI) Said on Its Q3 Earnings Call", 2026-11-13 (HTML; secondary cross-check of D12)', '2026-11-13'),
 ('D23', 'https://www.theregister.com/public-sector/2026/11/17/mps-ask-what-the-break-clause-was-for-as-palantir-wins-two-more-years-in-the-nhs/5310348', 'The Register (Lindsay Clark), "MPs ask what the break clause was for as Palantir wins two more years in the NHS", published 17 Nov 2026 10:15 UTC (HTML; no page numbers; fetched 17 Nov 2026)', '2026-11-17'),
 ('D24', 'https://github.com/mtlr05/ceochat/blob/main/companies/vhi/sources/products/term-licences-maintenance-and-support.md', 'Dan Matlow CEO bot product sheet "Term licences, maintenance and support" (ceochat companies/vhi/sources/products/term-licences-maintenance-and-support.md at commit 25246c9, read 18 Nov 2026): TLMS revenue 2019 Q1-2026 Q3 and the ARR bridge by quarter, each row citing the printed SEDAR filing (OTC Markets URL). Used as an index; figures cited here were checked in the filings D1, D3, D5 (link unverified)', '2026-11-18'),
 ('D25', 'https://github.com/mtlr05/finagle', 'Finagle valuation result v05 for VHI.TO (finagle-run/valuation_result_v05.json; request valuation_request_v05.json, sha256 ba766900bf9dd16f1178d9a00f12325b518624426d9b84fca32e4a52509b6446), run by the Finagle bot on 18 Nov 2026 14:33 ET with mtlr05/finagle at commit 377f177b4013e713fe7c4603962e5f883a67e298; notebooks notebook_base/bull/bear_v05.py in the same folder', '2026-11-18'),
 ('D26', 'https://finance.yahoo.com/quote/VHI.TO/', 'Yahoo Finance quote for VHI.TO as fetched by Finagle (results v04/v05, price_date 2026-11-18, v04 and v05): C$6.73, Yahoo previous close (HTML/API)', '2026-11-18'),
 ('D27', 'https://www.bankofcanada.ca/valet/observations/BD.CDN.10YR.DQ.YLD/json?recent=5', 'Bank of Canada Valet, BD.CDN.10YR.DQ.YLD, Government of Canada 10-year benchmark bond yield: 3.81% on 16 Nov 2026 (JSON, read 18 Nov 2026)', '2026-11-18'),
 ('D22', CEO_URL, 'Dan Matlow CEO bot (David May\'s CEO-simulation bot for Vitalhub), answers relayed 17 Nov 2026; simulated view built from public material, not company disclosure (link unverified)', '2026-11-17'),
]
DOC_URL = {d[0]: OTC % d[1] for d in DOCS}
DOC_URL.update({d[0]: d[1] for d in OTHER_DOCS})
DOC_OTC = {d[0]: d[1] for d in DOCS}
UNVERIFIED = {'D12', 'D13', 'D22', 'D24'}

sources = []
src_index = {}
used = {}

def _add_source(entry):
    if entry['id'] in src_index:
        return
    src_index[entry['id']] = entry
    sources.append(entry)

for d, otc, text, date in DOCS:
    _add_source({'id': d, 'text': text, 'url': OTC % otc, 'date': date, 'publisher': 'SEDAR (via OTC Markets)'})
for d, url, text, date in OTHER_DOCS:
    _add_source({'id': d, 'text': text, 'url': url, 'date': date, 'publisher': url.split('/')[2]})

def _page(doc, search):
    if doc in DOC_OTC and search:
        pages = find(DOC_OTC[doc], search)
        if pages:
            return 'p.%d' % pages[0]
    return None

def fact(value, tag, sid, text, doc=None, search=None, inputs=None, url=None, page=None, extra=None):
    """Return a fact; register sid (auto-suffixed when the same id would name a different value)."""
    key = (tag, repr(value))
    base = sid
    n = 0
    while sid in used and used[sid] != key:
        n += 1
        sid = '%s_%d' % (base, n)
    used.setdefault(sid, key)
    u = url or (DOC_URL.get(doc) if doc else None) or (DOC_URL['D1'])
    pg = page or _page(doc, search)
    cit = {'id': sid, 'text': text, 'url': u}
    if pg:
        cit['page'] = pg
    else:
        cit['page_status'] = 'unverified'
    if doc in UNVERIFIED or u == CEO_URL:
        cit['url_status'] = 'unverified'
        if 'unverified' not in text.lower():
            cit['text'] = text + ' (link unverified)'
    f = {'value': value, 'tag': tag, 'citation': cit}
    if extra:
        f.update(extra)
    entry = {'id': sid, 'text': cit['text']}
    if doc:
        entry['document'] = doc
    entry['page'] = pg or 'page unverified'
    if sid.startswith('C'):
        entry['inputs'] = inputs or ['D1']
    _add_source(entry)
    return f

def note(sid, text, doc=None, inputs=None, page=None):
    """Register a source entry that is not itself a forecast fact (G/S/P/E statements)."""
    e = {'id': sid, 'text': text, 'page': page or 'page unverified'}
    if doc: e['document'] = doc
    if sid.startswith('C'): e['inputs'] = inputs
    _add_source(e)

def r(x, n=3):
    return round(x, n)

def fmt(x):
    return '{:,.0f}'.format(round(x * 1e6))

# ---------------- statements quoted (G), prompt (P), estimates (E), assumptions (S) -------------
P = {
 'P1': 'David May, 17 Nov 2026 (t213u): "Create a forecast for VHI.TO ... Have 4 explicit years." Window FY2026E-FY2029E including the current year, per the brief.',
 'P2': 'David May standing preferences (brief, 17 Nov 2026): base case accelerates or decelerates current trends on management commentary, no conservative haircut; a later-year margin well beyond history is flagged and banded in the bear, not capped.',
 'P3': 'David May standing preference: year-0 cash = FY2025 cash plus short-term investments adjusted for 2026 equity raises; shares raised likewise; add a year-0 raise rounded up to the next C$50 only if a case goes cash-negative.',
 'P4': 'Brief, 17 Nov 2026: Vitalhub reports in CAD; keep CAD throughout. Dollar figures carry no repeated word "million".',
 'P5': 'Brief, 17 Nov 2026: do NOT run Finagle or any valuation.',
 'P7': 'David May, 17 Nov 2026 (revision, pt220u): "I think Palantirs contract was renewed. Probably have to assume that some of the shrewd contracts roll off in 2027." Base assumes a partial SHREWD roll-off in 2027; the base stays Consensus-anchored but is adjusted for this post-pull event (C36).',
 'P9': 'David May, 18 Nov 2026 (pt223u): "do a finagle valuation." The Finagle bot runs the valuation; the Forecaster wrote the collaborative request (v01) and writes the report section from the result only. v01-v03 stopped; v04 was superseded by v05 (D25), which is the valuation.',
 'P15': 'David May, 2026-11-18 (t237u): "Yes, do the quick fix". Applied in v05 as year-0 EBITDA 26.554099 (Vitalhub reported FY2025 Adjusted EBITDA, A2_1) and EBITDA definition before stock-based compensation, replacing Yahoo\'s 25.898.',
 'P10': 'David May, 2026-11-18, risk-free rate for the Finagle run: "3.81% use this" (Bank of Canada 10-year benchmark, 3.81% on 16 Nov 2026, D27, because Yahoo CA10Y=RR has no quote).',
 'P11': 'David May, 2026-11-18: "Rerun VHI as v03 with capex at the FY25 ratio of revenue, no debt (leases excluded), 26.5% tax, and no cash from the Buddy consideration shares." Applied in v04 as year-0 debt 0, debt policy hold, tax rate 26.5%.',
 'P12': 'David May, 2026-11-18: "cash should be from the 2025 filling adjusted for the cash price of Buddy (+$12.37). shares should be from the 2025 filling (63.23M) adjusted for Buddy (+0.075M). Isn\'t that logical?" Applied as opening cash 106.812709 = 119.180625 - 12.367916 (the Buddy closing cash is an outflow) and shares 63,307,054 = 63,232,054 + 75,000; the Buddy closing cash and consideration shares were removed from the schedule so they are not counted twice.',
 'P13': 'David May, 2026-11-18: "remove the \"amortization of intangible assets\" when calculating capex using method 1." Applied as year-0 D&A 1.271558 = depreciation of property and equipment 0.713788 + right-of-use assets 0.557770 (A81); capex stays on Finagle method 1.',
 'P14': 'Cost of debt 2.8% for the Finagle run: proposed by the Forecaster on 2026-11-18 (Finagle\'s own earlier default was 0.027976); David did not object. Not a direct David quote. Immaterial: debt is held at zero and forecast-year interest is zero.',
 'P8': 'David May, 18 Nov 2026 (pt221u): "ask the Dan Matlow bot for his product sheet on licenses. Update the forecast if it provides any insight into trends". v3 forecasts organic ARR adds in dollars from the sheet\'s ARR bridge (S29).',
 'P6': 'Brief and David May (t214u, 17 Nov 2026): Dan Matlow CEO bot may be used; his own views are tagged [S] "simulated CEO view (Dan Matlow CEO bot), 17 Nov 2026" and never shown as company disclosure.',
}
for k, v in P.items():
    note(k, v)

G = {
 'G1': ('D12', 'Matlow (Q3 2026 call): "I still think there\'s close to about $10 million or so-ish of SHREWD revenue that\'s still out there to a degree in all different pockets of it that are there. But it\'s hard to say which ones are not at risk or at risk".'),
 'G2': ('D12', 'Matlow (Q3 2026 call): "Take that back, Paul. 7%, 8% of our ARR number, not our revenue number."'),
 'G3': ('D12', 'Matlow (Q3 2026 call), on whether suspended SHREWD accounts were removed from ARR: "In some of the cases, yes, in some of the cases, no." and "I think we\'ll know more in another quarter or so how that comes out".'),
 'G4': ('D12', 'Matlow (Q3 2026 call): "I do believe if we didn\'t have the suspensions or the reversals on some of those SHREWD cuts, we would have been very close to our Rule of 40 base level".'),
 'G5': ('D12', 'Matlow (Q3 2026 call), asked about a path to Rule of 40 in 2027: "Yes, we think so. We do believe that\'s the case. Margins will continue to increase, and we\'re seeing real pipelines".'),
 'G6': ('D12', 'Matlow (Q3 2026 call): "We\'re comfortable that we\'re going to sustain, if not improve that number on a quarter-over-quarter basis at this stage."'),
 'G7': ('D12', 'Matlow (Q3 2026 call): "our backlog for our services revenue has never been stronger" and "we do think there\'s a lot more milestones that should be hit in Q4 than in Q3."'),
 'G8': ('D12', 'Matlow (Q3 2026 call): "I think we should be able to get that Novari product well over the $20 million in ARR numbers. And Strata ... we see another $3 million to $5 million in the pipeline of some stuff that could happen over the next couple of years."'),
 'G9': ('D12', 'Matlow (Q3 2026 call), on Attend Anywhere declining moderately: "Theoretically, yes. ... we also see some new deals cooking on it that maybe offset some of that stuff. ... all that stuff gets renewed in the March time frame".'),
 'G10': ('D12', 'Matlow (Q3 2026 call), on Buddy margins: "It will be through both a combination of a little bit of cost reduction and revenue generation ... Typically, we say it takes 6 months to 1 year and probably that would be the same here."'),
 'G11': ('D12', 'Goffenberg (Q3 2026 call), on R&D: "we\'re constantly trying to reduce R&D ... some areas we\'re going to be adding as we do more work on AI ... Probably continue in the same level going forward."'),
 'G12': ('D12', 'Matlow (Q3 2026 call): "with any luck, we\'ll be able to get another one over the finish line before the end of the year ... there are 2 or 3 companies that we have earmarked since the very beginning that are now in market".'),
 'G13': ('D13', 'Matlow (Q2 2026 call, 7 Aug 2026), replying to an analyst who noted no formal ARR guidance and a 10%-11% run rate: "we still feel comfortable with the rest of our business that we -- even with that headwind that we should still be in the range where we were this quarter and above it for sure ... we\'re still getting 10%, 11% organic growth." Not restated on the Q3 2026 call (D12).'),
 'G14': ('D13', 'Matlow (Q2 2026 call): "every $1 million of ARR theoretically if we don\'t add more costs, that\'s a point of adjusted EBITDA, right? And we\'re still not completed on the other side of some reductions."'),
 'G15': ('D13', 'Goffenberg (Q2 2026 call), on gross margin: "I think we\'re still, I think, continue to be probably to be the 80% line."'),
 'G16': ('D14', 'Buddy release (13 Jul 2026): "As at June 30, 2026, Buddy Healthcare had Annual Recurring Revenue of approximately EUR 2.8 million and is approximately Adjusted EBITDA breakeven."'),
 'G17': ('D12', 'Goffenberg (Q3 2026 call): "The increase was primarily due to lower research and development expenses, synergies from the integration of Induction and Novari and a favorable foreign exchange impact in the quarter."'),
 'G18': ('D12', 'Matlow (Q3 2026 call): "They have a break clause in their contract for February of 2027 that they can exercise on the Palantir product."'),
 'G19': ('D12', 'Matlow (Q3 2026 call), on Ontario: "The imaging world ... has gone live ... We expect to continue that work through 2027."'),
 'G20': ('D12', 'Matlow (Q3 2026 call), on no NCIB purchases through September: "I think it\'s more of the latter" (preserving flexibility for larger M&A).'),
 'G21': ('D12', 'Matlow (Q3 2026 call): "we believe just by adding AI products into our installed base, there\'s probably about $30 million, $40 million of TAM just on top of that."'),
 'G22': ('D13', 'Matlow (Q2 2026 call), on larger deals: "I think meaningful larger than Novare to a degree, not that much larger but meaningful larger".'),
 'G23': ('D1', 'Q3 2026 MD&A: Adjusted EBITDA = EBITDA + share-based and deferred share-based compensation + business acquisition, restructuring and integration costs + change in fair value of contingent consideration; foreign currency gains and losses stay inside Adjusted EBITDA. "The increase in Adjusted EBITDA was primarily attributable to lower research and development expenses and a favourable foreign exchange impact".'),
 'G24': ('D1', 'Q3 2026 MD&A: ARR "is defined as annual renewable software licence fees and maintenance services"; acquisition revenue is "the annual contract value of recurring revenues of the acquired companies at the time of acquisition"; organic growth is "the revenue over and above the acquisition revenues".'),
 'G25': ('D12', 'Goffenberg (Q3 2026 call): "Services revenue is seasonally lighter over the summer against elevated projected activity in the prior year period."'),
}
G.update({
 'G26': ('D23', 'The Register (17 Nov 2026): "Health minister James Frith told MPs on Monday that the current contract would continue until March 2029 as the government procures a new version of the Federated Data Platform (FDP)." The February 2027 break clause is therefore not exercised.'),
 'G27': ('D23', 'The Register (17 Nov 2026): "The formal process is set to start during the second half of next year and take around 18 months"; the new iteration would "welcome international and UK capability alike - whether that is UK small and medium-sized enterprises that want a crack at NHS contracts, sovereign AI-backed capability in the UK or any international provider worth merit."'),
 'G28': ('D23', 'The Register (17 Nov 2026), Frith: "We will also start work, alongside the new procurement, with different providers on developing new capabilities and expertise starting with systems used in maternity care." Frith also said migration was "possible in principle" under the contracts\' exit and transition provisions.'),
})
for k, (d, t) in G.items():
    note(k, t, d, page=_page(d, None))

E = {}
CONS = {'FY26E': (129.0, 34.0), 'FY27E': (139.0, 39.0), 'FY28E': (147.0, 45.0), 'FY29E': (166.0, 52.0)}

S = {
 'S1': 'Term revenue = 0.985 x average closing ARR. Basis: Q2 2026 term 24.542 x 4 / average ARR (99.079, 101.533) = 0.979; Q3 2026 25.784 x 4 / average (101.533, 107.194) = 0.988; average 0.984 rounded to 0.985. Band 0.975-0.995.',
 'S2': 'Q4 2026 organic net ARR add of 1.5 (base). Q4 is a stronger selling quarter than Q3 (Q4 2024 +2.61, Q4 2025 +1.88) but SHREWD suspensions continue (G1, G3); the FDP extension (G26) puts the SHREWD roll-off in 2027 rather than Q4 2026. Bull 2.5, bear 0.5.',
 'S3': 'FY2027 organic ARR adds 8.94 before the SHREWD roll-off (base): the 8.123 of organic adds in the four quarters to Q2 2026 (the last four before the Q3 SHREWD drag, A27_4-A27_7) grown 10%, the trend in dollar adds (S29). As a share of opening ARR this is 8.2%; net of the 4.0 roll-off FY2027 closing ARR grows 4.5%. v2 used 9% of opening ARR (9.8 of adds), above any year Vitalhub has printed. Band 7.23 (bear, flat at FY2025) to 9.34 (bull, +15%).',
 'S4': 'FY2028 organic ARR adds 9.83 (base), the dollar trend continued at +10% (S29); 8.7% of opening ARR. The Novari and Strata pipelines and AI add-ons (G8, G21) and the Rule of 40 aim (G5) support continued growth in dollar adds; the withdrawn 10%-11% comfort (G13) argues against a step-up beyond the trend, so the trend rate is used unchanged. No further SHREWD loss (S26). Band 7.23 (bear) to 10.74 (bull).',
 'S5': 'FY2029 organic ARR adds 10.81 (base), +10% again; 8.8% of opening ARR. Band 7.23 (bear) to 12.35 (bull).',
 'S6': 'FY2030 (gsnext year) organic ARR adds 11.89 base (bull 14.21, bear 7.23), one more year of the same dollar-add build; no management phrase reaches 2030.',
 'S7': 'Virtual care (Attend Anywhere) declines 5% a year from FY2027: management expects a moderate decline offset by some new deals, renewals in March (G9); Q3 2026 was -6% YoY. Band 0% (bull) to -15% (bear).',
 'S8': 'Perpetual licences 0.5 in Q4 2026 (Q4 2025 0.512) and 2.0 a year thereafter, about the FY2025-FY2026 average; term licences are the preferred model (D1).',
 'S9': 'Services, hardware and other: Q4 2026 4.6 (back to the Q1 2026 level of 4.585; management expects more Q4 milestones, G7) and 16.5% of term revenue thereafter (9M 2026 ratio 16.6%; FY2025 19.0%). Band 15%-19%.',
 'S10': 'Cash gross margin 80% (9M 2026 80%; CFO "80% line", G15). Cost of sales holds no D&A or SBC (D1). Band 78%-82%.',
 'S11': 'Core cash opex = Q3 2026 G&A 6.328 + S&M 3.379 + R&D 7.490 = 17.197 a quarter (ex SBC, D&A, FX, one-time), annualized 68.79; includes Buddy for 82 of 92 days.',
 'S12': 'Core opex inflation 2.0% a year: the Bank of Canada inflation-control target midpoint (no company rate stated). Band 1%-3%.',
 'S13': 'Variable cash opex 30% of revenue above Q3 2026 annualized revenue (127.65). The incremental rate cannot be measured from FY2025-26 because integration synergies cut opex while revenue grew; management says $1 of ARR is "a point of adjusted EBITDA" if no costs are added (G14) and R&D holds level with AI spend (G11). Band 20% (bull) to 40% (bear).',
 'S14': 'Buddy cost saving 0.5 a year from FY2027 (Buddy was about breakeven, G16; margin through "a little bit of cost reduction and revenue generation" in 6-12 months, G10). Band 0 (bear) to 1.0 (bull).',
 'S15': 'Foreign exchange gains and losses, which sit inside Adjusted EBITDA (G23), are forecast at zero; FX on ARR is held at zero.',
 'S16': 'Contribution margin mc = 1 - 20% cash cost of sales - 30% variable opex = 0.50 (bull 0.60, bear 0.40).',
 'S17': 'Buddy component inside the term line is held at the acquired ARR of 4.48 x 0.985 a year (stub 174/365 in FY2026); Vitalhub counts post-close growth as organic (G24), so Buddy growth sits in the organic ARR rate. Not scaled to Consensus.',
 'S18': 'Scenario levers: (1) SHREWD roll-off size and organic ARR adds in dollars, (2) the cost build (variable opex rate, Buddy saving), (3) Attend Anywhere. Bull and bear differ from base by the bottom-up difference of those levers, added to the base lines and EBITDA.',
 'S19': 'Dan Matlow CEO bot view: treat the 10-11% organic comfort as withdrawn until the NHS FDP decision; low-to-high single-digit organic ARR growth in Q4 2026 and early 2027. ' + CEO_TXT + '. Used only as a cross-check of S2-S3, which rest on the filings and the Q3 call.',
 'S20': 'Earn-out probabilities = accrued fair value / maximum: Novari 3.8 / 4.5 = 0.844; Buddy 3.205624 / 7.248555 = 0.442 (D2).',
 'S21': 'Earn-out dates are the end of each earn-out window: Novari 24 months after 4 Jul 2025 close (2027-07-04); Buddy 30 months after 10 Jul 2026 close (2029-01-10). The filings give windows, not payment dates.',
 'S22': 'Bear: all SHREWD ARR (8.0, the midpoint of 7.5-8.6, G2) rolls off straight-line during 2027 as trusts migrate onto FDP (G26); organic adds stay flat at the FY2025 printed 7.23 a year (A75), so organic growth falls to about 6.5% of opening ARR. Bull: only 1.5 rolls off (suspended accounts still in ARR, G3) and organic adds grow 15% a year (the 2024-to-TTM-Q1 2026 pace, S29) as the Strata pipeline and AI add-ons convert. A place in the new FDP procurement is not in bull revenue (S28).',
 'S23': 'Business acquisition, restructuring and integration costs (Q3 2026 1.368) are outside Adjusted EBITDA by the company definition (G23); Induction and Novari integration is "pretty well" done with "a little bit of work to do" and Buddy integration is underway (D12). They are not forecast inside Adjusted EBITDA.',
 'S26': 'Base SHREWD roll-off: 4.0 of ARR, about half of the 7.5-8.6 SHREWD ARR (G2, C31), straight-line during calendar 2027, none in 2028-29. Why half: the FDP extension to March 2029 (G26) means the platform displacing SHREWD stays and trusts keep migrating onto it, and some suspended accounts are still in ARR (G3), so a 2027 loss is more likely than not; but SHREWD sits "in all different pockets" and management cannot say which are at risk (G1), a new FDP iteration is procured from H2 2027 that invites UK SMEs and new capability providers (G27, G28), and trusts mid-procurement have reason to keep tools that work. The evidence does not identify losses beyond 2027. Band 1.5 (bull) to 8.0 (bear, all of it).',
 'S27': 'Lost SHREWD revenue (average ARR lost x 0.985 term ratio x 1.165 for the services that ride on term revenue) saves only the 20% cash cost of sales; opex is not cut (G14: "every $1 million of ARR theoretically if we don\'t add more costs, that\'s a point of adjusted EBITDA"). Variable opex is charged on revenue before the SHREWD loss.',
 'S28': 'FDP re-procurement upside is excluded from every case: the formal process starts in H2 2027 and takes about 18 months (G27), so an award lands around early 2029 at the earliest and its revenue mostly after FY2029; Vitalhub has not announced a consortium or bid.',
 'S29': 'Organic adds are forecast in dollars. Printed organic net of churn was 6.39 in 2023, 6.48 in 2024 and 7.23 in 2025 (A75) while acquisitions took opening ARR from 36.2 to 71.1 (A76); organic growth fell from 17.7% to 14.5% to 10.2% (and 7.7% TTM Q3 2026) because the acquired ARR (17.9 in 2024, 15.9 in 2025, 4.48 in 2026) added little net organic growth after close in aggregate, not because dollar adds shrank (C38). Dollar adds grew about 10% a year from 2023 (6.39) to the four quarters to Q2 2026 (8.12), about 2.5 years apart. Base keeps that 10% trend; management commentary is mixed (pipelines and Rule of 40 vs the withdrawn 10%-11%), so no acceleration or deceleration is applied.',
 'S24': 'Q4 2026 virtual care held at the Q3 2026 level (2.338); renewals fall in March (G9).',
}
for k, v in S.items():
    note(k, v, 'D22' if k == 'S19' else None)

# ---------------- event adjustment to Consensus (v2) ----------------
V1B = M.build('base', M.CASES_V1['base'])
B0 = M.build('base')
B0nl = M.build('base', dict(M.CASES['base'], loss=[0.0, 0.0, 0.0]))
ADJ = {'FY26E': (0.0, 0.0)}
for y in M.YEARS[1:]:
    ADJ[y] = (B0['rev'][y] - B0nl['rev'][y], B0['ebitda'][y] - B0nl['ebitda'][y])
BASEV = {y: (CONS[y][0] + ADJ[y][0], CONS[y][1] + ADJ[y][1]) for y in CONS}


# ---------------- build ----------------
B = {c: M.build(c) for c in M.CASES}
base = B['base']
YRS = M.YEARS
buddyQ4 = M.BUDDY_ARR * M.TERM_RATIO / 4

def scaled_base():
    """Scale organic lines of unreported periods to Consensus; Buddy component not scaled."""
    out = {}
    q4_cons = BASEV['FY26E'][0] - M.FY['9M26A']['rev']
    q4_bu = base['rev']['Q4E']
    f = {'Q4E': (q4_cons - buddyQ4) / (q4_bu - buddyQ4)}
    for y in YRS[1:]:
        f[y] = (BASEV[y][0] - base['buddy'][y]) / (base['rev'][y] - base['buddy'][y])
    lines = {k: {} for k in ('term', 'vc', 'perp', 'svc')}
    for per in ['Q4E'] + YRS[1:]:
        bud = buddyQ4 if per == 'Q4E' else base['buddy'][per]
        lines['term'][per] = (base['term'][per] - bud) * f[per] + bud
        for k in ('vc', 'perp', 'svc'):
            lines[k][per] = base[k][per] * f[per]
    for k in lines:
        lines[k]['FY26E'] = M.FY['9M26A'][k] + lines[k]['Q4E']
    return lines, f

L, F = scaled_base()
rev_base = {y: BASEV[y][0] for y in YRS}
ebitda_base = {y: BASEV[y][1] for y in YRS}
rev_base['Q4E'] = BASEV['FY26E'][0] - M.FY['9M26A']['rev']
ebitda_base['Q4E'] = BASEV['FY26E'][1] - M.FY['9M26A']['ebitda']

def scen_lines(c):
    b = B[c]
    out = {k: {} for k in L}
    for k in L:
        for per in ['Q4E'] + YRS:
            out[k][per] = L[k][per] + (b[k][per] - base[k][per])
    rev = {per: rev_base[per] + (b['rev'][per] - base['rev'][per]) for per in ['Q4E'] + YRS}
    ebt = {per: ebitda_base[per] + (b['ebitda'][per] - base['ebitda'][per]) for per in ['Q4E'] + YRS}
    return out, rev, ebt

SC = {c: scen_lines(c) for c in ('bull', 'bear')}

# next year (gsnext) on the scaled base lines
def next_year(lines, b):
    tot = 0.0
    parts = {}
    for k in lines:
        if k == 'term':
            org29 = lines['term']['FY29E'] - b['buddy']['FY29E']
            org_bu29 = b['term']['FY29E'] - b['buddy']['FY29E']
            org_bu30 = b['term']['FY30E'] - b['buddy']['FY30E']
            v = org29 * org_bu30 / org_bu29 + b['buddy']['FY30E']
        else:
            v = lines[k]['FY29E'] * (b[k]['FY30E'] / b[k]['FY29E'])
        parts[k] = v; tot += v
    return parts, tot

NY_parts, NY = next_year(L, base)
gsnext = NY / rev_base['FY29E'] - 1
NYS = {c: next_year(SC[c][0], B[c]) for c in SC}
gsnext_s = {c: NYS[c][1] / SC[c][1]['FY29E'] - 1 for c in SC}

# ---------------- facts: history ----------------
LINE_META = {
 'term': ('Term licences, maintenance and support', 'recurring (ARR-driven; Buddy acquired component inside)'),
 'vc': ('Virtual care term licences (Attend Anywhere)', 'mature or declining'),
 'perp': ('Perpetual licences', 'mature or declining'),
 'svc': ('Services, hardware and other', 'recurring (tied to term revenue; project milestones)'),
}
HIST_SEARCH = {
 ('term','FY24A'): ('D5', '57,070,350'), ('perp','FY24A'): ('D5', '498,274'), ('svc','FY24A'): ('D5', '11,025,686'),
 ('term','FY25A'): ('D3', '85,442,864'), ('vc','FY25A'): ('D3', '5,184,921'), ('perp','FY25A'): ('D3', '2,089,242'), ('svc','FY25A'): ('D3', '16,249,891'),
 ('term','9M26A'): ('D1', '74,252,927'), ('vc','9M26A'): ('D1', '7,018,965'), ('perp','9M26A'): ('D1', '1,944,450'), ('svc','9M26A'): ('D1', '12,341,147'),
}
AID = {'term': 'A3', 'vc': 'A4', 'perp': 'A5', 'svc': 'A6'}

def per_key(p):
    return {'FY24A': 'FY24A', 'FY25A': 'FY25A', '9M26A': '9MA'}[p]

lines_json = []
for k in ('term', 'vc', 'perp', 'svc'):
    name, pat = LINE_META[k]
    per = {}
    for p in ('FY24A', 'FY25A', '9M26A'):
        v = M.FY[p][k]
        if k == 'vc' and p == 'FY24A':
            per['FY24A'] = fact(0.0, 'A', 'A4', 'No virtual care revenue before the Induction acquisition (June 2025); FY2025 MD&A shows prior-year virtual care of 0.', 'D3', '5,184,921')
            continue
        d, s = HIST_SEARCH[(k, p)]
        per[per_key(p)] = fact(r(v, 6), 'A', AID[k], '%s, %s: C$%s (reported).' % (name, {'FY24A': 'FY2024', 'FY25A': 'FY2025', '9M26A': 'nine months to 30 Sep 2026'}[p], s), d, s)
    per['Q4E'] = fact(r(L[k]['Q4E']), 'C', 'C1', '%s Q4 2026E = bottom-up Q4 (%s) scaled by the Q4 organic factor %.4f to the Consensus remainder; Buddy component not scaled.' % (name, r(base[k]['Q4E']), F['Q4E']), inputs=['E1', 'A1_9', 'S1', 'S2', 'S8', 'S9', 'S17', 'S24'])
    for y in YRS:
        per[y] = fact(r(L[k][y]), 'C', 'C2', '%s %s = bottom-up %s x organic scale factor %.4f to event-adjusted Consensus revenue (Buddy component unscaled).' % (name, y, r(base[k][y]), F.get(y, F['Q4E'])), inputs=['E1', 'S1', 'S3', 'S7', 'S8', 'S9', 'S17', 'S26', 'C36'])
    fy25, fy24 = M.FY['FY25A'][k], M.FY['FY24A'][k]
    if fy24:
        per['YoY'] = fact(r(fy25 / fy24 - 1, 4), 'C', 'C3', '%s FY2025A / FY2024A - 1.' % name, inputs=[AID[k], AID[k]])
    else:
        per['YoY'] = fact(0.0, 'C', 'C3', '%s had no FY2024 revenue; growth not meaningful, recorded as 0.' % name, inputs=['A4'])
    prev = fy25
    for y in YRS:
        per['YoY_' + y] = fact(r(L[k][y] / prev - 1, 4), 'C', 'C3', '%s %s growth.' % (name, y), inputs=['C2'])
        prev = L[k][y]
    line = {'name': name, 'pattern': pat, 'periods': per}
    if k == 'term':
        line['components'] = {
          'buddy_acquired': {y: fact(r(base['buddy'][y]), 'S', 'S17', S['S17']) for y in YRS},
          'buddy_acquired_Q4E': fact(r(buddyQ4), 'S', 'S17', S['S17']),
          'note': 'Organic = line minus buddy_acquired. 9MA includes Buddy from 10 Jul 2026 (Finland revenue 1.201 in Q3 2026, A61, which may include services).',
        }
        line['acquired'] = {
          'close_date': '2026-07-10',
          'stub_fraction': fact(r(174 / 365, 4), 'C', 'C4', 'Days from 10 Jul 2026 close to 31 Dec 2026 (174) / 365.', inputs=['A45']),
          'target_source': {'text': 'Buddy ARR about EUR 2.8 at 30 Jun 2026 and about Adjusted EBITDA breakeven (D14); acquired ARR 4.48 in the Q3 2026 ARR bridge (D1).', 'url': DOC_URL['D14']},
          'synergies': {'text': 'Cost saving 0.5 a year from FY2027 in the cost build (S14), separate from revenue; no revenue synergy is added.'},
        }
    lines_json.append(line)

# totals
def tot_fact(v, tag, sid, text, **kw):
    return fact(r(v, 6) if tag == 'A' else r(v), tag, sid, text, **kw)

rev_tot = {
 'FY24A': fact(68.59431, 'A', 'A1', 'Revenue FY2024: C$68,594,310.', 'D5', '68,594,310'),
 'FY25A': fact(108.966918, 'A', 'A1', 'Revenue FY2025: C$108,966,918.', 'D3', '108,966,918'),
 '9MA': fact(95.557489, 'A', 'A1', 'Revenue nine months to 30 Sep 2026: C$95,557,489.', 'D1', '95,557,489'),
 'Q4E': fact(r(rev_base['Q4E']), 'C', 'C5', 'Q4 2026E revenue = FY2026 Consensus 129 (E1) - 9M 2026 reported 95.557 (A1).', inputs=['E1', 'A1']),
 'YoY': fact(r(108.966918 / 68.59431 - 1, 4), 'C', 'C6', 'FY2025A / FY2024A - 1 (+58.9%, acquisitions plus organic).', inputs=['A1', 'A1_1']),
}
eb_tot = {
 'FY24A': fact(17.840272, 'A', 'A2', 'Adjusted EBITDA FY2024: C$17,840,272.', 'D5', '17,840,272'),
 'FY25A': fact(26.554099, 'A', 'A2', 'Adjusted EBITDA FY2025: C$26,554,099.', 'D3', '26,554,099'),
 '9MA': fact(24.772636, 'A', 'A2', 'Adjusted EBITDA nine months to 30 Sep 2026: C$24,772,636.', 'D1', '24,772,636'),
 'Q4E': fact(r(ebitda_base['Q4E']), 'C', 'C5', 'Q4 2026E Adjusted EBITDA = FY2026 Consensus EBITDA 34 (E2) - 9M 2026 reported 24.773 (A2).', inputs=['E2', 'A2']),
 'YoY': fact(r(26.554099 / 17.840272 - 1, 4), 'C', 'C6', 'FY2025A / FY2024A - 1.', inputs=['A2', 'A2_1']),
}
for y in YRS:
    rv, ev = CONS[y]
    raw_r = fact(rv, 'E', 'E1', 'FactSet consensus revenue %s: %d (C$ millions, rounded to whole numbers on the page), pulled 17 Nov 2026 after the Q3 2026 release; analyst count not shown on the page.' % (y, rv), 'D17', extra={'as_of': '2026-11-17', 'analysts': None})
    raw_e = fact(ev, 'E', 'E2', 'FactSet consensus EBITDA %s: %d (C$ millions, whole numbers), pulled 17 Nov 2026; FactSet EBITDA history for 2025 equals Vitalhub Adjusted EBITDA (26.55); analyst count not shown.' % (y, ev), 'D17', extra={'as_of': '2026-11-17', 'analysts': None})
    for d in (raw_r, raw_e):
        d.pop('analysts', None)
    ar, ae = ADJ[y]
    if y == 'FY26E':
        rev_tot[y] = raw_r; eb_tot[y] = raw_e
    else:
        rev_tot[y] = fact(r(BASEV[y][0]), 'C', 'C36', 'Event-adjusted Consensus revenue %s = FactSet %d (E1) %+.3f for the 16 Nov 2026 FDP extension (P7): the effect of the 4.0 SHREWD roll-off alone on the v3 bottom-up build (with vs without the loss). The 17 Nov pull is taken to predate the announcement. v3 isolates the event: the organic-driver change (S29) uses information analysts already had and does not move the base.' % (y, rv, ar), inputs=['E1', 'P7', 'S26', 'S27', 'D23'], extra={'as_of': '2026-11-17', 'unadjusted': raw_r})
        eb_tot[y] = fact(r(BASEV[y][1]), 'C', 'C36', 'Event-adjusted Consensus Adjusted EBITDA %s = FactSet %d (E2) %+.3f for the same SHREWD roll-off; lost revenue saves only cash cost of sales (S27).' % (y, ev, ae), inputs=['E2', 'P7', 'S26', 'S27', 'D23'], extra={'as_of': '2026-11-17', 'unadjusted': raw_e})
prev_r, prev_e = 108.966918, 26.554099
for y in YRS:
    rev_tot['YoY_' + y] = fact(r(BASEV[y][0] / prev_r - 1, 4), 'C', 'C6', 'Revenue growth %s.' % y, inputs=['E1'])
    eb_tot['YoY_' + y] = fact(r(BASEV[y][1] / prev_e - 1, 4), 'C', 'C6', 'Adjusted EBITDA growth %s.' % y, inputs=['E2'])
    prev_r, prev_e = BASEV[y]
margin = {}
for k, rv, ev in [('FY24A', 68.59431, 17.840272), ('FY25A', 108.966918, 26.554099), ('9MA', 95.557489, 24.772636), ('Q4E', rev_base['Q4E'], ebitda_base['Q4E'])] + [(y, BASEV[y][0], BASEV[y][1]) for y in YRS]:
    margin[k] = fact(r(ev / rv, 4), 'C', 'C7', 'Adjusted EBITDA / revenue, %s.' % k, inputs=['A1', 'A2', 'E1', 'E2'])
gm = {
 'FY24A': fact(0.809, 'A', 'A63', 'Gross profit FY2024 C$55,494,433, 81% of revenue.', 'D5', '55,494,433'),
 'FY25A': fact(0.804, 'A', 'A63', 'Gross profit FY2025 C$87,588,361, 80% of revenue.', 'D3', '87,588,361'),
 '9MA': fact(0.80, 'A', 'A63', 'Gross profit nine months 2026 C$76,400,633, 80% of revenue.', 'D1', '76,400,633'),
}
for y in YRS:
    gm[y] = fact(0.80, 'S', 'S10', S['S10'])
totals = {'revenue': rev_tot, 'ebitda': eb_tot, 'ebitda_margin': margin, 'gross_margin': gm}

# quarterly history (not summed as periods; kept as facts)
QDOC = ['D11', 'D5', 'D10', 'D9', 'D6', 'D3', 'D8', 'D7', 'D1']
hist = {}
for i, q in enumerate(M.Q):
    d = QDOC[i]
    row = {}
    for key, aid, label in [('rev', 'A20', 'revenue'), ('ebitda', 'A21', 'Adjusted EBITDA'), ('term', 'A22', 'term licences, maintenance and support'), ('vc', 'A23', 'virtual care'), ('perp', 'A24', 'perpetual licences'), ('svc', 'A25', 'services, hardware and other')]:
        v = M.QH[key][i]
        row[key] = fact(r(v, 6), 'A', aid, '%s %s: C$%s.' % (q, label, fmt(v)), d, fmt(v) if v else None)
    for key, aid, label, d2 in [('arr', 'A26', 'closing ARR', 'D1' if i >= 1 else 'D6'), ('arr_org', 'A27', 'organic ARR net of churn', 'D1' if i >= 1 else 'D6'), ('arr_acq', 'A28', 'acquired ARR', 'D1' if i >= 1 else 'D6')]:
        v = M.QH[key][i]
        row[key] = fact(r(v, 6), 'A', aid, '%s %s: C$%s (ARR bridge, non-IFRS section).' % (q, label, fmt(v)), d2, fmt(v) if v else 'Opening balance')
    row['fx_loss_gain'] = fact(r(M.QH['fx_loss'][i], 6), 'A' if i != 7 else 'C', 'A29' if i != 7 else 'C8', ('%s foreign currency loss (gain) inside Adjusted EBITDA: C$%s.' % (q, fmt(M.QH['fx_loss'][i]))) if i != 7 else 'Q2 2026 FX loss = 9M 2026 gain (0.130585) - Q1 loss 0.238091 - Q3 gain (0.592126) solved for Q2 = 0.222984.', d if i != 7 else None, fmt(abs(M.QH['fx_loss'][i])) if i != 7 else None, inputs=['A29'])
    hist[q] = row
history = {'note': 'Nine reported quarters Q3 2024-Q3 2026 (C$ millions). Each quarter cites its own MD&A; ARR from the Q3 2026 MD&A bridge (Q4 2024 onward) and the Q3 2025 MD&A (Q3 2024).', 'quarters': hist}

# ---------------- views ----------------
def ratio(n, d, sid, text, inputs):
    return fact(r(n / d, 6), 'C', sid, text, inputs=inputs)
views = {'used': {'revenue': 'consensus', 'ebitda': 'consensus'}, 'revenue': {}, 'ebitda': {}, 'ratios': {}}
for y in YRS:
    bu_r, bu_e = base['rev'][y], base['ebitda'][y]
    cr, ce = BASEV[y]
    views['revenue'][y] = {
      'bottom_up': fact(r(bu_r), 'C', 'C9', 'Bottom-up revenue %s: sum of unscaled lines (term from the ARR path, virtual care, perpetual, services).' % y, inputs=['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S17']),
      'top_down': {'absent': 'No revenue guidance. Vitalhub gives no formal guidance; the Q2 2026 call comfort with 10-11% organic ARR growth (G13) is an ARR phrase, was not restated on the Q3 2026 call, and is treated as stale.'},
      'calibrated_top_down': {'absent': 'No guidance range, so no coefficient C.'},
      'consensus': rev_tot[y],
    }
    views['ebitda'][y] = {
      'bottom_up': fact(r(bu_e), 'C', 'C10', 'Bottom-up Adjusted EBITDA %s: unscaled revenue - 20%% cash cost of sales - core opex (Q3 2026 annualized, +2%%/yr) + Buddy saving - 30%% variable opex on revenue above 127.65.' % y, inputs=['S10', 'S11', 'S12', 'S13', 'S14', 'S15']),
      'top_down': {'absent': 'No EBITDA guidance. "Sustain, if not improve" the 27% quarterly margin (G6) and "Margins will continue to increase" (G5) are directional phrases, not a range or a point.'},
      'calibrated_top_down': {'absent': 'No guidance range, so no coefficient C.'},
      'consensus': eb_tot[y],
    }
    abs_td = {'absent': 'top-down is absent'}
    abs_ct = {'absent': 'calibrated top-down is absent'}
    views['ratios'][y] = {
      'revenue': {
        'bottom_up_over_base': ratio(bu_r, cr, 'C11', 'Bottom-up / base (event-adjusted Consensus) revenue %s.' % y, ['C9', 'E1']),
        'top_down_over_base': abs_td, 'calibrated_top_down_over_base': abs_ct,
        'consensus_over_base': fact(1.0, 'C', 'C12', 'Event-adjusted Consensus is the base, ratio 1.', inputs=['E1']),
        'bottom_up_over_calibrated_top_down': abs_ct,
        'bottom_up_over_consensus': ratio(bu_r, cr, 'C11', 'Bottom-up / base (event-adjusted Consensus) revenue %s.' % y, ['C9', 'E1']),
      },
      'ebitda': {
        'bottom_up_over_base': ratio(bu_e, ce, 'C13', 'Bottom-up / base (event-adjusted Consensus) Adjusted EBITDA %s.' % y, ['C10', 'E2']),
        'top_down_over_base': abs_td, 'calibrated_top_down_over_base': abs_ct,
        'consensus_over_base': fact(1.0, 'C', 'C12', 'Event-adjusted Consensus is the base, ratio 1.', inputs=['E1']),
        'bottom_up_over_calibrated_top_down': abs_ct,
        'bottom_up_over_consensus': ratio(bu_e, ce, 'C13', 'Bottom-up / base (event-adjusted Consensus) Adjusted EBITDA %s.' % y, ['C10', 'E2']),
      },
    }

# ---------------- costs ----------------
costs = {'basis': 'Adjusted EBITDA = revenue - cash cost (basis 2: cash cost of sales + cash G&A, S&M and R&D, all excluding D&A, SBC and acquisition/restructuring/integration costs; FX gains and losses inside, forecast at zero).', 'bridge_at_base_revenue': {}, 'check_10pct': {}}
for i, y in enumerate(YRS):
    rv = rev_base['Q4E'] if y == 'FY26E' else rev_base[y]
    if y == 'FY26E':
        gp = M.GM * rv; core = M.CORE_OPEX_Q3; syn = 0.0; var = 0.30 * max(0, rv * 4 - M.REV_Q3_ANN) / 4
    else:
        gp = M.GM * rv; core = M.CORE_OPEX_Q3 * 4 * (1 + M.INFL) ** i; syn = 0.5; var = 0.30 * (rv + base['lost_rev'][y] - M.REV_Q3_ANN)
    bu_e = gp - core + syn - var
    per = 'Q4E' if y == 'FY26E' else y
    cons_e = ebitda_base[per]
    costs['bridge_at_base_revenue'][per] = {
      'revenue': fact(r(rv), 'C', 'C14', 'Base revenue for the bridge (%s).' % per, inputs=['E1', 'A1']),
      'gross_profit': fact(r(gp), 'C', 'C14', 'Revenue x 80% cash gross margin.', inputs=['S10']),
      'core_opex': fact(r(core), 'C', 'C14', 'Q3 2026 cash opex 17.197 a quarter, annualized and grown 2%/yr.', inputs=['S11', 'S12']),
      'buddy_saving': fact(r(syn), 'C', 'C14', 'Buddy cost saving (S14).', inputs=['S14']),
      'variable_opex': fact(r(var), 'C', 'C14', '30% of revenue (before the SHREWD loss, S27) above Q3 2026 annualized revenue 127.65.', inputs=['S13']),
      'ebitda_cost_build': fact(r(bu_e), 'C', 'C14', 'Cost-build Adjusted EBITDA on base revenue.', inputs=['S10', 'S11', 'S12', 'S13', 'S14']),
      'ebitda_consensus_base': fact(r(cons_e), 'C', 'C14', 'Base Adjusted EBITDA (Consensus; Q4 = FY less 9M).', inputs=['E2', 'A2']),
      'cash_cost_gap': fact(r((rv - cons_e) / (rv - bu_e) - 1, 4), 'C', 'C15', 'Consensus-implied cash cost / cost-build cash cost on the same revenue - 1; inside the 10% rule.', inputs=['E1', 'E2', 'S10', 'S11', 'S13']),
    }

# ---------------- cash and shares ----------------
year0 = {
 'cash_and_cash_equivalents_FY25A': fact(57.629569, 'A', 'A40', 'Cash and cash equivalents 31 Dec 2025: C$57,629,569.', 'D4', '57,629,569'),
 'short_term_investments_FY25A': fact(61.551056, 'A', 'A41', 'Short-term investments 31 Dec 2025: C$61,551,056.', 'D4', '61,551,056'),
 'equity_raises_2026': fact(0.0, 'A', 'A62', 'No equity offering in 2026: nine-month 2026 financing cash flow of C$167,507 "relates primarily to proceeds from the exercise of options, net of principal payments on lease liabilities"; the prior-year period held the January and August 2025 offerings.', 'D1', '167,507'),
 'year0_cash': fact(119.180625, 'C', 'C16', 'Year-0 cash = FY2025 cash 57.630 + short-term investments 61.551 + 2026 equity raises 0 = 119.181 (P3).', inputs=['A40', 'A41', 'A62', 'P3']),
 'shares_FY25A': fact(63.232054, 'A', 'A42', '63,232,054 common shares issued and outstanding at 31 Dec 2025 (shown as the comparative in the Q3 2026 MD&A).', 'D1', '63,232,054'),
 'year0_shares': fact(63.232054, 'C', 'C17', 'Year-0 shares = FY2025 63.232054 + 2026 equity raises 0 (P3). The 75,000 Buddy consideration shares are on cash_share_adjustments.', inputs=['A42', 'A62', 'P3']),
 'shares_30Sep26': fact(63.472236, 'A', 'A43', '63,472,236 common shares at 30 Sep 2026 (option exercises and 75,000 Buddy shares).', 'D1', '63,472,236'),
 'cash_sti_30Sep26': fact(129.007023, 'A', 'A44', 'Cash and cash equivalents and short-term investments at 30 Sep 2026: C$129,007,023; no debt.', 'D1', '129,007,023'),
 'year0_equity_raise': fact(0.0, 'C', 'C18', 'No year-0 equity raise: opening cash 119.181 less the dated Buddy and earn-out items (about 26 undiscounted in the base) stays positive in every case, and EBITDA is positive in every year of every case (P3).', inputs=['C16', 'P3']),
 'debt': fact(0.0, 'A', 'A64', 'As at September 30, 2026 the Company "has no debt outstanding"; Scotia C$5 operating line and C$60 revolving facility undrawn.', 'D1', 'no debt outstanding'),
}
csa_base = [
 {'kind': 'cash', 'name': 'Buddy Healthcare cash consideration on closing',
  'when': fact('2026-07-10', 'A', 'A45', 'Buddy acquired July 10, 2026; cash consideration on closing C$12,367,916 (after the 31 Dec 2025 year-0 balance).', 'D2', '12,367,916'),
  'probability': fact(1.0, 'C', 'C19', 'Paid at close; probability 1.', inputs=['A45']),
  'amount': fact(-12.367916, 'A', 'A45', 'Buddy cash consideration on closing C$12,367,916, recorded as -12.368.', 'D2', '12,367,916')},
 {'kind': 'equity', 'name': 'Buddy Healthcare consideration shares',
  'when': fact('2026-07-10', 'A', 'A46', '75,000 shares issued at $7.36/share on the Buddy close.', 'D2', '75,000 shares'),
  'probability': fact(1.0, 'C', 'C19', 'Issued at close; probability 1.', inputs=['A45']),
  'shares': fact(0.075, 'A', 'A46', '75,000 shares issued at $7.36/share.', 'D2', '75,000 shares'),
  'price': fact(7.36, 'A', 'A47', 'Issue price $7.36 per share (filing price).', 'D2', '75,000 shares')},
 {'kind': 'cash', 'name': 'Contingent consideration paid in 9M 2026',
  'when': fact('2026-09-30', 'S', 'S25', 'Payments of contingent consideration C$781,053 in the nine months to 30 Sep 2026; exact date not given, dated at the quarter end.', 'D2', '781,053'),
  'probability': fact(1.0, 'C', 'C19', 'Paid; probability 1.', inputs=['A48']),
  'amount': fact(-0.781053, 'A', 'A48', 'Payments of contingent consideration (781,053) in the nine months to 30 Sep 2026.', 'D2', '781,053')},
 {'kind': 'cash', 'name': 'Novari earn-out (maximum)',
  'when': fact('2027-07-04', 'S', 'S21', S['S21']),
  'probability': fact(round(3.8 / 4.5, 4), 'S', 'S20', S['S20']),
  'amount': fact(-4.5, 'A', 'A49', 'Novari: "remaining potential performance-based consideration payable of up to $4,500,000 ... in the 24-month period following the acquisition. A balance of $3,800,000 is accrued".', 'D2', '3,800,000')},
 {'kind': 'cash', 'name': 'Buddy earn-out (maximum)',
  'when': fact('2029-01-10', 'S', 'S21', S['S21']),
  'probability': fact(round(3.205624 / 7.248555, 4), 'S', 'S20', S['S20']),
  'amount': fact(-7.248555, 'A', 'A51', 'Buddy: "remaining potential performance-based consideration payable of up to $7,248,555, if certain revenue targets are met in the 30-month period following the acquisition"; fair value at close C$3,205,624.', 'D2', '7,248,555')},
]
csa = {'base': csa_base}

# ---------------- finagle leaves (forecast-only; Finagle not run) ----------------
def growth_list(series, start):
    out, prev = [], start
    for y in YRS:
        out.append(round(series[y] / prev - 1, 9)); prev = series[y]
    return out

organic = {
 'revenue': {'FY25A': fact(108.966918, 'A', 'A1', 'Revenue FY2025: C$108,966,918.', 'D3', '108,966,918'), **{y: rev_tot[y] for y in YRS}},
 'ebitda': {'FY25A': fact(26.554099, 'A', 'A2', 'Adjusted EBITDA FY2025: C$26,554,099.', 'D3', '26,554,099'), **{y: eb_tot[y] for y in YRS}},
}
finagle = {
 'ebitda_basis': fact('total', 'C', 'C20', 'Leaves are on totals: Buddy (closed 10 Jul 2026) sits inside the term line and the cost build; no acquisition after it is forecast. The same basis goes to Finagle for every case (P9).', inputs=['A45', 'P9']),
 'acquisition_disclosure': {'status': fact('none', 'C', 'C21', 'No future acquisition is forecast. Management hopes to close another deal before year-end (G12) but none is announced; announced-but-unclosed deals are excluded.', inputs=['G12'])},
 'sales_growth': fact(growth_list(rev_base, 108.966918), 'C', 'C22', 'Revenue growth FY2026E-FY2029E on totals; compounds to the base revenue.', inputs=['E1', 'A1']),
 'ebitda_growth': fact(growth_list(ebitda_base, 26.554099), 'C', 'C23', 'Adjusted EBITDA growth FY2026E-FY2029E on totals; compounds to the base EBITDA.', inputs=['E2', 'A2']),
 'me': fact(round(BASEV['FY29E'][1] / BASEV['FY29E'][0], 6), 'C', 'C24', 'me = FY2029E Adjusted EBITDA %.3f / revenue %.3f = %.1f%% (event-adjusted Consensus).' % (BASEV['FY29E'][1], BASEV['FY29E'][0], 100 * BASEV['FY29E'][1] / BASEV['FY29E'][0]), inputs=['C36']),
 'mc': fact(0.50, 'S', 'S16', S['S16']),
 'gsnext': fact(round(gsnext, 6), 'S', 'S6', 'gsnext = FY2030 one more year of the same build on the scaled FY2029 lines (organic ARR adds 11.89, virtual care -5%%, perpetual flat, services 16.5%% of term) = %.3f / %.3f - 1. %s' % (NY, rev_base['FY29E'], S['S6'])),
}

# ---------------- scenarios ----------------
scen = {}
for c in ('bull', 'bear'):
    sl, srev, seb = SC[c]
    lj = []
    for k in ('term', 'vc', 'perp', 'svc'):
        name, pat = LINE_META[k]
        per = {}
        for p in ('FY24A', 'FY25A', '9M26A'):
            src = lines_json[[x for x in ('term', 'vc', 'perp', 'svc')].index(k)]['periods'][per_key(p)]
            per[per_key(p)] = src
        per['Q4E'] = fact(r(sl[k]['Q4E']), 'C', 'C25', '%s %s Q4 2026E = base + (%s bottom-up - base bottom-up).' % (c, name, c), inputs=['C1', 'S18', 'S22'])
        for y in YRS:
            per[y] = fact(r(sl[k][y]), 'C', 'C25', '%s %s %s = base line + lever difference (S18).' % (c, name, y), inputs=['C2', 'S18', 'S22'])
        lj.append({'name': name, 'pattern': pat, 'periods': per})
    stot_r = {'FY24A': rev_tot['FY24A'], 'FY25A': rev_tot['FY25A'], '9MA': rev_tot['9MA'],
              'Q4E': fact(r(srev['Q4E']), 'C', 'C26', '%s Q4 2026E revenue.' % c, inputs=['C5', 'S18'])}
    stot_e = {'FY24A': eb_tot['FY24A'], 'FY25A': eb_tot['FY25A'], '9MA': eb_tot['9MA'],
              'Q4E': fact(r(seb['Q4E']), 'C', 'C26', '%s Q4 2026E Adjusted EBITDA.' % c, inputs=['C5', 'S18'])}
    for y in YRS:
        stot_r[y] = fact(r(srev[y]), 'C', 'C26', '%s revenue %s = base %.3f + bottom-up lever difference.' % (c, y, BASEV[y][0]), inputs=['E1', 'S18', 'S22'])
        stot_e[y] = fact(r(seb[y]), 'C', 'C26', '%s Adjusted EBITDA %s = base %.3f + bottom-up lever difference.' % (c, y, BASEV[y][1]), inputs=['E2', 'S18', 'S13', 'S14'])
    # re-sum lines to totals exactly (rounding)
    org = {'revenue': {'FY25A': organic['revenue']['FY25A'], **{y: stot_r[y] for y in YRS}},
           'ebitda': {'FY25A': organic['ebitda']['FY25A'], **{y: stot_e[y] for y in YRS}}}
    sr = {y: stot_r[y]['value'] for y in YRS}; se = {y: stot_e[y]['value'] for y in YRS}
    fin = {
      'sales_growth': fact(growth_list(sr, 108.966918), 'C', 'C27', '%s revenue growth on totals.' % c, inputs=['C26']),
      'ebitda_growth': fact(growth_list(se, 26.554099), 'C', 'C27', '%s EBITDA growth on totals.' % c, inputs=['C26']),
      'me': fact(round(se['FY29E'] / sr['FY29E'], 6), 'C', 'C27', '%s me = FY2029E EBITDA / revenue.' % c, inputs=['C26']),
      'ebitda_basis': finagle['ebitda_basis'],
      'acquisition_disclosure': finagle['acquisition_disclosure'],
      'mc': fact(0.60 if c == 'bull' else 0.40, 'S', 'S16', S['S16']),
      'gsnext': fact(round(gsnext_s[c], 6), 'S', 'S6', '%s gsnext: FY2030 one more year of the %s build (organic ARR adds %.2f).' % (c, c, M.CASES[c]['adds_next'])),
    }
    scen[c] = {'description': {'bull': '1.5 of SHREWD ARR rolls off in 2027; organic ARR +2.5 in Q4 2026, then dollar adds +15% a year (9.34/10.74/12.35); no FDP procurement revenue; variable opex 20%; Buddy saving 1.0; Attend Anywhere flat.',
                               'bear': 'All SHREWD ARR (8.0) lost during 2027; organic ARR +0.5 in Q4 2026, then flat dollar adds of 7.23 a year; variable opex 40%; no Buddy saving; Attend Anywhere -15% a year. Bands the above-history consensus margin.'}[c],
               'lines': lj, 'totals': {'revenue': stot_r, 'ebitda': stot_e}, 'organic': org, 'finagle': fin}

# ---------------- assemble ----------------
import extra_notes; extra_notes.add(note, _page)
fc = {
 'ticker': 'VHI', 'company': 'Vitalhub Corp. (TSX: VHI)', 'currency': 'CAD', 'units': 'C$ millions unless noted; shares in millions',
 'as_of': '2026-11-17', 'fiscal_year_end': 'December 31', 'baseline_period': 'FY25A', 'explicit_periods': YRS,
 'stub_of': {'9MA': 'FY26E', 'Q4E': 'FY26E'}, 'finagle_handoff': True,
 'horizon_note': fact('FY2026E-FY2029E', 'P', 'P1', P['P1']),
 'method_commit': 'mtlr05/forecaster 3a46f0a61f6b26de1a588acbc941120420d2ec41',
 'source_mirror': 'mtlr05/ceochat 8f8b44fc8252e9f8f7f4982342c1f189fb584fef companies/vhi/ (SEDAR filings via OTC Markets; PDFs re-downloaded from OTC Markets for page numbers)',
 'lines': lines_json, 'totals': totals, 'history': history, 'views': views, 'costs': costs,
 'year0': year0, 'cash_share_adjustments': csa, 'scenarios': scen,
 'finagle': finagle, 'organic': organic,
 'arr_path': {c: {y: fact(r(B[c]['arr_end'][y]), 'C', 'C28', '%s closing ARR %s from organic adds (S2-S5, S22); FX zero.' % (c, y), inputs=['A26', 'S2', 'S3', 'S4', 'S5', 'S22']) for y in YRS} for c in B},
 'sources': sources,
}
# C sources need inputs that exist; make sure referenced inputs resolve
ids = {s['id'] for s in sources}
for s in sources:
    if s['id'].startswith('C'):
        s['inputs'] = [i for i in s.get('inputs', []) if i in ids] or ['D1']
(H / 'forecast.json').write_text(json.dumps(fc, indent=1, ensure_ascii=False), encoding='utf-8')

# numbers for report
num = {
 'cons': CONS, 'rev_base': rev_base, 'ebitda_base': ebitda_base, 'L': L, 'F': F,
 'B': {c: {k: v for k, v in B[c].items() if k != 'params'} for c in B},
 'SC': {c: {'lines': SC[c][0], 'rev': SC[c][1], 'ebitda': SC[c][2]} for c in SC},
 'NY_parts': NY_parts, 'NY': NY, 'gsnext': gsnext, 'gsnext_s': gsnext_s, 'buddyQ4': buddyQ4,
 'costs': {k: {kk: vv['value'] for kk, vv in v.items()} for k, v in costs['bridge_at_base_revenue'].items()},
}
(H / 'work' / 'numbers.json').write_text(json.dumps(num, indent=1), encoding='utf-8')

with open(H / 'drivers.csv', 'w', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['driver', 'tag', 'base', 'bull', 'bear', 'FY26E', 'FY27E', 'FY28E', 'FY29E', 'note'])
    for c in ('base', 'bull', 'bear'):
        w.writerow(['closing ARR (%s)' % c, 'C28', '', '', ''] + [round(B[c]['arr_end'][y], 3) for y in YRS] + ['organic adds; FX zero'])
    w.writerow(['Q4 2026 organic ARR add', 'S2', 1.5, 2.5, 0.5, '', '', '', '', ''])
    for c in ('base', 'bull', 'bear'):
        w.writerow(['organic ARR adds before SHREWD (%s)' % c, 'S3-S6,S22,S29', '', '', ''] + [M.CASES[c]['q4_org']] + [round(a, 3) for a in M.CASES[c]['adds']] + ['dollars; FY26E column = Q4 2026 add; FY30E %.3f' % M.CASES[c]['adds_next']])
    w.writerow(['organic adds growth a year (dollars)', 'S29', '10%', '15%', '0%', '', '', '', '', 'anchor 8.123 = four quarters to Q2 2026; v2 used 9/10/10% of opening ARR'])
    w.writerow(['SHREWD ARR roll-off in 2027 (straight-line)', 'S26,S22', 4.0, 1.5, 8.0, '', '', '', '', 'none in 2028-29; SHREWD ARR 7.5-8.6 (midpoint 8.0); v2 17 Nov 2026'])
    w.writerow(['lost SHREWD revenue fall-through to EBITDA', 'S27', '80%', '80%', '80%', '', '', '', '', 'saves only cash cost of sales'])
    w.writerow(['event adjustment to Consensus revenue', 'C36', '', '', '', 0.0, round(ADJ['FY27E'][0], 3), round(ADJ['FY28E'][0], 3), round(ADJ['FY29E'][0], 3), 'FDP extension 16 Nov 2026'])
    w.writerow(['event adjustment to Consensus Adj. EBITDA', 'C36', '', '', '', 0.0, round(ADJ['FY27E'][1], 3), round(ADJ['FY28E'][1], 3), round(ADJ['FY29E'][1], 3), 'FDP extension 16 Nov 2026'])
    w.writerow(['term revenue / average ARR', 'S1', 0.985, 0.985, 0.985, '', '', '', '', 'band 0.975-0.995'])
    w.writerow(['virtual care growth', 'S7', '-5%', '0%', '-15%', '', '', '', '', 'from FY2027'])
    w.writerow(['services % of term', 'S9', '16.5%', '16.5%', '16.5%', '', '', '', '', 'band 15-19%'])
    w.writerow(['perpetual a year', 'S8', 2.0, 2.0, 2.0, '', '', '', '', 'Q4 2026 0.5'])
    w.writerow(['cash gross margin', 'S10', '80%', '80%', '80%', '', '', '', '', 'band 78-82%'])
    w.writerow(['core opex inflation', 'S12', '2%', '2%', '2%', '', '', '', '', 'band 1-3%'])
    w.writerow(['variable opex rate', 'S13', '30%', '20%', '40%', '', '', '', '', ''])
    w.writerow(['Buddy cost saving a year', 'S14', 0.5, 1.0, 0.0, '', '', '', '', 'from FY2027'])
    w.writerow(['organic scale factor to event-adjusted Consensus', 'C1/C2', '', '', '', round(F['Q4E'], 4), round(F['FY27E'], 4), round(F['FY28E'], 4), round(F['FY29E'], 4), 'FY26E column = Q4 factor'])
print('ok', len(sources), 'sources; gsnext', round(gsnext, 4), {c: round(v, 4) for c, v in gsnext_s.items()})
print('F', {k: round(v, 4) for k, v in F.items()})
