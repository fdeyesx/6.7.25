def r(n):
    if n%2 != 0:
        return n-1
    return n

def f(s1,s2,m):
    if s1+s2 <= 212: return m%2 == 0
    if m == 0: return 0
    h = [f(s1-2,s2,m-1),f(s1,s2-2,m-1),f(r(s1)//2,s2,m-1),f(s1,r(s2)//2,m-1)]
    return any(h) if m%2 == 0 else all(h)
# для 19 задачи вместо all пишется any
print('19:', max([s for s in range(103,1000) if not f(110,s,1) and f(110,s,2)]))
print('20:', [s for s in range(103,1000) if not f(110,s,1) and f(110,s,3)])
print('21:', [s for s in range(103,1000) if not f(110,s,2) and f(110,s,4)])
