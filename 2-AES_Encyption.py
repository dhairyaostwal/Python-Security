# AES Encryption
"""
https://www.youtube.com/watch?v=artGrUA4SPY&list=PLFCG67nCTUMHHJ-LDUnOsLxA2l_Eu5RMY&index=6
"""

# Remark: Key & Message both must be 16, 24 or 32 bit long

from Crypto.Cipher import AES

key = '0123456789012345'
string_input = input()
cipher = AES.new(key)
cipher_text = cipher.encrypt(string_input)
print("Encrypted output: ", cipher_text)
print('\n')
plain_text = cipher.decrypt(cipher_text)
print("Decrypted text: ", plain_text)