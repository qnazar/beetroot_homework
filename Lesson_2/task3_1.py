# розбиваємо рядок на складники, щоб виділити числа та операнд
def parser(expr):
    if expr[0] == '-':  # визначаю, чи перше число від’ємне
        a = '-'
        expr = expr[1:]
    else:
        a = ''

    for i in expr:  # виокремлюю перше значення
        if not i.isdigit():  # коли цикл доходить до операнда, то він зупиняється і робить слайс залишку
            expr = expr[expr.index(i):]
            break
        a += i

    if expr[1].isdigit() or expr[1] == '-':  # операнди можуть складатися з 1 або 2 знаків, тому потрібна перевірка
        op = expr[0]
        b = expr[1:]
    else:
        op = expr[0:2]
        b = expr[2:]

    return a, op, b


# функція здійснює основні розрахунки
def processor(a, op, b):
    if op == '+':
        return int(a) + int(b)
    if op == '-':
        return int(a) - int(b)
    if op == '*':
        return int(a) * int(b)
    if op == '/':
        return int(a) / int(b)
    if op == '**':
        return int(a) ** int(b)
    if op == '//':
        return int(a) // int(b)
    if op == '%':
        return int(a) % int(b)
    else:
        return 'Невідома операція'


# частина для взаємодії з користувачем
def interface():
    print('Привіт! Я твій калькулятор!', 'Щоб закінчити роботу, введи "0".', sep='\n')
    while True:
        expr = input('Введи вираз: ').replace(' ', '')  # вхідні дані можуть бути з пробілами і без
        if expr == '0':  # умова  виходу з циклу
            break
        a, op, b = parser(expr)
        try:  # перевірка некоректно введених даних
            output = processor(a, op, b)
        except ValueError:
            print("Некоректний ввід")
        except ZeroDivisionError:
            print('Ділення на 0 неможливе.')
        else:
            print(output)


interface()
