"""
Project Euler - Problem 5
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

def p5(n):
	'''
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
	
	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to `n`?
	'''
	# From the problem, we know we can already start from 2520.
	# We also know that if a number is divisible by 20, then it must be divisible by 10 and 5.
	# Same reasoning for 12, 6 and 3, etc... So we can reduce the amount of numbers that need to
	# be tested to a very limited subset.
	# `n` should be between 11 and 20

	def test(cand, some_range):
		for i in some_range:
			if cand % i != 0:
				return False
		return True
	
	candid = 2520	
	for i in arange(12, n+1, 1):
		# It seems like trying to find the result for 11, then restart from
		# that result to find 12, then restart from that result to find 13,...
		# is more efficient than directly trying to browse through all the numbers
		# for my_range = arange(11, n+1, 1).
		my_range = arange(11, i+1, 1)
		print("Trying to find the answer for " + str(my_range))
		
		loop = True
		while loop:
			attemp = test(candid, my_range)
			if not attemp:
				candid += 1
			else :
				loop = False
		print("The answer for " + str(my_range) + " is " + str(candid))
	
	return candid
	
if __name__ == '__main__':
	import timeit
	print("Starting...")
	r = p5(20)
	print(r)
#	print(timeit.timeit("p5(20)", setup="from __main__ import p5", number=1))
	# Found in 6,88 [min] on my machine. Perhaps it could be improved by using the multiprocessing library.
