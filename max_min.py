s = [0 for i in range(5)]
for i in range(5):
    print(f"请输入第{i + 1}位学员的分数：")
    s[i] = int(input())
Max = s[0]
Min = s[0]
for i in range(1, 5):
    if Max < s[i]:
        Max = s[i]
    if Min > s[i]:
        Min = s[i]
print(f"最高分是：{Max}，最低分是：{Min}")
