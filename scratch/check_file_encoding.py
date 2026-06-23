import os

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
files_to_check = [
    r"guides\general-guide.html",
    r"guides\tiktok-youtube-shorts.html",
    r"resources\mcp\reddit-ready-to-post.html",
    r"resources\mcp\x-twitter-ready-to-post.html"
]

for rel_path in files_to_check:
    full_path = os.path.join(search_dir, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            raw = f.read(100)
            print(f"File: {rel_path}, BOM/First bytes: {raw[:10]}")
            # Try decode UTF-8
            try:
                raw.decode('utf-8')
                print("  UTF-8: Yes")
            except UnicodeDecodeError:
                print("  UTF-8: No")
            
            # Try decode UTF-16
            try:
                raw.decode('utf-16')
                print("  UTF-16: Yes")
            except UnicodeDecodeError:
                print("  UTF-16: No")

