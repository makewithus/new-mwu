import re, os, glob

def remove_cart_block(content):
    """Remove the navbar-cart block and the orphan <div></a></div> wrapper before it."""
    # Remove the entire outer wrapper div that contains the navbar-cart
    # Pattern: <div> (on its own) -> </a></div> -> <div class="navbar-cart">...full cart...</div> -> </div>
    content = re.sub(
        r'\s*<div>\s*</a></div>\s*<div class="navbar-cart">[\s\S]*?</div>\s*</div>',
        '',
        content
    )
    # Also remove any leftover standalone navbar-cart div
    content = re.sub(
        r'\s*<div class="navbar-cart">[\s\S]*?</div>\s*</div>',
        '',
        content
    )
    # Remove purchase-wrap buttons
    content = re.sub(r'\s*<div class="purchase-wrap">[\s\S]*?</div>', '', content)
    # Remove ALL PAGES variant button
    content = re.sub(
        r'\s*<a[^>]*w-variant-7de8b098-3e90-ba8b-bd0d-4ac008101edb[^>]*>[\s\S]*?</a>',
        '',
        content
    )
    # Remove orphan integrity attribute that might be left
    content = content.replace(
        ' integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="',
        ''
    )
    return content

all_patterns = [
    '*.html', '*.htm',
    'projects/*.html',
    'careers/*.html',
    'clients/*.html',
    'blog-posts/*.html',
    'blog-categories/*.html',
]

files = []
for p in all_patterns:
    files.extend(glob.glob(p))

for path in files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
        original = fh.read()
    cleaned = remove_cart_block(original)
    if cleaned != original:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(cleaned)
        print(f'Cleaned: {path} (removed {len(original) - len(cleaned)} chars)')

print('All done')
