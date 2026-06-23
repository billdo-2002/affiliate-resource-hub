import os

folder = "scratch"
files = [
    # Track profit like a pro
    "extracted_b2844f29_track-profit-like-a-pro.html_852.txt",
    "extracted_b2844f29_track-profit-like-a-pro.html_1043.txt",
    "extracted_b2844f29_track-profit-like-a-pro.html_1047.txt",
    # Scale safely with margins
    "extracted_b2844f29_scale-safely-with-margins.html_805.txt",
    "extracted_b2844f29_scale-safely-with-margins.html_860.txt",
    "extracted_b2844f29_scale-safely-with-margins.html_880.txt",
    # Stop losing 30% profit
    "extracted_b2844f29_stop-losing-30-profit.html_947.txt",
    "extracted_b2844f29_stop-losing-30-profit.html_955.txt",
    "extracted_b2844f29_stop-losing-30-profit.html_983.txt",
]

for filename in files:
    filepath = os.path.join(folder, filename)
    if os.path.exists(filepath):
        print("="*60)
        print(f"FILE: {filename}")
        print("="*60)
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
