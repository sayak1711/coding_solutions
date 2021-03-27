# find the minimum element in BST
#have to move in left and down direction whenever possible

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def min_in_bst(tree):
    if tree.left:
        min_in_bst(tree.left)
    elif tree.right:
        min_in_bst(tree.right)
    else:
        min_in_bst.ans = tree.val
        return

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
min_in_bst.ans = 0
min_in_bst(tree)
print(min_in_bst.ans)
print()
'''
          9
              
               10
                
                 11
'''
tree = Node(9)
tree.right = Node(10)
tree.right = Node(11)
min_in_bst.ans = 0
min_in_bst(tree)
print(min_in_bst.ans)