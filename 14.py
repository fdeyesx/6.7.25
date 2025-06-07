def f(n):
    s = ''
    a1 = ['a','b','c','d','e','f','g','h','i','j']
    a2 = ['k','l','m','n','o','p','q']
    while n!=0:
        r = n%27
        if r < 10:
            s = str(r) + s
        else:
            if 10 <= r <= 19:
                s = a1[r%10] + s
            else:
                s = a2[r%20] + s
        n //= 27
    return s

a1 = ['a','b','c','d','e','f','g','h','i','j']
a2 = ['k','l','m','n','o','p','q']
s1 = 4*729**2025 + 2*243**1413 - 5*81**169 - 3*9**107 + 7019
s0 = f(s1)
s0 = str(s0)
k = 0
for i in s0:
    r = 0
    if i in a1:
        for j in range(0, len(a1)):
            if str(i) == a1[j]:
                r = 10 + j
    elif i in a2:
        for j in range(0, len(a2)):
            if str(i) == a2[j]:
                r = 20 + j
    else: r = i
    if int(r)%3 == 0:
        k+=1
print(k)
