n = []
a, b, c = map(int, input().split())
n.append(a)
n.append(b)
n.append(c)
n = sorted(n)
print('->'.join(str(i) for i in n))
