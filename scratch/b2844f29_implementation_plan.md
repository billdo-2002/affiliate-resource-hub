# Implementation Plan — Create "Stop Losing 30% Profit" Angle Page

Create a new page `/guides/angles/stop-losing-30-profit.html` exactly matching the layout and responsive behavior of `/guides/angles/scale-safely-with-margins.html`.

## Open Questions

> [!IMPORTANT]
> **Missing Content:** In your request, you included the placeholder `[PASTE EXACT ANGLE 3 CONTENT HERE]` instead of pasting the actual Angle 3 text. Please provide the exact word-for-word text for Angle 3 (Why does this happen, How to pitch TrueProfit, Example Content) so I can add it to the page.

## Proposed Changes

### [guides/angles/stop-losing-30-profit.html](file:///c:/Users/khoadnd/Desktop/onboarding%20hub/guides/angles/stop-losing-30-profit.html)

#### [NEW] `stop-losing-30-profit.html`
- Create this file by making an exact copy of `scale-safely-with-margins.html`.
- **Page Identity Updates**:
  - Update `<title>` to: `Stop Losing 30% Profit — TrueProfit`
  - Update Breadcrumb: `Home › Guides › General Affiliate Guide › Stop Losing 30% Profit`
- **Hero Section**:
  - Title: `Stop Losing 30% Profit`
  - Subtitle: `A ready-to-post content angle that helps merchants understand how hidden costs can quietly reduce their actual profit.`
  - Tags: `Content Angle`, `Ready-to-Post`, `Hidden Costs`, `Profit Leak`
  - Illustration: Update image source to `/assets/guides/angle-stop-losing-profit-hero.svg`
- **Sidebar**:
  - Summary Card: Update text to `Stop Losing 30% Profit`
- **Article Content**:
  - Replace the 3 sections with the provided Angle 3 content (once you provide it).
  - Apply the exact same formatting rules: `.article-example-block` container for the example content, no italics, keep `[place your aff link here]` styled as emerald code.
- **In-Article Image**:
  - Insert `../../20.svg` (or `20.png`/etc as appropriate) exactly where referenced in the text.
  - Apply the requested styles:
    ```css
    width: 100%;
    max-width: 920px;
    height: auto;
    border-radius: 20px;
    border: 1px solid rgba(15, 23, 42, 0.10);
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.10);
    margin: 32px 0 40px;
    object-fit: contain;
    transition: all 250ms ease;
    cursor: zoom-in;
    ```
    And hover styles:
    ```css
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 24px 60px rgba(15, 23, 42, 0.15); /* Stronger shadow */
    border-color: rgba(16, 185, 129, 0.45);
    ```
- **Related Section**:
  - Rename eyebrow to `MORE CONTENT ANGLES`
  - Heading: `Continue with another ready-to-post angle`
  - Description: `Explore another angle you can adapt for your own content and audience.`
  - Card 1: `Track Profit Like A Pro`
  - Card 2: `Scale Safely With Margins`

## Verification Plan

### Manual Verification
- Render the newly created file in the browser to ensure the layout identically matches the template.
- Check that the in-article image hover effect works as prescribed.
- Verify that there are no leftover references to Angle 2 or its old hero image.
