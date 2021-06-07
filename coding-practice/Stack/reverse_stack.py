def reverse_stack_iterative(stack):
    if not stack:
        return
    temp_stack = []
    while stack:
        temp_stack.append(stack.pop())
    return temp_stack

def reverse_stack_recursive(stack):
    if not stack:
        return
    popped = stack.pop(0)
    reverse_stack_recursive(stack)
    stack.append(popped)

st = [1, 2, 3, 4, 5, 6]
#ans = reverse_stack_iterative(st)
#print(ans)
reverse_stack_recursive(st)
print(st)
