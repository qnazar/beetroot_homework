# eval() - виконує всі функції парсера і процесора =( А я так довго їх писав

print('Привіт! Я твій калькулятор!', 'Щоб закінчити роботу, введи "0".', sep='\n')
while True:
    expr = input('Введи вираз: ')
    if expr == '0':  # умова  виходу з циклу
        break
    try:  # перевірка некоректно введених даних
        output = eval(expr)
    except (ValueError, SyntaxError):
        print("Некоректний ввід")
    except ZeroDivisionError:
        print('Ділення на 0 неможливе.')
    else:
        print(output)
