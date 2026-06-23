import os
import re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"

# Check in style.css
style_css_path = os.path.join(BASE, "style.css")
if os.path.exists(style_css_path):
    with open(style_css_path, "r", encoding="utf-8", errors="ignore") as f:
        style_css = f.read()
    print("=== style.css Layout Rules ===")
    for line in style_css.splitlines():
        if ".guide-body" in line or ".guide-content" in line or ".guide-sidebar" in line or ".sidebar-toc" in line:
            print("  ", line.strip())

# Check in general-guide.html
gg_path = os.path.join(BASE, "guides", "general-guide.html")
if os.path.exists(gg_path):
    with open(gg_path, "r", encoding="utf-8") as f:
        gg = f.read()
    print("\n=== general-guide.html Style Block Layout Rules ===")
    # Extract style block content
    style_match = re.search(r"<style>(.*?)</style>", gg, re.DOTALL)
    if style_match:
        style_content = style_match.group(1)
        for line in style_content.splitlines():
            if ".guide-body" in line or ".guide-content" in line or ".guide-sidebar" in line or ".sidebar-toc" in line:
                print("  ", line.strip())
    else:
        print("  Style block not found in general-guide.html")
