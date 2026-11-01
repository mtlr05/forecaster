"""Scratch dry check (read-only copy of Finagle under /workspace/out/finagle_scratch; NOT a valuation; does not call the Finagle bot).
Usage: python3 dry11.py case_<sc>_v11.json  -> prints revenue, ebitda, capex, da, cash."""
import sys, json, os, tempfile, io, contextlib
sys.path.insert(0, '/workspace/out/finagle_scratch')
from finagle.agent.compile import compile_case, normalize_assumed_paths
from finagle.agent import runner
from finagle.company import company
def run(c):
    c, _ = normalize_assumed_paths(json.loads(json.dumps(c))); comp = compile_case(c)
    p = os.getcwd()
    with tempfile.TemporaryDirectory() as t, contextlib.redirect_stdout(io.StringIO()):
        os.chdir(t); m = company(**comp['constructor'])
        for st in comp['steps']: runner._invoke(m, st, comp['financials'])
        os.chdir(p)
    return {k: [float(x) for x in m.fin[k]] for k in ('revenue', 'ebitda', 'capex', 'da', 'cash', 'debt') if k in m.fin}
if __name__ == '__main__':
    f = run(json.load(open(sys.argv[1])))
    for k, v in f.items(): print(k, [round(x, 2) for x in v])
