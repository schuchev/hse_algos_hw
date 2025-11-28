import pytest
from homework_7.K_th_minheap.solve import kth_largest_minheap, kth_largest_heapq

def test_1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert kth_largest_minheap(nums, k) == 5
    assert kth_largest_heapq(nums, k) == 5

def test_2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert kth_largest_minheap(nums, k) == 4
    assert kth_largest_heapq(nums, k) == 4

def test_3():
    nums = [1,2,3,4,5]
    k = 5
    assert kth_largest_minheap(nums, k) == 1
    assert kth_largest_heapq(nums, k) == 1

def test_4():
    nums = [1,2,3,4,5]
    k = 1
    assert kth_largest_minheap(nums, k) == 5
    assert kth_largest_heapq(nums, k) == 5

def test_5():
    nums = [1,2,3]
    k = 5
    assert kth_largest_minheap(nums, k) is None
    assert kth_largest_heapq(nums, k) is None
