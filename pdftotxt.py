import PyPDF2

def pdf2txt(pdf_file, new_txt_name):
    #Opening the .pdf file
    with open(pdf_file, 'rb') as pdf:
        pdf_reader = PyPDF2.PdfReader(pdf)
    #Creating a .txt file
    with open(new_txt_name,"a") as f:     
        for page_num in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page_num]
            text = page_obj.extract_text()
            #for each page, the text is extracted and written in the .txt file
            f.write(text)
    return text