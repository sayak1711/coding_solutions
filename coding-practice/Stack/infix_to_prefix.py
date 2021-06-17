operators = {'+', '-', '*', '/', '^'}
priority = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
open_brackets = {'(', '{', '['}
close_brackets = {'(': ')', '{': '}', '[': ']'}


def infix_to_prefix(infix_expression):
    '''
    reverse the expression
    l-r and r-l get reversed priorities, close and open brackets act opposite
    '''
    stack = []
    answer = ''

    for token in infix_expression[::-1]:
        if token in open_brackets:
            close_found = False
            while stack and not close_found:
                top = stack.pop()
                if top == close_brackets[token]:
                    close_found = True
                else:
                    answer += top
        elif token in close_brackets.values():
            stack.append(token)
        elif token in operators:
            while stack and (stack[-1] in operators) and ((priority[stack[-1]] > priority[token]) or (stack[-1] == token == '^')):  # ^ has right to left priority
                answer += stack.pop()
            stack.append(token)
        else:
            answer += token
        print(f'Stack {stack}')
    while stack:
        answer += stack.pop()
    return answer[::-1]

prefix = infix_to_prefix('K+L-M*N+(O^P)*W/U/V*T+Q^J^A')
print(prefix)
