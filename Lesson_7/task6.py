"""Write function that sums up all numbers that are passed to it (*args used)"""


def summing(*args):
    return sum(args)


print(summing(2, 5, 8, -9, 15))
