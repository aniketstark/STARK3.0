import os
import sys
import time
from termcolor import colored
from core.starkmcore import *
import random
import urllib

######Functions
def reset():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
        
def netcheck():
 print(colored("""CHECKING INTERNET ON/OFF""", "green"))
 try :
    stri = "https://www.google.co.in"
    data = urllib.urlopen(stri)
    print "Connected"
 except:
    print(colored("""THIS TOOL REQUIRE INTERNET""", "red"))
    exit()


def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
        

########MainMenu
def guidemain():
    os.system("clear")
    print colored("""
    =========================================""","white"),colored("""
                      GUIDE                  ""","cyan"),colored("""
    =========================================""","white"),colored("""
    1. How To Install Metasploit Framework
    2. How To Install GUI In Termux
    3. How To Install Kali Nethunter
    4. How To Install Kali GUI""","green"),colored("""
    =========================================""","white"),colored("""
    5. Back""","green"),colored("""
    =========================================""","white")
    guide = raw_input("GUIDE > ")
    if guide == "1":
        installmetasploit()
    elif guide == "2":
        installguitermux()
    elif guide == "3":
        installkalinethunter()
    elif guide == "4":
        installkaligui()
    elif guide == "5":
        reset()
    else:
        os.system("echo Wrong Choice | lolcat -a -d 40")
        guidemain()
        
def installmetasploit():
    printslow(colored("""Ok Now Lets Install Metasploit Framework Just Follow Me\n1. Open New Session/Terminal\n\n2. Now Enter This Command-:\n pkg install unstable-repo metasploit\n\nThats It\n\n""","green"))
    os.system("echo Screen Back in 25s | lolcat -a -d 250")
    guidemain()
    
def installguitermux():
    printslow(colored("""Ok Now We Install GUI (Graphical User Interface) Termux\n""","green"))
    printslow(colored("""So Please Try To Understand Perfectly\n\n""", "red"))
    printslow(colored("""1. Open New Session/Terminal\n\n""","green"))
    printslow(colored("""2. Enter this command-:\n""","green"))
    printslow(colored(""" pkg install -y update tigervnc\n\n""","green"))
    printslow(colored("""3. Now Type "vncserver" and hit enter\nnow it will ask you enter password\nso enter pass whatever you want\nthen it will start session 1 now\n\n""","green"))
    printslow(colored("""4. Now need to insstall vncviewer from playstore\n i am redirecting you\n\n""","green"))
    os.system("termux-open https://play.google.com/store/apps/details\?id\=com.realvnc.viewer.android")
    printslow(colored("""5. Now you need to setup vnc connection\nIn VNCviewer so lets do it\nclick on plus button and setup adress like this -:\n localhost::5901\n  In Name choose whatever you want\n clik on ok/connect enter pasword that you enter when you seting pass in vncserver\n""","green"))
    printslow(colored("""\n\nPlease Remember These Things\n""","red"))
    printslow(colored("""Whenever you start vncserver don't forgot to close\nfor clossing use this command-:\nvncserver -kill :1\n\n""","green"))
    printslow(colored("""Some Pepole get confused what is 5901\nWhat is Vncserver:1""","red"))
    printslow(colored("""So 5901 its port of your session\nvncserver:1 its number of your session\nAnd you can open multiple sesseion like that-:\nvncserver:2\nvncserver:3\n....and more\n\n""","green"))
    printslow(colored("""So Don't Forgot to Closed it""","red"))
    os.system("echo Screen Back in 25s | lolcat -a -d 250")
    guidemain()

def installkalinethunter():
    printslow(colored("""Kali Nethunter Not bad not bad XD\n\n""","green"))
    printslow(colored("""first of all i am gonna redirect you on official page\n""","green"))
    printslow(colored("""Because of sometime links get change or new update""","green"))
    os.system("termux-open ")
    os.system("echo Guiding continue in 30s | lolcat -a -d 300")
    printslow(colored("""\n1. Open termux new session/terminal\n\n""","green"))
    printslow(colored("""2. Enter This command-:\ntermux-setup-storage\npkg install wget\nwget -O install-nethunter-termux https://offs.ec/2MceZWr\nchmod +x install-nethunter-termux\n./install-nethunter-termux\n\n""","green"))
    printslow(colored("""3. Now you can run nethunter with using this command-:\n nethunter\n\n""","green"))
    printslow(colored("""IMPORTANT WHEN NETHUNTER IS INSTALLED\n\n""","red"))
    printslow(colored("""run this command in nethunter\n""","green"))
    printslow(colored("""apt update && apt full-upgrade\n\n""","green"))
    printslow(colored("""If Yoy Have More Storage So Enter This Command\napt install kali-linux-full\n""","green"))
    os.system("echo Screen Back in 25s | lolcat -a -d 250")
    guidemain()

def installkaligui():
    printslow(colored("""So Official website says that you can install\nGUI Kali Nethunter with kex: Yeah but there errors like\n1. proot errors\n2. GUI connection not establishing\nAnd maybe more.....\n\n""","green"))
    printslow(colored("""So Now Forgot About those error\n Now we install kali GUI in termux\n\n""","green"))
    printslow(colored("""NETHUNTER INSTALLED RECOMMENDED XD\n\n""","red"))
    printslow(colored("""1. Start Nethunter in new terminal/session\n\n""","green"))
    printslow(colored("""2. Enter this command in nethunter-:\napt update && apt install tigervnc\n\n""","green"))
    printslow(colored("""3. Now Type this Command-:\n vncserver\n Now it will ask you enter password\n so enter the password\n now it will ask you again\n do you want set pass on view only mode\n so choose n\nNow Thats All Your Setup is Done Now\n\n""","green"))
    printslow(colored("""Now Setup is Done Now i am gonna redirect you\n For install VNC Viewer app from playstore""","green"))
    os.system("termux-open https://play.google.com/store/apps/details\?id\=com.realvnc.viewer.android")
    os.system("echo Guide will continue in 10s | lolcat -a -d 100")
    printslow(colored("""\n\nNow you need to setup vnc connection\nIn VNCviewer so lets do it\nclick on plus button and setup adress like this -:\n localhost::5901\n  In Name choose whatever you want\n clik on ok/connect enter pasword that you enter when you seting pass in vncserver\n""","green"))
    printslow(colored("""\n\nPlease Remember These Things\n""","red"))
    printslow(colored("""Whenever you start vncserver don't forgot to close\nfor clossing use this command-:\nvncserver -kill :1\n\n""","green"))
    printslow(colored("""Some Pepole get confused what is 5901\nWhat is Vncserver:1""","red"))
    printslow(colored("""So 5901 its port of your session\nvncserver:1 its number of your session\nAnd you can open multiple sesseion like that-:\nvncserver:2\nvncserver:3\n....and more\n\n""","green"))
    printslow(colored("""So Don't Forgot to Closed it""","red"))
    os.system("echo Screen Back in 25s | lolcat -a -d 250")
    guidemain()
