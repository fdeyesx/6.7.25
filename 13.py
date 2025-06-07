from ipaddress import *
k=0
n = ip_network('172.16.192.0/255.255.192.0')
for i in n:
    f = f'{i:b}'
    if int(str(f)[-8:],2)%2 == 0:
        if f.count('1')%3 == 0:
            k+=1
print(k)
