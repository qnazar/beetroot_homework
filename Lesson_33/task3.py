"""One way to improve the quicksort is to use an insertion sort on lists that are small in length
(call it the “partition limit”). Why does this make sense? Re-implement the quicksort and use it to sort a random
list of integers. Perform analysis using different list sizes for the partition limit."""
from random import randint
import time

# Quicksort algorithm is efficient if the size of the input is very large.
# Insertion sort is more efficient in case of small arrays as the number of comparisons and swaps are less.
# So we combine the two algorithms to sort efficiently using both approaches.


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        return end - start
    return wrapper


@timer
def extended_quick_sort(array, low=0, high=0, partition_limit=0):
    low = 0 if not low else low
    high = len(array) - 1 if not high else high

    while low < high:

        # insertion sort
        if high - low + 1 < partition_limit:
            insertion_sort(array, low, high)
            break

        # quick sort
        else:
            pivot = partition(array, low, high)
            if pivot - low < high - pivot:
                extended_quick_sort(array, low, pivot - 1, partition_limit)
                low = pivot + 1
            else:
                extended_quick_sort(array, pivot + 1, high, partition_limit)
                high = pivot - 1


def partition(array, low, high):
    pivot = array[high]
    j = low
    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[j] = array[j], array[i]
            j += 1
    array[j], array[high] = array[high], array[j]
    return j


@timer
def insertion_sort(array, start=0, end=0):
    # so we can use this func independently without passing parameters
    start = start if start else 0
    end = end if end else len(array) - 1

    for index in range(start+1, end+1):
        current_value = array[index]
        position = index
        while position > start and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1

        array[position] = current_value


@timer
def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)


def quick_sort_helper(array, first, last):
    if first < last:
        split_point = partition(array, first, last)

        quick_sort_helper(array, first, split_point - 1)
        quick_sort_helper(array, split_point + 1, last)


if __name__ == '__main__':
    with open('logs.txt', 'w') as file:

        length = 10000  # set the length of list
        partition_limit = 9  # set the partition limit

        file.write(f'Len = {length}, partition limit - {partition_limit}\n')
        count = {'quick': 0, 'hybrid': 0}

        for i in range(1, 11):
            l1 = [randint(-length, length) for n in range(length)]
            l2, l3 = l1[:], l1[:]

            # insert = round(insertion_sort(l1), 7)
            quick = round(quick_sort(l2), 10)
            hybrid = round(extended_quick_sort(l3, partition_limit), 10)
            if quick > hybrid:
                count['hybrid'] += 1
            else: count['quick'] += 1

            file.write(f'Pass {i}\n')
            # file.write(f'Insert: {insert}\n')
            file.write(f'Quick:  {quick}\n')
            file.write(f'Hybrid: {hybrid}\n\n')

        file.write(f'{count}')
