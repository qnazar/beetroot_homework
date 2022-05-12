""" The Guessing Game.
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement."""
from random import randint

nickname = input('Enter your nickname: ')
print(f'Hello, {nickname}! Let\'s play The Guessing Game!')

attempts = 3
total_score = 0
level = 0
while True:
    level += 1
    number = randint(1, 10)
    print(f'LEVEL {level}'.center(50))
    while True:
        if attempts == 0:
            level = 0
            print('Sorry, you lost! The answer was {}. Your final score is {}!'.format(number, total_score))
            break
        while True:
            try:
                answer = int(input(f'Your guess: '))
                if 0 < answer < 11:
                    break
                else:
                    print('It can be only from 1 to 10.')
            except ValueError:
                print('Only numbers, please!')
        if answer == number:
            print('That\'s how it does, buddy!!!')
            break
        elif answer < number:
            attempts -= 1
            print(f'More than {answer}.')
            print(f'Attempts left - {attempts}')
        elif answer > number:
            attempts -= 1
            print(f'Less than {answer}.')
            print(f'Attempts left - {attempts}')
    if level == 0:
        break
    else:
        total_score += attempts * 10
        print(f'You have earned {attempts * 10} points.', end=' ')
        print(f'Total score *** {total_score} ***')
        attempts = 3
        continue
