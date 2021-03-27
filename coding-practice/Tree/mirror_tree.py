# convert tree to its mirror and print inorder of mirror

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

def get_mirror(tree):
    if not tree:
        return
    root = Node(tree.val) # root will be same
    # left will be right and right will be left
    root.left = get_mirror(tree.right)
    root.right = get_mirror(tree.left)
    return root

'''
      10
       
    20   30
     
  40  60
'''
tree = Node(10)
tree.left = Node(20)
tree.right = Node(30)
tree.left.left = Node(40)
tree.left.right = Node(60)

ans = get_mirror(tree)
inorder_recu(ans)
print()
'''
      1
      
   2    3
'''
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
ans = get_mirror(tree)
inorder_recu(ans)
