import os
import time
from getpass import getuser

#Removes spaces and CAPS from string
def noSpc(string):
	string = string.replace(' ','')
	string = string.lower()
	return string

#Clears screen + Displays Loading...
def clrScreen():
	os.system('cls')
	multDots = 1
	dot = '.'
	
	for times in range(3):
		print '	Loading' + (dot * multDots)
		time.sleep(.4)
		os.system('cls')
		multDots = multDots + 1
	return None

#Creates a prompt for user to type function		
def askFunc():
	input = raw_input()
	noSpc(input)
	
	mkDir(input)
	rmDir(input)
	helpMenu(input)
	openFile(input)
	goBack(input)
	
	if input[:4] == 'open':
		openDir(input[5:])
	elif input[:3] == 'pop':
		clrScreen()
		popDir()
	else:
		print 'error'
		askFunc()

#tells cmd to open directory then shows directories in folder
def openDir(directory): 
	clrScreen()
	os.chdir(directory)
	os.system('dir')
	askFunc()

#Allows you to go back a directory
def goBack(directory):
	if directory[:4] == 'back':
		openDir('..')
	return directory
	
#Allows you to open files	
def openFile(directory):
	if directory[:4] == 'file':
		os.system(directory[5:])
		askFunc()
	return directory
#Allows you to make a directory	
def mkDir(directory):
	if directory[:4] == 'make':
		clrScreen()
		os.mkdir(directory[5:])
		os.system('dir')
		askFunc()
	return directory
	
#allows you to remove a directory	
def rmDir(directory):
	if directory[:6] == 'remove':
		clrScreen()
		os.rmdir(directory[7:])
		os.system('dir')
		print "	DIRECTORY REMOVED"
	return directory

#shows most popular directories	
def popDir():
	username = getuser()
	pop = raw_input("""Type 'help' if you would like to see the help menu.\n		
	DIRECTORIES \n	Computer  Programs\n	Users  %s\n	Documents  Pictures\n	""" % username)
	pop = noSpc(pop)
	helpMenu(pop)
	
	#takes you into popular directory
	if pop == 'opencomputer':
		openDir('C:/')
	elif pop == 'openprograms':
		openDir('C:/Program Files')
	elif pop == 'openusers':
		openDir('C:/Users')
	elif pop == 'open' + username.lower():
		openDir('C:/Users/%s' % username)
	elif pop == 'opendocuments':
		openDir('C:/Users/%s/Documents' % username)
	elif pop == 'openpictures':
		openDir('C:/Users/%s/Pictures' % username)
	else:
		print 'Error, invalid input.'
		
#displays the help menu		
def helpMenu(x):
	if x == 'help':
		print "To open a directory, type 'Open', then the name of the directory."
		print "To move back a directory, type 'Back'."
		print "To open a file, type 'File', then he name of the file and extension."
		print "To create a directory, type 'Make', then what you want to name it."
		print "To remove a directory, type 'Remove', then the name of the directory you want to remove."
		print "To look at popular folders, type 'Pop'"
		askFunc()
popDir()