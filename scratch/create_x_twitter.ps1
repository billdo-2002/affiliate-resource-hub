$html = Get-Content "c:\Users\khoadnd\Desktop\onboarding hub\guides\angles\track-profit-like-a-pro.html" -Raw

# Title & Head
$html = $html -replace '<title>.*?</title>', '<title>X/Twitter Ready-to-Post — TrueProfit MCP Promotion</title>'
$html = $html -replace '<meta name="description" content=".*?">', '<meta name="description" content="Two ready-to-use MCP promotion angles for short, punchy X/Twitter content.">'

# Breadcrumb
$breadcrumbOld = '<a href="\.\./\.\./index\.html">Home</a> <span class="sep">/</span>\s*<a href="\.\./\.\./guides\.html">Guides</a> <span class="sep">/</span>\s*<a href="\.\./\.\./guides\.html#angles">Content Angles</a> <span class="sep">/</span>\s*<span class="current">Track Profit Like A Pro</span>'
$breadcrumbNew = '<a href="../../index.html">Home</a> <span class="sep">/</span>
      <a href="../../guides.html">Resources</a> <span class="sep">/</span>
      <a href="/resources/mcp-promotion-playbook">MCP Promotion</a> <span class="sep">/</span>
      <span class="current">X/Twitter Ready-to-Post</span>'
$html = [regex]::Replace($html, $breadcrumbOld, $breadcrumbNew)

# Hero Title & Subtitle
$html = $html -replace '<h1 class="guide-hero-title">Track Profit Like A Pro</h1>', '<h1 class="guide-hero-title">X/Twitter Ready-to-Post</h1>'
$html = $html -replace '<p class="guide-hero-subtitle">.*?</p>', '<p class="guide-hero-subtitle">Two ready-to-use MCP promotion angles for short, punchy X/Twitter content.</p>'

# Hero Tags
$tagsOld = '(?s)<div class="guide-tags">.*?</div>'
$tagsNew = '<div class="guide-tags">
        <div class="guide-tag" style="display:flex;align-items:center;gap:4px;"><svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg> X/Twitter</div>
        <div class="guide-tag">MCP</div>
        <div class="guide-tag">Ready-to-Post</div>
        <div class="guide-tag">Short Copy</div>
      </div>'
$html = [regex]::Replace($html, $tagsOld, $tagsNew)

# CTA Button
$html = $html -replace 'Read the angle below', 'View post examples'

# Hero Visual Placeholder
$visualOld = '(?s)<div class="guide-hero-visual">.*?</div>\s*</div>'
$visualNew = '<div class="guide-hero-visual">
        <div class="guide-hero-illus-placeholder">
          <div class="illus-placeholder-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
          </div>
          <div>
            <div class="illus-placeholder-label">X/Twitter MCP Hero</div>
            <div class="illus-placeholder-sublabel">/assets/guides/mcp-x-twitter-hero.svg</div>
          </div>
        </div>
      </div>'
$html = [regex]::Replace($html, $visualOld, $visualNew)

# Sidebar
$html = $html -replace 'CONTENT ANGLE<span>Track Profit Like A Pro<br>3 sections • ~4 min read</span>', 'MCP CONTENT<span>X/Twitter Ready-to-Post<br>2 hooks • ~5 min read</span>'
$tocOld = '(?s)<ul class="sidebar-toc">.*?</ul>'
$tocNew = '<ul class="sidebar-toc">
        <li><a href="#hook-1">Hook #1</a></li>
        <li><a href="#hook-2">Hook #2</a></li>
        <li><a href="#materials">Materials</a></li>
      </ul>'
$html = [regex]::Replace($html, $tocOld, $tocNew)

$html = $html -replace 'Get your affiliate link and start promoting TrueProfit today\.', 'Pick one post, customize it for your audience, and add your affiliate link naturally.'
$html = $html -replace '<a href="../../guides.html" class="sidebar-link">\s*Back to Guides', '<a href="/resources/mcp-promotion-playbook" class="sidebar-link">
        Back to MCP Playbook'

