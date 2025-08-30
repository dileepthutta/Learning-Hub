# Write a Python script to load a PDF file using PyPDF2 and extract the number of pages in it.

import PyPDF2

with open('demo.pdf','rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    print(f"Length of PDF {len(pdf_reader.pages)}")