"""Write a Python program to access a function inside a function (Tips: use function, which returns another function)"""


def outer_func():
    print('Calling inner func')

    def inner_func():
        print('Inner func is here')

    return inner_func


func = outer_func()  # now func is the object of inner_func with __call__ method
func()
