class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_leaf(node):
    if node and not node.left and not node.right: # it is a leaf
        return node.val
    lsum = sum_leaf(node.left)
    rsum = sum_leaf(node.right)
    return lsum+rsum


'''
      10
       
    20     30
          
  40  60
'''
tree = Node(10)
tree.left = Node(20)
tree.right = Node(30)
tree.left.left = Node(40)
tree.left.right = Node(60)
print(sum_leaf(tree))