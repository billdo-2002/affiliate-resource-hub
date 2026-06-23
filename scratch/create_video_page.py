import os

# Paths
base_dir = r"c:\Users\khoadnd\Desktop\onboarding hub"
template_path = os.path.join(base_dir, "guides", "tiktok-youtube-shorts.html")
md_path = os.path.join(base_dir, "TrueProfit Affiliate Playbook (2).md")
output_path = os.path.join(base_dir, "resources", "mcp", "short-form-video-guidelines.html")

# Read template
with open(template_path, 'r', encoding='utf-8') as f:
    template_html = f.read()

# Read markdown to extract content
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Extract sections from markdown (approximate, we will hardcode the exact text since we already viewed it and know it)
markdown_why_it_works = """<p class="article-p">MCP is a feature most merchants haven't heard of and "AI connected to your profit data" sounds abstract until someone sees it in action. Short-form video closes that gap in 30–40 seconds by showing a real use case, not explaining a concept.</p>
<p class="article-p">The hook isn't "here's a new feature." The hook is a problem merchants already feel: checking profit is slow, dashboards don't explain why numbers change, AI tools need manual data every time. Once they see the problem framed clearly, the solution sells itself.</p>"""

markdown_directions = """<p class="article-p">Short-form works when you build around a single strong idea, not when you try to explain everything. Below are ready-to-use hook frameworks you can model directly. Each one includes:</p>
<ul class="article-list">
  <li>The core angle</li>
  <li>Exact script guidance</li>
  <li>How to integrate TrueProfit naturally</li>
  <li>What to show on screen</li>
  <li>Execution notes to avoid sounding promotional</li>
</ul>"""

# We'll split the template into Top (up to <section class="guide-hero">), and Bottom (from <!-- ============================== RELATED GUIDES)
# Actually, it's safer to split by known markers.

top_marker = '<!-- ==============================\n     HERO SECTION\n     ============================== -->'
bottom_marker = '<!-- ==============================\n     FOOTER\n     ============================== -->'
related_marker = '<!-- ==============================\n     RELATED GUIDES\n     ============================== -->'

parts = template_html.split(top_marker)
head_and_header = parts[0]
rest = top_marker + parts[1]

# Now split by related guides
parts2 = rest.split(related_marker)
hero_and_body = parts2[0]
related_and_footer = related_marker + parts2[1]

parts3 = related_and_footer.split(bottom_marker)
related_and_cta = parts3[0]
footer = bottom_marker + parts3[1]


# Constructing the new Hero
new_hero = """<!-- ==============================
     HERO SECTION
     ============================== -->
<section class="guide-hero">
  <div class="guide-hero-inner">
    <div class="guide-hero-left stagger-enter" style="animation-delay: 0.1s;">
      <!-- Breadcrumb -->
      <div class="guide-breadcrumb">
        <a href="../../index.html">Home</a>
        <span class="sep">›</span>
        <a href="../../guides.html">Resources</a>
        <span class="sep">›</span>
        <a href="../../guides/mcp-promotion-playbook.html">MCP Promotion</a>
        <span class="sep">›</span>
        <span class="current">Short-Form Video Guidelines</span>
      </div>
      <!-- Title -->
      <h1 class="guide-hero-title">MCP Short-Form Video Guidelines</h1>
      <!-- Subtitle -->
      <p class="guide-hero-subtitle">Two ready-to-use video hook frameworks to explain TrueProfit MCP naturally in short-form content without sounding promotional.</p>
      <!-- Tags -->
      <div class="guide-tags">
        <span class="guide-tag">MCP Promotion</span>
        <span class="guide-tag">Short-Form Video</span>
        <span class="guide-tag">TikTok</span>
        <span class="guide-tag">YouTube Shorts</span>
      </div>
      <!-- CTA button -->
      <div class="guide-hero-btns">
        <a href="#video-hooks" class="hero-btn-angles">
          View video hooks
          <svg class="hero-btn-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>

    <!-- Hero illustration -->
    <div class="guide-hero-visual stagger-enter" style="animation-delay: 0.2s;">
      <div class="guide-hero-illus-placeholder" style="background: rgba(26,122,94,0.05); border: 1px dashed rgba(26,122,94,0.3); border-radius: 20px; width: 100%; height: 280px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; color: var(--green);">
        <div class="illus-placeholder-icon">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect>
            <line x1="7" y1="2" x2="7" y2="22"></line>
            <line x1="17" y1="2" x2="17" y2="22"></line>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <line x1="2" y1="7" x2="7" y2="7"></line>
            <line x1="2" y1="17" x2="7" y2="17"></line>
            <line x1="17" y1="17" x2="22" y2="17"></line>
            <line x1="17" y1="7" x2="22" y2="7"></line>
          </svg>
        </div>
        <div class="illus-placeholder-label" style="font-weight: 700; font-size: 15px;">MCP Short-Form Video Hero</div>
        <div class="illus-placeholder-sublabel" style="font-size: 13px; opacity: 0.7;">/assets/guides/mcp-short-form-video-hero.svg</div>
      </div>
    </div>
  </div>
</section>
"""

