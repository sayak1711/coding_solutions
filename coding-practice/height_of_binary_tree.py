class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# longest path from root to leaf should be the height

def height_of_tree(tree):
    if not tree:
        return 0
    height_left = height_of_tree(tree.left)
    height_right = height_of_tree(tree.right)
    return 1+max(height_left, height_right)

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
print(height_of_tree(tree))

'''
 2
    1 
  3
'''
tree = Node(2)
tree.right = Node(1)
tree.right.left = Node(3)
print(height_of_tree(tree))

'''
  1
2   3
'''
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
print(height_of_tree(tree))