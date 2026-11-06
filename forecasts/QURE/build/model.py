"""QURE v11 (rev4) quarterly AMT-130 US pool model, m = 0.62 (David t97u 2026-10-30), capacity = CLPT AMT-130 ramp.
Same method as /workspace/out/AMT130_demand/scratch_m62/run25.py sim(): pool S, entrants E, leave m/4*S, demand u/4*S with
u = P(m+g)/(1-P), treated = min(capacity, demand, S). Interface (run/annual/refill/qname, keys) kept from the v10 model.py.
UK (bull only) is the v10 UK logic, unchanged."""
US_POP = 340.0
INC = {'base': 1.22, 'bull': 1.59}            # per 100k/yr (amt130_pool_model.py inputs) [S/A]
SHARE = {'base': 0.90, 'bull': 0.95}          # share of incident cases entering the early-manifest pool [S]
HAIR = {'base': dict(ref=0.90, will=0.90, cov=0.90), 'bull': dict(ref=0.95, will=0.95, cov=0.95)}
M_LEAVE = 0.62                                 # progression 0.60 + death 0.02 per yr [P David t97u]
G = 0.005                                      # entrant growth / yr
POOL0 = 6000.0                                 # uniQure slide 25 [G]
CLPT = {'base': (330, 2500, 3000), 'bull': (880, 4500, 3500)}   # FY27 (half year), FY28, cap/yr from FY29 [S, CLPT model]
CPW = 2.0                                      # procedures/center/week used only to express capacity as a center count (opex) [S]
WEEKS_Q = 13.0
BACKLOG0 = POOL0
# base entrant filter f: holds the steady pool at the 6,000 start pool, f = 6000*(m+g)/E(2026) = 1.0045 (run16.py case A, the reference run) [C]; bull unfiltered (f = 1) [S]
FILT = {'base': POOL0*(M_LEAVE+G)/(INC['base']/1e5*US_POP*1e6*SHARE['base']), 'bull': 1.0}
# v10 UK (bull only), unchanged
ATTR = 0.10
UK = dict(start_q=4, backlog=0.30*7500, pop=69.0, centers=[3, 6, 9, 12, 15], thr=13/3.0, price=1.5)
UK_INC, UK_H = 0.48, dict(elig=0.90, will=0.95, cov=0.95)
def P(n): h = HAIR[n]; return h['ref']*h['will']*h['cov']
def entrants(n, y): return INC[n]/1e5*US_POP*1e6*(1+G)**(y-2026)*SHARE[n]*FILT[n]
def refill(n):   # (incident cases, eligible entrants) in 2026 terms
    new = INC[n]/1e5*US_POP*1e6; return new, new*SHARE[n]
def qname(i):
    y = 2027+(i+2)//4; q = (i+2) % 4+1; return y, q
def capq(n, y):
    a, b, c = CLPT[n]; return a/2 if y == 2027 else (b/4 if y == 2028 else c/4)
def run(n, nq=60, delay=0, refill_override=None):
    if n == 'bear': return []
    m, p = M_LEAVE, P(n); u = p*(m+G)/(1-p); S = POOL0; rows = []
    ukback = UK['backlog']; ukrf = UK_INC/1e5*UK['pop']*1e6*UK_H['elig']*UK_H['will']*UK_H['cov']
    for i in range(nq):
        y, q = qname(i); j = i-delay
        E = entrants(n, y)/4 if refill_override is None else refill_override/4
        if j < 0:
            L = m/4*S; S = S+E-L
            rows.append(dict(y=y, q=q, centers=0, thr=0, util=0, cap=0, refill=E, entrants=E, demand=u/4*S, leave=L, treated=0, backlog=S, uk=dict(cap=0, treated=0, back=0))); continue
        yj = qname(j)[0]; cap = capq(n, yj)
        D = u/4*S; T = min(cap, D, S); L = m/4*S
        S = S+E-L-T
        uk = dict(cap=0, treated=0, back=0)
        if n == 'bull' and i >= UK['start_q']:
            k = min(i-UK['start_q'], len(UK['centers'])-1); ucap = UK['centers'][k]*UK['thr']*3
            ud = ukback+ukrf/4; ut = min(ucap, ud); ukback = (ud-ut)*(1-ATTR/4)
            if ukback < 1e-6: ucap = ukrf/4; ut = min(ucap, ud); ukback = 0.0
            uk = dict(cap=ucap, treated=ut, back=ukback)
        rows.append(dict(y=y, q=q, centers=cap/(CPW*WEEKS_Q), thr=CPW, util=T/cap if cap else 0, cap=cap, refill=E, entrants=E, demand=D, leave=L, treated=T, backlog=S, uk=uk))
    return rows
def annual(n, years=range(2026, 2041), **kw):
    R = run(n, **kw); out = {}; cum = 0
    for Y in years:
        rr = [r for r in R if r['y'] == Y]
        d = dict(cap=sum(r['cap'] for r in rr), refill=sum(r['refill'] for r in rr), treated=sum(r['treated'] for r in rr),
                 demand=sum(r['demand'] for r in rr), leave=sum(r['leave'] for r in rr),
                 backlog_end=rr[-1]['backlog'] if rr else (POOL0 if n != 'bear' else 0), centers_end=rr[-1]['centers'] if rr else 0,
                 uk_cap=sum(r['uk']['cap'] for r in rr), uk_treated=sum(r['uk']['treated'] for r in rr), uk_back=rr[-1]['uk']['back'] if rr else 0)
        cum += d['treated']; d['cum'] = cum; out[Y] = d
    return out
if __name__ == '__main__':
    for n in ('base', 'bull'):
        print(n, 'P', P(n), 'entrants2027', entrants(n, 2027), 'steady pool', entrants(n, 2026)/(M_LEAVE+G))
        for Y, d in annual(n, years=range(2027, 2036)).items(): print(Y, {k: round(v) for k, v in d.items()})
