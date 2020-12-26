def pprint_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

def generateMatrix(A):
    B = []
    for i in range(A):
        C = []
        for j in range(A):
            C.append(0)
        B.append(C)
    direction = 0
    l = 0
    r = A - 1
    t = 0
    b = A - 1
    num = 1
    while num <= pow(A,2):
        print(f'l {l} r {r} t {t} b {b} dir {direction} num {num}')
        if direction == 0:
            for i in range(l, r + 1):
                B[t][i] = num
                num += 1
            t += 1
        elif direction == 1:
            for i in range(t, b + 1):
                B[i][r] = num
                num += 1
            r -= 1
        elif direction == 2:
            for i in range(r, l-1, -1):
                B[b][i] = num
                num += 1
            b -= 1
        elif direction == 3:
            for i in range(b, t - 1, -1):
                B[i][l] = num
                num += 1
            l += 1
        direction = (direction + 1) % 4
        print(pprint_matrix(B))
    return B


ans = generateMatrix(6)
print()
print()
print(pprint_matrix(ans))