def interpolation_search(arr, x, n):
    low = 0
    high = n-1

    while low <= high and arr[low] <= x and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
        pos = low + ((high-low)//(arr[high]-arr[low]))*(x-arr[low])

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        elif arr[pos] > x:
            high = pos - 1
    return -1

# test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 27, 34]
result = interpolation_search(arr, 14, 16)
print(result)
result = interpolation_search(arr, 2, 16)
print(result)
result = interpolation_search(arr, -1, 16)
print(result)
result = interpolation_search(arr, 37, 16)
print(result)
result = interpolation_search(arr, 10, 16)
print(result)
arr= [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 13, 14, 27, 34]
result = interpolation_search(arr, 7, 16)
print(result)