import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<header')
end = html.find('</header>') + 9
urls = set(re.findall(r'href="([^"]+)"', html[start:end]))
print(urls)
