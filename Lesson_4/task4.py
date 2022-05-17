# Write a Python program to calculate the discriminant value.
from math import pow

a = float(input('a = ').strip())
b = float(input('b = ').strip())
c = float(input('c = ').strip())

D = pow(b, 2) - 4 * a * c
print(f'The discriminant is {D}')
