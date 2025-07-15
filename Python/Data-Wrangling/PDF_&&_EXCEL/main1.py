# How do you convert a pdf to text using python



import PyPDF2

file = open('PDF/demopdf.pdf', 'rb')

# Read the file using PDF reader method.
pdf_reader = PyPDF2.PdfReader(file)

#To find the number of Pages in the pdf.
print(len(pdf_reader.pages))


#To read a specific Page.
page_one = pdf_reader.pages[1]

#To extract text from specific Page Number.
page_one_text = page_one.extract_text()

#To print the page text.
print(page_one_text)


pdf_writer = PyPDF2.PdfWriter()

pdf_writer.add_page(page_one)

pdf_output = open('example.pdf','wb')
pdf_writer.write(pdf_output)

file.close()

