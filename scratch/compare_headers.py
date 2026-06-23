"""
Detailed comparison of header HTML between files.
Shows the announce bar + header + first 20 lines of body for each.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

FILES = [
    ('guides/general-guide.html', '../'),
    ('guides/angles/track-profit-like-a-pro.html', '../../'),
    ('resources/mcp/x-twitter-ready-to-post.html', '../../'),
    ('guides.html', ''),
]

for rel_path, prefix in FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    print("\n" + "=" * 60)
    print("FILE: %s" % rel_path)
    print("=" * 60)
    
    # Find body/header start
    body_start = None
    for i, line in enumerate(lines, 1):
        if '<body' in line:
            body_start = i
            break
    
    if body_start:
        print("Body starts at line %d" % body_start)
        # Print 80 lines from body start
        for j in range(body_start-1, min(body_start+80, len(lines))):
            print("%5d: %s" % (j+1, lines[j].rstrip()[:120]))
