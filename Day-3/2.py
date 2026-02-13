'''
Write a program to calculate the area of a circle given its radius and a triangle given its base and height. For example:

Input: Radius: 5, Base: 10, Height: 4
Output:
Area of Circle: 78.5
Area of Triangle: 20

'''

#area of circle= pi*r*r
#area of Triangle=1/2 * Base * Height

from math import pi

radius=5  # for flexibility u can use input
Base=10
Height=4

print(f"Area of Circle {pi*radius*radius}\nArea of Triangle {1/2*Base * Height}")
