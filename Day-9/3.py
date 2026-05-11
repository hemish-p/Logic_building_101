"""
Pattern 3
A B C D E
A B C D
A B C
A B
A
"""

a=70
for i in range(5):
    for j in range(65,a-i):
        print(chr(j),end=" ")
    print()
