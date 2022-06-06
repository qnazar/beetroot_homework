"""Write a decorator 'arg_rules' that validates arguments passed to the function
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise return the result"""


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            output = func(*args, **kwargs)
            if not isinstance(*args, type_):
                print(f'Only string can be passed', end='. ')
                return False
            if len(*args, **kwargs) > max_length:
                print("The name is too long", end='. ')
                return False
            for i in contains:
                if i not in output:
                    print(f'There are missing some of required symbols - {contains}', end='. ')
                    return False
            return output
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
print(create_slogan('Nazar'))
print(create_slogan(5))
print()


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
