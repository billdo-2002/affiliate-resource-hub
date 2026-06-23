$brainDir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain"
$targets = @("discord-blueprint", "tiktok-youtube-shorts")

Get-ChildItem -Path $brainDir -Filter "transcript.jsonl" -Recurse -ErrorAction SilentlyContinue | ForEach-Object {
    $logFile = $_.FullName
    $lines = Get-Content $logFile
    foreach ($line in $lines) {
        if ($line.Trim() -eq "") { continue }
        try {
            $obj = ConvertFrom-Json $line
            if ($obj.content) {
                $c = $obj.content
                if ($c.Contains("<!DOCTYPE html>")) {
                    foreach ($t in $targets) {
                        if ($c.Contains($t)) {
                            Write-Output ("FOUND FULL HTML IN CONTENT: Target=" + $t + " | StepIndex=" + $obj.step_index + " | Type=" + $obj.type + " | Length=" + $c.Length + " | Log=" + $logFile)
                        }
                    }
                }
            }
        } catch {}
    }
}
