def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)


#....pivot....

def partition(arr, l, h):
    i = l-1
    pivot_index = h
    pivot = arr[pivot_index]
    for j in range(l, pivot_index):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[pivot_index] = arr[pivot_index], arr[i+1]
    return i+1

arr = [10, 7, 8, -9, 1, 5]
quicksort(arr, 0, 5)
print(arr)