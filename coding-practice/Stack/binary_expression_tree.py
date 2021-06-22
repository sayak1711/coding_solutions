# for each leaf make the least precedence operator the root of the subtree

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

def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.val)

def preorder_recursive(root):
    if root:
        print(root.val)
        preorder_recursive(root.left)
        preorder_recursive(root.right)

priority = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

def infix_to_binary_expression(expression):
    if len(expression) == 1:
        return Node(expression[0])
    elif len(expression) == 0:
        return
    min_priority = 4
    min_priority_index = -1
    for i, token in enumerate(expression):
        if token in priority and priority[token] <= min_priority:
            min_priority = priority[token]
            min_priority_index = i
    root = Node(expression[min_priority_index])
    if min_priority_index > 0:
        root.left = infix_to_binary_expression(expression[:min_priority_index])
    if min_priority_index < len(expression)-1:
        root.right = infix_to_binary_expression(expression[min_priority_index+1:])
    return root

ans = infix_to_binary_expression(['a', '*', 'b', '/', 'c', '+', 'e', '/', 'f', '*', 'g', '+', 'k', '-', 'x', '*', 'y'])
print('Inorder(also infix) of the tree is ')
inorder_recu(ans)
print('Postorder(also postfix) of the binary tree is ')
postorder_recursive(ans)
print('Preorder(also prefix) of the binary tree is ')
preorder_recursive(ans)


def postfix_to_binary_expression(expression):
    stack = []
    for token in expression:
        if token in priority:
            right = stack.pop()
            left = stack.pop()
            head = Node(token)
            head.left = left
            head.right = right
            stack.append(head)
        else:
            stack.append(Node(token))
    assert len(stack) == 1
    return stack[0]

ans = postfix_to_binary_expression(['a', 'b', '*', 'c', '/', 'e', 'f', '/', 'g', '*', '+', 'k', '+', 'x', 'y', '*', '-'])
print('Inorder(also infix) of the tree is ')
inorder_recu(ans)
print('Postorder(also postfix) of the binary tree is ')
postorder_recursive(ans)
print('Preorder(also prefix) of the binary tree is ')
preorder_recursive(ans)
