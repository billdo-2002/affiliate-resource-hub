import sys, os
sys.stdout.reconfigure(encoding='utf-8')
base = r'c:\Users\khoadnd\Desktop\onboarding hub'
files = [
    'index.html','guides.html','mcp-promotion.html',
    'guides/discord-blueprint.html','guides/general-guide.html',
    'guides/tiktok-youtube-shorts.html',
    'guides/angles/scale-safely-with-margins.html',
    'guides/angles/stop-losing-30-profit.html',
    'guides/angles/track-profit-like-a-pro.html',
    'resources/mcp/reddit-ready-to-post.html',
    'resources/mcp/short-form-video-guidelines.html',
    'resources/mcp/x-twitter-ready-to-post.html',
]
print('%-45s  %5s  %5s' % ('File', '1023x', 'hmbg'))
print('-'*65)
for rel in files:
    path = os.path.join(base, rel.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    c1023 = text.count('@media (max-width: 1023px)')
    chmb  = text.count('.hamburger::before')
    status = 'NEEDS FIX' if c1023 > 1 else 'ok'
    print('%-45s  %5d  %5d  %s' % (rel.split('/')[-1], c1023, chmb, status))
