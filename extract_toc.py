import os
import fitz  # PyMuPDF
import sys

target_dir = r"C:\Users\arena\OneDrive\Documentos\MIR"
files = [f for f in os.listdir(target_dir) if f.lower().endswith(".pdf")]
print("PDF files found:", files)

if not files:
    print("No PDF files found.")
    sys.exit(0)

# Assuming the first one is the target if it matches partially
target_file = None
for f in files:
    if "12" in f and "OCTUBRE" in f.upper():
        target_file = os.path.join(target_dir, f)
        break

if not target_file:
    print("Target PDF not found!")
    sys.exit(1)

print("Opening:", target_file)
try:
    doc = fitz.open(target_file)
    toc = doc.get_toc() # [[level, title, page_number], ...]
    if toc:
        print("Table of contents found.")
        for item in toc:
            if "cardio" in item[1].lower():
                print(f"Match found in TOC: {item}")
    else:
        print("No TOC found. Will need to search text.")
except Exception as e:
    print("Error:", e)
