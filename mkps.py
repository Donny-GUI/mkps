# [author]:  Donald Guiles
# [date]:    sept 27 2022
# [license]: GNU3 / Freeware
# [description]
#    mkps - makes python scripts with all the seasoning on top.
#           saves time for writing commments and ifmain/main.
#	    will check for duplicates in arguments as well as 
#	    duplicate existing files. Time complexity minimized.
#
# --To do--
# - extended to macos and windows
# - create install.py
# - add python rich status

import os
from sys import argv 
from datetime import datetime

def get_filepath(filename):
	""" turns the filename into the filepath  """

	curdir = os.getcwd()
	file_path = f"{curdir}/{filename}"
	return file_path


def get_filepaths(file_list):
	""" takes a list of filenames and returns filepaths """

	return_list = []
	for file in file_list:
		fpath = get_filepath(file)
		return_list.append(fpath)

	return return_list


def make_default_pyfile(filepath):
	""" creates a standard function based python file with name filepath """

	date_time_now = datetime.now()
	username = os.getlogin()
	curdir = str(os.getcwd()) + "/"
	filename = filepath - curdir
	default_py = [
		f'#  [  filename ]:  {filename}',
		f'#  [      date ]:  {date_time_now}',
		f'#  [    author ]:  {username}',
		'#  [    module ]:  n/a'
		'#  [description]:  ',
		'',
		'import os', 
		'',
		'',
		'def main():',
		'	print("hi mom!")',
		'',
		"if __name__ == '__main__':",
		'	main()',
		''
	]

	os.system(f"touch {filepath}")
	file = open(filepath, 'w')
	for x in default_py:
		line = x + "\n"
		file.write(line)
	file.close()


def show_help():
	print("\n [ mkps ]    \n")
	print("      make python script \n")
	print("    [usage ]   \n")
	print("          mkps <filename> <filename>... \n")


	
def remove_extensions(arguments):
	files = []
	for x in arguments:
		if ".py" in x:
			y = x.split(".py")
			z = "".join(y)
			files.append(z)
		else:
			files.append(x)
	return files


def add_extensions(file_list):
	""" adds .py to all names """

	python_extended = []
	for file in file_list:
		if file.endswith(".py"):
			python_extended.append(file)
		else:
			x = file + ".py"
			python_extended.append(x)
	return python_extended


def check_args():
	""" checks to make sure there isnt one argument, returns argv[1:] """

	args = argv
	if int(len(args)) < 2:
		show_help()
		exit()
	else:
		return args[1:]


def make_scripts(file_list):
	file_paths = file_list
	for file_path in file_paths:
		make_default_pyfile(file_path)
		

def scan_pyfiles(file_list):
	""" checks the current directory for duplicates """
	
	return_list             = file_listst
	py_files                = []
	current_directory_files = os.listdir()
	
	for x in current_directory_files:
		if x.endswith('.py'):
			py_files.append(x)
	
	for py_file in py_files:
		if py_file in file_list:
			return_list.remove(pyfile)
			print(pyfile," already exists!")

	return return_list


def check_for_duplicates(args_list):
	""" removes duplicate filenames. Time complexity minimized """
	
	if len(args_list) == '1':
		return args_list

	set_of_arguments = set()
	list_of_arguments = args_list
	for arg in args_list:
		if arg in set_of_arguments:
			print("duplicate detected in filename given")
			list_of_arguments.remove(arg)
			check_for_duplicates(list_of_arguments)
		else:
			set_of_arguments.add(arg)

	return list_of_arguments


def main():
	
	print("checking args...")
	# this part just makes sure that no arguments are given
	# returns help if so.
	args            = check_args()
	
	print("checking filenames")
	# removing all extensions helps identify real duplicates
	# prevents events like mkps filename filename.py
	filenames       = remove_extensions(args)
	dargs 		= check_dupes(filenames)

	print("checking pre-existing files")
	# add the entensions back and check the current directory for the same files
	files           = add_extensions(filenames)
	makefiles       = scan_pyfiles(files)

	print("making... ")
	filepaths       = get_filepaths(makefiles)
	scripts         = make_scripts(filepaths)
	print("done.")


if __name__ == '__main__':
	main()
	


	

	
	
	
