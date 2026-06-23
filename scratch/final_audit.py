"""
Final comprehensive audit of all HTML files.
Check for all remaining issues.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

HTML_FILES = [
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

print("=" * 70)
print("FINAL AUDIT")
print("=" * 70)

all_pass = True

for rel_path, prefix in HTML_FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    
    with open(path, 'rb') as f:
        raw = f.read()
    
    try:
        text = raw.decode('utf-8')
        utf8 = True
    except:
        utf8 = False
        text = raw.decode('cp1252', errors='replace')
    
    issues = []
    notes = []
    
    # Encoding
    if not utf8:
        issues.append("NOT UTF-8")
    for bad_byte in [0x97, 0x96, 0x9B]:
        if raw.count(bytes([bad_byte])):
            issues.append("Raw 0x%02X byte found" % bad_byte)
    if '\ufffd' in text:
        issues.append("Replacement char (U+FFFD)")
    
    # charset meta
    if not re.search(r'<meta\s+charset\s*=\s*["\']?UTF-8', text, re.IGNORECASE):
        issues.append("Missing charset=UTF-8")
    
    # Stars in announce bar
    if 'announce-bar' in text:
        stars = re.findall(r'<span[^>]*announce-star[^>]*>([^<]*)</span>', text)
        if stars and any(s.strip() == '?' for s in stars):
            issues.append("Broken stars in announce bar: %s" % stars)
        elif not stars:
            issues.append("No announce-star spans found in announce bar")
        else:
            notes.append("Stars OK: %s" % stars[0])
    else:
        issues.append("NO announce-bar div!")
    
    # CTA arrow
    if 'Get affiliate link' in text:
        if '&rarr;' not in text and '→' not in text:
            issues.append("Missing arrow in CTA")
        else:
            notes.append("CTA arrow OK")
    
    # Close button
    if 'close-btn' in text and '<button' in text:
        close_btns = re.findall(r'<button[^>]*close-btn[^>]*>([^<]*)</button>', text)
        if close_btns and any('?' in b for b in close_btns):
            issues.append("Broken close button: %s" % close_btns)
        else:
            notes.append("Close btn OK")
    
    # Logo path
    logo_matches = re.findall(r'<img[^>]*class="logo-img"[^>]*>', text)
    for lm in logo_matches[:2]:
        src = re.search(r'src="([^"]*)"', lm)
        if src:
            logo_src = src.group(1)
            expected = prefix + 'logo.svg'
            if not logo_src.endswith('logo.svg'):
                issues.append("Wrong logo src: %s (expected %s)" % (logo_src, expected))
    
    # MCP link
    if 'mcp-promotion-playbook.html' in text:
        issues.append("Old MCP link: mcp-promotion-playbook.html")
    
    # scroll-margin-top
    if 'article-section' in text and 'scroll-margin-top' not in text:
        issues.append("Missing scroll-margin-top CSS")
    
    # Hook panels - only for video guidelines page
    if 'short-form-video' in rel_path:
        if 'hook-visual-panel' in text and '.hook-visual-panel' not in text:
            issues.append("Missing hook-visual-panel CSS")
    
    status = "PASS" if not issues else "FAIL"
    if issues:
        all_pass = False
    
    print("\n[%s] %s" % (status, rel_path))
    for issue in issues:
        print("    ISSUE: %s" % issue)
    if not issues:
        for note in notes[:3]:
            print("    note: %s" % note)

print("\n" + "=" * 70)
if all_pass:
    print("ALL FILES PASS AUDIT!")
else:
    print("SOME FILES HAVE ISSUES (see above)")
print("=" * 70)
