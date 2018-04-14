#!/usr/bin/python


'''
Funtion that show values of all tables in a database
'''
import sqlite3
import os.path

def sqliteShow(db, tabl):
	conn = sqlite3.connect(db)
	cursor = conn.execute("SELECT id, name, surname, age, address, email, telephon, salary from %s" % tabl)

	for row in cursor:
		print "ID = ", row[0],
		print "NAME = ", row[1],
		print "SURNAME = ", row[2]
		print "AGE = ", row[3],
		print "ADDRESS = ", row[4],
		print "EMAIL = ", row[5],
		print "TELEPHON = ", row[6],
		print "SALARY = ", row[7], "\n"
		
	conn.close()
