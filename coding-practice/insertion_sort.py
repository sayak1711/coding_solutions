def insertion_sort(arr):
    l = len(arr)
    for i in range(1, l):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# TEST
print(insertion_sort([64, 25, 12, 22, 11]))
print(insertion_sort([64, -25, -12, -22, 11]))
print(insertion_sort([5, 1, 4, 2, 8]))
print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))