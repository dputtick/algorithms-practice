import itertools
import pytest
import random as r

from binary_heap import BinaryHeap


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


@pytest.mark.skip
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
    heap.heap_list = [0, 1, 2, 3]
    heap.current_size = 3
    is_valid_heap(heap)
    heap2 = BinaryHeap()
    heap2.heap_list = [0, 1, 2, 3, 4]
    heap2.current_size = 4
    is_valid_heap(heap2)


def test_perc_down():
    assert True


def test_perc_up():
    assert True

#def test_naive_build_heap():
#    heap = BinaryHeap()
#    heap.heap_list = [0, 1, 2, 3, 5, 23, 120]
#    heap.current_size = 6
#    is_valid_heap(heap)



# helper functions here

def is_valid_heap(heap):
    n_single_child = 0
    n_leafs = 0
    for parent_index in range(1, heap.current_size + 1):
        child1, child2 = get_child_indices(heap, parent_index)
        if child1:
            assert heap.heap_list[child1] >= heap.heap_list[parent_index]
            if child2:
                # do the stuff for two children
                assert heap.heap_list[child2] >= heap.heap_list[parent_index]
            else:
                # do the stuff for one child
                n_single_child += 1
        else:
            # do the stuff for no children
            n_leafs += 1
    assert n_single_child <= 1
    nearest_power_of_two = heap.current_size // 2
    assert n_leafs == len(heap.heap_list[nearest_power_of_two + 1:])


def can_assert_true(thing):
    assert True

def can_assert_false(thing):
    assert False

def get_child_indices(heap, index):
    child_1 = index * 2
    child_2 = child_1 + 1
    if child_1 <= heap.current_size:
        if child_2 <= heap.current_size:
            return (child_1, child_2)
        else:
            return (child_1, None)
    else:
        return (None, None)

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
