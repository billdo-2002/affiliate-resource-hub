$logPath = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\97797bfe-2863-4a57-adac-9191425d5dd1\.system_generated\logs\transcript.jsonl"
if (Test-Path $logPath) {
    $lines = Get-Content $logPath
    foreach ($line in $lines) {
        if ($line.Trim() -eq "") { continue }
        try {
            $obj = ConvertFrom-Json $line
            $step = $obj.step_index
            if ($obj.tool_calls) {
                foreach ($tc in $obj.tool_calls) {
                    $name = $tc.name
                    $args = $tc.args
                    $target = ""
                    if ($args.TargetFile) { $target = $args.TargetFile }
                    elseif ($args.AbsolutePath) { $target = $args.AbsolutePath }
                    
                    if ($target -match "guides" -or $target -match "resources") {
                        $contentLength = 0
                        if ($args.CodeContent) { $contentLength = $args.CodeContent.Length }
                        elseif ($args.ReplacementContent) { $contentLength = $args.ReplacementContent.Length }
                        Write-Host "STEP $($step): Tool=$name Target=$target Length=$contentLength"
                    }
                }
            }
        } catch {
            # Ignore json parse error
        }
    }
} else {
    Write-Host "Log file not found at $logPath"
}
