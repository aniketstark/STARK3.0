import os
import sys
from time import sleep as timeout
from core.starkmcore import *
from termcolor import colored

def menu():

    print(colored("""
	 ..######..########....###....########..##....##
	 .##....##....##......##.##...##.....##.##...##.
	 .##..........##.....##...##..##.....##.##..##..
	 ..######.....##....##.....##.########..#####...
	 .......##....##....#########.##...##...##..##..
	 .##....##....##....##.....##.##....##..##...##.
	 ..######.....##....##.....##.##.....##.##....##

>>CREATED BY:ANIKETSTARK
>>SUBSCRIBE CHANNEL:Aniketstark tech

>>THIS IS VIDEO BETA VERSION<<
>>>ONLY FOR TERMUX<<<

===============================================
1. FACEBOOK HACK
2. INSTAGRAM HACK
3. LAZYMUX
4. RED_HAWK
5. SQL INJECTION
6. WEEMAN
7. SQL WEBSITE SCANNER
8. OhMyZsh (FOR TERMUX NEW LOOK)
9. InstaBot
================================================
10. EXIT
""", 'green'))

loop = True

while loop:
    menu()
    stark = raw_input("stark > ")
    
    if stark == "1":
          Facebookhack()
    elif stark == "2":
          Instagramhack()
    elif stark == "3":
          Lazymux()
    elif stark == "4":
    	  Redhawk()
    elif stark == "5":
          Sqli()
    elif stark == "6":
    	  Weeman()
    elif stark == "7":
    	   Sqlwebsitescanner()
    elif stark == "8":
    	   Ohmyzsh()
    elif stark == "9":
    	   Instabot()
    elif stark == "10":
    	   sys.exit()
    elif stark == "0":
          restartprogram()
    else:
		  print  (colored("ERROR: WRONG COMMAND BRO.?", 'red'))
		  timeout(2)
		  restartprogram()