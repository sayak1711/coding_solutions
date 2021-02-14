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

#lls = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
#lls = [generate_linked_list(l) for l in lls]
#print('Initial linked lists were:')
#for l in lls:
#    print_ll(l)
#print()
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

lls = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
lls = [generate_linked_list(l) for l in lls]
print('Initial linked lists were:')
for l in lls:
    print_ll(l)
print()
print_ll(approach_onebyone(lls))