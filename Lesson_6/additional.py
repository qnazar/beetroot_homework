# 1. Remove an empty tuple(s) from a list of tuples
# lst = [(1, 2), (2, 3), (), (3, 4)]
# lst = [i for i in lst if len(i) > 0]
# print(lst)


# 2. Swap two tuples in Python
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
#
# t1, t2 = t2, t1
# print(t1, t2)


# 3. Check if all items in the tuple are the same
# t = (0, 0, 1)
# for i in t:
#     if i != t[0]:
#         print(False)
#         break
# else:
#     print(True)


# 4. Given list of tuples, remove all the tuples with length K
# list_of_tuples = [(1, 2, 3), (7, 8), (4, 5, 6, 9), (1, ), (4, 6)]
# list_of_tuples = [t for t in list_of_tuples if len(t) != 2]
# print(list_of_tuples)


# 5. Multiply all numbers in the list
# from functools import reduce
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# result = reduce(lambda a, b: a * b, lst)
# print(result)


# 6. Program to convert Set into Tuple and Tuple into Set
def tuple_into_set(tpl):
    if isinstance(tpl, tuple):
        return set(tpl)
    else:
        return 'Give me the tuple, please'


def set_into_tuple(st):
    if isinstance(st, set) or isinstance(st, frozenset):
        return tuple(st)
    else:
        return 'Give me the set, please'


print(tuple_into_set((1, 2, 3, 3)))
print(set_into_tuple({1, 2, 3, 8, 4}))


# 7. Concatenate two lists index-wise
l1 = [1, 5, 6, -8, 76, 58, 8, 10]
l2 = [2, 5, 8, 78, -9, 0, 45, 10]
result = [i for i in map(lambda a, b: a+b, l1, l2)]
print(result)

