"""VHI bottom-up model and scenario levers (C$ millions). Imported by build_forecast.py."""
Q_ANN = 4
# ---- reported history (C$ millions) ----
FY = {
 'FY24A': dict(term=57.070350, vc=0.0, perp=0.498274, svc=11.025686, rev=68.594310, ebitda=17.840272),
 'FY25A': dict(term=85.442864, vc=5.184921, perp=2.089242, svc=16.249891, rev=108.966918, ebitda=26.554099),
 '9M26A': dict(term=74.252927, vc=7.018965, perp=1.944450, svc=12.341147, rev=95.557489, ebitda=24.772636),
}
Q = ['Q3FY24','Q4FY24','Q1FY25','Q2FY25','Q3FY25','Q4FY25','Q1FY26','Q2FY26','Q3FY26']
QH = {
 'rev':   [16.509135,20.590779,21.674966,23.857548,32.044030,31.390374,31.906402,31.737512,31.913575],
 'ebitda':[4.554597,5.046758,5.614686,6.304647,7.206257,7.428508,7.989761,8.162917,8.619958],
 'term':  [13.892323,17.673596,18.343566,19.894544,23.627391,23.577363,23.927139,24.542042,25.783746],
 'vc':    [0,0,0,0.324477,2.479354,2.381090,2.398653,2.282218,2.338094],
 'perp':  [0.293397,0.060875,0.157183,0.965281,0.454565,0.512213,0.995851,0.808087,0.140512],
 'svc':   [2.323415,2.856308,3.174217,2.673246,5.482720,4.919708,4.584759,4.105165,3.651223],
 'arr':   [53.452108,71.054210,73.687666,79.589081,93.693789,96.149750,99.078809,101.533157,107.194390],
 'arr_org':[1.081181,2.609657,1.777442,1.860849,1.711335,1.881405,2.729378,1.802495,0.815535],
 'arr_acq':[0,14.6,0,3.87,12.0,0,0,0,4.48],
 'fx_loss':[-0.323458,0.384805,-0.694407,-0.353294,0.069042,0.316191,0.238091,0.222984,-0.592126],
 'cogs':  [3.215845,3.841539,4.230673,4.499328,6.162109,6.486447,5.861731,5.844566,6.724559],
 'opex':  [None,None,None,None,None,17.157418,17.816819,16.782093,17.196952],
}
# ---- method inputs ----
ARR_Q3 = 107.194390
BUDDY_ARR = 4.48
TERM_RATIO = 0.985          # term revenue / average closing ARR (Q2-Q3 2026 average)
GM = 0.80                   # cash gross margin (cost of sales has no D&A)
CORE_OPEX_Q3 = 17.196952    # G&A + S&M + R&D, Q3 2026, ex SBC/D&A/FX/one-time
REV_Q3_ANN = 31.913575*4
INFL = 0.02
SVC_RATIO = 0.165           # services/hardware/other as % of term revenue (9M 2026 = 16.6%)
PERP = 2.0
PERP_Q4 = 0.5
SVC_Q4 = 4.6
BUDDY_STUB_DAYS = 174       # 10 Jul - 31 Dec 2026
YEARS = ['FY26E','FY27E','FY28E','FY29E']

# v2 (17 Nov 2026, after the FDP extension to March 2029): g is organic ARR growth before SHREWD;
# loss is SHREWD ARR rolling off during each year (FY27, FY28, FY29), straight-line inside the year.
SHREWD_ARR = 8.0            # midpoint of 7-8% x 107.194 = 7.5-8.6
# v3 (18 Nov 2026): organic ARR adds are forecast in dollars, not as a % of a base swollen by acquisitions.
# Anchor: organic adds in the four quarters to Q2 2026, before the Q3 SHREWD drag = 1.711+1.881+2.729+1.802 = 8.123.
ADDS_ANCHOR = 8.123
ADDS_FY25 = 7.231          # printed FY2025 organic net of churn
def _adds(g, n=4):
    return [round(ADDS_ANCHOR*(1+g)**k, 6) for k in range(1, n+1)]
CASES = {
 'base': dict(q4_org=1.5, adds=_adds(0.10)[:3], adds_next=_adds(0.10)[3], loss=[4.0,0.0,0.0], vc=-0.05, var=0.30, syn=0.5),
 'bull': dict(q4_org=2.5, adds=_adds(0.15)[:3], adds_next=_adds(0.15)[3], loss=[1.5,0.0,0.0], vc=0.0,  var=0.20, syn=1.0),
 'bear': dict(q4_org=0.5, adds=[ADDS_FY25]*3, adds_next=ADDS_FY25, loss=[8.0,0.0,0.0], vc=-0.15, var=0.40, syn=0.0),
}
# v2 (17 Nov 2026 10:05): organic growth as a % before SHREWD; kept for the change log.
CASES_V2 = {
 'base': dict(q4_org=1.5, g=[0.09,0.10,0.10], loss=[4.0,0.0,0.0], g_next=0.10, vc=-0.05, var=0.30, syn=0.5),
 'bull': dict(q4_org=2.5, g=[0.10,0.11,0.11], loss=[1.5,0.0,0.0], g_next=0.11, vc=0.0,  var=0.20, syn=1.0),
 'bear': dict(q4_org=0.5, g=[0.07,0.06,0.07], loss=[8.0,0.0,0.0], g_next=0.07, vc=-0.15, var=0.40, syn=0.0),
}
# v1 (first case, 17 Nov 2026 morning): SHREWD unresolved, no explicit roll-off; kept to size the event adjustment.
CASES_V1 = {
 'base': dict(q4_org=1.5, g=[0.08,0.10,0.10], loss=[0,0,0], g_next=0.10, vc=-0.05, var=0.30, syn=0.5),
 'bull': dict(q4_org=2.5, g=[0.10,0.11,0.11], loss=[0,0,0], g_next=0.11, vc=0.0,  var=0.20, syn=1.0),
 'bear': dict(q4_org=0.5, g=[0.02,0.06,0.07], loss=[0,0,0], g_next=0.07, vc=-0.15, var=0.40, syn=0.0),
}

