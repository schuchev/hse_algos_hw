def sift_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:  
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break


def makeheap_n_log_n(arr):
    heap = []
    for x in arr:
        heap.append(x)
        sift_up(heap, len(heap) - 1)
    return heap

def sift_down(heap, i, n):
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right

        if smallest == i:
            break

        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest


def makeheap(arr):
    n = len(arr)
    for i in reversed(range((n - 2) // 2 + 1)):
        sift_down(arr, i, n)
    return arr

import time
import random

arr = [random.randint(0, 1000000) for _ in range(100000)]

start = time.time()
makeheap_n_log_n(arr.copy())
end = time.time()
print(f"makeheap_n_log_n time: {end - start:.5f} s")

start = time.time()
makeheap(arr.copy())
end = time.time()
print(f"makeheap time: {end - start:.5f} s")