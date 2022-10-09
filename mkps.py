from sys import argv
from sh import date
import os



# [author]: donald guiles
# [date]:   oct. 8 2022
# [description]:  mkps make python script --
#                 for creating entire python3 scripts from the terminal cmdline



class MKPS:

	""" class version of mkps """


    user = os.getlogin()
    date = date()
    description = ""
    self.file = ""

    staticFile = [
	f'# [file]       : {self.file}',
	f'# [description]: {self.description}',
	f'# [author]     : {self.user}',
	f"# [date]       : {self.date}"
	'import os\n',
	]
   defmain = [
	'def main():',
	'\tpass',
	'\n'
	]		
   ifmain = [
	"if __name__ == '__main__':",
	"\tmain()"
    ]
    flags = ['-h', '-m', '-f', '-fi', '-ff']


    def __init__(self):

	self.filename = None
	self.values = None
        self.flag_values['filename'] = []
        for flag in self.flags:
            self.flag_values[f'{flag}'] = []
            self.current_flag = self.flag_values['filename']
        self.this_file = self.staticFile
        self.adding_modules = []

    def parseArgs(self):

        """ Parse the system args """

    	try:
    	    args = argv[1:]
   	except:
	    self.error("not filename given")
    	    self.helpMe()
    	self.current_flag = self.flag_values['filename']
    	
    	for arg in args:
	    if arg in self.flags:
    	        self.current_flag = self.flag_values[f'{arg}']
    	    else:
    	        self.current_flag.append(arg)
    	self.filename = self.flag_values['filename']
	

    def makeBlank(self):
	""" make a blank python file with the given filename """
        os.system(f"touch {self.filename}")


    def checkFlagValues(self):
    	
	""" check all the flag values collected and execute the methods necessary """
    	
	for x in self.flags:
    	    if self.flag_values[f'{x}'] == None:
    		continue
    	    else:
    		match x:
    		    case '-h':
    			self.helpMe()
    		    case '-f':
    			self.addFunction(self.flag_values['-f'].values)
    		    case '-fi':
			self.fromImport(self.flag_values['-fi'].values)
    		    case '-ff':
    			self.importFunctionFrom(self.flag_values['-ff'].values)
    		    case '-m':
    			self.addModule(self.flag_values['-m'])
    		    case '-i':
    			self.includeFile(self.flag_values['-i'])


    def importFunctionFrom(self, function_values):
    	
    	""" import a function from another file """

    	file = function_values[0]
    	function_name = function_values[1]

    	functions = []
	__lines_slice = []
	f = open(file, 'r')
	lines = enumerate(f.readlines())
	f.close()		
	mylines = []	
	for line in lines:		
	    if adding == True:
		mylines.append(line)
		xfuncx = f'def {function_name}'
	    if line.startswith(xfuncx):
		mylines.append(line)
		adding = True
		continue	
	    elif line.startswith('def ')
		adding = False 
		break
	for x in mylines:
	    self.defmain.append(x)


    def addModule(self, module_values):

    	""" add a module to the file """

    	for x in module_values:
    	    y = "import " + x
    	    self.adding_modules.append(y)


    def customFunction(self, custom_function_values):
    	
    	""" add a custom function to the file """

    	x = custom_function_values[0]
    	x.split()
    	name = x[0]
    	x.remove(x[0])
    	codelines = x[-1]
    	x.remove(x[-1])
    	args = x 
    	line1 = f"def {name}({[x for x in args]}):"
    	line2 = codelines.split('\n')
    	lines = [line1]
    	for x in line2:
    	    lines.append(x)

    	for line in lines:
    	    self.defmain.append(line)

    def fixFilename(self):
    	if self.filename == None:
    	    self.helpMe()
    	if self.filename.endswith('.py'):
            self.filename = self.filename
    	else:
            self.filename = self.filename + '.py'


    def helpMe(self):
    	help_page = [
    		'[ mkps ]', 
    		'     Make python script\n', 
    		'  [ usage ]', 
    		'    mkps <filename>', 
    		'    mkps <filename> -f "new_function x" "print(x)"', 
    		'    mkps <filename> -ff mom.py hello_world',
    		'\n  [ flags ]',
    		'     -f  --function        add a new function to the file',
    		'     -ff --function-file   add a new function FROM a file',
    		'     -fi --from-import     from <name> import <thing> flag',
    		'     -m  --modules         add another module to he file',
    		'     -h  --help            show this help page'
    		]
    	for x in help_page:
    	    print(x)
    	exit()

    def start(self):
    	self.parseArgs()
    	self.fixFilename()
    	self.checkFlagValues()
    	self.makeBlank()
    	for x in self.adding_modules:
    	    self.this_file.append(x)
    	for x in self.defmain:
    	    self.this_file.append(x)
    	for x in self.ifmain:
    	    self.this_file.append(x)
    	file = open(self.filename, 'w')
    	for line in self.this_file:
    	    line = line + "\n"
            file.write(line)

    	print('done')






mkps = MKPS()
mkps.start()



