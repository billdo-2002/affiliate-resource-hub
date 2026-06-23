$content = [System.IO.File]::ReadAllText("c:\Users\khoadnd\Desktop\onboarding hub\latest_tail.txt")
$sz = $content.Length
Write-Output "Total size: $sz"
if ($content.Contains("<!DOCTYPE html>")) { Write-Output "Contains DOCTYPE" } else { Write-Output "No DOCTYPE found" }
if ($content.Contains("discord-blueprint")) { Write-Output "Contains discord-blueprint" }
if ($content.Contains("tiktok-youtube-shorts")) { Write-Output "Contains tiktok-youtube-shorts" }
if ($content.Contains("general-guide.html")) { Write-Output "Contains general-guide.html" }
if ($content.Contains("scale-safely-with-margins")) { Write-Output "Contains scale-safely-with-margins" }
if ($content.Contains("track-profit-like-a-pro")) { Write-Output "Contains track-profit-like-a-pro" }
if ($content.Contains("reddit-ready-to-post")) { Write-Output "Contains reddit-ready-to-post" }
