# one by one number is coming and median has to be told for the nums seen so far

# APPROACH 1: naive: keep sorting everytime a new one comes O(nlogn)+O(1) ~ O(nlogn)
# APPROACH 2: when new num comes insert it in its correct place using bsearch so 
# that it stays sorted always O(logn)+O(n) ~ O(n)
# APPROACH 3: 2 heaps maxheap and minheap maxheap will represent the lower half of the numbers
# seen so far and min-heap the upper half. head of max-heap will be largest num of lower
# half while head of min-heap will be smallest of upper half
# at any point max-heap is allowed to contain 1 more element than the min-heap
# so if max-heap contains 1 extra then its head is the median otherwise average of 2 heads is median
# algo is to put in max-heap, then put head to min-heap, then if max-heap size is less than min-heap
# put min-heap head to max-heap

import heapq

min_heap = []
max_heap = []
def approach_heap(num):
    max_heap.append(num)
    heapq._heapify_max(max_heap)
    
    heapq.heappush(min_heap, heapq._heappop_max(max_heap))

    if len(max_heap) < len(min_heap):
        max_heap.append(heapq.heappop(min_heap))
        heapq._heapify_max(max_heap)
    print(f'max-heap {max_heap}')
    print(f'min-heap {min_heap}')
    if len(max_heap) > len(min_heap):
        print(f'Median is {max_heap[0]}')
    else:
        print(f'Median is {(max_heap[0]+min_heap[0])/2}')
    print()

for num in [41, 35, 62, 4, 97, 108]:
    approach_heap(num)


