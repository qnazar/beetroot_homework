def foo(*args):
    print("I'm imported function")
    return [i ** 2 for i in args]
