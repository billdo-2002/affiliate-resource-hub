with open('guides/general-guide.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search case-insensitive for '<div class="guide-body' or '<section'
import re
match = re.search(r'<div[^>]*class=["\'][^"\']*guide-body[^"\']*["\'][^>]*>', text)
if match:
    start = match.start()
    print("Found match:", match.group(0), "at", start)
    print(text[start:start+1000])
else:
    print("Not found")
