import sys, re
sys.stdout.reconfigure(encoding='utf-8')
for fname in ['guides/tiktok-youtube-shorts.html', 'resources/mcp/short-form-video-guidelines.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    count = text.count('@media (max-width: 1023px)')
    count2 = text.count('content: "?"')
    count3 = text.count('.hamburger::before')
    unclosed = text.count('@media (max-width: 1024px)')
    print('%s:' % fname.split('/')[-1])
    print('  @media 1023px count: %d' % count)
    print('  broken content char: %d' % count2)
    print('  .hamburger::before count: %d' % count3)
    print('  @media 1024px blocks: %d' % unclosed)
    print()
