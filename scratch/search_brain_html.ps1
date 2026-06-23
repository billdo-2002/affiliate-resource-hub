$brainDir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain"
$targets = @("discord-blueprint", "tiktok-youtube-shorts", "general-guide", "scale-safely-with-margins", "stop-losing-30-profit", "track-profit-like-a-pro", "reddit-ready-to-post", "short-form-video-guidelines", "x-twitter-ready-to-post")
$found = @{}

Get-ChildItem -Path $brainDir -File -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
    $file = $_
    if ($file.Length -gt 10000 -and ($file.Extension -eq ".txt" -or $file.Extension -eq ".log" -or $file.Extension -eq ".jsonl" -or $file.Extension -eq ".html")) {
        try {
            $content = [System.IO.File]::ReadAllText($file.FullName)
            if ($content.Contains("<!DOCTYPE html>")) {
                foreach ($t in $targets) {
                    if ($content.Contains($t)) {
                        if (!$found.ContainsKey($t) -or $content.Length -gt $found[$t].Length) {
                            $found[$t] = @{ Path = $file.FullName; Length = $content.Length }
                        }
                    }
                }
            }
        } catch {}
    }
}

$found.Keys | ForEach-Object {
    $k = $_
    $path = $found[$k].Path
    $len = $found[$k].Length
    Write-Output ($k + " -> " + $path + " (" + $len + ")")
}
