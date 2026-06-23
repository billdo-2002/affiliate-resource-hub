import os, re

base = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Read index.html and find the HTML body structure (announce bar + header + mega menu)
path = os.path.join(base, 'index.html')
with open(path, 'rb') as f:
    raw = f.read()
text = raw.decode('cp1252', errors='replace')
lines = text.split('\n')

print(f"Total lines: {len(lines)}")

# Find where body starts
for i, line in enumerate(lines, 1):
    if '</style>' in line or '<body' in line or 'id="announce' in line:
        print(f"Key marker at {i}: {line.strip()[:80]}")

# Find announce bar section
for i, line in enumerate(lines, 1):
    if 'id="announce' in line:
        print(f"\n=== ANNOUNCE BAR starting at line {i} ===")
        for j in range(i-1, min(i+20, len(lines))):
            print(f"{j+1:5d}: {lines[j].rstrip()}")
        break

# Find header/nav HTML
for i, line in enumerate(lines, 1):
    if 'id="header"' in line:
        print(f"\n=== HEADER HTML starting at line {i} ===")
        for j in range(i-1, min(i+120, len(lines))):
            print(f"{j+1:5d}: {lines[j].rstrip()}")
        break
