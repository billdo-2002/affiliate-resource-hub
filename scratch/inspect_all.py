from PIL import Image
import os

img_dir = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch"
files = [
    "hook_1_revenue_profit.png",
    "hook_2_scaling_margin.png",
    "hook_3_net_profit_check.png"
]

grid_w, grid_h = 40, 20

for file_name in files:
    img_path = os.path.join(img_dir, file_name)
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        continue
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    print(f"\n=== {file_name} ({width}x{height}) ===")
    
    for gy in range(grid_h):
        y = int(gy * (height - 1) / (grid_h - 1))
        row = ""
        for gx in range(grid_w):
            x = int(gx * (width - 1) / (grid_w - 1))
            r, g, b, a = img.getpixel((x, y))
            if r >= 250 and g >= 250 and b >= 250:
                row += "."
            elif r >= 225 and r <= 236 and g >= 238 and g <= 246 and b >= 250:
                row += "b"
            else:
                row += "#"
        print(row)
