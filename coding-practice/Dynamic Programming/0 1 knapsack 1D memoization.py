# https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542
def maxgain(n, weights, values, capacity):
    dp = [0 for _ in range(capacity+1)]
    for ind in range(n-1, -1, -1):
        for remaining_weight in range(capacity, -1, -1):
            if weights[ind] > remaining_weight:
                continue
            dp[remaining_weight] = max(dp[remaining_weight], values[ind]+dp[remaining_weight-weights[ind]])
    return dp[capacity]


t = int(input())

for _ in range(t):
    n = int(input())
    weights = input().split()
    weights = [int(w) for w in weights]
    values = input().split()
    values = [int(v) for v in values]
    capacity = int(input())
    print(maxgain(n, weights, values, capacity))