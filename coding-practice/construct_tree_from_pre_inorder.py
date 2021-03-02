from collections import defaultdict

def search(arr, num):
    for i, n in enumerate(arr):
        if n == num:
            return i

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_tree_levelorder(head):
    level_order = defaultdict(list)
    q = [(head, 0)]
    while q:
        cur_node, level = q.pop(0)
        level_order[level].append(cur_node.val)
        if cur_node.left:
            q.append((cur_node.left, level+1))
        if cur_node.right:
            q.append((cur_node.right, level+1))
    for level, values in level_order.items():
        print(f'Level {level} Values {values}')


def construct_tree(preorder, inorder, in_start, in_end):
    if in_start > in_end:
        return
    root = Node(preorder[construct_tree.pre_index])
    construct_tree.pre_index += 1
    if in_start == in_end:
        return root
    pos = search(inorder, root.val)
    
    root.left = construct_tree(preorder, inorder, in_start, pos-1)
    root.right = construct_tree(preorder, inorder, pos+1, in_end)

    return root
construct_tree.pre_index = 0
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
inorder = ['D', 'B', 'E', 'A', 'F', 'C']
ans = construct_tree(preorder, inorder, 0, len(preorder)-1)

print_tree_levelorder(ans)

#https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/