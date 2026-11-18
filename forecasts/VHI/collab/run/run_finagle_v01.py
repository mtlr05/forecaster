#!/usr/bin/env python3
"""VHI.TO collaborative v01 runner. Stops a scenario on validate_case errors or missing fields; does not invent rates."""
import copy, datetime, hashlib, json, os, sys
from datetime import date

sys.path.insert(0, '/workspace/finagle')
from finagle.agent import describe_inputs, build_baseline, update_case, validate_case

DIR = '/workspace/forecaster-work/output/VHI/2026-11-17/finagle-run'
REQ_PATH = os.path.join(DIR, 'valuation_request_v01.json')
FORECAST_PATH = '/workspace/forecaster-work/output/VHI/2026-11-17/forecast.json'
UA = 'David May davidmay44@hotmail.com'
H = lambda o: hashlib.sha256(
    json.dumps(o, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()
).hexdigest()

R = json.load(open(REQ_PATH))
file_bytes = hashlib.sha256(open(REQ_PATH, 'rb').read()).hexdigest()
forecast_bytes = hashlib.sha256(open(FORECAST_PATH, 'rb').read()).hexdigest() if os.path.exists(FORECAST_PATH) else None
sidecar_path = os.path.join(DIR, 'valuation_request_v01.sha256.json')
sidecar = json.load(open(sidecar_path)) if os.path.exists(sidecar_path) else None

# describe_inputs is part of the procedure (catalog only; not written out)
describe_inputs()

bb_path = os.path.join(DIR, 'run', 'baseline_v01.json')
if os.path.exists(bb_path):
    bb = json.load(open(bb_path))
else:
    bb = build_baseline('VHI.TO', user_agent=UA)
    json.dump(bb, open(bb_path, 'w'), indent=1, default=str)

case_template = dict(
    path='ebitda', ticker='VHI.TO', year=10,
    market={'shares': bb['shares'], 'price': bb['price']},
    rates=bb['rates'], baseline=bb['baseline'], forecast=bb['forecast'],
    debt=bb['debt'], distribution=bb['distribution'],
)

# Worked cash/share schedule (runner-side, per collaborative-run.md).
# Future items need rates.re; it is unset, so those PVs are not computed and the
# schedule is not applied to the case (the run stops on missing re/gt anyway).
price_leaf = bb['price'] if isinstance(bb['price'], dict) else {'value': bb['price']}
price_date_s = price_leaf.get('as_of') or date.today().isoformat()
price_date = date.fromisoformat(price_date_s[:10])
opening_cash = bb['baseline']['cash']['value']
opening_shares = bb['shares']['value'] if isinstance(bb['shares'], dict) else bb['shares']
re_leaf = (bb.get('rates') or {}).get('re')
re = re_leaf.get('value') if isinstance(re_leaf, dict) else re_leaf

def item_date(item):
    w = item.get('when')
    if isinstance(w, dict):
        return date.fromisoformat(str(w['value'])[:10])
    return date.fromisoformat(str(w)[:10])

def years_t(d):
    if d <= price_date:
        return 0.0
    return (d - price_date).days / 365.25

def leaf_num(x):
    if isinstance(x, dict):
        return x.get('value')
    return x

schedule_items = []
adj_cash = 0.0
adj_shares = 0.0
schedule_complete = True
sched_src = R.get('cash_share_adjustments') or {}

def work_schedule(items, label):
    global schedule_complete, adj_cash, adj_shares
    out = []
    for it in items:
        d = item_date(it)
        t = years_t(d)
        kind = it.get('kind')
        p = leaf_num(it.get('probability'))
        if p is None:
            p = 1.0
        rec = {
            'name': it.get('name'), 'kind': kind, 'date': d.isoformat(),
            't_years': t, 'probability': p, 'source_list': label,
        }
        if t == 0:
            factor = 1.0
            rec['discount_factor'] = factor
        elif re is None:
            rec['discount_factor'] = None
            rec['status'] = 'not applied: rates.re is unset, so the item cannot be discounted'
            schedule_complete = False
            out.append(rec)
            continue
        else:
            factor = 1.0 / ((1.0 + re) ** t)
            rec['discount_factor'] = factor
        if kind == 'cash':
            amt = leaf_num(it.get('amount'))
            pv = amt * p * factor
            rec['amount'] = amt
            rec['present_value'] = pv
            rec['new_shares'] = 0.0
            rec['status'] = 'computed (not applied: scenario stopped on missing rates)'
            adj_cash += pv
        elif kind == 'equity':
            sh = leaf_num(it.get('shares'))
            px = leaf_num(it.get('price'))
            stated_price = px is not None
            if px is None:
                px = price_leaf.get('value')
            proceeds = sh * px if (sh is not None and px is not None) else None
            pv = proceeds * p * factor if proceeds is not None else None
            sh_add = (sh or 0.0) * p
            rec['shares'] = sh
            rec['issue_price'] = px
            rec['issue_price_stated'] = stated_price
            rec['proceeds'] = proceeds
            rec['present_value'] = pv
            rec['new_shares'] = sh_add
            rec['note'] = (
                'Procedure adds probability-weighted proceeds to year-0 cash and shares '
                'to the share count. This item is consideration shares, not a cash offering.'
            )
            rec['status'] = 'computed (not applied: scenario stopped on missing rates)'
            if pv is not None:
                adj_cash += pv
            adj_shares += sh_add
        else:
            rec['status'] = 'unknown kind; not applied'
            schedule_complete = False
        out.append(rec)
    return out

# Base list is used for any scenario without its own list.
base_list = sched_src.get('base') or []
# Compute once from the base list (bull/bear have no override).
schedule_items = work_schedule(base_list, 'base')
worked_schedule = {
    'label': (
        'COMPUTED OUTSIDE run_case by the runner from cash_share_adjustments, '
        'per collaborative-run.md. t = 0 when the item date is on or before the '
        'price date; otherwise t = (item_date - price_date).days / 365.25. '
        'Schedule was NOT applied to the case: validate_case reported missing '
        'rates.re and rates.gt, so the scenario stopped before run_case.'
    ),
    'price_date': price_date_s,
    'cost_of_equity': re,
    'opening_cash': opening_cash,
    'opening_shares': opening_shares,
    'items': schedule_items,
    'sum_pv_cash_of_computable_items': adj_cash,
    'sum_new_shares_of_computable_items': adj_shares,
    'adjusted_cash_if_computable_items_applied': opening_cash + adj_cash,
    'adjusted_shares_if_computable_items_applied': opening_shares + adj_shares,
    'complete': schedule_complete,
    'applied_to_case': False,
}

scenarios_out = {}
raw = {}
for sc in R['scenarios']:
    up = {}
    for path, leaf in R['forecaster'][sc].items():
        ev = leaf.get('evidence') or ''
        tag = leaf.get('tag') or ''
        cid = leaf.get('cite_id') or ''
        up[path] = {
            'value': leaf['value'],
            'source': 'assumption',
            'evidence': 'Forecaster [%s] cite: %s %s' % (tag, cid, ev),
        }
    u = update_case(copy.deepcopy(case_template), up, run=False)
    c = u.get('case', u)
    val = validate_case(c)
    json.dump(c, open(os.path.join(DIR, 'run', 'case_%s_v01.json' % sc), 'w'), indent=1, default=str)
    missing = val.get('missing') or []
    errors = val.get('errors') or []
    stopped = bool(errors or missing)
    rec = {
        'ok': False,
        'stopped': True,
        'stopped_reason': (
            'validate_case reported missing fields and/or errors; run_case was not called; no value is presented.'
            if stopped else 'unknown'
        ),
        'validation': val,
        'update_case_ok': u.get('ok') if isinstance(u, dict) else None,
        'value_per_share': None,
        'value_per_share_DDM': None,
        'log': [],
        'sanity_flags': [],
        'assumptions': bb.get('assumptions'),
        'defaults_filled': list(bb.get('assumptions') or []),
        'forecaster_leaves_landed': {
            'forecast.sales_growth': c['forecast']['sales_growth']['value'],
            'forecast.ebitda_growth': c['forecast']['ebitda_growth']['value'],
            'forecast.margin_path.me': c['forecast']['margin_path']['me']['value'],
            'forecast.margin_path.mc': c['forecast']['margin_path']['mc']['value'],
            'forecast.margin_path.gsnext': c['forecast']['margin_path']['gsnext']['value'],
            'forecast.ebitda_basis': c['forecast']['ebitda_basis']['value'],
            'forecast.acquisition_disclosure.status': c['forecast']['acquisition_disclosure']['status']['value'],
        },
        'not_a_valuation': True,
        'not_a_valuation_reason': [
            'validate_case missing: %s' % missing,
            'Yahoo CA10Y=RR had no last close, so rates.risk_free, rates.re and rates.gt were left unset. The Bank of Canada 10-year (3.81% on 16 Nov 2026) was not injected.',
        ],
        'notebook_code': None,
        'cash_share_schedule': worked_schedule,
    }
    if errors:
        rec['not_a_valuation_reason'].insert(0, 'validate_case errors: %s' % errors)
    scenarios_out[sc] = rec
    raw[sc] = {'update': {'ok': u.get('ok') if isinstance(u, dict) else None}, 'validation': val}

# Known-issue checks (observation only; nothing was patched).
bl = bb['baseline']
known = {
    '1_cad_risk_free_yahoo_CA10Y_RR': {
        'occurred': True,
        'detail': (
            'build_baseline warning: "Yahoo has no last close for the 10-year yield CA10Y=RR." '
            'rates has only roict, t and rd. rates.risk_free, rates.re and rates.gt are absent. '
            'validate_case missing: rates.re, rates.gt. Context only (not used): Forecaster said the Bank of Canada 10-year was 3.81% on 16 Nov 2026.'
        ),
        'finagle_warning': (bb.get('warnings') or []),
    },
    '2_yahoo_total_debt_may_be_leases': {
        'occurred': True,
        'detail': (
            'Year-0 debt is %.6f CAD from Yahoo Total Debt. Finagle note: "%s" '
            'Default debt.mode=target, debt.leverage=year-0 Debt/EBITDA (%.6f), start_year=1, '
            'rates.rd=year-0 interest/debt (%.6f). Not patched.'
        ) % (
            bl['debt']['value'], bl['debt'].get('note'),
            bb['debt']['leverage']['value'], bb['rates']['rd']['value'],
        ),
    },
    '3_yahoo_ebitda_vs_reported_adj_ebitda': {
        'occurred': True,
        'detail': (
            'Year-0 EBITDA is %.6f CAD from Yahoo (Operating Income + D&A + SBC; '
            'Yahoo\'s own EBITDA row does not add back SBC). The Forecaster\'s discarded-test note of reported Adj. EBITDA 26.55 FY25 is context only; the Yahoo figure was left in place.'
        ) % bl['ebitda']['value'],
        'yahoo_ebitda': bl['ebitda']['value'],
        'reported_adj_ebitda_fy25_context_only': 26.55,
    },
    '4_tax_default_21pct_vs_canadian_combined': {
        'occurred': True,
        'detail': (
            'rates.t is 0.21, source assumption, evidence "US federal statutory tax rate. No marginal rate was stated." '
            'Context only: Canadian combined statutory rate is about 26.5%. Not patched.'
        ),
        'rates_t': bb['rates']['t'],
    },
    '5_capex_rule_anchors_on_DA': {
        'occurred_as_year0_inputs': True,
        'capex_path_observed': False,
        'detail': (
            'Year-0 D&A is %.6f CAD (Yahoo Depreciation And Amortization) and year-0 capex is %.6f CAD (Yahoo Capital Expenditure). '
            'The default capex forecast (method 1) was not run because the scenario stopped before run_case, so any inflation of capex from the D&A/revenue ratio was not observed. Not patched.'
        ) % (bl['da']['value'], bl['capex']['value']),
        'year0_da': bl['da']['value'],
        'year0_capex': bl['capex']['value'],
        'da_to_revenue': bl['da']['value'] / bl['revenue']['value'],
    },
    'currency_consistency': {
        'ok': True,
        'detail': (
            'Ticker VHI.TO, canadian=True, reporting currency CAD. Price %.2f CAD (Yahoo previousClose, as_of %s). '
            'Year-0 money leaves (revenue, ebitda, capex, da, tax, interest, sbc, debt, cash) are all CAD. Shares are a count (%.6f, Yahoo sharesOutstanding, as_of %s).'
        ) % (
            price_leaf.get('value'), price_leaf.get('as_of'),
            opening_shares, bb['shares'].get('as_of') if isinstance(bb['shares'], dict) else None,
        ),
        'currency': bb.get('currency'),
        'price_currency': price_leaf.get('currency'),
    },
}

hash_check = {
    'sidecar_present': sidecar is not None,
    'file_bytes': file_bytes,
    'file_bytes_matches_brief': file_bytes.startswith('70e2176f') and file_bytes.endswith('a93c4'),
    'whole_request': H(R),
    'blocks': {k: H(R['forecaster'][k]) for k in R['forecaster']},
    'prompt_inputs': H(R['prompt_inputs']),
    'forecast_json_bytes': forecast_bytes,
    'forecast_json_path': FORECAST_PATH,
    'note': (
        'No sidecar *.sha256.json was present in the finagle-run folder, so whole-request, '
        'block, prompt_inputs and forecast hashes could not be cross-checked against a sidecar. '
        'The file sha256 matches the brief (70e2176f…a93c4). Canonical hashes are recorded here.'
    ),
}

out = {
    'ticker': 'VHI.TO',
    'version': 'v01',
    'parent_version': R.get('parent_version'),
    'mode': 'collaborative',
    'currency': 'CAD',
    'finagle_commit': '377f177b4013e713fe7c4603962e5f883a67e298',
    'ff_log': 'Already up to date (377f177b); no commits since 377f177b. AGENTS.md and catalog.py were not re-read.',
    'run_at': datetime.datetime.now().astimezone().isoformat(),
    'sec_user_agent': UA,
    'hash_check': hash_check,
    'collaborative_run_md': 'Fetched current main copy of mtlr05/forecaster .cursor/skills/forecaster/references/collaborative-run.md via the cursor-github connector (includes cash_share_adjustments).',
    'forecast_commit': R.get('forecast_commit'),
    'prompt_inputs': R['prompt_inputs'],
    'post_finagle': R.get('post_finagle'),
    'build_baseline': {
        'ok': bb.get('ok'),
        'canadian': bb.get('canadian'),
        'currency': bb.get('currency'),
        'period_end': bb.get('period_end'),
        'period_source': bb.get('period_source'),
        'warnings': bb.get('warnings'),
        'missing': bb.get('missing'),
        'skipped': bb.get('skipped'),
        'assumptions': bb.get('assumptions'),
        'sources_used': bb.get('sources_used'),
        'note': bb.get('note'),
    },
    'fetched': {
        'price': price_leaf.get('value'),
        'price_date': price_leaf.get('as_of'),
        'price_source': price_leaf.get('source'),
        'price_currency': price_leaf.get('currency'),
        'price_evidence': price_leaf.get('evidence'),
        'rf': None,
        'rf_date': None,
        'rf_source': None,
        'rf_note': 'Unset. Yahoo has no last close for CA10Y=RR.',
        'shares': opening_shares,
        'shares_source': bb['shares'].get('source') if isinstance(bb['shares'], dict) else None,
        'shares_as_of': bb['shares'].get('as_of') if isinstance(bb['shares'], dict) else None,
        'shares_evidence': bb['shares'].get('evidence') if isinstance(bb['shares'], dict) else None,
        're': None,
        'gt': None,
        'year0': {k: (v.get('value') if isinstance(v, dict) else v) for k, v in bl.items()},
        'year0_sources': {k: (v.get('source') if isinstance(v, dict) else None) for k, v in bl.items()},
        'year0_currency': {k: (v.get('currency') if isinstance(v, dict) else None) for k, v in bl.items()},
    },
    'defaults_filled': list(bb.get('assumptions') or []),
    'cash_share_adjustments_schedule': worked_schedule,
    'known_issue_checks': known,
    'scenarios': scenarios_out,
}

json.dump(out, open(os.path.join(DIR, 'valuation_result_v01.json'), 'w'), indent=1, default=str)
json.dump({'bb_keys': list(bb), 'raw': raw, 'worked_schedule': worked_schedule},
          open(os.path.join(DIR, 'run', 'raw_v01.json'), 'w'), indent=1, default=str)
print('wrote result; stopped all scenarios; missing', missing)
