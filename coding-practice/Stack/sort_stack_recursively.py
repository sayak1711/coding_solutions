'''
https://www.geeksforgeeks.org/sort-a-stack-using-recursion/
Given a stack, sort it using recursion. Use of any loop constructs like while, for..etc is not allowed.
We can only use the following ADT functions on Stack S:

is_empty(S)  : Tests whether stack is empty or not.
push(S)         : Adds new element to the stack.
pop(S)         : Removes top element from the stack.
top(S)         : Returns value of the top element. Note that this
               function does not remove element from the stack.
'''


def sortedInsert(S, n):
    if not S or S[-1] < n:
        S.append(n)
    else:
        temp = S.pop()
        sortedInsert(S, n)
        S.append(temp)


def sortStack(S):
    if S:
        temp = S.pop()
        sortStack(S)
        sortedInsert(S, temp)

S = [-3, 14, 18, -5, 30]
print(f'before {S}')
sortStack(S)
print(f'after {S}')
