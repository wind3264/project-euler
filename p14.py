def collatz(n, i):
    if n == 1:
        return i
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1
    return collatz(n, i + 1)

ans = 0
maxc = collatz(1,1)
for i in range(1,1000000):
    if collatz(i,1) > maxc :
        maxc = collatz(i,1)
        ans = i
print(ans)
# solved, answer: 837799