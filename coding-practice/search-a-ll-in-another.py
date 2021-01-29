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


def search_ll(ll1, ll2):
    # search ll1 in ll2
    first = ll1
    second = ll2
    while ll2 is not None:
        while first is not None and second is not None:
            print(first.val, second.val)
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                first = ll1
                second = ll2.next
                ll2 = ll2.next
        if first is None:
            return True
        elif first is not None and second is None:
            return False
    return False


# TEST 1
# node_a: 1->2->3->4 
# node_b: 1->2->1->2->3->4 
node_a = generate_linked_list([1, 2, 3, 4])
node_b = generate_linked_list([1, 2, 1, 2, 3, 4])
  
if search_ll(node_a, node_b): 
    print("LIST FOUND") 
else: 
    print("LIST NOT FOUND")

print()
# TEST 2
# node_a: 10->20
# node_b: 5->10->20
node_a = generate_linked_list([10, 20])
node_b = generate_linked_list([5, 10, 20])

if search_ll(node_a, node_b): 
    print("LIST FOUND") 
else: 
    print("LIST NOT FOUND")

print()
# TEST 3
# node_a: 1->2->3->4
# node_b: 1->2->2->1->2->3
node_a = generate_linked_list([1, 2, 3, 4])
node_b = generate_linked_list([1, 2, 2, 1, 2, 3])

if search_ll(node_a, node_b): 
    print("LIST FOUND") 
else: 
    print("LIST NOT FOUND")