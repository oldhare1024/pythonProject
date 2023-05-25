n = int(input())
num = list(map(int, input().split()))
all1 = 0
num = sorted(num)
if n > 2:
    if n % 2 == 0:
        for i in num[1::2]:
            all1 += i
    else:
        for i in num[0::2]:
            all1 += i
elif n == 2:
    all1 = num[1]
else:
    all1 = num[0]
print(all1)
