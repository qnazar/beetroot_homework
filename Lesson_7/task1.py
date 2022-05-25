"""Write a function that takes on an input random ints (between 1 and 10) and returns the longest consecutive run
and the length of that run of elements of the list.
Ex. 	def task1(1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5) -> 6, 4
        def task1(1) -> 1, 1
        def task1() -> 0, None
Then create another function which takes on input result of function from the previous step and prints
Informative message about the longest consecutive run, something like - “Longest run is 6 of integers - 4”"""


def task1(*args):
    counts = {}
    for i in range(len(args)):
        if args[i] not in counts.keys():       # якщо такої цифри ще не було, то записую її в словник зі значенням 1
            counts[args[i]] = 1
            try:                               # виникає проблема, коли наприкінці є безперервна послідовність
                while args[i] == args[i + 1]:
                    counts[args[i]] += 1
                    i += 1
            except IndexError:
                pass
        else:                                  # якщо зустрічаємо нову послідовність цифри, яка вже є в нашому словнику
            try:
                alter_count = 1                    # створюю альтернативний лічильник
                while args[i] == args[i + 1]:      # перевіряю послідовність
                    alter_count += 1
                    i += 1
            except IndexError:
                pass
                if alter_count > counts[args[i]]:  # якщо нова послідовність більша за попередню,
                    counts[args[i]] = alter_count  # переписую її в словнику
    # print(counts)
    for key in counts:
        if counts[key] == max(counts.values()):
            return max(counts.values()), key
    return 0, None  # цей результат отримаємо, якщо функцію викликано без параметрів


print(task1(1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 4, 4, 2, 2, 5))
print(task1(1))
print(task1())


def task2(func):
    run, numb = func
    print(f'Longest run is {run} of integers - {numb}')


task2(task1(1, 1, 2, 2, 2, 3, 3))
