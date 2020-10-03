import hashlib

"""
Simple experiment on how hash a string in md5, using Hashlib, encode() and
hexdigest() function.

"""

message = input("Hash this:")
#encode the string in byte format and hashes it in md5
hashed = hashlib.md5(message.encode())
print("Hashed message: ")
#print hashed message in hex format. use 'digest()' for byte format
print(hashed.hexdigest())