# 1b.py

# Using the Miller-Rabin primality testing algorithm, generate two primes p and q of size n = 1024
# bits, and set N = pq. Implement the RSA trapdoor permutation:
# - Gen: choose e, d such that e*d = 1 mod phi(N) and output pk = e and sk = d;
# - Trapdoor(pk, x): given x in Z_N^*, output x^e mod N;
# - Inverse(sk, y): given y in Z_N^*, output y^d mod N.
# Generate 10 pairs(x, y) with y = Trapdoor(pk, x) and check correctness: Inverse(sk,Trapdoor(pk, x)) =
# x.

from Alex_Lobrano_implementation import *

# test RSA, do it 10 times

rsa = RSA()
rsa.gen()

for i in range(10):

	# Generate random x in Z_N^*
	x = randnum.randint(1, rsa.rsamodulus - 1)			# generate integer x between 1 and N-1
	while(fractions.gcd(x, rsa.rsamodulus) != 1):		# check if x is relatively prime to N
		x = randnum.randint(1, rsa.rsamodulus - 1)			# if not, generate new x and try again
	y = rsa.trapdoor(x)
	assert rsa.inverse(y) == x