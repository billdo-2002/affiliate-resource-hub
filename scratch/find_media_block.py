import os
from bs4 import BeautifulSoup

path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\tiktok-youtube-shorts.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')
style = soup.find('style')
if style:
    lines = style.string.splitlines()
    for i, line in enumerate(lines):
        if '@media (max-width: 1023px)' in line:
            start = max(0, i - 2)
            end = min(len(lines), i + 20)
            print(f"Match at line {i+1}:")
            print("\n".join(f"{start + idx + 1}: {lines[start+idx]}" for idx in range(end - start)))
            print("-" * 35)
