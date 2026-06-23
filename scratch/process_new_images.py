from PIL import Image
import collections
import base64
import os
import re

svg_files = [
    ("hook_1_revenue_profit (1).svg", "hook_1_revenue_profit (1).png", "hook_1"),
    ("hook_2_ad_spend_margin.svg", "hook_2_ad_spend_margin.png", "hook_2"),
    ("hook_3_net_profit.svg", "hook_3_net_profit.png", "hook_3")
]

workspace_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
scratch_dir = os.path.join(workspace_dir, "scratch")

# Define color matcher for background/shadow per hook
def get_bg_matcher(hook_type):
    if hook_type == "hook_1":
        def is_bg(r, g, b, a):
            if r >= 240 and g >= 240 and b >= 240:
                return True
            if r >= 220 and r <= 238 and g >= 235 and g <= 248 and b >= 248:
                return True
            if r >= 190 and r <= 225 and g >= 200 and g <= 235 and b >= 220 and b <= 248:
                return True
            return False
        return is_bg
    elif hook_type == "hook_2":
        def is_bg(r, g, b, a):
            if r >= 240 and g >= 240 and b >= 240:
                return True
            if r >= 245 and g >= 225 and g <= 242 and b >= 215 and b <= 237:
                return True
            if r >= 210 and r <= 250 and g >= 180 and g <= 230 and b >= 170 and b <= 220:
                return True
            return False
        return is_bg
    elif hook_type == "hook_3":
        def is_bg(r, g, b, a):
            if r >= 240 and g >= 240 and b >= 240:
                return True
            if r >= 225 and r <= 238 and g >= 240 and g <= 248 and b >= 235 and b <= 246:
                return True
            if r >= 180 and r <= 230 and g >= 200 and g <= 242 and b >= 190 and b <= 238:
                return True
            return False
        return is_bg

# Step 1: Extract PNGs from new SVGs
for svg_name, png_name, hook_type in svg_files:
    svg_path = os.path.join(workspace_dir, svg_name)
    if not os.path.exists(svg_path):
        print(f"SVG not found: {svg_path}")
        continue
        
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    match = re.search(r'href="data:image/png;base64,([^"]+)"', content)
    if not match:
        match = re.search(r'xlink:href="data:image/png;base64,([^"]+)"', content)
        
    if not match:
        print(f"No base64 image in {svg_name}")
        continue
        
    base64_data = match.group(1)
    img_data = base64.b64decode(base64_data)
    
    png_path = os.path.join(scratch_dir, png_name)
    with open(png_path, 'wb') as f_out:
        f_out.write(img_data)
    print(f"Extracted {png_name}")

# Step 2: Process PNGs
for svg_name, png_name, hook_type in svg_files:
    png_path = os.path.join(scratch_dir, png_name)
    if not os.path.exists(png_path):
        continue
        
    img = Image.open(png_path).convert("RGBA")
    width, height = img.size
    
    out_img = img.copy()
    pixels = out_img.load()
    
    is_bg = get_bg_matcher(hook_type)
    
    queue = collections.deque()
    visited = set()
    
    for x in range(width):
        queue.append((x, 0))
        queue.append((x, height - 1))
        visited.add((x, 0))
        visited.add((x, height - 1))
        
    for y in range(height):
        queue.append((0, y))
        queue.append((width - 1, y))
        visited.add((0, y))
        visited.add((width - 1, y))
        
    cleared = 0
    while queue:
        cx, cy = queue.popleft()
        r, g, b, a = pixels[cx, cy]
        if is_bg(r, g, b, a):
            pixels[cx, cy] = (0, 0, 0, 0)
            cleared += 1
            for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                if 0 <= nx < width and 0 <= ny < height:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        
    print(f"[{svg_name}] Cleared {cleared} background pixels.")
    
    # BBox
    min_x, max_x = width, 0
    min_y, max_y = height, 0
    has_content = False
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a > 0:
                has_content = True
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    if not has_content:
        print(f"[{svg_name}] Error: No content remains.")
        continue
        
    crop_box = (min_x, min_y, max_x + 1, max_y + 1)
    cropped_img = out_img.crop(crop_box)
    new_w, new_h = cropped_img.size
    print(f"[{svg_name}] Cropped to {new_w}x{new_h}")
    
    temp_out = os.path.join(scratch_dir, f"{hook_type}_new_processed.png")
    cropped_img.save(temp_out, format="PNG")
    
    with open(temp_out, 'rb') as img_f:
        encoded_string = base64.b64encode(img_f.read()).decode('utf-8')
        
    svg_path = os.path.join(workspace_dir, svg_name)
    with open(svg_path, 'r', encoding='utf-8') as f_svg:
        svg_content = f_svg.read()
        
    svg_content = re.sub(r'width="\d+"', f'width="{new_w}"', svg_content)
    svg_content = re.sub(r'height="\d+"', f'height="{new_h}"', svg_content)
    svg_content = re.sub(r'viewBox="0 0 \d+ \d+"', f'viewBox="0 0 {new_w} {new_h}"', svg_content)
    
    svg_content = re.sub(r'<image([^>]+)width="\d+"', f'<image\\1width="{new_w}"', svg_content)
    svg_content = re.sub(r'<image([^>]+)height="\d+"', f'<image\\1height="{new_h}"', svg_content)
    
    href_match = re.search(r'href="data:image/png;base64,([^"]+)"', svg_content)
    if href_match:
        old_b64 = href_match.group(1)
        svg_content = svg_content.replace(old_b64, encoded_string)
    else:
        xlink_match = re.search(r'xlink:href="data:image/png;base64,([^"]+)"', svg_content)
        if xlink_match:
            old_b64 = xlink_match.group(1)
            svg_content = svg_content.replace(old_b64, encoded_string)
            
    with open(svg_path, 'w', encoding='utf-8') as f_svg_out:
        f_svg_out.write(svg_content)
        
    print(f"[{svg_name}] Successfully processed and updated SVG in workspace!")
