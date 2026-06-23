import base64
import re
import os

svg_files = [
    r"c:\Users\khoadnd\Desktop\onboarding hub\hook_1_revenue_profit.svg",
    r"c:\Users\khoadnd\Desktop\onboarding hub\hook_2_scaling_margin.svg",
    r"c:\Users\khoadnd\Desktop\onboarding hub\hook_3_net_profit_check.svg"
]

for svg_path in svg_files:
    if not os.path.exists(svg_path):
        print(f"File not found: {svg_path}")
        continue
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'href="data:image/png;base64,([^"]+)"', content)
    if not match:
        match = re.search(r'xlink:href="data:image/png;base64,([^"]+)"', content)
        
    if not match:
        print(f"No base64 image in {os.path.basename(svg_path)}")
        continue
        
    base64_data = match.group(1)
    img_data = base64.b64decode(base64_data)
    
    name = os.path.basename(svg_path).replace('.svg', '.png')
    out_path = os.path.join(r"c:\Users\khoadnd\Desktop\onboarding hub\scratch", name)
    with open(out_path, 'wb') as f_out:
        f_out.write(img_data)
    print(f"Extracted {name} to {out_path}")
