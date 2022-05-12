"""Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers"""
from random import randint

first_list = []
while len(first_list) < 10:
    first_list.append(randint(1, 10))
print('First list -', first_list)

second_list = []
while len(second_list) < 10:
    second_list.append(randint(1, 10))
print('Second list -', second_list)

third_list = []
for i in first_list:
    if i in second_list and i not in third_list:
        third_list.append(i)
print('Result -', third_list)

# or using while
third_list = []
i = 0
while i < 10:
    if first_list[i] in second_list and first_list[i] not in third_list:
        third_list.append(first_list[i])
    i += 1
print('Result -', third_list)

