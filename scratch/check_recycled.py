import os, re, sys

folder = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\recovered_htmls"
for filename in os.listdir(folder):
    if filename.endswith(".html"):
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read(2000)
            title = re.search(r"<title>(.*?)</title>", content)
            t_str = title.group(1) if title else 'No title'
            out_str = f"File: {filename}, Size: {os.path.getsize(filepath)}, Title: {t_str}"
            print(out_str.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
