Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

public class TailExtractor {
    public static void Extract(string tailFile, string outDir) {
        string content = File.ReadAllText(tailFile, Encoding.UTF8);
        Console.WriteLine("File size: " + content.Length);
        
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
        
        var best = new Dictionary<string, string>();
        
        // Find all occurrences of <!DOCTYPE html> and extract forward
        int searchFrom = 0;
        while (true) {
            int docIdx = content.IndexOf("<!DOCTYPE html>", searchFrom);
            if (docIdx < 0) break;
            
            // Grab up to the next occurrence of <!DOCTYPE html> or end of a large chunk
            int nextDoc = content.IndexOf("<!DOCTYPE html>", docIdx + 100);
            int endIdx = nextDoc > 0 ? nextDoc : Math.Min(docIdx + 500000, content.Length);
            
            string chunk = content.Substring(docIdx, endIdx - docIdx);
            
            // Identify which file this belongs to - look backwards for filename
            int lookBack = Math.Max(0, docIdx - 500);
            string prefix = content.Substring(lookBack, docIdx - lookBack);
            
            foreach (var tf in targetFiles) {
                if (prefix.Contains(tf) || chunk.Contains(tf)) {
                    if (!best.ContainsKey(tf) || chunk.Length > best[tf].Length) {
                        best[tf] = chunk;
                        Console.WriteLine("Found chunk for: " + tf + " at pos=" + docIdx + " len=" + chunk.Length);
                    }
                }
            }
            
            searchFrom = docIdx + 100;
        }
        
        Console.WriteLine("\n--- SAVING ---");
        foreach (var kvp in best) {
            // Clean trailing garbage
            string html = kvp.Value;
            int closeIdx = html.LastIndexOf("</html>");
            if (closeIdx > 0) html = html.Substring(0, closeIdx + 7);
            
            string outPath = Path.Combine(outDir, kvp.Key);
            File.WriteAllText(outPath, html, Encoding.UTF8);
            Console.WriteLine("SAVED: " + kvp.Key + " (" + html.Length + " chars)");
        }
    }
}
"@ -Language CSharp

$tailFile = "c:\Users\khoadnd\Desktop\onboarding hub\latest_tail.txt"
$outDir = "c:\Users\khoadnd\Desktop\onboarding hub\scratch\restored_pages"

if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

[TailExtractor]::Extract($tailFile, $outDir)
