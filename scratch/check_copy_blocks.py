"""
Check copy blocks in detail.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Check the copy-post CSS in x-twitter
path = os.path.join(BASE, 'resources', 'mcp', 'x-twitter-ready-to-post.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Find copy-post-btn CSS
print("=== copy-post-btn CSS ===")
for i, line in enumerate(lines, 1):
    if 'copy-post-btn' in line or 'post-card' in line:
        if '{' in line or 'background' in line or 'padding' in line or 'border' in line or 'class=' in line:
            print("%5d: %s" % (i, line.rstrip()[:120]))

# Find a copy block HTML
print("\n=== First copy block HTML ===")
for i, line in enumerate(lines, 1):
    if 'copy-post-btn' in line and 'button' in line:
        # Show 40 lines of context
        for j in range(max(0, i-25), min(len(lines), i+15)):
            print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
        break

# Check affiliate-link spans in copy blocks
print("\n=== affiliate-link spans ===")
for i, line in enumerate(lines, 1):
    if 'affiliate-link' in line and ('span' in line.lower() or 'class=' in line):
        print("%5d: %s" % (i, line.rstrip()[:120]))
