import hashlib

hash = hashlib.md5(b'Hello Python')

# Returns HASH object 
print(hash)

# Returns block size 
print(hash.block_size)

# Returns digest size
print(hash.digest_size)

