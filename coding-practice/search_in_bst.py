# given a bst and an element to search find it

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search_in_bst(node, num): # find num in tree
    if not node:
        return
    if node.val == num:
        return node
    elif num < node.val:
        return search_in_bst(node.left, num)
    elif node.val < num:
        return search_in_bst(node.right, num)

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
ans = search_in_bst(tree, 3)
if ans:
    print(f'Found {ans.val}')
else:
    print('NOT FOUND')


'''
          9
              
               10
                
                 11
'''
'''
tree = Node(9)
tree.right = Node(10)
tree.right = Node(11)
ans = search_in_bst(tree, 11)
if ans:
    print(f'Found {ans.val}')
else:
    print('NOT FOUND')
'''