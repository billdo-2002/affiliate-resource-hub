import os, re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
gg_path = os.path.join(BASE, "guides", "general-guide.html")

with open(gg_path, "r", encoding="utf-8") as f:
    html = f.read()

style_match = re.search(r"<style>(.*?)</style>", html, re.DOTALL)
if style_match:
    style_content = style_match.group(1)
    # Search for blocks
    blocks = re.findall(r'(\.[a-zA-Z0-9_-]+\s*\{[^\}]*\})', style_content)
    for b in blocks:
        if any(cls in b for cls in [".guide-body", ".guide-content", ".guide-sidebar"]):
            print("="*40)
            print(b.strip())
else:
    print("No style block found.")
