# Walkthrough — Stop Losing 30% Profit Angle Page

I've successfully created the new page `/guides/angles/stop-losing-30-profit.html` exactly as you requested!

## What was done

- **Used the `.md` playbook:** I searched through `TrueProfit Affiliate Playbook (1).md` and found the full text for Angle 3 ("Stop Losing 30% Profit").
- **Exact Layout Replication:** Copied `scale-safely-with-margins.html` over to ensure the identical layout, sidebar styling, spacing, typography, and responsive behavior.
- **Updated Content Identity:**
  - Set the Hero title to `Stop Losing 30% Profit` and subtitle to focus on hidden costs.
  - Updated the tags (`Content Angle`, `Ready-to-Post`, `Hidden Costs`, `Profit Leak`).
  - Added the exact `[Insert Your Affiliate Link]` prompt formatted in emerald.
  - Applied the `.article-example-block` so the vent post has the proper rounded styling, without the quote/italics formatting.
- **In-Article Screenshot:**
  - I found the `20.png` file, placed it right after the mention in the "Why does this happen" section.
  - Implemented the requested `.article-in-post-img` hover CSS (zoom-in cursor, scaling up smoothly with a richer shadow and green border tint).
- **Related Pages:**
  - The "Related Guides" section at the bottom now properly links to *Track Profit Like A Pro* and *Scale Safely With Margins*.
- **Hero Banner Image Replacement:**
  - Replaced the placeholder hero banner image with `21.svg` (pointing to `../../21.svg`).
  - Set styling rules to match: desktop max-width `480px` (within the requested `420-520px` range), max-height `380px`, `object-fit: contain`, transparent background, with no placeholder border/frame or shadow boxes.
  - Adjusted the grid column width of the hero section on desktop to `480px` and the gap to `32px` to prevent "Profit" from wrapping to the next line while still keeping the hero image nice and large.
- **Track Profit Like A Pro Image Replacement:**
  - Replaced the hero image in `track-profit-like-a-pro.html` with `22.svg` (pointing to `../../22.svg`).
  - Adjusted desktop layout grid (`1fr 500px`, gap `32px`) and styling (`max-width: 500px`, `max-height: 400px`, `object-fit: contain`, transparent background, no box shadow or border frame) to make the illustration larger and clearer while keeping typography readable.
- **Updated General Guide Content Angles Navigation Section:**
  - Replaced the 3 list cards under "Content Angles That Convert" in `general-guide.html`.
  - Updated titles and URLs to link directly to the standalone pages (`Track Profit Like A Pro`, `Scale Safely With Margins`, and `Stop Losing 30% Profit`).
  - Removed the `Angle #1 / #2 / #3` prefixes to present them as clean, native playbook links.
- **Updated Main Guides Page (guides.html):**
  - Updated the "High-converting angles" cards to be fully clickable block links (`<a>` elements) leading to `/guides/angles/stop-losing-30-profit`, `/guides/angles/track-profit-like-a-pro`, and `/guides/angles/scale-safely-with-margins`.
  - Replaced the Angle 2 title with `"Track Profit Like A Pro"` and Angle 1 title with `"Stop Losing 30% Profit"`.
  - Added subtle hover interactions via CSS: card/image scales/lifts up (`translateY(-5px)`, `scale(1.1)` on image), cursor pointer, title color transitions smoothly to emerald (`var(--green-bright)`).

## Next Steps

Please test the pages in your browser. Verify the new clickable cards and hover effects in `/guides`, the navigation link updates on `/guides/general-guide`, and check the updated hero banner images (`21.svg` on Stop Losing 30% Profit and `22.svg` on Track Profit Like A Pro). Let me know if you need any other adjustments!
