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


def construct_tree(levelorder, inorder, instart, inend):
    if instart > inend:
        return
    least_index = 999  # least index in level order
    least_index_io = 999
    for i in range(instart, inend+1):
        if levelorder_pos[inorder[i]] < least_index:
            least_index = levelorder_pos[inorder[i]]
            least_index_io = i
    root = Node(levelorder[least_index])
    if instart == inend:
        return root
    root.left = construct_tree(levelorder, inorder, instart, least_index_io-1)
    root.right = construct_tree(levelorder, inorder, least_index_io+1, inend)
    return root

inorder = [4, 8, 10, 12, 14, 20, 22]
levelorder = [20, 8, 22, 4, 12, 10, 14]
levelorder_pos = dict(zip(levelorder, range(0, len(levelorder))))
ans = construct_tree(levelorder, inorder, 0, len(inorder)-1)

print_tree_levelorder(ans)
'''
in   = [4, 8, 10, 12, 14, 20, 22]
level = [20, 8, 22, 4, 12, 10, 14]
        20
    8        22
 4     12
     10   14   
'''