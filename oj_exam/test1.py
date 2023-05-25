n = int(input())
num = [i for i in range(1, n + 1)]
while len(num) != 1:
    del num[::2]
    num = sorted(num)
print(num[0])
