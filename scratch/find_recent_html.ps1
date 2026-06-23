$date = (Get-Date).AddDays(-7)
$files = Get-ChildItem -Path "C:\Users\khoadnd" -Filter "*.html" -Recurse -ErrorAction SilentlyContinue
foreach ($file in $files) {
    if ($file.LastWriteTime -gt $date) {
        Write-Output "$($file.FullName) | $($file.LastWriteTime)"
    }
}
