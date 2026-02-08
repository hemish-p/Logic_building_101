'''
Write a program that calculates the sum of the digits of a number entered by the user. For example:

Input: Enter a number: 1234
Output: Sum of digits: 10

'''

n=int(input("Enter the number "))
num=n
res=0
while(num>0):
    ld=num%10     #takes out last digit
    res+=ld
    num=num//10 # takes the number other than last digit 
    
print("Sum of digits: ",res)
