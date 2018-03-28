# 1a.py

# Implement the Miller-Rabin primality testing algorithm presented in class. Given a number N output
# 1 if it is prime and 0 otherwise.
# To check your implementation, develop a method to test that a small odd number N is prime. Consider
# all odd numbers less than p
# (N) and test if they are divisors of N.
# Test your Miller-Rabin implementation for 10 small numbers (size n = 20 bits).

from Alex_Lobrano_implementation import *

#test for 10 small numbers, size n = 20 bits.
n = 1024

# test RSA, do it 10 times

# Generate random x in Z_N^*

rsa = RSA()
rsa.gen()
x = randnum.randint(1, rsa.rsamodulus - 1)			# generate integer e between 1 and phi(N)-1
while(fractions.gcd(x, rsa.rsamodulus) != 1):		# check if e is relatively prime to phi(N)
	x = randnum.randint(1, rsa.rsamodulus - 1)			# if not, generate new e and try again
	
# print "X:", x
# y = rsa.trapdoor(x)
# print "Y:", y
# recovered_x = rsa.inverse(y)
# print "X:", recovered_x

y = rsa.trapdoor(x)
assert rsa.inverse(y) == x

# p = generate_prime(n)
# q = generate_prime(n)

# rsa = p*q

# phi = (p-1)*(q-1)

# e = randnum.randint(1, phi-1)			# generate N-1 random bits
# while(fractions.gcd(e, phi) != 1):
	# e = randnum.randint(1, phi-1)			# generate N-1 random bits
	
# d = modinv(e, phi) + phi
	
# print "Phi:", phi
# print "E:", e
# print "D:", d
# print "D + phi:", d+phi
# print "GCD phi and e:", fractions.gcd(e,phi)
# print "GCD phi and d:", fractions.gcd(d,phi)
# print "e*d mod phi:", e*d % phi

