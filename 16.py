from sys import setrecursionlimit
setrecursionlimit(100000)

def f(n):
    if n < 180: return 24
    return f(n-12) + 6

print(f(80000))
