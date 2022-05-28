"""Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except statement to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?"""


def oops():
    raise IndexError


def test():
    try:
        oops()
    except IndexError:
        print('IndexError is caught')


test()

# if I'll change IndexError to KeyError than the error will not be caught
