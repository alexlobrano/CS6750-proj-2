# 2.py

# Create a tree with n = 32 files and perform several read, check integrity and write operations as shown
# in the template.

from Alex_Lobrano_implementation import *

mt = MerkleTree()
#file_list = list of n strings/files
file_list = [None] * 32
for i in range(32):
	file_list[i] = generate_string(32)
mt.create_tree(file_list)

# m1 = hashlib.sha256(file_list[4])
# print "Hash of file 4:", m1.hexdigest()
# print "Tree index 35:", mt.tree[35]
# m2 = hashlib.sha256(file_list[5])
# print "Hash of file 5:", m2.hexdigest()
# print "Tree index 36:", mt.tree[36]
# m3 = hashlib.sha256(m1.hexdigest()+m2.hexdigest())
# print "Hash of file 4 and 5:", m3.hexdigest()
# m4 = hashlib.sha256(mt.tree[35] + mt.tree[36])
# print "Hash of tree index 35 and 36:", m4.hexdigest()
# m5 = hashlib.sha256(file_list[6])
# print "Hash of file 6:", m5.hexdigest()
# print "Tree index 37:", mt.tree[37]
# m6 = hashlib.sha256(file_list[7])
# print "Hash of file 7:", m6.hexdigest()
# print "Tree index 38:", mt.tree[38]
# m7 = hashlib.sha256(m5.hexdigest()+m6.hexdigest())
# print "Hash of file 6 and 7:", m7.hexdigest()
# m8 = hashlib.sha256(mt.tree[37] + mt.tree[38])
# print "Hash of tree index 37 and 38:", m8.hexdigest()
# m9 = hashlib.sha256(m3.hexdigest()+m7.hexdigest())
# print "Hash of file 4,5,6,7:", m9.hexdigest()
# m10 = hashlib.sha256(m4.hexdigest() + m8.hexdigest())
# print "Hash of tree index 35,36,37,38:", m10.hexdigest()

file, siblings_list = mt.read_file(6)

hash = hashlib.sha256(file)
for i in range(0, len(siblings_list)):
	if(siblings_list[i][0] % 2 == 0):		# sibling is even
		hash = hashlib.sha256(hash.hexdigest()+siblings_list[i][1])
	else:
		hash = hashlib.sha256(siblings_list[i][1]+hash.hexdigest())
	print hash.hexdigest()

print "Tree root:", mt.root

assert mt.check_integrity(6,siblings_list) == True

#Generate new value of file
pos = 7
new_file = generate_string(32)
mt.write_file(pos,new_file)

# Read file and check integrity
file, siblings_list =  mt.read_file(pos)
valid = mt.check_integrity(pos,siblings_list) 
assert (file == new_file and valid == True)

# # read 5 valid files
# pos = 4
# file, siblings_list =  mt.read_file(pos)
# valid = mt.check_integrity(pos,file,siblings_list) 
# assert (file == file_list[pos] and valid == True)

# # read 5 invalid files
# pos = 10

# file, siblings_list =  mt.read_file(pos)
# #file = random string
# valid = mt.check_integrity(pos,file,siblings_list) 
# assert (valid == False)

# # write 5 files
# pos = 7

# #Generate new value of file
# # new_file = random string
# mt.write_file(pos,new_file)

# # Read file and check integrity
# file, siblings_list =  mt.read_file(pos)
# valid = mt.check_integrity(pos,file,siblings_list) 
# assert (file == new_file and valid == True)