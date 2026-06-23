# RECOVERY MANIFEST - TrueProfit Affiliate Onboarding Hub

This manifest consolidates all design tokens, layouts, CSS classes, UI behaviors, and asset mappings for the 9 missing HTML files, sourced directly from project logs, walkthroughs, and implementation plans.

---

## Global Specifications & Dependencies

- **Theme & Palette**: 
  - Emerald Green (Primary Accent): `--green: #1a7a5e;`, `--green-bright: #23c48c;`
  - Deep Navy (Text/Headers): `#1e293b;` (Slate/Navy)
  - Muted Text: `#64748b;` (Slate)
  - Background Light/Neutral: `#F8FAFC;`
- **Typography**: `Plus Jakarta Sans` (Google Fonts prelink)
- **External CSS**: `style.css` (linked relatively: `../style.css` or `../../style.css`)
- **Global Components**: Common Navbar, Mega Menu, and Footer replicated from `index.html`.

---

## 1. guides/general-guide.html

- **Original Path**: `guides/general-guide.html`
- **Layout Description**:
  - Main body split into two columns: Left (dynamic sticky TOC sidebar), Right (Article Content).
- **CSS Classes Referenced**:
  - `.container`, `.grid-layout`, `.sidebar-toc`, `.toc-link`, `.article-content`, `.hero-section`, `.tag-pill`.
- **Image/SVG Mapping**:
  - Hero image: `../images/general_hero.svg` (or equivalent general guide illustration).
  - Navigation icons under "Content Angles That Convert".
- **Special UI Behaviors**:
  - Sticky sidebar TOC tracks scroll position and highlights active section (`.toc-link.active`).
- **Dependencies**:
  - `../style.css`
  - `../app.js`

---

## 2. guides/discord-blueprint.html

- **Original Path**: `guides/discord-blueprint.html`
- **Layout Description**:
  - Standard Guide Template (dynamic sticky sidebar TOC on the left, article column on the right).
- **CSS Classes Referenced**:
  - `.sidebar-toc`, `.article-content`, `.callout-box`, `.callout-warning` (red border-left).
- **Image/SVG Mapping**:
  - Discord server channel structure graphic (e.g., SVG/PNG placeholder in `images/`).
- **Special UI Behaviors**:
  - Dynamic scroll highlighting for TOC sidebar links.
  - Callout box vertical left border with red color `#EF4444` for rules/warnings.
- **Dependencies**:
  - `../style.css`
  - `../app.js`

---

## 3. guides/tiktok-youtube-shorts.html

- **Original Path**: `guides/tiktok-youtube-shorts.html`
- **Layout Description**:
  - Split column layout with sticky TOC. Focuses on video script visualization.
- **CSS Classes Referenced**:
  - `.video-intro-line` (`white-space: nowrap;` on desktop, wrapping on mobile).
  - `.iphone-mockup-frame` (300px width, 9:16 aspect ratio, 36px rounded corners, 10px solid bezel `#1e293b`, shadow `0 20px 40px rgba(15, 23, 42, 0.15)`).
  - `.article-table` (nested inside responsive overflow wrappers, border-radius 16px, background `#EEF3F8` headers).
  - `.callout-box` with red left border `#EF4444` (for Common Mistakes).
- **Image/SVG Mapping**:
  - iPhone Video Thumbnail: Image cover inside mockup.
  - Bottom CTA Background: `../images/16.svg` (opacity 0.2 gradient overlay).
- **Special UI Behaviors**:
  - Overlay play button icon hover effects on video thumbnail inside the iPhone mockup.
- **Dependencies**:
  - `../style.css`
  - `../app.js`

---

## 4. guides/angles/track-profit-like-a-pro.html

- **Original Path**: `guides/angles/track-profit-like-a-pro.html`
- **Layout Description**:
  - Split Hero Section (desktop grid layout `1fr 500px`, gap `32px`).
  - Centered justified copy-content area.
- **CSS Classes Referenced**:
  - `.copy-post-box` (background `#F8FAFC`, border-radius 20px, padding 38px, emerald border hover state).
  - `.copy-post-btn-wrapper` (Copy button wrapper above content box aligned top-right).
  - `.copy-post-btn` (compact pill style: background `#e6fbf1`, border `#10b981`, text `#047857`).
  - `.affiliate-link-code-pill` (green background `#e6fbf1`, border `#a7f3d0`, text `#047857`).
- **Image/SVG Mapping**:
  - Hero Image: `../../images/22.svg` (max-width 500px, max-height 400px, transparent background, object-fit contain).
  - Background decoration: `../../images/10.svg`.
