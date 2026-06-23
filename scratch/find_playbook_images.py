import os
import re

BASE = r"c:\Users\khoadnd\Desktop\onboarding hub"
md_path = os.path.join(BASE, "TrueProfit Affiliate Playbook (2).md")

with open(md_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines, 1):
    if "[image2]" in line or "[image3]" in line:
        print(f"Line {idx}: {line.strip()}")
