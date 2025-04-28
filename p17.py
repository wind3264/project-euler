def count(n):
    c = 0
    if n % 10 == 1 and n % 100 != 11:
        c += 3
    elif n % 10 == 2 and n % 100 != 12:
        c += 3
    elif n % 10 == 3 and n % 100 != 13:
        c += 5
    elif n % 10 == 4 and n % 100 != 14:
        c += 4
    elif n % 10 == 5 and n % 100 != 15:
        c += 4
    elif n % 10 == 6 and n % 100 != 16:
        c += 3
    elif n % 10 == 7 and n % 100 != 17:
        c += 5
    elif n % 10 == 8 and n % 100 != 18:
        c += 5
    elif n % 10 == 9 and n % 100 != 19:
        c += 4
    if n % 100 == 10:
        c += 3
    elif n % 100 == 11:
        c += 6
    elif n % 100 == 12:
        c += 6
    elif n % 100 == 13:
        c += 8
    elif n % 100 == 14:
        c += 8
    elif n % 100 == 15:
        c += 7
    elif n % 100 == 16:
        c += 7
    elif n % 100 == 17:
        c += 9
    elif n % 100 == 18:
        c += 8
    elif n % 100 == 19:
        c += 8
    elif (n % 100) // 10 == 2:
        c += 6
    elif (n % 100) // 10 == 3:
        c += 6
    elif (n % 100) // 10 == 4:
        c += 5
    elif (n % 100) // 10 == 5:
        c += 5
    elif (n % 100) // 10 == 6:
        c += 5
    elif (n % 100) // 10 == 7:
        c += 7
    elif (n % 100) // 10 == 8:
        c += 6
    elif (n % 100) // 10 == 9:
        c += 6
    if n >= 100 and n % 100 != 0:
        c += 3
    if n >= 100:
        c += 7
    if (n % 1000) // 100 == 1:
        c += 3
    if (n % 1000) // 100 == 2:
        c += 3
    if (n % 1000) // 100 == 3:
        c += 5
    if (n % 1000) // 100 == 4:
        c += 4
    if (n % 1000) // 100 == 5:
        c += 4
    if (n % 1000) // 100 == 6:
        c += 3
    if (n % 1000) // 100 == 7:
        c += 5
    if (n % 1000) // 100 == 8:
        c += 5
    if (n % 1000) // 100 == 9:
        c += 4

    return c
s = 0
for i in range(1000):
    s += count(i)
print(s+11)
# solved, answer: 21124