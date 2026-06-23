from PIL import Image

img_path = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\hook_1_revenue_profit.png"
img = Image.open(img_path).convert("RGBA")
width, height = img.size

# Let's define background pixels. Let's say a pixel is background if it is very close to white:
# e.g., R > 240, G > 240, B > 240. Or R > 240, G > 245, B > 250 (light blue/white).
# Let's count non-background pixels and find their min/max x and y.

min_x, max_x = width, 0
min_y, max_y = height, 0

bg_count = 0
for y in range(height):
    for x in range(width):
        r, g, b, a = img.getpixel((x, y))
        # Check if it's white or very light gray/blue
        is_bg = (r >= 240 and g >= 240 and b >= 240) or (r >= 235 and g >= 240 and b >= 245)
        if not is_bg:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y
        else:
            bg_count += 1

print(f"BBox of non-bg: X: {min_x} to {max_x}, Y: {min_y} to {max_y}")
print(f"BBox dimensions: {max_x - min_x} x {max_y - min_y}")
print(f"Background pixels: {bg_count} / {width * height} ({bg_count / (width * height) * 100:.2f}%)")
