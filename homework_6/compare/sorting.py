import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} выполнена за {end - start:.6f} секунд")
        return result
    return wrapper

def _mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = _mergesort(a[:mid])
    right = _mergesort(a[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

@timeit
def mergesort(a):
    return _mergesort(a)

def _quicksort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return _quicksort(left) + middle + _quicksort(right)

@timeit
def quicksort(a):
    return _quicksort(a)
