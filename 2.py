# 2.py

# Create a tree with n = 32 files and perform several read, check integrity and write operations as shown
# in the template.

from Alex_Lobrano_implementation import *

mt = MerkleTree()
file_list = [0] * 32
for i in range(32):
	file_list[i] = generate_string(32)
	
mt.create_tree(file_list)

# read 5 valid files
for i in range(5):
	pos = randnum.randint(0, len(file_list)-1)
	file, siblings_list =  mt.read_file(pos)
	valid = mt.check_integrity(pos,file,siblings_list) 
	assert (file == file_list[pos] and valid == True)

# read 5 invalid files
for i in range(5):
	pos = randnum.randint(0, len(file_list)-1)
	file, siblings_list =  mt.read_file(pos)
	file = generate_string(32)
	valid = mt.check_integrity(pos,file,siblings_list) 
	assert (valid == False)

# write 5 files
for i in range(5):
	pos = randnum.randint(0, len(file_list)-1)
	new_file = generate_string(32)
	mt.write_file(pos,new_file)

	file, siblings_list =  mt.read_file(pos)
	valid = mt.check_integrity(pos,file,siblings_list) 
	assert (file == new_file and valid == True)