with open('mcp-promotion.html', 'r', encoding='utf-8') as f:
    html = f.read()
    start = html.find('id="section-value"')
    print(html[max(0, start-100):start+3500])
