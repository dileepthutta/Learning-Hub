# To merge two PDF's

from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"Merged PDF saved to {output_path}")

# Example usage:
merge_pdfs(["first.pdf", "second.pdf"], "merged_output.pdf")
