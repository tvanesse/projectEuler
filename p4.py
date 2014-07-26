"""
Project Euler - Problem 4
Copyright (C) 2014  Thomas Vanesse

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
from __future__ import division
from pylab import *

def is_palindrome(n):
	# This is fucking elegant ! Got this from Peter Hull on Stack Overflow
	return str(n) == str(n)[::-1]
	

def p4():
	'''
	A palindromic number reads the same both ways. The largest palindrome made from the product of 
	two 2-digit numbers is 9009 = 91 x 99.
	
	Find the largest palindrome made from the product of two 3-digit numbers.
	'''
	# Brute force
	three_digit_numbers = range(100,1000,1)		# recall that range(a,b,1) returns [a, a+1, a+2, .., b-2, b-1]
	max_pal = (0, 0, 0)
	
	for a in three_digit_numbers:
		for b in three_digit_numbers:
			candid = a*b
			if is_palindrome(candid) and candid > max_pal[2] :
				max_pal = (a, b, candid)
	
	print(max_pal)
	return max_pal[2]

p4()

			
			
