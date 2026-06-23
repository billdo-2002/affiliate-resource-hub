$brainDir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain"
$subdirs = Get-ChildItem -Path $brainDir -Directory
foreach ($dir in $subdirs) {
    $logFile = Join-Path $dir.FullName ".system_generated\logs\transcript.jsonl"
    if (Test-Path $logFile) {
        # Check if the file contains references to writing our key files
        # We can scan the text of the log file for target files
        $content = Get-Content $logFile
        foreach ($line in $content) {
            if ($line -like "*discord-blueprint.html*" -and ($line -like "*write_to_file*" -or $line -like "*replace_file_content*" -or $line -like "*multi_replace_file_content*")) {
                Write-Output "Found in: $($dir.Name)"
                break
            }
        }
    }
}
