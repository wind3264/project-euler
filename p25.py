n = 1
t = 1
i = 2
while len(str(n)) < 1000:
    temp = n
    n += t
    t = temp
    i += 1
print(i)
# solved, answer: 4782