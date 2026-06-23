$rootDir = Resolve-Path (Join-Path $PSScriptRoot "..")

# All HTML files we want to process
$htmlFiles = Get-ChildItem -Path $rootDir -Filter "*.html" -Recurse | Where-Object { $_.FullName -notmatch '\.bak$' }

# Map of canonical root-relative paths for all our HTML pages
$knownPages = @{
    "index" = "index.html"
    "index.html" = "index.html"
    "guides" = "guides.html"
    "guides.html" = "guides.html"
    "mcp-promotion" = "mcp-promotion.html"
    "mcp-promotion.html" = "mcp-promotion.html"
    "guides/general-guide" = "guides/general-guide.html"
    "guides/general-guide.html" = "guides/general-guide.html"
    "guides/discord-blueprint" = "guides/discord-blueprint.html"
    "guides/discord-blueprint.html" = "guides/discord-blueprint.html"
    "guides/tiktok-youtube-shorts" = "guides/tiktok-youtube-shorts.html"
    "guides/tiktok-youtube-shorts.html" = "guides/tiktok-youtube-shorts.html"
    "guides/angles/track-profit-like-a-pro" = "guides/angles/track-profit-like-a-pro.html"
    "guides/angles/track-profit-like-a-pro.html" = "guides/angles/track-profit-like-a-pro.html"
    "guides/angles/scale-safely-with-margins" = "guides/angles/scale-safely-with-margins.html"
    "guides/angles/scale-safely-with-margins.html" = "guides/angles/scale-safely-with-margins.html"
    "guides/angles/stop-losing-30-profit" = "guides/angles/stop-losing-30-profit.html"
    "guides/angles/stop-losing-30-profit.html" = "guides/angles/stop-losing-30-profit.html"
    "resources/mcp/reddit-ready-to-post" = "resources/mcp/reddit-ready-to-post.html"
    "resources/mcp/reddit-ready-to-post.html" = "resources/mcp/reddit-ready-to-post.html"
    "resources/mcp/short-form-video-guidelines" = "resources/mcp/short-form-video-guidelines.html"
    "resources/mcp/short-form-video-guidelines.html" = "resources/mcp/short-form-video-guidelines.html"
    "resources/mcp/x-twitter-ready-to-post" = "resources/mcp/x-twitter-ready-to-post.html"
    "resources/mcp/x-twitter-ready-to-post.html" = "resources/mcp/x-twitter-ready-to-post.html"
}

# Helper to resolve a relative path to a root-relative path
function Get-RootRelativePath($currentRelDir, $link) {
    # If it has a leading slash, treat it as root-relative
    if ($link.StartsWith("/")) {
        return $link.TrimStart("/")
    }

    try {
        # Otherwise, combine current file's directory with the link
        $combined = Join-Path $currentRelDir $link
        # Normalize paths (resolve ..)
        $normalized = [System.IO.Path]::GetFullPath((Join-Path $rootDir $combined))
        $rootFullPath = [System.IO.Path]::GetFullPath($rootDir)

        # Make it relative to root again
        if ($normalized.StartsWith($rootFullPath)) {
            $result = $normalized.Substring($rootFullPath.Length).Replace("\", "/").TrimStart("/")
            return $result
        }
    } catch {
        # Ignore invalid path formats
    }
    return $null
}

# Helper to compute a relative path from current depth to target root-relative path
function Get-RelativePath($currentDepth, $targetRootRel) {
    $prefix = ""
    if ($currentDepth -gt 0) {
        $prefix = "../" * $currentDepth
    }
    return "$prefix$targetRootRel"
}

foreach ($file in $htmlFiles) {
    # Get relative path of this file to rootDir
    $rootPath = $rootDir.Path
    $fileSubPath = $file.FullName.Replace($rootPath, "").Replace("\", "/").TrimStart("/")
    $fileDir = ""
    if ($fileSubPath.Contains("/")) {
        $fileDir = $fileSubPath.Substring(0, $fileSubPath.LastIndexOf("/"))
    }
    
    # Calculate depth
    $parts = $fileSubPath.Split("/")
    $depth = $parts.Length - 1

    Write-Host "File: $fileSubPath (depth: $depth, dir: `"$fileDir`")" -ForegroundColor Cyan

    $content = [System.IO.File]::ReadAllText($file.FullName)
    $modified = $false

    # Regex to match href="..."
    $hrefRegex = [regex]'href="([^"]+)"'
    $hrefMatches = $hrefRegex.Matches($content)

    # We need to process matches in reverse order so replacements don't offset index positions
    for ($i = $hrefMatches.Count - 1; $i -ge 0; $i--) {
        $m = $hrefMatches[$i]
        $originalHref = $m.Groups[1].Value

        # Skip external protocols, mailto, javascript, data, anchor-only links
        if ($originalHref -match '^([a-zA-Z]+:|#)') {
            continue
        }

        # Extract anchor if present
        $anchor = ""
        $baseHref = $originalHref
        if ($originalHref -match '#(.*)$') {
            $anchor = "#" + $Matches[1]
            $baseHref = $originalHref -replace '#.*$', ''
        }

        if ([string]::IsNullOrEmpty($baseHref)) {
            continue
        }

        # Resolve the link to a root-relative path
        $rootRelPath = Get-RootRelativePath $fileDir $baseHref
        if ($null -eq $rootRelPath) {
            continue
        }

        # Check if the resolved path matches one of our known pages
        # Also try checking if we append .html or check without it
        $matchedKey = $null
        if ($knownPages.ContainsKey($rootRelPath)) {
            $matchedKey = $rootRelPath
        } elseif ($knownPages.ContainsKey("$rootRelPath.html")) {
            $matchedKey = "$rootRelPath.html"
        } else {
            # Try matching filename only if it's in the same directory
            $fileName = [System.IO.Path]::GetFileName($rootRelPath)
            $dirName = [System.IO.Path]::GetDirectoryName($rootRelPath).Replace("\", "/")
            if ($knownPages.ContainsKey("$fileDir/$fileName")) {
                $matchedKey = "$fileDir/$fileName"
            } elseif ($knownPages.ContainsKey("$fileDir/$fileName.html")) {
                $matchedKey = "$fileDir/$fileName.html"
            }
        }

        if ($matchedKey) {
            $canonicalTarget = $knownPages[$matchedKey]
            $newRelativeHref = (Get-RelativePath $depth $canonicalTarget) + $anchor

            if ($originalHref -ne $newRelativeHref) {
                Write-Host "  Replacing: '$originalHref' -> '$newRelativeHref'" -ForegroundColor Yellow
                
                # Replace this specific match using index and length
                $startIndex = $m.Groups[1].Index
                $length = $m.Groups[1].Length
                $content = $content.Remove($startIndex, $length).Insert($startIndex, $newRelativeHref)
                $modified = $true
            }
        }
    }

    if ($modified) {
        [System.IO.File]::WriteAllText($file.FullName, $content)
        Write-Host "  Saved changes for $fileSubPath" -ForegroundColor Green
    }
}

Write-Host "All links successfully linked!" -ForegroundColor Green
