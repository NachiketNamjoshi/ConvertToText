from subprocess import Popen, PIPE
from . import CTTutils as utils

def document_to_text(file_path):
	if file_path[-4:] == ".doc":
		cmd = ['antiword', file_path]
		p = Popen(cmd, stdout=PIPE)
		stdout, stderr = p.communicate()
	return stdout.decode('ascii', 'ignore')

def extract_text(file_path):
	return document_to_text(utils.check_path(file_path))
