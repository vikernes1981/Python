#!/usr/bin/python

import sqlite3
import os.path
from sqliteShow import sqliteShow

'''
Updates values of data in desired table
'''
def updateValues(dataname, tables):
	conn = sqlite3.connect(dataname)
	
	id1 = "ID"
	name1 = "NAME"
	surname1 = "SURNAME"
	age1 = "AGE"
	address1 = "ADDRESS"
	email1 = "EMAIL"
	telephon1 = "TELEPHON"
	salary1 = "SALARY"
	#UPDATE existing data

				
	# print table values BEFORE change
	sqliteShow(dataname, tables)
	while True:					
		print "Do you want to insert values now? : (y/n)"
		answer = raw_input("Enter your choice here : ")
					
		if answer == "y" or answer == "Y":
			while True:
				print "1) ID "
				print "2) NAME "
				print "3) SURNAME "
				print "4) AGE "
				print "5) ADDRESS "
				print "6) EMAIL "
				print "7) TELEPHON "
				print "8) SALARY "
				updateAnswer = int(raw_input("Which value do you want to update? : "))
				#update ID
				if updateAnswer == 1:
					secondaryId = int(raw_input("ID # of value you want changed : "))
					primaryId = int(raw_input("New ID : "))
					conn.execute("UPDATE %s SET '%s' = %d WHERE ID = %d" % (tables, id1, primaryId, secondaryId))
					conn.commit()
					print "Total number of rows updated :", conn.total_changes
					print "\nChanges made!"
								
					sqliteShow(dataname, tables)

					conn.close()
					break
					#update Name
				elif updateAnswer == 2:
					secondaryId = int(raw_input("ID # of value you want changed : "))
					name = raw_input("New name : ")
					conn.execute("UPDATE %s SET '%s' = '%s' WHERE ID = %d" % (tables, name1, name, secondaryId))
					conn.commit()
					print "Total number of rows updated :", conn.total_changes
					print "\nChanges made!"
								
					sqliteShow(dataname, tables)

					conn.close()
					break
				#update Surname
				elif updateAnswer == 3:
					secondaryId = int(raw_input("ID # of value you want changed : "))
					surname = (raw_input("New surname : "))
					conn.execute("UPDATE %s SET '%s' = '%s' WHERE ID = %d" % (tables, surname1, surname, secondaryId))
					conn.commit()
					print "Total number of rows updated :", conn.total_changes
					print "\nChanges made!"
								
					sqliteShow(dataname, tables)

					conn.close()
					break
				#update Age
				elif updateAnswer == 4:
					secondaryId = int(raw_input("ID # of value you want changed : "))
					age = int(raw_input("New age : "))
					conn.execute("UPDATE %s SET '%s' = %d WHERE ID = %d" % (tables, age1, age, secondaryId))
					conn.commit()
					print "Total number of rows updated :", conn.total_changes
					print "\nChanges made!"
								
					sqliteShow(dataname, tables)

					conn.close()
					break	
				#update Address
				elif updateAnswer == 5:
					secondaryId = int(raw_input("ID # of value you want changed : "))
					address = raw_input("New address : ")
					conn.execute("UPDATE %s SET '%s' = '%s' WHERE ID = %d" % (tables, address1, address, secondaryId))
					conn.commit()
					print "Total number of rows updated :", conn.total_changes
					print "\nChanges made!"
									
					sqliteShow(dataname, tables)
								
					conn.close()
					break
				#update Email
				elif updateAnswer == 6:
					secondaryId = int(raw_input("ID # of value you want changed : "))
					email = raw_input("New e-mail : ")
					conn.execute("UPDATE %s SET '%s' = '%s' WHERE ID = %d" % (tables, email1, email, secondaryId))
					conn.commit()
					print "Total number of rows updated :", conn.total_changes
					print "\nChanges made!"
									
					sqliteShow(dataname, tables)
												
					conn.close()
					break
				#update Telephon
				elif updateAnswer == 7:
					secondaryId = int(raw_input("ID # of value you want changed : "))
					telephon = int(raw_input("New Telephon : "))
					conn.execute("UPDATE %s SET '%s' = %d WHERE ID = %d" % (tables, telephon1, telephon, secondaryId))
					conn.commit()
					print "Total number of rows updated :", conn.total_changes
					print "\nChanges made!"
								
					sqliteShow(dataname, tables)

					conn.close()
					break
				#update Salary
				elif updateAnswer == 8:
					secondaryId = int(raw_input("ID # of value you want changed : "))
					salary = int(raw_input("New salary # : "))
					conn.execute("UPDATE %s SET '%s' = %d WHERE ID = %d" % (tables, salary1, salary, secondaryId))
					conn.commit()
					print "Total number of rows updated :", conn.total_changes
					print "\nChanges made!"
								
					sqliteShow(dataname, tables)
								
					conn.close()
					break
				else:
					print "Nothing changed.Try again!";
					continue
		elif answer == "n" or answer == "N":
			print "Operation done successfully.Nothing changed";
			conn.close()
			break
		else:
			continue
