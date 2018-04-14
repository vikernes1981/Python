#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  diceRoller.py
#  
#  Copyright 2018 penjo <penjo@vik3rn35>
#  
#  

from random import randint

def main():
	answer = 'y'
	while answer == 'y' or answer == 'Y':
		NoD = raw_input("How many dices you want to roll? : ")
		while NoD.isdigit() != True:
			print("Give a number not a letter!")
			NoD = raw_input("How many dices : \n")
		print "1: 4-sided\n2: 6-sided\n3: 8-sided\n4: 10-sided\n5: 12-sided\n6: 16-sided\n7: 20-sided\n"
		sides = raw_input("Roll the dices : \n")
		while sides.isdigit() != True:
			print("Give a number not a letter!")
			sides = raw_input("Roll the dices : \n")
		while int(sides) <= 0 or int(sides) > 7:
			print("Give a valid number!")
			sides = raw_input("Roll the dices : \n")
		for i in range(int(NoD)):
			if int(sides) == 1:
				a = randint(1,4)
				print "You rolled a 4-sided dice!"
				if a == 4:
					print "Your roll is : ", a
					print "PERFECT ROLL!!"
				else:
					print "Your roll is : ", a
			elif int(sides) == 2:
				a = randint(1,6)
				print "You rolled a 6-sided dice!"
				if a == 6:
					print "Your roll is : ", a
					print "PERFECT ROLL!!"
				else:
					print "Your roll is : ", a
			elif int(sides) == 3:
				a = randint(1,8)
				print "You rolled an 8-sided dice!"
				if a == 8:
					print "Your roll is : ", a
					print "PERFECT ROLL!!"
				else:
					print "Your roll is : ", a
			elif int(sides) == 4:
				a = randint(1,10)
				print "You rolled a 10-sided dice!"
				if a == 10:
					print "Your roll is : ", a
					print "PERFECT ROLL!!"
				else:
					print "Your roll is : ", a
			elif int(sides) == 5:
				a = randint(1,12)
				print "You rolled a 12-sided dice!"
				if a == 12:
					print "Your roll is : ", a
					print "PERFECT ROLL!!"
				else:
					print "Your roll is : ", a
			elif int(sides) == 6:
				a = randint(1,16)
				print "You rolled a 16-sided dice!"
				if a == 16:
					print "Your roll is : ", a
					print "PERFECT ROLL!!"
				else:
					print "Your roll is : ", a
			elif int(sides) == 7:
				a = randint(1,20)
				print "You rolled a 20-sided dice!"
				if a == 20:
					print "Your roll is : ", a
					print "PERFECT ROLL!!"
				else:
					print "Your roll is : ", a
				
		answer = raw_input("Do you want to roll again? (y/n) :")
	return 0

if __name__ == '__main__':
	main()

