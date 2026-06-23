import os
import re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
guides_file = os.path.join(BASE, "guides.html")

with open(guides_file, "r", encoding="utf-8") as f:
    content = f.read()

headings = re.findall(r"<h[1-6][^>]*>(.*?)</h[1-6]>", content)
print("Headings in guides.html:", headings)
