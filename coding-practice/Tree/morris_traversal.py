# node's datastructure
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

'''
     1
  2     3
4   5
      6
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(6)

def inorder_m(root):
    inorder_traversal = []
    
    cur = root
    while cur:
        if cur.left:
            # connect rightmost of left subtree to cur, so that we can return to cur, once done with left subtree
            prev = cur.left
            while prev.right and prev.right is not cur:
                prev = prev.right
            
            if not prev.right: # we are visiting this for first time
                prev.right = cur  # link for traceback later
                cur = cur.left  # now deal with left subtree in similar fashion
            else:
                inorder_traversal.append(cur.val)  # we are done with left subtree of root
                prev.right = None  # break link
                cur = cur.right  # now deal with right subtree in similar fashion
        else:
            inorder_traversal.append(cur.val)
            cur = cur.right 
    return inorder_traversal


ans = inorder_m(root)
print(f'Inorder: {ans}')


def preorder_m(root):
    preorder_traversal = []
    
    cur = root
    while cur:
        if cur.left:
            prev = cur.left
            while prev.right and prev.right is not cur:
                prev = prev.right
            
            if not prev.right:
                prev.right = cur
                preorder_traversal.append(cur.val)
                cur = cur.left
            else:
                prev.right = None
                cur = cur.right
        else:
            preorder_traversal.append(cur.val)
            cur = cur.right 
    return preorder_traversal

ans = preorder_m(root)
print(f'Preorder {ans}')