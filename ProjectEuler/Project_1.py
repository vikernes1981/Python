#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euler1.py
#
#  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#  The sum of these multiples is 23.
#
#  Find the sum of all the multiples of 3 or 5 below 1000.
#  
#  


def main(args):
	
	summ = 0
	summlist = []
	for i in range(1,1000):
		if i % 3 == 0 or i % 5 == 0:
			print i
			summ += i
	print summ

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
