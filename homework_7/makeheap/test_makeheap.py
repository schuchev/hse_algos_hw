import pytest
from homework_7.makeheap.makeheap import makeheap_n_log_n, makeheap

def is_minheap(heap):
    n = len(heap)
    for i in range(n):
        left = 2*i + 1
        right = 2*i + 2
        if left < n and heap[i] > heap[left]:
            return False
        if right < n and heap[i] > heap[right]:
            return False
    return True

def test_1():
    arr = []
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert result1 == []
    assert result2 == []

def test_2():
    arr = [9]
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert result1 == [9]
    assert result2 == [9]

def test_3():
    arr = [5, 3, 9, 1, 7, 2]
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert is_minheap(result1)
    assert is_minheap(result2)
    assert result1[0] == min(arr)
    assert result2[0] == min(arr)

def test_4():
    arr = [1,2,3,4,5]
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert is_minheap(result1)
    assert is_minheap(result2)

def test_5():
    arr = [5,4,3,2,1]
    result1 = makeheap_n_log_n(arr.copy())
    result2 = makeheap(arr.copy())
    assert is_minheap(result1)
    assert is_minheap(result2)

