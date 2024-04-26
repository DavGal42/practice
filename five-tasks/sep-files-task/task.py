import os
import sys


def get_directory():
	try:	 
		dir_name = sys.argv[1]
		return dir_name
	except:
   		return 'Enter directory name!'


def get_files_lists(directory):
	ml = os.listdir(directory)

	return ml


def get_files_dict(flist):
	md = {}

	txt_files = []
	py_files = []
	doc_files = []
	pdf_files = []
	xlsx_files = []

	for file in flist: 
		if file.endswith('.txt'):
			txt_files.append(file)
			md['txt'] = txt_files
		elif file.endswith('.py'):
			py_files.append(file)
			md['py'] = py_files
		elif file.endswith('.doc'):
			doc_files.append(file)
			md['docs'] = doc_files
		elif file.endswith('.pdf'):
			pdf_files.append(file)
			md['pdf'] = pdf_files
		elif file.endswith('.xlsx'):
			xlsx_files.append(file)
			md['xlsx'] = xlsx_files
			
	return md
	

def main():
	directory = get_directory()
	flist = get_files_lists(directory)
	files = get_files_dict(flist)
	print(files)


if __name__ == "__main__":
	main()