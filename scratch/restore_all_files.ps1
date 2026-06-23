$brainDir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain"
$subdirs = Get-ChildItem -Path $brainDir -Directory

# We want to find the files:
# 1. guides/discord-blueprint.html
# 2. guides/general-guide.html
# 3. guides/tiktok-youtube-shorts.html
# 4. guides/angles/scale-safely-with-margins.html
# 5. guides/angles/stop-losing-30-profit.html
# 6. guides/angles/track-profit-like-a-pro.html
# 7. resources/mcp/reddit-ready-to-post.html
# 8. resources/mcp/short-form-video-guidelines.html
# 9. resources/mcp/x-twitter-ready-to-post.html

$targets = @(
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

# We will search in reverse chronological order (or just check all transcripts)
# to find the most recent write_to_file call for each target
$foundFiles = @{}

foreach ($dir in $subdirs) {
    $logFile = Join-Path $dir.FullName ".system_generated\logs\transcript.jsonl"
    if (Test-Path $logFile) {
        $lines = Get-Content $logFile
        foreach ($line in $lines) {
            if ($line.Trim() -eq "") { continue }
            try {
                $obj = ConvertFrom-Json $line
                if ($obj.tool_calls) {
                    foreach ($tc in $obj.tool_calls) {
                        if ($tc.name -eq "write_to_file") {
                            $targetFile = $tc.args.TargetFile
                            $codeContent = $tc.args.CodeContent
                            if ($targetFile -and $codeContent) {
                                # Print all write_to_file paths for debugging
                                if ($targetFile -match "guides" -or $targetFile -match "resources") {
                                    Write-Host "Found write: $targetFile (Length: $($codeContent.Length))"
                                }
                                # Normalize path to relative path
                                $rel = $targetFile.ToLower().Replace("c:\users\khoadnd\desktop\onboarding hub\", "").Replace("c:/users/khoadnd/desktop/onboarding hub/", "").Replace("\", "/")
                                $normalizedTargets = $targets | ForEach-Object { $_.ToLower() }
                                if ($normalizedTargets -contains $rel) {
                                    Write-Host "MATCHED TARGET: $rel" -ForegroundColor Green
                                    $foundFiles[$rel] = $codeContent
                                }
                            }
                        }
                    }
                }
            } catch {
                # Ignore json error
            }
        }
    }
}

# Now write them back!
$destRoot = "c:\Users\khoadnd\Desktop\onboarding hub"
foreach ($key in $foundFiles.Keys) {
    $destPath = Join-Path $destRoot $key
    $destDir = Split-Path $destPath -Parent
    if (!(Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }
    [System.IO.File]::WriteAllText($destPath, $foundFiles[$key])
    Write-Host "Successfully restored: $key" -ForegroundColor Green
}
