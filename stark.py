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
    print(colored("""
         ..######..########....###....########..##....##
         .##....##....##......##.##...##.....##.##...##.
         .##..........##.....##...##..##.....##.##..##..
         ..######.....##....##.....##.########..#####...
         .......##....##....#########.##...##...##..##..
         .##....##....##....##.....##.##....##..##...##.
         ..######.....##....##.....##.##.....##.##....##
			       3.0
 >> CREATED BY:ANIKET STARK and Unknown_Girl
 >> Youtube:   GamersTech330
 >> Instagram: @aniketstark330
 >>>ONLY FOR TERMUX<<<

 ===============================================
 1. Basic Command
 2. Account Penatration
 3. Website Penetration
 4. Hash Cracker
 5. Termux
 6. Error Fixer
 7. Credits
 8. Follow Me!
 9. Open Old Stark2.0
 10. Hacker Movies
 G. Guide
 A. Start Assistant
 ================================================
 11. EXIT
 """, 'green'))

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
    elif stark == "7":
          Credits()
    elif stark == "8":
         os.system("clear")
         follow()
    elif stark == "9":
	 os.system("cd modules/STARK2.0/ && python2 stark.py")
    elif stark == "10":
     movie()
    elif stark == "11":
        sys.exit()
    elif stark == "secret" or stark == "secretfile" or stark == "69":
	secretcheck()
    elif stark == "nano starkmcore.py" or stark == "config":
         os.system("echo WOW WOW THIS DEVELOPER MODE ARE YOU!| lolcat -a -d 50")
	 os.system("echo DEVELOPER MODE START IN 10 Seconds | lolcat -a -d 100")
   	 os.system("cd core/ && nano starkmcore.py")
    elif stark == "0":
          reset()
    elif stark == "G" or stark == "g":
        guidemain()
    elif stark == "A" or stark == "a":
	 os.system("echo This Is Under Built Me And Unknown_Girl404 Working On It | lolcat -a -d 80")
    else:
                  print  (colored("ERROR: WRONG COMMAND BRO.?", 'red'))
                  timeout(1.5)
                  reset()
