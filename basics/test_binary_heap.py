import itertools
import pytest
import random as r

from binary_heap import BinaryHeap


skip = pytest.mark.skip
xfail = pytest.mark.xfail

heaps = {
    'built empty': BinaryHeap([]),
    'empty': BinaryHeap(),
    'single item': BinaryHeap([1])
    }

unsorted_lists = list(itertools.permutations([1, 2, 3]))

def make_valid_heaps():
    valid_heaps = []
    for permutation in unsorted_lists:
        heap = BinaryHeap()
        for item in permutation:
            heap.insert(item)
        valid_heaps.append(heap)
    return valid_heaps

valid_heaps = make_valid_heaps()


def test_empty_heap():
    heap = BinaryHeap()
    is_valid_heap(heap)


def test_simple_heaps_build():
    for permutation in unsorted_lists:
        heap = BinaryHeap(permutation)
        is_valid_heap(heap)


def test_manually_constructed_heaps():
    for permutation in unsorted_lists:
        heap = naive_construct_heap(permutation)
        is_valid_heap(heap)


def test_get_from_heaps():
    for heap in valid_heaps:
        is_valid_heap(heap)
        heap.get()
        is_valid_heap(heap)


def test_valid_heaps():
    heap = BinaryHeap()
    heap._list = [0, 1, 2, 3]
    heap._size = 3
    is_valid_heap(heap)
    heap2 = BinaryHeap()
    heap2._list = [0, 1, 2, 3, 4]
    heap2._size = 4
    is_valid_heap(heap2)


def test_min_child():
    heap = naive_construct_heap([1, 2, 3])
    min_child = heap._min_child(1)
    assert min_child == 2


def test_perc_down():
    heap = BinaryHeap()
    heap._list = [0, 1, 100, 2]
    heap._size = 3
    heap._perc_down(1)
    is_valid_heap(heap)


def test_perc_up():
    heap = BinaryHeap()
    heap._list = [0, 100, 101, 1]
    heap._size = 3
    heap._perc_up(3)
    is_valid_heap(heap)


# helper functions here

def is_valid_heap(heap):
    n_single_child = 0
    n_leafs = 0
    for parent_index in range(1, heap._size + 1):
        children = get_child_indices(heap, parent_index)
        for child in children:
            assert heap._list[child] >= heap._list[parent_index]
        if not children:
            n_leafs += 1
        elif len(children) == 1:
            n_single_child += 1
    assert n_single_child <= 1
    assert n_leafs == len(heap._list[heap._size // 2 + 1:])


def can_assert_true(thing):
    assert True

def can_assert_false(thing):
    assert False

def get_child_indices(heap, index):
    child_1 = index * 2
    child_2 = child_1 + 1
    if child_1 <= heap._size:
        if child_2 <= heap._size:
            return (child_1, child_2)
        else:
            return (child_1,)
    else:
        return ()

def naive_construct_heap(alist):
    new_heap = BinaryHeap()
    for number in alist:
        new_heap.insert(number)
    return new_heap




# I can either have a function that returns True or False if I have a valid heap
# and then uses asserts to check whether various things are giving me valid heaps
# OR
# I can have a master test_if_heap function that checks all the ways a heap can fail
# and I can programatically generate various heaps and see whether those pass


# list of properties of a heap, test each property individually
# how do I think of examples - random examples, simple examples that are easy to follow
# debugging: use the debugger, add comments for every line, think of the simplest possible test case
