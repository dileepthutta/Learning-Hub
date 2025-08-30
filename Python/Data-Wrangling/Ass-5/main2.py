# Split the pdf and save the first page into a new PDF.

import PyPDF2

def create_pdf(file_name, page_no, new_filename):
    with open(file_name, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        pdf = pdf_reader.pages[page_no]

        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf)

        with open(new_filename + '.pdf', 'wb') as pdf_output:
            pdf_writer.write(pdf_output)
            print("PDF successfully created!")

create_pdf('merged_output.pdf',1,'new_pdf')