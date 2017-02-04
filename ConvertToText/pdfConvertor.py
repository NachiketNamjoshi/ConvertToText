import os
import sys
from os import chdir, getcwd, listdir, path
import PyPDF2 as pyPdf
from time import strftime
import re

class pdfConvertor(object):

    def __init__(self,inputFile):
        inputFile = self.check_path(inputFile)
        if inputFile != None:
             self.extract_text(inputFile)
        else:
            sys.exit(1)


    def check_path(self, abs_path):
        if path.exists(abs_path) != True:
            print ("\nThe Specified path does not exist.\n")
            return None
        return abs_path

    def extract_text(self, path):
        content = ""
        name = path.replace(".pdf",".txt")
        pdf = pyPdf.PdfFileReader(open(path,"rb"))
        for i in range(0, pdf.getNumPages()):
            content += pdf.getPage(i).extractText() + "\n"
        content = self.ParaToSentence(content)
        print (strftime("%H:%M:%S"), " pdf -> txt ")
        f = open(name,'wb')
        f.write(content.encode("UTF-8"))
        f.close
        print("File Saved To: "+name)
        return

    def ParaToSentence(self, content):
        ConvertedText = ""
        sentences = re.split(r'((?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s)', content)
        for line in sentences:
            if re.match(r'^\s*$',line): ##To skip blank lines from op.
                continue
            ConvertedText += line
        return ConvertedText

