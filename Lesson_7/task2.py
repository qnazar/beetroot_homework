"""Create a function that takes on an input random ints (between 1 and 10) and returns the list, without
duplicates. Try to create two versions of this function - first with usage set and list constructors
and second only using for-in loops.
def task2(1,2,34,2,3,2,4) -> 1, 2, 34, 3, 4"""


def task2(*args):
    return list(set(args))


print(task2(1, 2, 34, 2, 3, 2, 4))


def task2(*args):
    result = []
    for i in args:
        if i not in result:
            result.append(i)
    return result


print(task2(1, 2, 34, 2, 3, 2, 4))
