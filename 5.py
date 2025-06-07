def f(n):
    s = ''
    while n!=0:
        s = str(n%3) + s
        n //= 3
    return s

def main(n):
    s = f(n)
    if n%5 == 0:
        s = s + s[-2:]
    else:
        s = s + f((n%5)*2)
    return int(s,3)

a = []
for i in range(1,1000):
    r = main(i)
    if r <= 514:
        a.append(r)
print(max(a))
