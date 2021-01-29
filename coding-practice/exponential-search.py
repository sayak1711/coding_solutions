# time complexity is O(log(n))

def binary_search(arr, l, h, num):
    while l <= h:
        mid = int(l+(h-l)//2)
        if arr[mid] == num:
            return mid
        if num < arr[mid]:
            h = mid-1
        elif arr[mid] < num:
            l = mid+1
    return -1
        

def exponential_search(arr, num, n): # array, number-to-find, length of array
    if arr[0] == num:
        return 0
    i = 1
    while i < n and arr[i] <= num:
        i *= 2
    
    return binary_search(arr, i/2, min(n-1, i), num)

# test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 27, 34]
result = exponential_search(arr, 14, 16)
print(result)
result = exponential_search(arr, 2, 16)
print(result)
result = exponential_search(arr, -1, 16)
print(result)
result = exponential_search(arr, 37, 16)
print(result)
result = exponential_search(arr, 10, 16)
print(result)
arr= [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 13, 14, 27, 34]
result = exponential_search(arr, 7, 16)
print(result)