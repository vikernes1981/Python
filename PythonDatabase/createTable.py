#!/usr/bin/python

import sqlite3
import os.path
from sqliteShow import sqliteShow

def createTable(dataname, tables):
	conn = sqlite3.connect(dataname)
	conn.execute('''CREATE TABLE %s
				(ID INT PRIMARY KEY     NOT NULL,
				NAME           TEXT     NOT NULL,
				SURNAME		   TEXT		NOT NULL,
				AGE            INT      NOT NULL,
				ADDRESS        CHAR(50) NOT NULL,
				EMAIL		   CHAR(50) NOT NULL,
				TELEPHON	   INT		NOT NULL,
				SALARY         REAL		NOT NULL);''' % tables)
	print "Table created successfully";
	print "Table row names are : NAME, SURNAME, AGE, ADDRESS, EMAIL,TELEPHON, SALARY"
	while True:
		print "Do you want to insert values now? : (y/n)"
		answer = raw_input("Enter your choice here : ")
					
		if answer == "y" or answer == "Y":
			name = raw_input("Name : ")
			surname = raw_input("Surname : ")
			age = int(raw_input("Age : "))
			address = raw_input("Address : ")
			email = raw_input("Email : ")
			telephon = int(raw_input("Tel : "))
			salary = int(raw_input("Salary : "))
			conn.execute("INSERT INTO %s (ID,NAME,SURNAME,AGE,ADDRESS,EMAIL,TELEPHON,SALARY) \
			VALUES (1, '%s', '%s', %d, '%s','%s', %d, %d )" % (tables, name, surname, age, address, email, telephon, salary));
			conn.commit()
			print "\n"
						
			sqliteShow(dataname, tables)
							
			conn.close()
			break
		elif answer == "n" or answer == "N":
			print "Operation done successfully.Nothing changed";
			conn.close()
			break
		else:
			continue
