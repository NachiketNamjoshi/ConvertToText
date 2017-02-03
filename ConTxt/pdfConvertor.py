import os
from os import chdir, getcwd, listdir, path
import PyPDF2 as pyPdf
from time import strftime

def check_path(prompt):
    abs_path = input(prompt)
    while path.exists(abs_path) != True:
        print ("\nThe Specified path does not exist.\n")
        abs_path = input(prompt)
    return abs_path

def extract_text():
    path = check_path("Absolute Path to folder containing all pdfs: ")
    name = path.replace(".pdf",".txt")
    content = ""
    pdf = pyPdf.PdfFileReader(open(path,"rb"))
    for i in range(0, pdf.getNumPages()):
        content += pdf.getPage(i).extractText() + "\n"
    print (strftime("%H:%M:%S"), " pdf -> txt ")
    f = open(name,'wb')
    f.write(content.encode("UTF-8"))
    f.close
    return name
