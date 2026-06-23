"""
Final verification - check for remaining problematic content.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

HTML_FILES = [
    'index.html',
    'guides.html',
    'mcp-promotion.html',
    'guides/discord-blueprint.html',
    'guides/general-guide.html',
    'guides/tiktok-youtube-shorts.html',
    'guides/angles/scale-safely-with-margins.html',
    'guides/angles/stop-losing-30-profit.html',
    'guides/angles/track-profit-like-a-pro.html',
    'resources/mcp/reddit-ready-to-post.html',
    'resources/mcp/short-form-video-guidelines.html',
    'resources/mcp/x-twitter-ready-to-post.html',
]

# Broken UTF-8 patterns that should not appear
# These are cp1252 chars that got double-encoded as UTF-8
BROKEN_PATTERNS = [
    b'\xe2\x80\x99',   # correct UTF-8 for curly apostrophe (this is OK!)
    # Actually, let's check for truly broken sequences
]

all_ok = True

for rel_path in HTML_FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    
    with open(path, 'rb') as f:
        raw = f.read()
    
    issues = []
    
    # 1. UTF-8 validation
    try:
        text = raw.decode('utf-8')
        utf8 = True
    except Exception as e:
        text = raw.decode('cp1252', errors='replace')
        utf8 = False
        issues.append("NOT valid UTF-8: " + str(e))
    
    # 2. Check for raw cp1252 problem bytes
    for bad_byte in [0x97, 0x96, 0x9B]:
        count = raw.count(bytes([bad_byte]))
        if count > 0:
            issues.append("Raw 0x%02X byte: %d occurrences" % (bad_byte, count))
    
    # 3. Check for replacement character (U+FFFD)
    fffd_count = text.count('\ufffd')
    if fffd_count > 0:
        issues.append("Replacement chars (FFFD): %d" % fffd_count)
    
    # 4. mcp-promotion.html announce bar stars
    if 'mcp-promotion' in rel_path:
        stars_in_bar = re.findall(r'<span[^>]*announce-star[^>]*>([^<]*)</span>', text)
        if stars_in_bar:
            issues.append("Stars in announce bar: " + str(stars_in_bar))
    
    # 5. Check CTA arrow 
    if 'Get affiliate link' in text:
        if '&rarr;' not in text and '\u2192' not in text:
            issues.append("CTA arrow may be missing or broken")
    
    status = "OK" if not issues else "ISSUES"
    if issues:
        all_ok = False
    
    print("[%s] %s" % (status, rel_path))
    for issue in issues:
        print("        ! " + issue)

print()
if all_ok:
    print("ALL FILES PASS - encoding is clean!")
else:
    print("Some files have issues (listed above)")
