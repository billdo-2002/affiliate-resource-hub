"""
Find hook-visual-panel CSS in the file.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'resources', 'mcp', 'short-form-video-guidelines.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Search for ALL CSS containing "hook" 
print("=== All CSS with 'hook' ===")
for i, line in enumerate(lines, 1):
    if 'hook' in line.lower() and i < 2100:  # CSS is before content
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Also check for article-table
print("\n=== All CSS with 'article-table' ===")
for i, line in enumerate(lines, 1):
    if '.article-table' in line:
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Check what CSS is added near end of <style>
print("\n=== CSS added by our script (near </style>) ===")
style_end = text.rfind('</style>')
if style_end > 0:
    relevant = text[max(0, style_end-3000):style_end]
    # Show last 50 lines before </style>
    rel_lines = relevant.split('\n')
    for j, ln in enumerate(rel_lines[-50:]):
        print("%s" % ln.rstrip()[:120])
