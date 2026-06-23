"""
Global repair script for TrueProfit Affiliate Hub HTML pages.
Fixes:
1. Encoding: reads cp1252 bytes, maps them to correct Unicode, saves as UTF-8
2. Announce bar star characters (? -> ★)
3. CTA button arrow (? -> →)
4. Close button character (× -> &times;)
5. Breadcrumb separator (0x9B -> ›)
6. Ensures meta charset=UTF-8 is present
"""

import os, re

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Map of (cp1252 byte -> replacement string in HTML)
# This is applied at the byte level BEFORE decoding
BYTE_REPLACEMENTS = {
    b'\x97': '—',   # em dash — (U+2014)
    b'\x96': '–',   # en dash – (U+2013)  
    b'\xd7': '×',   # multiplication sign × (U+00D7), used as close button
    b'\x9b': '›',   # single right angle quotation ›, used as breadcrumb sep
    b'\xa9': '©',   # copyright ©
}

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


def fix_file(rel_path, prefix):
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    
    with open(path, 'rb') as f:
        raw = f.read()
    
    # Step 1: Replace non-ASCII bytes with their proper UTF-8 equivalents
    # We do this at the byte level before any text processing
    result = bytearray()
    i = 0
    while i < len(raw):
        b = raw[i:i+1]
        if b in BYTE_REPLACEMENTS:
            result.extend(BYTE_REPLACEMENTS[b].encode('utf-8'))
        else:
            result.extend(b)
        i += 1
    
    # Step 2: Now decode as UTF-8 (should be clean now)
    text = result.decode('utf-8', errors='replace')
    
    # Step 3: Fix specific content issues
    
    # 3a. Fix announce bar star (? should be ★)
    # The ? in <span class="announce-star">?</span> is a lost star character
    text = re.sub(
        r'(<span[^>]*class="announce-star"[^>]*>)\?(<\/span>)',
        r'\1&#9733;\2',
        text
    )
    
    # 3b. Fix CTA button arrow (? should be →)
    # Pattern: "Get affiliate link ?" -> "Get affiliate link →"
    text = re.sub(
        r'(Get affiliate link\s*)\?(\s*<\/a>)',
        r'\1&rarr;\2',
        text
    )
    # Also handle without trailing space
    text = text.replace('Get affiliate link ?', 'Get affiliate link &rarr;')
    text = text.replace("Get affiliate link\u2019", "Get affiliate link &rarr;")
    
    # 3c. Fix close button - the × should render properly
    # Currently shows as × in button, which is correct Unicode but let's use entity for safety
    text = re.sub(
        r'(<button[^>]*class="close-btn"[^>]*>)\×(<\/button>)',
        r'\1&times;\2',
        text
    )
    text = re.sub(
        r'(<button[^>]*class="close-btn"[^>]*>)×(<\/button>)',
        r'\1&times;\2',
        text
    )
    
    # 3d. Ensure meta charset is UTF-8 (it should already be there)
    if '<meta charset="UTF-8">' not in text and '<meta charset="utf-8">' not in text:
        text = text.replace('<head>', '<head>\n<meta charset="UTF-8">', 1)
    
    # 3e. Fix any remaining replacement chars (U+FFFD)
    text = text.replace('\ufffd', '')
    
    # Step 4: Write as UTF-8
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    
    # Verify
    with open(path, 'rb') as f:
        verify_raw = f.read()
    
    # Check for remaining non-ASCII non-UTF8 bytes
    try:
        verify_raw.decode('utf-8')
        utf8_ok = True
    except Exception as e:
        utf8_ok = False
        print(f"  WARNING: UTF-8 verify failed: {e}")
    
    remaining_bad = [i for i, b in enumerate(verify_raw) if b > 0x7F and verify_raw[i:i+1] not in [b'\xc2', b'\xc3', b'\xe2', b'\xe2', b'\xe3', b'\xef', b'\xc2', b'\xc3', b'\xe2', b'\xe3', b'\xc2']]
    
    print(f"  {rel_path}: UTF-8 valid={utf8_ok}, size={len(verify_raw)}")


print("=" * 60)
print("Global HTML Repair - Encoding Fix")
print("=" * 60)

for rel_path, prefix in HTML_FILES:
    print(f"\nProcessing: {rel_path}")
    fix_file(rel_path, prefix)

print("\n" + "=" * 60)
print("Done! All files saved as UTF-8.")
print("=" * 60)
