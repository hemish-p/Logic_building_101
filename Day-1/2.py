'''
Write a program that displays the size of fundamental data types (int, float, double, and char) on your system.
For example:

Output:
Size of int: 4 bytes
Size of float: 4 bytes
Size of double: 8 bytes
Size of char: 1 byte
'''

import ctypes as ct

print("size of int:",ct.sizeof(ct.c_int),"bytes")
print("size of float:",ct.sizeof(ct.c_float),"bytes")
print("size of double:",ct.sizeof(ct.c_double),"bytes")
print("size of char:",ct.sizeof(ct.c_char),"byte")