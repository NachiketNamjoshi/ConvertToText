import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import ConTxt.pdfConvertor as pyPDF

converted_path = pyPDF.extract_text()
print ("File Saved to: "+converted_path)
