"""
Check announce bar state in mcp-promotion.html and also examine
header/navbar structure differences between files.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Read mcp-promotion.html
path = os.path.join(BASE, 'mcp-promotion.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Find announce bar HTML
print("=== mcp-promotion.html announce bar ===")
for i, line in enumerate(lines, 1):
    if 'announce-bar' in line or 'announce-star' in line:
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Find header/logo
print("\n=== mcp-promotion.html header ===")
for i, line in enumerate(lines, 1):
    if '<header' in line or 'header-inner' in line or 'header-logo' in line or 'mega-menu' in line.lower():
        print("%5d: %s" % (i, line.rstrip()[:120]))
        
# Find the body HTML start
print("\n=== mcp-promotion.html body start ===")
for i, line in enumerate(lines, 1):
    if '</style>' in line or '</head>' in line or '<body' in line:
        print("%5d: %s" % (i, line.rstrip()[:80]))
        # Show next 30 lines
        for j in range(i, min(i+30, len(lines))):
            print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
        break
