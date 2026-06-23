import difflib

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    current = f.readlines()

with open('index.html.bak', 'r', encoding='utf-8', errors='ignore') as f:
    backup = f.readlines()

diff = list(difflib.unified_diff(backup, current, fromfile='index.html.bak', tofile='index.html', n=3))

for line in diff[:100]: # Print first 100 lines of diff
    print(line, end='')
