from subprocess import Popen, PIPE
from . import CTTutils as utils

def document_to_text(file_path):
	if file_path[-4:] == ".doc":
		cmd = ['antiword', file_path]
		p = Popen(cmd, stdout=PIPE)
		stdout, stderr = p.communicate()
	return stdout.decode('ascii', 'ignore')

def docConvertor(file_path):
	ConvertedText = document_to_text(utils.check_path(file_path))
	name = file_path.replace(".doc",".txt")
	print (utils.getTime(), " doc -> txt ")
	f = open(name,'wb')
	f.write(ConvertedText.encode("UTF-8"))
	f.close
	print("File Saved To: "+name)
	return