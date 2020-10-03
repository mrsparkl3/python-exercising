#!/usr/bin/env python3
import os

#simple python script that makes it easier to use spd-say command on 
# Ubuntu. Make sure to add a proper alias to the bashrc file
# to run this script.
help= "\nSpd-say facilitator user, \nJust type something and your pc will say it.\nType \"quit\" to exit\n"
print(help)
while True:
	text= input("say something>")
	if text == "quit":
		break
	elif text == "help":
		print(help)
	else:
		cmd= "spd-say \'" +text + "\'"
		os.system(cmd)
		
