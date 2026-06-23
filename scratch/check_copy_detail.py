"""
Check the full copy-block CSS that was added and article-example-block HTML.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'resources', 'mcp', 'x-twitter-ready-to-post.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Show lines 1960-2025
print("=== Lines 1960-2030 (copy-block CSS area) ===")
for j in range(1959, min(2030, len(lines))):
    print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))

# Show article-example-block HTML
print("\n=== article-example-block HTML (line 3657+) ===")
for j in range(3655, min(3680, len(lines))):
    print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
