operators = {'+', '-', '*', '/', '^'}
priority = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
close_brackets = {')', '}', ']'}
open_brackets = {')': '(', '}': '{', ']': '['}


def infix_to_postfix(infix_expression):
    '''
    scan items left to right in expression
    a) if it is a operator, push it to stack
    b) if it's a number, append it to answer
    for a) if stack is non-empty and precedence of operator in top of stack is
    more than that of current operator scanned then pop from stack that operator
    repeat this process until this is not true or stack is empty
    push the current operator into stack
    '''
    stack = []
    answer = ''

    for token in infix_expression:
        if token in close_brackets:
            #print(stack)
            open_found = False
            while stack and not open_found:
                top = stack.pop()
                if top == open_brackets[token]:
                    open_found = True
                else:
                    answer += top
        elif token in open_brackets.values():
            stack.append(token)
        elif token in operators:
            #print(f'hey {stack}')
            while stack and (stack[-1] in operators) and (not (stack[-1] == token == '^')) and (priority[stack[-1]] >= priority[token]):  # ^ has right to left priority
                answer += stack.pop()
            stack.append(token)
        else:
            answer += token
        print(f'Stack {stack}')
    while stack:
        answer += stack.pop()
    return answer

postfix = infix_to_postfix('K+L-M*N+(O^P)*W/U/V*T+Q^J^A')
print(postfix)
