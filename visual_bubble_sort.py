import matplotlib.pyplot as plt
import numpy as np
import random
import string

n=5
l = []
for i in range(n):
    l.append(random.randint(1, 1000))

x = np.array(list(string.ascii_uppercase[:n]))
y = np.array(l)

plt.bar(x,y)
plt.show()



for j in range(n-1): #loop for 9 times
    for i in range(n-1): #loop for 9 times
        if l[i]>l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            y = np.array(l)
            plt.bar(x, y)
            plt.show()
