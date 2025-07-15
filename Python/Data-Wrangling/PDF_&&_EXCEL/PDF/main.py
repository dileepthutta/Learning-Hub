import PyPDF2


FILE_NAME = "demopdf.pdf"




def access_data(file_name,page):
    # Open the PDF file in binary read mode
    with open(file_name, 'rb') as file:
        # Create a PDF reader object to access the content of the file
        pdf_reader = PyPDF2.PdfReader(file)

        # Create a PDF writer object to write pages into a new PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Decide how many pages to copy (up to 5 or the total number of pages if less)
        num_pages_to_copy = min(page, len(pdf_reader.pages))

        # Loop through the selected pages and add them to the writer
        for i in range(num_pages_to_copy):
            page = pdf_reader.pages[i]  # Get the page from the original PDF
            pdf_writer.add_page(page)   # Add the page to the new PDF

        # Open a new file in binary write mode to save the selected pages
        with open('demo1.pdf', 'wb') as pdf_output:
            pdf_writer.write(pdf_output)  # Write all the added pages to the new file

        # Print a message to confirm the new PDF was created
        print("PDF successfully created!")



def create_pdf(file_name, page_no, new_filename):
    with open(file_name, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        pdf = pdf_reader.pages[page_no]

        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf)

        with open(new_filename + '.pdf', 'wb') as pdf_output:
            pdf_writer.write(pdf_output)
            print("PDF successfully created!")

# Read the data in the console by Providing the PageNumber.
def read_page(file_name,page_no):
    try:
        with open(file_name,'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # To read the Page Number.
            page = pdf_reader.pages[page_no]
            # To read the page numbers Text.
            page_text = page.extract_text()

            return page_text
    except IndexError as error:
        return error


# To return the length of the PDF.
def length_of_pdf(file_name):
    with open(file_name,'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        return f"Number of pages in PDF : {len(pdf_reader.pages)}."

# print(length_of_pdf(FILE_NAME))

# print(read_page(FILE_NAME,69-1))

# create_pdf(file_name=FILE_NAME,page_no=0,new_filename='demo')


loop_on = True
while loop_on:
    print("1. Number of Pages.")
    print("2. Read PDF Data.")
    print("3. Create a single Page PDF.")
    print("4. Create Multiple Page PDF.")
    print("5. Exit!")

    n = int(input("Enter input :"))
    if n == 1:
        print(length_of_pdf(FILE_NAME))

    elif n == 2:
        num = int(input("Enter page number :"))
        print(read_page(FILE_NAME,page_no=num))

    elif n ==3:
        num = int(input("Enter page number :"))
        file_name = input("Enter file name to save :")
        create_pdf(FILE_NAME,num,file_name)

    elif n ==4:
        num = int(input("Enter page number :"))
        access_data(FILE_NAME,num)

    elif n ==5:
        loop_on = False

    else:
        print("In-valid Input\n")

