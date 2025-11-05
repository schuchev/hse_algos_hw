import pytest
import random
from homework_6.compare.sorting import mergesort, quicksort

def test_1():
    arr = list(range(1000))
    res1 = quicksort(arr)
    res2 = mergesort(arr)
    assert res1 == res2 == sorted(arr)

def test_2():
    arr = [random.randint(0, 10000) for _ in range(1000)]
    res1 = quicksort(arr)
    res2 = mergesort(arr)
    assert res1 == res2 == sorted(arr)

def test_3():
    arr = list(range(200000, 0, -1)) 
    res1 = quicksort(arr)
    res2 = mergesort(arr)
    assert res1 == res2 == sorted(arr)
    
def test_4():
    arr = [38] * 200000 
    res1 = quicksort(arr)
    res2 = mergesort(arr)
    assert res1 == res2 == sorted(arr)