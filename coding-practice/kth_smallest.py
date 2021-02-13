def find_pivot(arr, l, r):
    pivot = r  # we choose last number to be pivot
    # now we find its rightful place in the array 'were it sorted'
    i = l-1
    for j in range(l, r):
        if arr[j] < arr[pivot]:  # then it belongs to the left of 'pivot's correct posi'
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]  # i+1 is the rightful place of our chosen pivot num
    # all elements to left of pivot will be lesser than it and ones to the right will be greater
    # but the left and right parts won't necessarily be sorted
    return i+1

def find_elem_quicksort(arr, k, l, r):
    if k > 0 and k <= r-l+1: # it is imp to check this
        pivot = find_pivot(arr, l, r)
        if pivot-l+1 == k:  # pivot-l+1 is the num of elements from l to pivot
            return arr[pivot]  # as pivot is in correct place so it is the kth smallest
        elif k < pivot-l+1:
            return find_elem_quicksort(arr, k, l, pivot-1)
        elif pivot-l+1 < k:  # then it is to the right of pivot
            # since we are looking from kth smallest globally it is k-(size_of_left_subarray-and-pivot)
            # positions to the right of pivot
            return find_elem_quicksort(arr, k-(pivot-l+1), pivot+1, r)
    else:
        return 'NO ANSWER'

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(find_elem_quicksort(arr, k, 0, len(arr)-1))

arr = [7, 10, 4, 3, 20, 15]
k = 4
print(find_elem_quicksort(arr, k, 0, len(arr)-1))