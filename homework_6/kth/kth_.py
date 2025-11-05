import random

def quickselect(a, k):

    def partition(left, right):
        pivot_index = random.randint(left, right)
        pivot = a[pivot_index]
        a[pivot_index], a[right] = a[right], a[pivot_index]
        store_index = left
        for i in range(left, right):
            if a[i] < pivot: 
                a[store_index], a[i] = a[i], a[store_index]
                store_index += 1
        a[store_index], a[right] = a[right], a[store_index]
        return store_index

    left, right = 0, len(a) - 1
    target = len(a) - k  
    while True:
        pivot_index = partition(left, right)
        if pivot_index == target:
            return a[pivot_index]
        elif pivot_index < target:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
