""" Words combination
Create a program that reads an input string and then creates and prints 5 random strings from characters of the input.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)"""
from random import sample   # sample(seq, k) --> []   створює список унікальних елементів заданої довжини k

# Базове рішення без додаткових перевірок

# word = input('Enter the string: ')
# for i in range(5):
#     combo = ''.join(sample(word, len(word)))
#     print(combo)


# Додано перевірки можливості створення 5-ти унік комбінацій залежно від довжини слова та к-сті унікальних символів

word = input('Enter the string: ')

# перевірка можливості створення 5-ти унікальних комбінацій
if len(word) >= 3:
    check_word = []
    for char in word:                                                      # пошук унікальних симолів у слові
        check_word.append(char) if char not in check_word else None
    if len(check_word) >= 3 or len(check_word) == 2 and len(word) > 5:
        check_list = []                                                    # для перевірки унікальності нової комбінації
        while len(check_list) < 5:
            combo = ''.join(sample(word, len(word)))
            # print(combo)
            check_list.append(combo) if combo not in check_list and combo != word else None  # сама перевірка
            # print(check_list)
        print(', '.join(check_list))
    else:
        print('I can\'t make 5 new combinations from this word.')
else:
    print('I can\'t make 5 new combinations from this word.')
