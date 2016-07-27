import random as r


def quicksort(sequence, low, high):
    if high > low:
        pivot_index = partition(sequence, low, high)
        quicksort(sequence, low, pivot_index - 1)
        quicksort(sequence, pivot_index + 1, high)


def partition(sequence, low, high):
    pivot_value = sequence[high]
    p = low
    for i in range(low, high):
        if sequence[i] < pivot_value:
            sequence[i], sequence[p] = sequence[p], sequence[i]
            p += 1
    sequence[p], sequence[high] = sequence[high], sequence[p]
    return p



r.seed(5)
sequence = list(range(1, 1000000))
r.shuffle(sequence)
quicksort(sequence, 0, len(sequence) - 1)