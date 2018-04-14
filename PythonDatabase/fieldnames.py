#!/usr/bin/python

def fieldNames():
	field1 = []
	while True:
		
		value = raw_input("Enter name of field : ")
		field1.append(value.upper())
		print "Do you want to add more fields? "
		answer = raw_input("y/n : ")
		if answer == "y":
			continue
		elif answer == "n":
			break
	for n in field1:
		print "%s" % n
	
fieldNames()
