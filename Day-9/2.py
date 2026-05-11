"""
Pattern 2
A
A B
A B C
A B C D
A B C D E
"""
a=65
for i in range(a,a+5):
    for j in range(a,i+1):
        print(chr(j),end=" ")
    print()