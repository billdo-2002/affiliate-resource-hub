with open('guides/general-guide.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find '<section class="guide-hero">' and print from there to 'related-section'
idx_hero = text.find('<section class="guide-hero">')
idx_related = text.find('<section class="related-section">')

print("=== HERO SECTION ===")
print(text[idx_hero:idx_hero+500])

idx_body = text.find('<div class="guide-body">')
idx_sidebar = text.find('<div class="guide-sidebar">')
print("\n=== BODY SECTION ===")
print(text[idx_body:idx_body+800])

print("\n=== SIDEBAR SECTION ===")
print(text[idx_sidebar:idx_sidebar+800])
