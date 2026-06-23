import os
import re

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
html_files = []

for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith(".html") and ".gemini" not in root:
            html_files.append(os.path.join(root, f))
if os.path.exists(os.path.join(search_dir, "style.css")):
    html_files.append(os.path.join(search_dir, "style.css"))

print(f"Searching CSS rules in {len(html_files)} files...")

for path in html_files:
    rel_path = os.path.relpath(path, search_dir)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # search for CSS rules like .note, .warning, .mistake, .recap, .callout, etc.
    # or look for classes like class="...note...", class="...warning...", etc.
    matches = re.findall(r"\.[a-zA-Z0-9_-]*(?:note|warning|mistake|callout|recap|tip)[a-zA-Z0-9_-]*", content, re.IGNORECASE)
    if matches:
        print(f"File: {rel_path} has CSS/class matches: {set(matches)}")
