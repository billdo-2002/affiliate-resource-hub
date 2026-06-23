import os

workspace_dir = r'c:\Users\khoadnd\Desktop\onboarding hub'
source_file = os.path.join(workspace_dir, 'mcp-promotion.html')

with open(source_file, 'r', encoding='utf-8') as f:
    html = f.read()

h_start = html.find('<header id="header"')
h_end = html.find('</header>') + 9

c_start = html.find('/* =========================================\n   MEGA MENU STYLES')
c_end = html.find('/* =========================================\n   HEADER NAV UNDERLINE ANIMATION')

m_start = html.find('@media (max-width: 1023px) {')
m_end = html.find('</style>')

js_start = html.find('<script>\n  document.addEventListener(\'DOMContentLoaded\'')
js_end = html.find('</script>', js_start) + 9

print(f"Header: {h_start != -1 and h_end > 8}")
print(f"Mega CSS: {c_start != -1 and c_end != -1}")
print(f"Media: {m_start != -1 and m_end != -1}")
print(f"JS: {js_start != -1 and js_end > 8}")
