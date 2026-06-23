import os, re
workspace_dir = r'c:\Users\khoadnd\Desktop\onboarding hub'
source_file = os.path.join(workspace_dir, 'mcp-promotion.html')
with open(source_file, 'r', encoding='utf-8') as f:
    source_html = f.read()

print('Header:', bool(re.search(r'<header id="header">.*?</header>', source_html, re.DOTALL)))
print('Mega CSS:', bool(re.search(r'/\*\s*=========================================\s*MEGA MENU STYLES\s*=========================================\s*\*/(.*?)/\*\s*=========================================\s*HEADER NAV UNDERLINE ANIMATION', source_html, re.DOTALL)))
print('Mobile CSS:', bool(re.search(r'/\*\s*Mobile Dropdown styles.*?\n\}', source_html, re.DOTALL)))
print('Media Queries:', bool(re.search(r'@media \(max-width: 1023px\).*?@media \(min-width: 1024px\) \{.*?\n\}\n?', source_html, re.DOTALL)))
print('JS:', bool(re.search(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var hamburgerBtn = document\.getElementById\(\'hamburgerBtn\'\).*?</script>', source_html, re.DOTALL)))
