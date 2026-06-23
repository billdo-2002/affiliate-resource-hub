import os

folder = "scratch"
for filename in sorted(os.listdir(folder)):
    if filename.startswith("extracted_b2844f29") and filename.endswith(".txt"):
        filepath = os.path.join(folder, filename)
        size = os.path.getsize(filepath)
        print("="*60)
        print(f"FILE: {filename} (size={size})")
        print("="*60)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # Print the first 500 chars and last 500 chars to avoid overwhelming the log
        if len(content) > 1000:
            print(content[:500])
            print("\n... [TRUNCATED] ...\n")
            print(content[-500:])
        else:
            print(content)
