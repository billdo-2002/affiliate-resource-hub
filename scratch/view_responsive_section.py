import os

gg_path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(gg_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(1234, min(1290, len(lines))):
    print(f"{i+1:4d}: {lines[i]}", end="")
