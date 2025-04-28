import math
def d(n):
    d = 0
    for i in range(1, n):
        if n % i == 0 :
            d += i
    return d
"""
max_d = 25320
ans = 0
l = [[] for _ in range(25321)]
for j in range(1, 10000):
    l[d(j)].append(j)
for list in l:
    ans += sum(list)
print(l)
print(ans)
"""
l = []
for i in range(1, 10000):
    j = d(i)
    if d(j) == i and i != j:
        if i not in l:
            l.append(i)
        if j not in l:
            l.append(j)
print(l)
print(sum(l))
# solved, answer: 31626