new_body = f"""<!-- ==============================
     GUIDE BODY — 2 COLUMN
     ============================== -->
<div class="guide-body">
  <div class="guide-body-inner">

    <!-- LEFT: GUIDE CONTENT -->
    <main class="guide-content">

      <!-- ======== SECTION 1 ======== -->
      <div class="article-section scroll-animate" id="why-short-form-works">
        <h2 class="article-h2">1. Why Short-Form Works for MCP Promotion</h2>
        {markdown_why_it_works}
      </div>

      <!-- ======== SECTION 2 ======== -->
      <div class="article-section scroll-animate" id="direction-angles">
        <h2 class="article-h2">2. Direction & Angles</h2>
        {markdown_directions}
      </div>

      <!-- ======== SECTION 3 ======== -->
      <div class="article-section scroll-animate" id="video-hooks">
        <h2 class="article-h2">3. Ready-to-Use Video Hooks</h2>
        <p class="article-p">These two hook frameworks are built to show MCP in action quickly. Each one starts with a merchant problem, shows the AI-powered insight, and introduces TrueProfit only after the value is clear.</p>

        <!-- Hook 1 -->
        <div class="hook-visual-panel">
          <div class="hook-panel-img-col">
            <div class="illus-placeholder" style="width: 100%; aspect-ratio: 4/3; background: #e2f6ed; border: 1px dashed #2dd498; border-radius: 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #1a7a5e; gap: 8px;">
               <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
               <span style="font-weight: 600; font-size: 13px;">/assets/guides/mcp-video-hook-1.svg</span>
            </div>
          </div>
          <div class="hook-panel-text-col">
            <div class="hook-panel-eyebrow">HOOK 1</div>
            <div class="hook-panel-title">AI already knows my store data</div>
            <div class="hook-panel-body">This hook works because it creates a surprising MCP moment: the merchant asks a normal business question and the AI already has the TrueProfit context to answer.</div>
            <div class="hook-panel-tags">
              <span class="hook-panel-tag">30–40s</span>
              <span class="hook-panel-tag">AI moment</span>
              <span class="hook-panel-tag">Casual surprise</span>
            </div>
          </div>
        </div>

        <div class="article-table-wrapper" style="overflow-x: auto; margin-bottom: 56px;">
          <table class="article-table" style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr style="background: var(--light-alt);">
                <th style="padding: 18px 22px; text-align: left; font-size: 13px; font-weight: 700; text-transform: uppercase; color: #475569; border-bottom: 1px solid #DDE4F0; white-space: nowrap;">Section</th>
                <th style="padding: 18px 22px; text-align: left; font-size: 13px; font-weight: 700; text-transform: uppercase; color: #475569; border-bottom: 1px solid #DDE4F0; white-space: nowrap;">What to Say (Script Guide)</th>
                <th style="padding: 18px 22px; text-align: left; font-size: 13px; font-weight: 700; text-transform: uppercase; color: #475569; border-bottom: 1px solid #DDE4F0; white-space: nowrap;">What to Show</th>
                <th style="padding: 18px 22px; text-align: left; font-size: 13px; font-weight: 700; text-transform: uppercase; color: #475569; border-bottom: 1px solid #DDE4F0; white-space: nowrap;">Execution Notes</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-dark); vertical-align: top;">Hook (0–3s)</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">"I asked Claude how my store was doing this week and it actually knew."</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Face-on. No caption needed.</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Slight pause after "actually knew." Let curiosity land before moving on.</td>
              </tr>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-dark); vertical-align: top;">Problem (3–12s)</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">"Usually I'd open TrueProfit, check revenue, cross-reference ad spend, do the math myself. Every. Single. Time."</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Quick cuts: Shopify tab &rarr; ads dashboard &rarr; spreadsheet</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Keep energy slightly frustrated. Relatable, not dramatic.</td>
              </tr>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-dark); vertical-align: top;">Insight (12–25s)</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">"TrueProfit has an MCP integration now. Connect once, and your AI already has your live profit data loaded: every conversation, automatically."</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Screen recording: Claude chat open, typing the question, answer appearing</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Show the actual AI response. Blur store name/revenue if needed. This is the proof moment, slow down slightly.</td>
              </tr>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-dark); vertical-align: top;">Mention TrueProfit MCP (25–35s)</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Primary: "I've been using TrueProfit for profit tracking, this just made it way more useful." Softer: "Didn't even know this was possible until I set it up."</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">3–5s dashboard clip. Blur specific numbers.</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Don't zoom in on pricing or features. Just enough to show it's real.</td>
              </tr>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: none; color: var(--text-dark); vertical-align: top;">CTA (35–40s)</td>
                <td style="padding: 18px 22px; border-bottom: none; color: var(--text-body); vertical-align: top;">"Install it from the Shopify App Store and the link's in the description, and connect it to whatever AI you're already using."</td>
                <td style="padding: 18px 22px; border-bottom: none; color: var(--text-body); vertical-align: top;">Caption: <em>Link below</em></td>
                <td style="padding: 18px 22px; border-bottom: none; color: var(--text-body); vertical-align: top;">Neutral tone. No urgency, no pressure.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Hook 2 -->
        <div class="hook-visual-panel">
          <div class="hook-panel-img-col">
            <div class="illus-placeholder" style="width: 100%; aspect-ratio: 4/3; background: #e2f6ed; border: 1px dashed #2dd498; border-radius: 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #1a7a5e; gap: 8px;">
               <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
               <span style="font-weight: 600; font-size: 13px;">/assets/guides/mcp-video-hook-2.svg</span>
            </div>
          </div>
          <div class="hook-panel-text-col">
            <div class="hook-panel-eyebrow">HOOK 2</div>
            <div class="hook-panel-title">Revenue looked fine. Profit didn't.</div>
            <div class="hook-panel-body">This hook works because it starts with a familiar ecommerce problem, then uses MCP as the fast way to uncover the real reason behind the profit mismatch.</div>
            <div class="hook-panel-tags">
              <span class="hook-panel-tag">35–45s</span>
              <span class="hook-panel-tag">Root cause</span>
              <span class="hook-panel-tag">Operator mindset</span>
            </div>
          </div>
        </div>

        <div class="article-table-wrapper" style="overflow-x: auto;">
          <table class="article-table" style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr style="background: var(--light-alt);">
                <th style="padding: 18px 22px; text-align: left; font-size: 13px; font-weight: 700; text-transform: uppercase; color: #475569; border-bottom: 1px solid #DDE4F0; white-space: nowrap;">Section</th>
                <th style="padding: 18px 22px; text-align: left; font-size: 13px; font-weight: 700; text-transform: uppercase; color: #475569; border-bottom: 1px solid #DDE4F0; white-space: nowrap;">What to Say</th>
                <th style="padding: 18px 22px; text-align: left; font-size: 13px; font-weight: 700; text-transform: uppercase; color: #475569; border-bottom: 1px solid #DDE4F0; white-space: nowrap;">What to Show</th>
                <th style="padding: 18px 22px; text-align: left; font-size: 13px; font-weight: 700; text-transform: uppercase; color: #475569; border-bottom: 1px solid #DDE4F0; white-space: nowrap;">Execution Notes</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-dark); vertical-align: top;">Hook (0–3s)</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">"Last month my revenue was up 18%. My actual profit was down $600. And I had no idea why."</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Face-on. Bold caption: <em>Revenue &ne; Profit</em></td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Say it matter-of-fact. The numbers do the work, don't over-emote.</td>
              </tr>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-dark); vertical-align: top;">Problem (3–15s)</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">"ROAS looked fine. Refunds were normal. Ad spend was actually lower. I went through everything manually and still couldn't find it."</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Text overlays: ROAS &check; Refunds &check; Ad spend &check; &rarr; then a question mark</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Faster pace. Keep the energy of someone genuinely confused, not panicking.</td>
              </tr>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-dark); vertical-align: top;">Insight (15–28s)</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">"I opened Claude, asked it why my margin dropped last month, it pulled my TrueProfit data and cross-referenced everything. Flagged a shipping cost I'd had wrong for weeks. $340 in avoidable losses."</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Screen recording: the actual AI response with root cause visible</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">This is the <em>aha</em> moment. Slow down. Let the number ($340) land before moving on.</td>
              </tr>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-dark); vertical-align: top;">Mention TrueProfit MCP (28–38s)</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Primary: "TrueProfit connects to Claude or ChatGPT directly before I touch the ad budget, I ask it first." Softer: "It's like having someone who already knows all your numbers."</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Product-level profit view. Show one SKU breakdown.</td>
                <td style="padding: 18px 22px; border-bottom: 1px solid #DDE4F0; color: var(--text-body); vertical-align: top;">Position as your standard operating practice, not a recommendation.</td>
              </tr>
              <tr>
                <td style="font-weight: 600; padding: 18px 22px; border-bottom: none; color: var(--text-dark); vertical-align: top;">CTA (38–45s)</td>
                <td style="padding: 18px 22px; border-bottom: none; color: var(--text-body); vertical-align: top;">"It's on the Shopify App Store, grab it and connect it to your AI. Link in the description."</td>
                <td style="padding: 18px 22px; border-bottom: none; color: var(--text-body); vertical-align: top;">Caption: <em>Link in description</em></td>
                <td style="padding: 18px 22px; border-bottom: none; color: var(--text-body); vertical-align: top;">Confident, not pushy. One sentence, no elaboration needed.</td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>

      <!-- ======== SECTION 4 ======== -->
      <div class="article-section scroll-animate" id="final-notes">
        <h2 class="article-h2">4. Final Notes</h2>
        <p class="article-p">The best MCP videos should not feel like a feature demo. Start with a real merchant problem, show the AI-powered insight, and let TrueProfit MCP appear as the reason the answer is accurate.</p>
      </div>

    </main>

    <!-- RIGHT: STICKY SIDEBAR -->
    <aside class="guide-sidebar">
      <div class="sidebar-progress scroll-animate">
        <svg class="sidebar-progress-icon" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
          <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
        </svg>
        <div class="sidebar-progress-text">
          MCP CONTENT
          <span>Short-Form Video Guidelines<br>2 hooks · ~8 min read</span>
        </div>
      </div>

      <div class="sidebar-card scroll-animate" style="transition-delay: 0.1s;">
        <div class="sidebar-card-title">On this page</div>
        <ul class="sidebar-toc">
          <li><a href="#why-short-form-works">Why Short-Form Works</a></li>
          <li><a href="#direction-angles">Direction & Angles</a></li>
          <li><a href="#video-hooks">Ready-to-Use Video Hooks</a></li>
          <li><a href="#final-notes">Final Notes</a></li>
        </ul>
      </div>

      <div class="sidebar-card scroll-animate" style="transition-delay: 0.2s;">
        <div class="sidebar-card-title">Ready to start?</div>
        <p class="sidebar-cta-text">Pick one hook, customize the script, and show MCP as part of a real merchant workflow.</p>
        <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="sidebar-btn-primary">Get affiliate link</a>
        <a href="../../guides/mcp-promotion-playbook.html" class="sidebar-link">Back to MCP Playbook <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg></a>
      </div>
    </aside>
  </div>
</div>
"""

