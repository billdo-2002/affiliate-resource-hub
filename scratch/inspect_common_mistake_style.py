import os
from bs4 import BeautifulSoup

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
path = os.path.join(search_dir, r"guides\tiktok-youtube-shorts.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')
style = soup.find('style')
if style:
    style_text = style.string or ""
    lines = style_text.splitlines()
    for i, line in enumerate(lines):
        if 'common-mistake' in line:
            start = max(0, i - 2)
            end = min(len(lines), i + 12)
            print("\n".join(f"{start + idx + 1}: {lines[start+idx]}" for idx in range(end - start)))
            print("-" * 30)
