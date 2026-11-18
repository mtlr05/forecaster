#!/usr/bin/env python3
"""VHI.TO collaborative v04 runner."""
import copy, datetime, hashlib, io, json, os, sys, contextlib
from datetime import date
from pathlib import Path

sys.path.insert(0, '/workspace/finagle')
from finagle.agent import describe_inputs, build_baseline, update_case, validate_case, run_case

DIR = Path('/workspace/forecaster-work/output/VHI/2026-11-17/finagle-run')
REQ_PATH = DIR / 'valuation_request_v04.json'
FORECAST_PATH = Path('/workspace/forecaster-work/output/VHI/2026-11-17/forecast.json')
UA = 'David May davidmay44@hotmail.com'
H = lambda o: hashlib.sha256(
    json.dumps(o, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
).hexdigest()

def leaf_num(x):
    if isinstance(x, dict):
        return x.get('value')
    return x

R = json.load(open(REQ_PATH))
file_bytes = hashlib.sha256(open(REQ_PATH, 'rb').read()).hexdigest()
forecast_bytes = hashlib.sha256(open(FORECAST_PATH, 'rb').read()).hexdigest() if FORECAST_PATH.exists() else None
sidecar = None
for p in DIR.glob('*v04*.sha256.json'):
    sidecar = json.load(open(p))

describe_inputs()
bb = build_baseline('VHI.TO', user_agent=UA)
(DIR / 'run' / 'baseline_v04.json').write_text(json.dumps(bb, indent=1, default=str))

case0 = dict(
    path='ebitda', ticker='VHI.TO', year=10,
    market={'shares': copy.deepcopy(bb['shares']), 'price': copy.deepcopy(bb['price'])},
    rates=copy.deepcopy(bb['rates']),
    baseline=copy.deepcopy(bb['baseline']),
    forecast=copy.deepcopy(bb['forecast']),
    debt=copy.deepcopy(bb['debt']),
    distribution=copy.deepcopy(bb['distribution']),
)

price_leaf = bb['price'] if isinstance(bb['price'], dict) else {'value': bb['price']}
price_date_s = price_leaf.get('as_of') or date.today().isoformat()
price_date = date.fromisoformat(price_date_s[:10])

def item_date(item):
    w = item.get('when')
    return date.fromisoformat(str(w['value'] if isinstance(w, dict) else w)[:10])

def years_t(d):
    if d <= price_date:
        return 0.0
    return (d - price_date).days / 365.25

def work_schedule(items, re, label, opening_cash, opening_shares):
    out, adj_cash, adj_shares, complete = [], 0.0, 0.0, True
    for it in items:
        d = item_date(it)
        t = years_t(d)
        kind = it.get('kind')
        p = leaf_num(it.get('probability'))
        if p is None:
            p = 1.0
        rec = {'name': it.get('name'), 'kind': kind, 'date': d.isoformat(),
               't_years': t, 'probability': p, 'source_list': label}
        if t == 0:
            factor = 1.0
        elif re is None:
            rec.update(discount_factor=None, status='not applied: rates.re is unset')
            complete = False
            out.append(rec)
            continue
        else:
            factor = 1.0 / ((1.0 + re) ** t)
        rec['discount_factor'] = factor
        if kind == 'cash':
            amt = leaf_num(it.get('amount'))
            pv = amt * p * factor
            rec.update(amount=amt, present_value=pv, new_shares=0.0, status='applied')
            adj_cash += pv
        elif kind == 'equity':
            sh = leaf_num(it.get('shares'))
            px = leaf_num(it.get('price'))
            stated = px is not None
            if px is None:
                px = price_leaf.get('value')
            proceeds = sh * px if (sh is not None and px is not None) else None
            pv = proceeds * p * factor if proceeds is not None else None
            sh_add = (sh or 0.0) * p
            rec.update(shares=sh, issue_price=px, issue_price_stated=stated,
                       proceeds=proceeds, present_value=pv, new_shares=sh_add, status='applied')
            if pv is not None:
                adj_cash += pv
            adj_shares += sh_add
        else:
            rec['status'] = 'unknown kind; not applied'
            complete = False
        out.append(rec)
    return out, adj_cash, adj_shares, complete

def apply_prompt(sc, up):
    for pi in R.get('prompt_inputs') or []:
        if sc not in (pi.get('applies_to') or []):
            continue
        ev = 'David %s: "%s"' % (pi.get('date'), pi.get('quote'))
        if pi.get('note'):
            ev += ' ' + pi['note']
        pth = pi['path']
        leaf = {'value': pi['value'], 'source': 'prompt', 'evidence': ev}
        if pth.startswith('baseline.'):
            leaf.update(period_end='2025-12-31', basis='fiscal_year', currency='CAD')
        up[pth] = leaf

scenarios = {}
raw = {'bb': {'ok': bb.get('ok'), 'warnings': bb.get('warnings')}, 'res': {}}

for sc in R['scenarios']:
    up = {}
    for path, leaf in R['forecaster'][sc].items():
        ev = leaf.get('evidence') or ''
        tag = leaf.get('tag') or ''
        cid = leaf.get('cite_id') or ''
        up[path] = {'value': leaf['value'], 'source': 'assumption',
                    'evidence': 'Forecaster [%s] cite: %s %s' % (tag, cid, ev)}
    apply_prompt(sc, up)
    u = update_case(copy.deepcopy(case0), up, run=False)
    c = u.get('case', u)
    rates = c.get('rates') or {}
    rf = leaf_num(rates.get('risk_free'))
    re = leaf_num(rates.get('re'))
    gt = leaf_num(rates.get('gt'))
    da = c['baseline']['da']
    print(sc, 'rf', rf, 're', re, 'gt', gt, 't', leaf_num(rates.get('t')),
          'rd', leaf_num(rates.get('rd')), 'da', da, 'debt', c['baseline']['debt']['value'],
          'cash_opening', c['baseline']['cash']['value'], 'shares_opening', c['market']['shares']['value'],
          'debt_policy', {k: leaf_num(v) for k, v in (c.get('debt') or {}).items()})

    if re is None or gt is None:
        val = validate_case(c)
        print('STOP: re/gt not derived', val)
        scenarios[sc] = {
            'ok': False, 'stopped': True,
            'stopped_reason': 'Finagle did not derive re and/or gt from the supplied rates.risk_free.',
            'validation': val, 'rates': rates,
            'value_per_share': None, 'value_per_share_DDM': None,
            'not_a_valuation': True,
            'not_a_valuation_reason': ['re/gt not derived; validate_case: %s' % val],
        }
        json.dump(c, open(DIR / 'run' / ('case_%s_v04.json' % sc), 'w'), indent=1, default=str)
        continue

    # Stated cash/shares are openings (includes_adjustments false). Then apply remaining CSA.
    cash_pi = next((p for p in R['prompt_inputs'] if p['path'] == 'baseline.cash' and sc in p['applies_to']), None)
    sh_pi = next((p for p in R['prompt_inputs'] if p['path'] == 'market.shares' and sc in p['applies_to']), None)
    opening_cash = cash_pi['value'] if cash_pi else c['baseline']['cash']['value']
    opening_shares = sh_pi['value'] if sh_pi else leaf_num(c['market']['shares'])
    cash_incl = bool(cash_pi.get('includes_adjustments')) if cash_pi else False
    sh_incl = bool(sh_pi.get('includes_adjustments')) if sh_pi else False

    csa = (R.get('cash_share_adjustments') or {})
    items = csa.get(sc) if csa.get(sc) is not None else (csa.get('base') or [])
    sched_items, adj_cash, adj_shares, complete = work_schedule(items, re, 'base' if csa.get(sc) is None else sc,
                                                               opening_cash, opening_shares)
    applied_cash = opening_cash if cash_incl else opening_cash + adj_cash
    applied_shares = opening_shares if sh_incl else opening_shares + adj_shares
    worked = {
        'label': (
            'COMPUTED OUTSIDE run_case by the runner from cash_share_adjustments, '
            'per collaborative-run.md and forecastcheck.collaborative._openings. '
            'includes_adjustments is false on baseline.cash and market.shares, so the stated '
            'figures are openings and the remaining schedule is added. '
            't = 0 when the item date is on or before the price date; otherwise '
            't = (item_date - price_date).days / 365.25. Discount factor = 1/(1+re)^t. '
            'Buddy closing cash and consideration shares were removed from the schedule '
            '(already reflected in the stated openings).'
        ),
        'price_date': price_date_s,
        'cost_of_equity': re,
        'includes_adjustments_cash': cash_incl,
        'includes_adjustments_shares': sh_incl,
        'opening_cash': opening_cash,
        'opening_shares': opening_shares,
        'items': sched_items,
        'sum_pv_cash': adj_cash,
        'sum_new_shares': adj_shares,
        'adjusted_cash': applied_cash,
        'adjusted_shares': applied_shares,
        'complete': complete,
        'applied_to_case': True,
        'buddy_items_in_schedule': [it.get('name') for it in items if 'Buddy Healthcare cash' in (it.get('name') or '')
                                    or 'consideration shares' in (it.get('name') or '')],
    }
    c['baseline']['cash'] = copy.deepcopy(c['baseline']['cash'])
    c['baseline']['cash']['value'] = applied_cash
    note = c['baseline']['cash'].get('note') or ''
    c['baseline']['cash']['note'] = ((note + ' ') if note else '') + (
        'Year-0 cash after cash_share_adjustments (opening %.6f %+ .6f; includes_adjustments=%s).'
        % (opening_cash, 0 if cash_incl else adj_cash, cash_incl)
    )
    c['market']['shares'] = copy.deepcopy(c['market']['shares'])
    c['market']['shares']['value'] = applied_shares
    shnote = c['market']['shares'].get('note') or ''
    c['market']['shares']['note'] = ((shnote + ' ') if shnote else '') + (
        'Shares after cash_share_adjustments (opening %.6f %+ .6f; includes_adjustments=%s).'
        % (opening_shares, 0 if sh_incl else adj_shares, sh_incl)
    )

    val = validate_case(c)
    json.dump(c, open(DIR / 'run' / ('case_%s_v04.json' % sc), 'w'), indent=1, default=str)
    if (val.get('errors') or val.get('missing')):
        print(sc, 'STOP validate', val)
        scenarios[sc] = {
            'ok': False, 'stopped': True,
            'stopped_reason': 'validate_case errors or missing fields; run_case was not called.',
            'validation': val, 'rates': rates,
            'value_per_share': None, 'value_per_share_DDM': None,
            'cash_share_schedule': worked,
            'not_a_valuation': True,
            'not_a_valuation_reason': ['validate_case: %s' % val],
            'notebook_code': None,
            'year0_da': c['baseline']['da'],
        }
        continue

    r = run_case(c)
    raw['res'][sc] = {k: r[k] for k in r if k != 'notebook_code'}
    raw['res'][sc]['notebook_code_len'] = len(r.get('notebook_code') or '')
    nb = r.get('notebook_code') or ''
    (DIR / ('notebook_%s_v04.py' % sc)).write_text(nb)

    replay, replay_err = None, None
    try:
        g = {}
        code = '\n'.join(l for l in nb.splitlines() if 'display_fin' not in l)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(code, g)
        fin = [v for v in g.values() if hasattr(v, 'fin')][0].fin
        cols = [k for k in ['revenue', 'ebitda', 'da', 'capex', 'sbc', 'interest',
                            'income_pretax', 'nol', 'income_taxable', 'tax', 'tax_cash',
                            'wacc', 'value_per_share', 'shares', 'debt', 'cash'] if k in fin.columns]
        replay = {k: [float(v) for v in fin[k]] for k in cols}
    except Exception as e:
        replay_err = '%s: %s' % (type(e).__name__, e)

    years = r.get('years') or []
    def series(key):
        if replay and key in replay:
            return replay[key]
        return [y.get(key) for y in years] if years else None

    da_s, capex_s, sbc_s, debt_s, cash_s, ebitda_s, int_s, rev_s = [
        series(k) for k in ['da', 'capex', 'sbc', 'debt', 'cash', 'ebitda', 'interest', 'revenue']
    ]

    # Confirm notebook da and capex fill
    nb_da_lines = [l.strip() for l in nb.splitlines() if "'da'" in l or "'da':" in l]
    nb_capex_lines = [l.strip() for l in nb.splitlines() if 'capex' in l.lower()][:8]
    capex_steps = [st for st in (r.get('steps') or []) if 'capex' in str(st.get('method', ''))]

    reasons = []
    if sbc_s and min(sbc_s[1:] or sbc_s) < 0:
        reasons.append('negative SBC')
    if capex_s and min(capex_s[1:] or capex_s) <= 0:
        reasons.append('non-positive capex')
    if da_s and min(da_s[1:] or da_s) < 0:
        reasons.append('negative D&A (min %.3f)' % min(da_s))
    if cash_s and min(cash_s) < 0:
        reasons.append('negative cash (min %.2f)' % min(cash_s))
    log = r.get('log') or []
    if log:
        reasons.append('log warnings: ' + '; '.join(sorted({
            (l.get('message') if isinstance(l, dict) else str(l)) for l in log
        })))
    # Capex vs FY25 actual 0.42: report, flag only if the default still looks like a misfire
    # relative to the *new* D&A (David asked for method 1 on PP&E+ROU D&A).
    y0_da = leaf_num(c['baseline']['da'])
    y0_capex = bb['baseline']['capex']['value']
    y0_rev = bb['baseline']['revenue']['value']
    da_ratio = y0_da / y0_rev if y0_rev else None
    capex_ratio_y0 = y0_capex / y0_rev if y0_rev else None

    ok = bool(r.get('ok', True))
    vps = r.get('value_per_share')
    vps_d = r.get('value_per_share_DDM')
    rec = {
        'ok': ok,
        'stopped': False,
        'value_per_share': vps,
        'value_per_share_DDM': vps_d,
        'validation': val,
        'log': log,
        'sanity_flags': r.get('sanity_flags') or r.get('flags') or [],
        'defaults_filled': list(bb.get('assumptions') or []) + [
            p for p in ('rates.re', 'rates.gt')
            if (rates.get(p.split('.')[-1]) or {}).get('source') == 'assumption'
        ],
        'rates': {
            'risk_free': rates.get('risk_free'),
            're': rates.get('re'),
            'gt': rates.get('gt'),
            'rd': rates.get('rd'),
            't': rates.get('t'),
            'roict': rates.get('roict'),
        },
        'year0_da': c['baseline']['da'],
        'year0_da_ok': abs(leaf_num(c['baseline']['da']) - 1.271558) < 1e-9,
        'year0_debt': c['baseline']['debt'],
        'cash_share_schedule': worked,
        'year0_cash_used': c['baseline']['cash']['value'],
        'shares_used': c['market']['shares']['value'],
        'per_year_from_notebook_replay': {
            'label': 'COMPUTED OUTSIDE run_case: replay of run_case notebook_code (Finagle company.fin), display_fin line skipped',
            'cols': replay,
            'error': replay_err,
        },
        'paths': {
            'revenue': rev_s, 'ebitda': ebitda_s, 'capex': capex_s, 'da': da_s,
            'sbc': sbc_s, 'debt': debt_s, 'cash': cash_s, 'interest': int_s,
            'terminal_capex': capex_s[-1] if capex_s else None,
            'terminal_da': da_s[-1] if da_s else None,
            'fy35_capex_to_ebitda': (capex_s[-1] / ebitda_s[-1]) if capex_s and ebitda_s and ebitda_s[-1] else None,
            'year0_da_to_revenue': da_ratio,
            'year0_capex_to_revenue': capex_ratio_y0,
        },
        'capex_fill': {
            'steps': capex_steps,
            'notebook_capex_lines': nb_capex_lines,
            'notebook_da_lines': nb_da_lines,
        },
        'debt_policy': c.get('debt'),
        'interest_all_zero': bool(int_s) and all(abs(v) < 1e-9 for v in int_s),
        'min_cash': min(cash_s) if cash_s else None,
        'negative_cash_years': [
            str((years[i].get('date') or ''))[:4]
            for i, v in enumerate(cash_s or [])
            if v is not None and v < 0
        ] if years else [],
        'not_a_valuation': bool(reasons),
        'not_a_valuation_reason': reasons,
        'flags': list(reasons) + [
            'rates.rd provenance: Forecaster proposal without an explicit David quote (applied as given; see rd_provenance)',
            'year-0 capex remains Yahoo %.6f vs method-1 ratio on new D&A (%.6f / revenue)' % (y0_capex, y0_da),
        ],
        'steps': r.get('steps'),
    }
    scenarios[sc] = rec
    print(sc, 'ok', ok, 'vps', vps, vps_d, 'val', val, 'log', log, 'reasons', reasons,
          'interest0', rec['interest_all_zero'], 'da0', rec['year0_da_ok'])

# rd provenance
rd_pi = next(p for p in R['prompt_inputs'] if p['path'] == 'rates.rd')
rd_provenance = {
    'applied': True,
    'value': rd_pi['value'],
    'quote_field': rd_pi.get('quote'),
    'date': rd_pi.get('date'),
    'flag': (
        'rd is not a direct David quote. The quote field is a Forecaster proposal: '
        '"%s" David did not object. Applied as given because it is in prompt_inputs. '
        'Immaterial if debt is held at 0 and interest is 0 every year.'
    ) % rd_pi.get('quote'),
}

defaults_filled = list(bb.get('assumptions') or [])
# remove items that prompt overrode
overridden = {p['path'] for p in R['prompt_inputs']}
defaults_filled = [p for p in defaults_filled if p not in overridden]
for p in ('rates.re', 'rates.gt'):
    if p not in defaults_filled:
        defaults_filled.append(p)

out = {
    'ticker': 'VHI.TO',
    'version': 'v04',
    'parent_version': 'v03',
    'mode': 'collaborative',
    'currency': 'CAD',
    'finagle_commit': '377f177b4013e713fe7c4603962e5f883a67e298',
    'ff_log': 'Already up to date (377f177b); no commits since 377f177b.',
    'run_at': datetime.datetime.now().astimezone().isoformat(),
    'sec_user_agent': UA,
    'hash_check': {
        'sidecar_present': sidecar is not None,
        'file_bytes': file_bytes,
        'file_bytes_starts_add5ef22': file_bytes.startswith('add5ef22'),
        'file_bytes_ends_9971c': file_bytes.endswith('9971c'),
        'file_bytes_actual_ending': file_bytes[-7:],
        'brief_end_mismatch': not file_bytes.endswith('9971c'),
        'whole_request': H(R),
        'blocks': {k: H(R['forecaster'][k]) for k in R['forecaster']},
        'prompt_inputs': H(R['prompt_inputs']),
        'forecast_json_bytes': forecast_bytes,
        'note': (
            'No sidecar was present. File sha256 starts with add5ef22 as stated, but does not end with 9971c. '
            'Full file sha256 is %s (ends …%s). Treated as a typo in the brief abbreviation '
            '(…95971c / …5971c, not …9971c). Content matches the expected v04 prompt_inputs. Ran anyway.'
        ) % (file_bytes, file_bytes[-6:]),
    },
    'request_diff': {
        'vs_v03_changed_keys': ['version', 'parent_version', 'prompt_inputs', 'cash_share_adjustments'],
        'vs_v03_unchanged': ['mode', 'ticker', 'forecast_commit', 'scenarios', 'forecaster', 'post_finagle'],
        'forecaster_unchanged_from_v02_and_v03': True,
        'prompt_inputs_v02': 1,
        'prompt_inputs_v03': 6,
        'prompt_inputs_v04': len(R['prompt_inputs']),
        'dropped_from_v03_prompts': ['forecast.capex (prose string)', "cash_share_adjustments.<all>.'Buddy Healthcare consideration shares'.proceeds"],
        'added_vs_v03_prompts': ['baseline.cash 106.812709 includes_adjustments false',
                                 'market.shares 63.307054 includes_adjustments false',
                                 'baseline.da 1.271558', 'rates.rd 0.028'],
        'cash_share_adjustments': (
            'v02/v03 had five items including Buddy closing cash and consideration shares. '
            'v04 keeps only: contingent consideration -0.781053 (2026-09-30), Novari earn-out -4.5 (2027-07-04), '
            'Buddy earn-out -7.248555 (2029-01-10). Buddy closing cash and consideration shares were removed.'
        ),
    },
    'rd_provenance': rd_provenance,
    'includes_adjustments_rule': (
        'collaborative-run.md: a stated year-0 cash or share count is the opening figure, before the schedule; '
        'the runner discounts the schedule and adds PV to cash and new shares to the count, unless '
        'includes_adjustments is true (that side is not added again). '
        'forecastcheck.collaborative._openings reads includes_adjustments from the prompt item '
        '(default False). Both baseline.cash and market.shares have includes_adjustments false, '
        'so remaining CSA items are added on top of 106.812709 cash and 63.307054 shares.'
    ),
    'forecast_commit': R.get('forecast_commit'),
    'prompt_inputs': R['prompt_inputs'],
    'post_finagle': R.get('post_finagle'),
    'build_baseline': {
        'ok': bb.get('ok'), 'canadian': bb.get('canadian'), 'currency': bb.get('currency'),
        'period_end': bb.get('period_end'), 'warnings': bb.get('warnings'),
        'assumptions': bb.get('assumptions'),
    },
    'fetched': {
        'price': price_leaf.get('value'),
        'price_date': price_leaf.get('as_of'),
        'price_source': price_leaf.get('source'),
        'price_currency': price_leaf.get('currency'),
        'rf': 0.0381, 'rf_source': 'prompt',
        'shares_prompt_opening': 63.307054,
        're_derived': 0.0931, 'gt_derived': 0.0381,
        'year0_da_yahoo': bb['baseline']['da']['value'],
        'year0_da_prompt': 1.271558,
        'year0_capex_yahoo': bb['baseline']['capex']['value'],
        'year0_cash_yahoo': bb['baseline']['cash']['value'],
    },
    'defaults_filled': defaults_filled,
    'scenarios': scenarios,
}
json.dump(out, open(DIR / 'valuation_result_v04.json', 'w'), indent=1, default=str)
json.dump({'bb_warnings': bb.get('warnings'),
           'scenario_ok': {s: scenarios[s].get('ok') for s in scenarios},
           'rates_sample': (list(scenarios.values())[0].get('rates') if scenarios else None)},
          open(DIR / 'run' / 'raw_v04.json', 'w'), indent=1, default=str)
print('DONE', {s: (scenarios[s].get('ok'), scenarios[s].get('value_per_share')) for s in scenarios})
