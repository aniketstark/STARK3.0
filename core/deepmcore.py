import os
import sys
from core.starkmcore import *

def deepstore():
 print(colored("""
     ==================================================
	   
	     ____
         /\  _`\
         \ \ \/\ \     __      __    _____
          \ \ \ \ \  /'__`\  /'__`\ /\ '__`\
           \ \ \_\ \/\  __/ /\  __/ \ \ \L\ \
            \ \____/\ \____\\ \____\ \ \ ,__/
             \/___/  \/____/ \/____/  \ \ \/
                                       \ \_\
                                        \/_/
 
     ==================================================
        1. My Blogger
        2. A Story (in progress)
        3. Phishing Websites (sites in search)
        4. Video on Termux Channels
        5. Play YouTube songs
     ==================================================
        6. log out
     ==================================================
        """, 'red'))

 deep = raw_input("stark > ")

 if deep == "1":
     blog()
 elif deep == "4":
 	os.system("clear")
        Youtube()
 elif deep == "3":
 	fish()
 elif deep == "5":
 	os.system("mpsyt")
 elif deep == "6":
     os.system("clear")
     restartprogram() 
 elif deep == "0":
     restartprogram()
 else:
        print_slow(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
        os.system("clear")
        restartprogram() 

def Youtube():
 os.system("clear")
 print(colored("""
  ===========================================================
 .##....##..#######..##.....##.########.##.....##.########..########
  ..##..##..##.....##.##.....##....##....##.....##.##.....##.##......
  ...####...##.....##.##.....##....##....##.....##.##.....##.##......
  ....##....##.....##.##.....##....##....##.....##.########..######..
  ....##....##.....##.##.....##....##....##.....##.##.....##.##......
  ....##....##.....##.##.....##....##....##.....##.##.....##.##......
  ....##.....#######...#######.....##.....#######..########..########
 The YouTubers are work for you
  Every Time ok thats not greate slogan :-[^_^
 ===========================================================
 1. GamersTech330
 2. Hax4us
 3. TechzIndia
 4. msfconsole tutorial
 5. kaburan
 6. arif tech
 ==================================================
 7. Exit
 ==================================================
 """, "red"))
 
 yt = raw_input("stark > ")
 
 if yt == "1":
 	gt330()
 elif yt == "2":
 	h4us()
 elif yt == "3":
 	tzi()
 elif yt == "4":
 	mt()
 elif yt == "5":
     kabu()
 elif yt == "6":
     at()
 elif yt == "7":
     os.system("clear")
     restartprogram() 
 elif deep == "0":
     restartprogram()
 else:
        print_slow(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
        os.system("clear")
        restartprogram() 


def blog():
 os.system("termux-open-url http://gamerstech330.blogspot.com/\?m\=1/")
 
def gt330():
	os.system("termux-open-url https://www.youtube.com/channel/UCjb4zsUpNuSSaCCUirQL_sQ")
	
def h4us():
	os.system("termux-open-url https://www.youtube.com/channel/UCvgw7hn5zgYvPqDVGPJj8cA")
	
def tzi():
	os.system("termux-open-url https://www.youtube.com/channel/UCDBs1lz_JFoTH4tHP8Q6quQ")
	
def mt():
	os.system("termux-open-url https://www.youtube.com/channel/UCS4quzdHANFLDF4zhSOlnhw")
	
def kabu():
	os.system("termux-open-url https://www.youtube.com/channel/UCIDNGto4ovSZthfJ4PbKrBQ")
	
def at():
	os.system("termux-open-url https://www.youtube.com/channel/UC816dYxiEkAErUaadm2FeUA")

def fish():
	print_slow(colored("i am searching the sites\nso be patiens.......", 'green'))
 
backtomenubanner = """
BACK TO MENU ?
[1] YES
[2]  NO"""

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

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
