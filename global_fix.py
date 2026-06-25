import re, glob, os

with open('seo_meta.txt', 'r', encoding='utf-8') as f:
    seo_meta = f.read()

root_footer = '''    <section class="section_default bg-black">
      <div>
        <div data-wf--spacing--variant="80" class="spacing w-variant-23cec5a7-8f8b-1449-a0ee-fb3db7e00280"></div>
        <div class="w-layout-grid grid-global">
          <div id="w-node-_00e60349-b76d-8deb-43f4-fae809c3c908-283cb5d6" class="w-layout-vflex">
            <div class="max-w-512">
              <p class="all-caps body-3">Join our newsletter</p>
              <div data-wf--spacing--variant="16" class="spacing w-variant-20f33489-51e7-08b1-3ecd-2e9aaaa3f69e"></div>
              <div class="form-block w-form">
                <form id="wf-form-Contact" name="wf-form-Contact" data-name="Contact" method="get" class="form">
                  <input class="form-input is-light w-input" maxlength="256" name="email" data-name="Email" placeholder="Email*" type="email" id="email" required="">
                  <div class="footer-submit_wrap"><input type="submit" data-wait="Please wait..." class="footer-submit_button w-button" value="Subscribe">
                    <div class="icon w-embed"><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewbox="0 0 155 157"><path stroke="currentColor" stroke-width="3" d="M1.5 87.688v1.5h109.691l-48.798 48.797-1.064 1.064 1.068 1.061 13.046 12.954 1.06 1.054 1.058-1.057 73.5-73.5 1.06-1.061-1.06-1.06-73.5-73.5L76.5 2.878l-1.06 1.06-12.955 12.955-1.06 1.06 1.059 1.06 48.711 48.799H1.5v19.874Z"></path></svg></div>
                  </div>
                </form>
                <div class="w-form-done"><div>Thank you! Your submission has been received!</div></div>
                <div class="w-form-fail"><div>Oops! Something went wrong while submitting the form.</div></div>
              </div>
            </div>
            <div data-wf--spacing--variant="200" class="spacing w-variant-f8d86e4f-0b1f-8fe1-0aea-1049b5e19c1c"></div>
            <div class="w-layout-vflex list-v_8"><a data-wf--text-link-underline--variant="title-2" href="{prefix}work-index.html" class="text-link w-variant-8d4b36f4-9b8c-2727-3896-6cae1c2a4cb0 w-inline-block"><div>Work</div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a><a data-wf--text-link-underline--variant="title-2" href="{prefix}news.html" class="text-link w-variant-8d4b36f4-9b8c-2727-3896-6cae1c2a4cb0 w-inline-block"><div>News</div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a><a data-wf--text-link-underline--variant="title-2" href="{prefix}about-1.html" class="text-link w-variant-8d4b36f4-9b8c-2727-3896-6cae1c2a4cb0 w-inline-block"><div>Studio</div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a><a data-wf--text-link-underline--variant="title-2" href="{prefix}services.html" class="text-link w-variant-8d4b36f4-9b8c-2727-3896-6cae1c2a4cb0 w-inline-block"><div>Services</div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a><a data-wf--text-link-underline--variant="title-2" href="{prefix}careers.html" class="text-link w-variant-8d4b36f4-9b8c-2727-3896-6cae1c2a4cb0 w-inline-block"><div>Jobs</div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a><a data-wf--text-link-underline--variant="title-2" href="{prefix}contact-3.html" class="text-link w-variant-8d4b36f4-9b8c-2727-3896-6cae1c2a4cb0 w-inline-block"><div>Contact</div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a></div>
          </div>
          <div id="w-node-_98660fa4-a0e1-b73c-135a-d2d3283cb5e5-283cb5d6">
            <div class="w-layout-vflex">
              <div class="color_muted2"><p class="all-caps body-3">Location</p></div>
              <div data-wf--spacing--variant="16" class="spacing w-variant-20f33489-51e7-08b1-3ecd-2e9aaaa3f69e"></div>
              <p>Trivandrum<br>Kerala</p>
            </div>
            <div data-wf--spacing--variant="80" class="spacing w-variant-23cec5a7-8f8b-1449-a0ee-fb3db7e00280"></div>
            <div class="w-layout-vflex">
              <div class="color_muted2"><p class="all-caps body-3">Contact</p></div>
              <div data-wf--spacing--variant="16" class="spacing w-variant-20f33489-51e7-08b1-3ecd-2e9aaaa3f69e"></div>
              <div class="w-layout-vflex list-v_4"><a href="{prefix}contact-1.html" class="text-link w-inline-block"><div class="w-layout-hflex list-h_center"><div>makewithus.in@gmail.com (</div><div class="icon w-embed"><svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24" fill="currentColor"><path d="M21 3C21.5523 3 22 3.44772 22 4V20.0066C22 20.5552 21.5447 21 21.0082 21H2.9918C2.44405 21 2 20.5551 2 20.0066V19H20V7.3L12 14.5L2 5.5V4C2 3.44772 2.44772 3 3 3H21ZM8 15V17H0V15H8ZM5 10V12H0V10H5ZM19.5659 5H4.43414L12 11.8093L19.5659 5Z"></path></svg></div><div>)</div></div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a><a href="https://cal.com/mwu-meeting" class="text-link w-inline-block"><div class="w-layout-hflex list-h_center"><div>Book a call (</div><div class="icon w-embed"><svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24" fill="currentColor"><path d="M19.9381 8H21C22.1046 8 23 8.89543 23 10V14C23 15.1046 22.1046 16 21 16H19.9381C19.446 19.9463 16.0796 23 12 23V21C15.3137 21 18 18.3137 18 15V9C18 5.68629 15.3137 3 12 3C8.68629 3 6 5.68629 6 9V16H3C1.89543 16 1 15.1046 1 14V10C1 8.89543 1.89543 8 3 8H4.06189C4.55399 4.05369 7.92038 1 12 1C16.0796 1 19.446 4.05369 19.9381 8ZM3 10V14H4V10H3ZM20 10V14H21V10H20ZM7.75944 15.7849L8.81958 14.0887C9.74161 14.6662 10.8318 15 12 15C13.1682 15 14.2584 14.6662 15.1804 14.0887L16.2406 15.7849C15.0112 16.5549 13.5576 17 12 17C10.4424 17 8.98882 16.5549 7.75944 15.7849Z"></path></svg></div><div>)</div></div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a></div>
              <div data-wf--spacing--variant="64" class="spacing w-variant-91a0d231-8691-787f-d5e0-9a56b044983a"></div>
            </div>
            <div data-wf--spacing--variant="80" class="spacing w-variant-23cec5a7-8f8b-1449-a0ee-fb3db7e00280"></div>
          </div>
          <div id="w-node-_3c03a582-744d-2791-ed5b-5e7d0245ce0a-283cb5d6">
            <div class="w-layout-vflex">
              <div class="color_muted2"><p class="all-caps body-3">Social</p></div>
              <div data-wf--spacing--variant="16" class="spacing w-variant-20f33489-51e7-08b1-3ecd-2e9aaaa3f69e"></div>
              <div class="w-layout-vflex list-v_4"><a data-wf--text-link-underline--variant="body-1" href="https://www.instagram.com/makewithus.in/" target="_blank" class="text-link w-inline-block"><div>Instagram</div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a><a data-wf--text-link-underline--variant="body-1" href="https://www.linkedin.com/company/makewithus/" target="_blank" class="text-link w-inline-block"><div>LinkedIn</div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a></div>
            </div>
          </div>
          <div id="w-node-_396884cb-79d8-8a54-3c13-0a5ca9f9fcb3-283cb5d6" class="list-v_4">
            <div class="w-layout-hflex"><p class="color_muted2">Designed by </p><a href="https://mosherhan.life/" target="_blank" class="text-link w-inline-block"><div class="w-layout-hflex list-h_center"><div>Mosherhan </div></div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a></div>
            <div class="w-layout-hflex"><p class="color_muted2">Developed by </p><a href="#" target="_blank" class="text-link w-inline-block"><div class="w-layout-hflex list-h_center"><div>Sudarsanan </div></div><div class="link-hover_wrap"><div class="link-hover_underline"></div></div></a></div>
          </div>
        </div>
        <div data-wf--spacing--variant="80" class="spacing w-variant-23cec5a7-8f8b-1449-a0ee-fb3db7e00280"></div>
        <div class="w-layout-grid grid-global is-gutter">
          <div id="w-node-_2c7431f9-c818-1290-187d-e8afa5dfad59-283cb5d6" class="w-layout-vflex color_muted2">
            <div class="body-3">&#169; Copyright 2025 <a href="#" target="_blank" style="text-decoration: none;" class="text-link_opacity-down is-light">MakeWithUs</a></div>
          </div>
          <div id="w-node-_8f9f53d2-7808-f62e-61d1-54dbd578f1ac-283cb5d6" class="w-layout-vflex tag-list"></div>
        </div>
        <div data-wf--spacing--variant="24" class="spacing w-variant-17d14426-734a-1068-67ce-98c6b1b35952"></div>
      </div>
      <div class="divider"></div><a id="w-node-_318e71a7-78f3-c083-72df-75e7a6d5ef7c-283cb5d6" href="{prefix}sitemap.html" class="footer-link_sitemap w-inline-block">
        <div data-wf--spacing--variant="80" class="spacing w-variant-23cec5a7-8f8b-1449-a0ee-fb3db7e00280"></div>
        <div class="footer-sitemap_heading">
          <p>makewithus&#174;</p>
          <div class="footer-sitemap_icon w-embed"><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewbox="0 0 155 157"><path stroke=\"currentColor\" stroke-width=\"3\" d=\"M1.5 87.688v1.5h109.691l-48.798 48.797-1.064 1.064 1.068 1.061 13.046 12.954 1.06 1.054 1.058-1.057 73.5-73.5 1.06-1.061-1.06-1.06-73.5-73.5L76.5 2.878l-1.06 1.06-12.955 12.955-1.06 1.06 1.059 1.06 48.711 48.799H1.5v19.874Z\"></path></svg></div>
        </div>
        <div data-wf--spacing--variant="64" class="spacing w-variant-91a0d231-8691-787f-d5e0-9a56b044983a"></div>
      </a>
    </section>
'''

def process_html(content, path):
    is_root = '/' not in path and '\\' not in path
    prefix = '' if is_root else '../'

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

    # 3. Logo replacement (Brann to makewithus.png)
    content = re.sub(r'(\.\./)?68a480bd18258a0deef8291e/68a480bd18258a0deef82a85_BRANN\.png', prefix + 'assets/logo/makewithus.png', content)

    # 4. Strip old footer and ALL garbage (including cart and buttons) using string slicing
    footer_start = content.rfind('<section class="section_default bg-black">')
    if footer_start != -1:
        nav_overlay = content.find('<div class="navbar_overlay">', footer_start)
        if nav_overlay != -1:
            # Replace everything from the footer to the nav overlay
            content = content[:footer_start] + root_footer.format(prefix=prefix) + content[nav_overlay:]
    else:
        # Fallback if no footer section found (rare, but maybe)
        content = re.sub(r'\s*<div class="purchase-wrap">.*?</div>', '', content, flags=re.DOTALL)

    return content

files = glob.glob('**/*.html', recursive=True) + glob.glob('*.htm')

for path in files:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        orig = f.read()
    
    cleaned = process_html(orig, path)
    
    if orig != cleaned:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f"Processed: {path}")

print("Global cleanup complete!")
