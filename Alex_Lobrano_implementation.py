import math
import random

randnum = random.SystemRandom()
############## Problem 1 a ##############

# Generate prime number of size n bits
def generate_prime(n, t):
	# sample uniform number of n bits
	# use isPrimeMR() to test that the generated number is prime
	
	p = random.getrandbits(n-1)			# generate N-1 random bits
	p = format(p, 'b')					# convert to binary string
	for i in range(n - len(p) - 1):
		p = "0" + p						# add missing zeroes
	p = "1" + p							# add 1 to front to ensure N bits
	p = int(p, 2)						# convert back to int
	return p

#get number p, test if it's prime using Miller-Rabin
def isPrimeMR(p, t):
	
	if(p % 2 == 0): return False
	if(isPerfectPower(p)): return False
	u = p - 1
	u = u/2
	r = 1
	while(u % 2 == 0):
		u = u/2
		r += 1
	#print "U:", u, "R:", r
	for j in range(1, t):
		a = randnum.randint(2, p-1)
		#print "A value:", a
		if(foundWitness(a,u,r,p)):
			return False
	return True

#get number p, test if it's a perfect power
def isPerfectPower(p):
	for e in range(2, len(format(p, 'b'))):
		a = 1
		b = p
		while(a <= b):
			m = (a+b)/2
			if(pow(m,e) == p): return True
			if(pow(m,e) > p):
				b = m - 1
			if(pow(m,e) < p):
				a = m + 1
	return False
	
def foundWitness(a, u, r, p):
	if((pow(a,u,p) != 1) and (pow(a,u,p) != p-1)):
		# if(r == 1):
			# #print "Witness:", a
			# return True
		for i in range(1, r):
			#print "Testing value i", i, "and exponent", 2**i*u
			if(pow(a,2**i*u,p) == p-1):
				return False
		#print "Witness:", a
		return True
	return False

# primality test using the naive approach
def isPrimeNaive(p):
	for i in range(2, int(math.sqrt(p))+2):
		if p % i == 0:
			return False
	return True

############## Problem 1 b ##############
class RSA:
	# initialize RSA, generate e, d
	def __init__(self):
		pass

	# Use generate_prime	
	def gen(self):
		# security parameter
		self.n = 1024
		
		# Primes p and q
		self.p = 0
		self.q = 0
		
		# RSA modulus N = pq
		self.rsamodulus = 0
		
		# Public key e
		self.e = 0
		
		# Secret key d
		self.d = 0
	
	def trapdoor(self, x):
		return y
	
	def inverse(self, y):
		return x

############## Problem 1 c ##############
class ISO_RSA:
	# initialize RSA, generate e, d, ISO RSA implementation
	def __init__(self):
		pass

	def gen(self):
		# security parameter for sauthenticated encryption 
		self.k =128
	
		# security parameter for trapdoor
		self.n = 1024
		
		# Primes p and q
		self.p = 0
		self.q = 0
		
		# RSA modulus N = pq
		self.rsamodulus = 0
		
		# Public key e
		self.e = 0
		
		# Secret key d
		self.d = 0
	
	def enc(self, m):
		return (y,c)
	
	def dec(self, y, c):
		return m

############## Problem 2 ##############
class MerkleTree:
	def __init__(self):
		pass

	# Number of files
		self.n = 0
	
	def create_tree(self, file_list):
		self.root = 0

	def read_file(self, i):
		pass
		
		# return file from Merkle Tree
		# Print siblings_list
		return (file, siblings_list)
		
	def write_file(self, i, file):
		pass
		# Update the root
		#self.root = NEW_ROOT
		
	def check_integrity(i,file,siblings_list):
		# Check that self.root matches root computed from the returned path
		# valid = True if integrity is verified
		
		return valid
		
def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
	#print "S:", s, "D:", d
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
		#print "Testing A:", a, "D:", d, "N:", n
		if pow(a, d, n) == 1:
			return False
		for i in range(s):
			#print "Testing A:", a, "Exp:", 2**i * d, "N:", n
			if pow(a, 2**i * d, n) == n-1:
				return False
		return True # n is definitely composite
 
    for i in range(10):
		a = random.randrange(2, n)
		if try_composite(a):
			return False
 
    return True # no base tested showed n as composite