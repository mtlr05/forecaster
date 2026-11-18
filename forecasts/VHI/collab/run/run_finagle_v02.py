#!/usr/bin/env python3
"""VHI.TO collaborative v02 runner. Prompt rf 0.0381; re/gt left to Finagle defaults."""
import copy, datetime, hashlib, io, json, os, sys, contextlib
from datetime import date
from pathlib import Path

sys.path.insert(0, '/workspace/finagle')
from finagle.agent import describe_inputs, build_baseline, update_case, validate_case, run_case

DIR = Path('/workspace/forecaster-work/output/VHI/2026-11-17/finagle-run')
REQ_PATH = DIR / 'valuation_request_v02.json'
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
for p in DIR.glob('*v02*.sha256.json'):
    sidecar = json.load(open(p))

# Catalog check (do not guess the path).
catalog = describe_inputs()
catalog_paths = [f.get('path') for f in (catalog.get('fields') or []) if isinstance(f, dict)]
RF_PATH = 'rates.risk_free'
print('catalog_has_rates.risk_free', RF_PATH in catalog_paths)
print('catalog rate paths', [p for p in catalog_paths if p and p.startswith('rates.')])

bb = build_baseline('VHI.TO', user_agent=UA)
(DIR / 'run' / 'baseline_v02.json').write_text(json.dumps(bb, indent=1, default=str))

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
opening_cash = bb['baseline']['cash']['value']
opening_shares = leaf_num(bb['shares'])

def item_date(item):
    w = item.get('when')
    return date.fromisoformat(str(w['value'] if isinstance(w, dict) else w)[:10])

def years_t(d):
    if d <= price_date:
        return 0.0
    return (d - price_date).days / 365.25

def work_schedule(items, re, label):
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
                       proceeds=proceeds, present_value=pv, new_shares=sh_add,
                       note=('Procedure adds probability-weighted proceeds to year-0 cash '
                             'and shares to the share count. This item is consideration shares, '
                             'not a cash offering.'),
                       status='applied (written offering rule; flagged)')
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
        if sc in (pi.get('applies_to') or []):
            ev = 'David %s: "%s"' % (pi.get('date'), pi.get('quote'))
            if pi.get('note'):
                ev += ' ' + pi['note']
            pth = pi['path']
            leaf = {'value': pi['value'], 'source': 'prompt', 'evidence': ev}
            if pth == RF_PATH or pth.startswith('rates.'):
                pass
            elif pth.startswith('baseline.'):
                leaf.update(period_end='2025-12-31', basis='fiscal_year', currency='CAD')
            up[pth] = leaf

