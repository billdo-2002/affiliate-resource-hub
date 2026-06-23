Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

public class ChunkExtractor {
    static string CleanViewFileContent(string raw) {
        // The content has escaped HTML entities: \u003c = < and \u003e = >
        // Also has \\r\\n for newlines, \" for quotes
        var sb = new StringBuilder(raw.Length);
        int i = 0;
        while (i < raw.Length) {
            if (raw[i] == '\\' && i + 1 < raw.Length) {
                char next = raw[i+1];
                if (next == 'n') { sb.Append('\n'); i += 2; }
                else if (next == 'r') { sb.Append('\r'); i += 2; }
                else if (next == 't') { sb.Append('\t'); i += 2; }
                else if (next == '"') { sb.Append('"'); i += 2; }
                else if (next == '\\') { sb.Append('\\'); i += 2; }
                else if (next == 'u' && i + 5 < raw.Length) {
                    string hex = raw.Substring(i+2, 4);
                    int codepoint;
                    if (int.TryParse(hex, System.Globalization.NumberStyles.HexNumber, null, out codepoint)) {
                        sb.Append((char)codepoint);
                        i += 6;
                    } else { sb.Append(raw[i]); i++; }
                }
                else { sb.Append(raw[i]); i++; }
            } else {
                sb.Append(raw[i]);
                i++;
            }
        }
        return sb.ToString();
    }
    
    public static void Extract(string tailFile, string outDir) {
        string content = File.ReadAllText(tailFile, Encoding.UTF8);
        Console.WriteLine("Tail file size: " + content.Length);
        
        // Find VIEW_FILE content blocks that contain HTML
        // Pattern in raw: "type\":\"VIEW_FILE\"...\"content\":\"...actual file content..."
        // We look for Showing lines X to Y sections in the content
        
        var targetFiles = new Dictionary<string, List<string>> {
            {"x-twitter-ready-to-post.html", new List<string>()},
            {"reddit-ready-to-post.html", new List<string>()},
            {"short-form-video-guidelines.html", new List<string>()},
            {"discord-blueprint.html", new List<string>()},
            {"tiktok-youtube-shorts.html", new List<string>()},
            {"general-guide.html", new List<string>()},
            {"track-profit-like-a-pro.html", new List<string>()},
            {"stop-losing-30-profit.html", new List<string>()},
            {"scale-safely-with-margins.html", new List<string>()},
        };
        
        // Search for "Total Lines:" pattern which appears in VIEW_FILE responses
        int pos = 0;
        while (pos < content.Length) {
            int tlIdx = content.IndexOf("Total Lines:", pos);
            if (tlIdx < 0) break;
            
            // Look backwards for file path
            int lookback = Math.Max(0, tlIdx - 600);
            string prefix = content.Substring(lookback, tlIdx - lookback);
            
            string matchedTarget = null;
            foreach (var key in targetFiles.Keys) {
                if (prefix.Contains(key)) { matchedTarget = key; break; }
            }
            
            if (matchedTarget != null) {
                // Find "The following code" marker or "Showing lines"
                int showIdx = content.IndexOf("Showing lines", tlIdx);
                int startContent = content.IndexOf("\\n1: ", showIdx);
                if (startContent < 0) startContent = content.IndexOf("\\n1:", showIdx);
                
                if (startContent > 0 && startContent - tlIdx < 500) {
                    // Find end: "The above content" or next VIEW_FILE
                    int endSearch = startContent + 100;
                    int endIdx = content.IndexOf("The above content", endSearch);
                    if (endIdx < 0 || endIdx - startContent > 200000) endIdx = startContent + 100000;
                    
                    string rawChunk = content.Substring(startContent, Math.Min(endIdx - startContent, 150000));
                    string cleanChunk = CleanViewFileContent(rawChunk);
                    
                    if (cleanChunk.Length > 500) {
                        targetFiles[matchedTarget].Add(cleanChunk);
                        Console.WriteLine("Found chunk for " + matchedTarget + " at pos=" + pos + " len=" + cleanChunk.Length);
                    }
                }
            }
            
            pos = tlIdx + 100;
        }
        
        // Now reassemble each file
        Console.WriteLine("\n--- ASSEMBLING FILES ---");
        foreach (var kvp in targetFiles) {
            if (kvp.Value.Count == 0) { Console.WriteLine("NO CHUNKS: " + kvp.Key); continue; }
            
            // Concatenate and clean line numbers (format: "N: content\n")
            var fullContent = new StringBuilder();
            foreach (var chunk in kvp.Value) {
                // Remove line numbers: pattern "\nN: " at start of each line
                var lines = chunk.Split('\n');
                foreach (var line in lines) {
                    // Check if line starts with digits followed by ": "
                    int colonIdx = line.IndexOf(": ");
                    if (colonIdx > 0 && colonIdx <= 6) {
                        bool allDigits = true;
                        for (int i = 0; i < colonIdx; i++) {
                            if (!char.IsDigit(line[i])) { allDigits = false; break; }
                        }
                        if (allDigits) {
                            fullContent.AppendLine(line.Substring(colonIdx + 2));
                            continue;
                        }
                    }
                    fullContent.AppendLine(line);
                }
            }
            
            string html = fullContent.ToString();
            string outPath = Path.Combine(outDir, kvp.Key);
            File.WriteAllText(outPath, html, Encoding.UTF8);
            Console.WriteLine("SAVED: " + kvp.Key + " (" + html.Length + " chars, " + kvp.Value.Count + " chunks)");
        }
    }
}
"@ -Language CSharp

$tailFile = "c:\Users\khoadnd\Desktop\onboarding hub\latest_tail.txt"
$outDir = "c:\Users\khoadnd\Desktop\onboarding hub\scratch\restored_pages"
if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

[ChunkExtractor]::Extract($tailFile, $outDir)
