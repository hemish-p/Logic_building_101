'''
Write a program to compare two integers entered by the user and print the larger one. For example:

Input: Enter two numbers: 15, 20
Output: The larger number is: 20
'''

a=int(input())
b=int(input())
print("largest number is ",a if a>b else b)