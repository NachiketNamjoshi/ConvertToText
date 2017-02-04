from os import path
from time import strftime

def check_path(abs_path):
        if path.exists(path.abspath(abs_path)) != True:
            print ("\nThe Specified path does not exist.\n")
            return None
        return abs_path

def ParaToSentence(content):
        ConvertedText = ""
        sentences = re.split(r'((?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s)', content)
        for line in sentences:
            if re.match(r'^\s*$',line): ##To skip blank lines from op.
                continue
            ConvertedText += line
        return ConvertedText

def getTime():
	return (strftime("%H:%M:%S"))