"""
Check article-example-block CSS in x-twitter page and add if missing.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Check x-twitter for article-example-block CSS
for rel_path in ['resources/mcp/x-twitter-ready-to-post.html', 'resources/mcp/reddit-ready-to-post.html']:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    
    print("=== %s ===" % rel_path)
    
    has_example_block_css = '.article-example-block' in text
    has_copy_content_css = '.copy-content' in text
    
    print("  Has .article-example-block CSS: %s" % has_example_block_css)
    print("  Has .copy-content CSS: %s" % has_copy_content_css)
    
    # Search for any existing article-example-block CSS
    if has_example_block_css:
        for i, line in enumerate(lines, 1):
            if '.article-example-block' in line:
                print("  Line %d: %s" % (i, line.rstrip()[:100]))

print("\n")
