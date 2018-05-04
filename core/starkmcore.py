##starkmcore.py - useful module for STARK2.0
import os
import sys
import time
from termcolor import colored

backtomenubanner = """
BACK TO MENU ?
[1] YES
[2]  NO"""

def deepstore():
 print_slow(colored("Welcome mr.Stark\n", 'blue'))
 print_slow(colored("Your work is currently working\nplease wait i am checking...............\nyour work is completed57%\nSo please patience\nyour work will complete soon ok.!\nplease update every day or every week..!\nbye......!", 'green'))
 backtomenu()

def achacking():
 print(colored("""
     ==================================================
     ....###.........######.....##.....##....###.....######..##....##
     ...##.##.......##....##....##.....##...##.##...##....##.##...##.
     ..##...##......##..........##.....##..##...##..##.......##..##..
     .##.....##.....##..........#########.##.....##.##.......#####...
     .#########.....##..........##.....##.#########.##.......##..##..
     .##.....##.###.##....##....##.....##.##.....##.##....##.##...##.
     .##.....##.###..######.....##.....##.##.....##..######..##....##
     ==================================================
	1. Facebook Hack
	2. Instagram Hack
	3. Phishy
	4. Weeman
     ==================================================
	5. Back
     ==================================================
    """, 'green'))

 acha = raw_input("stark > ")

 if acha == "1":
    	Facebookhack()
 elif acha == "2":
    	Instagramhack()
 elif acha == "3":
    	Phishy()
 elif acha == "4":
    	Weeman()
 elif acha == "5":
 	   os.system("clear")
 	   restartprogram()
 elif acha == "0":
        restartprogram()
 else:
	print_slow(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
	restartprogram()

def info():
 print(colored("""
      _ _  _ ____ ____     ____ ____ ___ _  _ ____ ____ _ _  _ ____ 
      | |\ | |___ |  |     | __ |__|  |  |__| |___ |__/ | |\ | | __ 
      | | \| |    |__| .   |__] |  |  |  |  | |___ |  \ | | \| |__] 

      ==============================================
      1. Red_Hawk
      2. ReconDog
      3. SQL Scanner
      4. Txtool
      ==============================================
      5. Back
      ==============================================
""", 'green'))

 info = raw_input("stark > ")
 
 if info == "1":
 	Redhawk()
 elif info == "2":
 	ReconDog()
 elif info == "3":
 	Sqlscanner()
 elif info == "4":
 	Txtool()
 elif info == "5":
 	os.system("clear")
 	restartprogram()
 elif info == "0":
     restartprogram()
 else:
	print_slow(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
	os.system("clear")
	restartprogram()
	
def webhacking():
 print(colored("""
                        _          _                   _     _               
       __      __  ___ | |__      | |__    __ _   ___ | | __(_) _ __    __ _ 
       \ \ /\ / / / _ \| '_ \     | '_ \  / _` | / __|| |/ /| || '_ \  / _` |
        \ V  V / |  __/| |_) | _  | | | || (_| || (__ |   < | || | | || (_| |
         \_/\_/   \___||_.__/ (_) |_| |_| \__,_| \___||_|\_\|_||_| |_| \__, |
                                                                       |___/
 """, 'red'))
 print(colored("""
       =====================================================================
       1. SQLInjection
       =====================================================================
       2.Back
       =====================================================================
 """, 'green'))
 
 webh = raw_input("stark > ")
 
 if webh == "1":
 	Sqli()
 elif webh == "2":
 	os.system("clear")
        restartprogram()
     
 elif info == "0":
     restartprogram()
 else:
	print_slow(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
	os.system("clear")
	restartprogram()
	
def termux():
 print(colored("""
       _____                                     
      |_   _|                                    
        | |    ___  _ __  _ __ ___   _   _ __  __
        | |   / _ \| '__|| '_ ` _ \ | | | |\ \/ /
        | |  |  __/| |   | | | | | || |_| | >  < 
        \_/   \___||_|   |_| |_| |_| \__,_|/_/\_\
                                            
      ============================================
      1. Lazymux
      2. Metasploit-Framework
      3. Txtool
      ============================================
      4. Back
      ============================================                                      
   """, 'green'))

 termux = raw_input("stark > ")
 
 if termux == "1":
 	Lazymux()
 elif termux == "2":
 	Metasploit()
 elif termux == "3":
 	Txtool()
 elif termux == "4":
     os.system("clear")
     restartprogram()
     
 elif info == "0":
     restartprogram()
 else:
	print_slow(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
	os.system("clear")
	restartprogram()
 
def Txtool():
 print_slow(colored("installing txtool", 'red'))
 os.system("git clone https://github.com/kuburan/txtool")
 os.system("mv txtool ~")
 backtomenu()

def ReconDog():
 print_slow(colored("installing ReconDog", 'green'))
 os.system("git clone https://github.com/UltimateHackers/ReconDog")
 os.system("mv ReconDog ~")
 backtomenu()
 
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
    
def Sqlscanner():
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
		os.system('curl -LO https://raw.githubusercontent.com/aniketstark/TMetasploit/master/metasploit.sh')
		os.system('mv metasploit.sh ~')
		os.system('cd ~ && chmod +x metasploit.sh')
	        print_slow(colored("Now go to home directory\nand run this command\nsh metasploit.sh", 'cyan'))
	elif metasploit == "n":
		print_slow(colored("your not using for educational purpose\nso you can not install\nplease install this tool for educational purpose", 'red'))
		time.sleep(2)
		sys.exit()
		
def Update():
	print_slow(colored("always update this tool ok.!", 'cyan'))
	print_slow(colored("updating.........\n", 'green'))
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
	print_slow(colored("hi this is aniket stark welcome to my tool\nhahaha sorry thats a python2 script edit and create by me\nthanks to undeadsec,anonhacker,Stackoverflow.com\nfor more tools please support me and subscribe me\ni have youtube channel Aniketstark Tech .!", 'red'))
	backtomenu()
