import os
from bs4 import BeautifulSoup

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
files_to_process = [
    r"guides\general-guide.html",
    r"guides\tiktok-youtube-shorts.html"
]

# Unified SVG icon
star_icon_svg = '<svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>'

def make_callout(box_class, title, content_html):
    return f"""<div class="callout-box {box_class}">
  <div class="callout-title">{title}</div>
  <div class="callout-bullets">
    <div class="callout-row">
      <div class="callout-icon">
        {star_icon_svg}
      </div>
      <div class="callout-text">
        {content_html}
      </div>
    </div>
  </div>
</div>"""

for rel_path in files_to_process:
    full_path = os.path.join(search_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Skipping non-existent file: {rel_path}")
        continue
        
    print(f"\nProcessing DOM of: {rel_path}")
    with open(full_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all callout/note boxes
    notes = soup.find_all(class_=lambda x: x and any(c in x for c in ['article-note', 'common-mistake']))
    
    replaced_count = 0
    for note in notes:
        text_content = note.get_text()
        
        # Check general-guide.html notes
        if "dropshippers who use Shopify to run their ecommerce stores" in text_content:
            # Note 1: Remember note
            content = '<strong>90%</strong> of our customers are dropshippers who use Shopify to run their ecommerce stores. They often engage in communities on Reddit, Discord, and courses, or search for related content using specific keywords.'
            new_html = make_callout("emerald", "Remember:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced Note 1: Remember")
            
        elif "spammy or vague content like" in text_content:
            # Note 2: Warning note
            content = '<strong>Spammy or vague content</strong> like "Hey, if you want to succeed/make more money, use TrueProfit—here\'s the link" will never work for our app.'
            new_html = make_callout("warning", "Quick Warning:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced Note 2: Quick Warning")
            
        elif "These references are completely usable" in text_content:
            # Note 3: Reference note
            content = '<strong>These references</strong> are completely usable, but it\'s best to treat them as raw inspiration for how to approach our audience, then develop your own content based on what works best for your specific channels and audiences.'
            new_html = make_callout("emerald", "Reference Note:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced Note 3: Reference Note")
            
        # Check tiktok-youtube-shorts.html notes
        elif "You don't need thousands of followers" in text_content:
            # Note 1: Followers Tip
            content = '<strong>You don\'t need</strong> thousands of followers. A well-structured 30–45 second video with a strong hook and clear problem can reach thousands of ecommerce viewers organically — even on a new account — because the algorithm rewards watch time, not follower count.'
            new_html = make_callout("emerald", "Quick Tip:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced TikTok Note 1: Followers Tip")
            
        elif "Saying \"TrueProfit is the best profit tracking tool\"" in text_content:
            # Note 2: Mistake 1
            content = '<strong>Saying "TrueProfit is the best profit tracking tool"</strong> — this sounds promotional and kills trust. Instead, describe what it shows you: real net profit after every cost. Let the result do the selling.'
            new_html = make_callout("mistake", "Common Mistake:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced TikTok Note 2: Mistake 1")
            
        elif "Leading with \"Let me show you an app\"" in text_content:
            # Note 3: Mistake 2
            content = '<strong>Leading with "Let me show you an app"</strong> — this immediately frames the video as an ad. Lead with the insight (scaling ads doesn\'t automatically mean more profit) and let TrueProfit appear as evidence, not the subject.'
            new_html = make_callout("mistake", "Common Mistake:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced TikTok Note 3: Mistake 2")
            
        elif "Spending more than 5–8 seconds talking" in text_content:
            # Note 4: Mistake 3
            content = '<strong>Spending more than 5–8 seconds</strong> talking about TrueProfit\'s features. The tool mention should feel like a natural part of your workflow — not a feature overview. Show clarity, not capabilities.'
            new_html = make_callout("mistake", "Common Mistake:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced TikTok Note 4: Mistake 3")
            
        elif "Universal Rule: Tool mention = 5" in text_content or "Tool mention = 5" in text_content:
            # Note 5: Universal Rule
            content = '<strong>Tool mention = 5–8 seconds.</strong> Always tie it to YOUR workflow. Show clarity, not features. Never say "This is the best app." Never lead with "Let me show you an app."'
            new_html = make_callout("warning", "Universal Rule:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced TikTok Note 5: Universal Rule")
            
        elif "Post consistently for at least 30" in text_content:
            # Note 6: Quick Tip consistent posting
            content = '<strong>Post consistently</strong> for at least 30–60 days before evaluating results. Short-form video compounds slowly at first, then accelerates. One video earning steady commissions is worth more than 10 videos that spike once and fade.'
            new_html = make_callout("emerald", "Quick Tip:", content)
            new_node = BeautifulSoup(new_html, 'html.parser').div
            note.replace_with(new_node)
            replaced_count += 1
            print("  -> Replaced TikTok Note 6: Quick Tip")
            
    # Save the updated DOM back to file
    if replaced_count > 0:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"  -> Replaced {replaced_count} HTML note elements in {rel_path} using DOM replacement.")
    else:
        print(f"  -> No notes matched in {rel_path}.")
