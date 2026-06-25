import re, glob, os

with open('seo_meta.txt', 'r', encoding='utf-8') as f:
    seo_meta = f.read()

def process_html(content, is_project=False):
    # 1. Clean old Brann meta tags
    strip_patterns = [
        r'<meta\s+content="Brann[^"]*"[^>]*>',
        r'<meta\s+content="A grid-based portfolio[^"]*"[^>]*>',
        r'<meta\s+property="og:title"[^>]*>',
        r'<meta\s+property="og:description"[^>]*>',
        r'<meta\s+property="og:image"[^>]*>',
        r'<meta\s+property="twitter:title"[^>]*>',
        r'<meta\s+property="twitter:description"[^>]*>',
        r'<meta\s+property="og:type"[^>]*>',
        r'<meta\s+name="twitter:card"[^>]*>',
        r'<meta\s+name="description"[^>]*>',
        r'<meta\s+name="keywords"[^>]*>',
        r'<meta\s+name="author"[^>]*>',
        r'<meta\s+name="robots"[^>]*>',
        r'<meta\s+name="theme-color"[^>]*>',
        r'<link\s+rel="canonical"[^>]*>',
        r'<meta\s+property="og:site_name"[^>]*>',
        r'<meta\s+property="og:url"[^>]*>',
        r'<meta\s+property="og:locale"[^>]*>',
        r'<meta\s+name="twitter:image"[^>]*>',
        r'<script\s+type="application/ld\+json">.*?</script>'
    ]
    for pat in strip_patterns:
        content = re.sub(pat, '', content, flags=re.DOTALL)
    
    # 2. Inject SEO Meta tags
    if '<meta charset="utf-8">' in content:
        parts = content.split('<meta charset="utf-8">', 1)
        content = parts[0] + '<meta charset="utf-8">\n  ' + seo_meta + parts[1]

    # 3. Logo replacement
    if is_project:
        content = content.replace('../68a480bd18258a0deef8291e/68a480bd18258a0deef82a85_BRANN.png', '../assets/logo/makewithus.png')
    else:
        content = content.replace('68a480bd18258a0deef8291e/68a480bd18258a0deef82a85_BRANN.png', 'assets/logo/makewithus.png')

    # 4. Remove navbar-cart block precisely
    content = re.sub(r'\s*<div>\s*</a></div>\s*<div class="navbar-cart">.*?</div>(?=\s*</div>)', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<div class="navbar-cart">.*?</div>(?=\s*</div>)', '', content, flags=re.DOTALL)

    # 5. Remove purchase-wrap buttons and ALL PAGES buttons
    content = re.sub(r'\s*<div class="purchase-wrap">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'\s*<a[^>]*w-variant-7de8b098-3e90-ba8b-bd0d-4ac008101edb[^>]*>.*?</a>', '', content, flags=re.DOTALL)
    
    return content

files = glob.glob('*.html') + glob.glob('*.htm') + glob.glob('projects/*.html')

for path in files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        orig = f.read()
    
    is_project = path.startswith('projects')
    cleaned = process_html(orig, is_project)
    
    if orig != cleaned:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"Processed: {path}")

print("Master cleanup complete!")
