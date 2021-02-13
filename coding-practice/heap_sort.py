def max_heapify(arr, i, n):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, n)
    
def build_max_heap(arr):
    n = len(arr) # no of elements
    # parent of last leaf(n-1 position) is last non-leaf
    # we know that parent is in (i-1)//2
    # so for this it is at (n-1 -1)//2 i.e n//2 - 1
    non_leaf = (n//2)-1
    for j in range(non_leaf, -1, -1):
        max_heapify(arr, j, n)

level_order1 = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i)

#heap_sort(level_order1)
#print(level_order1)
    
