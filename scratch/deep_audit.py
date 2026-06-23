import os, re

base = r'c:\Users\khoadnd\Desktop\onboarding hub'

# Read index.html as raw bytes and analyze ALL non-ASCII sequences
path = os.path.join(base, 'index.html')
with open(path, 'rb') as f:
    raw = f.read()

print(f"File: index.html ({len(raw)} bytes)")
print(f"\nAll non-ASCII byte contexts:")

i = 0
while i < len(raw):
    b = raw[i]
    if b > 0x7F:
        ctx_start = max(0, i - 40)
        ctx_end = min(len(raw), i + 40)
        ctx = raw[ctx_start:ctx_end]
        # Try to show as latin-1 for context
        ctx_str = ctx.decode('latin-1')
        print(f"\n  pos={i} byte=0x{b:02X}:")
        print(f"    Context: {repr(ctx_str)}")
    i += 1
