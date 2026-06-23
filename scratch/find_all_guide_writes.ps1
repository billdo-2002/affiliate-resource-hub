$logFile = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\7aa3ac27-55d6-4ed8-9355-a0f57acf21f6\.system_generated\logs\transcript.jsonl"

$lines = [System.IO.File]::ReadAllLines($logFile)
Write-Output "Total lines: $($lines.Count)"

foreach ($line in $lines) {
    if ($line.Trim() -eq "") { continue }
    try {
        $obj = ConvertFrom-Json $line
        if ($obj.tool_calls) {
            foreach ($tc in $obj.tool_calls) {
                $name = $tc.name
                # Look for any file write with target file
                if ($name -eq "write_to_file" -or $name -eq "replace_file_content" -or $name -eq "multi_replace_file_content") {
                    $tf = $tc.args.TargetFile
                    if ($tf) {
                        $tf2 = $tf.ToLower()
                        if ($tf2.Contains("discord-blueprint") -or $tf2.Contains("tiktok-youtube-shorts") -or $tf2.Contains("scale-safely") -or $tf2.Contains("stop-losing") -or $tf2.Contains("track-profit") -or $tf2.Contains("reddit-ready") -or $tf2.Contains("short-form-video") -or $tf2.Contains("x-twitter-ready")) {
                            Write-Output ("FOUND: step=" + $obj.step_index + " | tool=" + $name + " | file=" + $tf)
                        }
                    }
                }
            }
        }
    } catch {}
}
