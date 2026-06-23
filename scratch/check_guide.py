"""
Check guide pages for article layout issues and hook panels.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Check general-guide.html for article layout
path = os.path.join(BASE, 'guides', 'general-guide.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
print("=== general-guide.html (%d lines) ===" % len(lines))

# Find guide-body layout
for i, line in enumerate(lines, 1):
    if 'guide-body' in line or 'guide-sidebar' in line or 'guide-content' in line or 'article' in line.lower():
        if '<div' in line or 'class=' in line:
            print("%5d: %s" % (i, line.rstrip()[:120]))

# Find hook panels
print("\n--- Hook panels ---")
for i, line in enumerate(lines, 1):
    if 'hook' in line.lower() and ('panel' in line.lower() or 'card' in line.lower() or '<div' in line):
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Find scroll-margin
print("\n--- scroll-margin-top ---")
for i, line in enumerate(lines, 1):
    if 'scroll-margin' in line:
        print("%5d: %s" % (i, line.rstrip()[:100]))

# Show lines around guide-body
print("\n--- Guide body HTML context ---")
for i, line in enumerate(lines, 1):
    if 'guide-layout' in line or 'guide-main' in line or ('guide-body' in line and '<div' in line):
        print("Found at line %d:" % i)
        for j in range(max(0, i-3), min(len(lines), i+20)):
            print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
        break
