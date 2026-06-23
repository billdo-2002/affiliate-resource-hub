"""
Look at specific broken ? contexts in content files.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Check index.html around lines 1900-1990 and 2481 and 2874
path = os.path.join(BASE, 'index.html')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')

print("=== index.html broken ? contexts ===")
for target_line in [1898, 1899, 1900, 1967, 1968, 1975, 1982, 1989, 2479, 2480, 2481, 2873, 2874]:
    if target_line < len(lines):
        print("  L%d: %s" % (target_line+1, lines[target_line].rstrip()[:150]))

# Check general-guide.html
path2 = os.path.join(BASE, 'guides', 'general-guide.html')
with open(path2, 'r', encoding='utf-8') as f:
    text2 = f.read()

lines2 = text2.split('\n')
print("\n=== general-guide.html broken ? contexts ===")
for target_line in [2133, 2134, 2184, 2185, 2187, 2188]:
    if target_line < len(lines2):
        print("  L%d: %s" % (target_line+1, lines2[target_line].rstrip()[:150]))

# Check tiktok page
path3 = os.path.join(BASE, 'guides', 'tiktok-youtube-shorts.html')
with open(path3, 'r', encoding='utf-8') as f:
    text3 = f.read()

lines3 = text3.split('\n')
print("\n=== tiktok-youtube-shorts.html broken ? contexts ===")
for target_line in [2159, 2160, 2370, 2371, 2391, 2392]:
    if target_line < len(lines3):
        print("  L%d: %s" % (target_line+1, lines3[target_line].rstrip()[:150]))
