"""

Program to Perform Swapping of Two Numbers:

Write a program to swap two numbers entered by the user. For example:

Input:Enter first number: 10, Enter second number: 20
Output:
    

    Before swapping: a = 10, b = 20
    After swapping: a = 20, b = 10
"""

a=int(input("Enter the first number ")) #best to take input than fixed values
b=int(input("Enter the second value "))
print(f"before swapping \n{a} {b}")

a,b=b,a
print(f"after swapping \n{a} {b}")

