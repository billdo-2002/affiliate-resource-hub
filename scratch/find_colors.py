from PIL import Image
import collections

img_path = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\hook_1_revenue_profit.png"
img = Image.open(img_path).convert("RGBA")
width, height = img.size

# Let's count all unique colors and their frequency
counter = collections.Counter()
for y in range(height):
    for x in range(width):
        counter[img.getpixel((x, y))] += 1

print("Top 20 most common colors:")
for color, count in counter.most_common(20):
    print(f"Color: {color}, Count: {count} ({count / (width * height) * 100:.2f}%)")
