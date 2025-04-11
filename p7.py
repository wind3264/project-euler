import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
i = 0
ans = -1
n = 2
while i < 10001 :
    if is_prime(n):
        i += 1
        ans = n
    n += 1
print(ans)