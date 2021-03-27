class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# since it is BST they are in sorted order
# they either lie on same side or on opposite side
# if they are on opposite side of root then root is the LCA
def lca(root, node1, node2):
    while (root.val-node1.val)*(root.val-node2.val) > 0: # then it means they are on same side
        if node1.val < root.val:  # then they are both on left side
            root = root.left
        else:                     # both are on right side
            root = root.right
    return root   # now we can say that they are on opposite sides of current root

'''
              5
               
         4       6
                 
       3           7
                    
                     8
'''
tree = Node(5)
tree.left = Node(4)
tree.left.left = Node(3)
tree.right = Node(6)
tree.right.right = Node(7)
tree.right.right.right = Node(8)
ans = lca(tree, Node(3), Node(8))
print(f'LCA is {ans.val}')

'''
        6
    2        8
  0   4    7   9
    3   5
'''
tree = Node(6)
tree.left = Node(2)
tree.right = Node(8)
tree.left.left = Node(0)
tree.left.right = Node(4)
tree.right.left = Node(7)
tree.right.right = Node(9)
tree.left.right.left = Node(3)
tree.left.right.right = Node(5)
ans = lca(tree, Node(8), Node(9))
print(f'LCA is {ans.val}')