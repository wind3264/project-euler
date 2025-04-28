ans = 0
for i in range(2, 10000000):
    s = 0
    for c in str(i):
        s += int(c)**5
    if i == s:
        ans += i
print(ans)
# solved, answer: 443839