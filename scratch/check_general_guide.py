"""
Look at general-guide.html content body.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'guides', 'general-guide.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
print("Total lines: %d" % len(lines))

# Find guide-body and show content
for i, line in enumerate(lines, 1):
    if 'guide-body' in line and '<' in line:
        print("Guide body at line %d" % i)
        for j in range(i-1, min(i+150, len(lines))):
            print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
        break
