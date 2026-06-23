"""
Check mcp-promotion.html announce bar HTML location.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'mcp-promotion.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Find announce-bar div
for i, line in enumerate(lines, 1):
    if 'id="announce-bar"' in line or "id='announce-bar'" in line:
        print("Found announce-bar at line %d" % i)
        for j in range(i-1, min(i+20, len(lines))):
            print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
        break
else:
    print("NO announce-bar div found!")
    # Check for different format
    for i, line in enumerate(lines, 1):
        if 'announce' in line.lower() and ('<div' in line or '<span' in line):
            print("Announce at line %d: %s" % (i, line.strip()[:100]))

# Check near the header HTML
print("\n=== Lines 2075-2150 (near header HTML) ===")
for j in range(2074, min(2150, len(lines))):
    print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
