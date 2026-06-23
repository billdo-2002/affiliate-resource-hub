with open('mcp-promotion.html', 'r', encoding='utf-8') as f:
    html = f.read()
    
    start = html.find('<div style="position: relative; z-index: 2; max-width: 100%; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">')
    
    # find the end of this div
    count = 0
    end = -1
    for i in range(start, len(html)):
        if html[i:i+4] == '<div':
            count += 1
        elif html[i:i+6] == '</div>':
            count -= 1
            if count == 0:
                end = i + 6
                break
                
    print('Start:', start)
    print('End:', end)
    if start != -1 and end != -1:
        print('Length:', end - start)
