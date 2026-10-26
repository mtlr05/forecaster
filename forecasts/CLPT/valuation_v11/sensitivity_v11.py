"""v11 sensitivity (Finagle reruns, one input at a time) and PV split of value per share. Never sets gt."""
import json, copy
src = open("/workspace/out/clpt_val_v11/run_finagle_v11.py").read().split("\nout = {}\nRD")[0]
ns = {}; exec(src, ns)
ns["RD"], ns["RE"] = True, False
build, sbc_path, first_pos, run_case, leaf = ns["build"], ns["sbc_path"], ns["first_pos"], ns["run_case"], ns["leaf"]
def value(label, mod=None):
    c0 = build(label, True)
    if mod: mod(c0)
    nb = {}; exec(run_case(c0)["notebook_code"].replace("co.display_fin()", ""), nb)
    eb = list(nb["co"].fin["ebitda"]); st = first_pos(eb)
    c = build(label, True, sbc_path(eb, st, 15, eb[15]), st)
    if mod: mod(c)
    r = run_case(c); nb = {}; exec(r["notebook_code"].replace("co.display_fin()", ""), nb)
    return r["value_per_share"], nb["co"]
def setr(k, v): return lambda c: c["rates"].__setitem__(k, leaf(v, "assumption", "sensitivity"))
def setm(k, d): return lambda c: c["forecast"]["margin_path"].__setitem__(k, leaf(c["forecast"]["margin_path"][k]["value"] + d, "assumption", "sensitivity"))
out = {}
for label in ("base", "bull", "bear"):
    v, co = value(label)
    fin = co.fin; re = co.re; sh = co.shares
    div = list(fin["dividend"]); 
    pv = [div[i] / (1 + re) ** i for i in range(len(div))]
    exp = sum(pv[1:7]); fade = sum(pv[7:16]); total = float(fin["value_per_share_DDM"].iloc[0])
    cash0 = co.cash0 / sh
    out[label] = {"vps": v, "pv_fy26_31": exp, "pv_fy32_40": fade, "cash0_ps": cash0, "pv_terminal": total - exp - fade - cash0 - div[0]}
    for name, m in (("re -1pt", setr("re", re - 0.01)), ("re +1pt", setr("re", re + 0.01)),
                    ("mc -10pts", setm("mc", -0.10)), ("mc +10pts", setm("mc", 0.10)),
                    ("gsnext -5pts", setm("gsnext", -0.05)), ("gsnext +5pts", setm("gsnext", 0.05)),
                    ("roict 20%", setr("roict", 0.20)), ("roict 30%", setr("roict", 0.30))):
        out[label][name] = value(label, m)[0]
    print(label, {k: round(x, 2) for k, x in out[label].items()})
json.dump(out, open("/workspace/out/clpt_val_v11/sensitivity_v11.json", "w"), indent=1)
