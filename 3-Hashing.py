import hashlib
md5 = hashlib.md5()
md5.update(b'Python')

# bit encoded

print("md5.digest() = ",md5.digest())

# hexadecimal digest

print("md5.hexdigest() = ",md5.hexdigest())

sha = hashlib.sha1(b'Python')
print("sha.digest() = ", sha.digest())
print("sha.hexdigest() = ",sha.hexdigest())