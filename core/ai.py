# -*- coding: utf-8 -*-
import os
#!/usr/bin/python
import sys
import time
from termcolor import colored
import os.path
import random

####ChatSystem
hi = ['whats up\n', 'oh hi\n', 'how are you\n']
####MainStart
def mainstart():
 loop = True
 while loop:
		ai = raw_input(">|")
		if ai == "hi" or ai == "hello":
		 printslow(colored(random.choice(hi),"green"))
		elif ai == "fine" or ai == "i am fine" or ai == "i am ok":
		 print colored("""Yokatta thats good for me""","green"), colored("""(๑>◡<๑)\n""","magenta")
		elif ai == "your cute" or ai == "you cute" or ai == "you so much cute" or ai == "your so cute" or ai == "you are so cute":
		 print colored("""Aarigato Gozaimasu i Mean Thanks Now your Blushing me\n""","cyan")
		elif ai == "i want to change your name" or ai == "can i change your name" or ai == "change your name":
		 os.system("termux-toast -b red -c black ")
		 printslow(colored("""h.. How rude you dont like my name (emoji)\n""","magenta"))
		 printslow(colored("""Deteike i am not chatting with you baka\n""","magenta"))
		 exit()
		elif ai == "what is your name" or ai == "tell me your name" or ai == "your name" or ai == "whats your name":
		 printslow(colored("""My Name Is aiko\n""","green"))
		elif ai == "who is your developer" or ai == "your developer name" or ai == "what is name of your developer" or ai == "tell me your developer name":
		 print colored("""My Developer is Aniket Stark And Sagiri sakamoto\n""","green")
		else:
		 printslow(colored("""hontoni gumenasai i am just small girl i dont have knowledge of that\n but next time i swear i will answer those questions(sad emoji)\n would you like to send your question to my hahao\n""","green"))
		 os.system("termux-open https://www.instagram.com/p/CC6Z-7pl26X/?igshid=s6xtswthidt0")
		elif ai == "are you japanese" or ai == "are you from japan" or ai == "are you japan" or ai == "you from japan":
		 printslow(colored("""iye iye iye i was born in linux\nso how can i be japanese?\n""","green"))
		elif ai == "because you use japanese words" or ai == "because you talk like japanese" or ai == "you act like japanese":
		 printslow(colored("""Hontoni anata mo baka desu.\nMy one developer is japanese thats why\ni am just same like her""","green"))
		
####Function

def netcheck():
 print(colored("""CHECKING INTERNET Connection""", "green"))
 try :
    stri = "https://www.google.co.in"
    data = urllib.urlopen(stri)
    print "Connected"
 except:
    printslow(colored("""hora hora check your internet connection""", "red"))
    exit()

def reset():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

PATH='./data/user.txt'

def checkfile():
 if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "Every thing is allright"
    os.system("clear")
 else:
	printslow(colored("""Hi I Am aiko\n\n""","green"))
	printslow(colored("""Are You Girl(G)/Boy(B)\n""","green"))
	gender = raw_input("gender > ")
	if gender == "b" or gender == "B" or gender == "Boy" or gender == "boy":
		printslow(colored("""Ok Please Enter Your Name Mr. Not Full Name ne;)\n""","green"))
		save_path = 'data/'
		completeName = os.path.join(save_path, "user.txt")
		file1 = open(completeName, "w")
		toFile = raw_input(">> ")
		file1.write("Mr. ")
		file1.write(toFile)
		file1.close()
	elif gender == "g" or gender == "G" or gender == "Girl" or gender == "girl":
		printslow(colored("""Ok Please Enter Your Name Miss. Not Full Name ne;)\n""","green"))
		save_path = 'data/'
		completeName = os.path.join(save_path, "user.txt")
		file1 = open(completeName, "w")
		toFile = raw_input(">> ")
		file1.write("Miss. ")
		file1.write(toFile)
		file1.close()

def checkupdate():
 printslow(colored("""\n\nCan I Update some Important Packages For you y/n""","green"))
 checku = raw_input(">| ")
 if checku == "y" or checku == "Y" or checku == "yes" or checku == "ok" or checku == "Yes":
	 netcheck()
	 printslow(colored("""INSTALLING AND UPDATING PACKAGES\n""","green"))
	 os.system("apt install -y update && pkg install -y mpv libcurl pv ruby  git curl php python python2 wget termux-api zip")
	 os.system("termux-toast -b cyan -c black Package Updated!")
	 printslow(colored("""\n\nInstalling And Update pip Python Modules\n""","green"))
	 os.system("pip2 install -y lolcat beautifulsoup4 termcolor argparse request pysocks")
	 os.system("termux-toast -b cyan -c black Modules Updated!")
	 mainstart()
	 
 elif checku == "n" or checku == "N" or checku == "no" or checku == "No":
	 printslow(colored("""ok""","green"))
	 os.system("clear")
 	 mainstart()

PATH='./data/user.txt'

def checkdatafile():
 if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "Every thing is allright"
 else:
    os.system("mkdir data")
    time.sleep(2)
	 
######OnBoot
def boot():
 checkdatafile()
 checkfile()
 f= open("data/user.txt")
 r=f.read(100)
 printslow(colored("""Hello ""","green")), printslow(r)
 checkupdate()
 exit()

boot()
mainstart()

######main
