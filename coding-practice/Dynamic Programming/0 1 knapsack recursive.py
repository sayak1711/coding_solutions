# https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542
from functools import lru_cache

def maxgain(n, weights, values, capacity):
    @lru_cache(None)
    def get_maxgain(ind, remaining_weight):
        if ind == n or remaining_weight == 0:
            return 0
        if weights[ind] > remaining_weight:
            return get_maxgain(ind+1, remaining_weight)
        ignore = get_maxgain(ind+1, remaining_weight)
        consider = values[ind]+get_maxgain(ind+1, remaining_weight-weights[ind])
        return max(ignore, consider)
        
    return get_maxgain(0, capacity)

t = int(input())

for _ in range(t):
    n = int(input())
    weights = input().split()
    weights = [int(w) for w in weights]
    values = input().split()
    values = [int(v) for v in values]
    capacity = int(input())
    print(maxgain(n, weights, values, capacity))

