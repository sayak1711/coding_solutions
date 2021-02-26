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

def preorder_recursive(root):
    if root:
        print(root.val)
        preorder_recursive(root.left)
        preorder_recursive(root.right)

preorder_recursive(root)

def preorder_iterative(root):
    ans = []
    stack = [root]
    while stack:
        lifo = stack.pop()
        ans.append(str(lifo.val))
        if lifo.right:
            stack.append(lifo.right)
        if lifo.left:
            stack.append(lifo.left)
    print('-->'.join(ans))

preorder_iterative(root)
