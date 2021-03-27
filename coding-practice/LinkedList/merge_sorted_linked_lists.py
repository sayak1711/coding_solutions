class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def generate_linked_list(numbers):
    head = Node(numbers[0])
    prev = head
    i = 1
    while i < len(numbers):
        new_node = Node(numbers[i])
        prev.next = new_node
        prev = new_node
        i += 1
    return head

def print_ll(ll):
    answer = ''
    while ll is not None:
        answer += str(ll.val)+'-->'
        ll = ll.next
    answer += 'None'
    print(answer)

# APPROACH 1: naivest: put everything in a array, then make a linked list out of it
def approach_naive(list_of_ll):
    all_numbers = []
    for ll in list_of_ll:
        while ll is not None:
            all_numbers.append(ll.val)
            ll = ll.next
    all_numbers.sort()
    return generate_linked_list(all_numbers)

lls = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
lls = [generate_linked_list(l) for l in lls]
print('Initial linked lists were:')
for l in lls:
    print_ll(l)
print()
#print_ll(approach_naive(lls))

# APPROACH 2: compare one by one by using many pointers
def approach_onebyone(list_of_ll):
    all_numbers = []
    
    
    while True:
        smallest = 999999999
        smallest_idx = 0
        done = True
        for i, ll in enumerate(list_of_ll):
            if ll is None:
                continue
            done = False
            if ll.val < smallest:
                smallest = ll.val
                smallest_idx = i
        if done:
            break

        all_numbers.append(smallest)
        list_of_ll[smallest_idx] = list_of_ll[smallest_idx].next
    return generate_linked_list(all_numbers)

#print_ll(approach_onebyone(lls))

from queue import PriorityQueue
# APPROACH 3: Use priority queue
def approach_pq(list_of_ll):
    head = cur = Node(0)  # both pointing to a dummy node
    # take heads of all linked lists first just like previous approach
    pq = PriorityQueue()
    for ll in list_of_ll:
        if ll:
            pq.put((ll.val, ll))
    # priority queue will order them according to value
    
    while not pq.empty():
        val, node = pq.get()
        cur.next = Node(val)
        cur = cur.next
        if node.next is not None:
            pq.put((node.next.val, node.next))
    return head.next

#head = approach_pq(lls)
#print_ll(head)

# APPROACH 4: Merge 2 at a time..so k-1 merges for k ll O(kN)
def approach_twoatatime(list_of_ll):
    cur = list_of_ll[0]
    for i in range(1, len(list_of_ll)):
        cur = merge_two_ll(cur, list_of_ll[i])
    return cur

def merge_two_ll(ll1, ll2):
    cur = head = Node(0)  # dummy
    while ll1 is not None and ll2 is not None:
        if ll1.val < ll2.val:
            cur.next = Node(ll1.val)
            ll1 = ll1.next
            cur = cur.next
        else:
            cur.next = Node(ll2.val)
            ll2 = ll2.next
            cur = cur.next
    while ll1 is not None:
        cur.next = Node(ll1.val)
        ll1 = ll1.next
        cur = cur.next
    while ll2 is not None:
        cur.next = Node(ll2.val)
        ll2 = ll2.next
        cur = cur.next
    return head.next

#head = approach_twoatatime(lls)
#print_ll(head)

# APPROACH 5:Same as before but merge pairs of 2 at first step...1 and 2...3 and 4...5 and 6
# so now we have k/2 lls. then in next step again take pairs of 2 and so on
# advantage is that we avoid having many repeated comparisons O(NlogK)
def approach_merge_divide_and_conquer(list_of_ll):
    previous_level = list_of_ll
    while len(previous_level) > 1:
        cur_level = []
        i = 0
        while i < len(previous_level)-1:
            cur_level.append(merge_two_ll(previous_level[i], previous_level[i+1]))
            i += 2
        if i == len(previous_level)-1:
            cur_level.append(previous_level[i])
        previous_level = cur_level
    return previous_level[0]
head = approach_merge_divide_and_conquer(lls)
print_ll(head)

            