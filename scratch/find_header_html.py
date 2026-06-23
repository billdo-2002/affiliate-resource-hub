import os, re

base = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Read index.html and find HTML structure around announce bar and header start
path = os.path.join(base, 'index.html')
with open(path, 'rb') as f:
    raw = f.read()
text = raw.decode('cp1252', errors='replace')
lines = text.split('\n')

# Find announce bar
for i, line in enumerate(lines, 1):
    if 'announce' in line.lower() and '<div' in line.lower():
        print(f"\n=== ANNOUNCE BAR HTML at line {i} ===")
        for j in range(i-1, min(i+25, len(lines))):
            print(f"{j+1:5d}: {lines[j].rstrip()}")
        break

# Find header opening
for i, line in enumerate(lines, 1):
    if '<header' in line.lower() or 'id="header"' in line.lower():
        print(f"\n=== HEADER HTML at line {i} ===")
        for j in range(i-1, min(i+30, len(lines))):
            print(f"{j+1:5d}: {lines[j].rstrip()}")
        break

# Find mobile menu / overlay  
for i, line in enumerate(lines, 1):
    if 'mobile-menu' in line.lower() or 'mobile-overlay' in line.lower():
        print(f"\n=== MOBILE MENU at line {i} ===")
        for j in range(i-1, min(i+40, len(lines))):
            print(f"{j+1:5d}: {lines[j].rstrip()}")
        break
