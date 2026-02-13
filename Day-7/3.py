'''
Pattern 3: Inverted traingle
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

n=int(input("Ennter the rows"))
for i in range(n,0,-2):
    for j in range(n-i):
        print(" ",end='')
    for u in range(0,i):
        print("* ",end="")
    print()
    