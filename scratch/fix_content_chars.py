"""
Fix remaining broken ? characters across all HTML files.
"""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

BASE = r'c:\Users\khoadnd\Desktop\onboarding hub'

HTML_FILES = [
    'index.html',
    'guides.html',
    'mcp-promotion.html',
    'guides/discord-blueprint.html',
    'guides/general-guide.html',
    'guides/tiktok-youtube-shorts.html',
    'guides/angles/scale-safely-with-margins.html',
    'guides/angles/stop-losing-30-profit.html',
    'guides/angles/track-profit-like-a-pro.html',
    'resources/mcp/reddit-ready-to-post.html',
    'resources/mcp/short-form-video-guidelines.html',
    'resources/mcp/x-twitter-ready-to-post.html',
]

def fix_content(text, rel_path):
    changes = []
    original = text

    # -------------------------------------------------------
    # 1. Fix btn-arrow span: <span class="btn-arrow">?</span>
    #    -> <span class="btn-arrow">&rarr;</span>
    # -------------------------------------------------------
    new = re.sub(
        r'(<span[^>]*class="btn-arrow"[^>]*>)\?(<\/span>)',
        r'\1&rarr;\2',
        text
    )
    if new != text:
        changes.append('Fixed btn-arrow ?')
        text = new

    # -------------------------------------------------------
    # 2. Fix trending-up arrows: "> +23%" -> "&#8593; +23%"
    #    These appear as "? +NN%" inside badge/pill spans
    #    The ? before a space and + is a broken ↑ arrow
    # -------------------------------------------------------
    new = re.sub(
        r'(?<=>)\? (\+\d+%)',
        r'&#8593; \1',
        text
    )
    if new != text:
        changes.append('Fixed trending-up arrows')
        text = new

    # -------------------------------------------------------
    # 3. index.html L2481: "on Shopify ? a potential" 
    #    Context: "Anyone selling on Shopify ? a potential TrueProfit user"
    #    The ? is an em dash — 
    # -------------------------------------------------------
    new = text.replace(
        'Anyone selling on Shopify ? a potential TrueProfit user.',
        'Anyone selling on Shopify &mdash; a potential TrueProfit user.'
    )
    if new != text:
        changes.append('Fixed Shopify — em dash')
        text = new

    # Fix the second broken ? in same paragraph: "and doing serious volume ? they"
    new = text.replace(
        'and doing serious volume\u003c/span\u003e ? they',
        'and doing serious volume</span> &mdash; they'
    )
    if new != text:
        changes.append('Fixed volume — em dash')
        text = new
    
    # Try with literal < in text
    new = text.replace(
        '</span> ? they',
        '</span> &mdash; they'
    )
    if new != text:
        changes.append('Fixed </span> — they')
        text = new

    # -------------------------------------------------------
    # 4. index.html L2874: "Month 1 ? Month 12" 
    #    -> "Month 1 &ndash; Month 12"
    # -------------------------------------------------------
    new = text.replace('Month 1 ? Month 12', 'Month 1 &ndash; Month 12')
    if new != text:
        changes.append('Fixed Month 1 – Month 12')
        text = new

    # -------------------------------------------------------
    # 5. general-guide.html L2134/2185: "??" at start of <p> in note boxes
    #    These are broken emoji (likely 📌 pin or 💡 bulb)
    #    Context: article-note divs with important reminders
    #    Replace with a clean icon: 📌 or just a simple ✓ checkmark
    # -------------------------------------------------------
    # Pattern: starts a <p> or beginning of paragraph content
    new = re.sub(r'<p>\?\? (Remember:)', r'<p>&#128204; \1', text)  # 📌
    if new != text:
        changes.append('Fixed ?? Remember emoji')
        text = new
    
    new = re.sub(r'<p>\?\? (These references)', r'<p>&#128204; \1', text)  # 📌
    if new != text:
        changes.append('Fixed ?? These references emoji')
        text = new

    # -------------------------------------------------------
    # 6. general-guide.html L2188: "Your next step? ? Check out"
    #    Second ? is broken emoji (likely 👉 or →)
    # -------------------------------------------------------
    new = text.replace(
        'Your next step? ? Check out each Angle page',
        'Your next step? &#128073; Check out each Angle page'  # 👉
    )
    if new != text:
        changes.append('Fixed next step ? emoji')
        text = new

    # -------------------------------------------------------
    # 7. tiktok-youtube-shorts.html: "??" at start of note paragraphs
    #    These are broken emoji (likely 💡 or ✅)
    # -------------------------------------------------------
    # Pattern: <p>?? text
    new = re.sub(r'<p>\?\? (You don\'t need)', r'<p>&#128161; \1', text)  # 💡
    if new != text:
        changes.append('Fixed ?? You dont need emoji')
        text = new
    
    new = re.sub(r'<p>\?\? (Universal Rule)', r'<p>&#128161; \1', text)  # 💡
    if new != text:
        changes.append('Fixed ?? Universal Rule emoji')
        text = new
    
    new = re.sub(r'<p>\?\? (Post consistently)', r'<p>&#128161; \1', text)  # 💡
    if new != text:
        changes.append('Fixed ?? Post consistently emoji')
        text = new

    # -------------------------------------------------------
    # 8. Generic fallback: any remaining "??" at start of <p> content
    #    Replace with 💡 light bulb
    # -------------------------------------------------------
    new = re.sub(r'(<p[^>]*>)\?\? ', r'\1&#128161; ', text)
    if new != text:
        changes.append('Fixed remaining ?? emoji patterns')
        text = new

    # -------------------------------------------------------
    # 9. Fix remaining "? " patterns that look like broken arrows
    #    in specific contexts (button arrows, step indicators)
    # -------------------------------------------------------
    # "See What's Inside <span class="btn-arrow">?</span>" already handled above
    
    return text, changes


print("=" * 60)
print("CONTENT CHAR FIX")
print("=" * 60)

for rel_path in HTML_FILES:
    path = os.path.join(BASE, rel_path.replace('/', os.sep))
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    fixed, changes = fix_content(text, rel_path)
    
    if changes:
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(fixed)
        print("\n[FIXED] %s" % rel_path)
        for c in changes:
            print("  + %s" % c)
    else:
        print("[OK]    %s" % rel_path)

print("\n" + "=" * 60)
print("Done!")
