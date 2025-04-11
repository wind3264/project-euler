t = 1
n = 2
s = 0
while n < 4000000 :
    if n % 2 == 0:
        s += n
    temp = n
    n += t
    t = temp
print(s)
# solved, answer: 4613732