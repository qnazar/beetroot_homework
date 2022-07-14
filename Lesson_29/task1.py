"""Implement binary search using recursion."""


def binary_search(item, seq):
    if len(seq) == 0:
        return False
    mid = len(seq) // 2
    if seq[mid] == item:
        return True
    elif item < seq[mid]:
        return binary_search(item, seq[:mid])
    elif item > seq[mid]:
        return binary_search(item, seq[mid+1:])


lst = [1, 3, 8, 12, 34, 54, 60, 68, 79, 80, 85, 92, 99, 102]
print(binary_search(8, lst))
