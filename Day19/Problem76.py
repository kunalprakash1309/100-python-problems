# Question
# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".


import sys
import zlib

a = "hello world!hello world!hello world!hello world!".encode()
print("Size of data orginal: ", sys.getsizeof(a))

b = zlib.compress(a)

print("Size of data compress: ", sys.getsizeof(b))
print(zlib.decompress(b).decode())


