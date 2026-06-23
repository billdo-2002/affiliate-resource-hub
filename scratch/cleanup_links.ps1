$rootDir = Resolve-Path (Join-Path $PSScriptRoot "..")

# 1. Clean up guides.html
$guidesPath = Join-Path $rootDir "guides.html"
if (Test-Path $guidesPath) {
    $content = [System.IO.File]::ReadAllText($guidesPath)
    $content = $content -replace '\.\./\.\./\.\./\.\./\.\./', ''
    [System.IO.File]::WriteAllText($guidesPath, $content)
    Write-Host "Cleaned up guides.html" -ForegroundColor Green
}

# 2. Clean up mcp-promotion.html
$mcpPath = Join-Path $rootDir "mcp-promotion.html"
if (Test-Path $mcpPath) {
    $content = [System.IO.File]::ReadAllText($mcpPath)
    $content = $content -replace '\.\./\.\./\.\./\.\./\.\./', ''
    [System.IO.File]::WriteAllText($mcpPath, $content)
    Write-Host "Cleaned up mcp-promotion.html" -ForegroundColor Green
}

# 3. Clean up resources/mcp/x-twitter-ready-to-post.html
$twitterPath = Join-Path $rootDir "resources/mcp/x-twitter-ready-to-post.html"
if (Test-Path $twitterPath) {
    $content = [System.IO.File]::ReadAllText($twitterPath)
    # Fix the long relative path
    $content = $content -replace '\.\./\.\./\.\./\.\./\.\./\.\./\.\./', '../../'
    # Fix the absolute-style links in breadcrumb and CTAs
    $content = $content -replace 'href="/resources\.html"', 'href="../../guides.html"'
    $content = $content -replace 'href="/resources/mcp-promotion-playbook"', 'href="../../mcp-promotion.html"'
    [System.IO.File]::WriteAllText($twitterPath, $content)
    Write-Host "Cleaned up x-twitter-ready-to-post.html" -ForegroundColor Green
}
