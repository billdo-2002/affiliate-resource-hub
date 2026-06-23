Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Text;

public class MultiTranscriptExtractor {
    static string Unescape(string line, int startIdx) {
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
                else if (next == 'u' && i + 5 < line.Length) {
                    string hex = line.Substring(i + 2, 4);
                    int codepoint;
                    if (int.TryParse(hex, System.Globalization.NumberStyles.HexNumber, null, out codepoint)) {
                        sb.Append((char)codepoint);
                        i += 6;
                    } else { sb.Append(c); i++; }
                }
                else { sb.Append(c); i++; }
            } else if (c == '"') {
                break;
            } else {
                sb.Append(c);
                i++;
            }
        }
        return sb.ToString();
    }
    
    public static void ExtractAll(string brainDir, string outDir) {
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
        
        foreach (var transcriptFile in Directory.GetFiles(brainDir, "transcript.jsonl", SearchOption.AllDirectories)) {
            Console.WriteLine("Scanning: " + transcriptFile);
            
            var lines = File.ReadAllLines(transcriptFile, Encoding.UTF8);
            
            foreach (var line in lines) {
                foreach (var tf in targetFiles) {
                    if (!line.Contains(tf)) continue;
                    
                    // Look for content field with DOCTYPE html
                    string[] searchKeys = new string[] { "\"content\":\"", "\"CodeContent\":\"" };
                    
                    foreach (var key in searchKeys) {
                        int searchFrom = 0;
                        while (true) {
                            int keyIdx = line.IndexOf(key, searchFrom);
                            if (keyIdx < 0) break;
                            
                            int startIdx = keyIdx + key.Length;
                            string extracted = Unescape(line, startIdx);
                            
                            if (extracted.Contains("<!DOCTYPE html>") && extracted.Length > 10000) {
                                if (!bestContent.ContainsKey(tf) || extracted.Length > bestContent[tf].Length) {
                                    bestContent[tf] = extracted;
                                    Console.WriteLine("  -> MATCH: " + tf + " len=" + extracted.Length + " from " + Path.GetDirectoryName(transcriptFile));
                                }
                            }
                            
                            searchFrom = keyIdx + key.Length;
                        }
                    }
                }
            }
        }
        
        Console.WriteLine("\n--- SAVING ---");
        foreach (var kvp in bestContent) {
            string outPath = Path.Combine(outDir, kvp.Key);
            File.WriteAllText(outPath, kvp.Value, Encoding.UTF8);
            Console.WriteLine("SAVED: " + kvp.Key + " (" + kvp.Value.Length + " chars)");
        }
    }
}
"@ -Language CSharp

$brainDir = "C:\Users\khoadnd\.gemini\antigravity-ide\brain"
$outDir = "c:\Users\khoadnd\Desktop\onboarding hub\scratch\restored_pages"

if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

[MultiTranscriptExtractor]::ExtractAll($brainDir, $outDir)
