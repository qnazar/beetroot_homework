"""Given a list of integers with duplicate elements in it. Create a function to generate another list,
which contains only the duplicate elements and returns back to user (also try to use *args)"""


def foo(*args):
    result = []
    for i in args:
        if args.count(i) > 1 and i not in result:
            result.append(i)
    return result


print(foo(1, 1, 2, 3, 3, 5, 2, 8, 4, 9, 5))
