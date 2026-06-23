"""
Full structure dump of tiktok-youtube-shorts.html and short-form-video-guidelines.html
Outputs: line ranges for key sections, CSS issues, HTML structure.
"""
import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

def audit_file(rel_path):
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.split('\n')
    
    print('\n' + '='*70)
    print('FILE: %s  (%d lines)' % (rel_path, len(lines)))
    print('='*70)
    
    # 1. Find body/HTML section start
    body_line = next((i for i,l in enumerate(lines,1) if '<body' in l), None)
    head_end  = next((i for i,l in enumerate(lines,1) if '</head>' in l), None)
    print('\n--- Structure markers ---')
    print('  <head> ends  : L%s' % head_end)
    print('  <body> starts: L%s' % body_line)
    
    # 2. Key HTML landmarks
    landmarks = {
        'announce-bar'    : 'id="announce-bar"',
        'header'          : 'id="header"',
        'guide-hero'      : 'class="guide-hero"',
        'guide-body'      : 'class="guide-body"',
        'guide-body-inner': 'class="guide-body-inner"',
        'guide-content'   : 'class="guide-content"',
        'guide-sidebar'   : 'class="guide-sidebar"',
        'footer'          : '<footer',
    }
    print('\n--- HTML landmarks ---')
    for name, pattern in landmarks.items():
        found = [i+1 for i,l in enumerate(lines) if pattern in l]
        print('  %-22s: %s' % (name, found[:5]))
    
    # 3. CSS checks
    css_checks = {
        '.guide-body-inner grid'   : 'grid-template-columns' in text,
        '.hook-visual-panel CSS'   : '.hook-visual-panel' in text,
        '.article-table CSS'       : '.article-table' in text,
        'scroll-margin-top'        : 'scroll-margin-top' in text,
        'script-table class'       : 'script-table' in text,
        'article-table-wrapper'    : 'article-table-wrapper' in text,
    }
    print('\n--- CSS checks ---')
    for name, val in css_checks.items():
        print('  [%s] %s' % ('OK' if val else 'MISSING', name))
    
    # 4. Broken ? chars in body content
    print('\n--- Broken chars in content (after line %s) ---' % (head_end or 0))
    start = (head_end or 0)
    broken = []
    for i in range(start, len(lines)):
        l = lines[i]
        if re.search(r'(?<![=:?/\\])(?<![a-zA-Z0-9])\?(?![a-zA-Z0-9=:>"\'/\\])', l):
            # Skip legit question marks in English text
            if re.search(r'\?\s*[A-Z]', l) or re.search(r'[a-z]\?[^<>]{0,5}$', l):
                continue
            # Look for ? in icon/span contexts
            if re.search(r'>\?<|>\?\s+[A-Z+\d]|>\?\s*<', l):
                broken.append('  L%d: %s' % (i+1, l.strip()[:110]))
    for b in broken[:20]:
        print(b)
    if not broken:
        print('  None found.')
    
    # 5. Show first 50 lines of guide-body content
    gb_line = next((i for i,l in enumerate(lines) if 'class="guide-body"' in l), None)
    if gb_line is not None:
        print('\n--- guide-body content (L%d+) ---' % (gb_line+1))
        for j in range(gb_line, min(gb_line+60, len(lines))):
            print('  %5d: %s' % (j+1, lines[j].rstrip()[:110]))
    
    # 6. Tables
    tables = [i+1 for i,l in enumerate(lines) if '<table' in l.lower()]
    print('\n--- Tables at lines: %s ---' % tables)
    if tables:
        t = tables[0] - 1
        for j in range(t, min(t+50, len(lines))):
            print('  %5d: %s' % (j+1, lines[j].rstrip()[:110]))
    
    # 7. Hook panels
    hooks = [i+1 for i,l in enumerate(lines) if 'hook-visual-panel' in l and '<div' in l]
    print('\n--- hook-visual-panel at lines: %s ---' % hooks)
    if hooks:
        h = hooks[0] - 1
        for j in range(h, min(h+30, len(lines))):
            print('  %5d: %s' % (j+1, lines[j].rstrip()[:110]))

for rel in ['guides/tiktok-youtube-shorts.html',
            'resources/mcp/short-form-video-guidelines.html']:
    audit_file(rel)
