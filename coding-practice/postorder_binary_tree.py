from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.left.right = Node(12)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

'''
           10
    11          9
7       12   15     8
'''

def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.val)

postorder_recursive(root)

def postorder_iterative(root):
    stack = [root]
    ans = []
    while stack:
        lifo = stack.pop()
        ans.append(str(lifo.val))
        if lifo.left:
            stack.append(lifo.left)
        if lifo.right:
            stack.append(lifo.right)
    ans.reverse()
    print('-->'.join(ans))

postorder_iterative(root)
