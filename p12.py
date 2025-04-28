import math
def count_factors(n):
    c = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0 :
            c += 1
    return c * 2

n = 1
x = 0
while x <= 500:
    n += 1
    x = count_factors((n * (n+1)) // 2)
print((n * (n+1)) // 2)
# solved, answer: 76576500
