def isPrime(n):
	if n < 2:
		return False
	for i in xrange(2, int(n**0.5 )+ 1):
		if n % i == 0:
			return False
	return  True

def sieveOfEratosthenes(n):
	primes = []
	multiples = set()
	for i in xrange(2, n + 1):
		if i not in multiples:
			primes.append(i)
			for j in range(i * i, n + 1, i):
				multiples.add(j)
	return primes

print isPrime(949961)