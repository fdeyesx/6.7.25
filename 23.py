def f(n,e):
    if n > e: return 0
    if n == e: return 1
    if e == 24:
        if n == 22: return 0
    if n == 22: return f(n+4,e)+f(n*2,e)
    return f(n+2,e)+f(n+4,e)+f(n*2,e)

print(f(12,22)*f(22,38))
print(f(12,24)*f(24,38))

print(f(12,24)*f(24,38)+f(12,22)*f(22,38))

