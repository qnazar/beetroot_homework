# перевірити чи число просте
number = 8
i = 2

simple = True

while i < number:
    if number % i == 0:
        simple = False
        break
    i += 1

if simple:
    print('It is SIMPLE')
else:
    print('It is NOT SIMPLE')
