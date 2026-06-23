import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('resources/mcp/short-form-video-guidelines.html', 'r', encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')
print('Short-form video - common-mistake lines:')
for i,l in enumerate(lines,1):
    if 'common-mistake' in l:
        print('  L%d: %s' % (i, l.rstrip()[:100]))
print()
print('short-form has hook-visual-panel CSS:', '.hook-visual-panel' in text)
print('short-form has common-mistake CSS:', '.common-mistake' in text)
