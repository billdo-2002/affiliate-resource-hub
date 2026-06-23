$dir = "c:\Users\khoadnd\Desktop\onboarding hub"
$indexPath = Join-Path $dir "index.html"

$indexContent = Get-Content -Raw -Encoding UTF8 $indexPath

# Extract CSS
$cssPattern = '(?s)(\.mega-menu\s*\{.*?)\/\*\s*Featured MCP Card styling\s*\*\/'
if ($indexContent -match $cssPattern) {
    $cssBlock = $matches[1]
} else {
    Write-Host "CSS not found"
    exit 1
}

# Extract HTML
$htmlPattern = '(?s)(<div class="mega-menu">.*?)(?=\s*</div>\s*</div>\s*</nav>)'
if ($indexContent -match $htmlPattern) {
    $htmlBlock = $matches[1]
} else {
    Write-Host "HTML not found"
    exit 1
}

$files = Get-ChildItem -Path $dir -Recurse -Filter "*.html" | Where-Object { $_.Name -ne "index.html" }

$count = 0
foreach ($file in $files) {
    $content = Get-Content -Raw -Encoding UTF8 $file.FullName
    
    $newContent = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)\.mega-menu\s*\{.*?\/\*\s*Featured MCP Card styling\s*\*\/', $cssBlock.Replace('$', '$$') + '/* Featured MCP Card styling */')
    $newContent = [System.Text.RegularExpressions.Regex]::Replace($newContent, '(?s)<div class="mega-menu">.*?(?=\s*</div>\s*</div>\s*</nav>)', $htmlBlock.Replace('$', '$$'))
    
    if ($newContent -ne $content) {
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
        Write-Host ("Updated: " + $file.FullName)
        $count++
    }
}
Write-Host ("Successfully updated " + $count + " files.")
