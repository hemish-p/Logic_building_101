"""
Write a Program to Check Whether a Year Entered by the User is a Leap Year:

   Write a program to determine whether a given year is a leap year. For example:

   - Input:Enter a year: 2024
   - Output:2024 is a leap year.
"""

yr=int(input("Enter the year "))
print("Leap_year" if (yr%4 ==0) or (yr%400==0) and yr%100!=0 else "no_leap_year")