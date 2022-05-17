# Create a program that reads from the user input int radius and prints back the area of the circle
from math import pi, pow

radius = int(input('Enter the radius: '))
area = pi * pow(radius, 2)
print(area)
