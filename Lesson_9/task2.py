"""Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero)."""


def foo():
    a = input('a = ')
    b = input('b = ')
    try:
        return float(a) ** 2 / float(b)
    except ValueError:
        print('Input must be numbers')
    except ZeroDivisionError:
        print('Division by 0 is impossible')


print(foo())
