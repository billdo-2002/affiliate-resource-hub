"""
Check article-table CSS and structure in short-form-video-guidelines.html
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'resources', 'mcp', 'short-form-video-guidelines.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Find article-table CSS
print("=== article-table CSS ===")
for i, line in enumerate(lines, 1):
    if 'article-table' in line:
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Find table HTML
print("\n=== Table HTML structure (first table) ===")
for i, line in enumerate(lines, 1):
    if '<table' in line.lower():
        # Show 60 lines around table
        for j in range(max(0, i-5), min(len(lines), i+60)):
            print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
        break
