"""
Write a Program to Find the GCD or HCF of Two Numbers:

   Write a program where the user enters two numbers, and the program calculates their greatest common divisor (GCD) or highest common factor (HCF). For example:

   - Input:Enter two numbers: 60, 48
   - Output:The GCD of 60 and 48 is 12.


"""
from math import gcd 
num,num1=map(int,input("Enter the number ").split(","))
print(f"The GCD of {num} and {num1} is {gcd(num,num1)} ")