"""
Deep sweep for any remaining broken characters and CSS issues.
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

print("=" * 70)
print("DEEP SWEEP - Remaining Issues")
print("=" * 70)

for rel_path in HTML_FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    issues = []
    
    # Check raw bytes
    with open(path, 'rb') as f:
        raw = f.read()
    for bad_byte in [0x97, 0x96, 0x9B, 0xD7]:
        if raw.count(bytes([bad_byte])) > 0:
            issues.append("Raw byte 0x%02X found" % bad_byte)
    
    # Check UTF-8 validity
    try:
        raw.decode('utf-8')
    except Exception as e:
        issues.append("NOT valid UTF-8: %s" % str(e)[:50])
    
    # Check for stray single ? in HTML content areas (after line 1800, in HTML not CSS)
    html_start = None
    for i, line in enumerate(lines):
        if '</style>' in line or '</head>' in line:
            html_start = i
            break
    
    if html_start:
        for i in range(html_start, len(lines)):
            line = lines[i]
            # Look for ? that seems wrong (not in legit English text like "what?" or URLs)
            # Focus on: standalone ? in arrow/icon contexts
            if re.search(r'(?<=>)\?(?=\s*[\+\-]?\d)', line):  # ? before numbers (broken icon)
                issues.append("Broken icon? at L%d: %s" % (i+1, line.strip()[:80]))
            if re.search(r'class="btn-arrow">\?<', line):
                issues.append("Broken btn-arrow at L%d" % (i+1))
    
    # Check for duplicate CSS blocks
    guide_body_count = text.count('.guide-body-inner {')
    if guide_body_count > 2:
        issues.append("Duplicate .guide-body-inner CSS: %d occurrences" % guide_body_count)
    
    # Check announce-bar has stars (not ?)
    announce_match = re.search(r'id="announce-bar".*?</div>', text, re.DOTALL)
    if announce_match:
        bar_content = announce_match.group()
        star_spans = re.findall(r'<span[^>]*announce-star[^>]*>([^<]*)</span>', bar_content)
        for star in star_spans:
            if '?' in star and '&#' not in star:
                issues.append("Broken star in announce bar: %r" % star)
    
    # Check CTA btn
    cta_matches = re.findall(r'<a[^>]*btn-cta[^>]*>([^<]*)</a>', text)
    for cta in cta_matches:
        if '?' in cta and 'affiliate link' in cta.lower():
            issues.append("Broken CTA: %r" % cta[:60])
    
    if issues:
        print("\n[ISSUES] %s" % rel_path)
        for iss in issues:
            print("  ! %s" % iss)
    else:
        print("[CLEAN]  %s" % rel_path)

print("\n" + "=" * 70)
print("Deep sweep complete.")
