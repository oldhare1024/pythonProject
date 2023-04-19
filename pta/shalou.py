s = []
c1 = []
n = 0
c = 0
j = 0
e = 0
d = 0
x = y = x1 = y1 = 0
while c <= 1000:
    c1.append(2 * n + 1)
    c = (n + 1) ** 2
    s.append(c)
    n += 1
s.remove(1024)
b = [(i * 2 - 1) for i in s]
i, f = input().split()
i = int(i)
if i == 1:
    print(f, 0, sep='\n')
else:
    # 打印多出的符号
    for j in range(len(b)):
        if i <= b[j]:
            e = j - 1
            d = i - b[j - 1]
            # print(i - b[j-1])
            break
    # 打印上半部沙漏
    for x in range(e, 0, -1):
        for x1 in range(c1[e] // 2 - x):  # 打印空格
            print(' ', end='')
        for x1 in range(c1[x]):  # 打印字符
            print(f, end='')
        print('')
    # 打印下半部沙漏
    for x in range(e + 1):
        for x1 in range(c1[e] // 2 - x):  # 打印空格
            print(' ', end='')
        for x1 in range(c1[x]):  # 打印字符
            print(f, end='')
        print('')
    print(d)
