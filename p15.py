def f(n):
    if n == 0:
        return 1
    else: 
        return n * f(n-1)
n = f(20)
print(f(40)//(n*n))
# solved, answer: 137846528820