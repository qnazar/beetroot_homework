"""Extracting numbers.
Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration"""

start_list = [i for i in range(1, 101)]
i = 0
final_list = []
while i < len(start_list):
    if start_list[i] % 7 == 0 and start_list[i] % 5 != 0:
        final_list.append(start_list[i])
    i += 1
print(final_list)
