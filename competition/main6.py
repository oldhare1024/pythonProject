n = int(input())
num = input().split()
All = [0] * n
zuobiao = 0
for i in range(len(num)):
    num[i] = int(num[i])
MAX = min(num[0:2:]) + min(num[2:n:])
All[0] = MAX
zuobiao = 1
for i in range(3, n):
    All[i] = min(num[0:i:]) + min(num[i:n:])
    if MAX < All[i]:
        MAX = All[i]
        zuobiao = i
print(zuobiao + 1)
