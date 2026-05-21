"""
Factorial of a Number Using a For Loop:

   Write a program to calculate the factorial of a number entered by the user using a for loop. For example:

   - Input:Enter a number: 4
   - Output:Factorial of 4 is 24.


"""

num=int(input("enter the number "))
fact=1
for i in range(1,num+1):
    fact*=i
print(f"{num} factorial is {fact}")
    
