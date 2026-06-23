$lines = Get-Content "scratch\log_out.txt" -Encoding Unicode
foreach ($line in $lines) {
    if ($line -match '^STEP\s+(1[0-4]\d|\d{1,2}):') {
        Write-Output $line
    }
}
