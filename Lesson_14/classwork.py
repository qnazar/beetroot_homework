def check_by_zero(func):
    def wrapper(*args):
        if args[-1] == 0:
            print('You can not divide by zero')
            return False
        return func(*args)
    return wrapper


@check_by_zero
def divide(a, b):
    return a / b

print(divide(5, 0))


# -------------------------------------------- #
def outer(file_name):
    def middle(func):
        def inner(*args, **kwargs):
            if args[0].isdigit():
                with open(file_name, 'w') as file:
                    file.write(args[0])
            else:
                print('It is not digits')
            return func(*args, **kwargs)
        return inner
    return middle


@outer('test.txt')
def some_to_do(a: str):
    print(a)

# outer('test.txt')(some_to_do)('991199999258hs')

# ------------------------------------------------------- #
def lower_str(func):
    def wrapper(*args):
        res = func(*args).lower()
        print(res)
        return res
    return wrapper


def capital_str(func):
    def wrapper(*args):
        res = func(*args).capitalize()
        print(res)
        return res
    return wrapper


@capital_str
@lower_str
def some_str(s: str):
    return s


some_str('AAAAAN')
