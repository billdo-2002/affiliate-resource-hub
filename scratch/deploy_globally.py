import os, re

workspace_dir = r'c:\Users\khoadnd\Desktop\onboarding hub'
source_file = os.path.join(workspace_dir, 'mcp-promotion.html')

with open(source_file, 'r', encoding='utf-8') as f:
    source_html = f.read()

# 1. Header
h_start = source_html.find('<header id="header"')
h_end = source_html.find('</header>') + 9
header_block = source_html[h_start:h_end]

# 2. Mega CSS
c_start = source_html.find('/* =========================================\n   MEGA MENU STYLES')
c_end = source_html.find('/* =========================================', c_start + 100)
mega_css_block = source_html[c_start:c_end]

# 3. Media Queries block (starts with @media (max-width: 1023px) and ends at </style>)
m_start = source_html.find('@media (max-width: 1023px) {')
m_end = source_html.rfind('</style>')
media_queries_block = source_html[m_start:m_end]

# 4. Mobile Dropdown CSS
md_start = source_html.find('/* Mobile Dropdown styles')
md_end = m_start
if md_start == -1 or md_end == -1:
    print("Mobile CSS not found")
mobile_css_block = source_html[md_start:md_end]

# 5. JS
js_start = source_html.find('<script>\n  document.addEventListener(\'DOMContentLoaded\'')
js_end = source_html.find('</script>', js_start) + 9
js_block = source_html[js_start:js_end]

updated_count = 0

for root, _, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith(".html") and file != "mcp-promotion.html":
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = content
            
            # Calculate depth
            rel_path = os.path.relpath(file_path, workspace_dir)
            depth = rel_path.count(os.sep)
            prefix = "../" * depth if depth > 0 else ""
            
            def fix_urls(block):
                if depth == 0:
                    return block
                def replace_href(m):
                    url = m.group(1)
                    if url.startswith(('http', '#', '/', 'data:', 'mailto:')):
                        if url.startswith('#') and url != '#':
                            return f'href="{prefix}index.html{url}"'
                        return m.group(0)
                    return f'href="{prefix}{url}"'
                
                block = re.sub(r'href="([^"]+)"', replace_href, block)
                
                def replace_src(m):
                    url = m.group(1)
                    if url.startswith(('http', '/', 'data:')):
                        return m.group(0)
                    return f'src="{prefix}{url}"'
                
                block = re.sub(r'src="([^"]+)"', replace_src, block)
                return block

            # 1. Replace header
            new_header = fix_urls(header_block)
            
            # Find target header bounds
            t_h_start = new_content.find('<header id="header"')
            if t_h_start == -1: t_h_start = new_content.find('<header')
            t_h_end = new_content.find('</header>') + 9
            if t_h_start != -1 and t_h_end > 8:
                new_content = new_content[:t_h_start] + new_header + new_content[t_h_end:]
            else:
                new_content = new_content.replace('<body>', '<body>\n' + new_header)

            # 2. Replace MEGA MENU CSS
            new_mega_css = mega_css_block
            t_c_start = new_content.find('/* =========================================\n   MEGA MENU STYLES')
            if t_c_start != -1:
                t_c_end = new_content.find('/* =========================================', t_c_start + 100)
                if t_c_end != -1:
                    new_content = new_content[:t_c_start] + new_mega_css + new_content[t_c_end:]
                else:
                    new_content = new_content[:t_c_start] + new_mega_css + '</style>'
            else:
                if '</style>' in new_content:
                    new_content = new_content.replace('</style>', '\n' + new_mega_css + '</style>')

            # 3. Clean up mobile dropdown css and @media blocks
            # Find start of Mobile Dropdown styles
            t_md_start = new_content.find('/* Mobile Dropdown styles')
            if t_md_start != -1:
                # remove to the end of style block
                new_content = new_content[:t_md_start] + '</style>' + new_content[new_content.find('</style>', t_md_start)+8:]
            else:
                # also clean up if there's any stray @media blocks for nav
                t_mq_start = new_content.find('@media (max-width: 1023px) {\n  /* Hide all nav links')
                if t_mq_start != -1:
                    new_content = new_content[:t_mq_start] + '</style>' + new_content[new_content.find('</style>', t_mq_start)+8:]

            # 4. Insert new mobile dropdown and media queries
            if '</style>' in new_content:
                css_to_insert = '\n' + mobile_css_block + media_queries_block
                new_content = new_content.replace('</style>', css_to_insert + '</style>')
            
            # 5. Replace JS
            new_content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var hamburgerBtn = document\.getElementById\(\'hamburgerBtn\'\).*?</script>', '', new_content, flags=re.DOTALL)
            if '</body>' in new_content:
                new_content = new_content.replace('</body>', js_block + '\n</body>')
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                updated_count += 1
                print(f"Updated: {file_path}")

print(f"Done. Updated {updated_count} files.")
