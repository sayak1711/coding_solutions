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

# go level by level by using a queue. if you find the left or right of a node empty
# put new val as node there. if tree root itself not present(empty tree) put it as root
def insert_node_bt_levelorder(val, tree_root):
    q = []
    if not tree_root:
        node = Node(val)
        return node
    q.append(tree_root)
    while q:
        cur_node = q.pop(0)
        if cur_node.left is None:
            cur_node.left = Node(val)
            return tree_root
        else:
            q.append(cur_node.left)
        if cur_node.right is None:
            cur_node.right = Node(val)
            return tree_root
        else:
            q.append(cur_node.right)
print('Our tree before:')
print_tree_levelorder(root)
insert_node_bt_levelorder(12, root)
print('Our tree after:')
print_tree_levelorder(root)