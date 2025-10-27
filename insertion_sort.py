import random

for i in range(5):
    print()

n=100
l = []
for i in range(n):
    l.append(random.randint(1, 1000))
print(l)

for i in range(5):
    print()

t = 1

for j in range(n-1):
    for i in range(j+1):
        if l[t] < l[t-1]:
            l[t-1], l[t] = l[t], l[t-1]

        t-=1
    t+=j+2

print(l)

for i in range(5):
    print()