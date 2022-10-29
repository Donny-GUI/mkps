from sys import argv
import os
import datetime

user = os.getlogin()


def scandir(filename):
    cc = os.getcwd()
    files = os.listdir(cc)
    if filename in files:
        print("filename already exists")
        exit()
    

def write_script(filename:str):
    scandir(filename)
    if filename.endswith(".py"):
        pass
    else:
        filename = filename+".py"
    date = datetime.datetime.utcnow()
    with open(filename, 'w') as newfile:
        newfile.write(f"#{filename}\n#{user}\n{date}\n")
        newfile.write("import os\n\n\n\ndef main():\n\tpass\n\nif __name__ == '__main__':\n\tmain()\n")


def help_me():
    help_page = [
    '[ mkps ]', 
    '     Make python script\n', 
    '  [ usage ]', 
    '    mkps <filename>', 
    ]
    for x in help_page:
        print(x)
    exit()

        

if __name__ == '__main__':
    args = argv
    try:
        args = argv[1:]
    except:
        args.append("xxx")
    finally:
        args = argv[1:]
    
    if args[0] == "xxx":
        help_me()
    else:
        write_script(args[0])



