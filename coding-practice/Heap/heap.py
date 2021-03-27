# given level order for tree build max-heap
# given level order for tree build min-heap
# given level order of heap insert a element
# given level order of heap delete a element
# if time permits then heap sort

import copy

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

'''
BEFORE
                   1
              //     \\
             3          5
          //   \\     //  \\
         4       6    13    10
       // \\    // \\
      9    8   15   17

AFTER
                   17
              //      \\
             15         13
          //    \\      //  \\
          9        6    5   10
        // \\    //  \\
       4     8   3    1
'''

level_order1 = [1, 3, 6, 5, 9, 9]
build_max_heap(level_order1)
print(level_order1)
level_order2 = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
build_max_heap(level_order2)
heap1 = copy.deepcopy(level_order2)
print(level_order2)


def min_heapify(arr, i, n):
    smallest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, smallest, n)

def build_min_heap(arr):
    n = len(arr)
    non_leaf = (n//2)-1
    for j in range(non_leaf, -1, -1):
        min_heapify(arr, j, n)

build_min_heap(level_order1)
print(level_order1)
build_min_heap(level_order2)
print(level_order2)

def deletenode(arr, i, n):  # delete element at i position of arr(level order of heap)
    if i == n-1:
        n = n-1
        arr =arr[:-1]
        return
    arr[i] = arr[n-1]
    n = n-1
    arr[:] = arr[:-1]
    min_heapify(arr, i, n)

n = len(level_order2)
deletenode(level_order2, 5, n)
print(level_order2)


# if it is a min heap then insert number at root else if max heap 
# then insert at end. after that call corresponding heapify func
def insertnode(arr, n, num):
    arr.insert(0, num)
    #arr.append(num)
    #print(arr)
    min_heapify(arr, 0, n+1)
    #max_heapify(arr, n, n+1)

insertnode(level_order2, len(level_order2), 99)
print(level_order2)

#print(f'heap 1 before {heap1}')
#insertnode(heap1, len(heap1), -99)
#print(f'heap1 after f{heap1}')