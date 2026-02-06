'''
Write a program that verifies if a number entered by the user is a multiple of 7. For example:

Input: Enter a number: 14
Output: 14 is a multiple of 7.
'''

num = int(input("Enter the number "))
if num%7==0:
    print(f"{num} is multiple of 7.")