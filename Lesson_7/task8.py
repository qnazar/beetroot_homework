"""Using **kwargs to pass the variable keyword arguments to the function.
You should pass name, last name, age, phone. Find length of surname and return to the user."""


def user(**kwargs):
    try:
        kwargs['surname']
        return len(kwargs['surname'])
    except KeyError:
        return None


print(user(name='Nazar', last_name='Klypych', age=26, phone='0636760132'))

