$files = Get-ChildItem -Path "C:\Users\khoadnd" -Filter "*.bak" -Recurse -ErrorAction SilentlyContinue
foreach ($file in $files) {
    Write-Output "$($file.FullName) | $($file.Length)"
}