# Article Content
$articleOld = '(?s)<article class="article-body">.*?</article>'
$articleNew = '<article class="article-body" id="post-examples">
        <div class="article-top-label" style="display:flex;align-items:center;gap:6px;">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg> X/Twitter Post Formats
        </div>

        <section class="article-section" id="hook-1">
          <h2 class="article-h2">Hook #1: 2am, no app, still got my numbers.</h2>
          <div class="article-note emerald">
            <p><strong>Angle:</strong> Video shows the actual Claude conversation pulling store data. Text sets up the relatable moment first, video does the rest.</p>
          </div>
          
          <div class="article-example-block" style="position:relative; padding-top:48px;">
            <div style="position:absolute; top:16px; right:16px; font-size:11px; font-weight:700; color:#1a7a5e; background:rgba(26,122,94,0.1); padding:4px 10px; border-radius:4px; cursor:pointer;">COPY POST</div>
            <p class="article-p">Couldn''t sleep, started spiraling about whether this week was actually profitable or just high-revenue`</p>
            <p class="article-p">Typed into claude: "How''s my store doing vs last week"</p>
            <p class="article-p">It just answered. real margin, ad efficiency, everything and pulled straight from TrueProfit</p>
            <p class="article-p">It took 30 seconds.</p>
            <p class="article-p">If you did not try TrueProfit, grab it here <strong class="text-emerald">[your affiliate link]</strong>. Don’t let your store data just sit in an app doing nothing, connect it to your AI and actually use it.</p>
          </div>
        </section>

        <section class="article-section" id="hook-2">
          <h2 class="article-h2">Hook #2: Revenue looked fine. Something was still wrong.</h2>
          <div class="article-note emerald">
            <p><strong>Angle:</strong> Root cause. Hits the gap between revenue and real profit. Works as a standalone observation.</p>
          </div>
          
          <div class="article-example-block" style="position:relative; padding-top:48px;">
            <div style="position:absolute; top:16px; right:16px; font-size:11px; font-weight:700; color:#1a7a5e; background:rgba(26,122,94,0.1); padding:4px 10px; border-radius:4px; cursor:pointer;">COPY POST</div>
            <p class="article-p">January: best revenue month ever</p>
            <p class="article-p">Also January: margin quietly dropped 8 points</p>
            <p class="article-p">Also January: found out because I asked my AI, not because my dashboard told me</p>
            <p class="article-p">Shipping cost miscalculation. ~$340 in avoidable losses. 30 seconds to find.</p>
            <p class="article-p">So... Getting TrueProfit here <strong class="text-emerald">[your affiliate link]</strong> and putting it to work with your AI. Your store data shouldn''t just live in an app!!</p>
          </div>
        </section>

        <section class="article-section" id="materials">
          <h3 class="article-h3">Materials</h3>
          <ul class="article-list">
            <li><strong>Video:</strong> [material video] (Show the Claude/ChatGPT conversation pulling real store data)</li>
          </ul>
        </section>

      </article>'
$html = [regex]::Replace($html, $articleOld, $articleNew)

# Related section
$html = $html -replace 'MORE CONTENT ANGLES', 'MCP PROMOTION'
$html = $html -replace 'Continue with another ready-to-post angle', 'Continue with another MCP resource'
$htmlOldDesc = '<p class="related-desc">.*?</p>'
$html = [regex]::Replace($html, $htmlOldDesc, '') # Remove the original if any, but wait, the original didn''t have a description under related-title. Let me add it.
$html = $html -replace '<h2 class="related-title">Continue with another MCP resource</h2>', '<h2 class="related-title">Continue with another MCP resource</h2><p class="mcp-section-sub" style="margin-top:16px;">Choose another format to promote TrueProfit MCP naturally.</p>'

$relatedOld = '(?s)<div class="related-grid">.*?</div>\s*</div>\s*</section>'
$relatedNew = '<div class="related-grid">
        <!-- Related 1 -->
        <a href="/resources/mcp/reddit-ready-to-post" class="related-card scroll-animate" style="transition-delay: 0.1s;">
          <span class="related-card-tag">Ready-to-Post</span>
          <div class="related-card-title">Reddit Ready-to-Post</div>
          <div class="related-card-desc">Longer community-friendly MCP post angles for Reddit and ecommerce discussions.</div>
          <div class="related-card-footer">
            <div class="related-card-link">
              Read playbook
              <svg class="related-card-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
            </div>
          </div>
        </a>
        <!-- Related 2 -->
        <a href="/resources/mcp/short-form-video-guidelines" class="related-card scroll-animate" style="transition-delay: 0.2s;">
          <span class="related-card-tag">Guidelines</span>
          <div class="related-card-title">Short-Form Video Guidelines</div>
          <div class="related-card-desc">Two video hook frameworks with script flow, what to show, and execution notes.</div>
          <div class="related-card-footer">
            <div class="related-card-link">
              Read playbook
              <svg class="related-card-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M12 5l7 7-7 7"/></svg>
            </div>
          </div>
        </a>
      </div>
    </div>
  </section>'
$html = [regex]::Replace($html, $relatedOld, $relatedNew)

# Bottom CTA
$html = $html -replace '<h2 class="guide-cta-h2">Ready to use this angle in <span>your content\?</span></h2>', '<h2 class="guide-cta-h2">Ready to post your first MCP angle?</h2>'
$html = $html -replace '<p class="guide-cta-sub">Customize the example for your own audience, add your affiliate link naturally, and publish it where merchants already ask for help.</p>', '<p class="guide-cta-sub">Choose one hook, customize the copy, replace the affiliate link placeholder, and publish it on X.</p>'
$html = $html -replace '<a href="\.\./general-guide\.html" class="btn-cta-ghost">Back to General Guide</a>', '<a href="/resources/mcp-promotion-playbook" class="btn-cta-ghost">Back to MCP Playbook</a>'


Set-Content -Path "c:\Users\khoadnd\Desktop\onboarding hub\resources\mcp\x-twitter-ready-to-post.html" -Value $html -Encoding UTF8
