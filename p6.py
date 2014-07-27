"""
Project Euler - Problem 6
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
from numpy import power # because for some reason pylab calls numpy.random.power by default

def p6():
	'''
	The sum of the squares of the first ten natural numbers is 385
	
	The square of the sum of the first ten natural numbers is 3025
	
	Hence the difference between the sum of the squares of the first ten 
	natural numbers and the square of the sum is 3025 - 385 = 2640.
	
	Find the difference between the sum of the squares of the first one hundred 
	natural numbers and the square of the sum.
	'''
	my_range = arange(1,101,1)
	
	return power(sum(my_range), 2) - sum(power(my_range, 2))
	
print(p6())
	
	
