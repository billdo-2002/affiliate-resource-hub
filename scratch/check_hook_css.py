"""
Check hook-visual-panel CSS in short-form-video-guidelines.html
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'resources', 'mcp', 'short-form-video-guidelines.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

# Find hook-visual-panel CSS
print("=== hook-visual-panel CSS ===")
for i, line in enumerate(lines, 1):
    if 'hook-visual' in line or 'hook-panel' in line:
        print("%5d: %s" % (i, line.rstrip()[:120]))

# Find article-table CSS
print("\n=== article-table CSS ===")
in_css = False
for i, line in enumerate(lines, 1):
    if '.article-table' in line and '{' in line:
        in_css = True
        print("%5d: %s" % (i, line.rstrip()[:120]))
    elif in_css:
        print("%5d: %s" % (i, line.rstrip()[:120]))
        if '}' in line:
            in_css = False
