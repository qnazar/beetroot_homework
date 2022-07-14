"""Read about the Fibonacci search and implement it using python.
Explore its complexity and compare it to sequential, binary searches."""
import timeit
import big_o
from functools import partial


def fibonacci_search(item, seq):
    fib_min_2 = 0
    fib_min_1 = 1
    fib = fib_min_1 + fib_min_2
    while fib < len(seq):
        fib_min_2 = fib_min_1
        fib_min_1 = fib
        fib = fib_min_1 + fib_min_2
    index = -1
    while fib > 1:
        i = min(index + fib_min_2, len(seq) - 1)
        if seq[i] < item:
            fib = fib_min_1
            fib_min_1 = fib_min_2
            fib_min_2 = fib - fib_min_1
            index = i
        elif seq[i] > item:
            fib = fib_min_2
            fib_min_1 = fib_min_1 - fib_min_2
            fib_min_2 = fib - fib_min_1
        else:
            return i
    if fib_min_1 and index < (len(seq) - 1) and seq[index + 1] == item:
        return index + 1
    return -1


def linear_search(item, seq):
    for index, i in enumerate(seq):
        if i == item:
            return index
    return -1


def binary_search(item, seq):
    start = 0
    end = len(seq) - 1
    while start <= end:
        middle = (start + end) // 2
        if seq[middle] == item:
            return middle
        elif seq[middle] < item:
            start = middle + 1
        elif seq[middle] > item:
            end = middle - 1
    return -1


control_list = [x for x in range(200)]

print('fibonacci_search:', timeit.timeit(stmt=f'fibonacci_search(134, {control_list})',
                                         setup='from __main__ import fibonacci_search',
                                         number=100000))
print('linear_search:', timeit.timeit(stmt=f'linear_search(134, {control_list})',
                                      setup='from __main__ import linear_search',
                                      number=100000))
print('binary_search:', timeit.timeit(stmt=f'binary_search(134, {control_list})',
                                      setup='from __main__ import binary_search',
                                      number=100000))

data_gen = lambda n: big_o.datagen.integers(n, 1, n)
func = partial(fibonacci_search, 12000)
best, others = big_o.big_o(func, data_gen, min_n=200, max_n=20000, n_measures=100)
print(best)

data_gen = lambda n: big_o.datagen.integers(n, 1, n)
func = partial(linear_search, 12000)
best, others = big_o.big_o(func, data_gen, min_n=200, max_n=20000, n_measures=100)
print(best)

data_gen = lambda n: big_o.datagen.integers(n, 1, n)
func = partial(binary_search, 12000)
best, others = big_o.big_o(func, data_gen, min_n=200, max_n=20000, n_measures=100)
print(best)
