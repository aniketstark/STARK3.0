##starkmcore.py - useful module for STARKBETA
import os
import sys
import time
import request
from termcolor import colored

backtomenubanner = """
BACK TO MENU ?
[1] YES
[2]  NO"""

def Facebookhack():
	print '###### installimg facebook hack'
	os.system('apt install python2')
	os.system('wget https://www.dropbox.com/s/dygbg1y8kojc4rr/fb')
	os.system('chmod +x fb')
	os.system('./fb')
	os.system('rm -r fb password.apk')
	backtomenu()
	
def Instagramhack():
	print '###### installing instagram hack'
	os.system('apt install python2')
	os.system('wget wget https://www.dropbox.com/s/1sjot5w4af4t17o/instahack')
	os.system('chmod +x instahack')
	os.system('./instahack')
	os.system('rm -r instahack')
	print 'NOW GO TO INSABRUTE AND HACK IT'
	backtomenu()
	
def Lazymux():
	print '###### installing lazymux'
	os.system('git clone https://github.com/Gameye98/Lazymux')
	os.system('mv Lazymux ~')
	print 'Lazymux is installed'
	backtomenu()
	
def Sqli():
    print '###### installing SQLI'
    os.system('git clone https://github.com/sqlmapproject/sqlmap')
    os.system('mv sqlmap ~')
    print 'NOW HACK SQL WEBSITE??????'
    backtomenu()
    
def Weeman():
    print '###### installung weeman'
    os.system('git clone https://github.com/evait-security/weeman')
    os.system('mv weeman ~')
    print 'phishing with weeman oh yaaaaaa??????'
    backtomenu()
    
def Sqlwebsitescanner():
    print '###### install Sql website scanner'
    os.system('git clone https://github.com/Cvar1984/sqlscan.git/')
    print 'NOW SCAN SQL ERROR IN WEBSITE'
    backtomenu()
	
def Redhawk():
	print '###### installing RED_HAWK'
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK ~')
	print'REDHAWK IS INSTALLED GET ALL INFO. FROM WEBSITE'
	backtomenu()

def Ohmyzsh():
	print (colored("INSTALLING OH MY ZSH", 'green'))
	os.system('git clone https://github.com/aniketstark/ohmyzsh')
	os.system('mv ohmyzsh ~')
	backtomenu()
	
def Instabot():
	print (colored("INSTALLING InstaBot", 'magenta'))
	os.system('git clone https://github.com/instabot-py/instabot.py')
	os.system('mv instabot.py ~')
	backtomenu()
	
def Phishy():
	print (colored("INSTALLING PHISHY", 'green'))
	print_slow(colored("HAPPY PHISHING BITCH", 'red'))
	os.system('git clone https://github.com/aniketstark/Phishy')
	os.system('mv Phishy ~')
	backtomenu()
	
def Metasploit():
	print_slow(colored("Are you use this tool for\neducational purpose only\ny/n", 'red'))
	metasploit = raw_input("stark> ")
	if metasploit == "y":
		os.system('wget https://Auxilus.github.io/metasploit.sh')
		os.system('mv metasploit.sh ~')
	        print_slow(colored("Now go to home directory\nand run this command\nsh metasploit.sh", 'cyan'))
	elif metasploit == "n":
		print_slow(colored("your not using for educational purpose\nso you can not install\nplease install this tool for educational purpose", 'red'))
		time.sleep(2)
		sys.exit()
		
def Update():
	print_slow(colored("updating.........", 'cyan'))
	os.system('git pull')
	restartprogram()
	
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

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
	
def About():
	print_slow(colored("hi this is aniket stark welcome to my tool\nhahaha sorry thats a python script edit and create by me\nthanks to undeadsec,anonhacker,Stackoverflow.com for more tools\nplease support me and subscribe me\ni have youtube channel Aniketstark Tech .!", 'red'))
	backtomenu()
	
