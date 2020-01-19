import os
import sys
from time import sleep as timeout
from core.starkmcore import *
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
			    3.0(BETA)
>> CREATED BY:ANIKET STARK
>> Youtube:   GamersTech330
>> Instagram: @aniketstark330
>>>ONLY FOR TERMUX<<<

===============================================
1. Basic Command
2. Account Hacking
3. Website Hacking
4. Hash Cracker
5. Termux
6. Error Fixer
7. Credits
8. Follow Me!
9. Open Old Stark2.0
================================================
10. EXIT
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
        sys.exit()
    elif stark == "0":
          reset()
    else:
                  print  (colored("ERROR: WRONG COMMAND BRO.?", 'red'))
                  timeout(2)
                  reset()
