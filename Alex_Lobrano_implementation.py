# Alex_Lobrano_implementation.py

import math
import random
import fractions
import hashlib
import string
import time
import sys

randnum = random.SystemRandom()

# Generate prime number of size n bits
def generate_prime(n, filename):
	
	for i in xrange(3*pow(n,2)):						# Try for 3*n^2 iterations to find a prime number
		p = randnum.getrandbits(n-1)					# Generate n-1 random bits
		p = format(p, 'b')								# Convert to binary string
		for i in range(n - len(p) - 1):
			p = "0" + p									# Add missing zeroes
		p = "1" + p										# Add 1 to front to ensure n bits
		p = int(p, 2)									# Convert back to int
		if(isPrimeMR(p, filename)): 					# Check using Miller-Rabin if p is prime
			print p, "is prime\n"
			return p

# Get number p, test if it's prime using Miller-Rabin
def isPrimeMR(p, filename):
	
	print "Testing", p, "for primality"
	if(p % 2 == 0): 									# Check if p is even
		print p, "is even"
		return False
	#if(isPerfectPower(p)): return False				# Check if p is a perfect power
	u = p - 1											# Set u = p - 1 to begin finding u*2^r
	u = u / 2											# u is now even, so divide it by 2
	r = 1												# r is now equal to 1
	while(u % 2 == 0):									# Continue dividing u by 2 and incrementing r until u is odd
		u = u / 2
		r += 1
	for j in range(10):									# Look for 10 strong witnesses
		a = randnum.randint(2, p-1)						# Choose a random number between 2 and p-1
		if(foundWitness(a,u,r,p)):						# Check if a is a strong witness for p being composite
			print "Strong witness", a, "found for", p
			return False
	return True

# Get number p, test if it's a perfect power
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
	
# Get number p, test if it is composite by seeing if a is a strong witness with values u and r
def foundWitness(a, u, r, p):
	if((pow(a,u,p) != 1) and (pow(a,u,p) != p-1)):		# Test if a^u mod p is not equal to 1 or -1
		for i in range(1, r):							
			if(pow(a,2**i*u,p) == p-1):					# Test for all {1...r} if a^(u*2^i) is equal to -1
				return False							# If an a^(u*2^i) is equal to -1, then a is not a strong witness
		return True										# If all a^(u*2^i) were checked and none equaled -1, a is a strong witness 
	return False										# If a^u mod p is equal to 1 or -1, then a is not a strong witness

# Primality test using the naive approach
def isPrimeNaive(p, filename):
	print "Testing", p, "using naive approach"
	for i in range(2, int(math.sqrt(p))+2):				# Check if p is prime by checking divisibility by any number between 2 and sqrt(p)+2
		if p % i == 0:	
			print p, "is divisble by", i
			return False
	print p, "is prime"
	return True

