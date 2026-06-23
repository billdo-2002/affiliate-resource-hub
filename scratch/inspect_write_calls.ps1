$brainDir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain"
$targets = @("discord-blueprint", "tiktok-youtube-shorts", "general-guide", "scale-safely-with-margins", "stop-losing-30-profit", "track-profit-like-a-pro", "reddit-ready-to-post", "short-form-video-guidelines", "x-twitter-ready-to-post")

Get-ChildItem -Path $brainDir -Filter "transcript.jsonl" -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
    $logFile = $_.FullName
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
                            foreach ($t in $targets) {
                                if ($targetFile.ToLower().Contains($t)) {
                                    Write-Output ("FOUND WRITE: Target=" + $t + " | File=" + $targetFile + " | CodeContent Length=" + $codeContent.Length + " | Log=" + $logFile)
                                }
                            }
                        }
                    }
                }
            }
        } catch {}
    }
}
