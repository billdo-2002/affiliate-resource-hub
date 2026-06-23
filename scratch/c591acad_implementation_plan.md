# Goal Description

Build a new standalone HTML page `mcp-promotion.html`. This page acts as a subpage of the Affiliate Resource Hub, specifically designed to promote the new TrueProfit MCP (Model Context Protocol) feature. It must match the homepage design system, feature rich animations, smooth transitions, and a premium SaaS aesthetic.

## User Review Required

Please review the proposed structure and animations. Let me know if you would prefer the file to be named `guides/mcp-promotion-playbook.html` to match the existing megamenu link on the homepage, or if `mcp-promotion.html` in the root directory is exactly what you want. 

## Proposed Changes

### Root Directory

#### [NEW] [mcp-promotion.html](file:///c:/Users/khoadnd/Desktop/onboarding%20hub/mcp-promotion.html)

This file will contain the following:
1.  **Head & Styles:** Copying the `<head>` and global `<style>` from `index.html` to ensure the exact same fonts, variables, and global utilities are used. Adding specific animations requested (fade in, stagger, hover micro-interactions, pulse, ribbon oscillation).
2.  **Header & Navbar:** Exactly matching the homepage, including the megamenu.
3.  **Section 1 — Hero (Dark):** Top badge, headline, subtitle, CTAs, hero visual placeholder, ribbon background, and dotted grid.
4.  **Section 2 — What is TrueProfit MCP? (Light):** 2x2 grid of value cards.
5.  **Section 3 — Why Promote It Now? (Dark):** 3 stat cards in a row.
6.  **Section 4 — Promotion Toolkit (Light):** 3 large stacked cards with thumbnail placeholders.
7.  **Section 5 — How to Talk About MCP (Dark):** 2-column Do/Don't list with a tip box below.
8.  **Section 6 — CTA Block (Dark):** Match the CTA style from the homepage.
9.  **Footer:** Exactly matching the homepage footer.
10. **Scripts:** Intersection Observer logic for scroll animations (`.scroll-animate`), CountUp logic for stats, and navbar toggle scripts.

## Verification Plan

### Manual Verification
- Open `mcp-promotion.html` in the browser to visually verify the premium SaaS feel and dark/light section alternations.
- Check that all entrance and scroll animations trigger correctly and only once.
- Verify that hover states work smoothly.
- Ensure that links point to the correct URLs with `target="_blank"` where specified.
