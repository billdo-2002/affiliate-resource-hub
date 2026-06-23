import os
import re

search_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
files_to_update = [
    r"guides\general-guide.html",
    r"guides\discord-blueprint.html",
    r"guides\tiktok-youtube-shorts.html",
    r"guides\angles\scale-safely-with-margins.html",
    r"guides\angles\stop-losing-30-profit.html",
    r"guides\angles\track-profit-like-a-pro.html",
    r"resources\mcp\reddit-ready-to-post.html",
    r"resources\mcp\short-form-video-guidelines.html",
    r"resources\mcp\x-twitter-ready-to-post.html"
]

new_css = """/* Unified Callout / Note Boxes in "Quick Recap" Style */
.callout-box {
  border-left: 4px solid var(--green, #10b981);
  padding-left: 32px;
  margin: 36px 0;
  background: transparent !important;
  border-radius: 0 !important;
  box-shadow: none !important;
}
.callout-box.emerald {
  border-left-color: var(--green, #10b981);
}
.callout-box.warning,
.callout-box.mistake {
  border-left-color: #f97316;
}
.callout-title {
  font-size: 20px;
  font-weight: 700;
  color: var(--green, #10b981);
  margin-bottom: 18px;
  font-family: var(--font-family, inherit);
}
.callout-box.warning .callout-title,
.callout-box.mistake .callout-title {
  color: #ea580c;
}
.callout-bullets {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.callout-row {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}
.callout-icon {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1.5px dashed var(--green, #10b981);
  color: var(--green, #10b981);
  margin-top: 2px;
  box-sizing: border-box;
}
.callout-box.warning .callout-icon,
.callout-box.mistake .callout-icon {
  border-color: #f97316;
  color: #f97316;
}
.callout-icon svg {
  width: 14px;
  height: 14px;
  fill: currentColor;
}
.callout-text {
  font-size: 18px;
  line-height: 1.8;
  color: var(--text-color, #334155);
}
@media (max-width: 768px) {
  .callout-box {
    padding-left: 24px;
  }
  .callout-title {
    font-size: 18px;
  }
  .callout-text {
    font-size: 16px;
    line-height: 1.7;
  }
  .callout-bullets {
    gap: 16px;
  }
}"""

