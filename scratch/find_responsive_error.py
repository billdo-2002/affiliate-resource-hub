import os

gg_path = r"c:\Users\khoadnd\Desktop\onboarding hub\guides\general-guide.html"
with open(gg_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "@media (max-width: 1024px) {" in line:
        # Check if the next non-blank line starts another @media or if it has the closing brace
        print(f"Line {idx+1}: {line.strip()}")
        for offset in range(1, 10):
            print(f"  Line {idx+1+offset}: {lines[idx+offset].strip()}")
        print("-" * 50)
