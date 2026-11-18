#!/usr/bin/env python3
"""VHI.TO v03: stop if capex is not a numeric list or shares-without-proceeds cannot be expressed."""
import json
from pathlib import Path
R = json.load(open(Path(__file__).resolve().parents[1] / 'valuation_request_v03.json'))
capex = next(p for p in R['prompt_inputs'] if p['path'] == 'forecast.capex')
proceeds = next(p for p in R['prompt_inputs'] if 'proceeds' in p['path'])
print('STOPPED')
print('forecast.capex value type:', type(capex['value']).__name__)
print('forecast.capex value:', capex['value'])
print('proceeds path:', proceeds['path'], 'value:', proceeds['value'])
print('See valuation_result_v03.json. run_case was not called.')
