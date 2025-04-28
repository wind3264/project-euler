import math
def is_prime(n):
    if n < 2 :
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
p = 0
l = []
for a in range(-999, 1000) :
    for b in range(3, 1000, 2):
        n = 0
        i = 0
        while is_prime(n**2 + (a * n) + b):
            n += 1
            i += 1
        if i > p :
            p = i
            ans = a*b
            print(a,b,p)
for n in range(71) :
    print(n**2 + (-61 * n) + 971, is_prime(n**2 + (-61 * n) + 971))
print(ans)
# solved, answer: -59231