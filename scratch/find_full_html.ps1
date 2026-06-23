$files = Get-ChildItem -Path "c:\Users\khoadnd\Desktop\onboarding hub\scratch" -File
foreach ($file in $files) {
    if ($file.Length -gt 10000) { # larger than 10KB
        $content = Get-Content $file.FullName -Raw
        if ($content -match "<!DOCTYPE html>") {
            Write-Output "$($file.Name) | $($file.Length)"
        }
    }
}
