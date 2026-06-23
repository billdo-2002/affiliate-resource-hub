from PIL import Image
import collections
import os

img_dir = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch"
files = [
    "hook_1_revenue_profit.png",
    "hook_2_scaling_margin.png",
    "hook_3_net_profit_check.png"
]

for file_name in files:
    img_path = os.path.join(img_dir, file_name)
    if not os.path.exists(img_path):
        continue
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    
    counter = collections.Counter()
    # Sample 10000 pixels at random or regular intervals to find the background color
    for y in range(0, height, 5):
        for x in range(0, width, 5):
            counter[img.getpixel((x, y))] += 1
            
    print(f"\n=== {file_name} Common Colors ===")
    for color, count in counter.most_common(10):
        print(f"Color: {color}, Count: {count}")
