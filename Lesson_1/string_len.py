print('Введіть exit() щоб вийти з програми')
while True:
    string = input('Введіть ваш рядок: ')
    if string == 'exit()':
        print('Спасибі, що користувалися нашим сервісом, до побачення!')
        break
    numbs = 0
    letters = 0
    for char in string:
        if char.isdigit():
            numbs += 1
        if char.isalpha():
            letters += 1


    print('Кількість цифр -', numbs)
    print('Кількість літер -', letters)



