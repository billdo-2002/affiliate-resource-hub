import os, sys

folder = "scratch"
files = [
    "extracted_b2844f29_track-profit-like-a-pro.html_852.txt",
    "extracted_b2844f29_scale-safely-with-margins.html_860.txt",
    "extracted_b2844f29_stop-losing-30-profit.html_947.txt",
]

for filename in files:
    filepath = os.path.join(folder, filename)
    if os.path.exists(filepath):
        print("="*80)
        print(f"FILE: {filename}")
        print("="*80)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # Clean/replace curly quotes to regular ascii or ignore
        content = content.replace("", "'").replace("–", "-")
        out_str = content.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        print(out_str)
