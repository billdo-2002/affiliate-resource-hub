"""
Look at hook card sections in the angle pages.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'guides', 'angles', 'track-profit-like-a-pro.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Print lines 2155 to 2350 (guide content area)
print("=== track-profit-like-a-pro.html - guide body content ===")
for j in range(2154, min(2350, len(lines))):
    print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
