import os
import sys
import time
from time import sleep as timeout
from multiprocessing import Process
from termcolor import colored

def printslow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def troubleshoot():
 print colored("""
  =========================================""","white"), colored("""
  1. Why tool is not starting/running
  2. Why intool is crashing""","green"), colored("""
  =========================================""","green")
 trouble = raw_input("trouble > ")
 if trouble == "1":
   printslow (colored("""ok tool is not starting because of the tool is not\nexist in modules folder thats why tool is not running\n and plus you using old modules you need \nto run this command in stark3.0\n\n rm -rf modules\n then\n\nbash install.sh""","green"))
 elif trouble == "2":
   printslow (colored("""in tools are crashing because of they are not stable thats why\nor\nyou didn't install important package of that tool\nreport if tool is not working on instagram @aniketstark330 or on GitHub""","green"))

troubleshoot()
