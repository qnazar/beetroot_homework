# nested functions
# def parent_func(name):
#     print(f'I am your Father, {name}')
#     def daughter_func():
#         print(f'My name is {name}')
#     daughter_func()
#
#
# parent_func('Emma')

# nonlocal
# def parent_func(name):
#     print(f'I am your Father, {name}')
#     def daughter_func():
#         nonlocal name
#         name = 'Scott'
#         print(f'No, my name is {name}')
#     daughter_func()
#     print(name)
#
# parent_func('Emma')

# closures vs nested
# обо’язкова наявність вкладеної функції
# повинна посилатися на змінну, оголошену в верхній функції
# зовнішня функція повинна повертати вкладену
#
def func1():
    msg = 5
    def func2():
        print(msg)
    return func2

test = func1()  # func2
test()
func1
test()


# __closure__
print(test.__closure__)
print(test.__closure__[0].cell_contents)
print(func1.__closure__)
# цей атрибут повертає кортеж певних cell-об’єктів, якщо об’єкт є замиканням, інакше None


# encapsulation of outer vars
def func1():
    msg = [1, 2, 3]
    print(id(msg))
    def func2():
        msg.append(4)
        print(id(msg))
        print(msg)
    return func2

test = func1()
test()
del func1
test()


#lambda in nested

add_to_five = lambda a=2, b=3: lambda c: a + b + c

o = add_to_five(20, 30)
print(o(10))
