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
                    if ($name -eq "run_command") {
                        $cmd = $args.CommandLine
                        Write-Host "STEP $($step): CMD: $($cmd)"
                    } elseif ($name -eq "write_to_file") {
                        $target = $args.TargetFile
                        Write-Host "STEP $($step): WRITE: $($target)"
                    } elseif ($name -eq "replace_file_content" -or $name -eq "multi_replace_file_content") {
                        $target = $args.TargetFile
                        Write-Host "STEP $($step): EDIT: $($target)"
                    }
                }
            }
        } catch {
            # Ignore parsing errors
        }
    }
} else {
    Write-Host "Log not found"
}
