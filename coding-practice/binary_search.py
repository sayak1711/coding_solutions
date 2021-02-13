def binary_search(arr, num):
    if len(arr) == 0:
        return -1
    l = 0
    r = len(arr)-1
    
    while l <= r:
        if l == r:
            if arr[l] == num:
                return l
            else:
                return -1
        mid = l+(r-l)//2
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            r = mid-1
        elif arr[mid] < num:
            l = mid+1
    return -1

# find the posiition where num can be inserted
def bs_pos(arr, num):
    if len(arr) == 0:
        return -1
    l = 0
    r = len(arr)-1
    
    while l <= r:
        if l == r:
            if arr[l] == num:
                return l
            else:
                if num <= arr[l]:
                    return l
                else:
                    return l+1
        mid = l+(r-l)//2
        if arr[mid] == num or (arr[mid-1]< num and num < arr[mid]):
            return mid
        elif num < arr[mid]:
            r = mid-1
        elif arr[mid] < num:
            l = mid+1
    return -1
