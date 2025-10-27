t = 4
l =[]
for i in range(t):
    l.append(int(input()))

newl = []

for j in range(t-2):
    smallest = l[0]
    for i in range(t-1-j):
        if l[i+1]<smallest:
            smallest = l[i+1]
    newl.append(smallest)
    l.remove(smallest)


smallest = l[0]
if l[1]<smallest:
    smallest = l[1]
newl.append(smallest)
l.remove(smallest)
#1 thing left in l


newl.append(l[0])
l.remove(l[0])
#0 things left

print(newl)