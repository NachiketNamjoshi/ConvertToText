import os
import sys
from os import chdir, getcwd, listdir, path
import PyPDF2 as pyPdf
import re
from . import CTTutils as utils

def extract_text(path):
    content = ""
    path = utils.check_path(path)
    name = path.replace(".pdf",".txt")
    pdf = pyPdf.PdfFileReader(open(path,"rb"))
    for i in range(0, pdf.getNumPages()):
        content += pdf.getPage(i).extractText() + "\n"
    content = utils.ParaToSentence(content)
    print (utils.getTime(), " pdf -> txt ")
    return content

