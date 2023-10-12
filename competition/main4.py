n = int(input())
num = input().split()
all = 0
for i in range(len(num)):
    num[i] = int(num[i])
avg = sum(num) / len(num)  # x为平均数时，最小代价（方差）最小
# 平均数为小数时，正负小数转换整数需要分类讨论
if avg >= 0:
    avg = int(avg + 0.5)
else:
    avg = int(avg - 0.5)
# avg = int(avg)该方法不行
for i in range(len(num)):
    all += (num[i] - avg) ** 2
print(int(all))
