l=[]
for i in range(int(input("how many numbers: "))):
    l.append(input())
t = 1
while min(l) != l[0]:
    print(t)
    if t == 0:
        t+=1
    elif l[t] < l[t-1]:
        l[t-1], l[t] = l[t], l[t-1]
        t-=1
    else:
        t+=1


print(l)

