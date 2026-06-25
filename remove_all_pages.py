import re, glob

files = glob.glob('**/*.html', recursive=True) + glob.glob('*.htm')
pattern = re.compile(r'\s*<a\s+data-wf--button--variant="active"\s+href="[^"]*sitemap\.html"\s+class="button w-variant-7de8b098-3e90-ba8b-bd0d-4ac008101edb w-inline-block"><div class="button_text w-variant-7de8b098-3e90-ba8b-bd0d-4ac008101edb">ALL PAGES</div></a>', re.DOTALL)

count = 0
for path in files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = pattern.sub('', content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Fixed {path}")

print(f"Removed ALL PAGES button from {count} files.")
