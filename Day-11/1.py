"""
Write a Program to Find the Largest Number Among Three Numbers:

   Write a program where the user enters three numbers, and the program finds and displays the largest number among them. For example:

   - Input:Enter three numbers: 12, 25, 7
   - Output:The largest number is: 25`
       
"""

a,b,c=map(int,input("Enter the number ").split(","))

print(a if a>b and a>c else b if b>c else c)
