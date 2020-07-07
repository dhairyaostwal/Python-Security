# Different SHA methods
# SHA1, SHA224, SHA256, SHA384, SHA512

import hashlib
# for algorithms available on the computer
#print(hashlib.algorithms_available) 

# for algorithms available on hashlib library usage
#print(hashlib.algorithms_guaranteed)
sha1 = hashlib.sha1(b'Hello World')
print("SHA1 = ",sha1.hexdigest())

sha224 = hashlib.sha224(b'Hello World')
print("SHA224 = ",sha224.hexdigest())

sha256 = hashlib.sha256(b'Hello World')
print("SHA256 = ",sha256.hexdigest())

sha384 = hashlib.sha384(b'Hello World')
print("SHA384 = ",sha384.hexdigest())

sha512 = hashlib.sha512(b'Hello World')
print("SHA512 = ",sha512.hexdigest())

