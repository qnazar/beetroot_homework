from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return int(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return str(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return bool(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return float(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper


@TypeDecorators.to_int
def add(a, b):
    return a + b


test_int_1 = add(10, 2.5)
print(test_int_1, type(test_int_1))

test_int_2 = add('a', 'b')
print(test_int_2, type(test_int_2))