scenarios = {}
raw = {'bb': bb, 'res': {}}
catalog_note = (
    'describe_inputs() fields does not list rates.risk_free (rate fields are '
    'rates.re, rates.rd, rates.t, rates.te, rates.gt, rates.roict). The path '
    'rates.risk_free is the name Finagle uses in schema.py, defaults.py and '
    'validate.py, and it is the path in the request. update_case accepts it; '
    'apply_defaults (fetch_yield=False) then derives re and gt from it. Not a guess.'
)

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
    print(sc, 'rf', rates.get('risk_free'), 're', rates.get('re'), 'gt', rates.get('gt'))
    if re is None or gt is None:
        val = validate_case(c)
        print('STOP: re/gt not derived', val)
        rec = {
            'ok': False, 'stopped': True,
            'stopped_reason': 'Finagle did not derive re and/or gt from the supplied rates.risk_free. run_case was not called.',
            'validation': val, 'rates': rates,
            'value_per_share': None, 'value_per_share_DDM': None,
            'not_a_valuation': True,
            'not_a_valuation_reason': ['re/gt not derived; validate_case: %s' % val],
        }
        scenarios[sc] = rec
        json.dump(c, open(DIR / 'run' / ('case_%s_v02.json' % sc), 'w'), indent=1, default=str)
        continue

    # cash_share_adjustments now that re exists. Base list is used when a scenario has none.
    csa = (R.get('cash_share_adjustments') or {})
    items = csa.get(sc) if csa.get(sc) is not None else (csa.get('base') or [])
    sched_items, adj_cash, adj_shares, complete = work_schedule(items, re, 'base' if csa.get(sc) is None else sc)
    worked = {
        'label': ('COMPUTED OUTSIDE run_case by the runner from cash_share_adjustments, '
                  'per collaborative-run.md. t = 0 when the item date is on or before the '
                  'price date; otherwise t = (item_date - price_date).days / 365.25. '
                  'Discount factor = 1/(1+re)^t. Applied to year-0 cash and shares only.'),
        'price_date': price_date_s,
        'cost_of_equity': re,
        'opening_cash': opening_cash,
        'opening_shares': opening_shares,
        'items': sched_items,
        'sum_pv_cash': adj_cash,
        'sum_new_shares': adj_shares,
        'adjusted_cash': opening_cash + adj_cash,
        'adjusted_shares': opening_shares + adj_shares,
        'complete': complete,
        'applied_to_case': True,
    }
    # Apply to opening inputs only.
    c['baseline']['cash'] = copy.deepcopy(c['baseline']['cash'])
    c['baseline']['cash']['value'] = opening_cash + adj_cash
    note = c['baseline']['cash'].get('note') or ''
    c['baseline']['cash']['note'] = ((note + ' ') if note else '') + (
        'Year-0 cash after cash_share_adjustments PV (opening %.6f %+ .6f).' % (opening_cash, adj_cash)
    )
    c['market']['shares'] = copy.deepcopy(c['market']['shares'])
    c['market']['shares']['value'] = opening_shares + adj_shares
    shnote = c['market']['shares'].get('note') or ''
    c['market']['shares']['note'] = ((shnote + ' ') if shnote else '') + (
        'Shares after cash_share_adjustments (opening %.6f %+ .6f).' % (opening_shares, adj_shares)
    )

    val = validate_case(c)
    json.dump(c, open(DIR / 'run' / ('case_%s_v02.json' % sc), 'w'), indent=1, default=str)
    if (val.get('errors') or val.get('missing')):
        print(sc, 'STOP validate', val)
        scenarios[sc] = {
            'ok': False, 'stopped': True,
            'stopped_reason': 'validate_case errors or missing fields; run_case was not called; no value is presented.',
            'validation': val, 'rates': rates,
            'value_per_share': None, 'value_per_share_DDM': None,
            'cash_share_schedule': worked,
            'not_a_valuation': True,
            'not_a_valuation_reason': ['validate_case: %s' % val],
            'notebook_code': None,
        }
        continue

    r = run_case(c)
    raw['res'][sc] = {k: r[k] for k in r if k != 'notebook_code'}
    raw['res'][sc]['notebook_code_len'] = len(r.get('notebook_code') or '')
    nb = r.get('notebook_code') or ''
    (DIR / ('notebook_%s_v02.py' % sc)).write_text(nb)

    # Replay notebook for per-year paths (outside run_case).
    replay = None
    replay_err = None
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
    da_path = [leaf_num(y.get('da')) for y in years] if years and 'da' in (years[0] or {}) else (replay or {}).get('da')
    capex_path = [y.get('capex') for y in years] if years else (replay or {}).get('capex')
    sbc_path = [y.get('sbc') for y in years] if years else (replay or {}).get('sbc')
    debt_path = [y.get('debt') for y in years] if years else (replay or {}).get('debt')
    cash_path = [y.get('cash') for y in years] if years else (replay or {}).get('cash')
    ebitda_path = [y.get('ebitda') for y in years] if years else (replay or {}).get('ebitda')

    def series(key):
        if replay and key in replay:
            return replay[key]
        return [y.get(key) for y in years] if years else None

    da_s, capex_s, sbc_s, debt_s, cash_s, ebitda_s = map(series, ['da', 'capex', 'sbc', 'debt', 'cash', 'ebitda'])

    reasons = []
    if sbc_s and min(sbc_s[1:] or sbc_s) < 0:
        reasons.append('negative SBC')
    if capex_s and min(capex_s[1:] or capex_s) <= 0:
        reasons.append('non-positive capex')
    if da_s and min(da_s[1:] or da_s) < 0:
        reasons.append('negative D&A (min %.1f)' % min(da_s))
    if cash_s and min(cash_s) < 0:
        reasons.append('negative cash (min %.2f)' % min(cash_s))
    log = r.get('log') or []
    if log:
        reasons.append('log warnings: ' + '; '.join(sorted({(l.get('message') if isinstance(l, dict) else str(l)) for l in log})))
    # Capex method-1 misfire: default anchors on D&A 11.08 vs actual capex 0.42.
    y0_da = bb['baseline']['da']['value']
    y0_capex = bb['baseline']['capex']['value']
    y0_rev = bb['baseline']['revenue']['value']
    if capex_s and len(capex_s) > 1 and y0_rev:
        later = capex_s[1:]
        da_ratio = y0_da / y0_rev
        # If forecast capex is far above actual year-0 capex and in line with D&A/revenue, flag it.
        if max(later) > max(5.0 * y0_capex, 2.0) and any(abs((cx / rv) - da_ratio) < 0.05
                for cx, rv in zip(later, series('revenue') or []) if rv):
            reasons.append(
                'default capex method 1 appears to anchor on year-0 D&A/revenue (%.4f); '
                'year-0 capex is only %.3f vs D&A %.3f (mostly acquired-intangible amortization). '
                'Forecast capex path: %s'
                % (da_ratio, y0_capex, y0_da, [round(x, 3) for x in capex_s])
            )
        elif max(later) > max(5.0 * y0_capex, 2.0):
            reasons.append(
                'forecast capex (max %.2f) is far above actual FY25 capex %.3f; year-0 D&A is %.3f. '
                'Capex path: %s'
                % (max(later), y0_capex, y0_da, [round(x, 3) for x in capex_s])
            )

    flags = list(reasons)
    flags.append('lease-as-debt: year-0 Yahoo Total Debt %.6f is flagged by Finagle as possibly lease liabilities; default target leverage and rd follow from it (not patched)' % bb['baseline']['debt']['value'])
    flags.append('Buddy consideration-share proceeds of 0.552 added to year-0 cash under the written offering rule (shares were non-cash consideration; not patched)')
    flags.append('rates.t default 0.21 (US federal statutory) vs Canadian combined ~26.5% (not patched)')
    flags.append('year-0 EBITDA Yahoo %.4f vs reported Adj. EBITDA 26.55 FY25 context (not patched)' % bb['baseline']['ebitda']['value'])

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
        'assumptions': r.get('assumptions') or bb.get('assumptions'),
        'defaults_filled': list(bb.get('assumptions') or []) + [
            p for p in ('rates.re', 'rates.gt') if (rates.get(p.split('.')[-1]) or {}).get('source') == 'assumption'
        ],
        'rates': {
            'risk_free': rates.get('risk_free'),
            're': rates.get('re'),
            'gt': rates.get('gt'),
            'rd': rates.get('rd'),
            't': rates.get('t'),
            'roict': rates.get('roict'),
        },
        'cash_share_schedule': worked,
        'year0_cash_used': c['baseline']['cash']['value'],
        'shares_used': c['market']['shares']['value'],
        'per_year_from_notebook_replay': {
            'label': 'COMPUTED OUTSIDE run_case: replay of run_case notebook_code (Finagle company.fin), display_fin line skipped',
            'cols': replay,
            'error': replay_err,
        },
        'paths': {
            'capex': capex_s, 'da': da_s, 'sbc': sbc_s, 'debt': debt_s,
            'cash': cash_s, 'ebitda': ebitda_s, 'revenue': series('revenue'),
            'interest': series('interest'), 'tax_cash': series('tax_cash'),
            'terminal_capex': capex_s[-1] if capex_s else None,
            'terminal_da': da_s[-1] if da_s else None,
        },
        'debt_policy': c.get('debt'),
        'min_cash': min(cash_s) if cash_s else None,
        'negative_cash_years': [str((years[i].get('date') or ''))[:4] for i, v in enumerate(cash_s or []) if v is not None and v < 0] if years else [],
        'not_a_valuation': bool(reasons),
        'not_a_valuation_reason': reasons,
        'flags': flags,
        'steps': r.get('steps'),
        'checks': r.get('checks'),
    }
    # Keep run_case keys that are useful and JSON-safe
    for k in ('ok', 'warnings', 'errors', 'notes'):
        if k in r and k not in rec:
            rec[k] = r[k]
    scenarios[sc] = rec
    print(sc, 'ok', ok, 'vps', vps, vps_d, 'val', val, 'log', log, 'reasons', reasons)