# HTML Replacements mapping for specific files
html_reps = {
    r"guides\general-guide.html": [
        (
            '<div class="article-note emerald">\n<p>📌 Remember: <span class="text-emerald">90%</span> of our customers are dropshippers who use Shopify to run their ecommerce stores. They often engage in communities on Reddit, Discord, and courses, or search for related content using specific keywords.</p>\n</div>',
            '<div class="callout-box emerald">\n  <div class="callout-title">Remember:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>90%</strong> of our customers are dropshippers who use Shopify to run their ecommerce stores. They often engage in communities on Reddit, Discord, and courses, or search for related content using specific keywords.\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="article-note warning">\n<p>First, a quick warning: spammy or vague content like "Hey, if you want to succeed/make more money, use TrueProfit—here\'s the link" will never work for our app.</p>\n</div>',
            '<div class="callout-box warning">\n  <div class="callout-title">Quick Warning:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Spammy or vague content</strong> like "Hey, if you want to succeed/make more money, use TrueProfit—here\'s the link" will never work for our app.\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="article-note info">\n<p>📌 These references are completely usable, but it\'s best to treat them as raw inspiration for how to approach our audience, then develop your own content based on what works best for your specific channels and audiences.</p>\n</div>',
            '<div class="callout-box emerald">\n  <div class="callout-title">Reference Note:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>These references</strong> are completely usable, but it\'s best to treat them as raw inspiration for how to approach our audience, then develop your own content based on what works best for your specific channels and audiences.\n      </div>\n    </div>\n  </div>\n</div>'
        )
    ],
    r"guides\tiktok-youtube-shorts.html": [
        (
            '<div class="article-note emerald">\n<p>💡 You don\'t need thousands of followers. A well-structured 30–45 second video with a strong hook and clear problem can reach thousands of ecommerce viewers organically — even on a new account — because the algorithm rewards watch time, not follower count.</p>\n</div>',
            '<div class="callout-box emerald">\n  <div class="callout-title">Quick Tip:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>You don\'t need</strong> thousands of followers. A well-structured 30–45 second video with a strong hook and clear problem can reach thousands of ecommerce viewers organically — even on a new account — because the algorithm rewards watch time, not follower count.\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="common-mistake">\n<strong>Common Mistake:</strong> Saying "TrueProfit is the best profit tracking tool" — this sounds promotional and kills trust. Instead, describe what it shows you: real net profit after every cost. Let the result do the selling.\n        </div>',
            '<div class="callout-box mistake">\n  <div class="callout-title">Common Mistake:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Saying "TrueProfit is the best profit tracking tool"</strong> — this sounds promotional and kills trust. Instead, describe what it shows you: real net profit after every cost. Let the result do the selling.\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="common-mistake">\n<strong>Common Mistake:</strong> Leading with "Let me show you an app" — this immediately frames the video as an ad. Lead with the insight (scaling ads doesn\'t automatically mean more profit) and let TrueProfit appear as evidence, not the subject.\n        </div>',
            '<div class="callout-box mistake">\n  <div class="callout-title">Common Mistake:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Leading with "Let me show you an app"</strong> — this immediately frames the video as an ad. Lead with the insight (scaling ads doesn\'t automatically mean more profit) and let TrueProfit appear as evidence, not the subject.\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="common-mistake">\n<strong>Common Mistake:</strong> Spending more than 5–8 seconds talking about TrueProfit\'s features. The tool mention should feel like a natural part of your workflow — not a feature overview. Show clarity, not capabilities.\n        </div>',
            '<div class="callout-box mistake">\n  <div class="callout-title">Common Mistake:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Spending more than 5–8 seconds</strong> talking about TrueProfit\'s features. The tool mention should feel like a natural part of your workflow — not a feature overview. Show clarity, not capabilities.\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="article-note warning">\n<p>💡 Universal Rule: Tool mention = 5–8 seconds. Always tie it to YOUR workflow. Show clarity, not features. Never say "This is the best app." Never lead with "Let me show you an app."</p>\n</div>',
            '<div class="callout-box warning">\n  <div class="callout-title">Universal Rule:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Tool mention = 5–8 seconds.</strong> Always tie it to YOUR workflow. Show clarity, not features. Never say "This is the best app." Never lead with "Let me show you an app."\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="article-note info">\n<p>💡 Post consistently for at least 30–60 days before evaluating results. Short-form video compounds slowly at first, then accelerates. One video earning steady commissions is worth more than 10 videos that spike once and fade.</p>\n</div>',
            '<div class="callout-box emerald">\n  <div class="callout-title">Quick Tip:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Post consistently</strong> for at least 30–60 days before evaluating results. Short-form video compounds slowly at first, then accelerates. One video earning steady commissions is worth more than 10 videos that spike once and fade.\n      </div>\n    </div>\n  </div>\n</div>'
        )
    ],
    r"resources\mcp\reddit-ready-to-post.html": [
        (
            '<div class="article-note emerald">\n      <p><strong>Angle:</strong> Root cause, storytelling. (r/dropship, r/ecommerce). Numbers make it real with the $340 and the 8-point margin drop are the hook. Keep the TrueProfit mention casual, not the focus.</p>\n    </div>',
            '<div class="callout-box emerald">\n  <div class="callout-title">Reference Note:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Angle:</strong> Root cause, storytelling. (r/dropship, r/ecommerce). Numbers make it real with the $340 and the 8-point margin drop are the hook. Keep the TrueProfit mention casual, not the focus.\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="article-note emerald">\n      <p><strong>Angle:</strong> Context-aware, workflow improvement. (r/entrepreneur, r/SideProject). The frustration of manual AI workflows is the hook and frame TrueProfit MCP as the fix you stumbled onto, not the point of the post.</p>\n    </div>',
            '<div class="callout-box emerald">\n  <div class="callout-title">Reference Note:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Angle:</strong> Context-aware, workflow improvement. (r/entrepreneur, r/SideProject). The frustration of manual AI workflows is the hook and frame TrueProfit MCP as the fix you stumbled onto, not the point of the post.\n      </div>\n    </div>\n  </div>\n</div>'
        )
    ],
    r"resources\mcp\x-twitter-ready-to-post.html": [
        (
            '<div class="article-note emerald">\n      <p><strong>Angle:</strong> Video shows the actual Claude conversation pulling store data. Text sets up the relatable moment first, video does the rest.</p>\n    </div>',
            '<div class="callout-box emerald">\n  <div class="callout-title">Reference Note:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Angle:</strong> Video shows the actual Claude conversation pulling store data. Text sets up the relatable moment first, video does the rest.\n      </div>\n    </div>\n  </div>\n</div>'
        ),
        (
            '<div class="article-note emerald">\n      <p><strong>Angle:</strong> Root cause. Hits the gap between revenue and real profit. Works as a standalone observation.</p>\n    </div>',
            '<div class="callout-box emerald">\n  <div class="callout-title">Reference Note:</div>\n  <div class="callout-bullets">\n    <div class="callout-row">\n      <div class="callout-icon">\n        <svg viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>\n      </div>\n      <div class="callout-text">\n        <strong>Angle:</strong> Root cause. Hits the gap between revenue and real profit. Works as a standalone observation.\n      </div>\n    </div>\n  </div>\n</div>'
        )
    ]
}