new_related_and_cta = """<!-- ==============================
     RELATED GUIDES
     ============================== -->
<section class="related-section">
  <div class="related-inner">
    <div class="related-header scroll-animate">
      <div class="related-label">MCP PROMOTION</div>
      <h2 class="related-title">Continue with another MCP resource</h2>
      <p style="font-size: 18px; color: var(--text-body); margin-top: 12px;">Choose another format to promote TrueProfit MCP naturally.</p>
    </div>

    <div class="related-grid">
      <a href="x-twitter-ready-to-post.html" class="related-card scroll-animate" style="transition-delay: 0.1s;">
        <span class="related-card-tag">Content Angle</span>
        <div class="related-card-title">X/Twitter Ready-to-Post</div>
        <div class="related-card-desc">Short, punchy MCP post angles designed for quick awareness and creator updates.</div>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>

      <a href="reddit-ready-to-post.html" class="related-card scroll-animate" style="transition-delay: 0.2s;">
        <span class="related-card-tag">Content Angle</span>
        <div class="related-card-title">Reddit Ready-to-Post</div>
        <div class="related-card-desc">Longer community-friendly MCP post angles for Reddit and ecommerce discussions.</div>
        <div class="related-card-footer">
          <div class="related-card-link">
            Read playbook
            <svg class="related-card-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
          </div>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- ==============================
     BOTTOM CTA
     ============================== -->
<section class="guide-cta-section scroll-animate" style="background-color: #051d29; background-image: linear-gradient(rgba(5, 29, 41, 0.6), rgba(5, 29, 41, 0.6)), url('../../24.svg'); background-size: cover; background-position: center; background-repeat: no-repeat; position: relative; padding: 80px 28px; text-align: center; overflow: hidden;">
  <div class="guide-cta-inner" style="max-width: 720px; margin: 0 auto; position: relative; z-index: 2;">
    <h2 class="guide-cta-h2" style="font-size: 48px; font-weight: 900; color: #fff; margin-bottom: 20px; letter-spacing: -0.025em; line-height: 1.25;">Ready to create your first <span>MCP short-form video?</span></h2>
    <p class="guide-cta-sub" style="font-size: 18px; color: rgba(255,255,255,0.7); margin-bottom: 40px; line-height: 1.7;">Choose one hook, adapt the script to your style, show the MCP moment clearly, and add your affiliate link naturally.</p>
    <div class="guide-cta-btns" style="display: flex; gap: 24px; justify-content: center; flex-wrap: wrap;">
      <a href="https://affiliate.trueprofit.io/sign-up" target="_blank" class="btn-cta-white" style="background: #fff; color: var(--navy); font-weight: 700; height: 56px; display: inline-flex; align-items: center; justify-content: center; padding: 0 32px; border-radius: var(--radius); transition: var(--transition); font-family: var(--font); font-size: 16px; text-decoration: none;">Get affiliate link →</a>
      <a href="../../guides/mcp-promotion-playbook.html" class="btn-cta-ghost" style="background: transparent; color: #fff; border: 1.5px solid rgba(255,255,255,0.3); font-weight: 700; height: 56px; display: inline-flex; align-items: center; justify-content: center; padding: 0 32px; border-radius: var(--radius); transition: var(--transition); font-family: var(--font); font-size: 16px; text-decoration: none;">Back to MCP Playbook</a>
    </div>
  </div>
</section>
"""

# Need to fix the <title> tag in the head and link paths because we are in /resources/mcp/ instead of /guides/
# Paths in template are ../ (up one level to root). We need to change them to ../../ to go up two levels.

head_and_header = head_and_header.replace('<title>TikTok &amp; YouTube Shorts — TrueProfit Affiliate Resource Hub</title>', '<title>Short-Form Video Guidelines — TrueProfit Affiliate Resource Hub</title>')
head_and_header = head_and_header.replace('href="../', 'href="../../')
head_and_header = head_and_header.replace('src="../', 'src="../../')
head_and_header = head_and_header.replace("url('../", "url('../../")

footer = footer.replace('href="../', 'href="../../')
footer = footer.replace('src="../', 'src="../../')

# Put it all together
new_html = head_and_header + new_hero + new_body + new_related_and_cta + footer

# Write file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("File generated successfully.")
