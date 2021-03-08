class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_node_vals(node):
    if not node:
        return 0
    lsum=rsum=0
    if node.left:
        lsum = sum_node_vals(node.left)
    if node.right:
        rsum = sum_node_vals(node.right)
    return node.val+lsum+rsum


def tilt_of_tree(node):
    if not node:
        return 0
    tilt = abs(sum_node_vals(node.left)-sum_node_vals(node.right))
    ltiltsum = tilt_of_tree(node.left)
    rtiltsum = tilt_of_tree(node.right)
    return tilt+ltiltsum+rtiltsum
    


'''
      10
       
    20     30
          
  40  60
'''
'''
tree = Node(10)
tree.left = Node(20)
tree.right = Node(30)
tree.left.left = Node(40)
tree.left.right = Node(60)

print(tilt_of_tree(tree))
'''
'''
    4
    
  2   9
     
3   5   7
'''
tree = Node(4)
tree.left = Node(2)
tree.right = Node(9)
tree.left.left = Node(3)
tree.left.right = Node(5)
tree.right.right = Node(7)
print(tilt_of_tree(tree))