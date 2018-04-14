#!/usr/bin/python

import sqlite3
import os.path
from sqliteShow import sqliteShow

'''
Inserts new data in desired table
'''
def updateTable(dataname, tables):
	conn = sqlite3.connect(dataname)
	
	sqliteShow(dataname, tables)
	while True:					
		print "Do you want to insert values now? : (y/n)"
		answer = raw_input("Enter your choice here : ")				
		if answer == "y" or answer == "Y":
			primaryId = int(raw_input("ID : "))
			name = raw_input("Name : ")
			age = int(raw_input("Age : "))
			surname = raw_input("Surname : ")
			address = raw_input("Address : ")
			email = raw_input("Email : ")
			telephon = int(raw_input("Tel : "))
			salary = int(raw_input("Salary : "))
			conn.execute("INSERT INTO %s (ID,NAME,SURNAME,AGE,ADDRESS,EMAIL,TELEPHON,SALARY) \
			VALUES (%d, '%s', %d, '%s','%s', %d )" % (tables, primaryId, name, surname, age, address, email, telephon, salary));
			conn.commit()
						
			print "\nChanges made!"
						
			#print table values AFTER changes
			sqliteShow(dataname, tables)
						
			conn.close()
			break
		elif answer == "n" or answer == "N":
			print "Operation done successfully.Nothing changed";
			conn.close()
			break
		else:
			continue
