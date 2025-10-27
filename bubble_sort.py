import random

for i in range(5):
    print()

n=10
l = []
for i in range(n):
    l.append(random.randint(1, 1000))
print(l)

for i in range(5):
    print()

for j in range(n-1): #loop for 9 times
    for i in range(n-1): #loop for 9 times
        if l[i]>l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]

print(l)

for i in range(5):
    print()
