'''
Write a program to check whether a character entered by the user is a vowel (a, e, i, o, u) or a consonant. For example:

Input: Enter a character: e
Output: e is a vowel.
'''

char=input("Enter the character: ")

if char in "aeiouAEIOU":
    print(f"{char} is a vowel")
else:
    print(f"{char} is not  an vowel.")