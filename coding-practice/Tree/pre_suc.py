class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def successor(root):
    root = root.right
    while root.left:
        root = root.left
    return root

def predecessor(root):
    root = root.left
    while root.right:
        root = root.right
    return root
