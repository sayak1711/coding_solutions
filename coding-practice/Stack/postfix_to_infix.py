operators = {'+', '-', '*', '/', '^'}

def post_to_in(expression):
    '''
    scan left to right
    if its a number push to stack
    if its a operator pop 2 numbers
    top is op2, next is op1
    push back op1 operator op2
    '''
    stack = []
    for token in expression.split():
        if token in operators:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f'({op1} {token} {op2})')
        else:
            stack.append(token)

    return stack.pop()

ans = post_to_in("a b + e f / *")
print(ans)
