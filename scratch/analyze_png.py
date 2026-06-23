from PIL import Image
import os

img_path = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\hook_1_revenue_profit.png"
img = Image.open(img_path).convert("RGBA")
width, height = img.size
print(f"Image size: {width}x{height}")

# Let's inspect some rows/columns to see where the color changes from the outer background
# Let's check the middle row (height // 2)
middle_y = height // 2
colors_in_row = [img.getpixel((x, middle_y)) for x in range(width)]

# Find transition points where color is not the outer color.
# Let's assume the far left pixel (0, middle_y) is the outer background color.
bg_color = img.getpixel((0, middle_y))
print(f"Background color at (0, {middle_y}): {bg_color}")

transitions = []
for x in range(1, width):
    prev_color = colors_in_row[x-1]
    curr_color = colors_in_row[x]
    # Check if there is a difference
    if abs(curr_color[0] - prev_color[0]) > 5 or abs(curr_color[1] - prev_color[1]) > 5 or abs(curr_color[2] - prev_color[2]) > 5 or abs(curr_color[3] - prev_color[3]) > 5:
        transitions.append((x, curr_color))

print(f"Transitions in middle row: {len(transitions)}")
if len(transitions) > 0:
    print("First 10 transitions:")
    for t in transitions[:10]:
        print(t)
    print("Last 10 transitions:")
    for t in transitions[-10:]:
        print(t)
