"""Assemble report.md from work/report_body.md, generating Appendix B from forecast.json sources for every tag used."""
import json, re
from pathlib import Path
H = Path(__file__).parent
body = (H / 'work' / 'report_body.md').read_text(encoding='utf-8')
src = {s['id']: s for s in json.load(open(H / 'forecast.json'))['sources']}
tags = set(re.findall(r'\b([ACDEGPS]\d+(?:_\d+)?)\b', body))
for ch, a, b in re.findall(r'\[([ACDEGPS])(\d+)\]–\[[ACDEGPS](\d+)\]', body):
    tags.update(f'{ch}{i}' for i in range(int(a), int(b) + 1))
tags = {t for t in tags if t in src}
missing = sorted(set(re.findall(r'\[([ACDEGPS]\d+(?:_\d+)?)\]', body)) - set(src))
assert not missing, missing
# documents referenced by cited entries
for t in list(tags):
    d = src[t].get('document')
    if d: tags.add(d)
for d in ('D12', 'D13', 'D22'): tags.add(d)
key = lambda t: (int(re.match(r'[A-Z](\d+)', t).group(1)), int(t.split('_')[1]) if '_' in t else 0)
groups = [('Documents', 'D'), ('Actuals', 'A'), ('Guidance and management statements', 'G'), ('Estimates', 'E'), ('Assumptions', 'S'), ('Calculations', 'C'), ('Prompt and brief', 'P')]
out = []
for title, ch in groups:
    ids = sorted([t for t in tags if t[0] == ch], key=key)
    if not ids: continue
    out.append(f'**{title}**\n')
    for t in ids:
        s = src[t]; ex = []
        if ch == 'D': ex.append(s['url'])
        else:
            if s.get('document'): ex.append(s['document'])
            if s.get('page') and s['page'] != 'page unverified': ex.append(s['page'])
            if s.get('inputs'): ex.append('inputs ' + ', '.join(s['inputs']))
        out.append(f"- **{t}** {s['text']}" + (f" ({'; '.join(ex)})" if ex else ''))
    out.append('')
out.append('**Not verified**\n')
out.append('- D12 and D13 (Seeking Alpha transcripts): text read from the ceochat mirror; Seeking Alpha links not opened (link unverified).')
out.append('- D22 and S19 (Dan Matlow CEO bot): simulated CEO view, not company disclosure; link unverified.')
out.append('- E-series: whole-number consensus with no analyst count on the page.')
(H / 'report.md').write_text(body.replace('{{APPB}}', '\n'.join(out)), encoding='utf-8')
print(len(tags), 'tags')
