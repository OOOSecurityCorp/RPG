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
	print (green + bold +"[coded by  NakedSecurity]" + bold + green)
	t.sleep(0.5)
	print (yellow + bold + "==> github: https://www.github.com/NakedSecurity.git <==" +bold +yellow)
	print (" ")
	t.sleep(0.7)
	start = input("type start to proceed...  ")
	if start != "start":
		t.sleep(0.3)
		print (red +"invalid input!")
		exit()
	else:
		try :
			t.sleep(0.5)
			length = int(input(cyan+ bold+  "Enter the length of the password :   "+ bold + cyan))
			print (yellow + bold + ":::::>password generator<:::::" + bold + yellow)
			print ("  ")
			t.sleep(0.7)
			chara = "abcdefghijklmnopqrstuvwxyz0123456789@#$&%^*"
			password = (green + bold + " " + bold + green)
			for x in range(length):
				password += random.choice(chara)
				
			t.sleep(1.0)
			print (password)
			print ("  ")
			t.sleep(0.6)
			print (yellow +bold + "==> here is the password you requested for <==" +bold +yellow)
			print ("  ")
			t.sleep(1.5)
			print (green + bold +"*****THANK YOU FOR USING ME*****"+bold + green)
			
		except :
			t.sleep(0.7)
			print (red +"invalid input!")
			
if __name__ == "__main__":
	passwd()
