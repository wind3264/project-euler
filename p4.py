def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

ans = -1
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j):
            ans = max(ans, i*j)

print(ans)
# solved, answer: 906609