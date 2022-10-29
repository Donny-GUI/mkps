import os

if os.name == "posix":
	pass
else:
	print("posix only sorry")
	exit()
username = os.getlogin()
os.chdir(f"/home/{username}")
files = os.listdir()
myfiles = []
for file in files:
	if file.startswith(".bash"):
		myfiles.append(file)
cc = os.getcwd()
if ".bash_aliases" in myfiles:
	with open(".bash_aliases", 'a') as ali:
		ali.write(f"\nalias mkps='python3 {cc}/mkps/mkps.py'")
else:
	with open(".bashrc", 'a') as ali:
		ali.write(f"\nalias mkps='python3 {cc}/mkps/mkps.py'")
