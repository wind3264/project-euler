import math
n = 600851475143
ans = 1
arr = [n]
for i in range(2,int(math.sqrt(n) + 1)):
    if n % i == 0 :
        b = True
        for j in arr:
            if i % j == 0:
                b = False
        if b :
            ans = i
        arr.append(i)
print(ans)
# solved, answer: 6857
