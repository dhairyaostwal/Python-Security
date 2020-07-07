# Caesar Cipher or ROT13 tutorials
"""
https://www.youtube.com/watch?v=mhWK14yQkPE&list=PLFCG67nCTUMHHJ-LDUnOsLxA2l_Eu5RMY&index=1
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

string_input = input("Enter string: ")
string_input = string_input.upper()
string_len = len(string_input)
print("Input: ", string_input)

key = int(input("Enter key: "))

string_output = ""

for i in range(string_len):
    character = string_input[i]
    location = alpha.find(character)
    new_location = ((location)%26 + (key)%26)%26        
    string_output += alpha[new_location]    
print("Encrypted Output: ", string_output)

