##starkmcore.py - useful module for STARK2.0
import os
import sys
import time
from termcolor import colored

backtomenubanner = """
BACK TO MENU ?
[1] YES
[2]  NO"""

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
	5. MBF
	6. Shellphish
     ==================================================
	7. Back
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
 	   Mbf()
 elif acha == "6":
 	   shellphish()
 elif acha == "7":
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
      5. D-Tect
      6. CloudFail       ==>(This is scan or bypass the cloudflare)
      7. InurlBR
      ==============================================
      8. Back
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
 	dtect()
 elif info == "6":
 	os.system("git clone https://github.com/m0rtem/CloudFail")
	os.system("mv CloudFail ~")
 elif info == "7":
	os.system("git clone https://github.com/googleinurl/SCANNER-INURLBR")
	os.system("mv SCANNER-INURLBR ~") 
 elif info == "8":
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
      3. Beef Framework =>  ( to many error with unstable metasploit )
      4. ohmyzsh ============> (new look for termux)
      5. Tload ===============> (Best for Payloadmaker)
      6. LazyMeta ============>(payload maker tool)
      7. print architecture ======>(32 bit or 64 bit)
      8. Facebook
      9. FakeCall =============(Working 100%)
      10. TAssistant =========>(new tool)
      ============================================
      11. Back
      ============================================                                      
   """, 'green'))

 termux = raw_input("stark > ")
 
 if termux == "1":
 	Lazymux()
 elif termux == "2":
 	Metasploit()
 elif termux == "3":
 	os.system("""mkdir -p $PREFIX/etc/apt/sources.list.d && printf "deb [trusted=yes] https://hax4us.github.io/termux-tools/ extras main" > $PREFIX/etc/apt/sources.list.d/hax4us.list""")
 	os.system("apt update")
 	print_slow(colored("Now open new tab use this command\napt install update then pkg install beef-xss", 'green'))
 elif termux == "4":
 	Ohmyzsh()
 elif termux == "5":
 	tload()
 elif termux == "6":
 	lazymeta()
 elif termux == "7":
     os.system("dpkg --print-architecture")
     time.sleep(3)
     backtomenu()
 elif termux == "8":
 	Facebook()
        backtomenu()
 elif termux == "9":
 	os.system("git clone https://github.com/TheSpeedX/TBomb")
        os.system("mv TBomb ~")
	print_slow(colored("""Installed""", "green"))
	print_slow(colored("""You Need to Watch the Video""", "green"))
	os.system("termux-open-url https://www.youtube.com/channel/UC6CwdVj9ztWzJtO3q43isfg")
 elif termux == "10":
	os.system("git clone https://github.com/aniketstark/TAssistent")
	os.system("mv TAssistent ~")
	backtomenu()
 elif termux == "11":
     os.system("clear")
     restartprogram()
     
 elif info == "0":
     restartprogram()
 else:
	print_slow(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
	os.system("clear")
	restartprogram()
def Fix():
 print(colored("""
 
       .########.########..########...#######..########.
       .##.......##.....##.##.....##.##.....##.##.....##
       .##.......##.....##.##.....##.##.....##.##.....##
       .######...########..########..##.....##.########.
       .##.......##...##...##...##...##.....##.##...##..
       .##.......##....##..##....##..##.....##.##....##.
       .########.##.....##.##.....##..#######..##.....##

       .##..........#####...##.......
       .##....##...##...##..##....##.
       .##....##..##.....##.##....##.
       .##....##..##.....##.##....##.
       .#########.##.....##.#########
       .......##...##...##........##.
       .......##....#####.........##.
       
   """, 'red'))
 print(colored("""
    ==============================================  
    1. Metasploit database fixer
    2. Metasploit nokogiri fixer
    3. beef nokogiri fixer
    4. Setup storage in Termux
    5. Restore official source list
    6. Beef bundle not install Fix (thread,nokogiri,gem file fix)
    ==============================================
    7. Exit
    ==============================================
    """, 'green'))
 Fix = raw_input("stark > ")
 if Fix == "1":
     os.system("mkdir -p $PREFIX/var/lib/postgresql")
     os.system("initdb $PREFIX/var/lib/postgresql")
     os.system("pg_ctl -D $PREFIX/var/lib/postgresql start")
     print(colored("""FIXED.!""", "green"))
     print_slow(colored("""if you get this error again by again\n so fix from here ok. :)""","red"))
 
 elif Fix == "2":
     os.system("bundle config build.nokogiri --use-system-libraries")
     os.system("bundle install")
 
 elif Fix == "4":
 	print_slow(colored("""Fixing storage\n""", "green"))
 	os.system("termux-setup-storage")
        print_slow(colored("""Fixed..!""", "green"))
 
 elif Fix == "3":
     os.system("cd $PREFIX/share/beef-xss && gem install nokogiri")
     print_slow(colored("FIXED !", 'green'))
     
 elif Fix == "5":
     os.system("wget https://www.dropbox.com/s/tntdeo1q9bpwc6c/sources.list")
     os.system("rm -rf /data/data/com.termux/files/usr/etc/apt/sources.list")
     os.system("rm -rf /data/data/com.termux/files/usr/etc/apt/sources.list.d")
     os.system("mv sources.list /data/data/com.termux/files/usr/etc/apt/")

 elif Fix == "6":
 	os.system("cd $PREFIX/share/beef-xss && bundle install")
	backtomenu()

 elif Fix == "7":
     os.system("clear")
     restartprogram()
     
 elif info == "0":
     restartprogram()
 else:
	print_slow(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
	os.system("clear")
	restartprogram()

def shellphish():
 print_slow(colored("installing shellphish", 'red'))
 os.system("git clone https://github.com/thelinuxchoice/shellphish")
 os.system("mv shellphish ~")
 backtomenu()
 
def Ohmyzsh():
 print_slow(colored("New look for termux with\ncool features", 'cyan'))
 os.system(" https://github.com/aniketstark/ohmyzsh")
 os.system("mv ohmyzsh")
 backtomenu()

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
	print '###### installing facebook hack'
	os.system('apt install python2')
	os.system('cd && mkdir facebookhack')
	os.system('wget https://www.dropbox.com/s/4d72hyfwrii5vw7/facebook.py ')
	os.system('mv facebook.py $HOME/facebookhack')
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

def Mbf():
    print_slow(colored("installing MBF", 'green'))
    os.system("wget https://www.dropbox.com/s/6p3xdm8en3b2cn9/MBF.zip")
    os.system("unzip MBF.zip")
    os.system("rm -rf MBF.zip")
    os.system("mv MBF ~")
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
	os.system("wget https://Auxilus.github.io/metasploit.sh")
	os.system("chmod +x metasploit.sh")
	os.system("mv metasploit.sh ~")
	print_slow(colored("now run sh metasploit.sh", 'green'))
	backtomenu()
		
def tload():
	os.system("wget https://www.dropbox.com/s/ql8ydqoiyk6h779/T-Load.zip")
	os.system("unzip T-Load.zip")
	os.system("rm -rf T-Load.zip")
	os.system("mv T-Load ~")
	backtomenu()
	
def lazymeta():
	os.system("git clone https://github.com/aniketstark/LazyMeta")
	os.system("mv LazyMeta ~")
	backtomenu()
	
def Update():
	print_slow(colored("always update this tool ok.!", 'cyan'))
	print_slow(colored("updating.........\n", 'green'))
	os.system('git pull')
	restartprogram()

def Facebook():
	os.system("git clone https://github.com/xHak9x/fbi")
	os.system("mv fbi ~")

def dtect():
	os.system("git clone https://github.com/shawarkhanethicalhacker/D-TECT-1")
	os.system("mv D-TECT-1 ~")

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
	print_slow(colored("hi this is aniket stark welcome to my tool\nhahaha sorry thats a python2 script edit and create by me\nthanks to undeadsec,anonhacker,Stackoverflow.com\nfor more tools please support me and subscribe me\ni have youtube channel GamersTech330 .!", 'red'))
	backtomenu()

def gpst():
    os.system("wget https://www.dropbox.com/s/x3zmgz1fjd8b4od/gps.zip")
    time.sleep(2)
    os.system("unzip gps.zip")
    os.system("mv gps ~")
    os.system("rm -rf gps.zip")
