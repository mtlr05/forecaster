"""Re-execute Finagle's saved notebook_code per case (display_fin's Windows template path replaced) and
fill a copy of finagle/company_template.xlsx exactly as company.display_fin does. Writes
finagle_notebook_<case>.py, CLPT_<case>.xlsx and finagle_template_table.json. Never sets gt."""
import json, sys, datetime
from pathlib import Path
HERE = Path(__file__).parent
OUT = Path("/workspace/out/clpt_val_v11")
FIN = Path("/workspace/forecaster-work/finagle")
sys.path.insert(0, str(FIN))
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
d = json.load(open(OUT / "finagle_run_v11.json"))
ROWS = ['revenue', 'ebitda', 'sbc', 'da', 'interest', 'income_pretax', 'nol', 'income_taxable', 'tax_cash', 'tax', 'capex', 'MnA',
        'dDebt', 'dwc', 'fcf', 'fcfe', 'fcff', 'buybacks', 'dividend', 'cash', 'cashBS', 'noa', 'equity', 'debt', 'EV', 'wacc',
        'firm', 'shares', 'price', 'value_per_share', 'value_per_share_DDM']
out = {}
for case, v in d.items():
    code = v["result"]["notebook_code"]
    (OUT / f"finagle_notebook_{case}.py").write_text(code)
    ns = {}
    exec(code.replace("co.display_fin()", ""), ns)
    co = ns["co"]
    fin = co.fin
    wb = load_workbook(FIN / "company_template.xlsx")
    ws = wb["raw data"]
    for r in dataframe_to_rows(fin.T, index=True, header=True):
        ws.append(r)
    ws["A1"] = "date"
    ws = wb["report"]
    ws["B2"], ws["B3"], ws["B4"] = "CLPT " + case, datetime.date(2026, 10, 26).isoformat(), "David May"
    ws["B6"], ws["B7"], ws["B8"], ws["B9"] = co.rd, co.re, co.gt, co.t
    ws["B11"], ws["B12"], ws["B13"] = float(fin["cash"].iloc[-1]), co.fcfet, float(fin["equity"].iloc[-1])
    ws["B15"], ws["B17"] = co.shares, float(fin["value_per_share_DDM"].iloc[0])
    wb.save(OUT / f"CLPT_{case}.xlsx")
    cols = [c for c in ROWS if c in fin.columns]
    out[case] = {"header": dict(rd=co.rd, re=co.re, gt=co.gt, t=co.t, cash_generated=float(fin["cash"].iloc[-1]),
                                terminal_fcfe=co.fcfet, terminal_value=float(fin["equity"].iloc[-1]), shares=co.shares,
                                vps=float(fin["value_per_share"].iloc[0]), vps_ddm=float(fin["value_per_share_DDM"].iloc[0])),
                 "years": [str(x)[:10] for x in fin.index], "rows": {c: [float(x) for x in fin[c]] for c in cols}}
    print(case, out[case]["header"])
json.dump(out, open(OUT / "finagle_template_table_v11.json", "w"), indent=1)
