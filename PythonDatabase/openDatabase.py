#!/usr/bin/python

import sqlite3
import os.path

'''
Checking if database exists else it creates one
'''
def openDatabase(dataName):
	#Check if db exists
	if os.path.isfile(dataName):
		print "Database exists.Connecting...\n"
		conn = sqlite3.connect(dataName)
		print "Opened database successfully";
		res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
		print "Name of tables : \n"
		for name in res:
			print name[0],
		print "\n"
		conn.close()
	else:
		#Create new db else quit
		print "Database does not exist.Should I create it? (y/n)\n"
		answer = raw_input("Enter your choice here : ")
		if answer == "y":
			conn = sqlite3.connect(dataName)
			print "Created and opened database successfully\n";
			conn.close()
		else:
			print "Quiting!"
			conn.close()