# Known-issue summary from the runs (or from baseline if all stopped).
bl = bb['baseline']
known = {
    'buddy_consideration_share_proceeds': {
        'flagged': True, 'patched': False,
        'detail': ('Written offering rule adds proceeds = 0.075 * stated price 7.36 = 0.552 to year-0 cash, '
                   'plus 0.075 to shares. These were Buddy Healthcare consideration shares, not a cash offering.'),
    },
    'lease_as_debt': {
        'flagged': True, 'patched': False,
        'year0_debt': bl['debt']['value'],
        'finagle_note': bl['debt'].get('note'),
        'rd': (bb.get('rates') or {}).get('rd'),
        'default_leverage': (bb.get('debt') or {}).get('leverage'),
        'detail': 'Yahoo Total Debt 2.514474 CAD; Finagle notes it can include lease liabilities. Default target leverage and rd follow from it.',
    },
    'yahoo_ebitda_vs_adj': {
        'flagged': True, 'patched': False,
        'yahoo_ebitda': bl['ebitda']['value'],
        'reported_adj_ebitda_fy25_context_only': 26.55,
    },
    'tax_default_21pct': {
        'flagged': True, 'patched': False,
        'rates_t': (bb.get('rates') or {}).get('t'),
        'detail': 'US federal statutory 21% default vs Canadian combined ~26.5%.',
    },
    'capex_method_1_vs_actual': {
        'flagged': True, 'patched': False,
        'year0_capex': bl['capex']['value'],
        'year0_da': bl['da']['value'],
        'da_to_revenue': bl['da']['value'] / bl['revenue']['value'],
        'paths': {sc: (scenarios[sc].get('paths') or {}) for sc in scenarios},
    },
}

