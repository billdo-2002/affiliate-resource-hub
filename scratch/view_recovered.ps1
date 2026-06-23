$files = Get-ChildItem -Path "c:\Users\khoadnd\Desktop\onboarding hub\scratch" -Filter "recovered_*"
foreach ($file in $files) {
    Write-Output "=== $($file.Name) ==="
    Get-Content $file.FullName | Select-Object -First 10
}
