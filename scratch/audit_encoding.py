import os, re

base = r'c:\Users\khoadnd\Desktop\onboarding hub'

html_files = [
    'index.html',
    'guides.html',
    'mcp-promotion.html',
    'guides/discord-blueprint.html',
    'guides/general-guide.html',
    'guides/tiktok-youtube-shorts.html',
    'guides/angles/scale-safely-with-margins.html',
    'guides/angles/stop-losing-30-profit.html',
    'guides/angles/track-profit-like-a-pro.html',
    'resources/mcp/reddit-ready-to-post.html',
    'resources/mcp/short-form-video-guidelines.html',
    'resources/mcp/x-twitter-ready-to-post.html',
]

for rel_path in html_files:
    path = os.path.join(base, rel_path.replace('/', os.sep))
    try:
        with open(path, 'rb') as f:
            raw = f.read()
        
        bad_positions = [i for i, b in enumerate(raw) if b > 0x7F]
        print(f"\n=== {rel_path} ===")
        print(f"  File size: {len(raw)} bytes")
        print(f"  Non-ASCII bytes: {len(bad_positions)}")
        
        for i in bad_positions[:15]:
            b = raw[i]
            ctx_start = max(0, i - 25)
            ctx_end = min(len(raw), i + 25)
            ctx = raw[ctx_start:ctx_end]
            try:
                ctx_str = ctx.decode('cp1252', errors='replace')
            except:
                ctx_str = repr(ctx)
            print(f"  pos={i} byte=0x{b:02X}: ...{ctx_str.strip()!r}...")
    except Exception as e:
        print(f"\n=== {rel_path} === ERROR: {e}")
