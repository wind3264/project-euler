arr = []
for _ in range(20):
    arr.append(list(map(int, input().split())))
ans = -1
p = -1
for i in range(20):
    for j in range(17):
        p = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]
        ans = max(ans, p)
for i in range(17):
    for j in range(20):
        p = arr[i][j] * arr[i+1][j] * arr[i+2][j] * arr[i+3][j]
        ans = max(ans, p)
for i in range(17):
    for j in range(17):
        p = arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3]
        ans = max(ans, p)
for i in range(19, 2, -1):
    for j in range(17):
        p = arr[i][j] * arr[i-1][j+1] * arr[i-2][j+2] * arr[i-3][j+3]
        ans = max(ans, p)
print(ans)
# solved, answer: 70600674