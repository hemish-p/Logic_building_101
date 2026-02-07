'''
Write a program that acts as a calculator, taking two numbers and an operator (+, -, *, /) from the user, and performing the operation based on the operator. For example:

Input: Enter first number: 10, Operator: +, Second number: 20
Output: 10 + 20 = 30
'''

f_no=int(input("First number "))
l_no=int(input("last number "))

oper=input("Enter the operator (+,-,*,/) ")

match oper:
    case "+":
        print(f"{f_no} + {l_no} = {f_no + l_no}")
        
    case "-":
        print(f"{f_no} - {l_no} = {f_no - l_no}")
        
    case "*":
        print(f"{f_no} * {l_no} = {f_no * l_no}")
        
    case "/":
        print(f"{f_no} / {l_no} = {f_no / l_no}")
        
    case _ :
        print("Enter valid operation!")
        