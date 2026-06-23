from PIL import Image
import collections

img_path = r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\hook_1_revenue_profit.png"
img = Image.open(img_path).convert("RGBA")
width, height = img.size

# Create a copy to modify
out_img = img.copy()
pixels = out_img.load()

# Let's do a flood fill starting from the four corners.
# We will define a function to check if a pixel is part of the background/outer frame.
def is_background_pixel(r, g, b, a):
    # White border
    if r >= 240 and g >= 240 and b >= 240:
        return True
    # Light blue background
    if r >= 220 and r <= 238 and g >= 235 and g <= 248 and b >= 248:
        return True
    # Soft shadow (semi-transparent or slightly dark/grayish blue)
    # Shadows usually have R, G, B values close to each other, but slightly darker than background.
    # For example, (210, 225, 240) etc.
    if r >= 190 and r <= 225 and g >= 200 and g <= 235 and b >= 220 and b <= 248:
        return True
    return False

# Flood fill queue
queue = collections.deque()
visited = set()

# Add corners and edges
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

cleared_count = 0
while queue:
    cx, cy = queue.popleft()
    r, g, b, a = pixels[cx, cy]
    
    if is_background_pixel(r, g, b, a):
        pixels[cx, cy] = (0, 0, 0, 0)  # Make transparent
        cleared_count += 1
        
        # Check 4-neighbors
        for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

print(f"Cleared {cleared_count} background/shadow pixels.")
out_img.save(r"c:\Users\khoadnd\Desktop\onboarding hub\scratch\hook_1_transparent_test.png")
print("Saved test output to scratch/hook_1_transparent_test.png")
