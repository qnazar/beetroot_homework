# Calculate multiplication of two random float numbers
# Note:
# First random float number must be between 0.1 and 1
# Second random float number must be between 9.5 and 99.5
from random import random, uniform

a = random()
b = uniform(9.5, 99.5)
print('First number -', a)
print('Second number', b)
print('Result - ', a * b)

