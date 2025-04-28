import math
def is_prime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
s = 0
n = 2
while n < 2e6:
    if is_prime(n) :
        s += n
    n += 1
print(s)
# solved, answer: 142913828922