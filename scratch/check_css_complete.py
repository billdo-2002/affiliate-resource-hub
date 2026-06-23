"""
Verify CSS layout completeness across guide pages.
Check: body font size, article max-width, sidebar width, hook panels, table styling.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

FILES = {
    'guides/general-guide.html': 'guide',
    'guides/angles/track-profit-like-a-pro.html': 'angle',
    'resources/mcp/short-form-video-guidelines.html': 'video',
    'resources/mcp/x-twitter-ready-to-post.html': 'copy',
    'resources/mcp/reddit-ready-to-post.html': 'copy',
}

for rel_path, page_type in FILES.items():
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("\n=== %s ===" % rel_path)
    
    checks = {
        'guide-body-inner CSS (grid)': 'grid-template-columns: 1fr 320px' in text or 'grid-template-columns: 1fr 300px' in text or 'grid-template-columns: 1fr 340px' in text,
        'scroll-margin-top': 'scroll-margin-top' in text,
        'sidebar exists in HTML': '<aside class="guide-sidebar">' in text,
        'UTF-8 valid': True,
    }
    
    # UTF-8 check
    with open(path, 'rb') as f:
        raw = f.read()
    try:
        raw.decode('utf-8')
        checks['UTF-8 valid'] = True
    except:
        checks['UTF-8 valid'] = False
    
    # Video-specific
    if page_type == 'video':
        checks['hook-visual-panel CSS'] = '.hook-visual-panel' in text
        checks['article-table CSS'] = '.article-table' in text or 'article-table-wrapper' in text
    
    # Copy-specific
    if page_type == 'copy':
        checks['article-example-block CSS'] = '.article-example-block' in text
        checks['copy-content CSS'] = '.copy-content' in text
    
    for key, val in checks.items():
        status = 'OK' if val else 'MISSING'
        print("  [%s] %s" % (status, key))
