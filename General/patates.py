#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  patates.py
#  
#  Copyright 2017 penjo <penjo@vik3rn35>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Python 3.4.2



def main():
	
	gr = 0
	de = 0
	x = 0
	
	while gr < 1000 and de < 1000:
		
		patgr = int(input("How many potatoes Greece : "))
		patde = int(input("How many potatoes Germany : "))
		print("\n")
		
		if x == 0:
			maxgr = patgr
			maxde = patde
			
		if patgr > maxgr:
			maxgr = patgr
			
		if patde > maxde:
			maxde = patde

		gr = gr + patgr
		de = de + patde
		
		print("GR = %d, DE = %d \n" % (gr, de))
		x += 1
	
	mesosgr = gr // x
	mesosde = de // x
	
	print("Maximum number of potatoes Greece ever given was : %d" % maxgr)
	print("Maximum number of potatoes Germany ever given was : %d" % maxde)
	print("Mesos oros Greece : %d, mesos oros Germany : %d" % (mesosgr, mesosde))
	print("The number of times potatoes were given is : %d\n" % x)
	return 0

if __name__ == '__main__':
	main()

