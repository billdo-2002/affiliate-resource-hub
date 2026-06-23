"""
Check hook panels in angle pages.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

files = [
    'guides/angles/track-profit-like-a-pro.html',
    'guides/angles/scale-safely-with-margins.html',
]

for rel_path in files:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    print("\n" + "=" * 60)
    print("FILE: %s (%d lines)" % (rel_path, len(lines)))
    print("=" * 60)
    
    # Find hook panel elements
    print("\n--- Hook panels ---")
    for i, line in enumerate(lines, 1):
        if 'hook' in line.lower():
            print("%5d: %s" % (i, line.rstrip()[:120]))
    
    # Find where body content starts (after </header>)
    print("\n--- Body content start ---")
    for i, line in enumerate(lines, 1):
        if '</header>' in line:
            for j in range(i-1, min(i+40, len(lines))):
                print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
            break
    
    # Find guide hero section
    print("\n--- guide-hero ---")
    for i, line in enumerate(lines, 1):
        if 'guide-hero' in line and '<' in line and '/*' not in line:
            print("%5d: %s" % (i, line.rstrip()[:120]))