# Regex to match old CSS blocks
css_pattern = re.compile(
    r'\/\*\s*Insight\s*&\s*Info\s*Note\s*Blocks\s*\*\/.*?'
    r'\.article-note\s*\{.*?'
    r'\.article-note\.info\s*\{[^\}]*\}',
    re.DOTALL
)

mistake_css_pattern = re.compile(
    r'\/\*\s*=+\s*COMMON\s*MISTAKE\s*CALLOUT.*?'
    r'\.common-mistake\s*\{.*?'
    r'\.common-mistake\s*strong\s*\{[^\}]*\}',
    re.DOTALL | re.IGNORECASE
)

for rel_path in files_to_update:
    full_path = os.path.join(search_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Skipping non-existent file: {rel_path}")
        continue
    
    print(f"\nProcessing: {rel_path}")
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Replace CSS stylesheet rules
    css_replaced = False
    
    # Try finding note blocks styling
    if css_pattern.search(content):
        content = css_pattern.sub(new_css, content)
        css_replaced = True
        print("  -> Replaced .article-note CSS rule block.")
    else:
        # Fallback if comment is missing or slightly different
        fallback_pattern = re.compile(
            r'\.article-note\s*\{.*?'
            r'\.article-note\.info\s*\{[^\}]*\}',
            re.DOTALL
        )
        if fallback_pattern.search(content):
            content = fallback_pattern.sub(new_css, content)
            css_replaced = True
            print("  -> Replaced .article-note CSS rule block (fallback pattern).")
            
    # Try finding common mistake styling (specifically in tiktok guidelines page)
    if mistake_css_pattern.search(content):
        content = mistake_css_pattern.sub("", content)
        print("  -> Removed .common-mistake CSS rule block.")
        
    # 2. Replace HTML callout boxes if mappings exist
    html_replaced_count = 0
    if rel_path in html_reps:
        for old_html, new_html in html_reps[rel_path]:
            # Normalize newlines slightly if needed
            if old_html in content:
                content = content.replace(old_html, new_html)
                html_replaced_count += 1
            else:
                # Try finding with normalized spaces / newlines
                old_normalized = old_html.replace('\r\n', '\n')
                content_normalized = content.replace('\r\n', '\n')
                if old_normalized in content_normalized:
                    content_normalized = content_normalized.replace(old_normalized, new_html)
                    content = content_normalized
                    html_replaced_count += 1
                else:
                    print(f"  [WARNING] Could not find HTML block starting with: {old_html[:30].encode('ascii', errors='backslashreplace').decode('ascii')}...")
                    
    print(f"  -> Replaced {html_replaced_count} HTML notes.")
    
    # Save file
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  -> File updated successfully.")
