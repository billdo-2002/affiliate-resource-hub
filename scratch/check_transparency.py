from PIL import Image

img_path = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\hook_1_transparent_test.png"
img = Image.open(img_path).convert("RGBA")
width, height = img.size

grid_w, grid_h = 80, 40
for gy in range(grid_h):
    y = int(gy * (height - 1) / (grid_h - 1))
    row = ""
    for gx in range(grid_w):
        x = int(gx * (width - 1) / (grid_w - 1))
        r, g, b, a = img.getpixel((x, y))
        
        # Check if transparent
        if a == 0:
            row += "."
        # Check if light blue
        elif r >= 225 and r <= 236 and g >= 238 and g <= 246 and b >= 250:
            row += "b"
        else:
            row += "#"
    print(row)
