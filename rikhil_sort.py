import random

for i in range(5):
    print()

n=10
l = []
for i in range(n):
    l.append(random.randint(1, 1000))

for i in range(5):
    print()

c = 0
n = c+1
p = int(len(l)) - 1

for j in range(int(len(l)) - 1):
    for i in range(p):
        if l[c] > l[n]:
            l[c], l[n] = l[n], l[c]
        n+=1
    p-=1    
    c+=1
    n=c+1







print(l)