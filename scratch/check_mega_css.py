"""
Check mega-menu CSS (Creative Assets zone) for overflow/clipping issues.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Check a few representative files
FILES = ['index.html', 'guides/general-guide.html', 'resources/mcp/x-twitter-ready-to-post.html']

for rel_path in FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    
    print("\n=== %s ===" % rel_path)
    
    # Find mega-asset-card CSS
    in_mega = False
    for i, line in enumerate(lines, 1):
        if '.mega-asset-card' in line and i < 1800:
            in_mega = True
        if in_mega and i < 1800:
            print("  L%d: %s" % (i, line.rstrip()[:100]))
            if '}' in line and '.mega' not in line:
                in_mega = False
    
    # Check Creative Assets HTML zone exists
    has_creative = 'CREATIVE ASSETS' in text or 'Creative Assets' in text
    has_mega_asset_card = 'mega-asset-card' in text
    has_mega_zone_3 = 'mega-zone-3' in text
    
    print("  Creative Assets zone: %s" % has_creative)
    print("  mega-asset-card HTML: %s" % has_mega_asset_card)
    print("  mega-zone-3 HTML: %s" % has_mega_zone_3)
    
    # Check if mega-asset-svg overflow is handled
    has_overflow_fix = 'mega-asset-svg' in text
    print("  mega-asset-svg: %s" % has_overflow_fix)
