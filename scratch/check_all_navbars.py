import os, re

base = r'c:\Users\khoadnd\Desktop\onboarding hub'

files = [
    ('guides/general-guide.html', '../../'),
    ('guides/tiktok-youtube-shorts.html', '../../'),
    ('guides/discord-blueprint.html', '../../'),
    ('guides/angles/scale-safely-with-margins.html', '../../../'),
    ('guides/angles/stop-losing-30-profit.html', '../../../'),
    ('guides/angles/track-profit-like-a-pro.html', '../../../'),
    ('resources/mcp/reddit-ready-to-post.html', '../../'),
    ('resources/mcp/short-form-video-guidelines.html', '../../'),
    ('resources/mcp/x-twitter-ready-to-post.html', '../../'),
    ('guides.html', './'),
    ('mcp-promotion.html', './'),
]

for rel_path, prefix in files:
    path = os.path.join(base, rel_path.replace('/', os.sep))
    with open(path, 'rb') as f:
        raw = f.read()
    text = raw.decode('cp1252', errors='replace')
    lines = text.split('\n')
    
    print(f"\n{'='*50}")
    print(f"FILE: {rel_path}")
    print(f"{'='*50}")
    
    # Find announce bar 
    for i, line in enumerate(lines, 1):
        if 'announce' in line.lower() and ('<div' in line or '<button' in line or 'close-btn' in line or 'star' in line.lower()):
            print(f"  L{i}: {line.rstrip()[:100]}")
    
    # Find CTA button  
    for i, line in enumerate(lines, 1):
        if 'btn-cta' in line and 'affiliate' in line.lower():
            print(f"  CTA L{i}: {line.strip()[:120]}")
    
    # Find logo src
    for i, line in enumerate(lines, 1):
        if 'logo' in line.lower() and 'img' in line.lower() and 'src=' in line.lower():
            print(f"  Logo L{i}: {line.strip()[:100]}")
    
    # Count broken chars
    broken = text.count('\ufffd')
    print(f"  Replacement chars: {broken}")
    
    # Check non-ASCII bytes
    bad = [i for i, b in enumerate(raw) if b > 0x7F]
    print(f"  Non-ASCII bytes: {len(bad)}")
    
    # Find close button  
    for i, line in enumerate(lines, 1):
        if 'close-btn' in line and 'button' in line.lower():
            print(f"  CloseBtn L{i}: {line.strip()[:100]}")
