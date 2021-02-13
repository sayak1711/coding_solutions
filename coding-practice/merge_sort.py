def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1
    
# TEST
arrs = [[64, 25, 12, 22, 11], [64, -25, -12, -22, 11], [5, 1, 4, 2, 8], [64, 34, 25, 12, 22, 11, 90]]
for arr in arrs:
    merge_sort(arr)
    print(arr)
