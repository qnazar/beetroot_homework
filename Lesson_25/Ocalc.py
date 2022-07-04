from typing import List, Tuple
import big_o  # type: ignore
from random import randint
# ----------------------------------------------------------------------------------------------------------------------


def question1(first_list: List[int], second_list: List[int] = None) -> List[int]:
    if second_list is None:
        second_list = [randint(1, len(first_list)) for _ in range(len(first_list))]
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


int_gen = lambda n: big_o.datagen.integers(n, 1, n)
res = []
for _ in range(10):
    best, _ = big_o.big_o(question1, int_gen, min_n=1000, max_n=5000, n_measures=10)
    res.append(best.__class__.__name__)
print('1 ---', max(res, key=lambda n: res.count(n)), res)
# ----------------------------------------------------------------------------------------------------------------------


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


res = []
for _ in range(10):
    best, _ = big_o.big_o(question2, big_o.datagen.n_, n_measures=10)
    res.append(best.__class__.__name__)
print('2 ---', max(res, key=lambda n: res.count(n)), res)
# ----------------------------------------------------------------------------------------------------------------------


def question3(first_list: List[int], second_list: List[int] = None) -> List[int]:
    second_list = [randint(1, len(first_list)) for _ in range(len(first_list))]
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(el_second_list)
    return temp


int_gen = lambda n: big_o.datagen.integers(n, 1, n)
res = []
for _ in range(5):
    best, _ = big_o.big_o(question3, int_gen, n_measures=20, min_n=1000, max_n=5000)
    res.append(best.__class__.__name__)
print('3 ---', max(res, key=lambda n: res.count(n)), res)
# ----------------------------------------------------------------------------------------------------------------------


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


int_gen = lambda n: big_o.datagen.integers(n, 1, n)
res = []
for _ in range(10):
    best, _ = big_o.big_o(question4, int_gen)
    res.append(best.__class__.__name__)
print('4 ---', max(res, key=lambda n: res.count(n)), res)
# ----------------------------------------------------------------------------------------------------------------------


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


res = []
for _ in range(10):
    best, _ = big_o.big_o(question5, big_o.datagen.n_, n_measures=10, max_n=2000)
    res.append(best.__class__.__name__)
print('5 ---', max(res, key=lambda n: res.count(n)), res)
# ----------------------------------------------------------------------------------------------------------------------


def question6(n: int) -> int:
    while n > 1:
        n //= 3
    return n


res = []
data_gen = lambda n: 1_000_000_000_000
for _ in range(10):
    best, others = big_o.big_o(question6, data_gen)
    res.append(best.__class__.__name__)
print('6 ---', max(res, key=lambda n: res.count(n)), res)
for o in others:
    print(o)


def log_n(data):
    for index in range(0, len(data), 3):
        print(data[index])


int_gen = lambda n: big_o.datagen.integers(n, 1, n)
res = []
for i in range(10):
    best, other = big_o.big_o(log_n, int_gen, min_n=10, max_n=1000, n_measures=10)
    res.append(best.__class__.__name__)
print(res)
