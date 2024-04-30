import os
import sys


'''

Author: David Galstyan
Date: 28.04.2024
Description: This code seperates files from each other

'''



def get_directory():
	'''
    
        Description: enter directory name in terminal and get it
        Parameters: None
        Returns: directory's name
    
    '''

	try:	 
		dir_name = sys.argv[1]
		return dir_name
	except:
   		return 'Enter directory name!'


def get_files_lists(directory):
	'''
    
        Description: get list of all files in the given directory
        Parameters: directory's name
        Returns: list of files
    
    '''

	ml = os.listdir(directory)

	return ml


def get_files_dict(flist):
	'''
    
        Description: seperates types of files and give dict with seperated files
        Parameters: list of files
        Returns: dict of seperated files
    
    '''
		
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
	'''
    
        Description: The main function
        Parameters: None
        Returns: sorted files
    
    '''

	directory = get_directory()
	flist = get_files_lists(directory)
	files = get_files_dict(flist)
	print(files)


if __name__ == "__main__":
	main()