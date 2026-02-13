"""
 Pattern 2: traingle
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
n=int(input("Enter the no of rows "))
for  i in range(0,n,2):
    for j in range(n-i-1):
        print(" ",end="")
    for u in range(0,i+1):
        print("* ",end="")
    print()