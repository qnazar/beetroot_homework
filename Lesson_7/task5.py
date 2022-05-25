"""Create a function that concatenate two lists index-wise"""

l1 = [1, 2, 3, 4, 5, 45, 25, 65]
l2 = [5, 6, 7, 8, 9, 10, 15]


# short
def concatenate(first, second):
    return list(map(lambda a, b: a + b, first, second))


print(concatenate(l1, l2))


# this func can work with lists of diff len just appending last values to the result list
def concatenate(first, second):
    result = []
    if len(first) <= len(second):
        for i in range(len(first)):
            result.append(first[i] + second[i])
        len_delta = len(second) - len(first)
        for i in range(len_delta, 0, -1):
            result.append(second[-i])

    elif len(first) > len(second):
        for i in range(len(second)):
            result.append(first[i] + second[i])
        len_delta = len(first) - len(second)
        for i in range(len_delta, 0, -1):
            result.append(first[-i])
    return result


print(concatenate(l1, l2))

