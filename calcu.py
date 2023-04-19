len = 1
for i in range(2, 27):
    len = len * 2 + 1
print(len)
a, b, c = map(int, input().split())
print(a, b, c, a + b + c, sep=',')
