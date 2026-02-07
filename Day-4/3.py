'''
Write a program where the user enters a number, and the program prints it in reverse order. For example:

Input: 1234
Output: 4321
'''


n=int(input("Enter the number "))
num=n

while(num>0):                         
    l_digit=num%10
    print(l_digit,end="")
    num=num//10