from pylab import *

def sieve_of_Eratosthene(n):
	'''
	This function implements the well known sieve of Eratosthenes
	(http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). It returns
	all primer numbers up to some given limit `n`.
	'''
	candidates = range(2,n,1)
	curr_index = 0
	
	while(curr_index != len(candidates)-1):
		curr_int = candidates[curr_index]
	
		for i in candidates[curr_index+1:]:
			if i%curr_int == 0:
				candidates.remove(i)
			
		curr_index += 1
		curr_int = candidates[curr_index]
		
	return candidates
	
	
def my_way(n):
	'''
	The sieve is terrible when we increase `n`, mainly because the initial list
	becomes huge and takes all the available memory.
	Here is another implementation.
	'''
	primes = [2]
	test = primes[0] + 1
		
	while test<n:
		new_prime = True
		for p in primes:
			if test % p == 0:
				new_prime = False
				break
		if new_prime:
			primes.append(test)
		test += 1
		
	return primes
	
		
def p3_shitty(N):
	'''
	The prime factors of 13195 are 5, 7, 13 and 29.
	
	What is the largest prime factor of the number `N` ?
	'''
	# First compute the prime numbers below N
	candids = my_way(N)
	print("Prime numbers computed.")
	# Then browse through the prime numbers in decreasing order
	# and return the first guy that divides N.
	for i in arange(len(candids)-1, 0, -1):
		if N % candids[i] == 0:
			return candids[i]
			
#==========================================
#END OF SHITTYNESS
#==========================================		

#=========================
#BEGINNING OF AWESOMENESS	
#=========================

def prime_gen(n):
	'''
	The generators in Python : awesomeness level 976
	'''
	yield 2
	primes = [2]
	test = primes[0] + 1
		
	while test<n:
		new_prime = True
		for p in primes:
			if test % p == 0:
				new_prime = False
				break
		if new_prime:
			primes.append(test)
			yield test
		test += 1

def p3(N):
	'''
	The prime factors of 13195 are 5, 7, 13 and 29.
	
	What is the largest prime factor of the number `N` ?
	'''
#	A way to see the problem is that we can factorize N and try to
#	find the biggest prime number that divides N simply by using the 
#   euclidian division algorithm.
	primes = prime_gen(N)
	primes_memo = []
	Acc = {}
	
	def loop(N, Acc):
		print("Current N : " + str(N))
		s = sqrt(N)
		
		for p in primes_memo:
			if p > s:
				# Stop
				print(str(p) + "^2 is larger than " + str(N) + ", stopping (memo)")
				newAcc = Acc
				newAcc[N] = 1
				return newAcc
				
			attempt = N % p
			if attempt == 0:
				# Success !
				print(str(N) + " can be divided by " + str(p) + " (memo)")
				newAcc = Acc
				newAcc[p] += 1
				print("Remainder : " + str(N/p))
				return loop(N/p, newAcc)
			
		while True:
			next_p = primes.next()
			primes_memo.append(next_p)
			if next_p > s:
				print(str(next_p) + "^2 is larger than " + str(N) + ", stopping.")
				newAcc = Acc
				newAcc[N] = 1
				return newAcc
			
			attempt = N % next_p
			if attempt == 0:
				# Success !
				print(str(N) + " can be divided by " + str(next_p))
				newAcc = Acc
				newAcc[next_p] = 1
				print("Remainder : " + str(N/next_p))
				return loop(N/next_p, newAcc)
	
	return loop(N, Acc)
	
print(p3(600851475143))

