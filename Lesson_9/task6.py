"""Try to execute a function that returns a some number, raise an exception when 0 or 100 is returned."""
from random import randint


def foo():
    number = randint(0, 1)
    try:
        if number == 0 or number == 100:
            raise ValueError('SOME', number)
    except ValueError:
        print('Wrong number returned')
        raise ValueError
    return number


print(foo())
