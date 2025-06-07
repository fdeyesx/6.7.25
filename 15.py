for a in range(1,1000):
    d = set()
    for x in range(1,2000):
        f = ((35 <= x <= 65) <= ((x+1)%17 != 0)) or (x%a == 0)
        d.add(f)
    if False not in d:
        print(a)
