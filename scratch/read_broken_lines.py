"""
Fix remaining broken ? characters in HTML content.
These are places where emoji, arrows, or dashes were lost during encoding.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Read each file and show full truncated lines
FILES_TO_CHECK = {
    'index.html': [1899, 1967, 1974, 1981, 1988, 2480, 2873],
    'guides/general-guide.html': [2133, 2184, 2187],
    'guides/tiktok-youtube-shorts.html': [2159, 2370, 2391],
}

for rel_path, line_nums in FILES_TO_CHECK.items():
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print("\n=== %s ===" % rel_path)
    for ln in line_nums:
        if ln < len(lines):
            print("L%d: %s" % (ln+1, lines[ln].rstrip()))
