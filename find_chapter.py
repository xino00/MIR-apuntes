import re

with open(r"C:\Users\arena\OneDrive\Documentos\MIR\manual.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Search for potential section headers
for i, line in enumerate(lines):
    line = line.strip()
    if not line: continue
    
    # Check if 'cardiolog' is in the line
    if "cardiolog" in line.lower():
        # Heuristic for a major title: short line, mostly uppercase or Title Case
        if len(line) < 60 and line.isupper():
            print(f"[{i}] {line}")
        elif "SECCI" in line.upper() or "CAPITULO" in line.upper() or "CAPTULO" in line.upper():
            print(f"[{i}] {line}")