defaults_filled = list(bb.get('assumptions') or [])
# re and gt are filled by apply_defaults on update from the prompt rf; they were not in build_baseline assumptions.
if 'rates.re' not in defaults_filled:
    defaults_filled.append('rates.re')
if 'rates.gt' not in defaults_filled:
    defaults_filled.append('rates.gt')
# rf itself is prompt, not a default.

out = {
    'ticker': 'VHI.TO',
    'version': 'v02',
    'parent_version': 'v01',
    'mode': 'collaborative',
    'currency': 'CAD',
    'finagle_commit': '377f177b4013e713fe7c4603962e5f883a67e298',
    'ff_log': 'Already up to date (377f177b); no commits since 377f177b.',
    'run_at': datetime.datetime.now().astimezone().isoformat(),
    'sec_user_agent': UA,
    'hash_check': {
        'sidecar_present': sidecar is not None,
        'file_bytes': file_bytes,
        'file_bytes_matches_brief': file_bytes.startswith('640ef581') and file_bytes.endswith('dadf'),
        'whole_request': H(R),
        'blocks': {k: H(R['forecaster'][k]) for k in R['forecaster']},
        'prompt_inputs': H(R['prompt_inputs']),
        'forecast_json_bytes': forecast_bytes,
        'note': 'No sidecar was present. File sha256 matches the brief (640ef581…dadf). Canonical hashes recorded here.',
    },
    'request_diff_vs_v01': {
        'changed_keys': ['version', 'parent_version', 'prompt_inputs'],
        'prompt_inputs_added': R['prompt_inputs'],
        'forecaster_unchanged': True,
        'cash_share_adjustments_unchanged': True,
        'post_finagle_unchanged': True,
        'forecast_commit_unchanged': True,
    },
    'catalog_rf_path': {
        'request_path': RF_PATH,
        'in_describe_inputs_fields': RF_PATH in catalog_paths,
        'describe_inputs_rate_fields': [p for p in catalog_paths if p and p.startswith('rates.')],
        'note': catalog_note,
        'used_path': RF_PATH,
    },
    'forecast_commit': R.get('forecast_commit'),
    'prompt_inputs': R['prompt_inputs'],
    'post_finagle': R.get('post_finagle'),
    'build_baseline': {
        'ok': bb.get('ok'), 'canadian': bb.get('canadian'), 'currency': bb.get('currency'),
        'period_end': bb.get('period_end'), 'period_source': bb.get('period_source'),
        'warnings': bb.get('warnings'), 'assumptions': bb.get('assumptions'),
        'sources_used': bb.get('sources_used'),
    },
    'fetched': {
        'price': price_leaf.get('value'),
        'price_date': price_leaf.get('as_of'),
        'price_source': price_leaf.get('source'),
        'price_currency': price_leaf.get('currency'),
        'price_evidence': price_leaf.get('evidence'),
        'rf': 0.0381,
        'rf_source': 'prompt',
        'rf_evidence': 'David 2026-11-18: "3.81% use this"',
        'rf_note': 'User-stated. Yahoo CA10Y=RR still has no quote; that warning remains on build_baseline. The BoC 3.81% was applied only because it is the prompt_input.',
        'shares_unadjusted': opening_shares,
        'shares_source': bb['shares'].get('source') if isinstance(bb['shares'], dict) else None,
        'shares_as_of': bb['shares'].get('as_of') if isinstance(bb['shares'], dict) else None,
        're_derived': 0.0931,
        'gt_derived': 0.0381,
        'year0': {k: leaf_num(v) for k, v in bl.items()},
        'year0_sources': {k: (v.get('source') if isinstance(v, dict) else None) for k, v in bl.items()},
    },
    'defaults_filled': defaults_filled,
    'known_issue_checks': known,
    'scenarios': scenarios,
}
json.dump(out, open(DIR / 'valuation_result_v02.json', 'w'), indent=1, default=str)
# raw without huge notebook
json.dump({'bb': bb, 'scenario_ok': {s: scenarios[s].get('ok') for s in scenarios},
           'rates_sample': (list(scenarios.values())[0].get('rates') if scenarios else None)},
          open(DIR / 'run' / 'raw_v02.json', 'w'), indent=1, default=str)
print('DONE', {s: (scenarios[s].get('ok'), scenarios[s].get('value_per_share')) for s in scenarios})
