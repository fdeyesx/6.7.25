def pr(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
k = 0
for x in range(987_654-1, 0,-1):
    d = set()
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            d.add(i)
            d.add(x//i)
    d = sorted(list(d))
    if len(d) > 0:
        a = []
        for i in d:
            if pr(i) == True:
                if 100 <= i:
                    if i%100 == 17:
                        a.append(i)
        if len(a) != 0:
            print(x, min(a))
            k+=1
            if k == 5:
                break
