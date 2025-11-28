def sift_down(heap, i, n):
    while True:
        left = 2*i + 1
        right = 2*i + 2
        smallest = i
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        if smallest == i:
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest

def sift_up(heap, i):
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

def build_minheap(arr):
    n = len(arr)
    for i in reversed(range((n - 2)//2 + 1)):
        sift_down(arr, i, n)
    return arr

def replace_root(heap, val):
    heap[0] = val
    sift_down(heap, 0, len(heap))

def kth_largest_minheap(nums, k):
    if k > len(nums):
        return None
    heap = nums[:k]
    build_minheap(heap)
    for num in nums[k:]:
        if num > heap[0]:
            replace_root(heap, num)
    return heap[0]


import heapq

def kth_largest_heapq(nums, k):
    if k > len(nums):
        return None
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
