for a in range(1,999):
    for b in range(1,999-a+1):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2 :
            print(a*b*c)

# solved, answer: 31875000
