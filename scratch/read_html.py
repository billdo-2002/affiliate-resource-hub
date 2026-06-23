import os

base = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Read index.html
path = os.path.join(base, 'index.html')
with open(path, 'rb') as f:
    raw = f.read()
text = raw.decode('cp1252', errors='replace')
lines = text.split('\n')

# Print first 350 lines
print(f"=== index.html (first 350 lines) ===")
for i, line in enumerate(lines[:350], 1):
    print(f"{i:4d}: {line.rstrip()}")
