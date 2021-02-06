def find_in_rot(arr, num, l, r):
    if l > r:
        return 'NOT FOUND'
    if l <= r:
        mid = l+(r-l)//2
        if arr[mid] == num:
            return mid
        # we try to determine if the num lies in sorted part or unsorted part
        # if l...mid is sorted
        elif arr[l] <= arr[mid]:
            # is num within this?
            if arr[l] <= num and num < arr[mid]:
                return find_in_rot(arr, num, l, mid-1) # mid has already been checked before..so exclude
            else:

                return find_in_rot(arr, num, mid+1, r)
        
        # if it is not sorted then l lies left of rot point and mid to the right
        # so num could lie in mid+1 to r
        # or anywhere from l to mid-1
        # l.....rot_point....mid....r
        else:
            if arr[mid] < num and num <= arr[r]:
                return find_in_rot(arr, num, mid+1, r)
            else:
                return find_in_rot(arr, num, l, mid-1)

arrs = [[4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 7, 8, 9, 10, 1, 2, 3], [5, 6, 7, 8, 9, 10, 1, 2, 3], [30, 40, 50, 10, 20]]
keys = [6, 3, 30, 10]

for arr, key in zip(arrs, keys):
    print(find_in_rot(arr, key, 0, len(arr)-1))