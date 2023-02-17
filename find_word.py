a = input().strip('.')
b = input()
c = a.split()
if b in c:
    print(c.index(b)+1)
else:
    print(len(a) - len(c))
