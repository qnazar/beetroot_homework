"""Write a function that accepts string and try to parse it into integer - use try except to handle exceptions."""


def parser(string):
    try:
        return int(string)
    except (ValueError, TypeError):
        print('You can\'t make an integer from this')


print(parser('a'))