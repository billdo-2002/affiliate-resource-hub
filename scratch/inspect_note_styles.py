import os
import re
from bs4 import BeautifulSoup

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
html_files = []

for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith(".html") and ".gemini" not in root:
            html_files.append(os.path.join(root, f))

for path in html_files:
    rel_path = os.path.relpath(path, search_dir)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    style = soup.find('style')
    if style:
        style_text = style.string or ""
        # Find lines matching article-note or common-mistake
        matching_rules = []
        lines = style_text.splitlines()
        for i, line in enumerate(lines):
            if any(term in line for term in ['article-note', 'common-mistake']):
                # Capture a few lines around it
                start = max(0, i - 1)
                end = min(len(lines), i + 6)
                snippet = "\n".join(f"{start + idx + 1}: {lines[start+idx]}" for idx in range(end - start))
                matching_rules.append(snippet)
        if matching_rules:
            print(f"\n==================================================")
            print(f"FILE: {rel_path} has CSS rules:")
            print(f"==================================================")
            for r in matching_rules[:5]:
                print(r)
                print("-" * 20)