- **Special UI Behaviors**:
  - Click-to-copy button changes label to "Copied!" for 2 seconds using Clipboard API.
- **Dependencies**:
  - `../../style.css`
  - `../../app.js`

---

## 5. guides/angles/stop-losing-30-profit.html

- **Original Path**: `guides/angles/stop-losing-30-profit.html`
- **Layout Description**:
  - Clone of the Margins Angle layout. Desktop grid layout `1fr 480px`, gap `32px`.
- **CSS Classes Referenced**:
  - `.copy-post-box`, `.copy-post-btn`, `.article-in-post-img` (hover cursor zoom-in, smooth scaling, green border tint).
  - `.callout-box` (vertical left border `#f97316` or `#EF4444`, small dotted-circle star icon).
- **Image/SVG Mapping**:
  - Hero Image: `../../images/21.svg` (max-width 480px, max-height 380px, object-fit contain).
  - Article Image: `../../images/20.png` (with `.article-in-post-img` hover effects).
  - Background decoration: `../../images/10.svg`.
- **Special UI Behaviors**:
  - Click-to-copy trigger with dynamic status update.
  - Image magnification hover effect on `20.png`.
- **Dependencies**:
  - `../../style.css`
  - `../../app.js`

---

## 6. guides/angles/scale-safely-with-margins.html

- **Original Path**: `guides/angles/scale-safely-with-margins.html`
- **Layout Description**:
  - Foundational Angle layout. Split column Hero section, single column centered content.
- **CSS Classes Referenced**:
  - `.copy-post-box`, `.copy-post-btn-wrapper`, `.copy-post-btn`, `.callout-box` (vertical border-left `#10b981` with nested flex bullet rows starting with dotted-circle star SVGs).
- **Image/SVG Mapping**:
  - Hero Image: `../../images/23.svg` (or equivalent Angle 1 illustration).
  - Background decoration: `../../images/10.svg`.
- **Special UI Behaviors**:
  - Clipboard copy triggers temporary "Copied!" button state.
- **Dependencies**:
  - `../../style.css`
  - `../../app.js`

---

## 7. resources/mcp/x-twitter-ready-to-post.html

- **Original Path**: `resources/mcp/x-twitter-ready-to-post.html`
- **Layout Description**:
  - Resources list featuring stacked Twitter ready-to-copy threads.
- **CSS Classes Referenced**:
  - `.copy-post-box` (background `#F8FAFC`, border-radius 20px, padding 38px, font size 19px, line-height 1.8, slate `#1e293b`, `text-align: justify`).
  - `.copy-post-btn` (mint `#e6fbf1`, border `#10b981`, text `#047857`).
  - `.material-note` (centered, italic, slate `#64748b`, size 15px, margin-top 20px).
- **Image/SVG Mapping**:
  - Hero Image: `../../images/26.svg`.
  - Background decoration: `../../images/10.svg`.
- **Special UI Behaviors**:
  - Multiple distinct copy-post containers, each having an isolated Copy button in its own top-right wrapper.
- **Dependencies**:
  - `../../style.css`
  - `../../app.js`

---

## 8. resources/mcp/reddit-ready-to-post.html

- **Original Path**: `resources/mcp/reddit-ready-to-post.html`
- **Layout Description**:
  - Resources list format for Reddit threads with no bolded text in the positioning rules lists.
- **CSS Classes Referenced**:
  - `.copy-post-box` (text-align justify, 19px desktop font, hover emerald border-glow).
  - `.copy-post-btn-wrapper`, `.copy-post-btn`.
- **Image/SVG Mapping**:
  - Hero Image: `../../images/27.svg` (responsive max width 600px).
  - Background decoration: `../../images/10.svg`.
- **Special UI Behaviors**:
  - Isolated click-to-copy triggers for each Reddit post container.
- **Dependencies**:
  - `../../style.css`
  - `../../app.js`

---

## 9. resources/mcp/short-form-video-guidelines.html

- **Original Path**: `resources/mcp/short-form-video-guidelines.html`
- **Layout Description**:
  - Adapted from `tiktok-youtube-shorts.html`. Two columns with sticky sidebar.
- **CSS Classes Referenced**:
  - `.hook-visual-panel` (staggered layouts).
  - `.article-table` (nested in overflow borders).
- **Image/SVG Mapping**:
  - Hero Image: `../../images/28.svg` (max width 550px, drop shadow).
  - Bottom CTA Background: `../../images/16.svg` (gradient overlay with 0.2 opacity).
- **Special UI Behaviors**:
  - Interactive table scrolling and responsive accordion-like panels.
- **Dependencies**:
  - `../../style.css`
  - `../../app.js`
