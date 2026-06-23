"""
Check reddit page copy block HTML structure.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'resources', 'mcp', 'reddit-ready-to-post.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Find copy blocks
for i, line in enumerate(lines, 1):
    if 'article-example-block' in line or 'copy-post-btn' in line or 'copy-content' in line:
        print("%5d: %s" % (i, line.rstrip()[:120]))
