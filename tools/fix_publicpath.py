#!/usr/bin/env python3
"""
Patch Webflow runtime JS files to add a fallback when automatic publicPath detection fails.
Run this from the project root on Windows PowerShell like:
  python .\tools\fix_publicpath.py
"""
import re
from pathlib import Path

root = Path(r"c:\Downloaded Web Sites\brann-template.webflow.io")
js_dir = root / "68a480bd18258a0deef8291e" / "js"
if not js_dir.exists():
    print("JS directory not found:", js_dir)
    raise SystemExit(1)

pattern = re.compile(r'if\(!e\)throw Error\("Automatic publicPath is not supported in this browser"\);')
replacement = (
    'if(!e){try{e=(t&&t.currentScript&&t.currentScript.src)?t.currentScript.src:(r.g&&r.g.location?String(r.g.location):\'./\')}catch(err){e=\'./\'}}'
)

modified = []
for p in js_dir.glob('webflow.*.js'):
    text = p.read_text(encoding='utf-8')
    if pattern.search(text):
        bak = p.with_suffix(p.suffix + '.bak')
        if not bak.exists():
            bak.write_text(text, encoding='utf-8')
        new_text = pattern.sub(replacement, text, count=1)
        p.write_text(new_text, encoding='utf-8')
        modified.append(p.name)

print(f"Patcher finished. Modified {len(modified)} files.")
for m in modified:
    print(" -", m)
