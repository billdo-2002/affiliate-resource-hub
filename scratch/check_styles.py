import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html') and not f.endswith('.bak') and 'scratch' not in root:
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except Exception as e:
                continue
            
            # Count occurrences of </style>
            count_close = content.lower().count('</style>')
            count_open = content.lower().count('<style>')
            
            # Check if there is style text exposed
            exposed = False
            if 'bile for performance' in content:
                exposed = True
                
            if count_close > 1 or count_open > 1 or exposed:
                print(f'{path}: <style>={count_open}, </style>={count_close}, exposed={exposed}')
                # Let's find where </style> occurs
                lines = content.splitlines()
                for idx, line in enumerate(lines):
                    if '</style>' in line.lower():
                        print(f'  Line {idx+1}: {line}')
                    if 'bile for performance' in line:
                        print(f'  Line {idx+1}: {line}')
