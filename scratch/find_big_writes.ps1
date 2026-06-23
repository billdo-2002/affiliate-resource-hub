$logFile = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\7aa3ac27-55d6-4ed8-9355-a0f57acf21f6\.system_generated\logs\transcript.jsonl"

# Read all lines, find write_to_file tool calls for target files
$targets = @{
    "guides/discord-blueprint.html" = ""
    "guides/tiktok-youtube-shorts.html" = ""
    "guides/general-guide.html" = ""
    "guides/angles/scale-safely-with-margins.html" = ""
    "guides/angles/stop-losing-30-profit.html" = ""
    "guides/angles/track-profit-like-a-pro.html" = ""
}

$lines = [System.IO.File]::ReadAllLines($logFile)
Write-Output "Total lines: $($lines.Count)"

foreach ($line in $lines) {
    if ($line.Trim() -eq "") { continue }
    try {
        # Look for write_to_file with CodeContent
        if ($line.Contains("write_to_file") -and $line.Contains("CodeContent")) {
            $obj = ConvertFrom-Json $line
            if ($obj.tool_calls) {
                foreach ($tc in $obj.tool_calls) {
                    if ($tc.name -eq "write_to_file") {
                        $tf = $tc.args.TargetFile
                        $cc = $tc.args.CodeContent
                        if ($tf -and $cc -and $cc.Length -gt 50000) {
                            Write-Output ("BIG WRITE: step=" + $obj.step_index + " | file=" + $tf + " | length=" + $cc.Length)
                        }
                    }
                }
            }
        }
    } catch {}
}
