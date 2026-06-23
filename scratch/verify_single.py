import os, re

import sys
path = sys.argv[1] if len(sys.argv) > 1 else r'c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html'
with open(path, 'rb') as f:
    raw = f.read()

utf8 = True
try:
    text = raw.decode('utf-8')
except:
    utf8 = False
    text = raw.decode('cp1252', errors='replace')

issues = []
if not utf8:
    issues.append('NOT UTF-8')

for bad_byte in [0x97, 0x96, 0x9B]:
    if raw.count(bytes([bad_byte])):
        issues.append(f'Raw 0x{bad_byte:02X} byte')

if '\ufffd' in text:
    issues.append('Replacement char U+FFFD')

if not re.search(r'<meta\s+charset\s*=\s*["\']?UTF-8', text, re.IGNORECASE):
    issues.append('Missing charset=UTF-8')

if 'announce-bar' in text:
    stars = re.findall(r'<span[^>]*announce-star[^>]*>([^<]*)</span>', text)
    if stars and any(s.strip() == '?' for s in stars):
        issues.append('Broken stars')
    elif not stars:
        issues.append('No stars')
else:
    issues.append('No announce bar')

if 'Get affiliate link' in text:
    if '&rarr;' not in text and '→' not in text:
        issues.append('Missing arrow')

if 'close-btn' in text and '<button' in text:
    close_btns = re.findall(r'<button[^>]*close-btn[^>]*>([^<]*)</button>', text)
    if close_btns and any('?' in b for b in close_btns):
        issues.append('Broken close btn')

logo_matches = re.findall(r'<img[^>]*class="logo-img"[^>]*>', text)
for lm in logo_matches[:2]:
    src = re.search(r'src="([^"]*)"', lm)
    if src:
        logo_src = src.group(1)
        if not logo_src.endswith('logo.svg'):
            issues.append(f'Wrong logo src: {logo_src}')
        else:
            print(f"Logo src matches: {logo_src}")

if 'mcp-promotion-playbook.html' in text:
    issues.append('Old MCP link in text')

if 'article-section' in text and 'scroll-margin-top' not in text:
    issues.append('Missing scroll-margin-top')

print('=' * 50)
print(f'AUDIT RESULT FOR {os.path.basename(path)}:')
if issues:
    print("FAILED!")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("ALL TESTS PASSED! NO ISSUES FOUND.")
print('=' * 50)
