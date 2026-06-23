import os
import re

workspace_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
source_file = os.path.join(workspace_dir, "mcp-promotion.html")

with open(source_file, "r", encoding="utf-8") as f:
    source_html = f.read()

# Extract header
header_match = re.search(r'<header id="header">.*?</header>', source_html, re.DOTALL)
if not header_match:
    print("Failed to find header in source")
    exit(1)
header_block = header_match.group(0)

# Extract MEGA MENU CSS block
mega_css_match = re.search(r'/\*\s*=========================================\s*MEGA MENU STYLES\s*=========================================\s*\*/(.*?)/\*\s*=========================================\s*HEADER NAV UNDERLINE ANIMATION', source_html, re.DOTALL)
if not mega_css_match:
    print("Failed to find mega menu CSS in source")
    exit(1)
mega_css_block = mega_css_match.group(0)

# Extract new mobile dropdown css
mobile_css_match = re.search(r'/\*\s*Mobile Dropdown styles.*?\n\}', source_html, re.DOTALL)
if not mobile_css_match:
    print("Failed to find mobile dropdown CSS")
    exit(1)
mobile_css_block = mobile_css_match.group(0)

# Extract media queries at bottom
media_queries_match = re.search(r'@media \(max-width: 1023px\).*?@media \(min-width: 1024px\) \{.*?\n\}\n?', source_html, re.DOTALL)
if not media_queries_match:
    print("Failed to find media queries")
    exit(1)
media_queries_block = media_queries_match.group(0)

# Extract JS
js_match = re.search(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var hamburgerBtn = document\.getElementById\(\'hamburgerBtn\'\).*?</script>', source_html, re.DOTALL)
if not js_match:
    print("Failed to find JS in source")
    exit(1)
js_block = js_match.group(0)

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
                # replace href="url"
                def replace_href(m):
                    url = m.group(1)
                    if url.startswith(('http', '#', '/', 'data:', 'mailto:')):
                        if url.startswith('#') and url != '#':
                            # Anchor links like #dashboard-setup should point to index.html from nested files
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
            new_content = re.sub(r'<header id="header">.*?</header>', new_header.replace('\\', '\\\\'), new_content, flags=re.DOTALL)
            
            # 2. Replace MEGA MENU CSS
            new_mega_css = mega_css_block
            new_content = re.sub(
                r'/\*\s*=========================================\s*MEGA MENU STYLES\s*=========================================\s*\*/(.*?)/\*\s*=========================================\s*HEADER NAV UNDERLINE ANIMATION',
                new_mega_css.replace('\\', '\\\\'),
                new_content,
                flags=re.DOTALL
            )
            
            # 3. Clean up any existing media queries at bottom and mobile dropdown CSS
            new_content = re.sub(r'/\*\s*Mobile Dropdown styles.*?\n\}', '', new_content, flags=re.DOTALL)
            new_content = re.sub(r'@media \(max-width: 1023px\).*?@media \(min-width: 1024px\) \{.*?\n\}\n?', '', new_content, flags=re.DOTALL)
            
            # 4. Insert new media queries & mobile css before </style>
            if '</style>' in new_content:
                css_to_insert = '\n' + mobile_css_block + '\n' + media_queries_block + '\n'
                new_content = new_content.replace('</style>', css_to_insert + '</style>')
            
            # 5. Insert JS before </body>
            # First remove existing JS if present
            new_content = re.sub(r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*var hamburgerBtn = document\.getElementById\(\'hamburgerBtn\'\).*?</script>', '', new_content, flags=re.DOTALL)
            if '</body>' in new_content:
                new_content = new_content.replace('</body>', js_block + '\n</body>')
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                updated_count += 1
                print(f"Updated: {file_path}")

print(f"Done. Updated {updated_count} files.")
