# Shake Algorithm
import hashlib
hash = hashlib.shake_256(b'Hello World')
print(hash.digest(20))
print(hash.digest(40))
# important to specify size inside digest()