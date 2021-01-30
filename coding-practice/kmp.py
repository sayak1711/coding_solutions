# create the prefix table for the pattern
# d s g w a d s g z
# 0 0 0 0 0 1 2 3 0

def prefix_table(pattern):
    prefix_table = [0]
    l = len(pattern)
    first = 0
    for second in range(1, l):
        if pattern[first] == pattern[second]:
            #prefix_table.append(first+1)
            prefix_table.append(prefix_table[-1]+1)
            first += 1
        else:
            first = 0
            prefix_table.append(0)
    return prefix_table

#print(prefix_table('dsgwadsgz'))
#print(prefix_table('ababaca'))

def match_str(pattern, s, p_table):
    pi = 0
    si = 0
    while si < len(s):
        if s[si] == pattern[pi]:
            pi += 1
            si += 1
        else:
            if pi > 0:
                pi = p_table[pi-1]
            elif pi == 0:
                si += 1
        if pi == len(pattern):
            return True
    return False

s = 'THIS IS A TEST TEXT'
p = 'TEST'

pt = prefix_table(p)
print(match_str(p, s, pt))