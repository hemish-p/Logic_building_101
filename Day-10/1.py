"""
Pattern 1

A
B B
C C C
D D D D
E E E E E
"""

cnt=1    
for i in "ABCDE":
    for j in range(ord(i),ord(i)+cnt):
        print(i," ",end="")
    cnt+=1
    print()
    
