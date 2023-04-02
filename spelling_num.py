import functools


def cmp1(x, y):
    if x + y > y + x:
        return 1
    elif x + y < y + x:
        return -1
    else:
        return 0


n = int(input())
s = input()
num = [i for i in s.split()]
num.sort(key=functools.cmp_to_key(cmp1))
num.reverse()
key = ""
for i in range(0, n):
    key += num[i]
print(key)
