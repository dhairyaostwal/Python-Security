# Salting done for more security, not possible to crack via brute-force 

import hashlib, binascii

# hashlib.pbkdf2_hmac('Hashing Algo', 'Input Message', 'Salted Message', 'no. of iterations')

hash = hashlib.pbkdf2_hmac('sha512', b'SuperSecretPassword', b'saltthepassword', 1000000)

# Output in hexadecimal format
print(binascii.hexlify(hash)) 

# Output in byte format
print(hash)