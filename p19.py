week = ["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
curr = [1, 1, 1900] # month, day, year
i = 0

c = 0
while curr[2] < 2001:
    if week[i % 7] == "sun" and curr[2] != 1900 and curr[1] == 1:
        c += 1
        print(curr)

    i += 1
    curr[1] += 1
    if curr[2] == 1900 and curr[0] == 2 and curr[1] == 29:
        curr[1] = 1
        curr[0] += 1
    elif curr[0] == 2 and curr[1] == 30 and curr[2] % 4 == 0:
        curr[1] = 1
        curr[0] += 1
    elif curr[0] == 2 and curr[1] == 29 and curr[2] % 4 != 0:
        curr[1] = 1
        curr[0] += 1
    elif curr[0] in [4, 6, 9, 11] and curr[1] == 31:
        curr[1] = 1
        curr[0] += 1
    elif curr[0] in [1, 3, 5, 7, 8, 10, 12] and curr[1] == 32:
        curr[1] = 1
        curr[0] += 1
    if curr[0] == 13:
        curr[0] = 1
        curr[2] += 1
print(c)
# solved, answer: 171