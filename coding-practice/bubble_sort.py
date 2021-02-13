def bubble_sort(arr):
    l = len(arr)
    while True:
        i = 0
        alteration = False
        while i < l-1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                alteration = True
            i += 1
        if not alteration:
            break
    return arr

# TEST
print(bubble_sort([64, 25, 12, 22, 11]))
print(bubble_sort([64, -25, -12, -22, 11]))
print(bubble_sort([5, 1, 4, 2, 8]))
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
