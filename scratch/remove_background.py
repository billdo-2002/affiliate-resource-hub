import base64
import re
import os
from PIL import Image
import io

def main():
    svg_path = r"c:\Users\khoadnd\Desktop\onboarding hub\13.svg"
    output_svg_path = r"c:\Users\khoadnd\Desktop\onboarding hub\13.svg"
    
    with open(svg_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find the base64 data
    match = re.search(r'href="data:image/png;base64,([^"]+)"', content)
    if not match:
        # Check alternate format xlink:href
        match = re.search(r'xlink:href="data:image/png;base64,([^"]+)"', content)
        
    if not match:
        print("Base64 data not found in SVG")
        return
        
    base64_data = match.group(1)
    img_data = base64.b64decode(base64_data)
    
    # Load image with PIL
    img = Image.open(io.BytesIO(img_data)).convert("RGBA")
    width, height = img.size
    print(f"Loaded image size: {width}x{height}")
    
    corners = [img.getpixel((0, 0)), img.getpixel((width-1, 0)), img.getpixel((0, height-1)), img.getpixel((width-1, height-1))]
    print("Corner pixels:", corners)
    
    bg_colors = set()
    for x in range(30):
        for y in range(30):
            bg_colors.add(img.getpixel((x, y)))
            
    print("Sample background colors:", list(bg_colors)[:10])
    
    from collections import Counter
    sample_pixels = []
    for x in range(100):
        for y in range(100):
            sample_pixels.append(img.getpixel((x, y)))
    counter = Counter(sample_pixels)
    most_common = counter.most_common(5)
    print("Most common colors in corner:", most_common)
    
    checker_colors = [color for color, count in most_common[:2]]
    print("Identified checker colors to remove:", checker_colors)
    
    # Check if corner pixels are already fully transparent (alpha = 0)
    # If they are already transparent, we don't need to remove them!
    if checker_colors[0][3] == 0:
        print("Image corner is already transparent! No checkered background removal needed.")
        return
        
    # Let's do the replacement
    pix = img.load()
    removed_count = 0
    for y in range(height):
        for x in range(width):
            r, g, b, a = pix[x, y]
            is_checker = False
            for cr, cg, cb, ca in checker_colors:
                if abs(r - cr) < 3 and abs(g - cg) < 3 and abs(b - cb) < 3:
                    is_checker = True
                    break
            if is_checker:
                pix[x, y] = (0, 0, 0, 0)
                removed_count += 1
                
    print(f"Removed {removed_count} background pixels.")
    
    # Save the modified image back to base64
    out_buf = io.BytesIO()
    img.save(out_buf, format="PNG")
    new_base64 = base64.b64encode(out_buf.getvalue()).decode('utf-8')
    
    # Replace in SVG content
    new_content = content.replace(base64_data, new_base64)
    
    with open(output_svg_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("SVG file updated successfully!")

if __name__ == "__main__":
    main()
