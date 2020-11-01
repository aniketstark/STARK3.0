# encoding: utf-8
import os
import sys
from time import sleep as timeout
from core.starkmcore import *
from core.guidemcore import *
from multiprocessing import Process
from termcolor import colored

checkfile()
def menu():
 os.system("clear")
 print colored("""
         ..######..########....###....########..##....##
         .##....##....##......##.##...##.....##.##...##.
         .##..........##.....##...##..##.....##.##..##..
         ..######.....##....##.....##.########..#####...
         .......##....##....#########.##...##...##..##..
         .##....##....##....##.....##.##....##..##...##.
         ..######.....##....##.....##.##.....##.##....##
			       3.0
 >> CREATED BY:ANIKET STARK and Unknown_Girl404
 >> Youtube:   GamersTech330
 >> Instagram: @aniketstark330
 >>>ONLY FOR TERMUX<<<

 ===============================================
 1. Basic Command
 2. Account Penetration
 3. Website Penetration
 4. Hash Cracker
 5. Termux
 6. Error Fixer
 7. Open Old STARK2.0""","green"), colored("""
 I. Important Application's""","cyan", attrs=['bold']), colored("""
 M. Hacking Movie's""","green"), colored("""
 S. Secret			There Is No Secret0_0""","red", attrs=['bold']), colored("""
 F. Follow Us""","magenta", attrs=['bold']), colored("""
 C. Credits""","white", attrs=['bold']), colored("""
 U. Update""","blue", attrs=['bold']), colored("""
 ================================================""","green"), colored("""
 H. Help""","yellow", attrs=['bold']), colored("""
 E. EXIT
 ================================================
 """,'green')

loop = True

while loop:
    menu()
    stark = raw_input("stark > ")

    if stark == "1":
          os.system("clear")
          BasicC()
    elif stark == "2":
          os.system("clear")
          AccountH()
    elif stark == "3":
          os.system("clear")
          WebH()
    elif stark == "4":
          os.system("clear")
          HASH()
    elif stark == "5":
          os.system("clear")
          Termux()
    elif stark == "6":
          EFixer()
    elif stark == "i" or stark == "I":
		 checkofflineapp()
		 impapp()
    elif stark == "c" or stark == "C":
          Credits()
    elif stark == "f" or stark == "F":
         os.system("clear")
         follow()
    elif stark == "7":
	 os.system("cd modules/STARK2.0/ && python2 stark.py")
    elif stark == "m" or stark == "M":
		 movie()
    elif stark == "e" or stark == "E":
        sys.exit()
    elif stark == "secret" or stark == "S" or stark == "s":
		 os.system("echo Server Starting 5sec | lolcat -a -d 500")
		 os.system("termux-open http://localhost:8080")
		 os.system("cd modules/ && php -S localhost:8080 -t Secret")
    elif stark == "nano starkmcore.py" or stark == "config":
         os.system("echo WOW WOW THIS DEVELOPER MODE | lolcat -a -d 50")
         os.system("echo DEVELOPER MODE START IN 10 Seconds | lolcat -a -d 100")
         os.system("cd core/ && nano starkmcore.py")
    elif stark == "0":
         reset()
    elif stark == "H" or stark == "h":
         guidemain()
    elif stark == "u" or stark == "U":
		 printslow(colored("""THIS OPTION WILL UPDATE ONLY MAIN PACKAGES NOT THIS TOOL""","green"))
		 os.system("echo UPDATING SOME IMPORTANT PACKAGES | lolcat -a -d 50")
		 os.system("apt update && apt full-upgrade")
		 os.system("pkg install -y python python2 mpv ffmpeg git wget pv termux-api ruby php zip")
		 os.system("echo DONE | lolcat -a -d 90")
    elif stark == "A" or stark == "a":
		 os.system("echo ai feature is under work | lolcat -a -d 100")
		 os.system("cd core/ && python2 ai.py")
    else:
                  print  (colored("ERROR: WRONG COMMAND BRO.?", 'red'))
                  timeout(1.5)
                  reset()
                  
