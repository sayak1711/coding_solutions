import math
operators = {'+', '-', '*', '/', '^'}

def operate(operand1, operator, operand2):
    if operator == '+':
        return operand1+operand2
    elif operator == "-":
        return operand1-operand2
    elif operator == "*":
        return operand1*operand2
    elif operator == "/":
        return operand1/operand2
    elif operator == "^":
        return math.pow(operand1, operand2)

def evaluate_prefix(prefix_expression):
    '''
    scan right to left
    if its a number push to stack
    if its a operator pop 2 numbers
    top is op1, next is op2
    push back op1 operator op2
    '''
    stack = []
    for token in prefix_expression.split()[::-1]:
        print('-'*30)
        print(stack)
        if token in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            print(f'op1 {op1}, token {token}, op2 {op2}')
            stack.append(operate(op1, token, op2))
        else:
            print(f'operand {token}')
            stack.append(int(token))
    assert len(stack) == 1
    return stack[0]

ans = evaluate_prefix("- + 2 * 3 4 / 16 ^ 2 3")
print(ans)
