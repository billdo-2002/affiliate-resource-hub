import os

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
files = [
    r"guides\general-guide.html",
    r"guides\tiktok-youtube-shorts.html"
]

for rel in files:
    path = os.path.join(search_dir, rel)
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        
        idx = 0
        while True:
            idx = data.find(b'\x97', idx)
            if idx == -1:
                break
            
            # Show context (10 bytes before and after)
            start = max(0, idx - 15)
            end = min(len(data), idx + 15)
            chunk = data[start:end]
            print(f"File: {rel}, index: {idx}")
            print(f"  Bytes: {chunk}")
            # Try to decode context as latin-1 to see CP1252 characters
            print(f"  As Latin-1: {chunk.decode('latin-1')}")
            try:
                print(f"  As UTF-8 (errors='replace'): {chunk.decode('utf-8', errors='replace')}")
            except Exception as e:
                print(f"  As UTF-8 decode failed: {e}")
            idx += 1
