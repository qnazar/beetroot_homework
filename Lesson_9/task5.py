"""Create a function where you can generate fandom number and if it’s odd - raise an exception,
use finally block to print a number."""
from random import randint
number = randint(1, 100)


def foo(number):
    try:
        if number % 2 == 1:
            raise Exception('ODD')
    finally:
        print(number)


print(foo(number))
