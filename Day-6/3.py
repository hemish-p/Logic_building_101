'''
Pattern 3: Hallow Rectangle
* * * * *
*       *
*       *
*       *
* * * * *

'''

for i in range(1,6):       #u can use input() func 
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print("* ",end="")
        else:
            print("  ",end="")
            
    print()