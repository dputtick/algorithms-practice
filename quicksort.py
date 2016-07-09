import random as r


def sort(sequence, low_index, high_index):
    if low_index < high_index:
        pivot_index = partition(sequence, low_index, high_index)
        sort(sequence, low_index, pivot_index - 1)
        sort(sequence, pivot_index + 1, high_index)


def partition(sequence, low_index, high_index):
    pivot_value = sequence[high_index]
    left = low_index
    for right in range(low_index, high_index):
        if sequence[right] < pivot_value:
            sequence[left], sequence[right] = sequence[right], sequence[left]
            left += 1
    sequence[left], sequence[high_index] = sequence[high_index], sequence[left]
    return left


if __name__ == '__main__':
    r.seed(5)
    sequence = list(range(1, 8))
    r.shuffle(sequence)
    sort(sequence, 0, len(sequence) - 1)
    print("Done: ", sequence)