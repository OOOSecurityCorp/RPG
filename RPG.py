#-*-coding: utf-8-*-#
#//imports//#
import random
import pyfiglet
import os
import time as t
os.system("clear")
def passwd():
	#colors
	yellow =  '\033[93m'
	white = '\033[0m'
	green = '\033[92m'
	cyan = '\033[96m'
	pink ='\033[95m'
	red ='\033[91m'
	bold = '\033[1m'
	header = pyfiglet.figlet_format("RPG", font = "slant")
	
	#code
	t.sleep(0.3)
	print (red + bold+ header +red + bold +'\033[0m')
	print (" ")
	t.sleep(0.5)
	print (green + bold +"[coded by  000SecurityCorp]" + bold + green)
	t.sleep(0.5)
	print (yellow + bold + "[github: https://www.github.com/OOOSecurityCorp.git ]" +bold +yellow)
	print (" ")
	try :
			t.sleep(0.5)
			length = int(input(cyan+ bold+  "Enter the length of the password :   "+ bold + cyan))
	except :
			t.sleep(0.7)
			print (red +"invalid input!")
			passwd()
	print (yellow + bold + "[-] GENERATING PASSWORD" + bold + yellow)
	print ("  ")
	t.sleep(0.7)
	chara = "abcdefghijklmnopqrstuvwxyz0123456789@#$&%*"
	password = (green + bold + " " + bold + green)
	for x in range(length):
		password += random.choice(chara)
				
	t.sleep(1.0)
	print ("[+] PASSWORD: "+white+ password)
	print ("  ")
	t.sleep(0.6)
	#print (yellow +bold + "==> here is the password you requested for <==" +bold +yellow)
	print ("  ")
	t.sleep(1.5)
	print (green + bold +"*****THANK YOU FOR USING ME*****"+bold + green)
	con = input("[#] Do You Want To Continue(y/n)?? ")
	if con == "y" or con == "Y":
		passwd()
	elif con == "n" or con == "N":
		print ("[~] Aborting...")
		t.sleep(0.9)
		exit(1)
	else:
		print ('[!] Wrong Input!!!')
		t.sleep(0.2)
		print ("[×] Abouting Script....")
		t.sleep(0.9)
			
if __name__ == "__main__":
	passwd()
