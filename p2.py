"""
Project Euler - Problem 2
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

from pylab import *

def fibo_memo(n) :
	'''
	Returns the nth number in the fibonacci sequence.
	'''
	# A clean way to create a static attribute within a function
	if not hasattr(fibo_memo, "memo"):
		fibo_memo.memo = {}

	if n in fibo_memo.memo :
		return fibo_memo.memo[n]
	else :
		if n==0:
			return 0
		elif n <= 2 :
			return 1
		else :
			f = fibo_memo(n-1) + fibo_memo(n-2)
			fibo_memo.memo[n] = f
			return f

def p2 (N):
	'''
	Each new term in the Fibonacci sequence is generated by adding the 
	previous two terms. By starting with 1 and 2, the first 10 terms 
	will be:
	
	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
	By considering the terms in the Fibonacci sequence whose values 
	do not exceed `N`, find the sum of the even-valued terms.
	'''
	# Recall that even numbers always end with a digit of 0, 2, 4, 6 or 8.
	#	I noticed that if you take a closer look at the Fibonacci sequence, you
	#	have some kind of pattern alternating between even and odd values. See for
	#	yourself :
	#	
	#	Fib  : 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ...
	#	index: 1  2  3  4  5  6   7   8   9  10  11   12   13   14
	#	even : n  n  y  n  n  y   n   n   y   n   n    y    n    n
	#	
	#	But I can't explain why. Anyway I think I can only compute the nth Fibonacci
	#	number once every 3 step, according to the pattern above.
	
	curr_index = 3
	acc = []
	
	while True:
		f = fibo_memo(curr_index)
		if f > N:
			break
		else:
			acc.append(f)
			curr_index += 3
			
	return sum(acc)
	
print(p2(4000000))
