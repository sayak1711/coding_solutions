# delete a node from binary tree and replace it with deepest and rightmost node(last node)

from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

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

print('Our tree before:')
print_tree_levelorder(root)

# find the last node(bottommost rightmost) and replace node to be deleted with that. delete last node
def delete_node(val, root):
    q = [root]
    lastnode = None
    node_to_delete = None
    while q:
        cur_node = q.pop(0)
        lastnode = cur_node
        if cur_node.val == val:
            node_to_delete = cur_node
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

    if node_to_delete is None:
        return
    node_to_delete.val = lastnode.val
    q = [root]
    while q:
        cur_node = q.pop(0)
        if cur_node is lastnode:
            cur_node = None
            break
        if cur_node.left is lastnode:
            cur_node.left = None
            break
        else:
            q.append(cur_node.left)
        if cur_node.right is lastnode:
            cur_node.right = None
            break
        else:
            q.append(cur_node.right)

delete_node(11, root)
print('Our tree after deleting 11:')
print_tree_levelorder(root)

