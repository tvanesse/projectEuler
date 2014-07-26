from pylab import *

def p1 (n):
	'''
	Find all the multiples of 3 and 5 that lie strictly 
	below `n` and return their sum.
	'''
	candidates = arange(1,n,1)
	multiples = []
	for c in candidates:
		if (c % 3 == 0) or (c % 5 == 0) :
			multiples.append(c)
			
	return sum(multiples)
	
print(p1(1000))
