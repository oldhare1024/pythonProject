scores = [88, 89, 89, 56, 45, 4, 14, 4, 5, 4, 1, 55, 4, 5, 5, 5]
differ = 0
total = sum(scores)
avg = total / len(scores)  # 平均分
for i in scores:
    differ += ((i - avg) ** 2)
var = differ // len(scores)
print(f'平均分是：{int(avg)}\n方差是：{int(var)}')
