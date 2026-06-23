with open('mcp-promotion.html', 'r', encoding='utf-8') as f:
    html = f.read()
    start = html.find('key-value')
    if start != -1:
        print(html[max(0, start-300):start+3500])
    else:
        print("Not found")
