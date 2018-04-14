#!/usr/bin/python

import sqlite3
import os.path
import sqliteShow
from openDatabase import *
from createTable import *
from updateTable import *
from updateValues import *

def DbCreation():
	
	data = raw_input("Name of database please : \n")
	data += ".db"

	while True:	
		
		openDatabase(data)
		answer = ""
		menuAnswer = 0
		
		if menuAnswer == 0:
			print "What do you want to do?" 
			print "1) Create new table"
			print "2) Update existing table?" 
			print "3) Update existing data of table?"
			print "4) Show existing tables?"
			print "5) Exit"
			menuAnswer = int(raw_input("\nEnter your choice here : "))
			if menuAnswer == 1:
				conn = sqlite3.connect(data)
				res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
				print "Name of tables : \n"
				for name in res:
					print name[0],
				print "\n"
				table = raw_input("Name of table you want to create please : ")
				createTable(data, table)

			elif menuAnswer == 2:
				conn = sqlite3.connect(data)
				res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
				print "Name of tables : \n"
				for name in res:
					print name[0],
				print "\n"
				table = raw_input("Name of table you want to update please : ")
				updateTable(data, table)

			elif menuAnswer == 3:
				conn = sqlite3.connect(data)
				res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
				print "Name of tables : \n"
				for name in res:
					print name[0],
				print "\n"
				table = raw_input("Name of table you want to update please : ")
				updateValues(data, table)

			elif menuAnswer == 4:
				conn = sqlite3.connect(data)
				res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
				print "Name of tables : \n"
				for name in res:
					print name[0],
				print "\n"
				table = raw_input("Name of table you want to show please : ")
				sqliteShow(data, table)
				
			elif menuAnswer == 5:
				print "Quiting, farewell!"
				break
					
DbCreation()
