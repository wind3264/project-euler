l = []
for _ in range(15):
    l.append(list(map(int, input().split())))

def f(i,j):
    if i == 14:
        return l[i][j]
    return max(l[i][j] + f(i+1,j), l[i][j] + f(i+1, j+1))

print(f(0,0))
# solved, answer: 1074