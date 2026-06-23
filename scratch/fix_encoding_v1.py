import os, re

base = r'c:\Users\khoadnd\Desktop\onboarding hub'

# All HTML files with their path prefix for relative links
html_files = [
    ('index.html', ''),
    ('guides.html', ''),
    ('mcp-promotion.html', ''),
    ('guides/discord-blueprint.html', '../'),
    ('guides/general-guide.html', '../'),
    ('guides/tiktok-youtube-shorts.html', '../'),
    ('guides/angles/scale-safely-with-margins.html', '../../'),
    ('guides/angles/stop-losing-30-profit.html', '../../'),
    ('guides/angles/track-profit-like-a-pro.html', '../../'),
    ('resources/mcp/reddit-ready-to-post.html', '../../'),
    ('resources/mcp/short-form-video-guidelines.html', '../../'),
    ('resources/mcp/x-twitter-ready-to-post.html', '../../'),
]

print("Starting global repair...")

for rel_path, prefix in html_files:
    path = os.path.join(base, rel_path.replace('/', os.sep))
    
    with open(path, 'rb') as f:
        raw = f.read()
    
    # Decode as cp1252 (what the files actually are)
    text = raw.decode('cp1252', errors='replace')
    
    original = text
    
    # =========================================
    # 1. Fix encoding - replace cp1252 broken characters
    # =========================================
    
    # 0x97 = em-dash in cp1252, appears in CSS comments as separator (–)
    # These should be en-dash or em-dash. In CSS comments they're decorative –
    # But in content they should be proper chars.
    # Since 0x97 decoded as cp1252 becomes '\x97' but in the file it shows as "–"
    # Actually cp1252: 0x97 = U+2014 (em dash —)
    # 0xD7 = × (multiplication sign) -- used as close button ×
    # 0x9B = \x9b (CSI control) -- appears as separator › in some contexts
    
    # Fix the close button (0xD7 decoded from cp1252 = ×, should be ×)
    # In the file: close-btn shows "×" - this IS correct for a close button
    # The problem is it's being read as cp1252 × but written incorrectly
    
    # Actually let's check what's there now after cp1252 decode:
    # 0x97 -> \x97 (in cp1252 = U+2014 em dash —)
    # But Python cp1252 decode gives us the actual char
    
    # Let's look at what chars we have after decode
    # Find all non-ASCII chars
    bad_chars = set(c for c in text if ord(c) > 127)
    # print(f"{rel_path}: non-ASCII chars after cp1252 decode: {[hex(ord(c)) for c in bad_chars]}")
    
    # Now fix specific problematic patterns:
    
    # 1. CSS comment separators - 0x97 in cp1252 = em dash U+2014
    #    These appear in patterns like "HERO — Light sage editorial" 
    #    and "LOCAL FONTS — Plus Jakarta Sans"
    #    These are just decorative, replace with " - " or ":" 
    text = text.replace('\u2014', '-')  # em dash -> hyphen in CSS comments
    
    # 2. The close button character - 0xD7 in cp1252 = × (U+00D7 multiplication sign)  
    #    This is used as close button text - should be &times; or ×
    #    We'll replace it with the HTML entity in the button
    text = re.sub(r'(<button[^>]*close-btn[^>]*>)\xd7(</button>)', r'\1&times;\2', text, flags=re.IGNORECASE)
    text = re.sub(r'(<button[^>]*close-btn[^>]*>)\u00d7(</button>)', r'\1&times;\2', text, flags=re.IGNORECASE)
    
    # 3. The separator 0x9B in cp1252 - this is a CSI control char, appears in breadcrumbs
    #    as span.sep - should be › or /
    text = re.sub(r'(<span[^>]*sep[^>]*>)\x9b(</span>)', r'\1&rsaquo;\2', text, flags=re.IGNORECASE)
    text = re.sub(r'(<span[^>]*sep[^>]*>)\u009b(</span>)', r'\1&rsaquo;\2', text, flags=re.IGNORECASE)
    
    # 4. Fix announce bar star characters (0x3F = ? which is likely a broken emoji star)
    #    The "?" in announce-star should be ★ or a star emoji
    #    Looking at the code: <span class="announce-star">?</span>
    #    These "?" are already ASCII question marks after cp1252 decode
    #    They SHOULD be ★ based on the CSS class name
    text = re.sub(r'(<span class="announce-star">)\?(<\/span>)', r'\1&#9733;\2', text)
    
    # 5. Fix "Get affiliate link ?" - the ? should be → (right arrow)
    text = text.replace('Get affiliate link \u2019', 'Get affiliate link &rarr;')
    text = text.replace("Get affiliate link ?", "Get affiliate link &rarr;")
    # Also fix in CTA button
    text = text.replace('Get affiliate link\u2019', 'Get affiliate link &rarr;')
    
    # 6. Fix any remaining content broken chars:
    # Don't -> Don't
    text = text.replace('Don\u2019t', "Don't")
    text = text.replace('doesn\u2019t', "doesn't")
    text = text.replace('you\u2019re', "you're")
    text = text.replace('it\u2019s', "it's")
    # These are curly quotes from cp1252, fine to keep as-is or convert to straight
    # Actually these are valid Unicode, let's keep them
    
    # 7. Fix en-dashes in ranges (0x96 in cp1252 = U+2013 en dash)
    # These should display fine in UTF-8, keep them
    
    # 8. Fix the remaining ? in announce bar spans (the stars)
    # The "?" chars that appear in announce-star spans - these come from encoding issue
    # where the original star emoji or character was lost
    
    # Check what we changed
    if text != original:
        print(f"  Modified: {rel_path}")
    
    # Write as proper UTF-8
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Saved {rel_path} as UTF-8")

print("\nDone!")
