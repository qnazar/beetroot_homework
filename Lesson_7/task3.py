"""Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
- the call make_operation(‘+’, 7, 7, 2) should return 16
- the call make_operation(‘-’, 5, 5, -10, -20) should return 30
- the call make_operation(‘*’, 7, 6) should return 42  """
from functools import reduce


def make_operation(op, *args):
    if op == '+':
        return sum([i for i in args])
    if op == '-':
        return reduce(lambda a, b: a - b, [i for i in args])
    if op == '*':
        return reduce(lambda a, b: a * b, [i for i in args])


print(make_operation('+', 1, 2, 3, 4, 5))  # 15
print(make_operation('-', 100, 10, 10, -30))  # 110
print(make_operation('*', 5, 10, 15, 3))  # 2250
