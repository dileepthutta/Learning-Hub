# Write a Python script to merge multiple PDF files into one using PyPDF2.

from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list,output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"Pdf successfully merged and saved in this path{output_path}")

merge_pdfs(["first.pdf","second.pdf"],"merged.pdf")
