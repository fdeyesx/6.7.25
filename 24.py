#ABCDEF
#GHIJKLMNOPQRSTUVWXYZ
from os.path import split

s = open('24 (3).txt').readline()
a = []
p = ''
for i in s:
    p += i
    if p[0] == '0' or p[0] in 'GHIJKLMNOPQRSTUVWXYZ':
        p = ''
    if len(p) > 2:
        if p[-1] in 'GHIJKLMNOPQRSTUVWXYZ':
            if p .count('B') == 10:
                a.append(p[:-1])
                p = ''
b = []
k = 0
for i in a:
    r = int(i, 16)
    b.append(f'{k}.{r}')
    k += 1

c = []
for i in b:
    r = i.split('.')
    c.append(r[1])
o = max(c)
n = 0
for i in b:
    r = i.split('.')
    if o == r[1]:
        print(i)
        n = r[0]
print(a[n],len(a[n]))