# Returns x such that a*x + b*y = g
def modinv(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return y0
	#return b, y0, x0 #(g,x,y)
	
# Generates a string of size characters
def generate_string(size):
	temp = ''
	for i in range(size):
		temp += random.choice(string.ascii_letters + string.digits)
	return temp
	
class RSA:
	# Initialize RSA, generate e, d
	def __init__(self):
		pass

	# Use generate_prime	
	def gen(self, filename):
		
		# security parameter
		self.n = 1024
		
		# Primes p and q
		self.p = generate_prime(self.n, filename)		# Generate prime p
		self.q = generate_prime(self.n, filename)		# Generate prime q
		
		# RSA modulus N = pq
		self.rsamodulus = self.p * self.q				# Calculate RSA modulus N = p*q
		
		# Phi(N)
		self.phi = (self.p - 1)*(self.q - 1)			# Calculate phi(N) = (p-1)(q-1)
		
		# Public key e
		self.e = randnum.randint(1, self.phi - 1)		# Generate integer e between 1 and phi(N)-1
		while(fractions.gcd(self.e, self.phi) != 1):	# Check if e is relatively prime to phi(N)
			self.e = randnum.randint(1, self.phi - 1)	# If not relatively prime, generate new e and try again
		
		# Secret key d
		self.d = modinv(self.e, self.phi) + self.phi	# Calculate d as modular inverse of e	
	
	def trapdoor(self, x):
		y = pow(x, self.e, self.rsamodulus)				# Calculate y = x^e mod N
		return y
	
	def inverse(self, y):
		x = pow(y, self.d, self.rsamodulus)				# Calculate x = y^d mod N
		return x

class MerkleTree:
	def __init__(self, files):
		pass

	# Number of files
		self.n = 0
	
	def create_tree(self, file_list, filename):
		self.n = len(file_list)													# Save the number of files
		self.file_list = file_list												# Save the files themselves
		self.height = int(math.log(len(file_list))/math.log(2))					# Height is the number of levels in tree
		treesize = int(pow(2,self.height+1)-1)									# Treesize is the number of nodes in tree, including leaves and root
		print "Creating tree with", treesize, "nodes"
		self.tree = [None] * treesize											# Create the tree with treesize number of nodes
		
		leaf_start = int(pow(2,self.height)-1)									# Calculate which node is the first leaf
		for i in range(leaf_start, leaf_start+len(file_list)):					# Iterate through nodes which are leaves
			hash = hashlib.sha256(self.file_list[i-leaf_start])					# Generate hash for corresponding file
			self.tree[i] = hash.hexdigest()										# Save hash to proper leaf
			print "Node", i, "in tree:", self.tree[i], "( hash of file", i - leaf_start, ")"
		
		for level in range(self.height, 0, -1):									# Iterate through the levels in the tree
			for level_offset in range(pow(2,level)-1, pow(2,level+1)-1, 2):		# Iterate through the nodes in each level by 2 (using odd nodes)
				temp1 = pow(2, level) - 1
				temp2 = pow(2, level+1) - 1
				parent_index = temp1 + (level_offset - temp2)/2					# Calculate the parent index of two corresponding nodes
				data = self.tree[level_offset] + self.tree[level_offset+1]		# Concatenate the two child nodes
				hash = hashlib.sha256(data)										# Calculate the hash of the concatenated children
				self.tree[parent_index] = hash.hexdigest()						# Save hash to proper node
				print "Node", parent_index, "in tree:", self.tree[parent_index], "( hash of nodes", level_offset, "and", level_offset+1, ")"
		
		hash = hashlib.sha256(self.tree[1] + self.tree[2])						# Calculate hash of two children of root
		self.tree[0] = hash.hexdigest()											# Save hash to node 0
		self.root = self.tree[0]												# Set root to node 0
		return self.root														# Return root

	def read_file(self, i, filename):
		pass
		
		file = self.file_list[i]												# Find file i
		
		print "Reading file", i, "from tree:", file
		leaf_start = int(pow(2,self.height)-1)									# Calculate which node is the first leaf
		leaf_offset = leaf_start + i											# Calculate node containing hash of file i
		
		if(leaf_offset % 2 == 0): 												# Figure out if sibling node is left or right of current node
			sibling_index = leaf_offset - 1
		else:
			sibling_index = leaf_offset + 1
		print "Adding node", sibling_index, "to sibling list"
		siblings_list = [ [sibling_index,self.tree[sibling_index]] ]			# Add sibling index and node to siblings list
		
		for level in range(self.height, 1, -1):									# Iterate through the levels in the tree
			temp1 = pow(2, level) - 1
			temp2 = pow(2, level+1) - 1
			parent_index = temp1 + (leaf_offset - temp2)/2						# Calculate the parent index of the earlier node
			if(parent_index % 2 == 0):											# Figure out if uncle node is left or right of parent node
				uncle_index = parent_index - 1
			else:
				uncle_index = parent_index + 1
			print "Adding node", uncle_index, "to sibling list"					
			siblings_list.append([uncle_index,self.tree[uncle_index]])			# Add uncle index and node to siblings list
			leaf_offset = parent_index											# Set leaf_offset to parent_index for next loop
		
		return (file, siblings_list)											# Return file and siblings list
		
	def write_file(self, i, file, filename):
		pass
		
		self.file_list[i] = file												# Save file to file list
		
		print "Writing file", i, "to tree:", self.file_list[i]
		
		hash = hashlib.sha256(self.file_list[i])								# Calculate hash of new file
		leaf_start = int(pow(2,self.height)-1)									# Calculate which node is the first leaf
		leaf_offset = leaf_start+i												# Calculate node containing hash of file i
		self.tree[leaf_offset] = hash.hexdigest()								# Save hash of new file to this node
		print "Updating node", leaf_offset, "to", self.tree[leaf_offset], "( hash of file", i, ")"
		
		for level in range(self.height, 1, -1):									# Iterate through the levels in the tree
			if(leaf_offset % 2 == 0): 											# Figure out if sibling node is left or right of current node
				sibling_index = leaf_offset - 1
				hash = hashlib.sha256(self.tree[sibling_index] + self.tree[leaf_offset])	# Calculate new hash of parent
			else:
				sibling_index = leaf_offset + 1
				hash = hashlib.sha256(self.tree[leaf_offset] + self.tree[sibling_index])	# Calculate new hash of parent
			temp1 = pow(2, level) - 1
			temp2 = pow(2, level+1) - 1
			parent_index = temp1 + (leaf_offset - temp2)/2						# Calculate the parent index of the earlier node
			self.tree[parent_index] = hash.hexdigest()							# Save the new hash to the parent index node
			if(leaf_offset % 2 == 0):
				print "Updating node", parent_index, "to", self.tree[parent_index], "( hash of nodes", sibling_index, "and", leaf_offset, ")"
			else:
				print "Updating node", parent_index, "to", self.tree[parent_index], "( hash of nodes", leaf_offset, "and", sibling_index, ")"
			leaf_offset = parent_index											# Set leaf_offset to parent_index for next loop
		
		hash = hashlib.sha256(self.tree[1] + self.tree[2])						# Calculate hash of two children of root
		self.tree[0] = hash.hexdigest()											# Save hash to node 0
		print "Updating node 0 to", self.tree[0]
		self.root = self.tree[0]												# Set root to node 0
		return self.root														# Return root
		
	def check_integrity(self, i, file, siblings_list, root, filename):
		
		hash = hashlib.sha256(file)												# Calculate hash of file
		for i in range(0, len(siblings_list)):									# Iterate through the siblings list
			if(siblings_list[i][0] % 2 == 0):									# Check if sibling should be left or right term
				hash = hashlib.sha256(hash.hexdigest() + siblings_list[i][1])	# Perform hash operation with current hash and next sibling
			else:																
				hash = hashlib.sha256(siblings_list[i][1] + hash.hexdigest())	# Perform hash operation with current hash and next sibling
		
		if(hash.hexdigest() == root): 											# Check if calculated hash is equal to the root given as input
			print "Calculated root", hash.hexdigest(), "equals", root
			return True
		else: 
			print "Calculated root", hash.hexdigest(), "does not equal", root
			return False