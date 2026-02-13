"""
Pattern 1: Inverted Right-angled triangle
* * * * *
* * * *
* * *
* *
*

"""

n=int(input("Enter the no of rows "))
for i in range(n,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print()
