# Write a Python script to Extract Matching Text from pdf using PyPDF2

import re
from PyPDF2 import PdfReader

def find_text_in_pdf(pdf_file, pattern):
    reader = PdfReader(pdf_file)
    matches = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            matches += re.findall(pattern, text)
    return matches

# Example: Find all words that start with "Invoice"
pattern = r" class"  # Change this to match what you need

matches = find_text_in_pdf("merged_output.pdf", pattern)

# Print results
for match in matches:
    print(match)
