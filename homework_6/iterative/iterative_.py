import time
import random
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
    width = 1
    n = len(a)
    result = a[:]
    
    while width < n:
        for i in range(0, n, 2*width):
            left = result[i:i+width]
            right = result[i+width:i+2*width]
            result[i:i+2*width] = merge(left, right)
        width *= 2
    return result

@timeit
def quicksort(a):
    stack = [(0, len(a)-1)]
    result = a[:]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(result, low, high)
            stack.append((low, pivot_index-1))
            stack.append((pivot_index+1, high))
    return result

def partition(a, low, high):
    pivot_index = random.randint(low, high)
    a[pivot_index], a[high] = a[high], a[pivot_index]
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i+1
