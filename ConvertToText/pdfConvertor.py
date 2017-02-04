import os
import sys
from os import chdir, getcwd, listdir, path
import PyPDF2 as pyPdf
import re
from . import CTTutils as utils
class pdfConvertor(object):

    def __init__(self, inputFile):
        inputFile = utils.check_path(inputFile)
        if inputFile != None:
             self.extract_text(inputFile)
        else:
            sys.exit(1)

    def extract_text(self, path):
        content = ""
        name = path.replace(".pdf",".txt")
        pdf = pyPdf.PdfFileReader(open(path,"rb"))
        for i in range(0, pdf.getNumPages()):
            content += pdf.getPage(i).extractText() + "\n"
        content = utils.ParaToSentence(content)
        print (utils.getTime(), " pdf -> txt ")
        f = open(name,'wb')
        f.write(content.encode("UTF-8"))
        f.close
        print("File Saved To: "+name)
        return

