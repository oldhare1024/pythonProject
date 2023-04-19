T = int(input())
p = []
n = []
m = []
a = []
for i in range(T):
    x, y, z = map(int, input().split())
    n.append(x)
    m.append(y)
    a.append(z)
for i in range(T):
    if a[i] >= n[i] and a[i] >= m[i]:
        p.append(1)
    else:
        if n[i] % a[i] == 0:
            X = n[i] // a[i]
        else:
            X = n[i] // a[i] + 1
        if m[i] % a[i] == 0:
            Y = m[i] / a[i]
        else:
            Y = m[i] // a[i] + 1
        p.append(int(X * Y))
for i in range(T):
    print(p[i])
