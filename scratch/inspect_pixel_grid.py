from PIL import Image

img_path = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\hook_1_revenue_profit.png"
img = Image.open(img_path).convert("RGBA")
width, height = img.size

# We will sample the image on a 60x40 grid and print characters:
# '.' for white/near-white
# 'b' for light blue
# '#' for other colors (cards, text, etc.)

grid_w, grid_h = 80, 40
for gy in range(grid_h):
    y = int(gy * (height - 1) / (grid_h - 1))
    row = ""
    for gx in range(grid_w):
        x = int(gx * (width - 1) / (grid_w - 1))
        r, g, b, a = img.getpixel((x, y))
        
        # Check if it is white/near-white
        if r >= 250 and g >= 250 and b >= 250:
            row += "."
        # Check if it is light blue
        elif r >= 225 and r <= 236 and g >= 238 and g <= 246 and b >= 250:
            row += "b"
        else:
            row += "#"
    print(row)
