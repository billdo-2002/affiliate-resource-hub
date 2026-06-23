$logFiles = @(
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\7aa3ac27-55d6-4ed8-9355-a0f57acf21f6\.system_generated\tasks\task-246.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\97797bfe-2863-4a57-adac-9191425d5dd1\.system_generated\tasks\task-306.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\fa71a2a9-c0c1-4047-ba07-1f660674bc66\.system_generated\tasks\task-204.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\ca9e0b9e-a40e-4400-88c1-7468f0dc096c\.system_generated\tasks\task-254.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\ca9e0b9e-a40e-4400-88c1-7468f0dc096c\.system_generated\tasks\task-229.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\ca9e0b9e-a40e-4400-88c1-7468f0dc096c\.system_generated\tasks\task-186.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\b2844f29-72f5-4036-b247-e50bf3687ab6\.system_generated\tasks\task-125.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\be22a2d3-01ed-4d2c-a9ec-f93837c35ac5\.system_generated\tasks\task-131.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\ca9e0b9e-a40e-4400-88c1-7468f0dc096c\.system_generated\tasks\task-109.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\be22a2d3-01ed-4d2c-a9ec-f93837c35ac5\.system_generated\tasks\task-171.log",
  "C:\Users\khoadnd\.gemini\antigravity-ide\brain\97797bfe-2863-4a57-adac-9191425d5dd1\.system_generated\tasks\task-308.log"
)

$targets = @("discord-blueprint", "tiktok-youtube-shorts", "scale-safely-with-margins", "stop-losing-30-profit", "track-profit-like-a-pro", "reddit-ready-to-post", "short-form-video-guidelines", "x-twitter-ready-to-post")

foreach ($f in $logFiles) {
  $c = [System.IO.File]::ReadAllText($f)
  $sz = $c.Length
  $hits = @()
  foreach ($t in $targets) {
    if ($c.Contains($t)) { $hits += $t }
  }
  if ($hits.Count -gt 0) {
    $fname = ($f -split "\\")[-1]
    $session = ($f -split "\\")[-4]
    Write-Output ($session + "/" + $fname + " size=" + $sz + " hits=" + ($hits -join ","))
  }
}
