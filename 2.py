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
m1 = hashlib.sha256(file_list[0])
m2 = hashlib.sha256(file_list[1])
m3 = hashlib.sha256(m1.hexdigest()+m2.hexdigest())
m1 = hashlib.sha256(file_list[2])
m2 = hashlib.sha256(file_list[3])
m4 = hashlib.sha256(m1.hexdigest()+m2.hexdigest())
m = hashlib.sha256(m3.hexdigest()+m4.hexdigest())
print m.hexdigest()
m = hashlib.sha256(mt.tree[15]+mt.tree[16])
print m.hexdigest()
print mt.tree[7]


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