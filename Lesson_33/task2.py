"""Implement the mergeSort function without using the slice operator."""


def merge_sort(array):
    # умова виходу - з довжиною 1 список сортований
    if len(array) > 1:
        mid = len(array) // 2  # знайшли середину списку
        left_half = [array[i] for i in range(0, len(array)) if i % 2 == 0]  # робимо поділ схожий на shell sort
        right_half = [array[i] for i in range(0, len(array)) if i % 2 == 1]  #
        print(left_half, right_half)
        merge_sort(left_half)  # рекурсивно запускаємо з лівим списком
        merge_sort(right_half)  # рекурсивно з правим

        i = 0  # індекс лівого списку
        j = 0  # індекс правого
        k = 0  # індекс результату
        while i < len(left_half) and j < len(right_half):  # поки не закінчився один зі списків
            # порівнюємо елементи з двох списків і додаємо менший в основний список
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i = i + 1
            else:
                array[k] = right_half[j]
                j = j + 1
            k = k + 1
        # додаємо залишок списку
        while i < len(left_half):
            array[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            array[k] = right_half[j]
            j = j + 1
            k = k + 1


l = [2, 8, 6, 4, 7, 5, 3, 1]
merge_sort(l)
print(l)
