"""Write a Python program to detect the number of local variables declared in a function."""


def get_number_of_local_variables(func):
    return func.__code__.co_nlocals


def foo(number, increment):
    return number + increment


def spam():
    for i in range(10):
        pass
    x = 5
    y = 10
    total = x + y
    return total


print(get_number_of_local_variables(foo))
print(get_number_of_local_variables(spam))  # --> 4 \ 'i' from the loop count too

# or without wrapper
print(foo.__code__.co_nlocals)
print(spam.__code__.co_nlocals)
