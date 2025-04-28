from functools import cache
"""
k = 6

coins = [1, 2, 5, 10, 20, 50, 100, 200]
l = []
lst = []
def helper(m, l) :
    if m == 0:
        l.sort()
        if l not in lst:
            lst.append(l)
    else :
        for c in coins:
            if m >= c :
                l.append(c)
                helper(m - c, l[:])
                l.pop()
helper(k, l)
print(lst)
print(len(lst))

"""
coins = [1, 2, 5, 10, 20, 50, 100, 200]
@cache
def f(n, i):
    if n == 0:
        return 1
    m = 0
    for j, c in enumerate(coins[i:]):
        if n >= c :
            m += f(n-c, i+j)
    return m
print(f(200,0))

# the d in adam stands for dp
def g(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for c in coins:
        for i in range(c, n+1):
            dp[i] += dp[i-c]
    return dp[n]
print(g(200))