$logFile = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\7aa3ac27-55d6-4ed8-9355-a0f57acf21f6\.system_generated\logs\transcript.jsonl"
$outDir = "c:\Users\khoadnd\Desktop\onboarding hub\scratch\restored_pages"

if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

# Target steps for initial write_to_file (full HTML)
$targetSteps = @{
    2861 = "discord-blueprint.html"
    2954 = "tiktok-youtube-shorts.html"
}

$lines = [System.IO.File]::ReadAllLines($logFile)
Write-Output "Scanning $($lines.Count) lines..."

foreach ($line in $lines) {
    if ($line.Trim() -eq "") { continue }
    try {
        $obj = ConvertFrom-Json $line
        $stepIndex = $obj.step_index
        if ($targetSteps.ContainsKey($stepIndex)) {
            Write-Output "Found step $stepIndex"
            if ($obj.tool_calls) {
                foreach ($tc in $obj.tool_calls) {
                    if ($tc.name -eq "write_to_file") {
                        $cc = $tc.args.CodeContent
                        if ($cc) {
                            $filename = $targetSteps[$stepIndex]
                            $outPath = Join-Path $outDir $filename
                            [System.IO.File]::WriteAllText($outPath, $cc)
                            Write-Output "SAVED: $filename (length=$($cc.Length))"
                        }
                    }
                }
            }
        }
    } catch {}
}
Write-Output "Done."
