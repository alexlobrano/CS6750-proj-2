from Alex_Lobrano_implementation import *

for i in range(1000):
	p = generate_prime(20, 10)
	#print p
	#print isPrimeMR(p, 10)
	#print is_probable_prime(p)
	assert isPrimeMR(p,10) == is_probable_prime(p)