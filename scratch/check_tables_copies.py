"""
Check specific pages for tables and copy blocks.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Check short-form-video-guidelines for table
print("=== short-form-video-guidelines.html - tables ===")
path = os.path.join(BASE, 'resources', 'mcp', 'short-form-video-guidelines.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')

# Find table elements
for i, line in enumerate(lines, 1):
    if '<table' in line.lower() or '</table>' in line.lower() or '<thead' in line.lower() or '<tbody' in line.lower():
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Find script-table CSS
print("\n--- script-table CSS ---")
for i, line in enumerate(lines, 1):
    if 'script-table' in line or 'table-wrapper' in line:
        print("%5d: %s" % (i, line.rstrip()[:100]))

# Check x-twitter for copy blocks
print("\n\n=== x-twitter-ready-to-post.html - copy blocks ===")
path = os.path.join(BASE, 'resources', 'mcp', 'x-twitter-ready-to-post.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')

for i, line in enumerate(lines, 1):
    if 'copy-block' in line.lower() or 'copy-post' in line.lower() or 'copy-btn' in line.lower():
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Find affiliate link references
print("\n--- affiliate link ---")
for i, line in enumerate(lines, 1):
    if 'affiliate link' in line.lower() or 'affiliate-link' in line.lower():
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Find first content section after header
print("\n--- First body content sections ---")
body_found = False
for i, line in enumerate(lines, 1):
    if '</header>' in line or 'guide-body' in line or 'guide-hero' in line or 'article-section' in line:
        if not body_found:
            body_found = True
            print("Content sections starting at line %d" % i)
        print("%5d: %s" % (i, line.rstrip()[:100]))
