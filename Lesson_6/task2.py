# Find the the same numbers in two lists (without using a tuple or set)
list1 = [1, 5, 7, 11, 25, 18, 2, 36]
list2 = [1, 2, 9, 18, 58, -9, 11]

result = [i for i in list1 if i in list2]
print(result)
