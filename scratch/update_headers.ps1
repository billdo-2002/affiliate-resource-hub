$rootDir = Resolve-Path (Join-Path $PSScriptRoot "..")
$masterFile = Join-Path $rootDir "mcp-promotion.html"

# Read master header
$masterContent = [System.IO.File]::ReadAllText($masterFile)
$headerRegex = [regex]'(?i)<header\b[\s\S]*?id="header"[\s\S]*?</header>'
$headerMatch = $headerRegex.Match($masterContent)

if (-not $headerMatch.Success) {
    Write-Error "Could not find <header> in master file!"
    exit 1
}

$masterHeader = $headerMatch.Value

# List of HTML files
$htmlFiles = @(
    "guides.html",
    "index.html",
    "mcp-promotion.html",
    "guides/discord-blueprint.html",
    "guides/general-guide.html",
    "guides/tiktok-youtube-shorts.html",
    "guides/angles/scale-safely-with-margins.html",
    "guides/angles/stop-losing-30-profit.html",
    "guides/angles/track-profit-like-a-pro.html",
    "resources/mcp/reddit-ready-to-post.html",
    "resources/mcp/short-form-video-guidelines.html",
    "resources/mcp/x-twitter-ready-to-post.html"
)

foreach ($relPath in $htmlFiles) {
    $filePath = Join-Path $rootDir $relPath
    if (-not (Test-Path $filePath)) {
        Write-Warning "File does not exist: $relPath"
        continue
    }

    # Calculate depth
    $normalizedRel = $relPath.Replace("\", "/")
    $parts = $normalizedRel.Split("/")
    $depth = $parts.Length - 1
    $prefix = ""
    if ($depth -gt 0) {
        $prefix = "../" * $depth
    }

    Write-Host "Processing: $relPath (depth: $depth, prefix: `"$prefix`")"

    # Adapt the header template for this file
    $adaptedHeader = $masterHeader

    # Replace links in the header
    $linksToReplace = @(
        "index.html",
        "logo.svg",
        "guides.html",
        "mcp-promotion.html",
        "guides/general-guide.html",
        "guides/discord-blueprint.html",
        "guides/tiktok-youtube-shorts.html",
        "guides/angles/track-profit-like-a-pro.html",
        "guides/angles/scale-safely-with-margins.html",
        "guides/angles/stop-losing-30-profit.html",
        "resources/mcp/x-twitter-ready-to-post.html",
        "resources/mcp/reddit-ready-to-post.html",
        "resources/mcp/short-form-video-guidelines.html",
        "22.svg",
        "19.svg",
        "21.svg"
    )

    # Apply relative prefix to HTML and asset links
    foreach ($link in $linksToReplace) {
        $escapedLink = [regex]::Escape($link)
        $hrefRegex = [regex]("href=`"$escapedLink`"")
        $srcRegex = [regex]("src=`"$escapedLink`"")
        
        $adaptedHeader = $hrefRegex.Replace($adaptedHeader, "href=`"$prefix$link`"")
        $adaptedHeader = $srcRegex.Replace($adaptedHeader, "src=`"$prefix$link`"")
    }

    # Adapt the anchor navigation links
    $isTargetForLocalAnchors = ($relPath -eq "index.html" -or $relPath -eq "mcp-promotion.html")
    $anchorLinks = @(
        "#section-start",
        "#section-who",
        "#commission",
        "#section-opportunity",
        "#dashboard-setup"
    )

    foreach ($anchor in $anchorLinks) {
        $escapedAnchor = [regex]::Escape($anchor)
        $regex = [regex]("href=`"$escapedAnchor`"")
        if ($isTargetForLocalAnchors) {
            # Keep local scroll anchor
            $adaptedHeader = $regex.Replace($adaptedHeader, "href=`"$anchor`"")
        } else {
            # Point to index.html#anchor with proper prefix
            $adaptedHeader = $regex.Replace($adaptedHeader, "href=`"$prefix`index.html$anchor`"")
        }
    }

    # Resources dropdown trigger logic
    $adaptedHeader = $adaptedHeader -replace 'href="#resources"(\s+class="nav-dropdown-trigger")', "href=`"${prefix}guides.html`"$1"

    # Read destination content
    $destContent = [System.IO.File]::ReadAllText($filePath)

    # Replace header
    if ($destContent -match '(?i)<header\b[\s\S]*?id="header"[\s\S]*?</header>') {
        $destContent = $headerRegex.Replace($destContent, $adaptedHeader)
        [System.IO.File]::WriteAllText($filePath, $destContent)
        Write-Host "  Successfully updated header for $relPath" -ForegroundColor Green
    } else {
        Write-Error "  Error: Could not find <header> tag in $relPath"
    }
}

Write-Host "Header update completed!" -ForegroundColor Green
