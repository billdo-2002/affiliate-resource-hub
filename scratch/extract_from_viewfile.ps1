Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Text;

public class ViewFileExtractor {
    public static void Extract(string logFile, string outDir) {
        var lines = File.ReadAllLines(logFile, Encoding.UTF8);
        Console.WriteLine("Total lines: " + lines.Length);
        
        var targetFiles = new string[] {
            "discord-blueprint.html",
            "tiktok-youtube-shorts.html",
            "general-guide.html",
            "scale-safely-with-margins.html",
            "stop-losing-30-profit.html",
            "track-profit-like-a-pro.html",
            "reddit-ready-to-post.html",
            "short-form-video-guidelines.html",
            "x-twitter-ready-to-post.html"
        };
        
        var bestContent = new System.Collections.Generic.Dictionary<string, string>();
        int stepIdx = 0;
        
        foreach (var line in lines) {
            stepIdx++;
            // VIEW_FILE or WRITE_FILE steps have content field with the file content
            if (!line.Contains("VIEW_FILE") && !line.Contains("view_file")) continue;
            
            foreach (var tf in targetFiles) {
                if (!line.Contains(tf)) continue;
                
                // Find content field
                int contentIdx = line.IndexOf("\"content\":\"");
                if (contentIdx < 0) continue;
                
                int startIdx = contentIdx + "\"content\":\"".Length;
                var sb = new StringBuilder();
                int i = startIdx;
                while (i < line.Length) {
                    char c = line[i];
                    if (c == '\\' && i + 1 < line.Length) {
                        char next = line[i + 1];
                        if (next == '"') { sb.Append('"'); i += 2; }
                        else if (next == 'n') { sb.Append('\n'); i += 2; }
                        else if (next == 'r') { sb.Append('\r'); i += 2; }
                        else if (next == 't') { sb.Append('\t'); i += 2; }
                        else if (next == '\\') { sb.Append('\\'); i += 2; }
                        else { sb.Append(c); i++; }
                    } else if (c == '"') {
                        break;
                    } else {
                        sb.Append(c);
                        i++;
                    }
                }
                
                string extracted = sb.ToString();
                if (extracted.Contains("<!DOCTYPE html>") && extracted.Length > 5000) {
                    if (!bestContent.ContainsKey(tf) || extracted.Length > bestContent[tf].Length) {
                        bestContent[tf] = extracted;
                        Console.WriteLine("Found VIEW_FILE for " + tf + " length=" + extracted.Length);
                    }
                }
            }
        }
        
        foreach (var kvp in bestContent) {
            string outPath = Path.Combine(outDir, kvp.Key);
            File.WriteAllText(outPath, kvp.Value, Encoding.UTF8);
            Console.WriteLine("SAVED: " + kvp.Key + " (" + kvp.Value.Length + " chars)");
        }
    }
}
"@ -Language CSharp

$logFile = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\7aa3ac27-55d6-4ed8-9355-a0f57acf21f6\.system_generated\logs\transcript.jsonl"
$outDir = "c:\Users\khoadnd\Desktop\onboarding hub\scratch\restored_pages"

if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

[ViewFileExtractor]::Extract($logFile, $outDir)
