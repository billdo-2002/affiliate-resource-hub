"""
Check guide-body CSS in guide pages - ensure 2-column layout is correct.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

guide_files = [
    'guides/general-guide.html',
    'guides/angles/track-profit-like-a-pro.html',
    'resources/mcp/x-twitter-ready-to-post.html',
]

for rel_path in guide_files:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    
    print("\n=== %s ===" % rel_path)
    
    # Check guide-body CSS
    in_guide_body_css = False
    for i, line in enumerate(lines, 1):
        if '.guide-body' in line and i < 2200:
            print("  L%d CSS: %s" % (i, line.rstrip()[:100]))
    
    # Check if guide-body-inner has grid or flex
    guide_body_inner_section = []
    for i, line in enumerate(lines, 1):
        if '.guide-body-inner' in line and '{' in line and i < 2200:
            in_guide_body_css = True
        if in_guide_body_css and i < 2200:
            guide_body_inner_section.append("  L%d: %s" % (i, line.rstrip()[:100]))
            if '}' in line:
                in_guide_body_css = False
    
    for line in guide_body_inner_section:
        print(line)
    
    # Check if max-width is appropriate
    has_860 = '860px' in text
    has_max_width = 'max-width: 860px' in text or 'max-width:860px' in text
    print("  Has max-width 860px: %s" % has_860)
    
    # Check sidebar width  
    has_320 = '320px' in text or '300px' in text or '340px' in text
    print("  Has sidebar width: %s" % has_320)
