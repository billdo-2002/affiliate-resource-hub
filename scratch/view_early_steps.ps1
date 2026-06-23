$logPath = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\97797bfe-2863-4a57-adac-9191425d5dd1\.system_generated\logs\transcript.jsonl"
if (Test-Path $logPath) {
    $lines = Get-Content $logPath
    foreach ($line in $lines) {
        if ($line.Trim() -eq "") { continue }
        try {
            $obj = ConvertFrom-Json $line
            $step = $obj.step_index
            if ($step -lt 159) {
                if ($obj.tool_calls) {
                    foreach ($tc in $obj.tool_calls) {
                        Write-Host "STEP $($step): Tool=$($tc.name) Args=$($tc.args | Out-String -Width 120)"
                    }
                }
            }
        } catch {}
    }
}
