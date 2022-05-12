""" The math quiz program
Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong,
and then responds with a message accordingly."""
from random import choice

expressions = ['2 + 2 * 2', '0!', 'pi', '2x + 10 = 0  |  x', '12 ** 2']
answers = {
    '2 + 2 * 2': 6,
    '0!': 1,
    'pi': 3.14,
    '2x + 10 = 0  |  x': -5,
    '12 ** 2': 144
}


current_task = choice(expressions)
while True:
    try:
        answer = float(input(f'{current_task} = '))
    except ValueError:
        print('Invalid input')
        continue
    if answer == answers[current_task]:
        print('Good job!')
        break
    else:
        print('That is incorrect. Try again')
