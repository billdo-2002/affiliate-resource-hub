"""
Check for remaining ? characters in content (not just announce bar).
These could be broken emoji or characters.
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

print("Checking for stray ? characters in content...")

for rel_path in HTML_FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    
    # Find ? in HTML content (not in CSS, not in announce-star context)
    for i, line in enumerate(lines, 1):
        # Skip CSS (before line 2000 and containing CSS patterns)
        if i > 300 and i < 1900:  # CSS region
            continue
        # Skip announce-star spans (already fixed)
        if 'announce-star' in line:
            continue
        # Look for ? in visible content
        if '?' in line and not line.strip().startswith('/*') and not line.strip().startswith('//'):
            # More specific: look for ? surrounded by text/HTML
            if re.search(r'[^\\?<]?\?(?!\s*(=|>|\\|&|,|\.))', line):
                # Check if it's in a context that suggests broken char
                stripped = line.strip()
                if any(kw in stripped for kw in ['article-p', '<p', '<li', '<span', '<div>', '&rsaquo;', '<h2', '<h3']):
                    print("  %s L%d: %s" % (rel_path.split('/')[-1], i, stripped[:100]))