def build(case, params=None):
    p = params or CASES[case]
    out = {}
    # ARR path (organic adds; FX held at zero)
    a_q3 = ARR_Q3
    a_q4 = a_q3 + p['q4_org']
    ends = {'FY26E': a_q4}
    prev = a_q4
    if 'adds' in p:
        for y, a, l in zip(YEARS[1:], p['adds'], p['loss']):
            ends[y] = prev + a - l; prev = ends[y]
        ends['FY30E'] = prev + p['adds_next']
    else:
        for y, g, l in zip(YEARS[1:], p['g'], p['loss']):
            ends[y] = prev * (1 + g) - l; prev = ends[y]
        ends['FY30E'] = prev * (1 + p['g_next'])
    # term revenue
    buddy = {'FY26E': BUDDY_ARR*TERM_RATIO*BUDDY_STUB_DAYS/365}
    for y in YEARS[1:]+['FY30E']: buddy[y] = BUDDY_ARR*TERM_RATIO
    term_q4 = TERM_RATIO*(a_q3+a_q4)/2/4
    term = {'Q4E': term_q4, 'FY26E': FY['9M26A']['term'] + term_q4}
    prevend = a_q4
    for y in YEARS[1:]+['FY30E']:
        term[y] = TERM_RATIO*(prevend+ends[y])/2; prevend = ends[y]
    # VC
    vc_q4 = 2.338094
    vc = {'Q4E': vc_q4, 'FY26E': FY['9M26A']['vc']+vc_q4}
    prev = vc['FY26E']
    for y in YEARS[1:]+['FY30E']:
        vc[y] = prev*(1+p['vc']); prev = vc[y]
    perp = {'Q4E': PERP_Q4, 'FY26E': FY['9M26A']['perp']+PERP_Q4}
    svc = {'Q4E': SVC_Q4, 'FY26E': FY['9M26A']['svc']+SVC_Q4}
    for y in YEARS[1:]+['FY30E']:
        perp[y] = PERP; svc[y] = SVC_RATIO*term[y]
    rev = {k: term[k]+vc[k]+perp[k]+svc[k] for k in term}
    # revenue lost to SHREWD roll-off (average ARR lost x term ratio, plus the services that ride on it)
    lost_rev = {}; cum = 0.0
    for y, l in zip(YEARS[1:], p['loss']):
        lost_rev[y] = TERM_RATIO*(cum + l/2)*(1+SVC_RATIO); cum += l
    lost_rev['FY30E'] = TERM_RATIO*cum*(1+SVC_RATIO)
    # cost build
    core = {}; var = {}; syn = {}; cogs = {}; ebitda = {}
    q4rev = rev['Q4E']
    cogs['Q4E'] = (1-GM)*q4rev
    core['Q4E'] = CORE_OPEX_Q3
    var['Q4E'] = p['var']*max(0.0, q4rev*4-REV_Q3_ANN)/4
    syn['Q4E'] = 0.0
    ebitda['Q4E'] = q4rev - cogs['Q4E'] - core['Q4E'] - var['Q4E']
    ebitda['FY26E'] = FY['9M26A']['ebitda'] + ebitda['Q4E']
    for i, y in enumerate(YEARS[1:]+['FY30E'], start=1):
        cogs[y] = (1-GM)*rev[y]
        core[y] = CORE_OPEX_Q3*4*(1+INFL)**i
        syn[y] = -p['syn']   # negative cost = saving
        # lost SHREWD revenue saves only cash cost of sales, not opex (G14: 1 of ARR ~ 1 point of EBITDA if costs are not added)
        var[y] = p['var']*(rev[y]+lost_rev[y]-REV_Q3_ANN)
        ebitda[y] = rev[y]-cogs[y]-core[y]-syn[y]-var[y]
    return dict(arr_end=ends, term=term, buddy=buddy, vc=vc, perp=perp, svc=svc, rev=rev,
                cogs=cogs, core=core, var=var, syn=syn, ebitda=ebitda, lost_rev=lost_rev, params=p)

def cost_at(rev, year_index, case='base'):
    """Bottom-up cash cost of a given revenue in an explicit year (year_index 1..3 for FY27-29)."""
    p = CASES[case]
    return (1-GM)*rev + CORE_OPEX_Q3*4*(1+INFL)**year_index - p['syn'] + p['var']*(rev-REV_Q3_ANN)

if __name__ == '__main__':
    for c in CASES:
        b = build(c)
        print(c, {k: round(v,2) for k,v in b['rev'].items()}, {k: round(v,2) for k,v in b['ebitda'].items()})
        print('  arr', {k: round(v,2) for k,v in b['arr_end'].items()})
        print('  margin', {k: round(b['ebitda'][k]/b['rev'][k]*100,1) for k in b['rev']})
