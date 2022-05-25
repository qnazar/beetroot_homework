"""Initiate any error with **kwargs function"""


def foo(**kwargs):
    return kwargs


# TypeError
foo(5)
