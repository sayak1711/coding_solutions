# 64 25 12 22 11
# a = a+b
# b = a-b

def selection_sort(arr):
    i = 0
    while i < len(arr):
        smallest = 9999999
        pos = i
        for j in range(i, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                pos = j
        arr[pos] = arr[i]
        arr[i] = smallest
        i += 1
    return arr

print(selection_sort([64, -25, -12, -22, 11]))
