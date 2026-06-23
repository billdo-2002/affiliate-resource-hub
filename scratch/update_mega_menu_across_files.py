import os
import re

workspace_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
index_path = os.path.join(workspace_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Extract CSS
css_match = re.search(r'(\.mega-menu\s*\{.*?)\/\*\s*Featured MCP Card styling\s*\*\/', index_content, re.DOTALL)
if not css_match:
    print("Could not find CSS block in index.html")
    exit(1)
css_block = css_match.group(1)

# Extract HTML
html_match = re.search(r'(<div class="mega-menu">.*?)(?=\s*</div>\s*</div>\s*</nav>)', index_content, re.DOTALL)
if not html_match:
    print("Could not find HTML block in index.html")
    exit(1)
html_block = html_match.group(1)

# Process all HTML files
updated_count = 0
for root, _, files in os.walk(workspace_dir):
    for file in files:
        if file.endswith(".html") and file != "index.html":
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = content
            
            # Replace CSS
            new_content = re.sub(
                r'\.mega-menu\s*\{.*?\/\*\s*Featured MCP Card styling\s*\*\/',
                css_block.replace('\\', '\\\\') + "/* Featured MCP Card styling */",
                new_content,
                flags=re.DOTALL
            )
            
            # Replace HTML
            new_content = re.sub(
                r'<div class="mega-menu">.*?(?=\s*</div>\s*</div>\s*</nav>)',
                html_block.replace('\\', '\\\\'),
                new_content,
                flags=re.DOTALL
            )
            
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                updated_count += 1
                print(f"Updated: {file_path}")

print(f"Successfully updated {updated_count} files.")
