from random import randint

counter = 1
while counter <= 5:
    num = randint(10, 1000)
    if num % 7 == 0:
        print(num)
        counter += 1
