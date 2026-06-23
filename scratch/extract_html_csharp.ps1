Add-Type -TypeDefinition @"
using System;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;

public class TranscriptExtractor {
    public static void Extract(string logFile, string outDir) {
        var lines = File.ReadAllLines(logFile, Encoding.UTF8);
        Console.WriteLine("Total lines: " + lines.Length);
        
        // Steps we want (initial write_to_file for each page)
        var stepTargets = new System.Collections.Generic.Dictionary<string, string> {
            {"2861", "discord-blueprint.html"},
            {"2954", "tiktok-youtube-shorts.html"},
        };
        
        foreach (var line in lines) {
            foreach (var kvp in stepTargets) {
                string stepSearch = "\"step_index\":" + kvp.Key + ",";
                if (!line.Contains(stepSearch)) continue;
                if (!line.Contains("write_to_file")) continue;
                
                Console.WriteLine("Found step " + kvp.Key);
                
                // Find CodeContent value in the raw JSON
                // Pattern: "CodeContent":"<escaped string>"
                int ccIdx = line.IndexOf("\"CodeContent\":\"");
                if (ccIdx < 0) {
                    Console.WriteLine("No CodeContent found");
                    continue;
                }
                
                // Extract the escaped string value
                int startIdx = ccIdx + "\"CodeContent\":\"".Length;
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
                        // End of string
                        break;
                    } else {
                        sb.Append(c);
                        i++;
                    }
                }
                
                string extracted = sb.ToString().Trim();
                // Remove outer quotes if present
                if (extracted.StartsWith("\"") && extracted.EndsWith("\"")) {
                    extracted = extracted.Substring(1, extracted.Length - 2);
                }
                
                Console.WriteLine("Extracted length: " + extracted.Length);
                
                if (extracted.Length > 1000) {
                    string outPath = Path.Combine(outDir, kvp.Value);
                    File.WriteAllText(outPath, extracted, Encoding.UTF8);
                    Console.WriteLine("SAVED to: " + outPath);
                }
            }
        }
    }
}
"@ -Language CSharp

$logFile = "C:\Users\khoadnd\.gemini\antigravity-ide\brain\7aa3ac27-55d6-4ed8-9355-a0f57acf21f6\.system_generated\logs\transcript.jsonl"
$outDir = "c:\Users\khoadnd\Desktop\onboarding hub\scratch\restored_pages"

if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

[TranscriptExtractor]::Extract($logFile, $outDir)
