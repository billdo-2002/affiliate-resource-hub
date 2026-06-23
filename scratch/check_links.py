"""
Check article link hrefs in general-guide.html after fix.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'guides', 'general-guide.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

print("=== article-links hrefs ===")
for i, line in enumerate(lines, 1):
    if 'article-link-row' in line or ('href=' in line and 'angles' in line):
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Also check mcp-promotion link
print("\n=== MCP promotion links ===")
for i, line in enumerate(lines, 1):
    if 'mcp-promotion' in line.lower():
        print("%5d: %s" % (i, line.rstrip()[:120]))
