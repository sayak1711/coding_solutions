# https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542
def maxgain(n, weights, values, capacity):     
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for ind in range(n-1, -1, -1):
        for remaining_weight in range(capacity, -1, -1):
            if weights[ind] > remaining_weight:
                dp[ind][remaining_weight] = dp[ind+1][remaining_weight]
                continue
            dp[ind][remaining_weight] = max(dp[ind+1][remaining_weight], values[ind]+dp[ind+1][remaining_weight-weights[ind]])
    return dp[0][capacity]


t = int(input())

for _ in range(t):
    n = int(input())
    weights = input().split()
    weights = [int(w) for w in weights]
    values = input().split()
    values = [int(v) for v in values]
    capacity = int(input())
    print(maxgain(n, weights, values, capacity))