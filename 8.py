from itertools import *
k=0
for i in product('вдёжиноря', repeat = 5):
    s = ''.join(i)
    k+=1
    if s[0] == s[-1]:
        if s.count('р') > 1:
            if k%2 == 0:
                print(k, s, sep='. ')
