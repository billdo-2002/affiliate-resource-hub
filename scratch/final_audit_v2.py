"""
Final comprehensive audit of all HTML files.
Checks: encoding, announce-bar, header, MCP links, CSS health, file sizes.
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

FILES = [
    ('index.html', ''),
    ('guides.html', ''),
    ('mcp-promotion.html', ''),
    ('guides/discord-blueprint.html', '../'),
    ('guides/general-guide.html', '../'),
    ('guides/tiktok-youtube-shorts.html', '../'),
    ('guides/angles/scale-safely-with-margins.html', '../../'),
    ('guides/angles/stop-losing-30-profit.html', '../../'),
    ('guides/angles/track-profit-like-a-pro.html', '../../'),
    ('resources/mcp/reddit-ready-to-post.html', '../../'),
    ('resources/mcp/short-form-video-guidelines.html', '../../'),
    ('resources/mcp/x-twitter-ready-to-post.html', '../../'),
]

print('=' * 75)
print('FINAL COMPREHENSIVE AUDIT')
print('=' * 75)

all_pass = True

for rel_path, prefix in FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'rb') as f:
        raw = f.read()
    
    # UTF-8 check
    try:
        text = raw.decode('utf-8')
        utf8_ok = True
    except Exception as e:
        utf8_ok = False
        text = raw.decode('latin-1')

    issues = []

    # 1. Encoding
    if not utf8_ok:
        issues.append('NOT valid UTF-8')
    for bad in [0x97, 0x96, 0x9B]:
        if raw.count(bytes([bad])):
            issues.append('Raw 0x%02X byte' % bad)
    if '\ufffd' in text:
        issues.append('Replacement char U+FFFD')

    # 2. Announce bar
    if 'id="announce-bar"' not in text:
        issues.append('Missing announce-bar')
    else:
        stars = re.findall(r'class="announce-star"[^>]*>([^<]*)<', text)
        if stars and '?' in stars[0]:
            issues.append('Broken star in announce bar')

    # 3. MCP link
    if 'mcp-promotion-playbook.html' in text:
        issues.append('Old MCP link (mcp-promotion-playbook.html)')

    # 4. Broken arrows/CTAs
    if 'Get affiliate link ?' in text or 'Get My Affiliate Link ?' in text:
        issues.append('Broken arrow in CTA')
    
    # 5. Broken btn-arrow
    if re.search(r'class="btn-arrow">\?<', text):
        issues.append('Broken btn-arrow ?')

    # 6. Duplicate @media blocks
    c1023 = text.count('@media (max-width: 1023px)')
    if c1023 > 1:
        issues.append('%d duplicate @media 1023px blocks' % c1023)

    # 7. Broken hamburger content
    if 'content: "?"' in text:
        issues.append('Broken hamburger icon content: "?"')

    # 8. Unclosed @media 1024px (nested 1100px)
    if '@media (max-width: 1024px)' in text:
        idx = text.find('@media (max-width: 1024px)')
        next_media = text.find('@media', idx + 10)
        next_close = text.find('}', idx + 10)
        if next_media < next_close:
            # Another @media starts before the first } — means unclosed
            issues.append('Unclosed @media 1024px block (nested media)')

    # 9. Scroll margin
    if 'article-section' in text and 'scroll-margin-top' not in text:
        issues.append('Missing scroll-margin-top')

    # 10. File size sanity (should be reasonable after dedup)
    size_kb = len(raw) / 1024
    size_note = '%.1f KB' % size_kb
    if size_kb > 200:
        issues.append('File too large: %s' % size_note)

    status = 'PASS' if not issues else 'FAIL'
    if issues:
        all_pass = False
    
    print('\n[%s] %s  (%s)' % (status, rel_path, size_note))
    for iss in issues:
        print('  ! %s' % iss)

print('\n' + '=' * 75)
if all_pass:
    print('ALL 12 FILES PASS!')
else:
    print('SOME FILES HAVE ISSUES (see above)')
print('=' * 75)
