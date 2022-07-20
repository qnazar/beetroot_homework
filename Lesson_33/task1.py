"""A bubble sort can be modified to “bubble” in both directions. The first pass moves “up” the list
and the second pass moves “down.” This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate."""


def double_bubble_sort(seq):
    swapped = True
    start = 0
    end = len(seq) - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(end-1, start-1, -1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        start += 1


seq = [8, 4, 9, 6, 3, 2, 11, 0]
double_bubble_sort(seq)
print(seq)
