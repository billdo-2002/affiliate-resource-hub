"""
Look at specific lines in index.html to understand what the ? chars should be.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

path = os.path.join(BASE, 'index.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

print("=== index.html around line 1965 (broken icons) ===")
for j in range(1963, min(1995, len(lines))):
    print("%5d: %s" % (j+1, lines[j].rstrip()[:180]))
