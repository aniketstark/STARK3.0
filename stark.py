import os
import sys
from time import sleep as timeout
from core.starkmcore import *
from termcolor import colored

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

>>CREATED BY:ANIKET STARK
>>SUBSCRIBE CHANNEL:Aniketstark tech

>>Fuck ya<<
>>>ONLY FOR TERMUX<<<

===============================================
1. Account Hacking
2. Information Gathering
3. Website Hacking
4. Termux
5. Update
6. About
================================================
7. EXIT
""", 'green'))

loop = True

while loop:
    menu()
    stark = raw_input("stark > ")
    
    if stark == "1":
    	  os.system("clear")
          achacking() 
    elif stark == "2":
    	  os.system("clear")
          info()
    elif stark == "3":
    	  os.system("clear")
          webhacking()
    elif stark == "4":
    	  os.system("clear")
    	  termux()
    elif stark == "5":
          Update()
    elif stark == "6":
          About()
    elif stark == "7":
    	sys.exit()
    elif stark == "0":
          restartprogram()
    else:
		  print  (colored("ERROR: WRONG COMMAND BRO.?", 'red'))
		  timeout(2)
		  restartprogram()
