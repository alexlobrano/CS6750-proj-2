# 2.py

# Create a tree with n = 32 files and perform several read, check integrity and write operations as shown
# in the template.

from Alex_Lobrano_implementation import *

filename = time.strftime("%Y%m%d-%H%M%S")
sys.stdout = open(filename + '.txt', 'w')

number_of_files = 32
file_list = [0] * number_of_files
for i in range(number_of_files):
	file_list[i] = generate_string(32)
	print "File", i, ":", file_list[i]
	
mt = MerkleTree(number_of_files)	
root = mt.create_tree(file_list, filename)

# read 5 valid files
for i in range(5):
	pos = randnum.randint(0, number_of_files - 1)
	file, siblings_list =  mt.read_file(pos, filename)
	valid = mt.check_integrity(pos, file, siblings_list, root, filename) 
	assert (file == file_list[pos] and valid == True)

# read 5 invalid files
for i in range(5):
	pos = randnum.randint(0, number_of_files - 1)
	file, siblings_list =  mt.read_file(pos, filename)
	file = generate_string(32)
	valid = mt.check_integrity(pos, file, siblings_list, root, filename) 
	assert (valid == False)

# write 5 files
for i in range(5):
	pos = randnum.randint(0, number_of_files - 1)
	new_file = generate_string(32)
	root = mt.write_file(pos, new_file, filename)

	file, siblings_list =  mt.read_file(pos, filename)
	valid = mt.check_integrity(pos, file, siblings_list, root, filename) 
	assert (file == new_file and valid == True)

