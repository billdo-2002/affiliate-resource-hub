import os, re, sys

folder = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\restored_pages"
for filename in os.listdir(folder):
    if filename.endswith(".html"):
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8-sig", errors="ignore") as f:
            content = f.read()
        print("="*60)
        out_str = f"FILE: {filename} (length={len(content)})"
        print(out_str.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        print("="*60)
        lines = content.splitlines()
        for i in range(min(15, len(lines))):
            line_str = f"Line {i+1}: {lines[i]}"
            print(line_str.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
        print("Has html tag:", "html" in content.lower())
        print("Has json log:", '{"step_index":' in content)
