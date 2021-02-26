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


def inorder_recu(root):
    if root:
        inorder_recu(root.left)
        print(root.val)
        inorder_recu(root.right)

#inorder_recu(root)

def left_movement(stack, cur):
    while cur:
        stack.append(cur)
        cur = cur.left
    return cur

def inorder_iterative(root):
    ans = []
    stack = []
    cur = root
    while cur or stack:
        cur = left_movement(stack, cur)
        if cur is None:
            lifo_item = stack.pop()
            ans.append(lifo_item.val)
            cur = lifo_item.right
    print('-->'.join([str(a) for a in ans]))

inorder_iterative(root)

'''
           10
    11          9
7       12   15     8
'''