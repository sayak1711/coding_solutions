operators = {'+', '-', '*', '/', '^'}

def pre_to_in(expression):
    '''
    scan right to left
    if its a number push to stack
    if its a operator pop 2 numbers
    top is op1, next is op2
    push back op1 operator op2
    '''
    stack = []
    for token in expression.split()[::-1]:
        if token in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f'({op1} {token} {op2})')
        else:
            stack.append(token)

    return stack.pop()

ans = pre_to_in("* + a b / e f")
print(ans)
