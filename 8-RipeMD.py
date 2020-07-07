import hashlib

hash = hashlib.new('ripemd160')
hash.update(b'Hey World')

print(hash.hexdigest())