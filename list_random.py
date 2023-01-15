import random as r

a = [0 for i in range(20)]
b = [0 for j in range(20)]
c = 0
for i in range(20):
    a[i] = r.randint(0, 9)
    b[a[i]] += 1
print(a)
a.sort()
print(a)
for i in range(10):
    print(f"{i}出现了{b[i]}次")
