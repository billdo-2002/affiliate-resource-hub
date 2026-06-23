const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '..');
const masterFile = path.join(rootDir, 'mcp-promotion.html');

// Read master header
const masterContent = fs.readFileSync(masterFile, 'utf8');
const headerRegex = /<header id="header"[\s\S]*?<\/header>/i;
const headerMatch = masterContent.match(headerRegex);

if (!headerMatch) {
  console.error("Could not find <header> in master file!");
  process.exit(1);
}

const masterHeader = headerMatch[0];

// List of HTML files
const htmlFiles = [
  'guides.html',
  'index.html',
  'mcp-promotion.html',
  'guides/discord-blueprint.html',
  'guides/general-guide.html',
  'guides/tiktok-youtube-shorts.html',
  'guides/angles/scale-safely-with-margins.html',
  'guides/angles/stop-losing-30-profit.html',
  'guides/angles/track-profit-like-a-pro.html',
  'resources/mcp/reddit-ready-to-post.html',
  'resources/mcp/short-form-video-guidelines.html',
  'resources/mcp/x-twitter-ready-to-post.html'
];

htmlFiles.forEach(relPath => {
  const filePath = path.join(rootDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.warn(`File does not exist: ${relPath}`);
    return;
  }

  // Calculate depth
  const normalizedRel = path.normalize(relPath).replace(/\\/g, '/');
  const parts = normalizedRel.split('/');
  const depth = parts.length - 1;
  const prefix = depth > 0 ? '../'.repeat(depth) : '';

  console.log(`Processing: ${relPath} (depth: ${depth}, prefix: "${prefix}")`);

  // Adapt the header template for this file
  let adaptedHeader = masterHeader;

  // Replace links in the header
  const linksToReplace = [
    'index.html',
    'logo.svg',
    'guides.html',
    'mcp-promotion.html',
    'guides/general-guide.html',
    'guides/discord-blueprint.html',
    'guides/tiktok-youtube-shorts.html',
    'guides/angles/track-profit-like-a-pro.html',
    'guides/angles/scale-safely-with-margins.html',
    'guides/angles/stop-losing-30-profit.html',
    'resources/mcp/x-twitter-ready-to-post.html',
    'resources/mcp/reddit-ready-to-post.html',
    'resources/mcp/short-form-video-guidelines.html',
    '22.svg',
    '19.svg',
    '21.svg'
  ];

  // Apply relative prefix to HTML and asset links
  linksToReplace.forEach(link => {
    // Match exact href="link" or src="link"
    const escapedLink = link.replace(/\//g, '\\/').replace(/\./g, '\\.');
    const hrefRegex = new RegExp(`href="${escapedLink}"`, 'g');
    const srcRegex = new RegExp(`src="${escapedLink}"`, 'g');
    
    adaptedHeader = adaptedHeader.replace(hrefRegex, `href="${prefix}${link}"`);
    adaptedHeader = adaptedHeader.replace(srcRegex, `src="${prefix}${link}"`);
  });

  // Adapt the anchor navigation links
  const isTargetForLocalAnchors = (relPath === 'index.html' || relPath === 'mcp-promotion.html');
  const anchorLinks = [
    '#section-start',
    '#section-who',
    '#commission',
    '#section-opportunity',
    '#dashboard-setup'
  ];

  anchorLinks.forEach(anchor => {
    // In master file, they are href="#anchor"
    const regex = new RegExp(`href="${anchor}"`, 'g');
    if (isTargetForLocalAnchors) {
      // Keep local scroll anchor
      adaptedHeader = adaptedHeader.replace(regex, `href="${anchor}"`);
    } else {
      // Point to index.html#anchor with proper prefix
      adaptedHeader = adaptedHeader.replace(regex, `href="${prefix}index.html${anchor}"`);
    }
  });

  // Resources dropdown trigger logic:
  // In index.html, guides.html and subpages, Resources links to guides.html
  // Let's replace the resources trigger href
  adaptedHeader = adaptedHeader.replace(/href="#resources"(\s+class="nav-dropdown-trigger")/g, `href="${prefix}guides.html"$1`);

  // Read destination content
  let destContent = fs.readFileSync(filePath, 'utf8');

  // Replace header
  if (headerRegex.test(destContent)) {
    destContent = destContent.replace(headerRegex, adaptedHeader);
    fs.writeFileSync(filePath, destContent, 'utf8');
    console.log(`  Successfully updated header for ${relPath}`);
  } else {
    console.error(`  Error: Could not find <header> tag in ${relPath}`);
  }
});

console.log("Header update completed!");
