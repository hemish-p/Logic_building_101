"""
Print Fibonacci Series:

   Write a program to print the Fibonacci series up to a number N entered by the user. For example:

   - Input:Enter the number of terms: 7
   - Output:Fibonacci series: 0 1 1 2 3 5 8    
"""


def fibonacii(n):
    
    a=0
    b=1
    print(a,"",b,end=" ")
    
    while(n-2>0):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
        n-=1
fibonacii(7)
        