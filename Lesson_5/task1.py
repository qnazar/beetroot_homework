"""The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers"""
from random import randint

lst = []
while len(lst) < 10:
    lst.append(randint(-100, 100))
print(lst)
print(f'The largest number is {max(lst)}.')
