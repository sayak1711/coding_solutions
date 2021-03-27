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

def delete_node_from_bst(node, num):
    if not node:
        return
    if node.val == num:
        if not node.right:    # the case when node is leaf or only has only left child
            temp = node.left  # either None or node's predecessor
            del node          # the duplicate number will be dealt with later in line 22
            return temp
        else:
            temp = node.right
            while temp.left: # we find the minimum in right subtree of node
                temp = temp.left
            # the found value is node's sucessor
            node.val, temp.val = temp.val, node.val # swap their values
            # now that sucessor holds node's original value and will be dealt with later in line 23
    node.left = delete_node_from_bst(node.left, num)
    node.right = delete_node_from_bst(node.right, num)
    return node

'''
    5
  3   6
2  4   7
'''
tree = Node(5)
tree.left = Node(3)
tree.right = Node(6)
tree.left.left = Node(2)
tree.left.right = Node(4)
tree.right.right = Node(7)
print('Tree before')
inorder_recu(tree)
tree = delete_node_from_bst(tree, 3)
print('Tree after')
inorder_recu(tree)