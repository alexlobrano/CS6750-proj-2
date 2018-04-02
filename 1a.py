# 1a.py

# Implement the Miller-Rabin primality testing algorithm presented in class. Given a number N output
# 1 if it is prime and 0 otherwise.
# To check your implementation, develop a method to test that a small odd number N is prime. Consider
# all odd numbers less than p
# (N) and test if they are divisors of N.
# Test your Miller-Rabin implementation for 10 small numbers (size n = 20 bits).

from Alex_Lobrano_implementation import *

#test for 10 small numbers, size n = 20 bits.

filename = time.strftime("%Y%m%d-%H%M%S")
sys.stdout = open(filename + '.txt', 'w')

n = 20

for i in range(10):
	p = generate_prime(n, filename)
	assert isPrimeNaive(p, filename) == True