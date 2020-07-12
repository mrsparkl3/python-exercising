#!/usr/bin/env python3
import os

#simple python script that makes it easier to use spd-say command on 
# Ubuntu. Make sure to add a proper alias to the bashrc file
# to run this script.
while True:
	text= input("say something>")
	cmd= "spd-say \'" +text + "\'"
	os.system(cmd)
	
