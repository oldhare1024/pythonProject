def buddlesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def printarr(arr):
    for i in range(len(arr) - 1):
        print(arr[i], end=" ")  # 改名字
    print()


from random import *

a = []
n = 10
for i in range(n):
    a.append(randint(10, 99))
print("原列表")
printarr(a)
buddlesort(a)
print("排序后列表")
printarr(a)
y = int(input("Please input a number:"))
mid = False
j = 0
for j in range(n):
    if y < a[j]:
        mid = True
        break
if mid:
    a.append(0)
    for k in range(n, j, -1):
        a[k] = a[k - 1]
    a[j] = y
else:
    a.append(y)
# 加缩进
print("插入数值后的列表")
printarr(a)
