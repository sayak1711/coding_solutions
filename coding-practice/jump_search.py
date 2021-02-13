import math

# array needs to be sorted for this algo to work
def jump_search(arr, num): # arr is the list of numbers, num is the number to find in arr
    arr_size = len(arr)
    jump_size = math.sqrt(arr_size) # optimal jump size

    # keep jumping until we overshoot the value or reach the end
    i = jump_size
    prev = 0
    while arr[int(min(i, arr_size))-1] < num:
        prev = i
        i += jump_size
        if prev >= arr_size: # then it means that even arr[n-1] is less than our num
            return -1
        
    # now do linear search from prev to current position or last
    while arr[int(prev)] < num: # increment it by 1 step this time
        prev += 1
        if prev == min(arr_size, i): # element isn't present as it hasn't been found yet
            return -1
    
    if arr[int(prev)] == num:
        return int(prev)
    
    return -1

# test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 27, 34]
result = jump_search(arr, 14)
print(result)
result = jump_search(arr, 2)
print(result)
result = jump_search(arr, -1)
print(result)
result = jump_search(arr, 37)
print(result)
result = jump_search(arr, 10)
print(result)
