# insert a element to BST..guarantee that it doesn't already exist
# there are many possible valid answers
# we will try to take it to the leaf and ofcourse still maintain BST property

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_recu(root):
    if root:
        inorder_recu(root.left)
        print(root.val)
        inorder_recu(root.right)

def insert_to_BST(node, num):
    if not node:
        return Node(num)
    if node.val < num:
        node.right = insert_to_BST(node.right, num)
    if num < node.val:
        node.left = insert_to_BST(node.left, num)
    return node


'''
           5
             
        4      6
               
      3          7
     
    1
'''
tree = Node(5)
tree.left = Node(4)
tree.right = Node(6)
tree.left.left = Node(3)
tree.left.left.left = Node(1)
tree.right.right = Node(7)
print('Before')
inorder_recu(tree)
insert_to_BST(tree, 5.5)
print('After')
inorder_recu(tree)